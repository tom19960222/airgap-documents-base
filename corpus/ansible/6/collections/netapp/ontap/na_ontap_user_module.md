---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_user module – NetApp ONTAP user configuration and management"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_user_module.html
fetched_at: 2026-07-28T00:13:24+00:00
---
# netapp.ontap.na_ontap_user module – NetApp ONTAP user configuration and management

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_user_module.md#ansible-collections-netapp-ontap-na-ontap-user-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_user`.

New in netapp.ontap 2.6.0

- [Synopsis](na_ontap_user_module.md#synopsis)
- [Requirements](na_ontap_user_module.md#requirements)
- [Parameters](na_ontap_user_module.md#parameters)
- [Notes](na_ontap_user_module.md#notes)
- [Examples](na_ontap_user_module.md#examples)

## [Synopsis](na_ontap_user_module.md#id1)

- Create or destroy users.

## [Requirements](na_ontap_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **application_dicts**  list / elements=dictionary  added in netapp.ontap 21.6.0 | List of applications to grant access to. Provides better control on applications and authentication methods.  Creating a login with application console, telnet, rsh, and service-processor for a data vserver is not supported.  Module supports both service-processor and service_processor choices.  ZAPI requires service-processor, while REST requires service_processor, except for an issue with ONTAP 9.6 and 9.7.  snmp is not supported in REST.  Either `application_dicts` or `application_strs` is required. |
| **application**  string / required | name of the application.  Choices:   - `"console"` - `"http"` - `"ontapi"` - `"rsh"` - `"snmp"` - `"service_processor"` - `"service-processor"` - `"sp"` - `"ssh"` - `"telnet"` |
| **authentication_methods**  list / elements=string / required | list of authentication methods for the application (see `authentication_method`).  Choices:   - `"community"` - `"password"` - `"publickey"` - `"domain"` - `"nsswitch"` - `"usm"` - `"cert"` - `"saml"` |
| **second_authentication_method**  string | when using ssh, optional additional authentication method for MFA.  Choices:   - `"none"` - `"password"` - `"publickey"` - `"nsswitch"` |
| **application_strs**  aliases: application, applications  list / elements=string  added in netapp.ontap 21.6.0 | List of applications to grant access to.  This option maintains backward compatibility with the existing `applications` option, but is limited.  It is recommended to use the new `application_dicts` option which provides more flexibility.  Creating a login with application console, telnet, rsh, and service-processor for a data vserver is not supported.  Module supports both service-processor and service_processor choices.  ZAPI requires service-processor, while REST requires service_processor, except for an issue with ONTAP 9.6 and 9.7.  snmp is not supported in REST.  Either `application_dicts` or `application_strs` is required.  Choices:   - `"console"` - `"http"` - `"ontapi"` - `"rsh"` - `"snmp"` - `"service_processor"` - `"service-processor"` - `"sp"` - `"ssh"` - `"telnet"` |
| **authentication_method**  string | Authentication method for the application. If you need more than one method, use `application_dicts`.  Not all authentication methods are valid for an application.  Valid authentication methods for each application are as denoted in *authentication_choices_description*.  Password for console application  Password, domain, nsswitch, cert, saml for http application.  Password, domain, nsswitch, cert, saml for ontapi application.  SAML is only supported with REST, but seems to work with ZAPI as well.  Community for snmp application (when creating SNMPv1 and SNMPv2 users).  The usm and community for snmp application (when creating SNMPv3 users).  Password for sp application.  Password for rsh application.  Password for telnet application.  Password, publickey, domain, nsswitch for ssh application.  Required when `application_strs` is present.  Choices:   - `"community"` - `"password"` - `"publickey"` - `"domain"` - `"nsswitch"` - `"usm"` - `"cert"` - `"saml"` |
| **authentication_password**  string  added in netapp.ontap 20.6.0 | Password for the authentication protocol. This should be minimum 8 characters long.  This is required for ‘md5’, ‘sha’ and ‘sha2-256’ authentication protocols and not required for ‘none’.  Only available for ‘usm’ authentication method and non modifiable. |
| **authentication_protocol**  string  added in netapp.ontap 20.6.0 | Authentication protocol for the snmp user.  When cluster FIPS mode is on, ‘sha’ and ‘sha2-256’ are the only possible and valid values.  When cluster FIPS mode is off, the default value is ‘none’.  When cluster FIPS mode is on, the default value is ‘sha’.  Only available for ‘usm’ authentication method and non modifiable.  Choices:   - `"none"` - `"md5"` - `"sha"` - `"sha2-256"` |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **engine_id**  string  added in netapp.ontap 20.6.0 | Authoritative entity’s EngineID for the SNMPv3 user.  This should be specified as a hexadecimal string.  Engine ID with first bit set to 1 in first octet should have a minimum of 5 or maximum of 32 octets.  Engine Id with first bit set to 0 in the first octet should be 12 octets in length.  Engine Id cannot have all zeros in its address.  Only available for ‘usm’ authentication method and non modifiable. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **lock_user**  boolean | Whether the specified user account is locked.  Choices:   - `false` - `true` |
| **name**  string / required | The name of the user to manage. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **privacy_password**  string  added in netapp.ontap 20.6.0 | Password for the privacy protocol. This should be minimum 8 characters long.  This is required for ‘des’ and ‘aes128’ privacy protocols and not required for ‘none’.  Only available for ‘usm’ authentication method and non modifiable. |
| **privacy_protocol**  string  added in netapp.ontap 20.6.0 | Privacy protocol for the snmp user.  When cluster FIPS mode is on, ‘aes128’ is the only possible and valid value.  When cluster FIPS mode is off, the default value is ‘none’. When cluster FIPS mode is on, the default value is ‘aes128’.  Only available for ‘usm’ authentication method and non modifiable.  Choices:   - `"none"` - `"des"` - `"aes128"` |
| **remote_switch_ipaddress**  string  added in netapp.ontap 20.6.0 | This optionally specifies the IP Address of the remote switch.  The remote switch could be a cluster switch monitored by Cluster Switch Health Monitor (CSHM) or a Fiber Channel (FC) switch monitored by Metro Cluster Health Monitor (MCC-HM).  This is applicable only for a remote SNMPv3 user i.e. only if user is a remote (non-local) user, application is snmp and authentication method is usm. |
| **replace_existing_apps_and_methods**  string  added in netapp.ontap 20.6.0 | If the user already exists, the current applications and authentications methods are replaced when state=present.  If the user already exists, the current applications and authentications methods are removed when state=absent.  When using application_dicts or REST, this the only supported behavior.  When using application_strs and ZAPI, this is the behavior when this option is set to always.  When using application_strs and ZAPI, if the option is set to auto, applications that are not listed are not removed.  When using application_strs and ZAPI, if the option is set to auto, authentication mehods that are not listed are not removed.  `auto` preserve the existing behavior for backward compatibility, but note that REST and ZAPI have inconsistent behavior.  This is another reason to recommend to use `application_dicts`.  Choices:   - `"always"` - `"auto"` ← (default) |
| **role_name**  string | The name of the role. Required when `state=present` |
| **set_password**  string | Password for the user account.  It is ignored for creating snmp users, but is required for creating non-snmp users.  For an existing user, this value will be used as the new password. |
| **state**  string | Whether the specified user should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver**  aliases: svm  string / required | The name of the vserver to use.  With REST, for cluster scope, use a vserver entry with no value. |

## [Notes](na_ontap_user_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_user_module.md#id5)

```yaml+jinja
- name: Create User
  netapp.ontap.na_ontap_user:
    state: present
    name: SampleUser
    applications: ssh,console
    authentication_method: password
    set_password: apn1242183u1298u41
    lock_user: True
    role_name: vsadmin
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Delete User
  netapp.ontap.na_ontap_user:
    state: absent
    name: SampleUser
    applications: ssh
    authentication_method: password
    vserver: ansibleVServer
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"

- name: Create user with snmp application (ZAPI)
  netapp.ontap.na_ontap_user:
    state: present
    name: test_cert_snmp
    applications: snmp
    authentication_method: usm
    role_name: admin
    authentication_protocol: md5
    authentication_password: '12345678'
    privacy_protocol: 'aes128'
    privacy_password: '12345678'
    engine_id: '7063514941000000000000'
    remote_switch_ipaddress: 10.0.0.0
    vserver: "{{ vserver }}"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"

- name: Create user
  netapp.ontap.na_ontap_user:
    state: present
    name: test123
    application_dicts:
      - application: http
        authentication_methods: password
      - application: ssh
        authentication_methods: password,publickey
    role_name: vsadmin
    set_password: bobdole1234566
    vserver: "{{ vserver }}"
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
