---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership module – This module manages IP partnerships on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_sv_manage_ip_partnership_module.html
fetched_at: 2026-07-27T17:50:19+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership module – This module manages IP partnerships on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership`.

New in ibm.spectrum_virtualize 1.9.0

- [Synopsis](ibm_sv_manage_ip_partnership_module.md#synopsis)
- [Parameters](ibm_sv_manage_ip_partnership_module.md#parameters)
- [Notes](ibm_sv_manage_ip_partnership_module.md#notes)
- [Examples](ibm_sv_manage_ip_partnership_module.md#examples)

## [Synopsis](ibm_sv_manage_ip_partnership_module.md#id1)

- Ansible interface to manage ‘mkippartnership’, ‘rmpartnership’, and ‘chpartnership’ commands on local and remote systems.

## [Parameters](ibm_sv_manage_ip_partnership_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backgroundcopyrate**  integer | Specifies the maximum percentage of aggregate link bandwidth that can be used for background copy operations. This is a numeric value from 0 through 100. The default value is 50.  Valid when *state=present*. |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **compressed**  string | Specifies whether compression is enabled for this partnership.  Valid when *state=present*.  Choices:   - `"yes"` - `"no"` |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **link1**  string | Specifies the portset name to be used for WAN link 1 of the Spectrum Virtualize storage system.  Valid when *state=present*, to create an IP partnership. |
| **link2**  string | Specifies the portset name to be used for WAN link 2 of the Spectrum Virtualize storage system.  Valid when *state=present*, to create an IP partnership. |
| **linkbandwidthmbits**  integer | Specifies the aggregate bandwidth of the RC link between two clustered systems (systems) in megabits per second (Mbps). This is a numeric value from 1 through 100000.  Valid when *state=present*. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **remote_cluster_id**  string | Specifies the partnership ID of the partner system.  Required when *state=present*, to modify an existing IP partnership.  Required when *state=absent*, to remove an existing IP partnership. |
| **remote_clusterip**  string | Specifies the partner system IP address, either IPv4 or IPv6.  Required when *state=present*, to create an IP partnership. |
| **remote_clustername**  string / required | The hostname or management IP of the remote Spectrum Virtualize storage system. |
| **remote_domain**  string | Domain for the remote Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *remote_clustername*. |
| **remote_link1**  string | Specifies the portset name to be used for WAN link 1 of the remote Spectrum Virtualize storage system.  Valid when *state=present*, to create an IP partnership. |
| **remote_link2**  string | Specifies the portset name to be used for WAN link 2 of the remote Spectrum Virtualize storage system.  Valid when *state=present*, to create an IP partnership. |
| **remote_password**  string | REST API password for the remote Spectrum Virtualize storage system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_token**  string | The authentication token to verify a user on the remote Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **remote_username**  string | REST API username for the remote Spectrum Virtualize storage system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_validate_certs**  boolean | Validates certification for the remote Spectrum Virtualize storage system.  Choices:   - `false` ← (default) - `true` |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) an IP partnership.  Choices:   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **type**  string | Specifies the Internet Protocol (IP) address format for the partnership.  Valid when *state=present*.  Choices:   - `"ipv4"` - `"ipv6"` |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification for the local Spectrum Virtualize storage system.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_ip_partnership_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_ip_partnership_module.md#id4)

```yaml+jinja
- name: Create an IP partnership
  ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    remote_clustername: "{{ remote_clustername }}"
    remote_domain: "{{ remote_domain }}"
    remote_username: "{{ remote_username }}"
    remote_password: "{{ remote_password }}"
    log_path: "/tmp/debug.log"
    remote_clusterip: "{{ partner_ip }}"
    type: "ipv4"
    linkbandwidthmbits: 100
    backgroundcopyrate: 50
    compressed: yes
    link1: "{{ portsetname }}"
    remote_link1: "{{ remote_portsetname}}"
    state: "present"
- name: Update an IP partnership
  ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    remote_clustername: "{{ remote_clustername }}"
    remote_domain: "{{ remote_domain }}"
    remote_username: "{{ remote_username }}"
    remote_password: "{{ remote_password }}"
    log_path: "/tmp/debug.log"
    remote_cluster_id: "{{ cluster_id }}"
    linkbandwidthmbits: 110
    backgroundcopyrate: 60
    compressed: no
    state: "present"
- name: Remove an IP partnership
  ibm.spectrum_virtualize.ibm_sv_manage_ip_partnership:
    clustername: "{{ clustername }}"
    username: "{{ username }}"
    password: "{{ password }}"
    remote_clustername: "{{ remote_clustername }}"
    remote_username: "{{ remote_username }}"
    remote_password: "{{ remote_password }}"
    log_path: "/tmp/debug.log"
    remote_cluster_id: "{{ cluster_id }}"
    state: "absent"
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
