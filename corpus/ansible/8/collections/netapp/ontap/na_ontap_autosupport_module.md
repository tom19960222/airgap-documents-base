---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_autosupport module – NetApp ONTAP autosupport"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_autosupport_module.html
fetched_at: 2026-07-28T02:41:36+00:00
---
# netapp.ontap.na_ontap_autosupport module – NetApp ONTAP autosupport

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
> see [Requirements](na_ontap_autosupport_module.md#ansible-collections-netapp-ontap-na-ontap-autosupport-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_autosupport`.

New in netapp.ontap 2.7.0

- [Synopsis](na_ontap_autosupport_module.md#synopsis)
- [Requirements](na_ontap_autosupport_module.md#requirements)
- [Parameters](na_ontap_autosupport_module.md#parameters)
- [Notes](na_ontap_autosupport_module.md#notes)
- [Examples](na_ontap_autosupport_module.md#examples)

## [Synopsis](na_ontap_autosupport_module.md#id1)

- Enable/Disable Autosupport

## [Requirements](na_ontap_autosupport_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_autosupport_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **from_address**  string  *added in netapp.ontap 2.8.0* | specify the e-mail address from which the node sends AutoSupport messages. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **hostname_in_subject**  boolean  *added in netapp.ontap 2.8.0* | Specify whether the hostname of the node is included in the subject line of the AutoSupport message.  **Choices:**   - `false` - `true` |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **local_collection_enabled**  boolean  *added in netapp.ontap 21.5.0* | Specify whether collection of AutoSupport data when the AutoSupport daemon is disabled.  **Choices:**   - `false` - `true` |
| **mail_hosts**  list / elements=string | List of mail server(s) used to deliver AutoSupport messages via SMTP.  Both host names and IP addresses may be used as valid input. |
| **max_http_size**  integer  *added in netapp.ontap 21.5.0* | Specify delivery size limit for the HTTP transport protocol (in bytes). |
| **max_smtp_size**  integer  *added in netapp.ontap 21.5.0* | Specify delivery size limit for the SMTP transport protocol (in bytes). |
| **nht_data_enabled**  boolean  *added in netapp.ontap 21.5.0* | Specify whether the disk health data is collected as part of the AutoSupport data.  **Choices:**   - `false` - `true` |
| **node_name**  string / required | The name of the filer that owns the AutoSupport Configuration. |
| **noteto**  list / elements=string | Specifies up to five recipients of short AutoSupport e-mail messages. |
| **ondemand_enabled**  boolean  *added in netapp.ontap 21.5.0* | Specify whether the AutoSupport OnDemand Download feature is enabled.  **Choices:**   - `false` - `true` |
| **ontapi**  integer | The ontap api version to use |
| **partner_addresses**  list / elements=string  *added in netapp.ontap 2.8.0* | Specifies up to five partner vendor recipients of full AutoSupport e-mail messages. |
| **password**  aliases: pass  string | Password for the specified user. |
| **perf_data_enabled**  boolean  *added in netapp.ontap 21.5.0* | Specify whether the performance data is collected as part of the AutoSupport data.  **Choices:**   - `false` - `true` |
| **post_url**  string | The URL used to deliver AutoSupport messages via HTTP POST. |
| **private_data_removed**  boolean  *added in netapp.ontap 21.5.0* | Specify the removal of customer-supplied data.  **Choices:**   - `false` - `true` |
| **proxy_url**  string  *added in netapp.ontap 2.8.0* | specify an HTTP or HTTPS proxy if the ‘transport’ parameter is set to HTTP or HTTPS and your organization uses a proxy.  If authentication is required, use the format “username:password@host:port”. |
| **reminder_enabled**  boolean  *added in netapp.ontap 21.5.0* | Specify whether AutoSupport reminders are enabled or disabled.  **Choices:**   - `false` - `true` |
| **retry_count**  integer  *added in netapp.ontap 21.5.0* | Specify the maximum number of delivery attempts for an AutoSupport message. |
| **state**  string | Specifies whether the AutoSupport daemon is present or absent.  When this setting is absent, delivery of all AutoSupport messages is turned off.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **support**  boolean | Specifies whether AutoSupport notification to technical support is enabled.  **Choices:**   - `false` - `true` |
| **to_addresses**  list / elements=string  *added in netapp.ontap 2.8.0* | Specifies up to five recipients of full AutoSupport e-mail messages. |
| **transport**  string | The name of the transport protocol used to deliver AutoSupport messages.  **Choices:**   - `"http"` - `"https"` - `"smtp"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **validate_digital_certificate**  boolean  *added in netapp.ontap 21.5.0* | When set to true each node will validate the digital certificates that it receives.  **Choices:**   - `false` - `true` |

## [Notes](na_ontap_autosupport_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_autosupport_module.md#id5)

```yaml+jinja
- name: Enable autosupport
  netapp.ontap.na_ontap_autosupport:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: present
    node_name: test
    transport: https
    noteto: abc@def.com,def@ghi.com
    mail_hosts: 1.2.3.4,5.6.7.8
    support: False
    post_url: url/1.0/post
- name: Modify autosupport proxy_url with password
  netapp.ontap.na_ontap_autosupport:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: present
    node_name: test
    transport: https
    proxy_url: username:password@host.com:8000
- name: Modify autosupport proxy_url without password
  netapp.ontap.na_ontap_autosupport:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: present
    node_name: test
    transport: https
    proxy_url: username@host.com:8000
- name: Disable autosupport
  netapp.ontap.na_ontap_autosupport:
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: absent
    node_name: test
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
