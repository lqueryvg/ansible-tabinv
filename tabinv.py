#!/usr/bin/env python

import argparse
import sys
import os
#import sets

try:
    import json
except:
    import simplejson as json

#result = {}
TABINV = "tabinv.txt"

#print(json.dumps(result))

def get_groups():
  if not os.path.isfile(os.path.expanduser(TABINV)):
    return {}
  groups = {}
  with open(os.path.expanduser(TABINV)) as f:

    for line in f:
    line = (line.split("#")[0])   # strip comments
    fields = line.split()
    
    if len(fields) == 0:
        # skip blank lines
        continue
    
      host = fields.pop(0)
      fields.insert(0, "all")
      for group in fields:
        if group not in groups:
            new_set = set()
            new_set.add(host)
            groups[group] = new_set
        else:
          groups[group].add(host)
  # convert sets to lists
  for g in groups:
    groups[g] = list(groups[g])
    groups[g] = {
      'hosts': list(groups[g]),
      'vars': {
        'ansible_connection': 'jssh',
        'ansible_python_interpreter': '/opt/bin/python',
      }
    }

  return groups


def print_list():
  cfg = get_groups()
  print(json.dumps(cfg))


def print_host(host):
  # TODO
  return


def get_args(args_list):
  parser = argparse.ArgumentParser(
             description='get inventory from tabulated hosts file')
  mutex_group = parser.add_mutually_exclusive_group(required=True)
  help_list = 'list all hosts found'
  mutex_group.add_argument('--list', action='store_true', help=help_list)
  help_host = 'display variables for a host'
  mutex_group.add_argument('--host', help=help_host)
  return parser.parse_args(args_list)


def main(args_list):
  args = get_args(args_list)
  if args.list:
    print_list()
  if args.host:
    print_host(args.host)

if __name__ == '__main__':
  main(sys.argv[1:])
