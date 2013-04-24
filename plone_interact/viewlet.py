
import urllib

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
