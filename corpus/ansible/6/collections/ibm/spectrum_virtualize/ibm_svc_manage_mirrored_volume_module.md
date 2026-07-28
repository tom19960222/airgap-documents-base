---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume module – This module manages mirrored volumes on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_svc_manage_mirrored_volume_module.html
fetched_at: 2026-07-27T17:50:32+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume module – This module manages mirrored volumes on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ibm/spectrum_virtualize) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume`.

New in ibm.spectrum_virtualize 1.4.0

- [Synopsis](ibm_svc_manage_mirrored_volume_module.md#synopsis)
- [Parameters](ibm_svc_manage_mirrored_volume_module.md#parameters)
- [Notes](ibm_svc_manage_mirrored_volume_module.md#notes)
- [Examples](ibm_svc_manage_mirrored_volume_module.md#examples)

## [Synopsis](ibm_svc_manage_mirrored_volume_module.md#id1)

- Ansible interface to manage ‘mkvolume’, ‘addvolumecopy’, ‘rmvolumecopy’, and ‘rmvolume’ volume commands.

## [Parameters](ibm_svc_manage_mirrored_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **compressed**  boolean | Specifies if the volume to be created is compressed.  Choices:   - `false` - `true` |
| **deduplicated**  boolean | Specifies if the volume to be created is deduplicated.  Choices:   - `false` - `true` |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **grainsize**  string | Specifies the grain size (in KB) to use when creating the HyperSwap volume. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name to assign to the new volume. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **poolA**  string | Specifies the name of first storage pool to be used when creating a mirrored volume. |
| **poolB**  string | Specifies the name of second storage pool to be used when creating a mirrored volume. |
| **rsize**  string | Specifies the rsize (buffersize) in %. Defines how much physical space is initially allocated to the thin-provisioned or compressed volume. |
| **size**  string | Specifies the size of mirrored volume in MB. This can also be used to resize a mirrored volume. When resizing, only mandatory parameters can be passed. |
| **state**  string / required | Creates (`present`) or removes (`absent`) a mirrored volume.  Choices:   - `"absent"` - `"present"` |
| **thin**  boolean | Specifies if the volume to be created is thin-provisioned.  Choices:   - `false` - `true` |
| **token**  string  added in ibm.spectrum_virtualize 1.5.0 | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **type**  string | Specifies the desired volume type.  When the type is `local hyperswap`, a HyperSwap volume gets created.  When the type is `standard` and values for *PoolA* and *PoolB* arguments are also specified, a “standard mirror” volume gets created.  If a “standard” mirrored volume exists and either *PoolA* or *PoolB* is specified, the mirrored volume gets converted to a standard volume.  Choices:   - `"local hyperswap"` - `"standard"` |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_mirrored_volume_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_mirrored_volume_module.md#id4)

```yaml+jinja
- name: Create a HyperSwap volume
  ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    type: "local hyperswap"
    name: "vol1"
    state: present
    poolA: "pool1"
    poolB: "pool2"
    size: "1024"
- name: Create a thin-provisioned HyperSwap volume
  ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    type: "local hyperswap"
    name: "vol2"
    state: present
    poolA: "pool1"
    poolB: "pool2"
    size: "1024"
    thin: true
- name: Delete a mirrored volume
  ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: "vol2"
    state: absent
- name: Create a standard mirror volume
  block:
    - name: Create Volume
      ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume:
        clustername: "{{clustername}}"
        username: "{{username}}"
        password: "{{password}}"
        log_path: /tmp/playbook.debug
        name: "vol4"
        state: present
        type: "standard"
        poolA: "pool1"
        poolB: "pool3"
- name: Resize an existing mirrored volume
  block:
    - name: Resize an existing mirrored volume
      ibm.spectrum_virtualize.ibm_svc_manage_mirrored_volume:
        clustername: "{{clustername}}"
        username: "{{username}}"
        password: "{{password}}"
        log_path: /tmp/playbook.debug
        name: "vol1"
        state: present
        size: "{{new_size}}"
```

### Authors

- Rohit Kumar(@rohitk-github)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
