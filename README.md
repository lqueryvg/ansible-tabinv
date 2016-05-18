# tabinv

Horizontally group your Ansible hosts.

- dynamic inventory script
- reads hosts from `tabinv.txt` in the current directory
- one host per line
- first field is a host
- subsequent fields are groups which the host belongs to
- fields are separated by whitespace
- comment char is `#`
- blank lines are allowed
- the `VARS` variable inside the script can be edited to add the
  same vars to every group

## Example:

With the following `tabinv.txt` input:

```
host1 live web    # comment
host3 live app
# comment followed by blank line

host2 dev  web    # comment
```

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

