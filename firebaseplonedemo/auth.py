
from firebase_token_generator import create_token
from zope.component import getMultiAdapter

SECRET = '9eUKpltlO24bgtmRYlJe1ExR4zl5mHE3osDbw8xr'


class AuthTokenView(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        portal_state = getMultiAdapter((self.context, self.request), name="plone_portal_state")
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
        token = create_token(SECRET, custom_data, options)
        return token
