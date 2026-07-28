---
collection: ansible
version: "6"
title: "infoblox.nios_modules.nios_lookup lookup – Query Infoblox NIOS objects"
source_url: https://docs.ansible.com/projects/ansible/6/collections/infoblox/nios_modules/nios_lookup_lookup.html
fetched_at: 2026-07-27T17:51:07+00:00
---
# infoblox.nios_modules.nios_lookup lookup – Query Infoblox NIOS objects

> **Note:**
>
> This lookup plugin is part of the [infoblox.nios_modules collection](https://galaxy.ansible.com/infoblox/nios_modules) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infoblox.nios_modules`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](nios_lookup_lookup.md#ansible-collections-infoblox-nios-modules-nios-lookup-lookup-requirements) for details.
>
> To use it in a playbook, specify: `infoblox.nios_modules.nios_lookup`.

New in infoblox.nios_modules 1.0.0

- [Synopsis](nios_lookup_lookup.md#synopsis)
- [Requirements](nios_lookup_lookup.md#requirements)
- [Terms](nios_lookup_lookup.md#terms)
- [Keyword parameters](nios_lookup_lookup.md#keyword-parameters)
- [Notes](nios_lookup_lookup.md#notes)
- [Examples](nios_lookup_lookup.md#examples)
- [Return Value](nios_lookup_lookup.md#return-value)

## [Synopsis](nios_lookup_lookup.md#id1)

- Uses the Infoblox WAPI API to fetch NIOS specified objects. This lookup supports adding additional keywords to filter the return data and specify the desired set of returned fields.

## [Requirements](nios_lookup_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- infoblox-client

## [Terms](nios_lookup_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The name of the network object to be returned from the Infoblox appliance. |

## [Keyword parameters](nios_lookup_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('infoblox.nios_modules.nios_lookup', key1=value1, key2=value2, ...)` and `query('infoblox.nios_modules.nios_lookup', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **extattrs**  dictionary | A dict object that is used to filter based on extensible attributes. |
| **filter**  dictionary | A dict object that is used to filter the returned objects. |
| **return_fields**  list / elements=string | The list of field names to return for the specified object. |

## [Notes](nios_lookup_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('infoblox.nios_modules.nios_lookup', term1, term2, key1=value1, key2=value2)` and `query('infoblox.nios_modules.nios_lookup', term1, term2, key1=value1, key2=value2)`

## [Examples](nios_lookup_lookup.md#id6)

```yaml+jinja
- name: fetch all networkview objects
  ansible.builtin.set_fact:
    networkviews: "{{ lookup('infoblox.nios_modules.nios_lookup', 'networkview', provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

- name: fetch the default dns view
  ansible.builtin.set_fact:
    dns_views: "{{ lookup('infoblox.nios_modules.nios_lookup', 'view', filter={'name': 'default'},
                   provider={'host': 'nios01', 'username': 'admin', 'password': 'password'}) }}"

# all of the examples below use credentials that are  set using env variables
# export INFOBLOX_HOST=nios01
# export INFOBLOX_USERNAME=admin
# export INFOBLOX_PASSWORD=admin

- name: fetch all host records and include extended attributes
  ansible.builtin.set_fact:
    host_records: "{{ lookup('infoblox.nios_modules.nios_lookup', 'record:host', return_fields=['extattrs', 'name', 'view', 'comment']}) }}"

- name: use env variables to pass credentials
  ansible.builtin.set_fact:
    networkviews: "{{ lookup('infoblox.nios_modules.nios_lookup', 'networkview') }}"

- name: get a host record
  ansible.builtin.set_fact:
    host: "{{ lookup('infoblox.nios_modules.nios_lookup', 'record:host', filter={'name': 'hostname.ansible.com'}) }}"

- name: get the authoritative zone from a non default dns view
  ansible.builtin.set_fact:
    host: "{{ lookup('infoblox.nios_modules.nios_lookup', 'zone_auth', filter={'fqdn': 'ansible.com', 'view': 'ansible-dns'}) }}"
```

## [Return Value](nios_lookup_lookup.md#id7)

| Key | Description |
| --- | --- |
| **obj_type**  list / elements=string | The object type specified in the terms argument  Returned: always |
| **obj_field**  string | One or more obj_type fields as specified by return_fields argument or the default set of fields as per the object type  Returned: success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/infobloxopen/infoblox-ansible/issues)
[Homepage](https://github.com/infobloxopen/infoblox-ansible)
[Repository (Sources)](https://github.com/infobloxopen/infoblox-ansible/tree/master)
