
from firebase import Firebase

from .config import get_env_config
from .auth import get_auth_token_for_admin


def add_message(plone_userid, text):
    """Add a message to a user, with effective admin rights.
    """
    auth_token = get_auth_token_for_admin()
    config = get_env_config()
    url = '%s/users/%s/tasks' % (config['firebase_url'], plone_userid)
    tasks = Firebase(url, config['firebase_secret'])
    response = tasks.push({
        'from': 'admin',
        'content': text,
    })()
    return response
