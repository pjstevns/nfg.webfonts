
from zope import schema
from zope.interface import Interface

from nfg.webfonts import WebfontsMessageFactory as _

class IWebfontsSettings(Interface):
    """ Connection settings 
    """

    hostname = schema.ASCIILine(title=_(u"Host name"),
            description=_(u"The webfonts.biz host name"),
            required=False)

    apikey = schema.ASCIILine(title=_(u"API key"),
            description=_(u"The apikey you have generated for this site"),
            required=True)


