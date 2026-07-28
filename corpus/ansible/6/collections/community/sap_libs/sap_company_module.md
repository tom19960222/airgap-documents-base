---
collection: ansible
version: "6"
title: "community.sap_libs.sap_company module – This module will manage a company entities in a SAP S4HANA environment"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sap_libs/sap_company_module.html
fetched_at: 2026-07-27T17:21:02+00:00
---
# community.sap_libs.sap_company module – This module will manage a company entities in a SAP S4HANA environment

> **Note:**
>
> This module is part of the [community.sap_libs collection](https://galaxy.ansible.com/community/sap_libs) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.sap_libs`.
> You need further requirements to be able to use this module,
> see [Requirements](sap_company_module.md#ansible-collections-community-sap-libs-sap-company-module-requirements) for details.
>
> To use it in a playbook, specify: `community.sap_libs.sap_company`.

New in community.sap_libs 1.0.0

- [Synopsis](sap_company_module.md#synopsis)
- [Requirements](sap_company_module.md#requirements)
- [Parameters](sap_company_module.md#parameters)
- [Notes](sap_company_module.md#notes)
- [Examples](sap_company_module.md#examples)
- [Return Values](sap_company_module.md#return-values)

## [Synopsis](sap_company_module.md#id1)

- The [community.sap_libs.sap_user](sap_user_module.md#ansible-collections-community-sap-libs-sap-user-module) module depends on `pyrfc` Python library (version 2.4.0 and upwards). Depending on distribution you are using, you may need to install additional packages to have these available.
- This module will use the company BAPIs `BAPI_COMPANY_CLONE` and `BAPI_COMPANY_DELETE` to manage company entities.

## [Requirements](sap_company_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrfc >= 2.4.0

## [Parameters](sap_company_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **city**  string | The city where the company is located. |
| **client**  string | The client number to connect to.  You must quote the value to ensure retaining the leading zeros.  Default: `"000"` |
| **company_id**  string / required | The company id. |
| **conn_password**  string / required | The required password for the SAP system. |
| **conn_username**  string / required | The required username for the SAP system. |
| **country**  string | The country code for the company. For example, `'DE'`. |
| **e_mail**  string | General E-Mail address. |
| **host**  string / required | The required host for the SAP system. Can be either an FQDN or IP Address. |
| **name**  string | The company name. |
| **name_2**  string | Additional company name. |
| **post_code**  string | The post code from the city. |
| **state**  string | The decision what to do with the company.  Choices:   - `"present"` ← (default) - `"absent"` |
| **street**  string | Street where the company is located. |
| **street_no**  string | Street number. |
| **sysnr**  string | The system number of the SAP system.  You must quote the value to ensure retaining the leading zeros.  Default: `"01"` |
| **time_zone**  string | The timezone. |

## [Notes](sap_company_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](sap_company_module.md#id5)

```yaml+jinja
- name: Create SAP Company
  community.sap_libs.sap_company:
    conn_username: 'DDIC'
    conn_password: 'HECtna2021#'
    host: 100.0.201.20
    sysnr: '01'
    client: '000'
    state: present
    company_id: "Comp_ID"
    name: "Test_comp"
    name_2: "LTD"
    country: "DE"
    time_zone: "UTC"
    city: "City"
    post_code: "12345"
    street: "test_street"
    street_no: "1"
    e_mail: "test@test.de"

# pass in a message and have changed true
- name: Delete SAP Company
  community.sap_libs.sap_company:
    conn_username: 'DDIC'
    conn_password: 'HECtna2021#'
    host: 100.0.201.20
    sysnr: '01'
    client: '000'
    state: absent
    company_id: "Comp_ID"
    name: "Test_comp"
    name_2: "LTD"
    country: "DE"
    time_zone: "UTC"
    city: "City"
    post_code: "12345"
    street: "test_street"
    street_no: "1"
    e_mail: "test@test.de"
```

## [Return Values](sap_company_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A small execution description.  Returned: always  Sample: `"Company address COMP_ID created"` |
| **out**  list / elements=dictionary | A complete description of the executed tasks. If this is available.  Returned: always  Sample: `"{ \"RETURN\": [ { \"FIELD\": \"\", \"ID\": \"01\", \"LOG_MSG_NO\": \"000000\", \"LOG_NO\": \"\", \"MESSAGE\": \"Company address COMP_ID created\", \"MESSAGE_V1\": \"COMP_ID\", \"MESSAGE_V2\": \"\", \"MESSAGE_V3\": \"\", \"MESSAGE_V4\": \"\", \"NUMBER\": \"078\", \"PARAMETER\": \"\", \"ROW\": 0, \"SYSTEM\": \"\", \"TYPE\": \"S\" } ] } }"` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

[Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
[Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
