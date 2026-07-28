---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_user module – Manages users on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_user_module.html
fetched_at: 2026-07-28T00:15:51+00:00
---
# ngine_io.cloudstack.cs_user module – Manages users on Apache CloudStack based clouds.

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
> see [Requirements](cs_user_module.md#ansible-collections-ngine-io-cloudstack-cs-user-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_user`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_user_module.md#synopsis)
- [Requirements](cs_user_module.md#requirements)
- [Parameters](cs_user_module.md#parameters)
- [Notes](cs_user_module.md#notes)
- [Examples](cs_user_module.md#examples)
- [Return Values](cs_user_module.md#return-values)

## [Synopsis](cs_user_module.md#id1)

- Create, update, disable, lock, enable and remove users.

## [Requirements](cs_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the user will be created under.  Required on *state=present*. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the user is related to.  Default: `"ROOT"` |
| **email**  string | Email of the user.  Required on *state=present*. |
| **first_name**  string | First name of the user.  Required on *state=present*. |
| **keys_registered**  boolean | If API keys of the user should be generated.  Note: Keys can not be removed by the API again.  Choices:   - `false` ← (default) - `true` |
| **last_name**  string | Last name of the user.  Required on *state=present*. |
| **password**  string | Password of the user to be created.  Required on *state=present*.  Only considered on creation and will not be updated if user exists. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **state**  string | State of the user.  `unlocked` is an alias for `enabled`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` - `"locked"` - `"unlocked"` |
| **timezone**  string | Timezone of the user. |
| **username**  string / required | Username of the user. |

## [Notes](cs_user_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_user_module.md#id5)

```yaml+jinja
- name: Create an user in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_user:
    account: developers
    username: johndoe
    password: S3Cur3
    last_name: Doe
    first_name: John
    email: john.doe@example.com
    domain: CUSTOMERS

- name: Lock an existing user in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_user:
    username: johndoe
    domain: CUSTOMERS
    state: locked

- name: Disable an existing user in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_user:
    username: johndoe
    domain: CUSTOMERS
    state: disabled

- name: Enable/unlock an existing user in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_user:
    username: johndoe
    domain: CUSTOMERS
    state: enabled

- name: Remove an user in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_user:
    name: customer_xy
    domain: CUSTOMERS
    state: absent
```

## [Return Values](cs_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account name of the user.  Returned: success  Sample: `"developers"` |
| **account_type**  string | Type of the account.  Returned: success  Sample: `"user"` |
| **created**  string | Date the user was created.  Returned: success  Sample: `"Doe"` |
| **domain**  string | Domain the user is related.  Returned: success  Sample: `"ROOT"` |
| **email**  string | Emailof the user.  Returned: success  Sample: `"john.doe@example.com"` |
| **fist_name**  string | First name of the user.  Returned: success  Sample: `"John"` |
| **id**  string | UUID of the user.  Returned: success  Sample: `"87b1e0ce-4e01-11e4-bb66-0050569e64b8"` |
| **last_name**  string | Last name of the user.  Returned: success  Sample: `"Doe"` |
| **state**  string | State of the user.  Returned: success  Sample: `"enabled"` |
| **timezone**  string | Timezone of the user.  Returned: success  Sample: `"enabled"` |
| **user_api_key**  string | API key of the user.  Returned: success  Sample: `"JLhcg8VWi8DoFqL2sSLZMXmGojcLnFrOBTipvBHJjySODcV4mCOo29W2duzPv5cALaZnXj5QxDx3xQfaQt3DKg"` |
| **user_api_secret**  string | API secret of the user.  Returned: success  Sample: `"FUELo3LB9fa1UopjTLPdqLv_6OXQMJZv9g9N4B_Ao3HFz8d6IGFCV9MbPFNM8mwz00wbMevja1DoUNDvI8C9-g"` |
| **username**  string | Username of the user.  Returned: success  Sample: `"johndoe"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
