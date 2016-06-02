#!/usr/bin/env python

from __future__ import print_function

import argparse
import sys
import os

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

try:
    import json
except:
    import simplejson as json


def get_group_hosts(inventory_file):
  if not os.path.isfile(inventory_file):
    eprint("ERROR: inventory file " + inventory_file + " not found")
    return {}
  group_hosts = {}
  hostvars = {}
  with open(inventory_file) as f:

    for line in f:
      line = (line.split("#")[0])   # strip comments
      fields = line.split()
    
      if len(fields) == 0:
          # skip blank lines
          continue
    
      host = fields.pop(0)
      fields.insert(0, "all")   # TODO maybe Ansible does this for me ?
      for group in fields:
        if group not in group_hosts:
            new_set = set()
            new_set.add(host)
            group_hosts[group] = new_set
        else:
          group_hosts[group].add(host)

  # convert sets to lists, otherwise json.dumps() gets angry
  for g in group_hosts:
    l = list(group_hosts[g])
    l.sort()
    group_hosts[g] = {
      'hosts': l
    }

  group_hosts['_meta'] = {'hostvars': hostvars}
  return group_hosts


def print_list(inventory_file):
  group_hosts = get_group_hosts(inventory_file)
  print(json.dumps(group_hosts, indent=1))


def print_host(host):
  print(json.dumps({'_meta': {'hostvars': {}}}, indent=1))


def get_args(args_list):
  parser = argparse.ArgumentParser(
    description="get inventory from tabulated hosts file tabinv.txt "
                "(expected to be in the same dir as this script)")
  mutex_group = parser.add_mutually_exclusive_group(required=True)
  help_list = 'list all hosts found'
  mutex_group.add_argument('--list', action='store_true', help=help_list)
  help_host = 'display variables for a host'
  mutex_group.add_argument('--host', help=help_host)
  return parser.parse_args(args_list)


def main(args_list):
  inventory_file = os.path.dirname(__file__) + '/tabinv.txt'

  args = get_args(args_list)
  if args.list:
    print_list(inventory_file)
  if args.host:
    print_host(args.host)

if __name__ == '__main__':
  main(sys.argv[1:])
