---
collection: ansible
version: "6"
title: "community.network.opx_cps module – CPS operations on networking device running Openswitch (OPX)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/opx_cps_module.html
fetched_at: 2026-07-27T17:19:12+00:00
---
# community.network.opx_cps module – CPS operations on networking device running Openswitch (OPX)

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](opx_cps_module.md#ansible-collections-community-network-opx-cps-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.opx_cps`.

- [Synopsis](opx_cps_module.md#synopsis)
- [Requirements](opx_cps_module.md#requirements)
- [Parameters](opx_cps_module.md#parameters)
- [Examples](opx_cps_module.md#examples)
- [Return Values](opx_cps_module.md#return-values)

## [Synopsis](opx_cps_module.md#id1)

- Executes the given operation on the YANG object, using CPS API in the networking device running OpenSwitch (OPX). It uses the YANG models provided in <https://github.com/open-switch/opx-base-model>.

## [Requirements](opx_cps_module.md#id2)

The below requirements are needed on the host that executes this module.

- cps
- cps_object
- cps_utils

## [Parameters](opx_cps_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attr_data**  string | Attribute Yang path and their corresponding data. |
| **attr_type**  string | Attribute Yang type. |
| **commit_event**  boolean | Attempts to force the auto-commit event to the specified yang object.  Choices:   - `false` ← (default) - `true` |
| **db**  boolean | Queries/Writes the specified yang path from/to the db.  Choices:   - `false` ← (default) - `true` |
| **module_name**  string | Yang path to be configured. |
| **operation**  string | Operation to be performed on the object.  Choices:   - `"delete"` - `"create"` ← (default) - `"set"` - `"action"` - `"get"` |
| **qualifier**  string | A qualifier provides the type of object data to retrieve or act on.  Choices:   - `"target"` ← (default) - `"observed"` - `"proposed"` - `"realtime"` - `"registration"` - `"running"` - `"startup"` |

## [Examples](opx_cps_module.md#id4)

```yaml+jinja
- name: Create VLAN
  community.network.opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "base-if-vlan/if/interfaces/interface/id": 230,
         "if/interfaces/interface/name": "br230",
         "if/interfaces/interface/type": "ianaift:l2vlan"
    }
    operation: "create"
- name: Get VLAN
  community.network.opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "if/interfaces/interface/name": "br230",
    }
    operation: "get"
- name: Modify some attributes in VLAN
  community.network.opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "cps/key_data":
            { "if/interfaces/interface/name": "br230" },
         "dell-if/if/interfaces/interface/untagged-ports": ["e101-008-0"],
    }
    operation: "set"
- name: Delete VLAN
  community.network.opx_cps:
    module_name: "dell-base-if-cmn/if/interfaces/interface"
    attr_data: {
         "if/interfaces/interface/name": "br230",
    }
    operation: "delete"
```

## [Return Values](opx_cps_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commit_event**  boolean | Denotes if auto-commit event is set  Returned: when commit_event is set to True in module options  Sample: `true` |
| **cps_curr_config**  dictionary | Returns the CPS Get output i.e. the running configuration before CPS operation of set/delete is performed  Returned: when CPS operations set, delete  Sample: `[{"data": {"base-if-vlan/if/interfaces/interface/id": 230, "cps/key_data": {"if/interfaces/interface/name": "br230"}, "dell-base-if-cmn/if/interfaces/interface/if-index": 44, "dell-if/if/interfaces/interface/learning-mode": 1, "dell-if/if/interfaces/interface/mtu": 1532, "dell-if/if/interfaces/interface/phys-address": "", "dell-if/if/interfaces/interface/vlan-type": 1, "if/interfaces/interface/enabled": 0, "if/interfaces/interface/type": "ianaift:l2vlan"}, "key": "target/dell-base-if-cmn/if/interfaces/interface"}]` |
| **db**  boolean | Denotes if CPS DB transaction was performed  Returned: when db is set to True in module options  Sample: `true` |
| **diff**  dictionary | The actual configuration that will be pushed comparing the running configuration and input attributes  Returned: when CPS operations set, delete  Sample: `{"cps/key_data": {"if/interfaces/interface/name": "br230"}, "dell-if/if/interfaces/interface/untagged-ports": ["e101-007-0"]}` |
| **response**  list / elements=string | Output from the CPS transaction. Output of CPS Get operation if CPS set/create/delete not done.  Returned: when a CPS transaction is successfully performed.  Sample: `[{"data": {"base-if-vlan/if/interfaces/interface/id": 230, "cps/object-group/return-code": 0, "dell-base-if-cmn/if/interfaces/interface/if-index": 46, "if/interfaces/interface/name": "br230", "if/interfaces/interface/type": "ianaift:l2vlan"}, "key": "target/dell-base-if-cmn/if/interfaces/interface"}]` |

### Authors

- Senthil Kumar Ganesan (@skg-net)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
