---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_firewall_policy module – NetApp ONTAP Manage a firewall policy"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_firewall_policy_module.html
fetched_at: 2026-07-28T02:42:09+00:00
---
# netapp.ontap.na_ontap_firewall_policy module – NetApp ONTAP Manage a firewall policy

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_firewall_policy_module.md#ansible-collections-netapp-ontap-na-ontap-firewall-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_firewall_policy`.

New in netapp.ontap 2.7.0

- [Synopsis](na_ontap_firewall_policy_module.md#synopsis)
- [Requirements](na_ontap_firewall_policy_module.md#requirements)
- [Parameters](na_ontap_firewall_policy_module.md#parameters)
- [Notes](na_ontap_firewall_policy_module.md#notes)
- [Examples](na_ontap_firewall_policy_module.md#examples)

## [Synopsis](na_ontap_firewall_policy_module.md#id1)

- Configure firewall on an ONTAP node and manage firewall policy for an ONTAP SVM

## [Requirements](na_ontap_firewall_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python package ipaddress. Install using ‘pip install ipaddress’
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_firewall_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_list**  list / elements=string | A list of IPs and masks to use.  The host bits of the IP addresses used in this list must be set to 0. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **enable**  string | enable firewall on a node  **Choices:**   - `"enable"` - `"disable"` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **logging**  string | enable logging for firewall on a node  **Choices:**   - `"enable"` - `"disable"` |
| **node**  string | The node to run the firewall configuration on |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **policy**  string | A policy name for the firewall policy |
| **service**  string | The service to apply the policy to  https and ssh are not supported starting with ONTAP 9.6  portmap is supported for ONTAP 9.4, 9.5 and 9.6  none is supported for ONTAP 9.8 onwards.  **Choices:**   - `"dns"` - `"http"` - `"https"` - `"ndmp"` - `"ndmps"` - `"ntp"` - `"portmap"` - `"rsh"` - `"snmp"` - `"ssh"` - `"telnet"` - `"none"` |
| **state**  string | Whether to set up a firewall policy or not  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | This module only support ZAPI and will can not be swtich to REST  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will always use ZAPI.  **Default:** `"never"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vserver**  string | The Vserver to apply the policy to. |

## [Notes](na_ontap_firewall_policy_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_firewall_policy_module.md#id5)

```yaml+jinja
- name: create firewall Policy
  netapp.ontap.na_ontap_firewall_policy:
    state: present
    allow_list: [1.2.3.0/24,1.3.0.0/16]
    policy: pizza
    service: http
    vserver: ci_dev
    hostname: "{{ netapp hostname }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"

- name: Modify firewall Policy
  netapp.ontap.na_ontap_firewall_policy:
    state: present
    allow_list: [1.5.3.0/24]
    policy: pizza
    service: http
    vserver: ci_dev
    hostname: "{{ netapp hostname }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"

- name: Destory firewall Policy
  netapp.ontap.na_ontap_firewall_policy:
    state: absent
    policy: pizza
    service: http
    vserver: ci_dev
    hostname: "{{ netapp hostname }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"

- name: Enable firewall and logging on a node
  netapp.ontap.na_ontap_firewall_policy:
    node: test-vsim1
    enable: enable
    logging: enable
    hostname: "{{ netapp hostname }}"
    username: "{{ netapp username }}"
    password: "{{ netapp password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
