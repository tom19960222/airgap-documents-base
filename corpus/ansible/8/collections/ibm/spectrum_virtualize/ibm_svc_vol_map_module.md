---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_vol_map module – This module manages volume mapping on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_vol_map_module.html
fetched_at: 2026-07-28T02:35:10+00:00
---
# ibm.spectrum_virtualize.ibm_svc_vol_map module – This module manages volume mapping on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_vol_map`.

New in ibm.spectrum_virtualize 1.0.0

- [Synopsis](ibm_svc_vol_map_module.md#synopsis)
- [Parameters](ibm_svc_vol_map_module.md#parameters)
- [Notes](ibm_svc_vol_map_module.md#notes)
- [Examples](ibm_svc_vol_map_module.md#examples)

## [Synopsis](ibm_svc_vol_map_module.md#id1)

- Ansible interface to manage volume mapping commands ‘mkvdiskhostmap’, ‘rmvdiskhostmap’, ‘mkvolumehostclustermap’, and ‘rmvolumehostclustermap’.

## [Parameters](ibm_svc_vol_map_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **host**  string | Specifies the host name for host mapping.  This parameter is required to create or delete a volume-to-host mapping. |
| **hostcluster**  string | Specifies the name of the host cluster for host mapping.  This parameter is required to create or delete a volume-to-hostcluster mapping. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **scsi**  integer | Specifies the SCSI logical unit number (LUN) ID to assign to a volume on the specified host or host cluster.  Applies when *state=present*. |
| **state**  string / required | Creates (`present`) or removes (`absent`) a volume mapping.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **volname**  string / required | Specifies the volume name for host or hostcluster mapping. |

## [Notes](ibm_svc_vol_map_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_vol_map_module.md#id4)

```yaml+jinja
- name: Map a volume to a host
  ibm.spectrum_virtualize.ibm_svc_vol_map:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    volname: volume0
    host: host4test
    scsi: 1
    state: present
- name: Unmap a volume from a host
  ibm.spectrum_virtualize.ibm_svc_vol_map:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    volname: volume0
    host: host4test
    state: absent
```

### Authors

- Peng Wang(@wangpww)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
