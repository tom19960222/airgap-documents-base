---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_configuration module – Manages configuration on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_configuration_module.html
fetched_at: 2026-07-28T00:15:23+00:00
---
# ngine_io.cloudstack.cs_configuration module – Manages configuration on Apache CloudStack based clouds.

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
> see [Requirements](cs_configuration_module.md#ansible-collections-ngine-io-cloudstack-cs-configuration-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_configuration`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_configuration_module.md#synopsis)
- [Requirements](cs_configuration_module.md#requirements)
- [Parameters](cs_configuration_module.md#parameters)
- [Notes](cs_configuration_module.md#notes)
- [Examples](cs_configuration_module.md#examples)
- [Return Values](cs_configuration_module.md#return-values)

## [Synopsis](cs_configuration_module.md#id1)

- Manages global, zone, account, storage and cluster configurations.

## [Requirements](cs_configuration_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_configuration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Ensure the value for corresponding account. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **cluster**  string | Ensure the value for corresponding cluster. |
| **domain**  string | Domain the account is related to.  Only considered if *account* is used.  Default: `"ROOT"` |
| **name**  string / required | Name of the configuration. |
| **storage**  string | Ensure the value for corresponding storage pool. |
| **value**  string / required | Value of the configuration. |
| **zone**  string | Ensure the value for corresponding zone. |

## [Notes](cs_configuration_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_configuration_module.md#id5)

```yaml+jinja
- name: Ensure global configuration
  ngine_io.cloudstack.cs_configuration:
    name: router.reboot.when.outofband.migrated
    value: false

- name: Ensure zone configuration
  ngine_io.cloudstack.cs_configuration:
    name: router.reboot.when.outofband.migrated
    zone: ch-gva-01
    value: true

- name: Ensure storage configuration
  ngine_io.cloudstack.cs_configuration:
    name: storage.overprovisioning.factor
    storage: storage01
    value: 2.0

- name: Ensure account configuration
  ngine_io.cloudstack.cs_configuration:
    name: allow.public.user.templates
    value: false
    account: acme inc
    domain: customers
```

## [Return Values](cs_configuration_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account of the configuration.  Returned: success  Sample: `"admin"` |
| **category**  string | Category of the configuration.  Returned: success  Sample: `"Advanced"` |
| **cluster**  string | Cluster of the configuration.  Returned: success  Sample: `"cluster01"` |
| **description**  string | Description of the configuration.  Returned: success  Sample: `"Setup the host to do multipath"` |
| **Domain**  string | Domain of account of the configuration.  Returned: success  Sample: `"ROOT"` |
| **name**  string | Name of the configuration.  Returned: success  Sample: `"zone.vlan.capacity.notificationthreshold"` |
| **scope**  string | Scope (zone/cluster/storagepool/account) of the parameter that needs to be updated.  Returned: success  Sample: `"storagepool"` |
| **storage**  string | Storage of the configuration.  Returned: success  Sample: `"storage01"` |
| **value**  string | Value of the configuration.  Returned: success  Sample: `"0.75"` |
| **zone**  string | Zone of the configuration.  Returned: success  Sample: `"ch-gva-01"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
