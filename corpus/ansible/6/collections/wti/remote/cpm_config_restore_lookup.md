---
collection: ansible
version: "6"
title: "wti.remote.cpm_config_restore lookup – Send operational parameters to WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_config_restore_lookup.html
fetched_at: 2026-07-28T00:24:01+00:00
---
# wti.remote.cpm_config_restore lookup – Send operational parameters to WTI OOB and PDU devices

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/wti/remote) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_config_restore`.

New in wti.remote 2.9.0

- [Synopsis](cpm_config_restore_lookup.md#synopsis)
- [Keyword parameters](cpm_config_restore_lookup.md#keyword-parameters)
- [Notes](cpm_config_restore_lookup.md#notes)
- [Examples](cpm_config_restore_lookup.md#examples)
- [Return Value](cpm_config_restore_lookup.md#return-value)

## [Synopsis](cpm_config_restore_lookup.md#id1)

- Send operational parameters to WTI OOB and PDU devices

## [Keyword parameters](cpm_config_restore_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_config_restore', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_config_restore', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_filename**  string / required | This is the filename of the existing WTI device configuration file. |
| **cpm_password**  string / required | This is the Password of the WTI device to get the parameters from. |
| **cpm_path**  string | This is the directory path to the existing the WTI device configuration file.  Default: `"/tmp/"` |
| **cpm_url**  string / required | This is the URL of the WTI device to get the parameters from. |
| **cpm_username**  string / required | This is the Username of the WTI device to get the parameters from. |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_config_restore_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_config_restore_lookup.md#id4)

```yaml+jinja
-   name: Get the Parameters for a WTI device
    cpm_config_restore:
        cpm_url: "nonexist.wti.com"
        cpm_username: "super"
        cpm_password: "super"
        cpm_path: "/tmp/"
        cpm_filename: "wti-192-10-10-239-2020-02-13T16-05-57-xml"
        use_https: true
        validate_certs: false
```

## [Return Value](cpm_config_restore_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output XML configuration of the WTI device queried  Returned: always |
| **filelength**  integer | Length of the file uploaded in bytes  Returned: success  Sample: `[{"filelength": 329439}]` |
| **status**  list / elements=string | List of status returns from backup operation  Returned: success  Sample: `[{"code": 0, "text": "ok", "unittimestamp": "2020-02-14T00:18:57+00:00"}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
