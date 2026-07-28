---
collection: ansible
version: "8"
title: "community.vmware.vmware_host_iscsi module – Manage the iSCSI configuration of ESXi host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_host_iscsi_module.html
fetched_at: 2026-07-28T02:00:42+00:00
---
# community.vmware.vmware_host_iscsi module – Manage the iSCSI configuration of ESXi host

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
>
> To use it in a playbook, specify: `community.vmware.vmware_host_iscsi`.

- [Synopsis](vmware_host_iscsi_module.md#synopsis)
- [Parameters](vmware_host_iscsi_module.md#parameters)
- [Notes](vmware_host_iscsi_module.md#notes)
- [Examples](vmware_host_iscsi_module.md#examples)
- [Return Values](vmware_host_iscsi_module.md#return-values)

## [Synopsis](vmware_host_iscsi_module.md#id1)

- In this module, can manage the iSCSI configuration of ESXi host

## [Parameters](vmware_host_iscsi_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **esxi_hostname**  string / required | The ESXi hostname on which to change iSCSI settings. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead.  Environment variable support added in Ansible 2.6. |
| **iscsi_config**  dictionary | The iSCSI configs.  This parameter is required if *state=present* or *state=absent*. |
| **alias**  string | The new value for the alias of the adapter.  **Default:** `""` |
| **authentication**  dictionary | CHAP authentication parent settings for iSCSI. |
| **chap_auth_enabled**  boolean | Whether to enable CHAP authentication.  **Choices:**   - `false` ← (default) - `true` |
| **chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.  **Choices:**   - `"chapDiscouraged"` - `"chapPreferred"` - `"chapRequired"` - `"chapProhibited"` ← (default) |
| **chap_name**  string | CHAP user name if CHAP is enabled.  **Default:** `""` |
| **chap_secret**  string | The secret password of CHAP if CHAP is enabled. |
| **mutual_chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.  **Choices:**   - `"chapProhibited"` ← (default) - `"chapRequired"` |
| **mutual_chap_name**  string | The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.  **Default:** `""` |
| **mutual_chap_secret**  string | The secret password of mutual CHAP if Mutual-CHAP is enabled. |
| **force**  boolean | Force port bind VMkernels to be removed.  **Choices:**   - `false` ← (default) - `true` |
| **iscsi_name**  aliases: initiator_iqn  string | The name for the iSCSI HBA adapter.  This is iSCSI qualified name. |
| **port_bind**  list / elements=string | The list of the VMkernels if use port bindings.  **Default:** `[]` |
| **send_target**  dictionary | The iSCSI dynamic target settings. |
| **address**  string / required | The IP address or hostname of the storage device. |
| **authentication**  dictionary | CHAP authentication settings of a dynamic target for iSCSI. |
| **chap_auth_enabled**  boolean | Whether to enable CHAP authentication.  **Choices:**   - `false` ← (default) - `true` |
| **chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.  **Choices:**   - `"chapDiscouraged"` - `"chapPreferred"` - `"chapRequired"` - `"chapProhibited"` ← (default) |
| **chap_inherited**  boolean | Whether or not to inherit CHAP settings from the parent settings.  **Choices:**   - `false` - `true` ← (default) |
| **chap_name**  string | CHAP user name if CHAP is enabled.  **Default:** `""` |
| **chap_secret**  string | The secret password of CHAP if CHAP is enabled. |
| **mutual_chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.  **Choices:**   - `"chapProhibited"` ← (default) - `"chapRequired"` |
| **mutual_chap_inherited**  boolean | Whether or not to inherit Mutual-CHAP settings from the parent settings.  **Choices:**   - `false` - `true` ← (default) |
| **mutual_chap_name**  string | The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.  **Default:** `""` |
| **mutual_chap_secret**  string | The secret password of mutual CHAP if Mutual-CHAP is enabled. |
| **port**  integer | The TCP port of the storage device.  If not specified, the standard default of 3260 is used.  **Default:** `3260` |
| **static_target**  dictionary | The iSCSI static target settings. |
| **address**  string / required | The IP address or hostname of the storage device. |
| **authentication**  dictionary | CHAP authentication settings of a static target for iSCSI. |
| **chap_auth_enabled**  boolean | Whether to enable CHAP authentication.  **Choices:**   - `false` ← (default) - `true` |
| **chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of CHAP if CHAP is enabled.  **Choices:**   - `"chapDiscouraged"` - `"chapPreferred"` - `"chapRequired"` - `"chapProhibited"` ← (default) |
| **chap_inherited**  boolean | Whether or not to inherit CHAP settings from the parent settings.  **Choices:**   - `false` - `true` ← (default) |
| **chap_name**  string | CHAP user name if CHAP is enabled.  **Default:** `""` |
| **chap_secret**  string | The secret password of CHAP if CHAP is enabled. |
| **mutual_chap_authentication_type**  string | The preference for CHAP or non-CHAP protocol of Mutual-CHAP if CHAP is enabled.  **Choices:**   - `"chapProhibited"` ← (default) - `"chapRequired"` |
| **mutual_chap_inherited**  boolean | Whether or not to inherit Mutual-CHAP settings from the parent settings.  **Choices:**   - `false` - `true` ← (default) |
| **mutual_chap_name**  string | The user name that the target needs to use to authenticate with the initiator if Mutual-CHAP is enabled.  **Default:** `""` |
| **mutual_chap_secret**  string | The secret password of mutual CHAP if Mutual-CHAP is enabled. |
| **iscsi_name**  string / required | The name of the iSCSI target to connect to. |
| **port**  integer | The TCP port of the storage device.  If not specified, the standard default of 3260 is used.  **Default:** `3260` |
| **vmhba_name**  string / required | The iSCSI adapter name. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead.  Environment variable support added in Ansible 2.6. |
| **port**  integer | The port number of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  Environment variable support added in Ansible 2.6.  **Default:** `443` |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead.  This feature depends on a version of pyvmomi greater than v6.7.1.2018.12 |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **state**  string | If set to `present`, add the iSCSI target or the bind ports if they are not existing.  If set to `present`, update the iSCSI settings if they already exist and occur change.  If set to `absent`, remove the iSCSI target or the bind ports if they are existing.  If set to (enabled), enable the iSCSI of ESXi if the iSCSI is disabled.  If set to (disabled), disable the iSCSI of ESXi if the iSCSI is enabled.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disabled"` |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter or ESXi server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead.  Environment variable support added in Ansible 2.6. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  Environment variable support added in Ansible 2.6.  If set to `true`, please make sure Python >= 2.7.9 is installed on the given machine.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](vmware_host_iscsi_module.md#id3)

> **Note:**
>
> - All modules requires API write access and hence is not supported on a free ESXi license.

## [Examples](vmware_host_iscsi_module.md#id4)

```yaml+jinja
- name: Enable iSCSI of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    state: enabled

- name: Add a dynamic target to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      send_target:
        address: "{{ send_target_address }}"
    state: present

- name: Add a static target to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      static_target:
        iscsi_name: iqn.2011-08.com.xxxxxxx:as6104t-8c3e9d.target001
        address: "{{ send_target_address }}"
    state: present

- name: Add VMKernels to iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      port_bind:
        - vmk0
        - vmk1
    state: present

- name: Use CHAP authentication
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      authentication:
        chap_auth_enabled: true
        chap_authentication_type: chapPreferred
        chap_name: chap_user_name
        chap_secret: secret
    state: present

- name: Remove a dynamic target from iSCSI config of ESXi
  community.vmware.vmware_host_iscsi:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    esxi_hostname: "{{ esxi_hostname }}"
    iscsi_config:
      vmhba_name: vmhba65
      send_target:
        address: "{{ send_target_address }}"
    state: absent
```

## [Return Values](vmware_host_iscsi_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **iscsi_properties**  dictionary | Parameter return when system defaults config is changed.  **Returned:** changed  **Sample:** `{"iscsi_alias": "", "iscsi_authentication_properties": {"_vimtype": "vim.host.InternetScsiHba.AuthenticationProperties", "chapAuthEnabled": false, "chapAuthenticationType": "chapProhibited", "chapInherited": null, "chapName": "", "chapSecret": "XXXXXXXXXXXXXXXXXXXXX", "mutualChapAuthenticationType": "chapProhibited", "mutualChapInherited": null, "mutualChapName": "XXXXXXXXXXXXXXXXXXXXX", "mutualChapSecret": ""}, "iscsi_enabled": true, "iscsi_name": "", "iscsi_send_targets": [], "iscsi_static_targets": [], "port_bind": [], "vmhba_name": "vmhba65"}` |

### Authors

- sky-joker (@sky-joker)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
