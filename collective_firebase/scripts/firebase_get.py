
import sys
import datetime

from ..db import (
    get_messages,
    delete_messages,
)


def main(argv=sys.argv):
    args = argv[1:]
    if not 1 <= len(args) <= 1:
        raise RuntimeError(
            'Wrong parameters.\n'
            '\n'
            'Usage: firebase_get <plone_userid>\n')
    plone_userid = args[0]
    response = get_messages(plone_userid)
    messages = [(key, value) for (key, value) in response.iteritems()]
    messages.sort(key=lambda s: s[1]['ts'], reverse=True)
    print
    for i, (key, value) in enumerate(messages):
        ts = datetime.datetime.fromtimestamp(value['ts'] / 1000.0)
        print "#%i" % (i + 1, )
        print 'From:', value['from'],
        if value['from'] == plone_userid:
            print '(task to self)'
        else:
            print
        print 'Date:', ts
        if value['reason']:
            print 'Reason:', value['reason']
        print value['content']
        print
        print

    choice = None
    while not choice in ('y', 'Y', 'n', 'N', ''):
        choice = raw_input("Clear the tasks you have just read? (y/N) ")
    delete = choice in ('y', 'Y')

    if delete:
        keys = [item[0] for item in messages]
        response = delete_messages(plone_userid, keys)
        print "Deleted %i messages." % (len(keys), )


if __name__ == '__main__':
    main()
