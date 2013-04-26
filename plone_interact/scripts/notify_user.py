
import sys

from firebase import Firebase

from ..config import get_env_config
from ..auth import get_auth_token_for_admin


def add_message(plone_userid, text):
    auth_token = get_auth_token_for_admin()
    config = get_env_config()
    url = '%s/users/%s/tasks' % (config['firebase_url'], plone_userid)
    tasks = Firebase(url, config['firebase_secret'])
    tasks.push({'foo': 'bar'})()
    response = tasks.push({
        'from': plone_userid,
        'content': text,
    })()
    print "response:", response


def main(argv=sys.argv):
    args = argv[1:]
    if len(args) != 2:
        raise RuntimeError('Usage: add_message <plone_userid> <text>')
    plone_userid, text = args
    add_message(plone_userid, text)


if __name__ == '__main__':
    main()
