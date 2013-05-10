
# Copyright (c) 2013 Enfold Systems, Inc. All rights reserved.

from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets import common as base

from .config import get_config
from .auth import get_auth_token


class InteractViewlet(base.ViewletBase):
    """
    """

    def update(self):
        super(InteractViewlet, self).update()
        self.auth_token = get_auth_token(self.context, self.request)
        self.config = get_config()
        # Is the product installed?
        # We need to check it, as this information is not obvious based on
        # the configuration alone.
        # The importance of this check is to avoid the viewlet being
        # rendered before the product is installed with quickinstaller
        # in a newly created portal.
        qi = getToolByName(self.context, 'portal_quickinstaller')
        self.is_installed = qi.isProductInstalled('plone_interact')

    def render(self):
        if self.is_installed and self.auth_token:
            return super(InteractViewlet, self).render()
        else:
            return ''
