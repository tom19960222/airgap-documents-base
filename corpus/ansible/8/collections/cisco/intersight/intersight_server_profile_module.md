---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_server_profile module – Server Profile configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_server_profile_module.html
fetched_at: 2026-07-28T01:26:00+00:00
---
# cisco.intersight.intersight_server_profile module – Server Profile configuration for Cisco Intersight

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
> To use it in a playbook, specify: `cisco.intersight.intersight_server_profile`.

New in cisco.intersight 2.10

- [Synopsis](intersight_server_profile_module.md#synopsis)
- [Parameters](intersight_server_profile_module.md#parameters)
- [Examples](intersight_server_profile_module.md#examples)
- [Return Values](intersight_server_profile_module.md#return-values)

## [Synopsis](intersight_server_profile_module.md#id1)

- Server Profile configuration for Cisco Intersight.
- Used to configure Server Profiles with assigned servers and server policies.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_server_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **assigned_server**  string | Managed Obect ID (MOID) of assigned server.  Option can be omitted if user wishes to assign server later. |
| **boot_order_policy**  string | Name of Boot Order Policy to associate with this profile. |
| **description**  aliases: descr  string | The user-defined description of the Server Profile.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **imc_access_policy**  string | Name of IMC Access Policy to associate with this profile. |
| **lan_connectivity_policy**  string | Name of LAN Connectivity Policy to associate with this profile. |
| **local_user_policy**  string | Name of Local User Policy to associate with this profile. |
| **name**  string / required | The name assigned to the Server Profile.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **ntp_policy**  string | Name of NTP Policy to associate with this profile. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  **Default:** `"default"` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **storage_policy**  string | Name of Storage Policy to associate with this profile. |
| **tags**  string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **target_platform**  string | The platform for which the server profile is applicable.  Can either be a server that is operating in Standalone mode or which is attached to a Fabric Interconnect (FIAttached) managed by Intersight.  **Choices:**   - `"Standalone"` ← (default) - `"FIAttached"` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |
| **virtual_media_policy**  string | Name of Virtual Media Policy to associate with this profile. |

## [Examples](intersight_server_profile_module.md#id3)

```yaml+jinja
- name: Configure Server Profile
  cisco.intersight.intersight_server_profile:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: SP-Server1
    target_platform: FIAttached
    tags:
      - Key: Site
        Value: SJC02
    description: Profile for Server1
    assigned_server: 5e3b517d6176752d319a9999
    boot_order_policy: COS-Boot
    imc_access_policy: sjc02-d23-access
    lan_connectivity_policy: sjc02-d23-lan
    local_user_policy: guest-admin
    ntp_policy: lab-ntp
    storage_policy: storage
    virtual_media_policy: COS-VM

- name: Delete Server Profile
  cisco.intersight.intersight_server_profile:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    name: SP-Server1
    state: absent
```

## [Return Values](intersight_server_profile_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"AssignedServer": {"Moid": "5e3b517d6176752d319a0881", "ObjectType": "compute.Blade"}, "Name": "SP-IMM-6454-D23-1-1", "ObjectType": "server.Profile", "Tags": [{"Key": "Site", "Value": "SJC02"}], "TargetPlatform": "FIAttached", "Type": "instance"}}` |

### Authors

- David Soper (@dsoper2)
- Sid Nath (@SidNath21)
- Tse Kai “Kevin” Chan (@BrightScale)
- Soma Tummala (@SOMATUMMALA21)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
