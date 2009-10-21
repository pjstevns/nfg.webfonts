

from zope.component import queryUtility
from plone.app.layout.viewlets.common import ViewletBase
from plone.registry.interfaces import IRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from nfg.webfonts.interfaces import IWebfontsSettings
from plone.z3cform import layout

import logging
logger = logging.getLogger('nfg.webfonts')

class WebFontsControlPanelForm(RegistryEditForm):
    schema = IWebfontsSettings

WebFontsControlPanel = layout.wrap_form(WebFontsControlPanelForm, ControlPanelFormWrapper)

class WebfontsApiViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/webfonts-api.pt')

    def __init__(self, context, request, view, manager):
        super(WebfontsApiViewlet, self).__init__(context, request, view, manager)
        self.__parent__ = view
        self.view = view
        self.manager = manager
        self.hostname=''
        self.apikey=''
        registry = queryUtility(IRegistry)
        if registry is not None:
            self.hostname = registry.forInterface(IWebfontsSettings).hostname
            self.apikey = registry.forInterface(IWebfontsSettings).apikey

    @property
    def apiurl(self):
        apiurl = ''
        if self.hostname and self.apikey:
            apiurl = "%s/api?key=%s" %(self.hostname, self.apikey)
            if apiurl[:4] != 'http': 
                apiurl = "http://%s" % apiurl
        logger.info('apiurl [%s]' % apiurl)
        return apiurl

