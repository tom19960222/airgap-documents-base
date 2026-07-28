---
collection: ansible
version: "6"
title: "no-basestring"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/no-basestring.html
fetched_at: 2026-07-27T16:42:27+00:00
---
# no-basestring

Do not use `isinstance(s, basestring)` as basestring has been removed in
Python3. You can import `string_types`, `binary_type`, or `text_type`
from `ansible.module_utils.six` and then use `isinstance(s, string_types)`
or `isinstance(s, (binary_type, text_type))` instead.

If this is part of code to convert a string to a particular type,
`ansible.module_utils.common.text.converters` contains several functions
that may be even better for you: `to_text`, `to_bytes`, and `to_native`.
