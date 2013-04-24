
# Copyright (c) 2013 Enfold Systems, Inc. All rights reserved.

from firebase_token_generator import create_token
from zope.component import getMultiAdapter
from .config import get_config


def get_auth_token(context, request):
    portal_state = getMultiAdapter((context, request), name="plone_portal_state")
    plone_userid = portal_state.member().getId()
    if plone_userid is None:
        plone_username = 'Anonymous'
    else:
        plone_username = plone_userid

    admin = False

    custom_data = {
        'ploneUserid': plone_userid,
        'ploneUsername': plone_username,
    }
    options = {'admin': admin}
    config = get_config()
    token = create_token(config['firebase_secret'], custom_data, options)
    return token
