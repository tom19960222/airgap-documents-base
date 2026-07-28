---
collection: ansible
version: "8"
title: "wti.remote.cpm_plugcontrol module – Get and Set Plug actions on WTI OOB and PDU power devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_plugcontrol_module.html
fetched_at: 2026-07-28T02:59:39+00:00
---
# wti.remote.cpm_plugcontrol module – Get and Set Plug actions on WTI OOB and PDU power devices

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
> To use it in a playbook, specify: `wti.remote.cpm_plugcontrol`.

New in wti.remote 2.8.0

- [Synopsis](cpm_plugcontrol_module.md#synopsis)
- [Parameters](cpm_plugcontrol_module.md#parameters)
- [Examples](cpm_plugcontrol_module.md#examples)
- [Return Values](cpm_plugcontrol_module.md#return-values)

## [Synopsis](cpm_plugcontrol_module.md#id1)

- Get and Set Plug actions on WTI OOB and PDU devices

## [Parameters](cpm_plugcontrol_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_action**  string / required | This is the Action to send the module.  **Choices:**   - `"getplugcontrol"` - `"setplugcontrol"` |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **plug_id**  string / required | This is the plug number or the plug name that is to be manipulated  For the plugget command, the plug_id ‘all’ will return the status of all the plugs the  user has rights to access. |
| **plug_state**  string | This is what action to take on the plug.  **Choices:**   - `"on"` - `"off"` - `"boot"` - `"default"` |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](cpm_plugcontrol_module.md#id3)

```yaml+jinja
# Get Plug status for all ports
- name: Get the Plug status for ALL ports of a WTI device
  cpm_plugcontrol:
    cpm_action: "getplugcontrol"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    validate_certs: true
    plug_id: "all"

# Get Plug status for port 2
- name: Get the Plug status for the given port of a WTI device
  cpm_plugcontrol:
    cpm_action: "getplugcontrol"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    validate_certs: false
    plug_id: "2"

# Reboot plug 5
- name: Reboot Plug 5 on a given WTI device
  cpm_plugcontrol:
    cpm_action: "setplugcontrol"
    cpm_url: "rest.wti.com"
    cpm_username: "restpower"
    cpm_password: "restfulpowerpass12"
    use_https: true
    plug_id: "5"
    plug_state: "boot"
```

## [Return Values](cpm_plugcontrol_module.md#id4)

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
