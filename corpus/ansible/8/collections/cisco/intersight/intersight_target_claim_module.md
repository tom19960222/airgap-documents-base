---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_target_claim module – Target claim configuraiton for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_target_claim_module.html
fetched_at: 2026-07-28T01:26:00+00:00
---
# cisco.intersight.intersight_target_claim module – Target claim configuraiton for Cisco Intersight

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
> To use it in a playbook, specify: `cisco.intersight.intersight_target_claim`.

New in cisco.intersight 2.8

- [Synopsis](intersight_target_claim_module.md#synopsis)
- [Parameters](intersight_target_claim_module.md#parameters)
- [Examples](intersight_target_claim_module.md#examples)
- [Return Values](intersight_target_claim_module.md#return-values)

## [Synopsis](intersight_target_claim_module.md#id1)

- Target claim configuraiton for Cisco Intersight
- Used to claim or unclaim a Target from Cisco Intersight
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_target_claim_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **claim_code**  string | Claim code required for registering a new Target  Required if *state=present* |
| **device_id**  dictionary / required | Device id (serial number) of target  Targets containing multiple Target ids (e.g. IMM) can be formatted as <target1_id>&<target2_id> |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_target_claim_module.md#id3)

```yaml+jinja
- name: Claim new Target
  cisco.intersight.intersight_target_claim:
    device_id: "{{ device_id }}"
    claim_code: "{{ claim_code }}"
    state: present

- name: Delete a Target (unclaim)
  cisco.intersight.intersight_target_claim:
    device_id: "{{ device_id }}"
    state: absent
```

## [Return Values](intersight_target_claim_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"Account": {"ClassId": "mo.MoRef", "Moid": "8675309", "ObjectType": "iam.Account", "link": "https://www.intersight.com/api/v1/iam/Accounts/8675309"}, "AccountMoid": "8675309", "Ancestors": null, "ClassId": "asset.DeviceClaim", "CreateTime": "2021-05-10T17:32:13.522665238Z", "Device": {"ClassId": "mo.MoRef", "Moid": "9035768", "ObjectType": "asset.DeviceRegistration", "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/9035768"}, "DisplayNames": {"short": ["FDO241604EM&FDO24161700"]}, "DomainGroupMoid": "5b4e48a96a636d6d346cd1c5", "ModTime": "2021-05-10T17:32:13.522665238Z", "Moid": "8675309", "ObjectType": "asset.DeviceClaim", "Owners": ["90357688675309"], "PermissionResources": null, "SecurityToken": "A95486674376E", "SerialNumber": "FDO86753091&FDO86753092", "SharedScope": "", "Tags": [], "trace_id": "NB3e883980a98adace8f7b9c2409cced1a"}}` |

### Authors

- Brandon Beck (@techBeck03)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
