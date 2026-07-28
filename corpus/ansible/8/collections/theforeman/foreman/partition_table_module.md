---
collection: ansible
version: "8"
title: "theforeman.foreman.partition_table module – Manage Partition Table Templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/partition_table_module.html
fetched_at: 2026-07-28T02:56:19+00:00
---
# theforeman.foreman.partition_table module – Manage Partition Table Templates

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](partition_table_module.md#ansible-collections-theforeman-foreman-partition-table-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.partition_table`.

New in theforeman.foreman 1.0.0

- [Synopsis](partition_table_module.md#synopsis)
- [Requirements](partition_table_module.md#requirements)
- [Parameters](partition_table_module.md#parameters)
- [Attributes](partition_table_module.md#attributes)
- [Examples](partition_table_module.md#examples)
- [Return Values](partition_table_module.md#return-values)

## [Synopsis](partition_table_module.md#id1)

- Manage Partition Table Templates

Aliases: foreman_ptable

## [Requirements](partition_table_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](partition_table_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **file_name**  path | The path of a template file, that shall be imported.  Either this or *layout* is required as a source for the Partition Template “content”. |
| **layout**  string | The content of the Partitioning Table Template  Either this or *file_name* is required as a source for the Partition Template “content”. |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **locked**  boolean | Determines whether the template shall be locked  **Choices:**   - `false` - `true` |
| **name**  string | The name of the Partition Table.  If omited, will be determined from the `name` header of the template or the filename (in that order).  The special value “\*” can be used to perform bulk actions (modify, delete) on all existing Partition Tables. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **os_family**  string | The OS family the template shall be assigned with.  **Choices:**   - `"AIX"` - `"Altlinux"` - `"Archlinux"` - `"Coreos"` - `"Debian"` - `"Fcos"` - `"Freebsd"` - `"Gentoo"` - `"Junos"` - `"NXOS"` - `"Rancheros"` - `"Redhat"` - `"Rhcos"` - `"Solaris"` - `"Suse"` - `"VRP"` - `"Windows"` - `"Xenserver"` |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **updated_name**  string | New name of the template. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](partition_table_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](partition_table_module.md#id5)

```yaml+jinja
# Keep in mind, that in this case, the inline parameters will be overwritten
- name: "Create a Partition Table inline"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: A New Partition Template
    state: present
    layout: |
      <%#
        name: A Partition Template
      %>
        zerombr
        clearpart --all --initlabel
        autopart
    locations:
      - Gallifrey
    organizations:
      - TARDIS INC

- name: "Create a Partition Template from a file"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    file_name: timeywimey_template.erb
    state: present
    locations:
      - Gallifrey
    organizations:
      - TARDIS INC

- name: "Delete a Partition Template"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: timeywimey
    layout: |
      <%#
          dummy:
      %>
    state: absent

- name: "Create a Partition Template from a file and modify with parameter(s)"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    file_name: timeywimey_template.erb
    name: Wibbly Wobbly Template
    state: present
    locations:
      - Gallifrey
    organizations:
      - TARDIS INC

# Providing a name in this case wouldn't be very sensible.
# Alternatively make use of with_filetree to parse recursively with filter.
- name: "Parsing a directory of partition templates"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    file_name: "{{ item }}"
    state: present
    locations:
      - SKARO
    organizations:
      - DALEK INC
    with_fileglob:
       - "./arsenal_templates/*.erb"

# If the templates are stored locally and the ansible module is executed on a remote host
- name: Ensure latest version of all Ptable Community Templates
  theforeman.foreman.partition_table:
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
    layout: '{{ lookup("file", item.src) }}'
  with_filetree: '/path/to/partition/tables'
  when: item.state == 'file'

# with name set to "*" bulk actions can be performed
- name: "Delete *ALL* partition tables"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "*"
    state: absent

- name: "Assign all partition tables to the same organization(s)"
  theforeman.foreman.partition_table:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "*"
    state: present
    organizations:
      - DALEK INC
      - sky.net
      - Doc Brown's garage
```

## [Return Values](partition_table_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **ptables**  list / elements=dictionary | List of partition tables.  **Returned:** success |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG
- Matthias Dellweg (@mdellweg) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
