---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_security_ipsec_policy module – NetApp ONTAP module to create, modify or delete security IPsec policy."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_security_ipsec_policy_module.html
fetched_at: 2026-07-28T02:43:14+00:00
---
# netapp.ontap.na_ontap_security_ipsec_policy module – NetApp ONTAP module to create, modify or delete security IPsec policy.

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
> see [Requirements](na_ontap_security_ipsec_policy_module.md#ansible-collections-netapp-ontap-na-ontap-security-ipsec-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_security_ipsec_policy`.

New in netapp.ontap 22.1.0

- [Synopsis](na_ontap_security_ipsec_policy_module.md#synopsis)
- [Requirements](na_ontap_security_ipsec_policy_module.md#requirements)
- [Parameters](na_ontap_security_ipsec_policy_module.md#parameters)
- [Notes](na_ontap_security_ipsec_policy_module.md#notes)
- [Examples](na_ontap_security_ipsec_policy_module.md#examples)

## [Synopsis](na_ontap_security_ipsec_policy_module.md#id1)

- Create, modify or delete security IPsec policy.

## [Requirements](na_ontap_security_ipsec_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_security_ipsec_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action for the IPsec policy.  Cannot modify after create.  **Choices:**   - `"bypass"` - `"discard"` - `"esp_transport"` - `"esp_udp"` |
| **authentication_method**  string | Authentication method for the IPsec policy.  Supported from 9.10.1 or later.  Cannot modify after create.  **Choices:**   - `"none"` - `"psk"` - `"pki"` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **certificate**  string | Certificate for the IPsec policy.  Supported from 9.10.1 or later.  Required when `authentication_method` is ‘pki’ in create. |
| **enabled**  boolean | Indicates whether or not the policy is enabled.  **Choices:**   - `false` - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ipspace**  string | IPspace name where `svm` exist. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **local_endpoint**  dictionary | Local endpoint for the IPsec policy. |
| **address**  string / required | IPv4 or IPv6 address. |
| **netmask**  string / required | Input as netmask length (16) or IPv4 mask (255.255.0.0).  For IPv6, the default value is 64 with a valid range of 1 to 127. |
| **port**  string | Application port to be covered by the IPsec policy, example 23. |
| **local_identity**  string | local IKE endpoint’s identity for authentication purpose. |
| **name**  string / required | Name of the security IPsec policy |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **protocol**  string | protocol to be protected by by this policy.  example ‘any’ or ‘0’, ‘tcp’, ‘udp’ or protocol number. |
| **remote_endpoint**  dictionary | remote endpoint for the IPsec policy. |
| **address**  string / required | IPv4 or IPv6 address. |
| **netmask**  string / required | Input as netmask length (16) or IPv4 mask (255.255.0.0).  For IPv6, the default value is 64 with a valid range of 1 to 127. |
| **port**  string | Application port to be covered by the IPsec policy, example 23 or 23-23. |
| **remote_identity**  string | remote IKE endpoint’s identity for authentication purpose. |
| **secret_key**  string | Pre-shared key for IKE negotiation.  Required when `authentication_method` is ‘psk’ in create.  Cannot modify after create. |
| **state**  string | Create or delete security IPsec policy.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **svm**  string | The name of the SVM.  Required when creating security IPsec policy. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_security_ipsec_policy_module.md#id4)

> **Note:**
>
> - Supports check_mode.
> - Only supported with REST and requires ONTAP 9.8 or later.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_security_ipsec_policy_module.md#id5)

```yaml+jinja
- name: Create security IPsec policy with pre-shared Keys.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_psk
    ipspace: Default
    svm: ansibleSVM
    authentication_method: psk
    secret_key: "{{ secret_key }}"
    action: esp_transport
    local_endpoint:
      address: 10.23.43.23
      netmask: 24
      port: 201
    remote_endpoint:
      address: 10.23.43.30
      netmask: 24
      port: 205
    protocol: tcp
    enabled: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Create security IPsec policy with certificates.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_pki
    ipspace: Default
    svm: ansibleSVM
    authentication_method: pki
    certificate: "{{ cert_name }}"
    action: esp_transport
    local_endpoint:
      address: 10.23.43.23
      netmask: 24
      port: 201
    remote_endpoint:
      address: 10.23.43.30
      netmask: 24
      port: 205
    protocol: tcp
    enabled: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Create security IPsec policy without psk or certificates.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_none
    ipspace: Default
    svm: ansibleSVM
    action: bypass
    local_endpoint:
      address: 10.23.43.23
      netmask: 24
      port: 201
    remote_endpoint:
      address: 10.23.43.30
      netmask: 24
      port: 205
    protocol: tcp
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Modify security IPsec policy local, remote end_point.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_pki
    ipspace: Default
    svm: ansibleSVM
    authentication_method: pki
    certificate: "{{ cert_name }}"
    action: esp_transport
    local_endpoint:
      address: 10.23.43.50
      netmask: 24
      port: 201
    remote_endpoint:
      address: 10.23.43.60
      netmask: 24
      port: 205
    protocol: tcp
    enabled: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Modify security IPsec protocol, enable options.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_pki
    ipspace: Default
    svm: ansibleSVM
    authentication_method: pki
    certificate: "{{ cert_name }}"
    action: esp_transport
    local_endpoint:
      address: 10.23.43.50
      netmask: 24
      port: 201
    remote_endpoint:
      address: 10.23.43.60
      netmask: 24
      port: 205
    protocol: udp
    enabled: false
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Delete security IPsec policy.
  netapp.ontap.na_ontap_security_ipsec_policy:
    name: ipsec_policy_pki
    svm: ansibleSVM
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
