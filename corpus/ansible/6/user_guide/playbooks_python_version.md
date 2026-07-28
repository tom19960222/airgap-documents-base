---
collection: ansible
version: "6"
title: "Python3 in templates"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/playbooks_python_version.html
fetched_at: 2026-07-27T16:43:03+00:00
---
# Python3 in templates

Ansible uses Jinja2 to take advantage of Python data types and standard functions in templates and variables.
You can use these data types and standard functions to perform a rich set of operations on your data. However,
if you use templates, you must be aware of differences between Python versions.

These topics help you design templates that work on both Python2 and Python3. They might also help if you are upgrading from Python2 to Python3. Upgrading within Python2 or Python3 does not usually introduce changes that affect Jinja2 templates.

## Dictionary views

In Python2, the [`dict.keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys "(in Python v3.11)"), [`dict.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values "(in Python v3.11)"), and [`dict.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items "(in Python v3.11)")
methods return a list. Jinja2 returns that to Ansible via a string
representation that Ansible can turn back into a list.

In Python3, those methods return a [dictionary view](https://docs.python.org/3/library/stdtypes.html#dict-views "(in Python v3.11)") object. The
string representation that Jinja2 returns for dictionary views cannot be parsed back
into a list by Ansible. It is, however, easy to make this portable by
using the [`list`](https://jinja.palletsprojects.com/en/3.1.x/templates/#jinja-filters.list "(in Jinja v3.1.x)") filter whenever using [`dict.keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys "(in Python v3.11)"),
[`dict.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values "(in Python v3.11)"), or [`dict.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items "(in Python v3.11)").

```yaml+jinja
vars:
  hosts:
    testhost1: 127.0.0.2
    testhost2: 127.0.0.3
tasks:
  - debug:
      msg: '{{ item }}'
    # Only works with Python 2
    #loop: "{{ hosts.keys() }}"
    # Works with both Python 2 and Python 3
    loop: "{{ hosts.keys() | list }}"
```

## dict.iteritems()

Python2 dictionaries have [`iterkeys()`](https://docs.python.org/2/library/stdtypes.html#dict.iterkeys "(in Python v2.7)"), [`itervalues()`](https://docs.python.org/2/library/stdtypes.html#dict.itervalues "(in Python v2.7)"), and [`iteritems()`](https://docs.python.org/2/library/stdtypes.html#dict.iteritems "(in Python v2.7)") methods.

Python3 dictionaries do not have these methods. Use [`dict.keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys "(in Python v3.11)"), [`dict.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values "(in Python v3.11)"), and [`dict.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items "(in Python v3.11)") to make your playbooks and templates compatible with both Python2 and Python3.

```yaml+jinja
vars:
  hosts:
    testhost1: 127.0.0.2
    testhost2: 127.0.0.3
tasks:
  - debug:
      msg: '{{ item }}'
    # Only works with Python 2
    #loop: "{{ hosts.iteritems() }}"
    # Works with both Python 2 and Python 3
    loop: "{{ hosts.items() | list }}"
```

> **See also:**
>
> - The [Dictionary views](playbooks_python_version.md#pb-py-compat-dict-views) entry for information on
>   why the [`list filter`](https://jinja.palletsprojects.com/en/3.1.x/templates/#jinja-filters.list "(in Jinja v3.1.x)") is necessary
>   here.
