---
collection: ansible
version: "8"
title: "theforeman.foreman.job_template module – Manage Job Templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/job_template_module.html
fetched_at: 2026-07-28T02:56:11+00:00
---
# theforeman.foreman.job_template module – Manage Job Templates

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
> see [Requirements](job_template_module.md#ansible-collections-theforeman-foreman-job-template-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.job_template`.

New in theforeman.foreman 1.0.0

- [Synopsis](job_template_module.md#synopsis)
- [Requirements](job_template_module.md#requirements)
- [Parameters](job_template_module.md#parameters)
- [Attributes](job_template_module.md#attributes)
- [Examples](job_template_module.md#examples)
- [Return Values](job_template_module.md#return-values)

## [Synopsis](job_template_module.md#id1)

- Manage Remote Execution Job Templates

Aliases: foreman_job_template

## [Requirements](job_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](job_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **audit_comment**  string | Content of the audit comment field |
| **description_format**  string | description of the job template. Template inputs can be referenced. |
| **file_name**  path | The path of a template file, that shall be imported.  Either this or *template* is required as a source for the Job Template “content”. |
| **job_category**  string | The category the template should be assigend to |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **locked**  boolean | Determines whether the template shall be locked  **Choices:**   - `false` ← (default) - `true` |
| **name**  string | The name of the Job Template.  If omited, will be determined from the `name` header of the template or the filename (in that order).  The special value “\*” can be used to perform bulk actions (modify, delete) on all existing templates. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **provider_type**  string | Determines via which provider the template shall be executed |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **snippet**  boolean | Determines whether the template shall be a snippet  **Choices:**   - `false` - `true` |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **template**  string | The content of the Job Template.  Either this or *file_name* is required as a source for the Job Template “content”. |
| **template_inputs**  list / elements=dictionary | The template inputs used in the Job Template |
| **advanced**  boolean | Template Input is advanced  **Choices:**   - `false` - `true` |
| **default**  string  *added in theforeman.foreman 3.8.0* | Default value for user input |
| **description**  string | description of the Template Input |
| **fact_name**  string | Fact name to use.  Required when *input_type=fact*. |
| **hidden_value**  boolean | The value contains sensitive information and should’t be normally visible, useful e.g. for passwords  **Choices:**   - `false` - `true` |
| **input_type**  string / required | input type  **Choices:**   - `"user"` - `"fact"` - `"variable"` - `"puppet_parameter"` |
| **name**  string / required | name of the Template Input |
| **options**  list / elements=any | Template values for user inputs. Must be an array of any type. |
| **puppet_class_name**  string | Puppet class name.  Required when *input_type=puppet_parameter*. |
| **puppet_parameter_name**  string | Puppet parameter name.  Required when *input_type=puppet_parameter*. |
| **required**  boolean | Is the input required  **Choices:**   - `false` - `true` |
| **resource_type**  string | Type of the resource |
| **value_type**  string | Type of the value  **Choices:**   - `"plain"` - `"search"` - `"date"` - `"resource"` |
| **variable_name**  string | Variable name to use.  Required when *input_type=variable*. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](job_template_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](job_template_module.md#id5)

```yaml+jinja
- name: "Create a Job Template inline"
  theforeman.foreman.job_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: A New Job Template
    state: present
    template: |
      <%#
          name: A Job Template
      %>
      rm -rf <%= input("toDelete") %>
    template_inputs:
      - name: toDelete
        input_type: user
    locations:
    - Gallifrey
    organizations:
    - TARDIS INC

- name: "Create a Job Template from a file"
  theforeman.foreman.job_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: a new job template
    file_name: timeywimey_template.erb
    template_inputs:
      - name: a new template input
        input_type: user
    state: present
    locations:
    - Gallifrey
    organizations:
    - TARDIS INC

- name: "remove a job template's template inputs"
  theforeman.foreman.job_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: a new job template
    template_inputs: []
    state: present
    locations:
    - Gallifrey
    organizations:
    - TARDIS INC

- name: "Delete a Job Template"
  theforeman.foreman.job_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: timeywimey
    state: absent

- name: "Create a Job Template from a file and modify with parameter(s)"
  theforeman.foreman.job_template:
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
- name: Parsing a directory of Job templates
  theforeman.foreman.job_template:
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
- name: Ensure latest version of all your Job Templates
  theforeman.foreman.job_template:
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
    template: '{{ lookup("file", item.src) }}'
    name: '{{ item.path }}'
  with_filetree: '/path/to/job/templates'
  when: item.state == 'file'

# with name set to "*" bulk actions can be performed
- name: "Delete *ALL* Job Templates"
  theforeman.foreman.job_template:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "*"
    state: absent

- name: "Assign all Job Templates to the same organization(s)"
  theforeman.foreman.job_template:
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

## [Return Values](job_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **job_templates**  list / elements=dictionary | List of job templates.  **Returned:** success |
| **template_inputs**  list / elements=dictionary | List of template inputs associated with the job template.  **Returned:** success |

### Authors

- Manuel Bonk (@manuelbonk) ATIX AG
- Matthias Dellweg (@mdellweg) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
