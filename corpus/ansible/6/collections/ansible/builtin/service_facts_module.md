---
collection: ansible
version: "6"
title: "ansible.builtin.service_facts module – Return service state information as fact data"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/service_facts_module.html
fetched_at: 2026-07-27T16:44:07+00:00
---
# ansible.builtin.service_facts module – Return service state information as fact data

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `service_facts` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](service_facts_module.md#synopsis)
- [Requirements](service_facts_module.md#requirements)
- [Attributes](service_facts_module.md#attributes)
- [Notes](service_facts_module.md#notes)
- [Examples](service_facts_module.md#examples)
- [Returned Facts](service_facts_module.md#returned-facts)

## [Synopsis](service_facts_module.md#id1)

- Return service state information as fact data for various service management utilities.

## [Requirements](service_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- Any of the following supported init systems: systemd, sysv, upstart, openrc, AIX SRC

## [Attributes](service_facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **facts** | Support: full | Action returns an `ansible_facts` dictionary that will update existing host facts |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [Notes](service_facts_module.md#id4)

> **Note:**
>
> - When accessing the `ansible_facts.services` facts collected by this module, it is recommended to not use “dot notation” because services can have a `-` character in their name which would result in invalid “dot notation”, such as `ansible_facts.services.zuul-gateway`. It is instead recommended to using the string value of the service name as the key in order to obtain the fact data value like `ansible_facts.services['zuul-gateway']`
> - AIX SRC was added in version 2.11.

## [Examples](service_facts_module.md#id5)

```yaml+jinja
- name: Populate service facts
  ansible.builtin.service_facts:

- name: Print service facts
  ansible.builtin.debug:
    var: ansible_facts.services
```

## [Returned Facts](service_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **services**  complex | States of the services with service name as key.  Returned: always |
| **name**  string | Name of the service.  Returned: always  Sample: `"arp-ethers.service"` |
| **source**  string | Init system of the service.  One of `rcctl`, `systemd`, `sysv`, `upstart`, `src`.  Returned: always  Sample: `"sysv"` |
| **state**  string | State of the service.  This commonly includes (but is not limited to) the following: `failed`, `running`, `stopped` or `unknown`.  Depending on the used init system additional states might be returned.  Returned: always  Sample: `"running"` |
| **status**  string | State of the service.  Either `enabled`, `disabled`, `static`, `indirect` or `unknown`.  Returned: systemd systems or RedHat/SUSE flavored sysvinit/upstart or OpenBSD  Sample: `"enabled"` |

### Authors

- Adam Miller (@maxamillion)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
