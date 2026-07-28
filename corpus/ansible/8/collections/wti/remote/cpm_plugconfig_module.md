---
collection: ansible
version: "8"
title: "wti.remote.cpm_plugconfig module – Get and Set Plug Parameters on WTI OOB and PDU power devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_plugconfig_module.html
fetched_at: 2026-07-28T02:59:38+00:00
---
# wti.remote.cpm_plugconfig module – Get and Set Plug Parameters on WTI OOB and PDU power devices

> **Note:**
>
> This module is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_plugconfig`.

New in wti.remote 2.8.0

- [Synopsis](cpm_plugconfig_module.md#synopsis)
- [Parameters](cpm_plugconfig_module.md#parameters)
- [Examples](cpm_plugconfig_module.md#examples)
- [Return Values](cpm_plugconfig_module.md#return-values)

## [Synopsis](cpm_plugconfig_module.md#id1)

- Get and Set Plug Parameters on WTI OOB and PDU devices

## [Parameters](cpm_plugconfig_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_action**  string / required | This is the Action to send the module.  **Choices:**   - `"getplugconfig"` - `"setplugconfig"` |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **plug_bootdelay**  integer | On a reboot command, this is the time when a plug will turn on power, after it has been turned off.  0=’0.5 Secs’, 1=’1 Sec’, 2=’2 Sec’, 3=’5 Sec’, 4=’15 Sec’, 5=’30 Sec’, 6=’1 Min’, 7=’2 Mins’, - 8=’3 Mins’, 9=’5 Mins’.  **Choices:**   - `0` - `1` - `2` - `3` - `4` - `5` - `6` - `7` - `8` - `9` |
| **plug_bootpriority**  integer | Prioritizes which plug gets its state changed first. The lower the number the higher the priority.  Valid value can from 1 to the maximum number of plugs of the WTI unit. |
| **plug_default**  integer | What the Plugs default state is when the device starts. 0 - Off, 1 - On.  **Choices:**   - `0` - `1` |
| **plug_id**  string / required | This is the plug number that is to be manipulated  For the getplugconfig command, the plug_id ‘all’ will return the status of all the plugs the  user has rights to access. |
| **plug_name**  string | The new name of the Plug. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](cpm_plugconfig_module.md#id3)

```yaml+jinja
# Get Plug parameters for all ports
- name: Get the Plug parameters for ALL ports of a WTI Power device
  cpm_plugconfig:
    cpm_action: "getplugconfig"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    validate_certs: true
    plug_id: "all"

# Get Plug parameters for port 2
- name: Get the Plug parameters for the given port of a WTI Power device
  cpm_plugconfig:
    cpm_action: "getplugconfig"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    validate_certs: false
    plug_id: "2"

# Configure plug 5
- name: Configure parameters for Plug 5 on a given WTI Power device
  cpm_plugconfig:
    cpm_action: "setplugconfig"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    plug_id: "5"
    plug_name: "NewPlugNameFive"
    plug_bootdelay: "3"
    plug_default: "0"
    plug_bootpriority: "1"
```

## [Return Values](cpm_plugconfig_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  string | The output JSON returned from the commands sent  **Returned:** always |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
