---
collection: ansible
version: "6"
title: "community.network.ig_unit_information module – Get unit information from an Ingate SBC."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ig_unit_information_module.html
fetched_at: 2026-07-27T17:18:51+00:00
---
# community.network.ig_unit_information module – Get unit information from an Ingate SBC.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](ig_unit_information_module.md#ansible-collections-community-network-ig-unit-information-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.ig_unit_information`.

- [Synopsis](ig_unit_information_module.md#synopsis)
- [Requirements](ig_unit_information_module.md#requirements)
- [Parameters](ig_unit_information_module.md#parameters)
- [Notes](ig_unit_information_module.md#notes)
- [Examples](ig_unit_information_module.md#examples)
- [Return Values](ig_unit_information_module.md#return-values)

## [Synopsis](ig_unit_information_module.md#id1)

- Get unit information from an Ingate SBC.

## [Requirements](ig_unit_information_module.md#id2)

The below requirements are needed on the host that executes this module.

- ingatesdk >= 1.0.6

## [Parameters](ig_unit_information_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client**  string | A dict object containing connection details. |
| **address**  string / required | The hostname or IP address to the unit. |
| **password**  string / required | The password for the REST API user. |
| **port**  integer | Which HTTP(S) port to connect to. |
| **scheme**  string / required | Which HTTP protocol to use.  Choices:   - `"http"` - `"https"` |
| **timeout**  integer | The timeout (in seconds) for REST API requests. |
| **username**  string / required | The username of the REST API user. |
| **validate_certs**  aliases: verify_ssl  boolean | Verify the unit’s HTTPS certificate.  Choices:   - `false` - `true` ← (default) |
| **version**  string | REST API version.  Choices:   - `"v1"` ← (default) |

## [Notes](ig_unit_information_module.md#id4)

> **Note:**
>
> - This module requires that the Ingate Python SDK is installed on the host. To install the SDK use the pip command from your shell `pip install ingatesdk`.

## [Examples](ig_unit_information_module.md#id5)

```yaml+jinja
- name: Get unit information
  community.network.ig_unit_information:
    client:
      version: v1
      scheme: http
      address: 192.168.1.1
      username: alice
      password: foobar
```

## [Return Values](ig_unit_information_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **unit-information**  complex | Information about the unit  Returned: success |
| **installid**  string | The installation identifier  Returned: success  Sample: `"any"` |
| **interfaces**  string | List of interface names  Returned: success  Sample: `"eth0 eth1 eth2 eth3 eth4 eth5"` |
| **lang**  string | The unit’s language  Returned: success  Sample: `"en"` |
| **lic_email**  string | License email information  Returned: success  Sample: `"example@example.com"` |
| **lic_mac**  string | License MAC information  Returned: success  Sample: `"any"` |
| **lic_name**  string | License name information  Returned: success  Sample: `"Example Inc"` |
| **macaddr**  string | The MAC address of the first interface  Returned: success  Sample: `"52:54:00:4c:e2:07"` |
| **mode**  string | Operational mode of the unit  Returned: success  Sample: `"Siparator"` |
| **modules**  string | Installed module licenses  Returned: success  Sample: `"failover vpn sip qturn ems qos rsc voipsm"` |
| **patches**  list / elements=string | Installed patches on the unit  Returned: success  Sample: `[]` |
| **product**  string | The product name  Returned: success  Sample: `"Software SIParator/Firewall"` |
| **serial**  string | The serial number of the unit  Returned: success  Sample: `"IG-200-839-2008-0"` |
| **systemid**  string | The system identifier of the unit  Returned: success  Sample: `"IG-200-839-2008-0"` |
| **unitname**  string | The name of the unit  Returned: success  Sample: `"Testname"` |
| **version**  string | Firmware version  Returned: success  Sample: `"6.2.0-beta2"` |

### Authors

- Ingate Systems AB (@ingatesystems)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
