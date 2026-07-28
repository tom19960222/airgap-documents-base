---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_net_ifgrp module – NetApp Ontap modify network interface group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_net_ifgrp_module.html
fetched_at: 2026-07-28T02:42:45+00:00
---
# netapp.ontap.na_ontap_net_ifgrp module – NetApp Ontap modify network interface group

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
> see [Requirements](na_ontap_net_ifgrp_module.md#ansible-collections-netapp-ontap-na-ontap-net-ifgrp-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_net_ifgrp`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_net_ifgrp_module.md#synopsis)
- [Requirements](na_ontap_net_ifgrp_module.md#requirements)
- [Parameters](na_ontap_net_ifgrp_module.md#parameters)
- [Notes](na_ontap_net_ifgrp_module.md#notes)
- [Examples](na_ontap_net_ifgrp_module.md#examples)

## [Synopsis](na_ontap_net_ifgrp_module.md#id1)

- Create, modify ports, destroy the network interface group

## [Requirements](na_ontap_net_ifgrp_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_net_ifgrp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **broadcast_domain**  string  *added in netapp.ontap 21.14.0* | Specify the broadcast_domain name.  Only supported with REST and is ignored with ZAPI.  Required with ONTAP 9.6 and 9.7, but optional with 9.8 or later. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **distribution_function**  string | Specifies the traffic distribution function for the ifgrp.  **Choices:**   - `"mac"` - `"ip"` - `"sequential"` - `"port"` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_lag_ports**  list / elements=string  *added in netapp.ontap 2.14.0* | Only supported with REST and is ignored with ZAPI.  Specify all the ports to find current LAG port.  Ignored if LAG found with exact match of `ports`.  Example if current LAG has ports `['e0c','e0d']` and `ports=['e0c','e0d']`, then from_lag_ports will be ignored.  If LAG not found with `ports`, then ports in this list are used to find the current LAG.  Ports in this list are used only for finding current LAG, provide exact match of all the ports in the current LAG.  Ignored when `state=absent`. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ipspace**  string  *added in netapp.ontap 21.14.0* | Specify the ipspace for the broadcast domain.  Only supported with REST and is ignored with ZAPI.  Required with ONTAP 9.6 and 9.7, but optional with 9.8 or later. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **mode**  string | Specifies the link policy for the ifgrp. |
| **name**  string | Specifies the interface group name.  Not supported with REST, use `ports` or `from_lag_ports`.  Required with ZAPI. |
| **node**  string / required | Specifies the name of node. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **ports**  aliases: port  list / elements=string  *added in netapp.ontap 2.8.0* | List of expected ports to be present in the interface group.  If a port is present in this list, but not on the target, it will be added.  If a port is not in the list, but present on the target, it will be removed.  Make sure the list contains all ports you want to see on the target.  With REST, ports in this list are used to find the current LAG port.  If LAG is not found or only partial port matches, then `from_lag_port` are used to get the current LAG.  With REST, when `state=absent` is set, all of the ports in ifgrp should be provided to delete it.  Example `ports=['e0c','e0a']` will delete ifgrp that has ports `['e0c','e0a']`. |
| **state**  string | Whether the specified network interface group should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_net_ifgrp_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_net_ifgrp_module.md#id5)

```yaml+jinja
- name: create ifgrp
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    distribution_function: ip
    name: a0c
    ports: [e0a]
    mode: multimode
    node: "{{ Vsim node name }}"
- name: modify ports in an ifgrp
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    distribution_function: ip
    name: a0c
    port: [e0a, e0c]
    mode: multimode
    node: "{{ Vsim node name }}"
- name: delete ifgrp
  netapp.ontap.na_ontap_net_ifgrp:
    state: absent
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    name: a0c
    node: "{{ Vsim node name }}"
- name: create ifgrp - REST
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    distribution_function: ip
    ports: [e0a,e0b]
    mode: multimode
    node: "{{ Vsim node name }}"
    broadcast_domain: Default
    ipspace: Default
- name: Remove e0a and add port e0d to above created lag REST
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    from_lag_ports: [a0a,e0b]
    ports: [e0b,e0d]
    node: "{{ Vsim node name }}"
- name: Add e0a to lag that has port e0b e0d REST
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    distribution_function: ip
    ports: [e0b,e0d,e0a]
    mode: multimode
    node: "{{ Vsim node name }}"
- name: Modify broadcast_domain and ipspace REST
  netapp.ontap.na_ontap_net_ifgrp:
    state: present
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    broadcast_domain: test
    ipspace: test
    ports: [e0b,e0d,e0a]
    node: "{{ Vsim node name }}"
- name: Delete LAG with exact match of ports
  netapp.ontap.na_ontap_net_ifgrp:
    state: absent
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    hostname: "{{ netapp_hostname }}"
    ports: [e0b,e0d,e0a]
    node: "{{ Vsim node name }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
