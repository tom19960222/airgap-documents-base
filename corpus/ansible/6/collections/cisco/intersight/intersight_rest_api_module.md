---
collection: ansible
version: "6"
title: "cisco.intersight.intersight_rest_api module – REST API configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/intersight/intersight_rest_api_module.html
fetched_at: 2026-07-27T16:55:02+00:00
---
# cisco.intersight.intersight_rest_api module – REST API configuration for Cisco Intersight

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
> To use it in a playbook, specify: `cisco.intersight.intersight_rest_api`.

New in cisco.intersight 2.8

- [Synopsis](intersight_rest_api_module.md#synopsis)
- [Parameters](intersight_rest_api_module.md#parameters)
- [Examples](intersight_rest_api_module.md#examples)
- [Return Values](intersight_rest_api_module.md#return-values)

## [Synopsis](intersight_rest_api_module.md#id1)

- Direct REST API configuration for Cisco Intersight.
- All REST API resources and properties must be specified.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_rest_api_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_body**  dictionary | The paylod for API requests used to modify resources. |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  Default: `"https://intersight.com/api/v1"` |
| **query_params**  dictionary | Query parameters for the Intersight API query languange. |
| **resource_path**  string / required | Resource URI being configured related to api_uri. |
| **return_list**  boolean | If `yes`, will return a list of API results in the api_response.  By default only the 1st element of the API Results list is returned.  Can only be used with GET operations.  Choices:   - `false` ← (default) - `true` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_method**  string | The HTTP method used for update operations.  Some Intersight resources require POST operations for modifications.  Choices:   - `"patch"` ← (default) - `"post"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  Choices:   - `false` - `true` ← (default) |

## [Examples](intersight_rest_api_module.md#id3)

```yaml+jinja
- name: Configure Boot Policy
  intersight_rest_api:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    api_key_uri: "{{ api_key_uri }}"
    validate_certs: "{{ validate_certs }}"
    resource_path: /boot/PrecisionPolicies
    query_params:
      $filter: "Name eq 'vmedia-localdisk'"
    api_body: {
      "Name": "vmedia-localdisk",
      "ConfiguredBootMode": "Legacy",
      "BootDevices": [
        {
          "ObjectType": "boot.VirtualMedia",
          "Enabled": true,
          "Name": "remote-vmedia",
          "Subtype": "cimc-mapped-dvd"
        },
        {
          "ObjectType": "boot.LocalDisk",
          "Enabled": true,
          "Name": "localdisk",
          "Slot": "MRAID",
          "Bootloader": null
        }
      ],
    }
    state: present

- name: Delete Boot Policy
  intersight_rest_api:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    api_key_uri: "{{ api_key_uri }}"
    validate_certs: "{{ validate_certs }}"
    resource_path: /boot/PrecisionPolicies
    query_params:
      $filter: "Name eq 'vmedia-localdisk'"
    state: absent
```

## [Return Values](intersight_rest_api_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  Returned: always  Sample: `{"api_response": {"BootDevices": [{"Enabled": true, "Name": "remote-vmedia", "ObjectType": "boot.VirtualMedia", "Subtype": "cimc-mapped-dvd"}, {"Bootloader": null, "Enabled": true, "Name": "boot-lun", "ObjectType": "boot.LocalDisk", "Slot": "MRAID"}], "ConfiguredBootMode": "Legacy", "Name": "vmedia-localdisk", "ObjectType": "boot.PrecisionPolicy"}}` |

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
[Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
