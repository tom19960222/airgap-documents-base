---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_facts module – Gather facts on instances of Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_facts_module.html
fetched_at: 2026-07-28T00:15:25+00:00
---
# ngine_io.cloudstack.cs_facts module – Gather facts on instances of Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_facts_module.md#ansible-collections-ngine-io-cloudstack-cs-facts-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_facts`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_facts_module.md#synopsis)
- [Requirements](cs_facts_module.md#requirements)
- [Parameters](cs_facts_module.md#parameters)
- [Examples](cs_facts_module.md#examples)
- [Return Values](cs_facts_module.md#return-values)

## [Synopsis](cs_facts_module.md#id1)

- This module fetches data from the metadata API in CloudStack. The module must be called from within the instance itself.

## [Requirements](cs_facts_module.md#id2)

The below requirements are needed on the host that executes this module.

- yaml

## [Parameters](cs_facts_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **filter**  string | Filter for a specific fact.  Choices:   - `"cloudstack_service_offering"` - `"cloudstack_availability_zone"` - `"cloudstack_public_hostname"` - `"cloudstack_public_ipv4"` - `"cloudstack_local_hostname"` - `"cloudstack_local_ipv4"` - `"cloudstack_instance_id"` - `"cloudstack_user_data"` |
| **meta_data_host**  string | Host or IP of the meta data API service.  If not set, determination by parsing the dhcp lease file. |

## [Examples](cs_facts_module.md#id4)

```yaml+jinja
# Gather all facts on instances
- name: Gather cloudstack facts
  ngine_io.cloudstack.cs_facts:

# Gather specific fact on instances
- name: Gather cloudstack facts
  ngine_io.cloudstack.cs_facts: filter=cloudstack_instance_id

# Gather specific fact on instances with a given meta_data_host
- name: Gather cloudstack facts
  ngine_io.cloudstack.cs_facts:
    filter: cloudstack_instance_id
    meta_data_host: 169.254.169.254
```

## [Return Values](cs_facts_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cloudstack_availability_zone**  string | zone the instance is deployed in.  Returned: success  Sample: `"ch-gva-2"` |
| **cloudstack_instance_id**  string | UUID of the instance.  Returned: success  Sample: `"ab4e80b0-3e7e-4936-bdc5-e334ba5b0139"` |
| **cloudstack_local_hostname**  string | local hostname of the instance.  Returned: success  Sample: `"VM-ab4e80b0-3e7e-4936-bdc5-e334ba5b0139"` |
| **cloudstack_local_ipv4**  string | local IPv4 of the instance.  Returned: success  Sample: `"185.19.28.35"` |
| **cloudstack_public_hostname**  string | public IPv4 of the router. Same as *cloudstack_public_ipv4*.  Returned: success  Sample: `"VM-ab4e80b0-3e7e-4936-bdc5-e334ba5b0139"` |
| **cloudstack_public_ipv4**  string | public IPv4 of the router.  Returned: success  Sample: `"185.19.28.35"` |
| **cloudstack_service_offering**  string | service offering of the instance.  Returned: success  Sample: `"Micro 512mb 1cpu"` |
| **cloudstack_user_data**  dictionary | data of the instance provided by users.  Returned: success  Sample: `{"bla": "foo"}` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
