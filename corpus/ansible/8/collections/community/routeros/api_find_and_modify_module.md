---
collection: ansible
version: "8"
title: "community.routeros.api_find_and_modify module – Find and modify information using the API"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/api_find_and_modify_module.html
fetched_at: 2026-07-28T01:59:01+00:00
---
# community.routeros.api_find_and_modify module – Find and modify information using the API

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/ui/repo/published/community/routeros/) (version 2.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
> You need further requirements to be able to use this module,
> see [Requirements](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module-requirements) for details.
>
> To use it in a playbook, specify: `community.routeros.api_find_and_modify`.

New in community.routeros 2.1.0

- [Synopsis](api_find_and_modify_module.md#synopsis)
- [Requirements](api_find_and_modify_module.md#requirements)
- [Parameters](api_find_and_modify_module.md#parameters)
- [Attributes](api_find_and_modify_module.md#attributes)
- [Notes](api_find_and_modify_module.md#notes)
- [See Also](api_find_and_modify_module.md#see-also)
- [Examples](api_find_and_modify_module.md#examples)
- [Return Values](api_find_and_modify_module.md#return-values)

## [Synopsis](api_find_and_modify_module.md#id1)

- Allows to find entries for a path by conditions and modify the values of these entries.
- Use the [community.routeros.api_find_and_modify](api_find_and_modify_module.md#ansible-collections-community-routeros-api-find-and-modify-module) module to set all entries of a path to specific values, or change multiple entries in different ways in one step.

## [Requirements](api_find_and_modify_module.md#id2)

The below requirements are needed on the host that executes this module.

- librouteros
- Python >= 3.6 (for librouteros)

## [Parameters](api_find_and_modify_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_no_matches**  boolean | Whether to allow that no match is found.  If not specified, this value is induced from whether `require_matches_min` is 0 or larger.  **Choices:**   - `false` - `true` |
| **ca_path**  path  *added in community.routeros 1.2.0* | PEM formatted file that contains a CA certificate to be used for certificate validation.  See also `validate_cert_hostname`. Only used when `tls=true` and `validate_certs=true`. |
| **encoding**  string  *added in community.routeros 2.1.0* | Use the specified encoding when communicating with the RouterOS device.  Default is `ASCII`. Note that `UTF-8` requires librouteros 3.2.1 or newer.  **Default:** `"ASCII"` |
| **find**  dictionary / required | Fields to search for.  The module will only consider entries in the given `path` that match all fields provided here.  Use YAML `~`, or prepend keys with `!`, to specify an unset value.  Note that if the dictionary specified here is empty, every entry in the path will be matched. |
| **force_no_cert**  boolean  *added in community.routeros 2.4.0* | Set to `true` to connect without a certificate when `tls=true`.  See also `validate_certs`.  **Note:** this forces the use of anonymous Diffie-Hellman (ADH) ciphers. The protocol is susceptible to Man-in-the-Middle attacks, because the keys used in the exchange are not authenticated. Instead of simply connecting without a certificate to “make things work” have a look at `validate_certs` and `ca_path`.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string / required | RouterOS hostname API. |
| **password**  string / required | RouterOS user password. |
| **path**  string / required | Path to query.  An example value is `ip address`. This is equivalent to running `/ip address` in the RouterOS CLI. |
| **port**  integer | RouterOS api port. If `tls` is set, port will apply to TLS/SSL connection.  Defaults are `8728` for the HTTP API, and `8729` for the HTTPS API. |
| **require_matches_max**  integer | Make sure that there are no more matches than this number.  If there are more matches, fail instead of modifying anything.  If not specified, there is no upper limit. |
| **require_matches_min**  integer | Make sure that there are no less matches than this number.  If there are less matches, fail instead of modifying anything.  **Default:** `0` |
| **timeout**  integer  *added in community.routeros 2.3.0* | Timeout for the request.  **Default:** `10` |
| **tls**  aliases: ssl  boolean | If is set TLS will be used for RouterOS API connection.  **Choices:**   - `false` ← (default) - `true` |
| **username**  string / required | RouterOS login user. |
| **validate_cert_hostname**  boolean  *added in community.routeros 1.2.0* | Set to `true` to validate hostnames in certificates.  See also `validate_certs`. Only used when `tls=true` and `validate_certs=true`.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean  *added in community.routeros 1.2.0* | Set to `false` to skip validation of TLS certificates.  See also `validate_cert_hostname`. Only used when `tls=true`.  **Note:** instead of simply deactivating certificate validations to “make things work”, please consider creating your own CA certificate and using it to sign certificates used for your router. You can tell the module about your CA certificate with the `ca_path` option.  **Choices:**   - `false` - `true` ← (default) |
| **values**  dictionary / required | On all entries matching the conditions in `find`, set the keys of this option to the values specified here.  Use YAML `~`, or prepend keys with `!`, to specify to unset a value. |

## [Attributes](api_find_and_modify_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.routeros.api** | Use `group/community.routeros.api` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | **Platform:** **RouterOS** | Target OS/families that can be operated against. |

## [Notes](api_find_and_modify_module.md#id5)

> **Note:**
>
> - If you want to change values based on their old values (like change all comments ‘foo’ to ‘bar’) and make sure that there are at least N such values, you can use `require_matches_min=N` together with `allow_no_matches=true`. This will make the module fail if there are less than N such entries, but not if there is no match. The latter case is needed for idempotency of the task: once the values have been changed, there should be no further match.

## [See Also](api_find_and_modify_module.md#id6)

> **See also:**
>
> [community.routeros.api](api_module.md#ansible-collections-community-routeros-api-module)
> :   Ansible module for RouterOS API.
>
> [community.routeros.api_facts](api_facts_module.md#ansible-collections-community-routeros-api-facts-module)
> :   Collect facts from remote devices running MikroTik RouterOS using the API.
>
> [community.routeros.api_modify](api_modify_module.md#ansible-collections-community-routeros-api-modify-module)
> :   Modify data at paths with API.
>
> [community.routeros.api_info](api_info_module.md#ansible-collections-community-routeros-api-info-module)
> :   Retrieve information from API.
>
> [How to connect to RouterOS devices with the RouterOS API](docsite/api-guide.md#ansible-collections-community-routeros-docsite-api-guide)
> :   How to connect to RouterOS devices with the RouterOS API

## [Examples](api_find_and_modify_module.md#id7)

```yaml+jinja
---
- name: Rename bridge from 'bridge' to 'my-bridge'
  community.routeros.api_find_and_modify:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: interface bridge
    find:
      name: bridge
    values:
      name: my-bridge

- name: Change IP address to 192.168.1.1 for interface bridge - assuming there is only one
  community.routeros.api_find_and_modify:
    hostname: "{{ hostname }}"
    password: "{{ password }}"
    username: "{{ username }}"
    path: ip address
    find:
      interface: bridge
    values:
      address: "192.168.1.1/24"
    # If there are zero entries, or more than one: fail! We expected that
    # exactly one is configured.
    require_matches_min: 1
    require_matches_max: 1
```

## [Return Values](api_find_and_modify_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **match_count**  integer | The number of entries that matched the criteria in `find`.  **Returned:** success  **Sample:** `1` |
| **modify__count**  integer | The number of entries that were modified.  **Returned:** success  **Sample:** `1` |
| **new_data**  list / elements=dictionary | A list of all elements for the current path after a change was made.  **Returned:** success  **Sample:** `[{".id": "*1", "actual-interface": "bridge", "address": "192.168.1.1/24", "comment": "awesome", "disabled": false, "dynamic": false, "interface": "bridge", "invalid": false, "network": "192.168.1.0"}]` |
| **old_data**  list / elements=dictionary | A list of all elements for the current path before a change was made.  **Returned:** success  **Sample:** `[{".id": "*1", "actual-interface": "bridge", "address": "192.168.88.1/24", "comment": "defconf", "disabled": false, "dynamic": false, "interface": "bridge", "invalid": false, "network": "192.168.88.0"}]` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.routeros)
- [Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-routeros)
