---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_ems_config module – NetApp ONTAP module to modify EMS configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_ems_config_module.html
fetched_at: 2026-07-28T02:41:55+00:00
---
# netapp.ontap.na_ontap_ems_config module – NetApp ONTAP module to modify EMS configuration.

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
> see [Requirements](na_ontap_ems_config_module.md#ansible-collections-netapp-ontap-na-ontap-ems-config-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_ems_config`.

New in netapp.ontap 22.8.0

- [Synopsis](na_ontap_ems_config_module.md#synopsis)
- [Requirements](na_ontap_ems_config_module.md#requirements)
- [Parameters](na_ontap_ems_config_module.md#parameters)
- [Notes](na_ontap_ems_config_module.md#notes)
- [Examples](na_ontap_ems_config_module.md#examples)

## [Synopsis](na_ontap_ems_config_module.md#id1)

- Configure event notification and logging for the cluster.

## [Requirements](na_ontap_ems_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_ems_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **mail_from**  string | The email address that the event notification system uses as the “From” address for email notifications. |
| **mail_server**  string | The name or IP address of the SMTP server that the event notification system uses to send email notification of events. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **proxy_password**  string | Password for HTTP or HTTPS proxy. |
| **proxy_url**  string | HTTP or HTTPS proxy server URL used by rest-api type EMS notification destinations if your organization uses a proxy. |
| **proxy_user**  string | User name for the HTTP or HTTPS proxy server if authentication is required. |
| **pubsub_enabled**  boolean | Indicates whether or not events are published to the Publish/Subscribe messaging broker.  Requires ONTAP 9.10 or later.  **Choices:**   - `false` - `true` |
| **state**  string | modify EMS configuration, only present is supported.  **Choices:**   - `"present"` ← (default) |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_ems_config_module.md#id4)

> **Note:**
>
> - Only supported with REST and requires ONTAP 9.6 or later.
> - Module is not idempotent when proxy_password is set.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_ems_config_module.md#id5)

```yaml+jinja
- name: Modify EMS mail config
  netapp.ontap.na_ontap_ems_config:
    state: present
    mail_from: administrator@mycompany.com
    mail_server: mail.mycompany.com
    pubsub_enabled: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: "{{ validate_certs }}"

- name: Modify EMS proxy config
  netapp.ontap.na_ontap_ems_config:
    state: present
    proxy_url: http://proxy.example.com:8080
    pubsub_enabled: true
    proxy_user: admin
    proxy_password: password
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
