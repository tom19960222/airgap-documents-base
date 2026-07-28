---
collection: ansible
version: "8"
title: "wti.remote.cpm_metering lookup – Get Power and Current data from WTI OOB/Combo and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_metering_lookup.html
fetched_at: 2026-07-28T03:00:02+00:00
---
# wti.remote.cpm_metering lookup – Get Power and Current data from WTI OOB/Combo and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_metering`.

New in wti.remote 2.7.0

- [Synopsis](cpm_metering_lookup.md#synopsis)
- [Terms](cpm_metering_lookup.md#terms)
- [Keyword parameters](cpm_metering_lookup.md#keyword-parameters)
- [Notes](cpm_metering_lookup.md#notes)
- [Examples](cpm_metering_lookup.md#examples)
- [Return Value](cpm_metering_lookup.md#return-value)

## [Synopsis](cpm_metering_lookup.md#id1)

- Get Power and Current data from WTI OOB/Combo and PDU devices

## [Terms](cpm_metering_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | This is the Action to send the module.  **Choices:**   - `"getpower"` - `"getcurrent"` |

## [Keyword parameters](cpm_metering_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_metering', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_metering', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **enddate**  string | End date of the range to look for power data |
| **startdate**  string | Start date of the range to look for power data |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_metering_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('wti.remote.cpm_metering', term1, term2, key1=value1, key2=value2)` and `query('wti.remote.cpm_metering', term1, term2, key1=value1, key2=value2)`

## [Examples](cpm_metering_lookup.md#id5)

```yaml+jinja
# Get Power data
  - name: Get Power data for a given WTI device
  - debug:
        var: lookup('cpm_metering',
                'getpower',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12')

# Get Current data
  - name: Get Current data for a given WTI device
  - debug:
        var: lookup('cpm_metering',
                'getcurrent',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12')

# Get Power data for a date range
  - name: Get Power data for a given WTI device given a certain date range
  - debug:
        var: lookup('cpm_metering',
                'getpower',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12',
                startdate='08-12-2018'
                enddate='08-14-2018')
```

## [Return Value](cpm_metering_lookup.md#id6)

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
