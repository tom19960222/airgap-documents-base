---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_instance_password_reset module – Allows resetting VM the default passwords on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_instance_password_reset_module.html
fetched_at: 2026-07-28T00:15:31+00:00
---
# ngine_io.cloudstack.cs_instance_password_reset module – Allows resetting VM the default passwords on Apache CloudStack based clouds.

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
> see [Requirements](cs_instance_password_reset_module.md#ansible-collections-ngine-io-cloudstack-cs-instance-password-reset-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_instance_password_reset`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_instance_password_reset_module.md#synopsis)
- [Requirements](cs_instance_password_reset_module.md#requirements)
- [Parameters](cs_instance_password_reset_module.md#parameters)
- [Notes](cs_instance_password_reset_module.md#notes)
- [Examples](cs_instance_password_reset_module.md#examples)
- [Return Values](cs_instance_password_reset_module.md#return-values)

## [Synopsis](cs_instance_password_reset_module.md#id1)

- Resets the default user account’s password on an instance.
- Requires cloud-init to be installed in the virtual machine.
- The passwordenabled flag must be set on the template associated with the VM.

## [Requirements](cs_instance_password_reset_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_instance_password_reset_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the virtual machine belongs to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Name of the domain the virtual machine belongs to. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the virtual machine belongs to. |
| **vm**  string / required | Name of the virtual machine to reset the password on. |
| **zone**  string / required | Name of the zone in which the instance is deployed. |

## [Notes](cs_instance_password_reset_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_instance_password_reset_module.md#id5)

```yaml+jinja
- name: stop the virtual machine before resetting the password
  ngine_io.cloudstack.cs_instance:
    name: myvirtualmachine
    zone: zone01
    state: stopped

- name: reset and get new default password
  ngine_io.cloudstack.cs_instance_password_reset:
    vm: myvirtualmachine
    zone: zone01
  register: root

- debug:
    msg: "new default password is {{ root.password }}"

- name: boot the virtual machine to activate the new password
  ngine_io.cloudstack.cs_instance:
    name: myvirtualmachine
    zone: zone01
    state: started
  when: root is changed
```

## [Return Values](cs_instance_password_reset_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **id**  string | ID of the virtual machine.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **password**  string | The new default password.  Returned: success  Sample: `"ahQu5nuNge3keesh"` |

### Authors

- Gregor Riepl (@onitake)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
