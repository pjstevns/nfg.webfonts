
from zope.interface import implements
from persistent import Persistent
from nfg.webfonts.interfaces import IWebfontsSettings

class WebfontsSettings(Persistent):
    implements(IWebfontsSettings)

    hostname='webfonts.biz'
    apikey=''


    def getApikey(self):
        return self.apikey

    def getHostname(self):
        return self.hostname
