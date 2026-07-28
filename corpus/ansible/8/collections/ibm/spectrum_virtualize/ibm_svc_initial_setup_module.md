---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_initial_setup module – This module allows users to manage the initial setup configuration on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_initial_setup_module.html
fetched_at: 2026-07-28T02:34:51+00:00
---
# ibm.spectrum_virtualize.ibm_svc_initial_setup module – This module allows users to manage the initial setup configuration on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_initial_setup`.

New in ibm.spectrum_virtualize 1.7.0

- [Synopsis](ibm_svc_initial_setup_module.md#synopsis)
- [Parameters](ibm_svc_initial_setup_module.md#parameters)
- [Notes](ibm_svc_initial_setup_module.md#notes)
- [Examples](ibm_svc_initial_setup_module.md#examples)

## [Synopsis](ibm_svc_initial_setup_module.md#id1)

- Ansible interface to perform various initial system configuration

## [Parameters](ibm_svc_initial_setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cloud**  integer | Specifies the number of enclosures for the transparent cloud tiering function. |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **compression**  integer | Changes system licensing for the compression function.  Depending on the type of system, specify a capacity value in terabytes (TB) or specify the total number of storage capacity units (SCUs) that user is licensed to virtualize across tiers of storage on the system or specify the total number of internal and external enclosures that user has licensed on the system. |
| **dnsip**  list / elements=string | Specifies the DNS server Internet Protocol (IP) address. |
| **dnsname**  list / elements=string | Specifies a unique name for the system DNS server being created.  Maximum two DNS servers can be configured. User needs to provide the complete list of DNS servers that are required to be configured. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **easytier**  integer | Specifies the number of enclosures on which user can run Easy Tier. |
| **encryption**  string | Specifies whether the encryption license function is enabled or disabled.  **Choices:**   - `"on"` - `"off"` |
| **flash**  integer | Changes system licensing for the FlashCopy function.  Depending on the type of system, specify a capacity value in terabytes (TB) or specify the total number of internal and external enclosures for the FlashCopy function. |
| **license_key**  list / elements=string | Provides the license key to activate a feature that contains 16 hexadecimal characters organized in four groups of four numbers with each group separated by a hyphen (such as 0123-4567-89AB-CDEF). |
| **log_path**  string | Path of debug log file. |
| **ntpip**  string | Specifies the IPv4 address or fully qualified domain name (FQDN) for the Network Time Protocol (NTP) server.  To remove an already configured NTP IP, user must specify 0.0.0.0. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **physical_flash**  string | For physical disk licensing, this parameter enables or disables the FlashCopy function.  **Choices:**   - `"on"` - `"off"` ← (default) |
| **remote**  integer | Changes system licensing for remote-copy functions such as Metro Mirror, Global Mirror, and HyperSwap.  Depending on the type of system, specify a capacity value in terabytes (TB) or specify the total number of internal and external enclosures that user has licensed on the system. There must be an enclosure license for all enclosures. |
| **system_name**  string | Specifies system name. |
| **time**  string | Specifies the time to which the system must be set.  This value must be in the following format MMDDHHmmYYYY (where M is month, D is day, H is hour, m is minute, and Y is year). |
| **timezone**  string | Specifies the time zone to set for the system. |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **virtualization**  integer | Changes system licensing for the Virtualization function.  Depending on the type of system, specify a capacity value in terabytes (TB) or specify the total number of storage capacity units (SCUs) that user is licensed to virtualize across tiers of storage on the system or specify the number of enclosures of external storage that user is authorized to use. |

## [Notes](ibm_svc_initial_setup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_initial_setup_module.md#id4)

```yaml+jinja
- name: Initial configuration on FlashSystem 9200
  ibm.spectrum_virtualize.ibm_svc_initial_setup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    system_name: cluster_test_0
    time: 101009142021
    timezone: 200
    remote: 50
    virtualization: 50
    flash: 50
    license_key:
      - 0123-4567-89AB-CDEF
      - 8921-4567-89AB-GHIJ
- name: Add DNS servers
  ibm.spectrum_virtualize.ibm_svc_initial_setup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    system_name: cluster_test_
    dnsname:
      - dns_01
      - dns_02
    dnsip:
      - '1.1.1.1'
      - '2.2.2.2'
- name: Delete dns_02 server
  ibm.spectrum_virtualize.ibm_svc_initial_setup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    system_name: cluster_test_
    dnsname:
      - dns_01
    dnsip:
      - '1.1.1.1'
```

### Authors

- Shilpi Jain (@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
