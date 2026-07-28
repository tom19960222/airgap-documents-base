---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_svc_manage_sra module – This module manages remote support assistance configuration on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_svc_manage_sra_module.html
fetched_at: 2026-07-27T17:50:36+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_sra module – This module manages remote support assistance configuration on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_sra`.

New in ibm.spectrum_virtualize 1.7.0

- [Synopsis](ibm_svc_manage_sra_module.md#synopsis)
- [Parameters](ibm_svc_manage_sra_module.md#parameters)
- [Notes](ibm_svc_manage_sra_module.md#notes)
- [Examples](ibm_svc_manage_sra_module.md#examples)

## [Synopsis](ibm_svc_manage_sra_module.md#id1)

- Ansible interface to manage ‘chsra’ support remote assistance command.

## [Parameters](ibm_svc_manage_sra_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  list / elements=string | Specifies the list of unique names for the support center or proxy to be defined.  Required when *support=remote*, to enable remote support assistance. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **sra_ip**  list / elements=string | Specifies the list of IP addresses or fully qualified domain names for the new support center or proxy server.  Required when *support=remote* and *state=enabled*, to enable support remote assistannce. |
| **sra_port**  list / elements=string | Specifies the list of port numbers for the new support center or proxy server.  Required when *support=remote* and *state=enabled*, to enable support remote assistannce. |
| **state**  string / required | Enables (`enabled`) or disables (`disabled`) the remote support assistance.  Choices:   - `"enabled"` - `"disabled"` |
| **support**  string / required | Specifies the support assistance through `remote` or `onsite`.  Choices:   - `"remote"` - `"onsite"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_sra_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_sra_module.md#id4)

```yaml+jinja
- name: Enable support remote assistance
  ibm.spectrum_virtualize.ibm_svc_manage_sra:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    support: remote
    state: enabled
    name:
      - proxy_1
      - proxy_2
      - proxy_3
    sra_ip:
      - '0.0.0.0'
      - '1.1.1.1'
      - '2.1.2.2'
    sra_port:
      - 8888
      - 9999
      - 8800
- name: Disable support remote assistance
  ibm.spectrum_virtualize.ibm_svc_manage_sra:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    support: remote
    state: disabled
    name:
      - proxy_1
      - proxy_2
      - proxy_3
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
