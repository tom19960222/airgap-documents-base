---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_ip_address module – Manages public IP address associations on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_ip_address_module.html
fetched_at: 2026-07-28T02:45:56+00:00
---
# ngine_io.cloudstack.cs_ip_address module – Manages public IP address associations on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_ip_address_module.md#ansible-collections-ngine-io-cloudstack-cs-ip-address-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_ip_address`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_ip_address_module.md#synopsis)
- [Requirements](cs_ip_address_module.md#requirements)
- [Parameters](cs_ip_address_module.md#parameters)
- [Notes](cs_ip_address_module.md#notes)
- [Examples](cs_ip_address_module.md#examples)
- [Return Values](cs_ip_address_module.md#return-values)

## [Synopsis](cs_ip_address_module.md#id1)

- Acquires and associates a public IP to an account or project.
- Due to API limitations this is not an idempotent call, so be sure to only conditionally call this when *state=present*.
- Tagging the IP address can also make the call idempotent.

## [Requirements](cs_ip_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_ip_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the IP address is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **domain**  string | Domain the IP address is related to. |
| **ip_address**  string | Public IP address.  Required if *state=absent* and *tags* is not set. |
| **network**  string | Network the IP address is related to.  Mutually exclusive with *vpc*. |
| **poll_async**  boolean | Poll async jobs until job has finished.  **Choices:**   - `false` - `true` ← (default) |
| **project**  string | Name of the project the IP address is related to. |
| **state**  string | State of the IP address.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  Tags can be used as an unique identifier for the IP Addresses.  In this case, at least one of them must be unique to ensure idempotency. |
| **vpc**  string | VPC the IP address is related to.  Mutually exclusive with *network*. |
| **zone**  string / required | Name of the zone in which the IP address is in. |

## [Notes](cs_ip_address_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_ip_address_module.md#id5)

```yaml+jinja
- name: Associate an IP address conditionally
  ngine_io.cloudstack.cs_ip_address:
    network: My Network
    zone: zone01
  register: ip_address
  when: instance.public_ip is undefined

- name: Disassociate an IP address
  ngine_io.cloudstack.cs_ip_address:
    ip_address: 1.2.3.4
    zone: zone01
    state: absent

- name: Associate an IP address with tags
  ngine_io.cloudstack.cs_ip_address:
    network: My Network
    zone: zone01
    tags:
      - key: myCustomID
        value: 5510c31a-416e-11e8-9013-02000a6b00bf
  register: ip_address

- name: Disassociate an IP address with tags
  ngine_io.cloudstack.cs_ip_address:
    state: absent
    zone: zone01
    tags:
      - key: myCustomID
        value: 5510c31a-416e-11e8-9013-02000a6b00bf
```

## [Return Values](cs_ip_address_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the IP address is related to.  **Returned:** success  **Sample:** `"example account"` |
| **domain**  string | Domain the IP address is related to.  **Returned:** success  **Sample:** `"example domain"` |
| **id**  string | UUID of the Public IP address.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **ip_address**  string | Public IP address.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **project**  string | Name of project the IP address is related to.  **Returned:** success  **Sample:** `"Production"` |
| **tags**  dictionary | List of resource tags associated with the IP address.  **Returned:** success  **Sample:** `"[ { \"key\": \"myCustomID\", \"value\": \"5510c31a-416e-11e8-9013-02000a6b00bf\" } ]"` |
| **zone**  string | Name of zone the IP address is related to.  **Returned:** success  **Sample:** `"ch-gva-2"` |

### Authors

- Darren Worrall (@dazworrall)
- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
