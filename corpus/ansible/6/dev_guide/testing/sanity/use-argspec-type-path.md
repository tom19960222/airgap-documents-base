---
collection: ansible
version: "6"
title: "use-argspec-type-path"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/use-argspec-type-path.html
fetched_at: 2026-07-27T16:42:37+00:00
---
# use-argspec-type-path

The AnsibleModule argument_spec knows of several types beyond the standard python types. One of
these is `path`. When used, type `path` ensures that an argument is a string and expands any
shell variables and tilde characters.

This test looks for use of [`os.path.expanduser`](https://docs.python.org/2/library/os.path.html#os.path.expanduser "(in Python v2.7)") in modules. When found, it tells the user to
replace it with `type='path'` in the module’s argument_spec or list it as a false positive in the
test.
