---
collection: ansible
version: "8"
title: "theforeman.foreman.hostgroup module – Manage Hostgroups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/hostgroup_module.html
fetched_at: 2026-07-28T02:56:04+00:00
---
# theforeman.foreman.hostgroup module – Manage Hostgroups

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
> see [Requirements](hostgroup_module.md#ansible-collections-theforeman-foreman-hostgroup-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.hostgroup`.

New in theforeman.foreman 1.0.0

- [Synopsis](hostgroup_module.md#synopsis)
- [Requirements](hostgroup_module.md#requirements)
- [Parameters](hostgroup_module.md#parameters)
- [Attributes](hostgroup_module.md#attributes)
- [Examples](hostgroup_module.md#examples)
- [Return Values](hostgroup_module.md#return-values)

## [Synopsis](hostgroup_module.md#id1)

- Create, update, and delete Hostgroups

Aliases: foreman_hostgroup

## [Requirements](hostgroup_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](hostgroup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activation_keys**  string | Activation Keys used for deployment.  Comma separated list.  Only available for Katello installations. |
| **ansible_roles**  list / elements=string  *added in theforeman.foreman 2.1.0* | A list of ansible roles to associate with the hostgroup.  The foreman-ansible plugin must be installed to use this parameter. |
| **architecture**  string | Architecture name |
| **compute_profile**  string | Compute profile name |
| **compute_resource**  string | Compute resource name |
| **config_groups**  list / elements=string | Config groups list |
| **content_source**  string | Content Source (Smart Proxy with Content) name.  Only available for Katello installations. |
| **content_view**  string | Content view.  Only available for Katello installations. |
| **description**  string | Description of hostgroup |
| **domain**  string | Domain name |
| **environment**  string | Puppet environment name |
| **kickstart_repository**  string | Kickstart repository name.  You need to provide this to use the “Synced Content” feature.  Mutually exclusive with *medium*.  Only available for Katello installations. |
| **lifecycle_environment**  string | Lifecycle environment.  Only available for Katello installations. |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **medium**  aliases: media  string | Medium name  Mutually exclusive with *kickstart_repository*. |
| **name**  string / required | Name of hostgroup |
| **openscap_proxy**  string | OpenSCAP proxy name.  Only available when the OpenSCAP plugin is installed. |
| **operatingsystem**  string | Operating systems are looked up by their title which is composed as “<name> <major>.<minor>”.  You can omit the version part as long as you only have one operating system by that name. |
| **organization**  string | Organization for scoped resources attached to the hostgroup.  Only used for Katello installations.  This organization will implicitly be added to the *organizations* parameter if needed. |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **parameters**  list / elements=dictionary | Hostgroup specific host parameters |
| **name**  string / required | Name of the parameter |
| **parameter_type**  string | Type of the parameter  **Choices:**   - `"string"` ← (default) - `"boolean"` - `"integer"` - `"real"` - `"array"` - `"hash"` - `"yaml"` - `"json"` |
| **value**  any / required | Value of the parameter |
| **parent**  string | Hostgroup parent name |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **ptable**  string | Partition table name |
| **puppet_ca_proxy**  string | Puppet CA proxy name |
| **puppet_proxy**  string | Puppet server proxy name |
| **puppetclasses**  list / elements=string | List of puppet classes to include in this host group. Must exist for hostgroup’s puppet environment. |
| **pxe_loader**  string | PXE Bootloader  **Choices:**   - `"PXELinux BIOS"` - `"PXELinux UEFI"` - `"Grub UEFI"` - `"Grub2 BIOS"` - `"Grub2 ELF"` - `"Grub2 UEFI"` - `"Grub2 UEFI SecureBoot"` - `"Grub2 UEFI HTTP"` - `"Grub2 UEFI HTTPS"` - `"Grub2 UEFI HTTPS SecureBoot"` - `"iPXE Embedded"` - `"iPXE UEFI HTTP"` - `"iPXE Chain BIOS"` - `"iPXE Chain UEFI"` - `"None"` |
| **realm**  string | Realm name |
| **root_pass**  string | Root password.  Will result in the entity always being updated, as the current password cannot be retrieved. |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subnet**  string | IPv4 Subnet name |
| **subnet6**  string | IPv6 Subnet name |
| **updated_name**  string | New name of hostgroup. When this parameter is set, the module will not be idempotent. |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](hostgroup_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](hostgroup_module.md#id5)

```yaml+jinja
- name: "Create a Hostgroup"
  theforeman.foreman.hostgroup:
    name: "new_hostgroup"
    architecture: "architecture_name"
    operatingsystem: "operatingsystem_name"
    medium: "media_name"
    ptable: "Partition_table_name"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: "Update a Hostgroup"
  theforeman.foreman.hostgroup:
    name: "new_hostgroup"
    architecture: "updated_architecture_name"
    operatingsystem: "updated_operatingsystem_name"
    organizations:
      - Org One
      - Org Two
    locations:
      - Loc One
      - Loc Two
      - Loc One/Nested loc
    medium: "updated_media_name"
    ptable: "updated_Partition_table_name"
    root_pass: "password"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: "My nested hostgroup"
  theforeman.foreman.hostgroup:
    parent: "new_hostgroup"
    name: "my nested hostgroup"

- name: "My hostgroup with some proxies"
  theforeman.foreman.hostgroup:
    name: "my hostgroup"
    environment: production
    puppet_proxy: puppet-proxy.example.com
    puppet_ca_proxy: puppet-proxy.example.com
    openscap_proxy: openscap-proxy.example.com

- name: "My katello related hostgroup"
  theforeman.foreman.hostgroup:
    organization: "My Org"
    name: "kt hostgroup"
    content_source: capsule.example.com
    lifecycle_environment: "Production"
    content_view: "My content view"
    parameters:
      - name: "kt_activation_keys"
        value: "my_prod_ak"

- name: "Delete a Hostgroup"
  theforeman.foreman.hostgroup:
    name: "new_hostgroup"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent
```

## [Return Values](hostgroup_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **hostgroups**  list / elements=dictionary | List of hostgroups.  **Returned:** success |

### Authors

- Manisha Singhal (@Manisha15) ATIX AG
- Baptiste Agasse (@bagasse)

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
