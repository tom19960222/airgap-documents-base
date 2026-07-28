---
collection: ansible
version: "8"
title: "telekom_mms.icinga_director.icinga_service module – Manage services in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/telekom_mms/icinga_director/icinga_service_module.html
fetched_at: 2026-07-28T02:55:08+00:00
---
# telekom_mms.icinga_director.icinga_service module – Manage services in Icinga2

> **Note:**
>
> This module is part of the [telekom_mms.icinga_director collection](https://galaxy.ansible.com/ui/repo/published/telekom_mms/icinga_director/) (version 1.35.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install telekom_mms.icinga_director`.
>
> To use it in a playbook, specify: `telekom_mms.icinga_director.icinga_service`.

New in telekom_mms.icinga_director 1.0.0

- [Synopsis](icinga_service_module.md#synopsis)
- [Parameters](icinga_service_module.md#parameters)
- [Notes](icinga_service_module.md#notes)
- [Examples](icinga_service_module.md#examples)

## [Synopsis](icinga_service_module.md#id1)

- Add or remove a service to Icinga2 through the director API.

## [Parameters](icinga_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  *added in telekom_mms.icinga_director 1.25.0* | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  **Choices:**   - `false` - `true` |
| **check_command**  string | Check command definition. |
| **check_interval**  string | Your regular check interval. |
| **check_period**  string | The name of a time period which determines when this object should be monitored. Not limited by default. |
| **check_timeout**  string | Check command timeout in seconds. Overrides the CheckCommand’s timeout attribute. |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **disabled**  boolean | Disabled objects will not be deployed.  **Choices:**   - `false` ← (default) - `true` |
| **display_name**  string | Alternative name for this service. |
| **enable_active_checks**  boolean | Whether to actively check this object.  **Choices:**   - `false` - `true` |
| **enable_event_handler**  boolean | Whether to enable event handlers this object.  **Choices:**   - `false` - `true` |
| **enable_notifications**  boolean | Whether to send notifications for this object.  **Choices:**   - `false` - `true` |
| **enable_passive_checks**  boolean | Whether to accept passive check results for this object.  **Choices:**   - `false` - `true` |
| **enable_perfdata**  boolean | Whether to process performance data provided by this object.  **Choices:**   - `false` - `true` |
| **force**  boolean | If `yes` do not get a cached copy.  **Choices:**   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  list / elements=string | Service groups that should be directly assigned to this service.  Servicegroups can be useful for various reasons.  They are helpful to provided service-type specific view in Icinga Web 2, either for custom dashboards or as an instrument to enforce restrictions.  Service groups can be directly assigned to single services or to service templates.  **Default:** `[]` |
| **host**  string | Choose the host this single service should be assigned to.  This field will be required when `service_set` is not defined. |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  **Default:** `"ansible-httpget"` |
| **imports**  list / elements=string | Importable templates, add as many as you want.  Please note that order matters when importing properties from multiple templates - last one wins.  **Default:** `[]` |
| **max_check_attempts**  string | Defines after how many check attempts a new hard state is reached. |
| **notes**  string  *added in telekom_mms.icinga_director 1.8.0* | Additional notes for this object. |
| **notes_url**  string  *added in telekom_mms.icinga_director 1.8.0* | An URL pointing to additional notes for this object.  Separate multiple urls like this “’<http://url1>’ ‘<http://url2>’”.  Maximum length is 255 characters. |
| **object_name**  aliases: name  string / required | Name of the service. |
| **retry_interval**  string | Retry interval, will be applied after a state change unless the next hard state is reached. |
| **service_set**  string  *added in telekom_mms.icinga_director 1.29.0* | Choose the service set name this single service should be assigned to.  This field will be required when `host` is not defined. |
| **state**  string | Apply feature state.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_agent**  boolean | Whether the check command for this service should be executed on the Icinga agent.  **Choices:**   - `false` - `true` |
| **use_gssapi**  boolean  *added in ansible-core 2.11* | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  **Choices:**   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vars**  dictionary | Custom properties of the service.  **Default:** `{}` |
| **volatile**  boolean | Whether this check is volatile.  **Choices:**   - `false` - `true` |

## [Notes](icinga_service_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_service_module.md#id4)

```yaml+jinja
- name: Create service
  tags: service
  telekom_mms.icinga_director.icinga_service:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "foo service"
    display_name: "foo service"
    check_command: hostalive
    use_agent: false
    host: foohost
    vars:
      procs_argument: consul
      procs_critical: '1:'
      procs_warning: '1:'

- name: Update service
  tags: service
  telekom_mms.icinga_director.icinga_service:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "foo service"
    display_name: "foo service"
    host: foohost
    notes: "example note"
    notes_url: "'http://url1' 'http://url2'"
    append: true

- name: Create serviceset service
  telekom_mms.icinga_director.icinga_service:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: "foo service serviceset"
    service_set: "foo_serviceset"
```

### Authors

- Sebastian Gumprich (@rndmh3ro)

### Collection links

- [Issue Tracker](https://github.com/telekom-mms/ansible-collection-icinga-director/issues)
- [Repository (Sources)](https://github.com/telekom-mms/ansible-collection-icinga-director)
