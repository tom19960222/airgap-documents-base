---
collection: ansible
version: "6"
title: "community.general.dnsimple_info module – Pull basic info from DNSimple API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dnsimple_info_module.html
fetched_at: 2026-07-27T17:08:47+00:00
---
# community.general.dnsimple_info module – Pull basic info from DNSimple API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dnsimple_info`.

New in community.general 4.2.0

- [Synopsis](dnsimple_info_module.md#synopsis)
- [Parameters](dnsimple_info_module.md#parameters)
- [Examples](dnsimple_info_module.md#examples)
- [Return Values](dnsimple_info_module.md#return-values)

## [Synopsis](dnsimple_info_module.md#id1)

- Retrieve existing records and domains from DNSimple API.

## [Parameters](dnsimple_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_id**  string / required | The account ID to query. |
| **api_key**  string / required | The API key to use. |
| **name**  string | The domain name to retrieve info from.  Will return all associated records for this domain if specified.  If not specified, will return all domains associated with the account ID. |
| **record**  string | The record to find.  If specified, only this record will be returned instead of all records. |
| **sandbox**  boolean | Whether or not to use sandbox environment.  Choices:   - `false` ← (default) - `true` |

## [Examples](dnsimple_info_module.md#id3)

```yaml+jinja
- name: Get all domains from an account
  community.general.dnsimple_info:
    account_id: "1234"
    api_key: "1234"

- name: Get all records from a domain
  community.general.dnsimple_info:
    name: "example.com"
    account_id: "1234"
    api_key: "1234"

- name: Get all info from a matching record
  community.general.dnsimple_info:
    name: "example.com"
    record: "subdomain"
    account_id: "1234"
    api_key: "1234"
```

## [Return Values](dnsimple_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnsimple_domain_info**  list / elements=dictionary | Returns a list of dictionaries of all domains associated with the supplied account ID.  Returned: success when *name* is not specified  Sample: `[{"account_id": 1234, "created_at": "2021-10-16T21:25:42Z", "id": 123456, "last_transferred_at": null, "name": "example.com", "reverse": false, "secondary": false, "updated_at": "2021-11-10T20:22:50Z"}]` |
| **account_id**  integer | The account ID.  Returned: success |
| **created_at**  string | When the domain entry was created.  Returned: success |
| **id**  integer | ID of the entry.  Returned: success |
| **last_transferred_at**  string | Date the domain was transferred, or empty if not.  Returned: success |
| **name**  string | Name of the record.  Returned: success |
| **reverse**  boolean | Whether or not it is a reverse zone record.  Returned: success |
| **updated_at**  string | When the domain entry was updated.  Returned: success |
| **dnsimple_record_info**  list / elements=dictionary | Returns a list of dictionaries that match the record supplied.  Returned: success when *name* and *record* are specified  Sample: `[{"content": "1.2.3.4", "created_at": "2021-11-15T23:55:51Z", "id": 123456, "name": "catheadbiscuit", "parent_id": null, "priority": null, "regions": ["global"], "system_record": false, "ttl": 3600, "type": "A", "updated_at": "2021-11-15T23:55:51Z", "zone_id": "example.com"}]` |
| **content**  string | Content of the returned record.  Returned: success |
| **created_at**  string | When the domain entry was created.  Returned: success |
| **id**  integer | ID of the entry.  Returned: success |
| **name**  string | Name of the record.  Returned: success |
| **parent_id**  integer | Parent record or null.  Returned: success |
| **priority**  string | Priority setting of the record.  Returned: success |
| **regions**  list / elements=string | List of regions where the record is available.  Returned: success |
| **system_record**  boolean | Whether or not it is a system record.  Returned: success |
| **ttl**  integer | Record TTL.  Returned: success |
| **type**  string | Record type.  Returned: success |
| **updated_at**  string | When the domain entry was updated.  Returned: success |
| **zone_id**  string | ID of the zone that the record is associated with.  Returned: success |
| **dnsimple_records_info**  list / elements=dictionary | Returns a list of dictionaries with all records for the domain supplied.  Returned: success when *name* is specified, but *record* is not  Sample: `[{"content": "ns1.dnsimple.com admin.dnsimple.com", "created_at": "2021-10-16T19:07:34Z", "id": 12345, "name": "catheadbiscuit", "parent_id": null, "priority": null, "regions": ["global"], "system_record": true, "ttl": 3600, "type": "SOA", "updated_at": "2021-11-15T23:55:51Z", "zone_id": "example.com"}]` |
| **content**  string | Content of the returned record.  Returned: success |
| **created_at**  string | When the domain entry was created.  Returned: success |
| **id**  integer | ID of the entry.  Returned: success |
| **name**  string | Name of the record.  Returned: success |
| **parent_id**  integer | Parent record or null.  Returned: success |
| **priority**  string | Priority setting of the record.  Returned: success |
| **regions**  list / elements=string | List of regions where the record is available.  Returned: success |
| **system_record**  boolean | Whether or not it is a system record.  Returned: success |
| **ttl**  integer | Record TTL.  Returned: success |
| **type**  string | Record type.  Returned: success |
| **updated_at**  string | When the domain entry was updated.  Returned: success |
| **zone_id**  string | ID of the zone that the record is associated with.  Returned: success |

### Authors

- Edward Hilgendorf (@edhilgendorf)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
