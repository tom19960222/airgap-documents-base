---
collection: ansible
version: "8"
title: "cisco.mso.mso_site module – Manage sites"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/mso/mso_site_module.html
fetched_at: 2026-07-28T01:38:16+00:00
---
# cisco.mso.mso_site module – Manage sites

> **Note:**
>
> This module is part of the [cisco.mso collection](https://galaxy.ansible.com/ui/repo/published/cisco/mso/) (version 2.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.mso`.
> You need further requirements to be able to use this module,
> see [Requirements](mso_site_module.md#ansible-collections-cisco-mso-mso-site-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.mso.mso_site`.

- [Synopsis](mso_site_module.md#synopsis)
- [Requirements](mso_site_module.md#requirements)
- [Parameters](mso_site_module.md#parameters)
- [Notes](mso_site_module.md#notes)
- [Examples](mso_site_module.md#examples)

## [Synopsis](mso_site_module.md#id1)

- Manage sites on Cisco ACI Multi-Site.

## [Requirements](mso_site_module.md#id2)

The below requirements are needed on the host that executes this module.

- Multi Site Orchestrator v2.1 or newer

## [Parameters](mso_site_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apic_login_domain**  string | The AAA login domain for the username for the APICs.  The apic_login_domain attribute is not supported when using with ND platform.  See the ND collection for complete site management. |
| **apic_password**  string | The password for the APICs.  The apic_password attribute is not supported when using with ND platform.  See the ND collection for complete site management. |
| **apic_site_id**  string | The site ID of the APICs. |
| **apic_username**  string | The username for the APICs.  The apic_username attribute is not supported when using with ND platform.  See the ND collection for complete site management.  **Default:** `"admin"` |
| **host**  aliases: hostname  string | IP Address or hostname of the ACI Multi Site Orchestrator host.  If the value is not specified in the task, the value of environment variable `MSO_HOST` will be used instead. |
| **labels**  list / elements=string | The labels for this site.  Labels that do not already exist will be automatically created.  The labels attribute is not supported when using with ND platform.  See the ND collection for complete site management. |
| **location**  dictionary | Location of the site.  The location attribute is not supported when using with ND platform.  See the ND collection for complete site management. |
| **latitude**  float | The latitude of the location of the site. |
| **longitude**  float | The longitude of the location of the site. |
| **login_domain**  string | The login domain name to use for authentication.  The default value is Local.  If the value is not specified in the task, the value of environment variable `MSO_LOGIN_DOMAIN` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_login_domain` will be used if this attribute is not specified. |
| **output_level**  string | Influence the output of this MSO module.  `normal` means the standard output, incl. `current` dict  `info` adds informational output, incl. `previous`, `proposed` and `sent` dicts  `debug` adds debugging output, incl. `filter_string`, `method`, `response`, `status` and `url` information  If the value is not specified in the task, the value of environment variable `MSO_OUTPUT_LEVEL` will be used instead.  **Choices:**   - `"debug"` - `"info"` - `"normal"` ← (default) |
| **password**  string | The password to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_PASSWORD` or `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Port number to be used for the REST connection.  The default value depends on parameter `use_ssl`.  If the value is not specified in the task, the value of environment variable `MSO_PORT` will be used instead. |
| **site**  aliases: name  string | The name of the site. |
| **state**  string | Use `present` or `absent` for adding or removing.  Use `query` for listing an object or multiple objects.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"query"` |
| **timeout**  integer | The socket level timeout in seconds.  The default value is 30 seconds.  If the value is not specified in the task, the value of environment variable `MSO_TIMEOUT` will be used instead. |
| **urls**  list / elements=string | A list of URLs to reference the APICs.  The urls attribute is not supported when using with ND platform.  See the ND collection for complete site management. |
| **use_proxy**  boolean | If `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  If the value is not specified in the task, the value of environment variable `MSO_USE_PROXY` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |
| **use_ssl**  boolean | If `false`, an HTTP connection will be used instead of the default HTTPS connection.  If the value is not specified in the task, the value of environment variable `MSO_USE_SSL` will be used instead.  When using a HTTPAPI connection plugin the inventory variable `ansible_httpapi_use_ssl` will be used if this attribute is not specified.  The default is `false` when using a HTTPAPI connection plugin (mso or nd) and `true` when using the legacy connection method (only for mso).  **Choices:**   - `false` - `true` |
| **username**  string | The username to use for authentication.  If the value is not specified in the task, the value of environment variables `MSO_USERNAME` or `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only set to `false` when used on personally controlled sites using self-signed certificates.  If the value is not specified in the task, the value of environment variable `MSO_VALIDATE_CERTS` will be used instead.  The default is `true`.  **Choices:**   - `false` - `true` |

## [Notes](mso_site_module.md#id4)

> **Note:**
>
> - This module was written to support Multi Site Orchestrator v2.1 or newer. Some or all functionality may not work on earlier versions.

## [Examples](mso_site_module.md#id5)

```yaml+jinja
- name: Add a new site
  cisco.mso.mso_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    site: north_europe
    description: North European Datacenter
    apic_username: mso_admin
    apic_password: AnotherSecretPassword
    apic_site_id: 12
    urls:
    - 10.2.3.4
    - 10.2.4.5
    - 10.3.5.6
    labels:
    - NEDC
    - Europe
    - Diegem
    location:
      latitude: 50.887318
      longitude: 4.447084
    state: present
  delegate_to: localhost

- name: Remove a site
  cisco.mso.mso_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    site: north_europe
    state: absent
  delegate_to: localhost

- name: Query a site
  cisco.mso.mso_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    site: north_europe
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all sites
  cisco.mso.mso_site:
    host: mso_host
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result
```

### Authors

- Dag Wieers (@dagwieers)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-mso/issues)
- [Homepage](https://cisco.com/go/aci)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-mso)
