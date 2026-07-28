---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_callhome module – This module manages Call Home feature configuration on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_callhome_module.html
fetched_at: 2026-07-28T02:35:29+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_callhome module – This module manages Call Home feature configuration on IBM Storage Virtualize family systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_callhome`.

New in ibm.storage_virtualize 1.7.0

- [Synopsis](ibm_svc_manage_callhome_module.md#synopsis)
- [Parameters](ibm_svc_manage_callhome_module.md#parameters)
- [Notes](ibm_svc_manage_callhome_module.md#notes)
- [Examples](ibm_svc_manage_callhome_module.md#examples)

## [Synopsis](ibm_svc_manage_callhome_module.md#id1)

- Ansible interface to manage cloud and email Call Home feature.

## [Parameters](ibm_svc_manage_callhome_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | Specifies the first line of the user’s address as it should appear in Call Home email.  Required when *state=enabled*. |
| **callhome_type**  string / required | Specifies the transmission type.  **Choices:**   - `"cloud services"` - `"email"` - `"both"` |
| **censorcallhome**  string | Specifies that sensitive data is deleted from the enhanced Call Home data.  Applies when *state=enabled*.  If unspecified, default value ‘off’ will be used.  **Choices:**   - `"on"` - `"off"` |
| **city**  string | Specifies the user’s city as it should appear in Call Home email.  Required when *state=enabled*. |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **company_name**  string | Specifies the user’s organization as it should appear in Call Home email.  Required when *state=enabled*. |
| **contact_email**  string | Specifies the email of the person.  Required when *state=enabled*. |
| **contact_name**  string | Specifies the name of the person receiving the email.  Required when *state=enabled*. |
| **country**  string | Specifies the country in which the machine resides as it should appear in Call Home email.  Required when *state=enabled*. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **enhancedcallhome**  string | Specifies that the Call Home function is to send enhanced reports to the support center.  Applies when *state=enabled*.  If unspecified, default value ‘off’ will be used.  **Choices:**   - `"on"` - `"off"` |
| **invemailinterval**  integer | Specifies the interval at which inventory emails are sent to the configured email recipients.  The interval is measured in days. The value must be in the range 0 - 15.  Setting the value to ‘0’ turns off the inventory email notification function. Valid if *inventory* is set to ‘on’. |
| **inventory**  string | Specifies whether the recipient mentioned in parameter *contact_email* receives inventory email notifications.  Applies when *state=enabled*. If unspecified, default value ‘off’ will be used.  **Choices:**   - `"on"` - `"off"` |
| **location**  string | Specifies the physical location of the system that has reported the error.  Required when *state=enabled*. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **phonenumber_primary**  string | Specifies the primary contact telephone number.  Required when *state=enabled*. |
| **phonenumber_secondary**  string | Specifies the secondary contact telephone number.  Required when *state=enabled*. |
| **postalcode**  string | Specifies the user’s zip code or postal code as it should appear in Call Home email.  Required when *state=enabled*. |
| **province**  string | Specifies the user’s state or province as it should appear in Call Home email.  Required when *state=enabled*. |
| **proxy_password**  string | Specifies the proxy’s password.  Applies when *state=enabled* and *proxy_type=basic_authentication*. |
| **proxy_port**  integer | Specifies the proxy server port number. The value must be in the range 1 - 65535.  Applies when *state=enabled* and *proxy_type=open_proxy* or *proxy_type=basic_authentication*. |
| **proxy_type**  string | Specifies the proxy type.  Required when *state=enabled*, to create or modify Call Home feature.  Proxy gets deleted for *proxy_type=no_proxy*.  The parameter is mandatory when *callhome_type=’cloud services’*) or *callhome_type=’both’*.  **Choices:**   - `"open_proxy"` - `"basic_authentication"` - `"certificate"` - `"no_proxy"` |
| **proxy_url**  string | Specifies the proxy server URL with a protocol prefix in fully qualified domain name format.  Applies when *state=enabled* and *proxy_type=open_proxy* or *proxy_type=basic_authentication*. |
| **proxy_username**  string | Specifies the proxy’s username.  Applies when *state=enabled* and *proxy_type=basic_authentication*. |
| **serverIP**  string | Specifies the IP address of the email server.  Required when *state=enabled* and *callhome_type=email* or *callhome_type=both*. |
| **serverPort**  integer | Specifies the port number of the email server.  The value must be in the range 1 - 65535.  Required when *state=enabled* and *callhome_type=email* or *callhome_type=both*. |
| **sslcert**  string | Specifies the file path of proxy’s certificate.  Applies when *state=enabled* and *proxy_type=certificate*. |
| **state**  string / required | Enables or updates (`enabled`) or disables (`disabled`) Call Home feature.  **Choices:**   - `"enabled"` - `"disabled"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_callhome_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_callhome_module.md#id4)

```yaml+jinja
- name: Configure callhome with both email and cloud
  ibm.storage_virtualize.ibm_svc_manage_callhome:
    clustername: "{{ clustername }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "/tmp/playbook.debug"
    state: "enabled"
    callhome_type: "both"
    address: "{{ address }}"
    city: "{{ city }}"
    company_name: "{{ company_name }}"
    contact_email: "{{ contact_email }}"
    contact_name: "{{ contact_name }}"
    country: "{{ country }}"
    location: "{{ location }}"
    phonenumber_primary: "{{ primary_phonenumber }}"
    postalcode: "{{ postal_code }}"
    province: "{{ province }}"
    proxy_type: "{{ proxy_type }}"
    proxy_url: "{{ proxy_url }}"
    proxy_port: "{{ proxy_port }}"
    serverIP: "{{ server_ip }}"
    serverPort: "{{ server_port }}"
    inventory: "on"
    invemailinterval: 1
    enhancedcallhome: "on"
    censorcallhome: "on"
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
