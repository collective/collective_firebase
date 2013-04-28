
# Copyright (c) 2013 Enfold Systems, Inc. All rights reserved.

from firebase_token_generator import create_token
from zope.component import getMultiAdapter
from Products.Five import BrowserView

from .config import (
    get_config,
    get_properties,
    get_env_config,
)


def get_auth_token_for_admin():
    """Create an auth token with full admin rights.

    Used from privilegized console scripts.
    This needs the url, and the secret from env variables.
    """
    config = get_env_config()
    custom_data = {
        'ploneUserid': 'admin',
    }
    options = {
        'admin': True,
    }
    token = create_token(config['firebase_secret'], custom_data, options)
    return token


def get_allowed_userid(context, request):
    """Return the userid, None (if anon), or False,
    if the user is not allowed to use this feature.
    """
    portal_state = getMultiAdapter((context, request), name="plone_portal_state")
    plone_userid = portal_state.member().getId()

    # If the user is not allowed, refuse to give a token.
    props = get_properties()
    if props is not None and \
            props.getProperty('filter_users', False) and \
            plone_userid not in props.getProperty('allowed_users', ()):
        # User is not allowed.
        return False
    else:
        return plone_userid


def get_auth_token(context, request):
    plone_userid = get_allowed_userid(context, request)

    if plone_userid is False:
        # If the user is not allowed, return a void token.
        return ''

    if plone_userid is None:
        # If the user is anonymous (ot logged in), we do not 
        # allow it either. Return a void token.
        return ''

    # Admin is always false for now.
    admin = False

    custom_data = {
        'ploneUserid': plone_userid,
        'userPrefix': '/users/%s' % (plone_userid, ),
    }
    options = {
        'admin': admin,
    }
    config = get_config()
    token = create_token(config['firebase_secret'], custom_data, options)
    return token


class AllowedUseridView(BrowserView):

    def __call__(self):
        return get_allowed_userid(self.context, self.request)
