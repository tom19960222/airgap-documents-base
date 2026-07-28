---
collection: ansible
version: "8"
title: "community.general.nsupdate module – Manage DNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nsupdate_module.html
fetched_at: 2026-07-28T01:48:13+00:00
---
# community.general.nsupdate module – Manage DNS records

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
> see [Requirements](nsupdate_module.md#ansible-collections-community-general-nsupdate-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nsupdate`.

- [Synopsis](nsupdate_module.md#synopsis)
- [Requirements](nsupdate_module.md#requirements)
- [Parameters](nsupdate_module.md#parameters)
- [Attributes](nsupdate_module.md#attributes)
- [Examples](nsupdate_module.md#examples)
- [Return Values](nsupdate_module.md#return-values)

## [Synopsis](nsupdate_module.md#id1)

- Create, update and remove DNS records using DDNS updates

Aliases: net_tools.nsupdate

## [Requirements](nsupdate_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnspython

## [Parameters](nsupdate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **key_algorithm**  string | Specify key algorithm used by `key_secret`.  **Choices:**   - `"HMAC-MD5.SIG-ALG.REG.INT"` - `"hmac-md5"` ← (default) - `"hmac-sha1"` - `"hmac-sha224"` - `"hmac-sha256"` - `"hmac-sha384"` - `"hmac-sha512"` |
| **key_name**  string | Use TSIG key name to authenticate against DNS `server` |
| **key_secret**  string | Use TSIG key secret, associated with `key_name`, to authenticate against `server` |
| **port**  integer | Use this TCP port when connecting to `server`.  **Default:** `53` |
| **protocol**  string | Sets the transport protocol (TCP or UDP). TCP is the recommended and a more robust option.  **Choices:**   - `"tcp"` ← (default) - `"udp"` |
| **record**  string / required | Sets the DNS record to modify. When zone is omitted this has to be absolute (ending with a dot). |
| **server**  string / required | Apply DNS modification on this server, specified by IPv4 or IPv6 address. |
| **state**  string | Manage DNS record.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | Sets the record TTL.  **Default:** `3600` |
| **type**  string | Sets the record type.  **Default:** `"A"` |
| **value**  list / elements=string | Sets the record value. |
| **zone**  string | DNS record will be modified on this `zone`.  When omitted DNS will be queried to attempt finding the correct zone.  Starting with Ansible 2.7 this parameter is optional. |

## [Attributes](nsupdate_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nsupdate_module.md#id5)

```yaml+jinja
- name: Add or modify ansible.example.org A to 192.168.1.1"
  community.general.nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "ansible"
    value: "192.168.1.1"

- name: Add or modify ansible.example.org A to 192.168.1.1, 192.168.1.2 and 192.168.1.3"
  community.general.nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "ansible"
    value: ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

- name: Remove puppet.example.org CNAME
  community.general.nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "puppet"
    type: "CNAME"
    state: absent

- name: Add 1.1.168.192.in-addr.arpa. PTR for ansible.example.org
  community.general.nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    record: "1.1.168.192.in-addr.arpa."
    type: "PTR"
    value: "ansible.example.org."
    state: present

- name: Remove 1.1.168.192.in-addr.arpa. PTR
  community.general.nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    record: "1.1.168.192.in-addr.arpa."
    type: "PTR"
    state: absent
```

## [Return Values](nsupdate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  string | If module has modified record  **Returned:** success |
| **dns_rc**  integer | dnspython return code  **Returned:** always  **Sample:** `4` |
| **dns_rc_str**  string | dnspython return code (string representation)  **Returned:** always  **Sample:** `"REFUSED"` |
| **record**  string | DNS record  **Returned:** success  **Sample:** `"ansible"` |
| **ttl**  integer | DNS record TTL  **Returned:** success  **Sample:** `86400` |
| **type**  string | DNS record type  **Returned:** success  **Sample:** `"CNAME"` |
| **value**  list / elements=string | DNS record value(s)  **Returned:** success  **Sample:** `["192.168.1.1"]` |
| **zone**  string | DNS record zone  **Returned:** success  **Sample:** `"example.org."` |

### Authors

- Loic Blot (@nerzhul)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
