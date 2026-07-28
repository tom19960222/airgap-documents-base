---
collection: ansible
version: "8"
title: "Working with versions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/docsite/filter_guide_working_with_versions.html
fetched_at: 2026-07-28T03:00:45+00:00
---
# Working with versions

If you need to sort a list of version numbers, the Jinja `sort` filter is problematic. Since it sorts lexicographically, `2.10` will come before `2.9`. To treat version numbers correctly, you can use the [community.general.version_sort filter](../version_sort_filter.md#ansible-collections-community-general-version-sort-filter):

```yaml+jinja
- name: Sort list by version number
  debug:
    var: ansible_versions | community.general.version_sort
  vars:
    ansible_versions:
      - '2.8.0'
      - '2.11.0'
      - '2.7.0'
      - '2.10.0'
      - '2.9.0'
```

This produces:

```ansible-output
TASK [Sort list by version number] ********************************************************
ok: [localhost] => {
    "ansible_versions | community.general.version_sort": [
        "2.7.0",
        "2.8.0",
        "2.9.0",
        "2.10.0",
        "2.11.0"
    ]
}
```
