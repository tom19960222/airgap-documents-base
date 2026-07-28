---
collection: ansible
version: "6"
title: "community.sap_libs.sap_snote module – This module will upload and (de)implements SNOTES in a SAP S4HANA environment."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sap_libs/sap_snote_module.html
fetched_at: 2026-07-27T17:21:04+00:00
---
# community.sap_libs.sap_snote module – This module will upload and (de)implements `SNOTES` in a SAP S4HANA environment.

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
> see [Requirements](sap_snote_module.md#ansible-collections-community-sap-libs-sap-snote-module-requirements) for details.
>
> To use it in a playbook, specify: `community.sap_libs.sap_snote`.

New in community.sap_libs 1.0.0

- [Synopsis](sap_snote_module.md#synopsis)
- [Requirements](sap_snote_module.md#requirements)
- [Parameters](sap_snote_module.md#parameters)
- [Examples](sap_snote_module.md#examples)
- [Return Values](sap_snote_module.md#return-values)

## [Synopsis](sap_snote_module.md#id1)

- The `sap_snote` module depends on `pyrfc` Python library (version 2.4.0 and upwards). Depending on distribution you are using, you may need to install additional packages to have these available.
- This module will use the Function Group `SCWB_API`.
- The `TMS` must be configured at first.
- Integrating SNOTES cannot be done via `DDIC`- or `SAP*`-User.

## [Requirements](sap_snote_module.md#id2)

The below requirements are needed on the host that executes this module.

- pyrfc >= 2.4.0

## [Parameters](sap_snote_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client**  string | The client number to connect to.  You must quote the value to ensure retaining the leading zeros.  Default: `"000"` |
| **conn_password**  string / required | The required password for the SAP system. |
| **conn_username**  string / required | The required username for the SAP system. |
| **host**  string / required | The required host for the SAP system. Can be either an FQDN or IP Address. |
| **snote**  string | With the `snote` paramter only implementation and deimplementation will work.  Upload SNOTES to the System is only available if `snote_path` is provided. |
| **snote_path**  string | The path to the extracted SNOTE txt file.  The File could be extracted from SAR package.  If `snote_path` is not provided, the `snote` parameter must be defined.  The SNOTE txt file must be at a place where the SAP System is authorized for. For example `/usr/sap/trans/files`. |
| **state**  string | The decision what to do with the SNOTE.  Could be `'present'`, `'absent'`  Choices:   - `"present"` ← (default) - `"absent"` |
| **sysnr**  string | The system number of the SAP system.  You must quote the value to ensure retaining the leading zeros.  Default: `"01"` |

## [Examples](sap_snote_module.md#id4)

```yaml+jinja
- name: test snote module
  hosts: localhost
  tasks:
  - name: implement SNOTE
    community.sap_libs.sap_snote:
      conn_username: 'DDIC'
      conn_password: 'Passwd1234'
      host: 192.168.1.100
      sysnr: '01'
      client: '000'
      state: present
      snote_path: /usr/sap/trans/tmp/0002949148.txt

- name: test snote module without path
  hosts: localhost
  tasks:
  - name: deimplement SNOTE
    community.sap_libs.sap_snote:
      conn_username: 'DDIC'
      conn_password: 'Passwd1234'
      host: 192.168.1.100
      sysnr: '01'
      client: '000'
      state: absent
      snote: 0002949148
```

## [Return Values](sap_snote_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | A small execution description.  Returned: always  Sample: `"SNOTE 000298026 implemented."` |
| **out**  list / elements=dictionary | A complete description of the SNOTE implementation. If this is available.  Returned: always  Sample: `"{ \"RETURN\": [{\"ES_MSG\": { \"MSGNO\": \"000\", \"MSGTY\": \"\", \"MSGTXT\": \"\", \"MSGV1\": \"\" }, \"ET_MSG\": [], \"EV_RC\": 0, \"ET_MISSING_NOTES\": [], \"IT_FILENAME\": [{\"FILENAME\": \"/usr/sap/trans/tmp/0002980265.txt\"}], \"IT_NOTES\": [{\"NUMM\": \"0002980265\", \"VERSNO\": \"0000\"}] }]}"` |

### Authors

- Rainer Leber (@rainerleber)

### Collection links

[Issue Tracker](https://github.com/sap-linuxlab/community.sap_libs)
[Repository (Sources)](https://github.com/sap-linuxlab/community.sap_libs)
