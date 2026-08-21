#!/usr/bin/env python3
"""
HTTP server with Range request support for PMTiles.

Usage:
    python serve.py                           # start on port 8000, open browser
    python serve.py --port 8001               # use a different port
    python serve.py --no-browser              # don't open the browser (server mode)
    python serve.py --host 0.0.0.0            # bind to all interfaces (LAN / direct VPS access)

Press Ctrl+C to stop the server (or close this window).
"""

import argparse
import http.server
import os
import signal
import socketserver
import sys
import threading
import webbrowser

parser = argparse.ArgumentParser(description="MapSplat local map server")
parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")
parser.add_argument("--host", default="127.0.0.1",
                    help="Address to bind to (default: 127.0.0.1; use 0.0.0.0 for LAN or direct VPS access)")
parser.add_argument("--no-browser", action="store_true", help="Do not open the browser on startup")
args = parser.parse_args()

PORT = args.port
HOST = args.host
server_running = True


class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """Multi-threaded HTTP server — handles concurrent requests."""
    daemon_threads = True


class RangeRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler with support for Range requests (required for PMTiles)."""

    server_version = "MapSplat"
    sys_version = ""

    def version_string(self):
        """Hide server implementation details."""
        return self.server_version

    def log_error(self, format, *args):
        """Suppress connection aborted errors (normal when browser cancels requests)."""
        if "ConnectionAbortedError" not in str(args):
            super().log_error(format, *args)

    def handle(self):
        """Handle requests, silently ignoring connection aborts."""
        try:
            super().handle()
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError):
            pass  # Browser cancelled the request, this is normal

    def send_head(self):
        """Handle HEAD requests and Range requests."""
        path = self.translate_path(self.path)

        if os.path.isdir(path):
            index = os.path.join(path, "index.html")
            if os.path.exists(index):
                path = index
            else:
                self.send_error(403, "Directory listing not allowed")
                return None

        if not os.path.exists(path):
            self.send_error(404, "File not found")
            return None

        file_size = os.path.getsize(path)

        # Check for Range header
        range_header = self.headers.get("Range")

        if range_header:
            # Parse Range header — supports single ranges only.
            # Examples: "bytes=0-1023", "bytes=1024-", "bytes=-500" (last 500 bytes)
            try:
                if not range_header.startswith("bytes="):
                    raise ValueError("unsupported range unit")
                range_spec = range_header[6:]  # strip "bytes="
                if "," in range_spec:
                    raise ValueError("multi-range not supported")
                start_str, end_str = range_spec.split("-", 1)
                # Suffix range: "bytes=-N" means the last N bytes
                if start_str == "":
                    suffix_len = int(end_str)
                    start = max(0, file_size - suffix_len)
                    end = file_size - 1
                else:
                    start = int(start_str)
                    end = int(end_str) if end_str else file_size - 1
                end = min(end, file_size - 1)
                if start < 0 or start > end:
                    raise ValueError(f"invalid range {start}-{end}")
                length = end - start + 1

                self.send_response(206)  # Partial Content
                self.send_header("Content-Type", self.guess_type(path))
                self.send_header("Content-Length", str(length))
                self.send_header("Content-Range", f"bytes {start}-{end}/{file_size}")
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

                f = open(path, "rb")
                try:
                    f.seek(start)
                    return _FileWrapper(f, length)
                except Exception:
                    f.close()
                    raise
            except (ValueError, OSError):
                self.send_error(416, "Range Not Satisfiable")
                return None
        else:
            # Normal request
            self.send_response(200)
            self.send_header("Content-Type", self.guess_type(path))
            self.send_header("Content-Length", str(file_size))
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            return open(path, "rb")

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, HEAD, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Range")
        self.send_header("Access-Control-Expose-Headers", "Content-Length, Content-Range")
        self.end_headers()


class _FileWrapper:
    """Wrapper to read a specific byte range from a file."""
    def __init__(self, f, length):
        self.f = f
        self.remaining = length

    def read(self, size=None):
        if self.remaining <= 0:
            return b""
        if size is None or size > self.remaining:
            size = self.remaining
        data = self.f.read(size)
        self.remaining -= len(data)
        return data

    def close(self):
        self.f.close()


def shutdown_server(signum=None, frame=None):
    """Handle shutdown signal."""
    global server_running
    server_running = False
    print("\nShutting down server...")
    httpd.shutdown()
    print("Server stopped.")
    sys.exit(0)

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")

    print(f"Starting server at http://localhost:{PORT}")
    if HOST != "127.0.0.1":
        print(f"  (listening on {HOST}:{PORT})")
    print("Press Ctrl+C to stop (or close this window)\n")

    httpd = ThreadingHTTPServer((HOST, PORT), RangeRequestHandler)

    # Register signal handlers for clean shutdown
    signal.signal(signal.SIGINT, shutdown_server)
    signal.signal(signal.SIGTERM, shutdown_server)
    # Windows-specific: handle Ctrl+Break
    if hasattr(signal, "SIGBREAK"):
        signal.signal(signal.SIGBREAK, shutdown_server)

    # Run server in a daemon thread
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    if not args.no_browser:
        webbrowser.open(f"http://localhost:{PORT}")

    try:
        # Keep main thread alive with a simple loop
        while server_running:
            server_thread.join(timeout=0.5)
            if not server_thread.is_alive():
                break
    except KeyboardInterrupt:
        shutdown_server()
