---
collection: ansible
version: "8"
title: "community.general.cloudflare_dns module – Manage Cloudflare DNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cloudflare_dns_module.html
fetched_at: 2026-07-28T01:45:07+00:00
---
# community.general.cloudflare_dns module – Manage Cloudflare DNS records

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
> see [Requirements](cloudflare_dns_module.md#ansible-collections-community-general-cloudflare-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.cloudflare_dns`.

- [Synopsis](cloudflare_dns_module.md#synopsis)
- [Requirements](cloudflare_dns_module.md#requirements)
- [Parameters](cloudflare_dns_module.md#parameters)
- [Attributes](cloudflare_dns_module.md#attributes)
- [Examples](cloudflare_dns_module.md#examples)
- [Return Values](cloudflare_dns_module.md#return-values)

## [Synopsis](cloudflare_dns_module.md#id1)

- Manages dns records via the Cloudflare API, see the docs: <https://api.cloudflare.com/>.

Aliases: net_tools.cloudflare_dns

## [Requirements](cloudflare_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](cloudflare_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_api_key**  aliases: account_api_token  string | Account API key.  Required for api keys authentication.  You can obtain your API key from the bottom of the Cloudflare ‘My Account’ page, found here: <https://dash.cloudflare.com/>. |
| **account_email**  string | Account email. Required for API keys authentication. |
| **algorithm**  integer | Algorithm number.  Required for `type=DS` and `type=SSHFP` when `state=present`. |
| **api_token**  string  *added in community.general 0.2.0* | API token.  Required for api token authentication.  You can obtain your API token from the bottom of the Cloudflare ‘My Account’ page, found here: <https://dash.cloudflare.com/>.  Can be specified in `CLOUDFLARE_TOKEN` environment variable since community.general 2.0.0. |
| **cert_usage**  integer | Certificate usage number.  Required for `type=TLSA` when `state=present`.  **Choices:**   - `0` - `1` - `2` - `3` |
| **hash_type**  integer | Hash type number.  Required for `type=DS`, `type=SSHFP` and `type=TLSA` when `state=present`.  **Choices:**   - `1` - `2` |
| **key_tag**  integer | DNSSEC key tag.  Needed for `type=DS` when `state=present`. |
| **port**  integer | Service port.  Required for `type=SRV` and `type=TLSA`. |
| **priority**  integer | Record priority.  Required for `type=MX` and `type=SRV`  **Default:** `1` |
| **proto**  string | Service protocol. Required for `type=SRV` and `type=TLSA`.  Common values are TCP and UDP.  Before Ansible 2.6 only TCP and UDP were available. |
| **proxied**  boolean | Proxy through Cloudflare network or just use DNS.  **Choices:**   - `false` ← (default) - `true` |
| **record**  aliases: name  string | Record to add.  Required if `state=present`.  Default is `@` (that is, the zone name).  **Default:** `"@"` |
| **selector**  integer | Selector number.  Required for `type=TLSA` when `state=present`.  **Choices:**   - `0` - `1` |
| **service**  string | Record service.  Required for `type=SRV`. |
| **solo**  boolean | Whether the record should be the only one for that record type and record name.  Only use with `state=present`.  This will delete all other records with the same record name and type.  **Choices:**   - `false` - `true` |
| **state**  string | Whether the record(s) should exist or not.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **timeout**  integer | Timeout for Cloudflare API calls.  **Default:** `30` |
| **ttl**  integer | The TTL to give the new record.  Must be between 120 and 2,147,483,647 seconds, or 1 for automatic.  **Default:** `1` |
| **type**  string | The type of DNS record to create. Required if `state=present`.  `type=DS`, `type=SSHFP`, and `type=TLSA` were added in Ansible 2.7.  **Choices:**   - `"A"` - `"AAAA"` - `"CNAME"` - `"DS"` - `"MX"` - `"NS"` - `"SPF"` - `"SRV"` - `"SSHFP"` - `"TLSA"` - `"TXT"` |
| **value**  aliases: content  string | The record value.  Required for `state=present`. |
| **weight**  integer | Service weight.  Required for `type=SRV`.  **Default:** `1` |
| **zone**  aliases: domain  string / required | The name of the Zone to work with (e.g. “example.com”).  The Zone must already exist. |

## [Attributes](cloudflare_dns_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](cloudflare_dns_module.md#id5)

```yaml+jinja
- name: Create a test.example.net A record to point to 127.0.0.1
  community.general.cloudflare_dns:
    zone: example.net
    record: test
    type: A
    value: 127.0.0.1
    account_email: test@example.com
    account_api_key: dummyapitoken
  register: record

- name: Create a record using api token
  community.general.cloudflare_dns:
    zone: example.net
    record: test
    type: A
    value: 127.0.0.1
    api_token: dummyapitoken

- name: Create a example.net CNAME record to example.com
  community.general.cloudflare_dns:
    zone: example.net
    type: CNAME
    value: example.com
    account_email: test@example.com
    account_api_key: dummyapitoken
    state: present

- name: Change its TTL
  community.general.cloudflare_dns:
    zone: example.net
    type: CNAME
    value: example.com
    ttl: 600
    account_email: test@example.com
    account_api_key: dummyapitoken
    state: present

- name: Delete the record
  community.general.cloudflare_dns:
    zone: example.net
    type: CNAME
    value: example.com
    account_email: test@example.com
    account_api_key: dummyapitoken
    state: absent

- name: Create a example.net CNAME record to example.com and proxy through Cloudflare's network
  community.general.cloudflare_dns:
    zone: example.net
    type: CNAME
    value: example.com
    proxied: true
    account_email: test@example.com
    account_api_key: dummyapitoken
    state: present

# This deletes all other TXT records named "test.example.net"
- name: Create TXT record "test.example.net" with value "unique value"
  community.general.cloudflare_dns:
    domain: example.net
    record: test
    type: TXT
    value: unique value
    solo: true
    account_email: test@example.com
    account_api_key: dummyapitoken
    state: present

- name: Create an SRV record _foo._tcp.example.net
  community.general.cloudflare_dns:
    domain: example.net
    service: foo
    proto: tcp
    port: 3500
    priority: 10
    weight: 20
    type: SRV
    value: fooserver.example.net

- name: Create a SSHFP record login.example.com
  community.general.cloudflare_dns:
    zone: example.com
    record: login
    type: SSHFP
    algorithm: 4
    hash_type: 2
    value: 9dc1d6742696d2f51ca1f1a78b3d16a840f7d111eb9454239e70db31363f33e1

- name: Create a TLSA record _25._tcp.mail.example.com
  community.general.cloudflare_dns:
    zone: example.com
    record: mail
    port: 25
    proto: tcp
    type: TLSA
    cert_usage: 3
    selector: 1
    hash_type: 1
    value: 6b76d034492b493e15a7376fccd08e63befdad0edab8e442562f532338364bf3

- name: Create a DS record for subdomain.example.com
  community.general.cloudflare_dns:
    zone: example.com
    record: subdomain
    type: DS
    key_tag: 5464
    algorithm: 8
    hash_type: 2
    value: B4EB5AC4467D2DFB3BAF9FB9961DC1B6FED54A58CDFAA3E465081EC86F89BFAB
```

## [Return Values](cloudflare_dns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **record**  complex | A dictionary containing the record data.  **Returned:** success, except on record deletion |
| **content**  string | The record content (details depend on record type).  **Returned:** success  **Sample:** `"192.0.2.91"` |
| **created_on**  string | The record creation date.  **Returned:** success  **Sample:** `"2016-03-25T19:09:42.516553Z"` |
| **data**  dictionary | Additional record data.  **Returned:** success, if type is SRV, DS, SSHFP or TLSA  **Sample:** `{"name": "jabber", "port": 8080, "priority": 10, "proto": "_tcp", "service": "_xmpp", "target": "jabberhost.sample.com", "weight": 5}` |
| **id**  string | The record ID.  **Returned:** success  **Sample:** `"f9efb0549e96abcb750de63b38c9576e"` |
| **locked**  boolean | No documentation available.  **Returned:** success  **Sample:** `false` |
| **meta**  dictionary | No documentation available.  **Returned:** success  **Sample:** `{"auto_added": false}` |
| **modified_on**  string | Record modification date.  **Returned:** success  **Sample:** `"2016-03-25T19:09:42.516553Z"` |
| **name**  string | The record name as FQDN (including _service and _proto for SRV).  **Returned:** success  **Sample:** `"www.sample.com"` |
| **priority**  integer | Priority of the MX record.  **Returned:** success, if type is MX  **Sample:** `10` |
| **proxiable**  boolean | Whether this record can be proxied through Cloudflare.  **Returned:** success  **Sample:** `false` |
| **proxied**  boolean | Whether the record is proxied through Cloudflare.  **Returned:** success  **Sample:** `false` |
| **ttl**  integer | The time-to-live for the record.  **Returned:** success  **Sample:** `300` |
| **type**  string | The record type.  **Returned:** success  **Sample:** `"A"` |
| **zone_id**  string | The ID of the zone containing the record.  **Returned:** success  **Sample:** `"abcede0bf9f0066f94029d2e6b73856a"` |
| **zone_name**  string | The name of the zone containing the record.  **Returned:** success  **Sample:** `"sample.com"` |

### Authors

- Michael Gruener (@mgruener)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
