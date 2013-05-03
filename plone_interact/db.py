
import time

from firebase import Firebase

from .config import get_env_config
from .auth import get_auth_token_for_admin

DEFAULT_REASON = 'Added by privileged console script'


def get_tasks(plone_userid):
    auth_token = get_auth_token_for_admin()
    config = get_env_config()
    url = '%s/users/%s/tasks' % (config['firebase_url'], plone_userid)
    tasks = Firebase(url, auth_token=auth_token)
    return tasks


def get_task(plone_userid, key):
    auth_token = get_auth_token_for_admin()
    config = get_env_config()
    url = '%s/users/%s/tasks/%s' % (config['firebase_url'], plone_userid, key)
    task = Firebase(url, auth_token=auth_token)
    return task


def add_message(plone_userid, text, reason=None):
    """Add a message to a user, with effective admin rights.
    """
    if reason is None:
        reason = DEFAULT_REASON
    tasks = get_tasks(plone_userid)
    tasks.push({
        'from': 'admin',
        'content': text.decode('string-escape'),
        'ts': time.time() * 1000,
        'reason': reason,
    })()


def get_messages(plone_userid):
    """Get all messages sent to a user, with effective admin rights.
    """
    tasks = get_tasks(plone_userid)
    response = tasks.get()()
    return response


def delete_messages(plone_userid, keys):
    """Delete selected messages sent to a user, with effective admin rights.
    """
    tasks = get_tasks(plone_userid)
    for key in keys:
        task = get_task(plone_userid, key)
        task.remove()
