---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_svc_manage_portset module – This module manages portset configuration on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_svc_manage_portset_module.html
fetched_at: 2026-07-27T17:50:34+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_portset module – This module manages portset configuration on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_portset`.

New in ibm.spectrum_virtualize 1.8.0

- [Synopsis](ibm_svc_manage_portset_module.md#synopsis)
- [Parameters](ibm_svc_manage_portset_module.md#parameters)
- [Notes](ibm_svc_manage_portset_module.md#notes)
- [Examples](ibm_svc_manage_portset_module.md#examples)

## [Synopsis](ibm_svc_manage_portset_module.md#id1)

- Ansible interface to manage IP portsets ‘mkportset’, ‘chportset’ and ‘rmportset’ commands.

## [Parameters](ibm_svc_manage_portset_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of portset. |
| **noownershipgroup**  boolean | Specify to remove the ownership group from portset.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Applies only during updation of portset.  Choices:   - `false` - `true` |
| **ownershipgroup**  string | The name of the ownership group to which the portset object is being mapped.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Applies when *state=present*. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **portset_type**  string | Specifies the type for the portset.  Applies only during creation of portset.  Choices:   - `"host"` ← (default) - `"replication"` |
| **state**  string / required | Creates (`present`) or Deletes (`absent`) the IP portset.  Choices:   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_portset_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_portset_module.md#id4)

```yaml+jinja
- name: Create a portset
  ibm.spectrum_virtualize.ibm_svc_manage_portset:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   name: portset1
   portset_type: host
   ownershipgroup: owner1
   state: present
- name: Update a portset
  ibm.spectrum_virtualize.ibm_svc_manage_portset:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   name: portset1
   noownershipgroup: true
   state: present
- name: Delete a portset
  ibm.spectrum_virtualize.ibm_svc_manage_portset:
   clustername: "{{cluster}}"
   username: "{{username}}"
   password: "{{password}}"
   name: portset1
   state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
