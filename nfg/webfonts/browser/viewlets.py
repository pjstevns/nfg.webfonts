from plone.app.layout.viewlets.common import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class WebfontsApiViewlet(ViewletBase):
    render = ViewPageTemplateFile('templates/webfonts-api.pt')

