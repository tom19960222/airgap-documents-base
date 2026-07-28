---
collection: ansible
version: "8"
title: "no-unicode_literals"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/testing/sanity/no-unicode-literals.html
fetched_at: 2026-07-28T01:03:40+00:00
---
# no-unicode_literals

The use of `from __future__ import unicode_literals` has been deemed an anti-pattern. The
problems with it are:

- It makes it so one can’t jump into the middle of a file and know whether a bare literal string is
  a byte string or text string. The programmer has to first check the top of the file to see if the
  import is there.
- It removes the ability to define native strings (a string which should be a byte string on python2
  and a text string on python3) by a string literal.
- It makes for more context switching. A programmer could be reading one file which has
  unicode_literals and know that bare string literals are text strings but then switch to another
  file (perhaps tracing program execution into a third party library) and have to switch their
  understanding of what bare string literals are.
