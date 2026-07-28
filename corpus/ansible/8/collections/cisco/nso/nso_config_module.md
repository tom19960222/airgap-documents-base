---
collection: ansible
version: "8"
title: "cisco.nso.nso_config module – Manage Cisco NSO configuration and service synchronization."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nso/nso_config_module.html
fetched_at: 2026-07-28T01:38:22+00:00
---
# cisco.nso.nso_config module – Manage Cisco NSO configuration and service synchronization.

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
> see [Requirements](nso_config_module.md#ansible-collections-cisco-nso-nso-config-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.nso.nso_config`.

- [Synopsis](nso_config_module.md#synopsis)
- [Requirements](nso_config_module.md#requirements)
- [Parameters](nso_config_module.md#parameters)
- [See Also](nso_config_module.md#see-also)
- [Examples](nso_config_module.md#examples)
- [Return Values](nso_config_module.md#return-values)

## [Synopsis](nso_config_module.md#id1)

- This module provides support for managing configuration in Cisco NSO and can also ensure services are in sync.

## [Requirements](nso_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- Cisco NSO version 3.4.12 or higher, 4.2.7 or higher, 4.3.8 or higher, 4.4.3 or higher, 4.5 or higher.

## [Parameters](nso_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commit_flags**  list / elements=string | A list containing commit flags. See the API documentation for supported commit flags. <https://developer.cisco.com/docs/nso/guides/#!life-cycle-operations-how-to-manipulate-existing-services-and-devices/commit-flags-and-device-service-actions> |
| **data**  dictionary / required | NSO data in format as | display json converted to YAML. List entries can be annotated with a __state entry. Set to in-sync/deep-in-sync for services to verify service is in sync with the network. Set to absent in list entries to ensure they are deleted if they exist in NSO. |
| **password**  string / required | NSO password |
| **timeout**  integer | JSON-RPC request timeout in seconds  **Default:** `300` |
| **url**  string / required | NSO JSON-RPC URL, <http://localhost:8080/jsonrpc> |
| **username**  string / required | NSO username |
| **validate_certs**  boolean | When set to true, validates the SSL certificate of NSO when using SSL  **Choices:**   - `false` ← (default) - `true` |

## [See Also](nso_config_module.md#id4)

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

## [Examples](nso_config_module.md#id5)

```yaml+jinja
- name: CREATE DEVICE IN NSO
  cisco.nso.nso_config:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    data:
      tailf-ncs:devices:
        device:
        - address: 10.10.20.175
          description: CONFIGURED BY ANSIBLE!
          name: dist-rtr01
          authgroup: "labadmin"
          device-type:
            cli:
              ned-id: "cisco-ios-cli-6.44"
            port: "22"
            state:
              admin-state: "unlocked"

- name: ADD NEW LOOPBACK
  cisco.nso.nso_config:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    data:
        tailf-ncs:devices:
        device:
        - name: dist-rtr01
          config:
            tailf-ned-cisco-ios:interface:
                Loopback:
                - name: "1"
                  description: Created by Ansible!

- name: CONFIGURE IP ADDRESS ON LOOPBACK
  cisco.nso.nso_config:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    data:
      tailf-ncs:devices:
        device:
        - name: dist-rtr01
          config:
            tailf-ned-cisco-ios:interface:
              Loopback:
              - name: "1"
                description: Created by Ansible!
                ip:
                  address:
                    primary:
                      address: 10.10.10.10
                      mask: 255.255.255.255

- name: CONFIGURE NTP SERVER ON DEVICE
  cisco.nso.nso_config:
    url: https://10.10.20.49/jsonrpc
    username: developer
    password: C1sco12345
    data:
      tailf-ncs:devices:
        device:
        - name: dist-rtr01
          config:
            tailf-ned-cisco-ios:ntp:
              server:
                peer-list:
                  - name: 2.2.2.2
```

## [Return Values](nso_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changes**  complex | List of changes  **Returned:** always  **Sample:** `[{"from": null, "path": "/ncs:devices/device{dist-rtr01}/config/ios:interface/Loopback{1}/ip/address/primary/address", "to": "10.10.10.10", "type": "set"}]` |
| **from**  string | Previous value if any, else null  **Returned:** When previous value is present on value change |
| **path**  string | Path to value changed  **Returned:** always |
| **commit_result**  complex | Return values from commit operation  **Returned:** always  **Sample:** `[{"commit_queue": {"id": 1611776004976, "status": "async"}}]` |
| **commit_queue**  dictionary | Commit queue ID and status, if any  **Returned:** When commit-queue is set in commit_flags |
| **diffs**  complex | List of sync changes  **Returned:** always |
| **diff**  string | configuration difference triggered the re-deploy  **Returned:** always |
| **path**  string | keypath to service changed  **Returned:** always |

### Authors

- Claes Nästén (@cnasten)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-nso/issues)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-nso)
