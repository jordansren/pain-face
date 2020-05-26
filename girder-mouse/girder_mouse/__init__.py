from girder import plugin
from girder.api import access
from girder.api.describe import Description, autoDescribeRoute, describeRoute
from girder.api.rest import Resource
from girder.constants import AccessType
from girder.models.folder import Folder
from girder.models.item import Item


class GirderPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'mouse-pain'
    CLIENT_SOURCE_PATH = 'web_client'

    def load(self, info):
        # add plugin loading logic here
        info['apiRoot'].fileupload = FileUpload()
        



class FileUpload(Resource):
    def __init__(self):
        super(FileResource, self).__init__()
        self.resourceName = "FileUpload"

        self.route("POST", (":id",), self.set_file)


    @access.user
    @describeRoute(Description("create folder with uploaded file"))
    def set_file(self, params):
        return None
