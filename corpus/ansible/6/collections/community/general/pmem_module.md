---
collection: ansible
version: "6"
title: "community.general.pmem module – Configure Intel Optane Persistent Memory modules"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pmem_module.html
fetched_at: 2026-07-27T17:11:58+00:00
---
# community.general.pmem module – Configure Intel Optane Persistent Memory modules

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pmem_module.md#ansible-collections-community-general-pmem-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pmem`.

New in community.general 4.5.0

- [Synopsis](pmem_module.md#synopsis)
- [Requirements](pmem_module.md#requirements)
- [Parameters](pmem_module.md#parameters)
- [Examples](pmem_module.md#examples)
- [Return Values](pmem_module.md#return-values)

## [Synopsis](pmem_module.md#id1)

- This module allows Configuring Intel Optane Persistent Memory modules (PMem) using ipmctl and ndctl command line tools.

## [Requirements](pmem_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipmctl and ndctl command line tools
- xmltodict

## [Parameters](pmem_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **appdirect**  integer | Percentage of the total capacity to use in AppDirect Mode (`0`-`100`).  Create AppDirect capacity utilizing hardware interleaving across the requested PMem modules if applicable given the specified target.  Total of *appdirect*, *memorymode* and *reserved* must be `100` |
| **appdirect_interleaved**  boolean | Create AppDirect capacity that is interleaved any other PMem modules.  Choices:   - `false` - `true` ← (default) |
| **memorymode**  integer | Percentage of the total capacity to use in Memory Mode (`0`-`100`). |
| **namespace**  list / elements=dictionary | This enables to set the configuration for the namespace of the PMem. |
| **mode**  string / required | The mode of namespace. The detail of the mode is in the man page of ndctl-create-namespace.  Choices:   - `"raw"` - `"sector"` - `"fsdax"` - `"devdax"` |
| **size**  string | The size of namespace. This option supports the suffixes `k` or `K` or `KB` for KiB, `m` or `M` or `MB` for MiB, `g` or `G` or `GB` for GiB and `t` or `T` or `TB` for TiB.  This option is required if multiple namespaces are configured.  If this option is not set, all of the available space of a region is configured. |
| **type**  string | The type of namespace. The detail of the type is in the man page of ndctl-create-namespace.  Choices:   - `"pmem"` - `"blk"` |
| **namespace_append**  boolean | Enable to append the new namespaces to the system.  The default is `false` so the all existing namespaces not listed in *namespace* are removed.  Choices:   - `false` ← (default) - `true` |
| **reserved**  integer | Percentage of the capacity to reserve (`0`-`100`). *reserved* will not be mapped into the system physical address space and will be presented as reserved capacity with Show Device and Show Memory Resources Commands.  *reserved* will be set automatically if this is not configured. |
| **socket**  list / elements=dictionary | This enables to set the configuration for each socket by using the socket ID.  Total of *appdirect*, *memorymode* and *reserved* must be `100` within one socket. |
| **appdirect**  integer / required | Percentage of the total capacity to use in AppDirect Mode (`0`-`100`) within the socket ID. |
| **appdirect_interleaved**  boolean | Create AppDirect capacity that is interleaved any other PMem modules within the socket ID.  Choices:   - `false` - `true` ← (default) |
| **id**  integer / required | The socket ID of the PMem module. |
| **memorymode**  integer / required | Percentage of the total capacity to use in Memory Mode (`0`-`100`) within the socket ID. |
| **reserved**  integer | Percentage of the capacity to reserve (`0`-`100`) within the socket ID. |

## [Examples](pmem_module.md#id4)

```yaml+jinja
- name: Configure the Pmem as AppDirect 10, Memory Mode 70, and the Reserved 20 percent.
  community.general.pmem:
    appdirect: 10
    memorymode: 70

- name: Configure the Pmem as AppDirect 10, Memory Mode 80, and the Reserved 10 percent.
  community.general.pmem:
    appdirect: 10
    memorymode: 80
    reserved: 10

- name: Configure the Pmem as AppDirect with not interleaved 10, Memory Mode 70, and the Reserved 20 percent.
  community.general.pmem:
    appdirect: 10
    appdirect_interleaved: false
    memorymode: 70

- name: Configure the Pmem each socket.
  community.general.pmem:
    socket:
      - id: 0
        appdirect: 10
        appdirect_interleaved: false
        memorymode: 70
        reserved: 20
      - id: 1
        appdirect: 10
        memorymode: 80
        reserved: 10

- name: Configure the two namespaces.
  community.general.pmem:
    namespace:
      - size: 1GB
        type: pmem
        mode: raw
      - size: 320MB
        type: pmem
        mode: sector
```

## [Return Values](pmem_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **reboot_required**  boolean | Indicates that the system reboot is required to complete the PMem configuration.  Returned: success  Sample: `true` |
| **result**  list / elements=dictionary | Shows the value of AppDirect, Memory Mode and Reserved size in bytes.  If *socket* argument is provided, shows the values in each socket with `socket` which contains the socket ID.  If *namespace* argument is provided, shows the detail of each namespace.  Returned: success  Sample: `[{"appdirect": 111669149696, "memorymode": 970662608896, "reserved": 3626500096, "socket": 0}, {"appdirect": 111669149696, "memorymode": 970662608896, "reserved": 3626500096, "socket": 1}]` |
| **appdirect**  integer | AppDirect size in bytes.  Returned: success |
| **memorymode**  integer | Memory Mode size in bytes.  Returned: success |
| **namespace**  list / elements=string | The list of the detail of namespace.  Returned: success |
| **reserved**  integer | Reserved size in bytes.  Returned: success |
| **socket**  integer | The socket ID to be configured.  Returned: success |

### Authors

- Masayoshi Mizuma (@mizumm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
