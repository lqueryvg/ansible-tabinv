# tabinv.py

[![Build Status](https://travis-ci.org/lqueryvg/ansible-tabinv.svg?branch=master)](https://travis-ci.org/lqueryvg/ansible-tabinv)

Horizontally group your Ansible hosts.

- dynamic inventory script
- reads hosts from `tabinv.txt` in the same directory as tabinv.py
- one host per line
- first field is a host
- subsequent fields are groups which the host belongs to
- fields are separated by whitespace
- comment char is `#`
- blank lines are allowed
- the `VARS` variable inside the script can be edited to add the
  same vars to every group

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
   "host2", 
   "host1"
  ], 
  "vars": {}
 }, 
 "all": {
  "hosts": [
   "host3", 
   "host2", 
   "host1"
  ], 
  "vars": {}
 }, 
 "app": {
  "hosts": [
   "host3"
  ], 
  "vars": {}
 }, 
 "live": {
  "hosts": [
   "host3", 
   "host1"
  ], 
  "vars": {}
 }, 
 "dev": {
  "hosts": [
   "host2"
  ], 
  "vars": {}
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

## Big Tip
Instead of pointing Ansible at a single inventory file or script (with `-i`)
you can point at a directory. Thus you could combine `tabinv` with files
containing specific host or group var settings. For example, in the above
example you could specify a different connection type for the "live" group.
