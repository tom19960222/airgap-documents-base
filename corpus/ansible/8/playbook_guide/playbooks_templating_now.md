---
collection: ansible
version: "8"
title: "The now function: get the current time"
source_url: https://docs.ansible.com/projects/ansible/8/playbook_guide/playbooks_templating_now.html
fetched_at: 2026-07-28T00:59:54+00:00
---
# The now function: get the current time

New in version 2.8.

The `now()` Jinja2 function retrieves a Python datetime object or a string representation for the current time.

The `now()` function supports 2 arguments:

utc
:   Specify `True` to get the current time in UTC. Defaults to `False`.

fmt
:   Accepts a [strftime](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) string that returns a formatted date time string.
