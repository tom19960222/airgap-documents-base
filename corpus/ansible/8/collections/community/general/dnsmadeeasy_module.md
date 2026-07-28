---
collection: ansible
version: "8"
title: "community.general.dnsmadeeasy module – Interface with dnsmadeeasy.com (a DNS hosting service)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dnsmadeeasy_module.html
fetched_at: 2026-07-28T01:45:26+00:00
---
# community.general.dnsmadeeasy module – Interface with dnsmadeeasy.com (a DNS hosting service)

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](dnsmadeeasy_module.md#ansible-collections-community-general-dnsmadeeasy-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dnsmadeeasy`.

- [Synopsis](dnsmadeeasy_module.md#synopsis)
- [Requirements](dnsmadeeasy_module.md#requirements)
- [Parameters](dnsmadeeasy_module.md#parameters)
- [Attributes](dnsmadeeasy_module.md#attributes)
- [Notes](dnsmadeeasy_module.md#notes)
- [Examples](dnsmadeeasy_module.md#examples)

## [Synopsis](dnsmadeeasy_module.md#id1)

- Manages DNS records via the v2 REST API of the DNS Made Easy service. It handles records only; there is no manipulation of domains or monitor/account support yet. See: <https://www.dnsmadeeasy.com/integration/restapi/>

Aliases: net_tools.dnsmadeeasy

## [Requirements](dnsmadeeasy_module.md#id2)

The below requirements are needed on the host that executes this module.

- hashlib
- hmac

## [Parameters](dnsmadeeasy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_key**  string / required | Account API Key. |
| **account_secret**  string / required | Account Secret Key. |
| **autoFailover**  boolean | If true, fallback to the primary IP address is manual after a failover.  If false, fallback to the primary IP address is automatic after a failover.  **Choices:**   - `false` ← (default) - `true` |
| **contactList**  string | Name or id of the contact list that the monitor will notify.  The default `''` means the Account Owner. |
| **domain**  string / required | Domain to work with. Can be the domain name (e.g. “mydomain.com”) or the numeric ID of the domain in DNS Made Easy (e.g. “839989”) for faster resolution |
| **failover**  boolean | If `true`, add or change the failover. This is applicable only for A records.  **Choices:**   - `false` ← (default) - `true` |
| **httpFile**  string | The file at the Fqdn that the monitor queries for HTTP or HTTPS. |
| **httpFqdn**  string | The fully qualified domain name used by the monitor. |
| **httpQueryString**  string | The string in the httpFile that the monitor queries for HTTP or HTTPS. |
| **ip1**  string | Primary IP address for the failover.  Required if adding or changing the monitor or failover. |
| **ip2**  string | Secondary IP address for the failover.  Required if adding or changing the failover. |
| **ip3**  string | Tertiary IP address for the failover. |
| **ip4**  string | Quaternary IP address for the failover. |
| **ip5**  string | Quinary IP address for the failover. |
| **maxEmails**  integer | Number of emails sent to the contact list by the monitor.  **Default:** `1` |
| **monitor**  boolean | If `true`, add or change the monitor. This is applicable only for A records.  **Choices:**   - `false` ← (default) - `true` |
| **port**  integer | Port used by the monitor.  **Default:** `80` |
| **protocol**  string | Protocol used by the monitor.  **Choices:**   - `"TCP"` - `"UDP"` - `"HTTP"` ← (default) - `"DNS"` - `"SMTP"` - `"HTTPS"` |
| **record_name**  string | Record name to get/create/delete/update. If record_name is not specified; all records for the domain will be returned in “result” regardless of the state argument. |
| **record_ttl**  integer | record’s “Time to live”. Number of seconds the record remains cached in DNS servers.  **Default:** `1800` |
| **record_type**  string | Record type.  **Choices:**   - `"A"` - `"AAAA"` - `"CNAME"` - `"ANAME"` - `"HTTPRED"` - `"MX"` - `"NS"` - `"PTR"` - `"SRV"` - `"TXT"` |
| **record_value**  string | Record value. HTTPRED: <redirection URL>, MX: <priority> <target name>, NS: <name server>, PTR: <target name>, SRV: <priority> <weight> <port> <target name>, TXT: <text value>”  If record_value is not specified; no changes will be made and the record will be returned in ‘result’ (in other words, this module can be used to fetch a record’s current id, type, and ttl) |
| **sandbox**  boolean | Decides if the sandbox API should be used. Otherwise (default) the production API of DNS Made Easy is used.  **Choices:**   - `false` ← (default) - `true` |
| **sensitivity**  string | Number of checks the monitor performs before a failover occurs where Low = 8, Medium = 5,and High = 3.  **Choices:**   - `"Low"` - `"Medium"` ← (default) - `"High"` |
| **state**  string / required | whether the record should exist or not  **Choices:**   - `"present"` - `"absent"` |
| **systemDescription**  string | Description used by the monitor.  **Default:** `""` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](dnsmadeeasy_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](dnsmadeeasy_module.md#id5)

> **Note:**
>
> - The DNS Made Easy service requires that machines interacting with the API have the proper time and timezone set. Be sure you are within a few seconds of actual time by using NTP.
> - This module returns record(s) and monitor(s) in the “result” element when ‘state’ is set to ‘present’. These values can be be registered and used in your playbooks.
> - Only A records can have a monitor or failover.
> - To add failover, the ‘failover’, ‘autoFailover’, ‘port’, ‘protocol’, ‘ip1’, and ‘ip2’ options are required.
> - To add monitor, the ‘monitor’, ‘port’, ‘protocol’, ‘maxEmails’, ‘systemDescription’, and ‘ip1’ options are required.
> - The monitor and the failover will share ‘port’, ‘protocol’, and ‘ip1’ options.

## [Examples](dnsmadeeasy_module.md#id6)

```yaml+jinja
- name: Fetch my.com domain records
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
  register: response

- name: Create a record
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1

- name: Update the previously created record
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_value: 192.0.2.23

- name: Fetch a specific record
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
  register: response

- name: Delete a record
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    record_type: A
    state: absent
    record_name: test

- name: Add a failover
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: true
    ip1: 127.0.0.2
    ip2: 127.0.0.3

- name: Add a failover
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: true
    ip1: 127.0.0.2
    ip2: 127.0.0.3
    ip3: 127.0.0.4
    ip4: 127.0.0.5
    ip5: 127.0.0.6

- name: Add a monitor
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: true
    ip1: 127.0.0.2
    protocol: HTTP  # default
    port: 80  # default
    maxEmails: 1
    systemDescription: Monitor Test A record
    contactList: my contact list

- name: Add a monitor with http options
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: true
    ip1: 127.0.0.2
    protocol: HTTP  # default
    port: 80  # default
    maxEmails: 1
    systemDescription: Monitor Test A record
    contactList: 1174  # contact list id
    httpFqdn: http://my.com
    httpFile: example
    httpQueryString: some string

- name: Add a monitor and a failover
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: true
    ip1: 127.0.0.2
    ip2: 127.0.0.3
    monitor: true
    protocol: HTTPS
    port: 443
    maxEmails: 1
    systemDescription: monitoring my.com status
    contactList: emergencycontacts

- name: Remove a failover
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    failover: false

- name: Remove a monitor
  community.general.dnsmadeeasy:
    account_key: key
    account_secret: secret
    domain: my.com
    state: present
    record_name: test
    record_type: A
    record_value: 127.0.0.1
    monitor: false
```

### Authors

- Brice Burgess (@briceburg)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
