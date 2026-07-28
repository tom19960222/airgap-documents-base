---
collection: ansible
version: "8"
title: "community.general.one_template module – Manages OpenNebula templates"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/one_template_module.html
fetched_at: 2026-07-28T01:48:22+00:00
---
# community.general.one_template module – Manages OpenNebula templates

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](one_template_module.md#ansible-collections-community-general-one-template-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.one_template`.

New in community.general 2.4.0

- [Synopsis](one_template_module.md#synopsis)
- [Requirements](one_template_module.md#requirements)
- [Parameters](one_template_module.md#parameters)
- [Attributes](one_template_module.md#attributes)
- [Examples](one_template_module.md#examples)
- [Return Values](one_template_module.md#return-values)

## [Synopsis](one_template_module.md#id1)

- Manages OpenNebula templates.

Aliases: cloud.opennebula.one_template

## [Requirements](one_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyone

## [Parameters](one_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_password**  aliases: api_token  string | The password or token for XMLRPC authentication.  If not specified then the value of the [`ONE_PASSWORD`](../../environment_variables.md#envvar-ONE_PASSWORD) environment variable, if any, is used. |
| **api_url**  aliases: api_endpoint  string | The ENDPOINT URL of the XMLRPC server.  If not specified then the value of the [`ONE_URL`](../../environment_variables.md#envvar-ONE_URL) environment variable, if any, is used. |
| **api_username**  string | The name of the user for XMLRPC authentication.  If not specified then the value of the [`ONE_USERNAME`](../../environment_variables.md#envvar-ONE_USERNAME) environment variable, if any, is used. |
| **id**  integer | A `id` of the template you would like to manage. If not set then a  new template will be created with the given `name`. |
| **name**  string | A `name` of the template you would like to manage. If a template with  the given name does not exist it will be created, otherwise it will be  managed by this module. |
| **state**  string | `present` - state that is used to manage the template.  `absent` - delete the template.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **template**  string | A string containing the template contents. |
| **validate_certs**  boolean | Whether to validate the TLS/SSL certificates or not.  This parameter is ignored if `PYTHONHTTPSVERIFY` environment variable is used.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | Time to wait for the desired state to be reached before timeout, in seconds.  **Default:** `300` |

## [Attributes](one_template_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  Note that check mode always returns `changed=true` for existing templates, even if the template would not actually change. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](one_template_module.md#id5)

```yaml+jinja
- name: Fetch the TEMPLATE by id
  community.general.one_template:
    id: 6459
  register: result

- name: Print the TEMPLATE properties
  ansible.builtin.debug:
    var: result

- name: Fetch the TEMPLATE by name
  community.general.one_template:
    name: tf-prd-users-workerredis-p6379a
  register: result

- name: Create a new or update an existing TEMPLATE
  community.general.one_template:
    name: generic-opensuse
    template: |
      CONTEXT = [
        HOSTNAME = "generic-opensuse"
      ]
      CPU = "1"
      CUSTOM_ATTRIBUTE = ""
      DISK = [
        CACHE = "writeback",
        DEV_PREFIX = "sd",
        DISCARD = "unmap",
        IMAGE = "opensuse-leap-15.2",
        IMAGE_UNAME = "oneadmin",
        IO = "threads",
        SIZE = "" ]
      MEMORY = "2048"
      NIC = [
        MODEL = "virtio",
        NETWORK = "testnet",
        NETWORK_UNAME = "oneadmin" ]
      OS = [
        ARCH = "x86_64",
        BOOT = "disk0" ]
      SCHED_REQUIREMENTS = "CLUSTER_ID=\"100\""
      VCPU = "2"

- name: Delete the TEMPLATE by id
  community.general.one_template:
    id: 6459
    state: absent
```

## [Return Values](one_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group_id**  integer | template’s group id  **Returned:** when `state=present`  **Sample:** `1` |
| **group_name**  string | template’s group name  **Returned:** when `state=present`  **Sample:** `"one-users"` |
| **id**  integer | template id  **Returned:** when `state=present`  **Sample:** `153` |
| **name**  string | template name  **Returned:** when `state=present`  **Sample:** `"app1"` |
| **owner_id**  integer | template’s owner id  **Returned:** when `state=present`  **Sample:** `143` |
| **owner_name**  string | template’s owner name  **Returned:** when `state=present`  **Sample:** `"ansible-test"` |
| **template**  dictionary | the parsed template  **Returned:** when `state=present` |

### Authors

- Georg Gadinger (@nilsding)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
