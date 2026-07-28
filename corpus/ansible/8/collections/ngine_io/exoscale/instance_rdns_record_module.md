---
collection: ansible
version: "8"
title: "ngine_io.exoscale.instance_rdns_record module – Manages reverse DNS records for Exoscale compute instances."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/exoscale/instance_rdns_record_module.html
fetched_at: 2026-07-28T02:46:48+00:00
---
# ngine_io.exoscale.instance_rdns_record module – Manages reverse DNS records for Exoscale compute instances.

> **Note:**
>
> This module is part of the [ngine_io.exoscale collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/exoscale/) (version 1.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.exoscale`.
> You need further requirements to be able to use this module,
> see [Requirements](instance_rdns_record_module.md#ansible-collections-ngine-io-exoscale-instance-rdns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.exoscale.instance_rdns_record`.

New in ngine_io.exoscale 1.1.0

- [Synopsis](instance_rdns_record_module.md#synopsis)
- [Requirements](instance_rdns_record_module.md#requirements)
- [Parameters](instance_rdns_record_module.md#parameters)
- [Notes](instance_rdns_record_module.md#notes)
- [Examples](instance_rdns_record_module.md#examples)
- [Return Values](instance_rdns_record_module.md#return-values)

## [Synopsis](instance_rdns_record_module.md#id1)

- Set and unset reverse DNS record on Exoscale instance.

## [Requirements](instance_rdns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](instance_rdns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **content**  aliases: value  string | Reverse DSN name of the compute instance. Required if state=present. |
| **name**  string / required | Name of the compute instance |
| **state**  string | State of the record.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](instance_rdns_record_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](instance_rdns_record_module.md#id5)

```yaml+jinja
- name: Set the reverse DNS for a compute instance
  ngine_io.exoscale.instance_rdns_record:
    name: web-vm-1
    content: www.example.com

- name: Delete the reverse DNS for a compute instance
  ngine_io.exoscale.instance_rdns_record:
    name: web-vm-1
    state: absent
```

## [Return Values](instance_rdns_record_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **instance_rdns_domain**  string | Reverse DSN name of the compute instance  **Returned:** success |

### Authors

- Lorenz Schori (@znerol)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-exoscale/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-exoscale)
