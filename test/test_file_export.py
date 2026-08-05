# coding=utf-8
"""Tests for the extracted file export module."""


def test_file_export_module_exposes_exporter_class():
    from web_map_exporter.file_export import FileExport

    assert FileExport is not None
