---
collection: ansible
version: "8"
title: "community.general.spectrum_model_attrs module – Enforce a model’s attributes in CA Spectrum"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/spectrum_model_attrs_module.html
fetched_at: 2026-07-28T01:50:44+00:00
---
# community.general.spectrum_model_attrs module – Enforce a model’s attributes in CA Spectrum

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](spectrum_model_attrs_module.md#ansible-collections-community-general-spectrum-model-attrs-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.spectrum_model_attrs`.

New in community.general 2.5.0

- [Synopsis](spectrum_model_attrs_module.md#synopsis)
- [Requirements](spectrum_model_attrs_module.md#requirements)
- [Parameters](spectrum_model_attrs_module.md#parameters)
- [Attributes](spectrum_model_attrs_module.md#attributes)
- [Notes](spectrum_model_attrs_module.md#notes)
- [Examples](spectrum_model_attrs_module.md#examples)
- [Return Values](spectrum_model_attrs_module.md#return-values)

## [Synopsis](spectrum_model_attrs_module.md#id1)

- This module can be used to enforce a model’s attributes in CA Spectrum.

Aliases: monitoring.spectrum_model_attrs

## [Requirements](spectrum_model_attrs_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](spectrum_model_attrs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  list / elements=dictionary / required | A list of attribute names and values to enforce.  All values and parameters are case sensitive and must be provided as strings only. |
| **name**  string / required | Attribute name OR hex ID.  Currently defined names are:  `App_Manufacturer` (`0x230683`)  `CollectionsModelNameString` (`0x12adb`)  `Condition` (`0x1000a`)  `Criticality` (`0x1290c`)  `DeviceType` (`0x23000e`)  `isManaged` (`0x1295d`)  `Model_Class` (`0x11ee8`)  `Model_Handle` (`0x129fa`)  `Model_Name` (`0x1006e`)  `Modeltype_Handle` (`0x10001`)  `Modeltype_Name` (`0x10000`)  `Network_Address` (`0x12d7f`)  `Notes` (`0x11564`)  `ServiceDesk_Asset_ID` (`0x12db9`)  `TopologyModelNameString` (`0x129e7`)  `sysDescr` (`0x10052`)  `sysName` (`0x10b5b`)  `Vendor_Name` (`0x11570`)  `Description` (`0x230017`)  Hex IDs are the direct identifiers in Spectrum and will always work.  To lookup hex IDs go to the UI: Locator -> Devices -> By Model Name -> <enter any model> -> Attributes tab. |
| **value**  string / required | Attribute value. Empty strings should be `""` or `null`. |
| **name**  string / required | Model name. |
| **type**  string / required | Model type. |
| **url**  string / required | URL of OneClick server. |
| **url_password**  aliases: password  string / required | OneClick password. |
| **url_username**  aliases: username  string / required | OneClick username. |
| **use_proxy**  boolean | if `false`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  **Choices:**   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Validate SSL certificates. Only change this to `false` if you can guarantee that you are talking to the correct endpoint and there is no man-in-the-middle attack happening.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](spectrum_model_attrs_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](spectrum_model_attrs_module.md#id5)

> **Note:**
>
> - Tested on CA Spectrum version 10.4.2.0.189.
> - Model creation and deletion are not possible with this module. For that use [community.general.spectrum_device](spectrum_device_module.md#ansible-collections-community-general-spectrum-device-module) instead.

## [Examples](spectrum_model_attrs_module.md#id6)

```yaml+jinja
- name: Enforce maintenance mode for modelxyz01 with a note about why
  community.general.spectrum_model_attrs:
    url: "http://oneclick.url.com"
    username: "{{ oneclick_username }}"
    password: "{{ oneclick_password }}"
    name: "modelxyz01"
    type: "Host_Device"
    validate_certs: true
    attributes:
      - name: "isManaged"
        value: "false"
      - name: "Notes"
        value: "MM set on {{ ansible_date_time.iso8601 }} via CO {{ CO }} by {{ tower_user_name | default(ansible_user_id) }}"
  delegate_to: localhost
  register: spectrum_model_attrs_status
```

## [Return Values](spectrum_model_attrs_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed_attrs**  dictionary | Dictionary of changed name or hex IDs (whichever was specified) to their new corresponding values.  **Returned:** always  **Sample:** `{"Notes": "MM set on 2021-02-03T22:04:02Z via CO CO9999 by tgates", "isManaged": "true"}` |
| **msg**  string | Informational message on the job result.  **Returned:** always  **Sample:** `"Success"` |

### Authors

- Tyler Gates (@tgates81)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
