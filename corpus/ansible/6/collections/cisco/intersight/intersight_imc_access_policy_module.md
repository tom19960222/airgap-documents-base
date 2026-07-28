---
collection: ansible
version: "6"
title: "cisco.intersight.intersight_imc_access_policy module – IMC Access Policy configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/intersight/intersight_imc_access_policy_module.html
fetched_at: 2026-07-27T16:55:00+00:00
---
# cisco.intersight.intersight_imc_access_policy module – IMC Access Policy configuration for Cisco Intersight

> **Note:**
>
> This module is part of the [cisco.intersight collection](https://galaxy.ansible.com/cisco/intersight) (version 1.0.22).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.intersight`.
>
> To use it in a playbook, specify: `cisco.intersight.intersight_imc_access_policy`.

New in cisco.intersight 2.10

- [Synopsis](intersight_imc_access_policy_module.md#synopsis)
- [Parameters](intersight_imc_access_policy_module.md#parameters)
- [Examples](intersight_imc_access_policy_module.md#examples)
- [Return Values](intersight_imc_access_policy_module.md#return-values)

## [Synopsis](intersight_imc_access_policy_module.md#id1)

- IMC Access Policy configuration for Cisco Intersight.
- Used to configure IP addresses and VLAN used for external connectivity to Cisco IMC.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_imc_access_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  Default: `"https://intersight.com/api/v1"` |
| **descrption**  aliases: descr  string | The user-defined description of the IMC access policy.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **ip_pool**  string / required | IP Pool used to assign IP address and other required network settings. |
| **name**  string / required | The name assigned to the IMC Access Policy.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  Default: `"default"` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  Choices:   - `false` - `true` ← (default) |
| **vlan_id**  integer / required | VLAN to be used for server access over Inband network. |

## [Examples](intersight_imc_access_policy_module.md#id3)

```yaml+jinja
- name: Configure IMC Access policy
  intersight_imc_access_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: sjc02-d23-access
    description: IMC access for SJC02 rack D23
    tags:
      - Site: D23
    vlan_id: 131
    ip_pool: sjc02-d23-ext-mgmt

- name: Delete IMC Access policy
  intersight_imc_access_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: sjc02-d23-access
    state: absent
```

## [Return Values](intersight_imc_access_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  Returned: always  Sample: `{"api_response": {"Name": "sjc02-d23-access", "ObjectType": "access.Policy", "Profiles": [{"Moid": "5e4ec7ae77696e2d30840cfc", "ObjectType": "server.Profile"}, {"Moid": "5e84d78777696e2d302ec195", "ObjectType": "server.Profile"}], "Tags": [{"Key": "Site", "Value": "SJC02"}]}}` |

### Authors

- David Soper (@dsoper2)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
[Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
