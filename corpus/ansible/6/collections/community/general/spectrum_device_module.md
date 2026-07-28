---
collection: ansible
version: "6"
title: "community.general.spectrum_device module – Creates/deletes devices in CA Spectrum"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/spectrum_device_module.html
fetched_at: 2026-07-27T17:13:20+00:00
---
# community.general.spectrum_device module – Creates/deletes devices in CA Spectrum

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.spectrum_device`.

- [Synopsis](spectrum_device_module.md#synopsis)
- [Parameters](spectrum_device_module.md#parameters)
- [Notes](spectrum_device_module.md#notes)
- [Examples](spectrum_device_module.md#examples)
- [Return Values](spectrum_device_module.md#return-values)

## [Synopsis](spectrum_device_module.md#id1)

- This module allows you to create and delete devices in CA Spectrum <https://www.ca.com/us/products/ca-spectrum.html>.
- Tested on CA Spectrum 9.4.2, 10.1.1 and 10.2.1

## [Parameters](spectrum_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **agentport**  integer | UDP port used for SNMP discovery.  Default: `161` |
| **community**  string / required | SNMP community used for device discovery.  Required when *state=present*. |
| **device**  aliases: host, name  string / required | IP address of the device.  If a hostname is given, it will be resolved to the IP address. |
| **landscape**  string / required | Landscape handle of the SpectroServer to which add or remove the device. |
| **state**  string | On `present` creates the device when it does not exist.  On `absent` removes the device when it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  aliases: oneclick_url  string / required | HTTP, HTTPS URL of the Oneclick server in the form `(http|https`://host.domain[:port]). |
| **url_password**  aliases: oneclick_password  string / required | Oneclick user password. |
| **url_username**  aliases: oneclick_user  string / required | Oneclick user name. |
| **use_proxy**  boolean | if `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](spectrum_device_module.md#id3)

> **Note:**
>
> - The devices will be created inside the *Universe* container of the specified landscape.
> - All the operations will be performed only on the specified landscape.

## [Examples](spectrum_device_module.md#id4)

```yaml+jinja
- name: Add device to CA Spectrum
  local_action:
    module: spectrum_device
    device: '{{ ansible_host }}'
    community: secret
    landscape: '0x100000'
    oneclick_url: http://oneclick.example.com:8080
    oneclick_user: username
    oneclick_password: password
    state: present

- name: Remove device from CA Spectrum
  local_action:
    module: spectrum_device
    device: '{{ ansible_host }}'
    landscape: '{{ landscape_handle }}'
    oneclick_url: http://oneclick.example.com:8080
    oneclick_user: username
    oneclick_password: password
    use_proxy: false
    state: absent
```

## [Return Values](spectrum_device_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **device**  dictionary | device data when state = present  Returned: success  Sample: `{"address": "10.10.5.1", "landscape": "0x100000", "model_handle": "0x1007ab"}` |

### Authors

- Renato Orgito (@orgito)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
