import pytest

from girder.plugin import loadedPlugins


@pytest.mark.plugin('girder_mouse')
def test_import(server):
    assert 'girder_mouse' in loadedPlugins()
