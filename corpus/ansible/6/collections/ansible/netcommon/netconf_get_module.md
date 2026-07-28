---
collection: ansible
version: "6"
title: "ansible.netcommon.netconf_get module – Fetch configuration/state data from NETCONF enabled network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/netconf_get_module.html
fetched_at: 2026-07-27T16:44:34+00:00
---
# ansible.netcommon.netconf_get module – Fetch configuration/state data from NETCONF enabled network devices.

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
> You need further requirements to be able to use this module,
> see [Requirements](netconf_get_module.md#ansible-collections-ansible-netcommon-netconf-get-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.netconf_get`.

New in ansible.netcommon 1.0.0

- [Synopsis](netconf_get_module.md#synopsis)
- [Requirements](netconf_get_module.md#requirements)
- [Parameters](netconf_get_module.md#parameters)
- [Notes](netconf_get_module.md#notes)
- [Examples](netconf_get_module.md#examples)
- [Return Values](netconf_get_module.md#return-values)

## [Synopsis](netconf_get_module.md#id1)

- NETCONF is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
- This module allows the user to fetch configuration and state data from NETCONF enabled network devices.

## [Requirements](netconf_get_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)
- jxmlease (for display=json)
- xmltodict (for display=native)

## [Parameters](netconf_get_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **display**  string | Encoding scheme to use when serializing output from the device. The option *json* will serialize the output as JSON data. If the option value is *json* it requires jxmlease to be installed on control node. The option *pretty* is similar to received XML response but is using human readable format (spaces, new lines). The option value *xml* is similar to received XML response but removes all XML namespaces.  Choices:   - `"json"` - `"pretty"` - `"xml"` - `"native"` |
| **filter**  any | This argument specifies the string which acts as a filter to restrict the portions of the data to be are retrieved from the remote device. If this option is not specified entire configuration or state data is returned in result depending on the value of `source` option. The `filter` value can be either XML string or XPath or JSON string or native python dictionary, if the filter is in XPath format the NETCONF server running on remote host should support xpath capability else it will result in an error. If the filter is in JSON format the xmltodict library should be installed on the control node for JSON to XML conversion. |
| **lock**  string | Instructs the module to explicitly lock the datastore specified as `source`. If no *source* is defined, the *running* datastore will be locked. By setting the option value *always* is will explicitly lock the datastore mentioned in `source` option. By setting the option value *never* it will not lock the `source` datastore. The value *if-supported* allows better interworking with NETCONF servers, which do not support the (un)lock operation for all supported datastores.  Choices:   - `"never"` ← (default) - `"always"` - `"if-supported"` |
| **source**  string | This argument specifies the datastore from which configuration data should be fetched. Valid values are *running*, *candidate* and *startup*. If the `source` value is not set both configuration and state information are returned in response from running datastore.  Choices:   - `"running"` - `"candidate"` - `"startup"` |

## [Notes](netconf_get_module.md#id4)

> **Note:**
>
> - This module requires the NETCONF system service be enabled on the remote device being managed.
> - This module supports the use of connection=netconf
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](netconf_get_module.md#id5)

```yaml+jinja
- name: Get running configuration and state data
  ansible.netcommon.netconf_get:

- name: Get configuration and state data from startup datastore
  ansible.netcommon.netconf_get:
    source: startup

- name: Get system configuration data from running datastore state (junos)
  ansible.netcommon.netconf_get:
    source: running
    filter: <configuration><system></system></configuration>

- name: Get configuration and state data in JSON format
  ansible.netcommon.netconf_get:
    display: json

- name: get schema list using subtree w/ namespaces
  ansible.netcommon.netconf_get:
    display: json
    filter: <netconf-state xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring"><schemas><schema/></schemas></netconf-state>
    lock: never

- name: get schema list using xpath
  ansible.netcommon.netconf_get:
    display: xml
    filter: /netconf-state/schemas/schema

- name: get interface configuration with filter (iosxr)
  ansible.netcommon.netconf_get:
    display: pretty
    filter: <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"></interface-configurations>
    lock: if-supported

- name: Get system configuration data from running datastore state (junos)
  ansible.netcommon.netconf_get:
    source: running
    filter: <configuration><system></system></configuration>
    lock: if-supported

- name: Get complete configuration data from running datastore (SROS)
  ansible.netcommon.netconf_get:
    source: running
    filter: <configure xmlns="urn:nokia.com:sros:ns:yang:sr:conf"/>

- name: Get complete state data (SROS)
  ansible.netcommon.netconf_get:
    filter: <state xmlns="urn:nokia.com:sros:ns:yang:sr:state"/>

- name: "get configuration with json filter string and native output (using xmltodict)"
  netconf_get:
    filter: |
              {
                  "interface-configurations": {
                      "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
                      "interface-configuration": null
                  }
              }
    display: native

- name: Define the Cisco IOSXR interface filter
  set_fact:
    filter:
      interface-configurations:
        "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"
        interface-configuration: null

- name: "get configuration with native filter type using set_facts"
  ansible.netcommon.netconf_get:
    filter: "{{ filter }}"
    display: native
  register: result

- name: "get configuration with direct native filter type"
  ansible.netcommon.netconf_get:
    filter: {
            "interface-configurations": {
            "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
            "interface-configuration": null
      }
    }
    display: native
  register: result

# Make a round-trip interface description change, diff the before and after
# this demonstrates the use of the native display format and several utilities
# from the ansible.utils collection

- name: Define the openconfig interface filter
  set_fact:
    filter:
      interfaces:
        "@xmlns": "http://openconfig.net/yang/interfaces"
        interface:
          name: Ethernet2

- name: Get the pre-change config using the filter
  ansible.netcommon.netconf_get:
    source: running
    filter: "{{ filter }}"
    display: native
  register: pre

- name: Update the description
  ansible.utils.update_fact:
    updates:
    - path: pre.output.data.interfaces.interface.config.description
      value: "Configured by ansible {{ 100 | random }}"
  register: updated

- name: Apply the new configuration
  ansible.netcommon.netconf_config:
    content:
      config:
        interfaces: "{{ updated.pre.output.data.interfaces }}"

- name: Get the post-change config using the filter
  ansible.netcommon.netconf_get:
    source: running
    filter: "{{ filter }}"
    display: native
  register: post

- name: Show the differences between the pre and post configurations
  ansible.utils.fact_diff:
    before: "{{ pre.output.data|ansible.utils.to_paths }}"
    after: "{{ post.output.data|ansible.utils.to_paths }}"

# TASK [Show the differences between the pre and post configurations] ********
# --- before
# +++ after
# @@ -1,11 +1,11 @@
#  {
# -    "@time-modified": "2020-10-23T12:27:17.462332477Z",
# +    "@time-modified": "2020-10-23T12:27:21.744541708Z",
#      "@xmlns": "urn:ietf:params:xml:ns:netconf:base:1.0",
#      "interfaces.interface.aggregation.config['fallback-timeout']['#text']": "90",
#      "interfaces.interface.aggregation.config['fallback-timeout']['@xmlns']": "http://arista.com/yang/openconfig/interfaces/augments",
#      "interfaces.interface.aggregation.config['min-links']": "0",
#      "interfaces.interface.aggregation['@xmlns']": "http://openconfig.net/yang/interfaces/aggregate",
# -    "interfaces.interface.config.description": "Configured by ansible 56",
# +    "interfaces.interface.config.description": "Configured by ansible 67",
#      "interfaces.interface.config.enabled": "true",
#      "interfaces.interface.config.mtu": "0",
#      "interfaces.interface.config.name": "Ethernet2",
```

## [Return Values](netconf_get_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  complex | Based on the value of display option will return either the set of transformed XML to JSON format from the RPC response with type dict or pretty XML string response (human-readable) or response with namespace removed from XML string.  Returned: If the display format is selected as *json* it is returned as dict type and the conversion is done using jxmlease python library. If the display format is selected as *native* it is returned as dict type and the conversion is done using xmltodict python library. If the display format is xml or pretty it is returned as a string apart from low-level errors (such as action plugin). |
| **formatted_output**  string | Contains formatted response received from remote host as per the value in display format.  Returned: success |
| **stdout**  string | The raw XML string containing configuration or state data received from the underlying ncclient library.  Returned: always apart from low-level errors (such as action plugin)  Sample: `"..."` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low-level errors (such as action plugin)  Sample: `["...", "..."]` |

### Authors

- Ganesh Nalawade (@ganeshrn)
- Sven Wisotzky (@wisotzky)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
