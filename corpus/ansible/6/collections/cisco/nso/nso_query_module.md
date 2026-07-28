---
collection: ansible
version: "6"
title: "cisco.nso.nso_query module – Query data from Cisco NSO."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nso/nso_query_module.html
fetched_at: 2026-07-27T17:01:30+00:00
---
# cisco.nso.nso_query module – Query data from Cisco NSO.

> **Note:**
>
> This module is part of the [cisco.nso collection](https://galaxy.ansible.com/cisco/nso) (version 1.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nso`.
> You need further requirements to be able to use this module,
> see [Requirements](nso_query_module.md#ansible-collections-cisco-nso-nso-query-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nso.nso_query`.

- [Synopsis](nso_query_module.md#synopsis)
- [Requirements](nso_query_module.md#requirements)
- [Parameters](nso_query_module.md#parameters)
- [See Also](nso_query_module.md#see-also)
- [Examples](nso_query_module.md#examples)
- [Return Values](nso_query_module.md#return-values)

## [Synopsis](nso_query_module.md#id1)

- This module provides support for querying data from Cisco NSO using XPath.

## [Requirements](nso_query_module.md#id2)

The below requirements are needed on the host that executes this module.

- Cisco NSO version 3.4 or higher.

## [Parameters](nso_query_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **fields**  list / elements=string / required | List of fields to select from matching nodes. |
| **password**  string / required | NSO password |
| **timeout**  integer | JSON-RPC request timeout in seconds  Default: `300` |
| **url**  string / required | NSO JSON-RPC URL, <http://localhost:8080/jsonrpc> |
| **username**  string / required | NSO username |
| **validate_certs**  boolean | When set to true, validates the SSL certificate of NSO when using SSL  Choices:   - `false` ← (default) - `true` |
| **xpath**  string / required | XPath selection relative to the root. |

## [See Also](nso_query_module.md#id4)

> **See also:**
>
> [Cisco DevNet NSO Sandbox](https://blogs.cisco.com/developer/nso-learning-lab-and-sandbox)
> :   Provides a reservable pod with NSO, virtual network topology simulated with Cisco CML and a Linux host running Ansible
>
> [NSO Developer Resources on DevNet](https://developer.cisco.com/docs/nso/)
> :   Documentation for getting started using NSO
>
> [NSO Developer Hub](https://community.cisco.com/t5/nso-developer-hub/ct-p/5672j-dev-nso)
> :   Collaboration community portal for NSO developers
>
> [NSO Developer Github](https://github.com/NSO-developer/)
> :   Code for NSO on Github

## [Examples](nso_query_module.md#id5)

```yaml+jinja
- name: QUERY DEVICES DISPLAYING NAME AND DESCRIPTION
  cisco.nso.nso_query:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    xpath: /ncs:devices/device
    fields:
    - name
    - description
  register: nso_query_result

- name: DISPLAY NSO_QUERY RESULT
  debug:
    var: nso_query_result
```

## [Return Values](nso_query_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  list / elements=string | Value of matching nodes  Returned: success |

### Authors

- Claes Nästén (@cnasten)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-nso/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-nso)
