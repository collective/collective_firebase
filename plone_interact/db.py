
import time

from firebase import Firebase

from .config import get_env_config
from .auth import get_auth_token_for_admin

DEFAULT_REASON = 'Added by privileged console script'


def add_message(plone_userid, text, reason=None):
    """Add a message to a user, with effective admin rights.
    """
    if reason is None:
        reason = DEFAULT_REASON
    auth_token = get_auth_token_for_admin()
    config = get_env_config()
    url = '%s/users/%s/tasks' % (config['firebase_url'], plone_userid)
    tasks = Firebase(url, auth_token=auth_token)
    response = tasks.push({
        'from': 'admin',
        'content': text.decode('string-escape'),
        'ts': time.time() * 1000,
        'reason': reason,
    })()
    return response
