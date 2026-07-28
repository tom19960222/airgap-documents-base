---
collection: ansible
version: "8"
title: "community.sap_libs.sap_pyrfc module – Ansible Module for use of SAP PyRFC to execute SAP RFCs (Remote Function Calls) to SAP remote-enabled function modules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/sap_libs/sap_pyrfc_module.html
fetched_at: 2026-07-28T01:59:16+00:00
---
# community.sap_libs.sap_pyrfc module – Ansible Module for use of SAP PyRFC to execute SAP RFCs (Remote Function Calls) to SAP remote-enabled function modules

> **Note:**
>
> This module is part of the [community.sap_libs collection](https://galaxy.ansible.com/ui/repo/published/community/sap_libs/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap_libs`.
> You need further requirements to be able to use this module,
> see [Requirements](sap_pyrfc_module.md#ansible-collections-community-sap-libs-sap-pyrfc-module-requirements) for details.
>
> To use it in a playbook, specify: `community.sap_libs.sap_pyrfc`.

New in community.sap_libs 1.2.0

- [Synopsis](sap_pyrfc_module.md#synopsis)
- [Requirements](sap_pyrfc_module.md#requirements)
- [Parameters](sap_pyrfc_module.md#parameters)
- [Examples](sap_pyrfc_module.md#examples)
- [Return Values](sap_pyrfc_module.md#return-values)

## [Synopsis](sap_pyrfc_module.md#id1)

- This module will executes rfc calls on a sap system.
- It is a generic approach to call rfc functions on a SAP System.
- This module should be used where no module or role is provided.

## [Requirements](sap_pyrfc_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrfc >= 2.4.0

## [Parameters](sap_pyrfc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **connection**  dictionary / required | The required connection details. |
| **ashost**  string / required | The required host for the SAP system. Can be either an FQDN or IP Address. |
| **client**  string / required | The client number to connect to.  You must quote the value to ensure retaining the leading zeros. |
| **lang**  string | The used language to execute. |
| **passwd**  string / required | The required password for the SAP system. |
| **sysid**  string | The systemid of the SAP system. |
| **sysnr**  string / required | The system number of the SAP system.  You must quote the value to ensure retaining the leading zeros. |
| **user**  string / required | The required username for the SAP system. |
| **function**  string / required | The SAP RFC function to call. |
| **parameters**  dictionary / required | The parameters which are needed by the function. |

## [Examples](sap_pyrfc_module.md#id4)

```yaml+jinja
- name: test the pyrfc module
  community.sap_libs.sap_pyrfc:
    function: STFC_CONNECTION
    parameters:
      REQUTEXT: "Hello SAP!"
    connection:
      ashost: s4hana.poc.cloud
      sysid: TDT
      sysnr: "01"
      client: "400"
      user: DDIC
      passwd: Password1
      lang: EN
```

## [Return Values](sap_pyrfc_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **result**  dictionary | The execution description.  **Returned:** always  **Sample:** `{"ECHOTEXT": "Hello SAP!", "RESPTEXT": "SAP R/3 Rel. 756   Sysid: TST      Date: 20220710   Time: 140717   Logon_Data: 000/DDIC/E"}` |

### Authors

- Sean Freeman (@seanfreeman)
- Rainer Leber (@rainerleber)

### Collection links

- [Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
- [Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
