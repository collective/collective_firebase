
# Copyright (c) 2013 Enfold Systems, Inc. All rights reserved.

import os

from zope.component import queryUtility
from Products.CMFCore.interfaces import IPropertiesTool


def get_properties():
    ptool = queryUtility(IPropertiesTool)
    if ptool is not None:
        return getattr(ptool, 'interact_properties', None)


def get_env_config():
    """Get the configuration

    Data comes from the PLONE_INTERACT_XXX environment variables.
    """
    return {
        'firebase_url': os.getenv('PLONE_INTERACT_FIREBASE_URL', ''),
        'firebase_secret': os.getenv('PLONE_INTERACT_FIREBASE_SECRET', ''),
    }


def get_config():
    """Get the configuration

    Data comes from the plone site properties.

    If a given property is not found, then a
    PLONE_INTERACT_XXX environment variable is sourced.

    """
    props = get_properties()
    if props is None:
        return None
    config = {
        'firebase_url': props.getProperty('firebase_url', ''),
        'firebase_secret': props.getProperty('firebase_secret', ''),
    }
    for key, value in get_env_config().iteritems():
        if not config[key]:
            config[key] = value
    return config
