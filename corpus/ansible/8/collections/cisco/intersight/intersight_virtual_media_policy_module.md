---
collection: ansible
version: "8"
title: "cisco.intersight.intersight_virtual_media_policy module – Virtual Media policy configuration for Cisco Intersight"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/intersight/intersight_virtual_media_policy_module.html
fetched_at: 2026-07-28T01:26:01+00:00
---
# cisco.intersight.intersight_virtual_media_policy module – Virtual Media policy configuration for Cisco Intersight

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
> To use it in a playbook, specify: `cisco.intersight.intersight_virtual_media_policy`.

New in cisco.intersight 2.10

- [Synopsis](intersight_virtual_media_policy_module.md#synopsis)
- [Parameters](intersight_virtual_media_policy_module.md#parameters)
- [Examples](intersight_virtual_media_policy_module.md#examples)
- [Return Values](intersight_virtual_media_policy_module.md#return-values)

## [Synopsis](intersight_virtual_media_policy_module.md#id1)

- Virtual Media policy configuration for Cisco Intersight.
- Used to configure Virtual Media image mappings on Cisco Intersight managed devices.
- For more information see [Cisco Intersight](https://intersight.com/apidocs).

## [Parameters](intersight_virtual_media_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key_id**  string / required | Public API Key ID associated with the private key.  If not set, the value of the INTERSIGHT_API_KEY_ID environment variable is used. |
| **api_private_key**  string / required | Filename (absolute path) or string of PEM formatted private key data to be used for Intersight API authentication.  If a string is used, Ansible vault should be used to encrypt string data.  Ex. ansible-vault encrypt_string –vault-id [tme@/Users/dsoper/Documents/vault_password_file](mailto:tme%40/Users/dsoper/Documents/vault_password_file) ‘—–BEGIN EC PRIVATE KEY—–  <your private key data>  —–END EC PRIVATE KEY—–’  If not set, the value of the INTERSIGHT_API_PRIVATE_KEY environment variable is used. |
| **api_uri**  string | URI used to access the Intersight API.  If not set, the value of the INTERSIGHT_API_URI environment variable is used.  **Default:** `"https://intersight.com/api/v1"` |
| **cdd_virtual_media**  string | CDD Virtual Media image mapping options. |
| **enable**  boolean | Enable or disable CDD image mapping.  **Choices:**   - `false` - `true` ← (default) |
| **mount_type**  string / required | Type (protocol) of network share used by the remote_hostname.  Ensure that the remote_hostname’s communication port for the mount type that you choose is accessible from the managed endpoint.  For CIFS as your mount type, ensure port 445 (which is its communication port) on the remote_hostname is accessible.  For HTTP, ensure port 80 is accessible.  For HTTPS, ensure port 443 is accessible.  For NFS, ensure port 2049 is accessible.  **Choices:**   - `"nfs"` - `"cifs"` - `"http"` - `"https"` |
| **password**  string | The password for the selected username, if required. |
| **remote_file**  string / required | Filename of the remote image.  Ex. custom_image.iso |
| **remote_hostname**  string / required | Hostname or IP address of the server hosting the virtual media image. |
| **remote_path**  string / required | Filepath (not including the filename) of the remote image.  Ex. mnt/SHARE/ISOS |
| **username**  string | The username for the specified Mount Type, if required. |
| **volume**  string / required | A user defined name of the image mounted for mapping. |
| **descrption**  aliases: descr  string | The user-defined description of the NTP policy.  Description can contain letters(a-z, A-Z), numbers(0-9), hyphen(-), period(.), colon(:), or an underscore(_). |
| **enable**  boolean | Enable or disable virtual media.  **Choices:**   - `false` - `true` ← (default) |
| **encryption**  boolean | If enabled, allows encryption of all Virtual Media communications  **Choices:**   - `false` ← (default) - `true` |
| **hdd_virtual_media**  string | HDD Virtual Media image mapping options. |
| **authentication_protocol**  string | Authentication Protocol for CIFS Mount Type |
| **enable**  boolean | Enable or disable HDD image mapping.  **Choices:**   - `false` ← (default) - `true` |
| **mount_options**  string | Mount options for the Virtual Media mapping.  For NFS, supported options are ro, rw, nolock, noexec, soft, port=VALUE, timeo=VALUE, retry=VALUE  For CIFS, supported options are soft, nounix, noserverino, guest |
| **mount_type**  string / required | Type (protocol) of network share used by the remote_hostname.  Ensure that the remote_hostname’s communication port for the mount type that you choose is accessible from the managed endpoint.  For CIFS as your mount type, ensure port 445 (which is its communication port) on the remote_hostname is accessible.  For HTTP, ensure port 80 is accessible.  For HTTPS, ensure port 443 is accessible.  For NFS, ensure port 2049 is accessible.  **Choices:**   - `"nfs"` - `"cifs"` - `"http"` - `"https"` |
| **password**  string | The password for the selected username, if required. |
| **remote_file**  string / required | Filename of the remote image.  Ex. custom_image.iso |
| **remote_hostname**  string / required | Hostname or IP address of the server hosting the virtual media image. |
| **remote_path**  string / required | Filepath (not including the filename) of the remote image.  Ex. mnt/SHARE/ISOS |
| **username**  string | The username for the specified Mount Type, if required. |
| **volume**  string / required | A user defined name of the image mounted for mapping. |
| **low_power_usb**  boolean | If enabled, the virtual drives appear on the boot selection menu after mapping the image and rebooting the host.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | The name assigned to the NTP policy.  The name must be between 1 and 62 alphanumeric characters, allowing special characters :-_. |
| **organization**  string | The name of the Organization this resource is assigned to.  Profiles and Policies that are created within a Custom Organization are applicable only to devices in the same Organization.  **Default:** `"default"` |
| **state**  string | If `present`, will verify the resource is present and will create if needed.  If `absent`, will verify the resource is absent and will delete if needed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags in Key:<user-defined key> Value:<user-defined value> format. |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Boolean control for verifying the api_uri TLS certificate  **Choices:**   - `false` - `true` ← (default) |

## [Examples](intersight_virtual_media_policy_module.md#id3)

```yaml+jinja
- name: Configure Virtual Media Policy
  cisco.intersight.intersight_virtual_media_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: lab-vmedia
    description: Virutal Media policy for lab use
    tags:
      - Key: Site
        Value: RCDN
    cdd_virtual_media:
      mount_type: nfs
      volume: nfs-cdd
      remote_hostname: 172.28.224.77
      remote_path: mnt/SHARE/ISOS/CENTOS
      remote_file: CentOS7.iso
    hdd_virtual_media:
      mount_type: nfs
      volume: nfs-hdd
      remote_hostname: 172.28.224.77
      remote_path: mnt/SHARE/ISOS/CENTOS
      remote_file: CentOS7.iso

- name: Delete Virtual Media Policy
  cisco.intersight.intersight_virtual_media_policy:
    api_private_key: "{{ api_private_key }}"
    api_key_id: "{{ api_key_id }}"
    organization: DevNet
    name: lab-vmedia
    state: absent
```

## [Return Values](intersight_virtual_media_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_repsonse**  dictionary | The API response output returned by the specified resource.  **Returned:** always  **Sample:** `{"api_response": {"Name": "lab-ntp", "ObjectType": "ntp.Policy", "Tags": [{"Key": "Site", "Value": "RCDN"}]}}` |

### Authors

- David Soper (@dsoper2)
- Sid Nath (@SidNath21)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/intersight-ansible)
- [Repository (Sources)](https://github.com/CiscoDevNet/intersight-ansible)
