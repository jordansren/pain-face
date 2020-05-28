from girder import plugin
from girder.api import access
from girder.api.describe import Description, autoDescribeRoute
from girder.api.rest import Resource
from girder.constants import AccessType
from girder.models.folder import Folder
from girder.models.item import Item


class MousePainPlugin(plugin.GirderPlugin):
    DISPLAY_NAME = 'mouse-pain'

    def load(self, info):
        # add plugin loading logic here
        info['apiRoot'].mouse_pain_face = MousePain()


class MousePain(Resource):
    def __init__(self):
        super(MousePain, self).__init__()
        self.resourceName = "mouse_pain_face"
        self.route("POST", (":id",), self.process)


    @access.user
    @autoDescribeRoute(Description("create folder with uploaded file")
                        .m,odelParam())
    def process(self,b):
        return "Processing " + id 


