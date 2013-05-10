
import sys

from ..db import add_message


def main(argv=sys.argv):
    args = argv[1:]
    if not 2 <= len(args) <= 3:
        raise RuntimeError(
            'Wrong parameters.\n'
            '\n'
            'Usage: firebase_put <plone_userid> <text>\n'
            '       firebase_put <plone_userid> <text> <reason>\n')
    plone_userid, text, reason = (args + [None])[:3]
    response = add_message(plone_userid, text, reason)
    print "Added."

if __name__ == '__main__':
    main()
