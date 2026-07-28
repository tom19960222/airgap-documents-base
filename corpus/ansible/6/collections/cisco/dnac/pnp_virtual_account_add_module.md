---
collection: ansible
version: "6"
title: "cisco.dnac.pnp_virtual_account_add module – Resource module for Pnp Virtual Account Add"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/pnp_virtual_account_add_module.html
fetched_at: 2026-07-27T16:53:20+00:00
---
# cisco.dnac.pnp_virtual_account_add module – Resource module for Pnp Virtual Account Add

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](pnp_virtual_account_add_module.md#ansible-collections-cisco-dnac-pnp-virtual-account-add-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.pnp_virtual_account_add`.

New in cisco.dnac 3.1.0

- [Synopsis](pnp_virtual_account_add_module.md#synopsis)
- [Requirements](pnp_virtual_account_add_module.md#requirements)
- [Parameters](pnp_virtual_account_add_module.md#parameters)
- [Notes](pnp_virtual_account_add_module.md#notes)
- [See Also](pnp_virtual_account_add_module.md#see-also)
- [Examples](pnp_virtual_account_add_module.md#examples)
- [Return Values](pnp_virtual_account_add_module.md#return-values)

## [Synopsis](pnp_virtual_account_add_module.md#id1)

- Manage operation create of the resource Pnp Virtual Account Add.
- Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database. The devices present in the registered virtual account are synced with the PnP database as well. The response payload returns the new profile.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](pnp_virtual_account_add_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](pnp_virtual_account_add_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoSyncPeriod**  integer | Pnp Virtual Account Add’s autoSyncPeriod. |
| **ccoUser**  string | Pnp Virtual Account Add’s ccoUser. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **expiry**  integer | Pnp Virtual Account Add’s expiry. |
| **lastSync**  integer | Pnp Virtual Account Add’s lastSync. |
| **profile**  dictionary | Pnp Virtual Account Add’s profile. |
| **addressFqdn**  string | Pnp Virtual Account Add’s addressFqdn. |
| **addressIpV4**  string | Pnp Virtual Account Add’s addressIpV4. |
| **cert**  string | Pnp Virtual Account Add’s cert. |
| **makeDefault**  boolean | MakeDefault flag.  Choices:   - `false` - `true` |
| **name**  string | Pnp Virtual Account Add’s name. |
| **port**  integer | Pnp Virtual Account Add’s port. |
| **profileId**  string | Pnp Virtual Account Add’s profileId. |
| **proxy**  boolean | Proxy flag.  Choices:   - `false` - `true` |
| **smartAccountId**  string | Pnp Virtual Account Add’s smartAccountId. |
| **syncResult**  dictionary | Pnp Virtual Account Add’s syncResult. |
| **syncList**  list / elements=dictionary | Pnp Virtual Account Add’s syncList. |
| **deviceSnList**  list / elements=string | Pnp Virtual Account Add’s deviceSnList. |
| **syncType**  string | Pnp Virtual Account Add’s syncType. |
| **syncMsg**  string | Pnp Virtual Account Add’s syncMsg. |
| **syncResultStr**  string | Pnp Virtual Account Add’s syncResultStr. |
| **syncStartTime**  integer | Pnp Virtual Account Add’s syncStartTime. |
| **syncStatus**  string | Pnp Virtual Account Add’s syncStatus. |
| **tenantId**  string | Pnp Virtual Account Add’s tenantId. |
| **token**  string | Pnp Virtual Account Add’s token. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |
| **virtualAccountId**  string | Pnp Virtual Account Add’s virtualAccountId. |

## [Notes](pnp_virtual_account_add_module.md#id4)

> **Note:**
>
> - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.add_virtual_account,
> - Paths used are post /dna/intent/api/v1/onboarding/pnp-settings/savacct,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](pnp_virtual_account_add_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Device Onboarding (PnP) AddVirtualAccount](https://developer.cisco.com/docs/dna-center/#!add-virtual-account)
> :   Complete reference of the AddVirtualAccount API.

## [Examples](pnp_virtual_account_add_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.pnp_virtual_account_add:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    autoSyncPeriod: 0
    ccoUser: string
    expiry: 0
    lastSync: 0
    profile:
      addressFqdn: string
      addressIpV4: string
      cert: string
      makeDefault: true
      name: string
      port: 0
      profileId: string
      proxy: true
    smartAccountId: string
    syncResult:
      syncList:
      - deviceSnList:
        - string
        syncType: string
      syncMsg: string
    syncResultStr: string
    syncStartTime: 0
    syncStatus: string
    tenantId: string
    token: string
    virtualAccountId: string
```

## [Return Values](pnp_virtual_account_add_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"autoSyncPeriod": 0, "ccoUser": "string", "expiry": 0, "lastSync": 0, "profile": {"addressFqdn": "string", "addressIpV4": "string", "cert": "string", "makeDefault": true, "name": "string", "port": 0, "profileId": "string", "proxy": true}, "smartAccountId": "string", "syncResult": {"syncList": [{"deviceSnList": ["string"], "syncType": "string"}], "syncMsg": "string"}, "syncResultStr": "string", "syncStartTime": 0, "syncStatus": "string", "tenantId": "string", "token": "string", "virtualAccountId": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
