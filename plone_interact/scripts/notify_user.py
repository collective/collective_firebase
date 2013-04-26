
import sys

from ..db import add_message

def main(argv=sys.argv):
    args = argv[1:]
    if len(args) != 2:
        raise RuntimeError('Usage: add_message <plone_userid> <text>')
    plone_userid, text = args
    response = add_message(plone_userid, text)
    print "response:", response

if __name__ == '__main__':
    main()
