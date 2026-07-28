---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_domain_record module – Manage DigitalOcean domain records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_domain_record_module.html
fetched_at: 2026-07-27T17:06:40+00:00
---
# community.digitalocean.digital_ocean_domain_record module – Manage DigitalOcean domain records

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_domain_record`.

New in community.digitalocean 1.1.0

- [Synopsis](digital_ocean_domain_record_module.md#synopsis)
- [Parameters](digital_ocean_domain_record_module.md#parameters)
- [Notes](digital_ocean_domain_record_module.md#notes)
- [Examples](digital_ocean_domain_record_module.md#examples)
- [Return Values](digital_ocean_domain_record_module.md#return-values)

## [Synopsis](digital_ocean_domain_record_module.md#id1)

- Create/delete a domain record in DigitalOcean.

## [Parameters](digital_ocean_domain_record_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **data**  string | This is the value of the record, depending on the record type.  Default: `""` |
| **domain**  string / required | Name of the domain. |
| **flags**  integer | An unsignedinteger between 0-255 used for CAA records. |
| **force_update**  boolean | If there is already a record with the same `name` and `type` force update it.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Required for `A, AAAA, CNAME, TXT, SRV` records. The host name, alias, or service being defined by the record.  Default: `"@"` |
| **oauth_token**  aliases: API_TOKEN  string | DigitalOcean OAuth token. Can be specified in `DO_API_KEY`, `DO_API_TOKEN`, or `DO_OAUTH_TOKEN` environment variables |
| **port**  integer | The port that the service is accessible on for SRV records only. |
| **priority**  integer | The priority of the host for `SRV, MX` records). |
| **record_id**  integer | Used with `force_update=yes` and `state='absent'` to update or delete a specific record. |
| **state**  string | Indicate desired state of the target.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tag**  string | The parameter tag for CAA records.  Choices:   - `"issue"` - `"wildissue"` - `"iodef"` |
| **ttl**  integer | Time to live for the record, in seconds.  Default: `1800` |
| **type**  string | The type of record you would like to create.  Choices:   - `"A"` - `"AAAA"` - `"CNAME"` - `"MX"` - `"TXT"` - `"SRV"` - `"NS"` - `"CAA"` |
| **weight**  integer | The weight of records with the same priority for SRV records only. |

## [Notes](digital_ocean_domain_record_module.md#id3)

> **Note:**
>
> - Version 2 of DigitalOcean API is used.
> - The number of requests that can be made through the API is currently limited to 5,000 per hour per OAuth token.

## [Examples](digital_ocean_domain_record_module.md#id4)

```yaml+jinja
- name: Create default A record for example.com
  community.digitalocean.digital_ocean_domain_record:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: A
    name: "@"
    data: 127.0.0.1

- name: Create A record for www
  community.digitalocean.digital_ocean_domain_record:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: A
    name: www
    data: 127.0.0.1

- name: Update A record for www based on name/type/data
  community.digitalocean.digital_ocean_domain_record:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: A
    name: www
    data: 127.0.0.2
    force_update: yes

- name: Update A record for www based on record_id
  community.digitalocean.digital_ocean_domain_record:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    record_id: 123456
    type: A
    name: www
    data: 127.0.0.2
    force_update: yes

- name: Remove www record based on name/type/data
  community.digitalocean.digital_ocean_domain_record:
    state: absent
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: A
    name: www
    data: 127.0.0.1

- name: Remove www record based on record_id
  community.digitalocean.digital_ocean_domain_record:
    state: absent
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    record_id: 1234567

- name: Create MX record with priority 10 for example.com
  community.digitalocean.digital_ocean_domain_record:
    state: present
    oauth_token: "{{ lookup('ansible.builtin.env', 'DO_API_TOKEN') }}"
    domain: example.com
    type: MX
    data: mail1.example.com
    priority: 10
```

## [Return Values](digital_ocean_domain_record_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | a DigitalOcean Domain Record  Returned: success  Sample: `{"data": "192.168.0.1", "flags": 16, "id": 3352896, "name": "www", "port": 5556, "priority": 10, "tag": "issue", "ttl": 3600, "type": "CNAME", "weight": 10}` |

### Authors

- Adam Papai (@woohgit)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
