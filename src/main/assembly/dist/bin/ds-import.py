#!/usr/bin/env python3

import argparse
import requests

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('batch',
                    help='batch of deposits to import')
parser.add_argument('-c', '--continue',
                    action='store_true',
                    dest='continue_previous',
                    help='continue previously stopped batch (output directory is allowed to be non-empty)')
args = parser.parse_args()

r = requests.post('http://localhost:20000/import', json = {
    'batch': args.batch,
    'continue': args.continue_previous
})

print('Server responded: %s' % r.text)