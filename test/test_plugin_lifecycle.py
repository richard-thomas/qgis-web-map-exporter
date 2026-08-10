# coding=utf-8
"""Lifecycle tests: classFactory -> initGui -> unload."""

from unittest.mock import MagicMock

def test_class_factory_returns_instance(qgis_iface):
    """classFactory returns a plugin instance."""
    from web_map_exporter.web_map_exporter import WebMapExporter
    plugin = WebMapExporter(qgis_iface)
    assert plugin is not None


def test_init_gui_registers_action(qgis_iface):
    """initGui adds a toolbar icon via iface."""
    from web_map_exporter.web_map_exporter import WebMapExporter
    plugin = WebMapExporter(qgis_iface)
    plugin.initGui()
    assert plugin.actions
    plugin.unload()


def test_unload_removes_action(qgis_iface, monkeypatch):
    """unload removes the toolbar icon via iface."""
    from web_map_exporter.web_map_exporter import WebMapExporter
    plugin = WebMapExporter(qgis_iface)
    remove_toolbar_icon = MagicMock()
    monkeypatch.setattr(qgis_iface, "removeToolBarIcon", remove_toolbar_icon)
    plugin = WebMapExporter(qgis_iface)
    plugin.initGui()
    plugin.unload()
    remove_toolbar_icon.assert_called()
