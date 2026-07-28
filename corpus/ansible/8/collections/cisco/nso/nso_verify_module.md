---
collection: ansible
version: "8"
title: "cisco.nso.nso_verify module – Verifies Cisco NSO configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nso/nso_verify_module.html
fetched_at: 2026-07-28T01:38:24+00:00
---
# cisco.nso.nso_verify module – Verifies Cisco NSO configuration.

> **Note:**
>
> This module is part of the [cisco.nso collection](https://galaxy.ansible.com/ui/repo/published/cisco/nso/) (version 1.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nso`.
> You need further requirements to be able to use this module,
> see [Requirements](nso_verify_module.md#ansible-collections-cisco-nso-nso-verify-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nso.nso_verify`.

- [Synopsis](nso_verify_module.md#synopsis)
- [Requirements](nso_verify_module.md#requirements)
- [Parameters](nso_verify_module.md#parameters)
- [See Also](nso_verify_module.md#see-also)
- [Examples](nso_verify_module.md#examples)
- [Return Values](nso_verify_module.md#return-values)

## [Synopsis](nso_verify_module.md#id1)

- This module provides support for verifying Cisco NSO configuration is in compliance with specified values.

## [Requirements](nso_verify_module.md#id2)

The below requirements are needed on the host that executes this module.

- Cisco NSO version 3.4.12 or higher, 4.2.7 or higher, 4.3.8 or higher, 4.4.3 or higher, 4.5 or higher.

## [Parameters](nso_verify_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  dictionary / required | NSO data in format as `| display json` converted to YAML. List entries can be annotated with a `__state` entry. Set to in-sync/deep-in-sync for services to verify service is in sync with the network. Set to absent in list entries to ensure they are deleted if they exist in NSO. |
| **password**  string / required | NSO password |
| **timeout**  integer | JSON-RPC request timeout in seconds  **Default:** `300` |
| **url**  string / required | NSO JSON-RPC URL, <http://localhost:8080/jsonrpc> |
| **username**  string / required | NSO username |
| **validate_certs**  boolean | When set to true, validates the SSL certificate of NSO when using SSL  **Choices:**   - `false` ← (default) - `true` |

## [See Also](nso_verify_module.md#id4)

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

## [Examples](nso_verify_module.md#id5)

```yaml+jinja
- name: VERIFY INTERFACE IS ADMINISTRATIVELY UP
  cisco.nso.nso_verify:
    url: http://localhost:8080/jsonrpc
    username: username
    password: password
    data:
      tailf-ncs:devices:
        device:
        - name: dist-sw01
          config:
            interface:
              Ethernet:
                - name: "1/1"
                  shutdown: false
```

## [Return Values](nso_verify_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **violations**  complex | List of value violations  **Returned:** failed  **Sample:** `[{"expected-value": false, "path": "/ncs:devices/device{dist-sw01}/config/interface/Ethernet{1/1}/shutdown", "value": true}]` |
| **expected-value**  string | Expected value of path  **Returned:** always |
| **path**  string | Path to the value in violation  **Returned:** always |
| **value**  string | Current value of path  **Returned:** always |

### Authors

- Claes Nästén (@cnasten)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-nso/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-nso)
