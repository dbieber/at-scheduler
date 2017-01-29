import json
import parsedatetime
import redis

import sys

class CLI(object):

    def __init__(self, *args):
        if len(args) == 1:
            print('Usage: {command} time command'.format(command='at'))
            return

        text = ' '.join(args)
        r = redis.Redis()
        r.rpush('at:command-queue', text)

if __name__ == '__main__':
    argv = sys.argv
    CLI(*argv)
