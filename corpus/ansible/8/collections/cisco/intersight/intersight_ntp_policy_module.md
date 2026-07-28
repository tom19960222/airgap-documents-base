---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_ntp_policy module – NTP policy configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_ntp_policy_module.html
fetched_at: 2026-07-28T01:25:58+00:00
---
# cisco.intersight.intersight_ntp_policy module – NTP policy configuration for Cisco Intersight

> **Note:**
>
> This module is part of the [cisco.intersight collection](https://galaxy.ansible.com/ui/repo/published/cisco/intersight/) (version 1.0.27).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.intersight`.
>
> To use it in a playbook, specify: `cisco.intersight.intersight_ntp_policy`.

New in cisco.intersight 2.10

- [Synopsis](intersight_ntp_policy_module.md#synopsis)
- [Parameters](intersight_ntp_policy_module.md#parameters)
- [Examples](intersight_ntp_policy_module.md#examples)
- [Return Values](intersight_ntp_policy_module.md#return-values)

## [Synopsis](intersight_ntp_policy_module.md#id1)

- NTP policy configuration for Cisco Intersight.
- Used to configure NTP servers and timezone settings on Cisco Intersight managed devices.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_ntp_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **description**  aliases: descr  string | The user-defined description of the NTP policy.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **enable**  boolean | Enable or disable NTP.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name assigned to the NTP policy.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **ntp_servers**  list / elements=string | List of NTP servers configured on the endpoint. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  **Default:** `"default"` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **timezone**  string | Timezone of services on the endpoint. |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_ntp_policy_module.md#id3)

```yaml+jinja
- name: Configure NTP Policy
  cisco.intersight.intersight_ntp_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: lab-ntp
    description: NTP policy for lab use
    tags:
      - Key: Site
        Value: RCDN
    ntp_servers:
      - ntp.esl.cisco.com
    timezone: America/Chicago

- name: Delete NTP Policy
  cisco.intersight.intersight_ntp_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: lab-ntp
    state: absent
```

## [Return Values](intersight_ntp_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"Name": "lab-ntp", "ObjectType": "ntp.Policy", "Tags": [{"Key": "Site", "Value": "RCDN"}]}}` |

### Authors

- David Soper (@dsoper2)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
