---
collection: ansible
version: "8"
title: "Community.Dns"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/index.html
fetched_at: 2026-07-28T01:02:09+00:00
---
# Community.Dns

Collection version 2.6.4

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Guides](index.md#guides)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Plugins and modules for working with DNS

**Authors:**

- Felix Fontein (github.com/felixfontein)
- Markus Bergholz (github.com/markuman)

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Guides](index.md#id3)

- [Community.Dns Filter Guide](docsite/filter_guide.md)
- [Hetzner DNS Guide](docsite/hetzner_guide.md)
- [HostTech DNS Guide](docsite/hosttech_guide.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.dns collection:

### Modules

- [hetzner_dns_record module](hetzner_dns_record_module.md#ansible-collections-community-dns-hetzner-dns-record-module) – Add or delete a single record in Hetzner DNS service
- [hetzner_dns_record_info module](hetzner_dns_record_info_module.md#ansible-collections-community-dns-hetzner-dns-record-info-module) – Retrieve records in Hetzner DNS service
- [hetzner_dns_record_set module](hetzner_dns_record_set_module.md#ansible-collections-community-dns-hetzner-dns-record-set-module) – Add or delete record sets in Hetzner DNS service
- [hetzner_dns_record_set_info module](hetzner_dns_record_set_info_module.md#ansible-collections-community-dns-hetzner-dns-record-set-info-module) – Retrieve record sets in Hetzner DNS service
- [hetzner_dns_record_sets module](hetzner_dns_record_sets_module.md#ansible-collections-community-dns-hetzner-dns-record-sets-module) – Bulk synchronize DNS record sets in Hetzner DNS service
- [hetzner_dns_zone_info module](hetzner_dns_zone_info_module.md#ansible-collections-community-dns-hetzner-dns-zone-info-module) – Retrieve zone information in Hetzner DNS service
- [hosttech_dns_record module](hosttech_dns_record_module.md#ansible-collections-community-dns-hosttech-dns-record-module) – Add or delete a single record in Hosttech DNS service
- [hosttech_dns_record_info module](hosttech_dns_record_info_module.md#ansible-collections-community-dns-hosttech-dns-record-info-module) – Retrieve records in Hosttech DNS service
- [hosttech_dns_record_set module](hosttech_dns_record_set_module.md#ansible-collections-community-dns-hosttech-dns-record-set-module) – Add or delete record sets in Hosttech DNS service
- [hosttech_dns_record_set_info module](hosttech_dns_record_set_info_module.md#ansible-collections-community-dns-hosttech-dns-record-set-info-module) – Retrieve record sets in Hosttech DNS service
- [hosttech_dns_record_sets module](hosttech_dns_record_sets_module.md#ansible-collections-community-dns-hosttech-dns-record-sets-module) – Bulk synchronize DNS record sets in Hosttech DNS service
- [hosttech_dns_zone_info module](hosttech_dns_zone_info_module.md#ansible-collections-community-dns-hosttech-dns-zone-info-module) – Retrieve zone information in Hosttech DNS service
- [nameserver_info module](nameserver_info_module.md#ansible-collections-community-dns-nameserver-info-module) – Look up nameservers for a DNS name
- [nameserver_record_info module](nameserver_record_info_module.md#ansible-collections-community-dns-nameserver-record-info-module) – Look up all records of a type from all nameservers for a DNS name
- [wait_for_txt module](wait_for_txt_module.md#ansible-collections-community-dns-wait-for-txt-module) – Wait for TXT entries to be available on all authoritative nameservers

### Filter Plugins

- [get_public_suffix filter](get_public_suffix_filter.md#ansible-collections-community-dns-get-public-suffix-filter) – Returns the public suffix of a DNS name
- [get_registrable_domain filter](get_registrable_domain_filter.md#ansible-collections-community-dns-get-registrable-domain-filter) – Returns the registrable domain name of a DNS name
- [remove_public_suffix filter](remove_public_suffix_filter.md#ansible-collections-community-dns-remove-public-suffix-filter) – Removes the public suffix from a DNS name
- [remove_registrable_domain filter](remove_registrable_domain_filter.md#ansible-collections-community-dns-remove-registrable-domain-filter) – Removes the registrable domain name from a DNS name

### Inventory Plugins

- [hetzner_dns_records inventory](hetzner_dns_records_inventory.md#ansible-collections-community-dns-hetzner-dns-records-inventory) – Create inventory from Hetzner DNS records
- [hosttech_dns_records inventory](hosttech_dns_records_inventory.md#ansible-collections-community-dns-hosttech-dns-records-inventory) – Create inventory from Hosttech DNS records

### Lookup Plugins

- [lookup lookup](lookup_lookup.md#ansible-collections-community-dns-lookup-lookup) – Look up DNS records
- [lookup_as_dict lookup](lookup_as_dict_lookup.md#ansible-collections-community-dns-lookup-as-dict-lookup) – Look up DNS records as dictionaries

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
