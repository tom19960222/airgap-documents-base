---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_lacp module – Global Link Aggregation Control Protocol (LACP) Junos resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_lacp_module.html
fetched_at: 2026-07-28T02:39:39+00:00
---
# junipernetworks.junos.junos_lacp module – Global Link Aggregation Control Protocol (LACP) Junos resource module

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_lacp_module.md#ansible-collections-junipernetworks-junos-junos-lacp-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_lacp`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_lacp_module.md#synopsis)
- [Requirements](junos_lacp_module.md#requirements)
- [Parameters](junos_lacp_module.md#parameters)
- [Notes](junos_lacp_module.md#notes)
- [Examples](junos_lacp_module.md#examples)
- [Return Values](junos_lacp_module.md#return-values)

## [Synopsis](junos_lacp_module.md#id1)

- This module provides declarative management of global LACP on Juniper Junos network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: lacp

## [Requirements](junos_lacp_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)

## [Parameters](junos_lacp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of LACP global options |
| **link_protection**  string | Enable LACP link-protection for the system. If the value is set to `non-revertive` it will not revert links when a better priority link comes up. By default the link will be reverted.  **Choices:**   - `"revertive"` - `"non-revertive"` |
| **system_priority**  integer | LACP priority for the system. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show chassis aggregated-devices ethernet lacp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state of the configuration after module completion  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](junos_lacp_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 18.1R1.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).

## [Examples](junos_lacp_module.md#id5)

```yaml+jinja
# Using deleted

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }

- name: Delete global LACP attributes
  junipernetworks.junos.junos_lacp:
    state: deleted

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
#

# Using merged

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
#

- name: Merge global LACP attributes
  junipernetworks.junos.junos_lacp:
    config:
      system_priority: 63
      link_protection: revertive
    state: merged

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }

# Using replaced

# Before state:
# -------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection {
#    non-revertive;
# }

- name: Replace global LACP attributes
  junipernetworks.junos.junos_lacp:
    config:
      system_priority: 30
      link_protection: non-revertive
    state: replaced

# After state:
# ------------
# user@junos01# show chassis aggregated-devices ethernet lacp
# system-priority 30;
# link-protection;
#
# Using gathered
# Before state:
# ------------
#
# ansible@cm123456tr21# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection;

- name: Gather junos lacp as in given arguments
  junipernetworks.junos.junos_lacp:
    state: gathered
# Task Output (redacted)
# -----------------------
#
# "gathered": {
#         "link_protection": "revertive",
#         "system_priority": 63
#     }
# After state:
# ------------
#
# ansible@cm123456tr21# show chassis aggregated-devices ethernet lacp
# system-priority 63;
# link-protection;
# Using rendered
- name: Render platform specific xml from task input using rendered state
  junipernetworks.junos.junos_lacp:
    config:
      system_priority: 63
      link_protection: revertive
    state: rendered
# Task Output (redacted)
# -----------------------
# "rendered": "<nc:chassis
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:aggregated-devices>
#         <nc:ethernet>
#             <nc:lacp>
#                 <nc:system-priority>63</nc:system-priority>
#                 <nc:link-protection>
#                     <nc:non-revertive delete="delete"/>
#                 </nc:link-protection>
#             </nc:lacp>
#         </nc:ethernet>
#     </nc:aggregated-devices>
# </nc:chassis>
#
# Using parsed
# parsed.cfg
# ------------
#
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#     <chassis>
#         <aggregated-devices>
#             <ethernet>
#                 <lacp>
#                     <system-priority>63</system-priority>
#                     <link-protection>
#                     </link-protection>
#                 </lacp>
#             </ethernet>
#         </aggregated-devices>
#     </chassis>
#     </configuration>
# </rpc-reply>
# - name: Convert lacp config to argspec without connecting to the appliance
#   junipernetworks.junos.junos_lacp:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
# Task Output (redacted)
# -----------------------
# "parsed": {
#         "link_protection": "revertive",
#         "system_priority": 63
#     }
```

## [Return Values](junos_lacp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **xml**  list / elements=string | The set of xml rpc payload pushed to the remote device.  **Returned:** always  **Sample:** `["<nc:chassis xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:aggregated-devices> <nc:ethernet> <nc:lacp> <nc:system-priority>63</nc:system-priority> <nc:link-protection> <nc:non-revertive delete=\"delete\"/> </nc:link-protection> </nc:lacp> </nc:ethernet> </nc:aggregated-devices> </nc:chassis>", "xml 2", "xml 3"]` |

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
