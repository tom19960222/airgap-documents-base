---
collection: ansible
version: "6"
title: "t_systems_mms.icinga_director.icinga_host_template module – Manage host templates in Icinga2"
source_url: https://docs.ansible.com/projects/ansible/6/collections/t_systems_mms/icinga_director/icinga_host_template_module.html
fetched_at: 2026-07-28T00:20:07+00:00
---
# t_systems_mms.icinga_director.icinga_host_template module – Manage host templates in Icinga2

> **Note:**
>
> This module is part of the [t_systems_mms.icinga_director collection](https://galaxy.ansible.com/t_systems_mms/icinga_director) (version 1.31.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install t_systems_mms.icinga_director`.
>
> To use it in a playbook, specify: `t_systems_mms.icinga_director.icinga_host_template`.

New in t_systems_mms.icinga_director 1.2.0

- [Synopsis](icinga_host_template_module.md#synopsis)
- [Parameters](icinga_host_template_module.md#parameters)
- [Notes](icinga_host_template_module.md#notes)
- [Examples](icinga_host_template_module.md#examples)

## [Synopsis](icinga_host_template_module.md#id1)

- Add or remove a host template to Icinga2 through the director API.

## [Parameters](icinga_host_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_config**  boolean  added in t_systems_mms.icinga_director 1.9.0 | Whether the agent is configured to accept config.  Choices:   - `false` - `true` |
| **address**  string | Host address. Usually an IPv4 address, but may be any kind of address your check plugin is able to deal with. |
| **address6**  string | Host IPv6 address. Usually an IPv6 address, but may be any kind of address your check plugin is able to deal with. |
| **append**  boolean  added in t_systems_mms.icinga_director 1.25.0 | Do not overwrite the whole object but instead append the defined properties.  Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.  Note - Variables that are set by default will also be applied, even if not set.  Choices:   - `false` - `true` |
| **check_command**  string | The name of the check command.  Though this is not required to be defined in the director, you still have to supply a check_command in a host or host-template. |
| **check_interval**  string | Your regular check interval. |
| **check_period**  string | The name of a time period which determines when this object should be monitored. Not limited by default. |
| **check_timeout**  string | Check command timeout in seconds. Overrides the CheckCommand’s timeout attribute |
| **client_cert**  path | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **command_endpoint**  string | The endpoint where commands are executed on. |
| **disabled**  boolean | Disabled objects will not be deployed.  Choices:   - `false` ← (default) - `true` |
| **display_name**  string | Alternative name for this host. Might be a host alias or and kind of string helping your users to identify this host. |
| **enable_active_checks**  boolean | Whether to actively check this object.  Choices:   - `false` - `true` |
| **enable_event_handler**  boolean | Whether to enable event handlers this object.  Choices:   - `false` - `true` |
| **enable_flapping**  boolean | Whether flap detection is enabled on this object.  Choices:   - `false` - `true` |
| **enable_notifications**  boolean | Whether to send notifications for this object.  Choices:   - `false` - `true` |
| **enable_passive_checks**  boolean | Whether to accept passive check results for this object.  Choices:   - `false` - `true` |
| **enable_perfdata**  boolean | Whether to process performance data provided by this object.  Choices:   - `false` - `true` |
| **event_command**  string | Event command for host which gets called on every check execution if one of these conditions matches  The host is in a soft state  The host state changes into a hard state  The host state recovers from a soft or hard state to OK/Up |
| **flapping_threshold_high**  string | Flapping upper bound in percent for a service to be considered flapping |
| **flapping_threshold_low**  string | Flapping lower bound in percent for a service to be considered not flapping |
| **force**  boolean | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **groups**  list / elements=string | Hostgroups that should be directly assigned to this node. Hostgroups can be useful for various reasons.  You might assign service checks based on assigned hostgroup. They are also often used as an instrument to enforce restricted views in Icinga Web 2.  Hostgroups can be directly assigned to single hosts or to host templates.  You might also want to consider assigning hostgroups using apply rules.  Default: `[]` |
| **has_agent**  boolean  added in t_systems_mms.icinga_director 1.9.0 | Whether this host has the Icinga 2 Agent installed.  Choices:   - `false` - `true` |
| **http_agent**  string | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **icon_image**  string | An URL pointing to an icon for this object.  Try “tux.png” for icons relative to public/img/icons or “cloud” (no extension) for items from the Icinga icon font |
| **icon_image_alt**  string | Alternative text to be shown in case above icon is missing |
| **imports**  list / elements=string | Choose a host-template. |
| **master_should_connect**  boolean  added in t_systems_mms.icinga_director 1.9.0 | Whether the parent (master) node should actively try to connect to this agent.  Choices:   - `false` - `true` |
| **max_check_attempts**  string | Defines after how many check attempts a new hard state is reached. |
| **notes**  string  added in t_systems_mms.icinga_director 1.8.0 | Additional notes for this object. |
| **notes_url**  string  added in t_systems_mms.icinga_director 1.8.0 | An URL pointing to additional notes for this object.  Separate multiple urls like this “’<http://url1>’ ‘<http://url2>’”.  Maximum length is 255 characters. |
| **object_name**  aliases: name  string / required | Icinga object name for this host template.  This is usually a fully qualified host name but it could basically be any kind of string.  To make things easier for your users we strongly suggest to use meaningful names for templates.  For example “generic-host” is ugly, “Standard Linux Server” is easier to understand. |
| **retry_interval**  string | Retry interval, will be applied after a state change unless the next hard state is reached. |
| **state**  string | Apply feature state.  Choices:   - `"present"` ← (default) - `"absent"` |
| **url**  string / required | HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path |
| **url_password**  string | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vars**  dictionary | Custom properties of the host. |
| **volatile**  boolean | Whether this check is volatile.  Choices:   - `false` - `true` |
| **zone**  string | Set the zone. |

## [Notes](icinga_host_template_module.md#id3)

> **Note:**
>
> - This module supports check mode.

## [Examples](icinga_host_template_module.md#id4)

```yaml+jinja
- name: Create host template
  t_systems_mms.icinga_director.icinga_host_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    accept_config: true
    check_command: hostalive
    check_interval: 90s
    check_timeout: 60
    command_endpoint: fooendpoint
    disabled: false
    display_name: foohosttemplate
    enable_active_checks: true
    enable_event_handler: false
    enable_flapping: false
    enable_notifications: true
    enable_passive_checks: false
    enable_perfdata: false
    flapping_threshold_high: "30.0"
    flapping_threshold_low: "25.0"
    has_agent: true
    icon_image_alt: "alt text"
    icon_image: "http://url1"
    master_should_connect: true
    max_check_attempts: 3
    object_name: foohosttemplate
    retry_interval: "1m"
    volatile: false
    groups:
      - "foohostgroup"
    imports:
      - ''
    vars:
      dnscheck: "no"

- name: Update host template
  t_systems_mms.icinga_director.icinga_host_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: foohosttemplate
    notes: "example note"
    notes_url: "'http://url1' 'http://url2'"
    append: true
```

### Authors

- Michaela Mattes (@michaelamattes)

### Collection links

[Issue Tracker](https://github.com/T-Systems-MMS/ansible-collection-icinga-director/issues)
[Repository (Sources)](https://github.com/T-Systems-MMS/ansible-collection-icinga-director)
