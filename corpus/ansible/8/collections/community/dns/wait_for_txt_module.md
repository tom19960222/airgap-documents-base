---
collection: ansible
version: "8"
title: "community.dns.wait_for_txt module – Wait for TXT entries to be available on all authoritative nameservers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/wait_for_txt_module.html
fetched_at: 2026-07-28T01:43:33+00:00
---
# community.dns.wait_for_txt module – Wait for TXT entries to be available on all authoritative nameservers

> **Note:**
>
> This module is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
> You need further requirements to be able to use this module,
> see [Requirements](wait_for_txt_module.md#ansible-collections-community-dns-wait-for-txt-module-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.wait_for_txt`.

New in community.dns 0.1.0

- [Synopsis](wait_for_txt_module.md#synopsis)
- [Requirements](wait_for_txt_module.md#requirements)
- [Parameters](wait_for_txt_module.md#parameters)
- [Attributes](wait_for_txt_module.md#attributes)
- [Examples](wait_for_txt_module.md#examples)
- [Return Values](wait_for_txt_module.md#return-values)

## [Synopsis](wait_for_txt_module.md#id1)

- Wait for TXT entries with specific values to show up on **all** authoritative nameservers for the DNS name.

## [Requirements](wait_for_txt_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnspython >= 1.15.0 (maybe older versions also work)

## [Parameters](wait_for_txt_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **always_ask_default_resolver**  boolean | When set to `true` (default), will use the default resolver to find the authoritative nameservers of a subzone.  When set to `false`, will use the authoritative nameservers of the parent zone to find the authoritative nameservers of a subzone. This only makes sense when the nameservers were recently changed and have not yet propagated.  **Choices:**   - `false` - `true` ← (default) |
| **max_sleep**  float | Maximal amount of seconds to sleep between two rounds of probing the TXT records.  **Default:** `10.0` |
| **query_retry**  integer | Number of retries for DNS query timeouts.  **Default:** `3` |
| **query_timeout**  float | Timeout per DNS query in seconds.  **Default:** `10.0` |
| **records**  list / elements=dictionary / required | A list of DNS names with TXT entries to look out for. |
| **mode**  string | Comparison modes for the values in `records[].values`.  If `subset`, `records[].values` should be a (not necessarily proper) subset of the TXT values set for the DNS name.  If `superset`, `records[].values` should be a (not necessarily proper) superset of the TXT values set for the DNS name. This includes the case that no TXT entries are set.  If `superset_not_empty`, `records[].values` should be a (not necessarily proper) superset of the TXT values set for the DNS name, assuming at least one TXT record is present.  If `equals`, `records[].values` should be the same set of strings as the TXT values for the DNS name (up to order).  If `equals_ordered`, `records[].values` should be the same ordered list of strings as the TXT values for the DNS name.  **Choices:**   - `"subset"` ← (default) - `"superset"` - `"superset_not_empty"` - `"equals"` - `"equals_ordered"` |
| **name**  string / required | A DNS name, like `www.example.com`. |
| **values**  list / elements=string / required | The TXT values to look for. |
| **servfail_retries**  integer  *added in community.dns 2.6.0* | How often to retry on SERVFAIL errors.  **Default:** `0` |
| **timeout**  float | Global timeout for waiting for all records in seconds.  If not set, will wait indefinitely. |

## [Attributes](wait_for_txt_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.dns 2.4.0*  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](wait_for_txt_module.md#id5)

```yaml+jinja
- name: Wait for a TXT entry to appear
  community.dns.wait_for_txt:
    records:
      # We want that www.example.com has a single TXT record with value 'Hello world!'.
      # There should not be any other TXT record for www.example.com.
      - name: www.example.com
        values: "Hello world!"
        mode: equals
      # We want that example.com has a specific SPF record set.
      # We do not care about other TXT records.
      - name: www.example.com
        values: "v=spf1 a mx -all"
        mode: subset
```

## [Return Values](wait_for_txt_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **completed**  integer | How many of the checks were completed.  **Returned:** always  **Sample:** `3` |
| **records**  list / elements=dictionary | Results on the TXT records queried.  The entries are in a 1:1 correspondence to the entries of the `records` parameter, in exactly the same order.  **Returned:** always  **Sample:** `[{"check_count": 1, "done": true, "name": "example.com", "values": ["a", "b", "c"]}, {"check_count": 0, "done": false, "name": "foo.example.org"}]` |
| **check_count**  integer | How often the TXT records for this DNS name were checked.  **Returned:** always  **Sample:** `3` |
| **done**  boolean | Whether the check completed.  **Returned:** always  **Sample:** `false` |
| **name**  string | The DNS name this check is for.  **Returned:** always  **Sample:** `"example.com"` |
| **values**  dictionary | For every authoritative nameserver for the DNS name, lists the TXT records retrieved during the last lookup made.  Once the check completed for all TXT records retrieved, the TXT records for this DNS name are no longer checked.  If these are multiple TXT entries for a nameserver, the order is as it was received from that nameserver. This might not be the same order provided in the check.  **Returned:** lookup was done at least once  **Sample:** `{"ns1.example.com": ["TXT value 1", "TXT value 2"], "ns2.example.com": ["TXT value 2"]}` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
