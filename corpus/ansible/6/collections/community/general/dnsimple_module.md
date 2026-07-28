---
collection: ansible
version: "6"
title: "community.general.dnsimple module – Interface with dnsimple.com (a DNS hosting service)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dnsimple_module.html
fetched_at: 2026-07-27T17:08:47+00:00
---
# community.general.dnsimple module – Interface with dnsimple.com (a DNS hosting service)

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](dnsimple_module.md#ansible-collections-community-general-dnsimple-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dnsimple`.

- [Synopsis](dnsimple_module.md#synopsis)
- [Requirements](dnsimple_module.md#requirements)
- [Parameters](dnsimple_module.md#parameters)
- [Examples](dnsimple_module.md#examples)

## [Synopsis](dnsimple_module.md#id1)

- Manages domains and records via the DNSimple API, see the docs: <http://developer.dnsimple.com/>.

## [Requirements](dnsimple_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnsimple >= 2.0.0

## [Parameters](dnsimple_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account_api_token**  string | Account API token. See *account_email* for more information. |
| **account_email**  string | Account email. If omitted, the environment variables `DNSIMPLE_EMAIL` and `DNSIMPLE_API_TOKEN` will be looked for.  If those aren’t found, a `.dnsimple` file will be looked for, see: <https://github.com/mikemaccana/dnsimple-python#getting-started>.  `.dnsimple` config files are only supported in dnsimple-python<2.0.0 |
| **domain**  string | Domain to work with. Can be the domain name (e.g. “mydomain.com”) or the numeric ID of the domain in DNSimple.  If omitted, a list of domains will be returned.  If domain is present but the domain doesn’t exist, it will be created. |
| **priority**  integer | Record priority. |
| **record**  string | Record to add, if blank a record for the domain will be created, supports the wildcard (\*). |
| **record_ids**  list / elements=string | List of records to ensure they either exist or do not exist. |
| **sandbox**  boolean  added in community.general 3.5.0 | Use the DNSimple sandbox environment.  Requires a dedicated account in the dnsimple sandbox environment.  Check <https://developer.dnsimple.com/sandbox/> for more information.  Choices:   - `false` ← (default) - `true` |
| **solo**  boolean | Whether the record should be the only one for that record type and record name.  Only use with `state` is set to `present` on a record.  Choices:   - `false` ← (default) - `true` |
| **state**  string | whether the record should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | The TTL to give the new record in seconds.  Default: `3600` |
| **type**  string | The type of DNS record to create.  Choices:   - `"A"` - `"ALIAS"` - `"CNAME"` - `"MX"` - `"SPF"` - `"URL"` - `"TXT"` - `"NS"` - `"SRV"` - `"NAPTR"` - `"PTR"` - `"AAAA"` - `"SSHFP"` - `"HINFO"` - `"POOL"` - `"CAA"` |
| **value**  string | Record value.  Must be specified when trying to ensure a record exists. |

## [Examples](dnsimple_module.md#id4)

```yaml+jinja
- name: Authenticate using email and API token and fetch all domains
  community.general.dnsimple:
    account_email: test@example.com
    account_api_token: dummyapitoken
  delegate_to: localhost

- name: Delete a domain
  community.general.dnsimple:
    domain: my.com
    state: absent
  delegate_to: localhost

- name: Create a test.my.com A record to point to 127.0.0.1
  community.general.dnsimple:
    domain: my.com
    record: test
    type: A
    value: 127.0.0.1
  delegate_to: localhost
  register: record

- name: Delete record using record_ids
  community.general.dnsimple:
    domain: my.com
    record_ids: '{{ record["id"] }}'
    state: absent
  delegate_to: localhost

- name: Create a my.com CNAME record to example.com
  community.general.dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    state: present
  delegate_to: localhost

- name: Change TTL value for a record
  community.general.dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    ttl: 600
    state: present
  delegate_to: localhost

- name: Delete the record
  community.general.dnsimple:
    domain: my.com
    record: ''
    type: CNAME
    value: example.com
    state: absent
  delegate_to: localhost
```

### Authors

- Alex Coomans (@drcapulet)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
