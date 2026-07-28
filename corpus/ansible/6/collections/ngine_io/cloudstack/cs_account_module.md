---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_account module – Manages accounts on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_account_module.html
fetched_at: 2026-07-28T00:15:20+00:00
---
# ngine_io.cloudstack.cs_account module – Manages accounts on Apache CloudStack based clouds.

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
> see [Requirements](cs_account_module.md#ansible-collections-ngine-io-cloudstack-cs-account-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_account`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_account_module.md#synopsis)
- [Requirements](cs_account_module.md#requirements)
- [Parameters](cs_account_module.md#parameters)
- [Notes](cs_account_module.md#notes)
- [Examples](cs_account_module.md#examples)
- [Return Values](cs_account_module.md#return-values)

## [Synopsis](cs_account_module.md#id1)

- Create, disable, lock, enable and remove accounts.

## [Requirements](cs_account_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_account_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_type**  string | Type of the account.  Choices:   - `"user"` ← (default) - `"root_admin"` - `"domain_admin"` |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the account is related to.  Default: `"ROOT"` |
| **email**  string | Email of the user to be created if account did not exist.  Required on *state=present* if *ldap_domain* is not set. |
| **first_name**  string | First name of the user to be created if account did not exist.  Required on *state=present* if *ldap_domain* is not set. |
| **last_name**  string | Last name of the user to be created if account did not exist.  Required on *state=present* if *ldap_domain* is not set. |
| **ldap_domain**  string | Name of the LDAP group or OU to bind.  If set, account will be linked to LDAP. |
| **ldap_type**  string | Type of the ldap name. GROUP or OU, defaults to GROUP.  Choices:   - `"GROUP"` ← (default) - `"OU"` |
| **name**  string / required | Name of account. |
| **network_domain**  string | Network domain of the account. |
| **password**  string | Password of the user to be created if account did not exist.  Required on *state=present* if *ldap_domain* is not set. |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **role**  string | Creates the account under the specified role name or id. |
| **state**  string | State of the account.  `unlocked` is an alias for `enabled`.  Choices:   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` - `"locked"` - `"unlocked"` |
| **timezone**  string | Timezone of the user to be created if account did not exist. |
| **username**  string | Username of the user to be created if account did not exist.  Required on *state=present*. |

## [Notes](cs_account_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_account_module.md#id5)

```yaml+jinja
- name: create an account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    username: customer_xy
    password: S3Cur3
    last_name: Doe
    first_name: John
    email: john.doe@example.com
    domain: CUSTOMERS
    role: Domain Admin

- name: Lock an existing account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    domain: CUSTOMERS
    state: locked

- name: Disable an existing account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    domain: CUSTOMERS
    state: disabled

- name: Enable an existing account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    domain: CUSTOMERS
    state: enabled

- name: Remove an account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    domain: CUSTOMERS
    state: absent

- name: Create a single user LDAP account in domain 'CUSTOMERS'
  ngine_io.cloudstack.cs_account:
    name: customer_xy
    username: customer_xy
    domain: CUSTOMERS
    ldap_domain: cn=customer_xy,cn=team_xy,ou=People,dc=domain,dc=local

- name: Create a LDAP account in domain 'CUSTOMERS' and bind it to a LDAP group
  ngine_io.cloudstack.cs_account:
    name: team_xy
    username: customer_xy
    domain: CUSTOMERS
    ldap_domain: cn=team_xy,ou=People,dc=domain,dc=local
```

## [Return Values](cs_account_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_type**  string | Type of the account.  Returned: success  Sample: `"user"` |
| **domain**  string | Domain the account is related.  Returned: success  Sample: `"ROOT"` |
| **id**  string | UUID of the account.  Returned: success  Sample: `"87b1e0ce-4e01-11e4-bb66-0050569e64b8"` |
| **name**  string | Name of the account.  Returned: success  Sample: `"linus@example.com"` |
| **network_domain**  string | Network domain of the account.  Returned: success  Sample: `"example.local"` |
| **role**  string | The role name of the account  Returned: success  Sample: `"Domain Admin"` |
| **state**  string | State of the account.  Returned: success  Sample: `"enabled"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
