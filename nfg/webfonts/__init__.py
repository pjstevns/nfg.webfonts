"""Main product initializer
"""

from zope.i18nmessageid import MessageFactory

WebfontsMessageFactory = MessageFactory('nfg.webfonts')

def initialize(context):
    """Initializer called when used as a Zope 2 product.

       This is referenced from configure.zcml. Regstrations as a "Zope 2 product"
       is necessary for GenericSetup profiles to work, for example.

       Here, we call the Archetypes machinery to register our content types
       with Zope and the CMF.
       """

