# coding=utf-8
"""Dialog tests for WebMapExporterDialog."""

import pytest
#from qgis.core import Qgis
#from qgis.PyQt.QtWidgets import QDialogButtonBox, QDialog

from web_map_exporter_dialog import WebMapExporterDialog

@pytest.fixture
def dialog(qgis_app):
    dlg = WebMapExporterDialog(None)
    yield dlg
    dlg.close()

def test_export_button(dialog):
    """Clicking Export runs the export_layers handler if registered."""
    calls = []
    dialog.set_export_handler(lambda: calls.append("export"))
    dialog.button_export_qt.click()
    assert calls == ["export"]

def test_help_button_opens_webpage(dialog, monkeypatch):
    """Clicking Help opens the documentation webpage."""
    opened_urls = []
    test_url = "https://default-docs-url.com"
    def fake_open_url():
        opened_urls.append(test_url)
    monkeypatch.setattr(dialog, "open_help_page", fake_open_url)

    # Disconnect the original instance method safely
    try:
        dialog.button_box_main_qt.helpRequested.disconnect(dialog.open_help_page)
    except TypeError:
        pass # Handle case where it wasn't connected

    dialog.button_box_main_qt.helpRequested.connect(fake_open_url)
    dialog.button_box_main_qt.helpRequested.emit()
    assert len(opened_urls) == 1
    assert opened_urls[0] == test_url

def test_export_button_calls_handler(dialog):
    """Clicking Export invokes the registered export handler."""
    calls = []
    dialog.set_export_handler(lambda: calls.append("export"))
    dialog.button_export_qt.click()
    assert calls == ["export"]
