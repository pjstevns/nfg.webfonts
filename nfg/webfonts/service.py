
from zope.interface import implements
from persistent import Persistent
from nfg.webfonts.interfaces import IWebfontsSettings

class WebfontsSettings(Persistent):
    implements(IWebfontsSettings)

    hostname='webfonts.biz'
    apikey=''


