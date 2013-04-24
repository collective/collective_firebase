
# Copyright (c) 2013 Enfold Systems, Inc. All rights reserved.

from firebase_token_generator import create_token
from zope.component import getMultiAdapter
from Products.Five import BrowserView

from .config import get_config, get_properties


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
        plone_username = 'Anonymous'
    else:
        plone_username = plone_userid

    # Admin is always false for now.
    admin = False

    custom_data = {
        'ploneUserid': plone_userid,
        'ploneUsername': plone_username,
    }
    options = {'admin': admin}
    config = get_config()
    token = create_token(config['firebase_secret'], custom_data, options)
    return token


class AllowedUseridView(BrowserView):

    def __call__(self):
        return get_allowed_userid(self.context, self.request)
