---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_info module – Gather information about Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_info_module.html
fetched_at: 2026-07-28T01:25:57+00:00
---
# cisco.intersight.intersight_info module – Gather information about Intersight

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
> To use it in a playbook, specify: `cisco.intersight.intersight_info`.

New in cisco.intersight 2.8

- [Synopsis](intersight_info_module.md#synopsis)
- [Parameters](intersight_info_module.md#parameters)
- [Examples](intersight_info_module.md#examples)
- [Return Values](intersight_info_module.md#return-values)

## [Synopsis](intersight_info_module.md#id1)

- Gathers information about servers in [Cisco Intersight](https://intersight.com).
- This module was called `intersight_facts` before Ansible 2.9. The usage did not change.

## [Parameters](intersight_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **server_names**  list / elements=string / required | Server names to retrieve information from.  An empty list will return all servers. |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_info_module.md#id3)

```yaml+jinja
- name: Get info for all servers
  intersight_info:
    api_private_key: ~/Downloads/SecretKey.txt
    api_key_id: 64612d300d0982/64612d300d0b00/64612d300d3650
    server_names:
- debug:
    msg: "server name {{ item.Name }}, moid {{ item.Moid }}"
  loop: "{{ intersight_servers }}"
  when: intersight_servers is defined

- name: Get info for servers by name
  intersight_info:
    api_private_key: ~/Downloads/SecretKey.txt
    api_key_id: 64612d300d0982/64612d300d0b00/64612d300d3650
    server_names:
      - SJC18-L14-UCS1-1
- debug:
    msg: "server moid {{ intersight_servers[0].Moid }}"
  when: intersight_servers[0] is defined
```

## [Return Values](intersight_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **intersight_servers**  complex | A list of Intersight Servers. See [Cisco Intersight](https://intersight.com/apidocs) for details.  **Returned:** always |
| **Moid**  string | The unique identifier of this Managed Object instance.  **Returned:** always  **Sample:** `"5978bea36ad4b000018d63dc"` |
| **Name**  string | The name of the server.  **Returned:** always  **Sample:** `"SJC18-L14-UCS1-1"` |

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
