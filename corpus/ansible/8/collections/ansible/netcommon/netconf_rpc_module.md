---
collection: ansible
version: "8"
title: "ansible.netcommon.netconf_rpc module – Execute operations on NETCONF enabled network devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/netconf_rpc_module.html
fetched_at: 2026-07-28T01:09:10+00:00
---
# ansible.netcommon.netconf_rpc module – Execute operations on NETCONF enabled network devices.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](netconf_rpc_module.md#ansible-collections-ansible-netcommon-netconf-rpc-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.netconf_rpc`.

New in ansible.netcommon 1.0.0

- [Synopsis](netconf_rpc_module.md#synopsis)
- [Requirements](netconf_rpc_module.md#requirements)
- [Parameters](netconf_rpc_module.md#parameters)
- [Notes](netconf_rpc_module.md#notes)
- [Examples](netconf_rpc_module.md#examples)
- [Return Values](netconf_rpc_module.md#return-values)

## [Synopsis](netconf_rpc_module.md#id1)

- NETCONF is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
- This module allows the user to execute NETCONF RPC requests as defined by IETF RFC standards as well as proprietary requests.

## [Requirements](netconf_rpc_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)
- jxmlease

## [Parameters](netconf_rpc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **content**  string | This argument specifies the optional request content (all RPC attributes). The *content* value can either be provided as XML formatted string or as dictionary. |
| **display**  string | Encoding scheme to use when serializing output from the device. The option *json* will serialize the output as JSON data. If the option value is *json* it requires jxmlease to be installed on control node. The option *pretty* is similar to received XML response but is using human readable format (spaces, new lines). The option value *xml* is similar to received XML response but removes all XML namespaces.  **Choices:**   - `"json"` - `"pretty"` - `"xml"` |
| **rpc**  string / required | This argument specifies the request (name of the operation) to be executed on the remote NETCONF enabled device. |
| **xmlns**  string | NETCONF operations not defined in rfc6241 typically require the appropriate XML namespace to be set. In the case the *request* option is not already provided in XML format, the namespace can be defined by the *xmlns* option. |

## [Notes](netconf_rpc_module.md#id4)

> **Note:**
>
> - This module requires the NETCONF system service be enabled on the remote device being managed.
> - This module supports the use of connection=netconf
> - To execute `get-config`, `get` or `edit-config` requests it is recommended to use the Ansible *netconf_get* and *netconf_config* modules.
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](netconf_rpc_module.md#id5)

```yaml+jinja
- name: lock candidate
  ansible.netcommon.netconf_rpc:
    rpc: lock
    content:
      target:
        candidate:

- name: unlock candidate
  ansible.netcommon.netconf_rpc:
    rpc: unlock
    xmlns: urn:ietf:params:xml:ns:netconf:base:1.0
    content: "{'target': {'candidate': None}}"

- name: discard changes
  ansible.netcommon.netconf_rpc:
    rpc: discard-changes

- name: get-schema
  ansible.netcommon.netconf_rpc:
    rpc: get-schema
    xmlns: urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring
    content:
      identifier: ietf-netconf
      version: '2011-06-01'

- name: copy running to startup
  ansible.netcommon.netconf_rpc:
    rpc: copy-config
    content:
      source:
        running:
      target:
        startup:

- name: get schema list with JSON output
  ansible.netcommon.netconf_rpc:
    rpc: get
    content: |
      <filter>
        <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring">
          <schemas/>
        </netconf-state>
      </filter>
    display: json

- name: get schema using XML request
  ansible.netcommon.netconf_rpc:
    rpc: get-schema
    xmlns: urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring
    content: |
      <identifier>ietf-netconf-monitoring</identifier>
      <version>2010-10-04</version>
    display: json
```

## [Return Values](netconf_rpc_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  complex | Based on the value of display option will return either the set of transformed XML to JSON format from the RPC response with type dict or pretty XML string response (human-readable) or response with namespace removed from XML string.  **Returned:** when the display format is selected as JSON it is returned as dict type, if the display format is xml or pretty pretty it is returned as a string apart from low-level errors (such as action plugin). |
| **formatted_output**  string | Contains formatted response received from remote host as per the value in display format.  **Returned:** success |
| **stdout**  string | The raw XML string containing configuration or state data received from the underlying ncclient library.  **Returned:** always apart from low-level errors (such as action plugin)  **Sample:** `"..."` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low-level errors (such as action plugin)  **Sample:** `["...", "..."]` |

### Authors

- Ganesh Nalawade (@ganeshrn)
- Sven Wisotzky (@wisotzky)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
