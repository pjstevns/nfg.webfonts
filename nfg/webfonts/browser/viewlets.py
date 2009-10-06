
from zope.component import getUtility
from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from nfg.webfonts.interfaces import IWebfontsSettings

class WebfontsApiViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/webfonts-api.pt')

    def __init__(self, context, request, view, manager):
        super(WebfontsApiViewlet, self).__init__(context, request, view, manager)
        self.__parent__ = view
        self.view = view
        self.manager = manager
        self.webfontssettings = getUtility(IWebfontsSettings)

    @property
    def apiurl(self):
        hostname = self.webfontssettings.getHostname()
        apikey = self.webfontssettings.getApikey()
        if hostname and apikey:
            return "http://%s/api?key=%s" %(hostname, apikey)
        return ''

