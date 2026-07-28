---
collection: ansible
version: "8"
title: "cisco.ise.pan_ha module – Resource module for Pan Ha"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ise/pan_ha_module.html
fetched_at: 2026-07-28T01:29:56+00:00
---
# cisco.ise.pan_ha module – Resource module for Pan Ha

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/ui/repo/published/cisco/ise/) (version 2.6.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](pan_ha_module.md#ansible-collections-cisco-ise-pan-ha-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.pan_ha`.

New in cisco.ise 1.0.0

- [Synopsis](pan_ha_module.md#synopsis)
- [Requirements](pan_ha_module.md#requirements)
- [Parameters](pan_ha_module.md#parameters)
- [Notes](pan_ha_module.md#notes)
- [Examples](pan_ha_module.md#examples)
- [Return Values](pan_ha_module.md#return-values)

## [Synopsis](pan_ha_module.md#id1)

- Manage operations create and delete of the resource Pan Ha.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pan_ha_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.1.1
- python >= 3.5

## [Parameters](pan_ha_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **failedAttempts**  integer | Pan Ha’s failedAttempts. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_single_request_timeout**  integer  *added in cisco.ise 3.0.0* | Timeout (in seconds) for RESTful HTTP requests.  **Default:** `60` |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  *added in cisco.ise 1.1.0* | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  **Choices:**   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  *added in cisco.ise 3.0.0* | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  **Choices:**   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  **Default:** `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  **Choices:**   - `false` - `true` ← (default) |
| **isEnabled**  boolean | IsEnabled flag.  **Choices:**   - `false` - `true` |
| **pollingInterval**  integer | Pan Ha’s pollingInterval. |
| **primaryHealthCheckNode**  string | Pan Ha’s primaryHealthCheckNode. |
| **secondaryHealthCheckNode**  string | Pan Ha’s secondaryHealthCheckNode. |

## [Notes](pan_ha_module.md#id4)

> **Note:**
>
> - SDK Method used are sync_ise_node.ReplicationStatus.get_node_replication_status,
> - Paths used are get /api/v1/replication-status/{node}
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](pan_ha_module.md#id5)

```yaml+jinja
- name: Create
  cisco.ise.pan_ha:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    failedAttempts: 0
    isEnabled: true
    pollingInterval: 0
    primaryHealthCheckNode: string
    secondaryHealthCheckNode: string

- name: Delete all
  cisco.ise.pan_ha:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
```

## [Return Values](pan_ha_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"isEnabled\": true,\n    \"primaryHealthCheckNode\": \"string\",\n    \"secondaryHealthCheckNode\": \"string\",\n    \"pollingInterval\": 0,\n    \"failedAttempts\": 0\n  }\n]\n"` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
- [Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
