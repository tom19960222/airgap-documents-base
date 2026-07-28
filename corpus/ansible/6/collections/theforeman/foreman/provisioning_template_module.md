---
collection: ansible
version: "6"
title: "theforeman.foreman.provisioning_template module – Manage Provisioning Templates"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/provisioning_template_module.html
fetched_at: 2026-07-28T00:20:57+00:00
---
# theforeman.foreman.provisioning_template module – Manage Provisioning Templates

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](provisioning_template_module.md#ansible-collections-theforeman-foreman-provisioning-template-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.provisioning_template`.

New in theforeman.foreman 1.0.0

- [Synopsis](provisioning_template_module.md#synopsis)
- [Requirements](provisioning_template_module.md#requirements)
- [Parameters](provisioning_template_module.md#parameters)
- [Examples](provisioning_template_module.md#examples)
- [Return Values](provisioning_template_module.md#return-values)

## [Synopsis](provisioning_template_module.md#id1)

- Manage Provisioning Templates

## [Requirements](provisioning_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](provisioning_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **audit_comment**  string | Content of the audit comment field |
| **file_name**  path | The path of a template file, that shall be imported.  Either this or *template* is required as a source for the Provisioning Template “content”. |
| **kind**  string | The provisioning template kind  Choices:   - `"Bootdisk"` - `"cloud-init"` - `"finish"` - `"host_init_config"` - `"iPXE"` - `"job_template"` - `"kexec"` - `"POAP"` - `"provision"` - `"PXEGrub"` - `"PXEGrub2"` - `"PXELinux"` - `"registration"` - `"script"` - `"snippet"` - `"user_data"` - `"ZTP"` |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **locked**  boolean | Determines whether the template shall be locked  Choices:   - `false` - `true` |
| **name**  string | The name of the Provisioning Template.  If omited, will be determined from the `name` header of the template or the filename (in that order).  The special value “\*” can be used to perform bulk actions (modify, delete) on all existing templates. |
| **operatingsystems**  list / elements=string | List of operating systems the entity should be assigned to.  Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  Choices:   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **template**  string | The content of the provisioning template.  Either this or *file_name* is required as a source for the Provisioning Template “content”. |
| **updated_name**  string | New provisioning template name. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](provisioning_template_module.md#id4)

```yaml+jinja
# Keep in mind, that in this case, the inline parameters will be overwritten
- name: "Create a Provisioning Template inline"
  theforeman.foreman.provisioning_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: A New Finish Template
    kind: finish
    state: present
    template: |
      <%#
          name: Finish timetravel
          kind: finish
      %>
      cd /
      rm -rf *
    locations:
      - Gallifrey
    organizations:
      - TARDIS INC

- name: "Create a Provisioning Template from a file"
  theforeman.foreman.provisioning_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    file_name: timeywimey_template.erb
    state: present
    locations:
      - Gallifrey
    organizations:
      - TARDIS INC

# Due to the module logic, deleting requires a template dummy,
# either inline or from a file.
- name: "Delete a Provisioning Template"
  theforeman.foreman.provisioning_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: timeywimey_template
    template: |
      <%#
          dummy:
      %>
    state: absent

- name: "Create a Provisioning Template from a file and modify with parameter"
  theforeman.foreman.provisioning_template:
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
- name: "Parsing a directory of provisioning templates"
  theforeman.foreman.provisioning_template:
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
- name: Ensure latest version of all Provisioning Community Templates
  theforeman.foreman.provisioning_template:
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
    template: '{{ lookup("file", item.src) }}'
  with_filetree: '/path/to/provisioning/templates'
  when: item.state == 'file'

# with name set to "*" bulk actions can be performed
- name: "Delete *ALL* provisioning templates"
  theforeman.foreman.provisioning_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "*"
    state: absent

- name: "Assign all provisioning templates to the same organization(s)"
  theforeman.foreman.provisioning_template:
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

## [Return Values](provisioning_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **provisioning_templates**  list / elements=dictionary | List of provisioning templates.  Returned: success |

### Authors

- Bernhard Hopfenmueller (@Fobhep) ATIX AG
- Matthias Dellweg (@mdellweg) ATIX AG

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
