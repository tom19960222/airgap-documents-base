---
collection: ansible
version: "8"
title: "wti.remote.cpm_status lookup – Get status and parameters from WTI OOB and PDU devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_status_lookup.html
fetched_at: 2026-07-28T03:00:10+00:00
---
# wti.remote.cpm_status lookup – Get status and parameters from WTI OOB and PDU devices.

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_status`.

New in wti.remote 2.7.0

- [Synopsis](cpm_status_lookup.md#synopsis)
- [Terms](cpm_status_lookup.md#terms)
- [Keyword parameters](cpm_status_lookup.md#keyword-parameters)
- [Notes](cpm_status_lookup.md#notes)
- [Examples](cpm_status_lookup.md#examples)
- [Return Value](cpm_status_lookup.md#return-value)

## [Synopsis](cpm_status_lookup.md#id1)

- Get various status and parameters from WTI OOB and PDU devices.

## [Terms](cpm_status_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | This is the Action to send the module.  **Choices:**   - `"temperature"` - `"firmware"` - `"status"` - `"alarms"` |

## [Keyword parameters](cpm_status_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_status', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_status', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Basic Authentication Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Basic Authentication Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_status_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('wti.remote.cpm_status', term1, term2, key1=value1, key2=value2)` and `query('wti.remote.cpm_status', term1, term2, key1=value1, key2=value2)`

## [Examples](cpm_status_lookup.md#id5)

```yaml+jinja
# Get temperature
  - name: run Get Device Temperature
  - debug:
        var: lookup('cpm_status',
                'temperature',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='rest',
                cpm_password='restfulpassword')

# Get firmware version
  - name: Get the firmware version of a given WTI device
  - debug:
        var: lookup('cpm_status',
                'firmware',
                validate_certs=false,
                use_https=true,
                cpm_url="192.168.0.158",
                cpm_username="super",
                cpm_password="super")

# Get status output
  - name: Get the status output from a given WTI device
  - debug:
        var: lookup('cpm_status',
                'status',
                validate_certs=true,
                use_https=true,
                cpm_url="rest.wti.com",
                cpm_username="rest",
                cpm_password="restfulpassword")

# Get Alarm output
  - name: Get the alarms status of a given WTI device
  - debug:
        var: lookup('cpm_status',
                'alarms',
                validate_certs=false,
                use_https=false,
                cpm_url="192.168.0.158",
                cpm_username="super",
                cpm_password="super")
```

## [Return Value](cpm_status_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | The output JSON returned from the commands sent  **Returned:** always |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
