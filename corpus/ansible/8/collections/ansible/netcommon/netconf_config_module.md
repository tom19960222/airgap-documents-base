---
collection: ansible
version: "8"
title: "ansible.netcommon.netconf_config module – netconf device configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/netconf_config_module.html
fetched_at: 2026-07-28T01:09:09+00:00
---
# ansible.netcommon.netconf_config module – netconf device configuration

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
> see [Requirements](netconf_config_module.md#ansible-collections-ansible-netcommon-netconf-config-module-requirements) for details.
>
> To use it in a playbook, specify: `ansible.netcommon.netconf_config`.

New in ansible.netcommon 1.0.0

- [Synopsis](netconf_config_module.md#synopsis)
- [Requirements](netconf_config_module.md#requirements)
- [Parameters](netconf_config_module.md#parameters)
- [Notes](netconf_config_module.md#notes)
- [Examples](netconf_config_module.md#examples)
- [Return Values](netconf_config_module.md#return-values)

## [Synopsis](netconf_config_module.md#id1)

- Netconf is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
- This module allows the user to send a configuration XML file to a netconf device, and detects if there was a configuration change.

## [Requirements](netconf_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient

## [Parameters](netconf_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | This argument will cause the module to create a full backup of the current `running-config` from the remote device before any changes are made. If the `backup_options` value is not given, the backup file is written to the `backup` folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.  **Choices:**   - `false` ← (default) - `true` |
| **backup_options**  dictionary | This is a dict object containing configurable options related to backup file path. The value of this option is read only when `backup` is set to *yes*, if `backup` is set to *no* this option will be silently ignored. |
| **dir_path**  path | This option provides the path ending with directory name in which the backup configuration file will be stored. If the directory does not exist it will be first created and the filename is either the value of `filename` or default filename as described in `filename` options description. If the path value is not given in that case a *backup* directory will be created in the current working directory and backup configuration will be copied in `filename` within *backup* directory. |
| **filename**  string | The filename to be used to store the backup configuration. If the filename is not given it will be generated based on the hostname, current time and date in format defined by <hostname>_config.<current-date>@<current-time> |
| **commit**  boolean | This boolean flag controls if the configuration changes should be committed or not after editing the candidate datastore. This option is supported only if remote Netconf server supports :candidate capability. If the value is set to *False* commit won’t be issued after edit-config operation and user needs to handle commit or discard-changes explicitly.  **Choices:**   - `false` - `true` ← (default) |
| **confirm**  integer | This argument will configure a timeout value for the commit to be confirmed before it is automatically rolled back. If the `confirm_commit` argument is set to False, this argument is silently ignored. If the value of this argument is set to 0, the commit is confirmed immediately. The remote host MUST support :candidate and :confirmed-commit capability for this option to .  **Default:** `0` |
| **confirm_commit**  boolean | This argument will execute commit operation on remote device. It can be used to confirm a previous commit.  **Choices:**   - `false` ← (default) - `true` |
| **content**  aliases: xml  any | The configuration data as defined by the device’s data models, the value can be either in xml string format or text format or python dictionary representation of JSON format.  In case of json string format it will be converted to the corresponding xml string using xmltodict library before pushing onto the remote host.  In case the value of this option isn *text* format the format should be supported by remote Netconf server.  If the value of `content` option is in *xml* format in that case the xml value should have *config* as root tag. |
| **default_operation**  string | The default operation for <edit-config> rpc, valid values are *merge*, *replace* and *none*. If the default value is merge, the configuration data in the `content` option is merged at the corresponding level in the `target` datastore. If the value is replace the data in the `content` option completely replaces the configuration in the `target` datastore. If the value is none the `target` datastore is unaffected by the configuration in the config option, unless and until the incoming configuration data uses the `operation` operation to request a different operation.  **Choices:**   - `"merge"` - `"replace"` - `"none"` |
| **delete**  boolean | It instructs the module to delete the configuration from value mentioned in `target` datastore.  **Choices:**   - `false` ← (default) - `true` |
| **error_option**  string | This option controls the netconf server action after an error occurs while editing the configuration.  If *error_option=stop-on-error*, abort the config edit on first error.  If *error_option=continue-on-error*, continue to process configuration data on error. The error is recorded and negative response is generated if any errors occur.  If *error_option=rollback-on-error*, rollback to the original configuration if any error occurs. This requires the remote Netconf server to support the *error_option=rollback-on-error* capability.  **Choices:**   - `"stop-on-error"` ← (default) - `"continue-on-error"` - `"rollback-on-error"` |
| **format**  string | The format of the configuration provided as value of `content`.  In case of json string format it will be converted to the corresponding xml string using xmltodict library before pushing onto the remote host.  In case of *text* format of the configuration should be supported by remote Netconf server.  If the value of `format` options is not given it tries to guess the data format of `content` option as one of *xml* or *json* or *text*.  If the data format is not identified it is set to *xml* by default.  **Choices:**   - `"xml"` - `"text"` - `"json"` |
| **get_filter**  any | This argument specifies the XML string which acts as a filter to restrict the portions of the data retrieved from the remote device when comparing the before and after state of the device following calls to edit_config. When not specified, the entire configuration or state data is returned for comparison depending on the value of `source` option. The `get_filter` value can be either XML string or XPath or JSON string or native python dictionary, if the filter is in XPath format the NETCONF server running on remote host should support xpath capability else it will result in an error. |
| **lock**  string | Instructs the module to explicitly lock the datastore specified as `target`. By setting the option value *always* is will explicitly lock the datastore mentioned in `target` option. It the value is *never* it will not lock the `target` datastore. The value *if-supported* lock the `target` datastore only if it is supported by the remote Netconf server.  **Choices:**   - `"never"` - `"always"` ← (default) - `"if-supported"` |
| **save**  boolean | The `save` argument instructs the module to save the configuration in `target` datastore to the startup-config if changed and if :startup capability is supported by Netconf server.  **Choices:**   - `false` ← (default) - `true` |
| **source_datastore**  aliases: source  string | Name of the configuration datastore to use as the source to copy the configuration to the datastore mentioned by `target` option. The values can be either *running*, *candidate*, *startup* or a remote URL |
| **target**  aliases: datastore  string | Name of the configuration datastore to be edited. - auto, uses candidate and fallback to running - candidate, edit <candidate/> datastore and then commit - running, edit <running/> datastore directly  **Choices:**   - `"auto"` ← (default) - `"candidate"` - `"running"` |
| **validate**  boolean | This boolean flag if set validates the content of datastore given in `target` option. For this option to work remote Netconf server should support :validate capability.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](netconf_config_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - This module supports devices with and without the candidate and confirmed-commit capabilities. It will always use the safer feature.
> - This module supports the use of connection=netconf
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](netconf_config_module.md#id5)

```yaml+jinja
- name: use lookup filter to provide xml configuration
  ansible.netcommon.netconf_config:
    content: "{{ lookup('file', './config.xml') }}"

- name: set ntp server in the device
  ansible.netcommon.netconf_config:
    content: |
      <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
              <ntp>
                  <enabled>true</enabled>
                  <server>
                      <name>ntp1</name>
                      <udp><address>127.0.0.1</address></udp>
                  </server>
              </ntp>
          </system>
      </config>

- name: wipe ntp configuration
  ansible.netcommon.netconf_config:
    content: |
      <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
          <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
              <ntp>
                  <enabled>false</enabled>
                  <server operation="remove">
                      <name>ntp1</name>
                  </server>
              </ntp>
          </system>
      </config>

- name: configure interface while providing different private key file path (for connection=netconf)
  ansible.netcommon.netconf_config:
    backup: yes
  register: backup_junos_location
  vars:
    ansible_private_key_file: /home/admin/.ssh/newprivatekeyfile

- name: configurable backup path
  ansible.netcommon.netconf_config:
    backup: yes
    backup_options:
      filename: backup.cfg
      dir_path: /home/user

- name: "configure using direct native format configuration (cisco iosxr)"
  ansible.netcommon.netconf_config:
    format: json
    content: {
                "config": {
                    "interface-configurations": {
                        "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
                        "interface-configuration": {
                            "active": "act",
                            "description": "test for ansible Loopback999",
                            "interface-name": "Loopback999"
                        }
                    }
                }
            }
    get_filter: {
                  "interface-configurations": {
                      "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
                      "interface-configuration": null
                  }
              }

- name: "configure using json string format configuration (cisco iosxr)"
  ansible.netcommon.netconf_config:
    format: json
    content: |
            {
                "config": {
                    "interface-configurations": {
                        "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
                        "interface-configuration": {
                            "active": "act",
                            "description": "test for ansible Loopback999",
                            "interface-name": "Loopback999"
                        }
                    }
                }
            }
    get_filter: |
            {
                  "interface-configurations": {
                      "@xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
                      "interface-configuration": null
                  }
              }

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

## [Return Values](netconf_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_path**  string | The full path to the backup file  **Returned:** when backup is yes  **Sample:** `"/playbooks/ansible/backup/config.2016-07-16@22:28:34"` |
| **diff**  dictionary | If –diff option in enabled while running, the before and after configuration change are returned as part of before and after key.  **Returned:** when diff is enabled  **Sample:** `{"after": "<rpc-reply> <data> <configuration> <version>17.3R1.10</version>...<--snip-->", "before": "<rpc-reply> <data> <configuration> <version>17.3R1.10</version>...<--snip-->"}` |
| **server_capabilities**  list / elements=string | list of capabilities of the server  **Returned:** success  **Sample:** `["urn:ietf:params:netconf:base:1.1", "urn:ietf:params:netconf:capability:confirmed-commit:1.0", "urn:ietf:params:netconf:capability:candidate:1.0"]` |

### Authors

- Leandro Lisboa Penz (@lpenz)
- Ganesh Nalawade (@ganeshrn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
