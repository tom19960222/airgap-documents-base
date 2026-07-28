---
collection: ansible
version: "8"
title: "inspur.ispim.edit_ldap module – Set ldap information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_ldap_module.html
fetched_at: 2026-07-28T02:36:41+00:00
---
# inspur.ispim.edit_ldap module – Set ldap information

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/ui/repo/published/inspur/ispim/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](edit_ldap_module.md#ansible-collections-inspur-ispim-edit-ldap-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_ldap`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_ldap_module.md#synopsis)
- [Requirements](edit_ldap_module.md#requirements)
- [Parameters](edit_ldap_module.md#parameters)
- [Notes](edit_ldap_module.md#notes)
- [Examples](edit_ldap_module.md#examples)
- [Return Values](edit_ldap_module.md#return-values)

## [Synopsis](edit_ldap_module.md#id1)

- Set ldap information on Inspur server.

## [Requirements](edit_ldap_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_ldap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Server Address. |
| **attr**  string | Attribute of User Login.  **Choices:**   - `"cn"` - `"uid"` |
| **base**  string | Search Base,  Search base is a string of 4 to 64 alpha-numeric characters;  It must start with an alphabetical character;  Special Symbols like dot(.), comma(,), hyphen(-), underscore(_), equal-to(=) are allowed. |
| **ca**  string | CA certificate file path.  Required when *encry=StartTLS*. |
| **ce**  string | Certificate file path.  Required when *encry=StartTLS*. |
| **cn**  string | Common name type.  Required when *encry=StartTLS*.  **Choices:**   - `"ip"` - `"fqdn"` |
| **code**  string | Password.  Required when *enable=enable*. |
| **dn**  string | Bind DN.  Bind DN is a string of 4 to 64 alpha-numeric characters;  It must start with an alphabetical character;  Special Symbols like dot(.), comma(,), hyphen(-), underscore(_), equal-to(=) are allowed. |
| **enable**  string | LDAP/E-Directory Authentication Status.  **Choices:**   - `"enable"` - `"disable"` |
| **encry**  string | Encryption Type.  **Choices:**   - `"no"` - `"SSL"` - `"StartTLS"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **pk**  string | Private Key file path.  Required when *encry=StartTLS*. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **server_port**  integer | Server Port. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_ldap_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_ldap_module.md#id5)

```yaml+jinja
- name: Ldap test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set ldap information"
    inspur.ispim.edit_ldap:
      enable: "disable"
      provider: "{{ ism }}"

  - name: "Set ldap information"
    inspur.ispim.edit_ldap:
      enable: "enable"
      encry: "SSL"
      address: "100.2.2.2"
      server_port: 389
      dn: "cn=manager,ou=login,dc=domain,dc=com"
      code: "123456"
      base: "cn=manager"
      attr: "uid"
      provider: "{{ ism }}"
```

## [Return Values](edit_ldap_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ispim)

### Collection links

- [Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
- [Repository (Sources)](https://github.com/ispim/inspur.ispim)
