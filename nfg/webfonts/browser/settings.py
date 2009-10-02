
from zope.component import getUtility
from zope.formlib import form

from plone.app.controlpanel.form import ControlPanelForm

from nfg.webfonts.interfaces import IWebfontsSettings
from nfg.webfonts import WebfontsMessageFactory as _

def webfonts_settings(context):
    return getUtility(IWebfontsSettings)

class ControlPanel(ControlPanelForm):
    form_fields = form.FormFields(IWebfontsSettings)
    form_name = _(u"Webfonts settings")
    label = _(u"Webfonts settings")
    description = _(u"Please enter the appropriate connection settings"
            "for the webfonts webservice")

