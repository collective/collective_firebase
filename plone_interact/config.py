
import os

from zope.component import queryUtility
from Products.CMFCore.interfaces import IPropertiesTool


def get_config():
    """Get the configuration

    Data comes from the plone site properties.

    If a given property is not found, then a
    PLONE_INTERACT_XXX environment variable is sourced.

    """
    ptool = queryUtility(IPropertiesTool)
    if ptool is None:
        return None
    props = getattr(ptool, 'interact_properties', None)
    if props is None:
        return None
    config = {}
    config['firebase_url'] = props.getProperty('firebase_url', '') or \
        os.getenv('PLONE_INTERACT_FIREBASE_URL', '')
    config['firebase_secret'] = props.getProperty('firebase_secret', '') or \
        os.getenv('PLONE_INTERACT_FIREBASE_SECRET', '')
    return config
