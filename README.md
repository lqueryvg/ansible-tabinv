# tabinv.py

[![Build Status](https://travis-ci.org/lqueryvg/ansible-tabinv.svg?branch=master)](https://travis-ci.org/lqueryvg/ansible-tabinv)

Horizontally group your Ansible hosts.

- dynamic inventory script
- reads hosts from `tabinv.txt`
- one host per line
- first field is the host name
- subsequent fields specify groups which the host belongs to
- fields are separated by whitespace
- comment char is `#`
- blank lines are allowed
- `tabinv.txt` is expected to be found in the same directory as `tabinv.py`

## Example:

The following `tabinv.txt` file

```
host1 live web
host2 dev  web
host3 live app
```

is equivalent to this:
```
[live]
host1
host3

[web]
host1
host2

[dev]
host2

[app]
host3
```

Which do you think is more readable and manageable ?

## Output:

`tabinv.py --list` produces the following:
```
{
 "web": {
  "hosts": [
   "host1", 
   "host2"
  ]
 }, 
 "all": {
  "hosts": [
   "host1", 
   "host2", 
   "host3"
  ]
 }, 
 "_meta": {
  "hostvars": {}
 }, 
 "app": {
  "hosts": [
   "host3"
  ]
 }, 
 "dev": {
  "hosts": [
   "host2"
  ]
 }, 
 "live": {
  "hosts": [
   "host1", 
   "host3"
  ]
 }
}
```

`tabinv.py --host {string}` always produces empty `_meta` output:
```
{
 "_meta": {
  "hostvars": {}
 }
}
```

## Using `tabinv.py` from an inventory directory

Instead of specifying a single inventory file or script with `ansible -i`
you can point it at a directory, where it will discover inventory files and scripts.
If you want `tabinv.py` to live in such a directory, 
note that `tabinv.txt` must go in the same directory and you
must therefore tell Ansible to ignore this file. One way to do this would be
to put the the following in `~/.ansible.cfg`:

```
inventory_ignore_extensions = .txt
```

## Host and group variables

The `tabinv.txt` format does not support host and group variables, but this problem is easily overcome by using `host_vars` and `group_vars` directories in your playbook directory or your global inventory path (e.g. `/etc/ansible`). See http://docs.ansible.com/ansible/intro_inventory.html.
