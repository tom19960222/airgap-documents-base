---
collection: ansible
version: "6"
title: "Paths"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/docsite/filter_guide_paths.html
fetched_at: 2026-07-28T00:24:48+00:00
---
# Paths

The `path_join` filter has been added in ansible-base 2.10. If you want to use this filter, but also need to support Ansible 2.9, you can use `community.general`’s `path_join` shim, `community.general.path_join`. This filter redirects to `path_join` for ansible-base 2.10 and ansible-core 2.11 or newer, and re-implements the filter for Ansible 2.9.

```yaml+jinja
# ansible-base 2.10 or newer:
path: {{ ('/etc', path, 'subdir', file) | path_join }}

# Also works with Ansible 2.9:
path: {{ ('/etc', path, 'subdir', file) | community.general.path_join }}
```

New in version 3.0.0.
