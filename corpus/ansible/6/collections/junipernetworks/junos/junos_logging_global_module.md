---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_logging_global module – Manage logging configuration on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_logging_global_module.html
fetched_at: 2026-07-27T17:54:27+00:00
---
# junipernetworks.junos.junos_logging_global module – Manage logging configuration on Junos devices.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_logging_global_module.md#ansible-collections-junipernetworks-junos-junos-logging-global-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_logging_global`.

New in junipernetworks.junos 2.4.0

- [Synopsis](junos_logging_global_module.md#synopsis)
- [Requirements](junos_logging_global_module.md#requirements)
- [Parameters](junos_logging_global_module.md#parameters)
- [Notes](junos_logging_global_module.md#notes)
- [Examples](junos_logging_global_module.md#examples)
- [Return Values](junos_logging_global_module.md#return-values)

## [Synopsis](junos_logging_global_module.md#id1)

- This module manages logging configuration on devices running Junos.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_logging_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_logging_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of logging configuration. |
| **allow_duplicates**  boolean | Do not suppress the repeated message for all targets.  Choices:   - `false` - `true` |
| **archive**  dictionary | Specify archive file information. |
| **binary_data**  boolean | Mark file as if it contains binary data.  Choices:   - `false` - `true` |
| **file_size**  integer | Size of files to be archived (65536..1073741824 bytes). |
| **files**  integer | Specify number of files to be archived (1..1000). |
| **no_binary_data**  boolean | Don’t mark file as if it contains binary data.  Choices:   - `false` - `true` |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **set**  boolean | Set archive file information.  Choices:   - `false` - `true` |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **console**  dictionary | Set console logging parameters. |
| **any**  dictionary | Set All facilities. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **authorization**  dictionary | Specify authorization system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **change_log**  dictionary | Specify configuration change log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **conflict_log**  dictionary | Specify configuration conflict log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **daemon**  dictionary | Specify various system processes. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **dfc**  dictionary | Specify dynamic flow capture. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **external**  dictionary | Specify Local external applications. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **firewall**  dictionary | Specify Firewall filtering system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **ftp**  dictionary | Specify FTP process. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **interactive_commands**  dictionary | Specify commands executed by the UI. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **kernel**  dictionary | Specify Kernel specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **ntp**  dictionary | Specify NTP process specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **pfe**  dictionary | Specify Packet Forwarding Engine specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **security**  dictionary | Specify Security related logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **user**  dictionary | Specify user specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **files**  list / elements=dictionary | Specify files logging. |
| **allow_duplicates**  boolean | Do not suppress the repeated message for all targets.  Choices:   - `false` - `true` |
| **any**  dictionary | Set All facilities. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **archive**  dictionary | Specify archive file information. |
| **archive_sites**  list / elements=string | Specify Primary and failover URLs to receive archive facilities. |
| **binary_data**  boolean | Mark file as if it contains binary data.  Choices:   - `false` - `true` |
| **file_size**  integer | Size of files to be archived (65536..1073741824 bytes). |
| **files**  integer | Specify number of files to be archived (1..1000). |
| **no_binary_data**  boolean | Don’t mark file as if it contains binary data.  Choices:   - `false` - `true` |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **set**  boolean | Set archive file information.  Choices:   - `false` - `true` |
| **start_time**  string | Specify start time for file transmission (yyyy-mm-dd.hh:mm). |
| **transfer_interval**  integer | Specify frequency at which to transfer files to archive sites (5..2880 minutes). |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **authorization**  dictionary | Specify authorization system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **change_log**  dictionary | Specify configuration change log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **conflict_log**  dictionary | Specify configuration conflict log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **daemon**  dictionary | Specify various system processes. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **dfc**  dictionary | Specify dynamic flow capture. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **explicit_priority**  boolean | Include priority and facility in messages.  Choices:   - `false` - `true` |
| **external**  dictionary | Specify Local external applications. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **firewall**  dictionary | Specify Firewall filtering system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **ftp**  dictionary | Specify FTP process. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **interactive_commands**  dictionary | Specify commands executed by the UI. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **kernel**  dictionary | Specify Kernel specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **match**  string | Specify regular expression for lines to be logged. |
| **match_strings**  list / elements=string | Specify matching string(s) for lines to be logged. |
| **name**  string | Specify filename in which to log data. |
| **ntp**  dictionary | Specify NTP process specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **pfe**  dictionary | Specify Packet Forwarding Engine specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **security**  dictionary | Specify Security related logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **structured_data**  dictionary | Specify Log system message in structured format. |
| **brief**  boolean | Omit English-language text from end of logged messages.  Choices:   - `false` - `true` |
| **set**  boolean | Set Log system message in structured format.  Choices:   - `false` - `true` |
| **user**  dictionary | Specify user specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **hosts**  list / elements=dictionary | Specify hosts to be notified. |
| **allow_duplicates**  boolean | Do not suppress the repeated message for all targets.  Choices:   - `false` - `true` |
| **any**  dictionary | Set All facilities. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **authorization**  dictionary | Specify authorization system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **change_log**  dictionary | Specify configuration change log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **conflict_log**  dictionary | Specify configuration conflict log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **daemon**  dictionary | Specify various system processes. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **dfc**  dictionary | Specify dynamic flow capture. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **exclude_hostname**  boolean | Specify exclude hostname field in messages.  Choices:   - `false` - `true` |
| **explicit_priority**  boolean | Include priority and facility in messages.  Choices:   - `false` - `true` |
| **external**  dictionary | Specify Local external applications. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **facility_override**  string | Specify alternate facility for logging to remote host. |
| **firewall**  dictionary | Specify Firewall filtering system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **ftp**  dictionary | Specify FTP process. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **interactive_commands**  dictionary | Specify commands executed by the UI. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **kernel**  dictionary | Specify Kernel specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **log_prefix**  string | Prefix for all logging to this host. |
| **match**  string | Specify regular expression for lines to be logged. |
| **match_strings**  list / elements=string | Specify matching string(s) for lines to be logged. |
| **name**  string | Specify the host name. |
| **ntp**  dictionary | Specify NTP process specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **pfe**  dictionary | Specify Packet Forwarding Engine specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **port**  integer | Specify port number. |
| **routing_instance**  string | Specify routing-instance. |
| **security**  dictionary | Specify Security related logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **source_address**  string | Specify address as source address. |
| **structured_data**  dictionary | Specify Log system message in structured format. |
| **brief**  boolean | Omit English-language text from end of logged messages.  Choices:   - `false` - `true` |
| **set**  boolean | Set Log system message in structured format.  Choices:   - `false` - `true` |
| **user**  dictionary | Specify user specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **log_rotate_frequency**  integer | Specify Rotate log frequency (1..59 minutes). |
| **routing_instance**  string | Specify Routing routing-instance. |
| **server**  dictionary | Specify syslog server logging. |
| **routing_instance**  dictionary | nable/disable syslog server in routing-instances. |
| **all**  boolean | Enable/disable all routing instances.  Choices:   - `false` - `true` |
| **default**  boolean | Enable/disable default routing instances.  Choices:   - `false` - `true` |
| **routing_instances**  list / elements=dictionary | Specify routing-instances. |
| **disable**  boolean | Disable syslog server in this routing instances.  Choices:   - `false` - `true` |
| **name**  string | Specify routing-instance name. |
| **set**  boolean | Enable syslog server.  Choices:   - `false` - `true` |
| **source_address**  string | Specify address as source address. |
| **time_format**  dictionary | Specify additional information to include in system log timestamp. |
| **millisecond**  boolean | Include milliseconds in timestamp.  Choices:   - `false` - `true` |
| **set**  boolean | Set time-format  Choices:   - `false` - `true` |
| **year**  boolean | Include year in timestamp.  Choices:   - `false` - `true` |
| **users**  list / elements=dictionary | Specify user logging |
| **allow_duplicates**  boolean | Do not suppress the repeated message for all targets.  Choices:   - `false` - `true` |
| **any**  dictionary | Set All facilities. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **authorization**  dictionary | Specify authorization system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **change_log**  dictionary | Specify configuration change log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **conflict_log**  dictionary | Specify configuration conflict log. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **daemon**  dictionary | Specify various system processes. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **dfc**  dictionary | Specify dynamic flow capture. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **external**  dictionary | Specify Local external applications. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **firewall**  dictionary | Specify Firewall filtering system. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **ftp**  dictionary | Specify FTP process. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **interactive_commands**  dictionary | Specify commands executed by the UI. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **kernel**  dictionary | Specify Kernel specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **match**  string | Specify regular expression for lines to be logged. |
| **match_strings**  list / elements=string | Specify matching string(s) for lines to be logged. |
| **name**  string | Specify user name. |
| **ntp**  dictionary | Specify NTP process specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **pfe**  dictionary | Specify Packet Forwarding Engine specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **security**  dictionary | Specify Security related logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **user**  dictionary | Specify user specific logging. |
| **level**  string / required | Set severity logging level.  Choices:   - `"alert"` - `"any"` - `"critical"` - `"emergency"` - `"error"` - `"info"` - `"none"` - `"notice"` - `"warning"` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show system syslog**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"overridden"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_logging_global_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`.
> - See [the Junos OS Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
> - Tested against JunOS v18.4R1

## [Examples](junos_logging_global_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show system syslog
#
# [edit]
# vagrant@vsrx# show routing-instances
# inst11 {
#     description inst11;
# }
- name: Merge provided logging configuration into running configuration.
  junipernetworks.junos.junos_logging_global:
    config:
      allow_duplicates: true
      archive:
        set: true
        no_binary_data: true
        files: 10
        file_size: 65578
        no_world_readable: true
      console:
        any:
          level: "info"
        authorization:
          level: "any"
        change_log:
          level: "critical"
        ftp:
          level: "none"
      files:
        - name: "file101"
          allow_duplicates: true
        - name: "file102"
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
        - name: "file103"
          archive:
            set: true
            no_binary_data: true
            files: 10
            file_size: 65578
            no_world_readable: true
          explicit_priority: true
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
      hosts:
        - name: host111
          exclude_hostname: true
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
            brief: true
          facility_override: "ftp"
          log_prefix: "field"
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
          port: 1231
          routing_instance: "inst11"
          source_address: "11.1.1.11"
      routing_instance: "inst11"
      log_rotate_frequency: 45
      source_address: "33.33.33.33"
      time_format:
        millisecond: true
        year: true
      users:
        - name: "user1"
          allow_duplicates: true
        - name: "user2"
          allow_duplicates: true
          any:
            level: "any"
          user:
            level: info
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "allow_duplicates": true,
#         "archive": {
#             "file_size": 65578,
#             "files": 10,
#             "no_binary_data": true,
#             "no_world_readable": true
#         },
#         "console": {
#             "any": {
#                 "level": "info"
#             },
#             "authorization": {
#                 "level": "any"
#             },
#             "change_log": {
#                 "level": "critical"
#             },
#             "ftp": {
#                 "level": "none"
#             }
#         },
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file101"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             },
#             {
#                 "archive": {
#                     "file_size": 65578,
#                     "files": 10,
#                     "no_binary_data": true,
#                     "no_world_readable": true
#                 },
#                 "explicit_priority": true,
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "file103"
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host111",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "log_rotate_frequency": 45,
#         "routing_instance": "inst11",
#         "source_address": "33.33.33.33",
#         "time_format": {
#             "millisecond": true,
#             "year": true
#         },
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:syslog><nc:allow-duplicates/><nc:archive><nc:files>10</nc:files>"
#         "<nc:no-binary-data/><nc:size>65578</nc:size><nc:no-world-readable/></nc:archive>"
#         "<nc:console><nc:name>change-log</nc:name><nc:critical/></nc:console><nc:console>"
#         "<nc:name>any</nc:name><nc:info/></nc:console><nc:console><nc:name>authorization</nc:name>"
#         "<nc:any/></nc:console><nc:console><nc:name>ftp</nc:name><nc:none/></nc:console><nc:file>"
#         "<nc:name>file101</nc:name><nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name>"
#         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/>"
#         "</nc:file><nc:file><nc:name>file103</nc:name><nc:archive><nc:files>10</nc:files><nc:no-binary-data/>"
#         "<nc:size>65578</nc:size><nc:no-world-readable/></nc:archive><nc:explicit-priority/>"
#         "<nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
#         "<nc:match-strings>^prompt</nc:match-strings></nc:file><nc:host><nc:name>host111</nc:name>"
#         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents>"
#         "<nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
#         "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
#         "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
#         "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
#         "<nc:structured-data><nc:brief/></nc:structured-data></nc:host>"
#         "<nc:log-rotate-frequency>45</nc:log-rotate-frequency><nc:routing-instance>inst11</nc:routing-instance>"
#         "<nc:source-address>33.33.33.33</nc:source-address><nc:time-format><nc:millisecond/>"
#         "<nc:year/></nc:time-format><nc:user><nc:name>user1</nc:name><nc:allow-duplicates/></nc:user>"
#         "<nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/>"
#         "</nc:contents><nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system syslog
# archive size 65578 files 10 no-world-readable no-binary-data;
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host111 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# allow-duplicates;
# file file101 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
# file file103 {
#     match "^set*";
#     archive size 65578 files 10 no-world-readable no-binary-data;
#     explicit-priority;
#     match-strings [ "^delete" "^prompt" ];
# }
# console {
#     any info;
#     authorization any;
#     ftp none;
#     change-log critical;
# }
# time-format year millisecond;
# source-address 33.33.33.33;
# routing-instance inst11;
# log-rotate-frequency 45;
# Using replaced
#
# Before state
# ------------
#
# vagrant@vsrx# show system syslog
# archive size 65578 files 10 no-world-readable no-binary-data;
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host111 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# allow-duplicates;
# file file101 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
# file file103 {
#     match "^set*";
#     archive size 65578 files 10 no-world-readable no-binary-data;
#     explicit-priority;
#     match-strings [ "^delete" "^prompt" ];
# }
# console {
#     any info;
#     authorization any;
#     ftp none;
#     change-log critical;
# }
# time-format year millisecond;
# source-address 33.33.33.33;
# routing-instance inst11;
# log-rotate-frequency 45;
- name: Replaced running logging global configuration with provided configuration
  junipernetworks.junos.junos_logging_global:
    config:
      files:
        - name: "file104"
          allow_duplicates: true
        - name: "file102"
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
      hosts:
        - name: host222
          exclude_hostname: true
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
            brief: true
          facility_override: "ftp"
          log_prefix: "field"
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
          port: 1231
          routing_instance: "inst11"
          source_address: "11.1.1.11"
      users:
        - name: "user1"
          allow_duplicates: true
        - name: "user2"
          allow_duplicates: true
          any:
            level: "any"
          user:
            level: info
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file104"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host222",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "before": {
#         "allow_duplicates": true,
#         "archive": {
#             "file_size": 65578,
#             "files": 10,
#             "no_binary_data": true,
#             "no_world_readable": true
#         },
#         "console": {
#             "any": {
#                 "level": "info"
#             },
#             "authorization": {
#                 "level": "any"
#             },
#             "change_log": {
#                 "level": "critical"
#             },
#             "ftp": {
#                 "level": "none"
#             }
#         },
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file101"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             },
#             {
#                 "archive": {
#                     "file_size": 65578,
#                     "files": 10,
#                     "no_binary_data": true,
#                     "no_world_readable": true
#                 },
#                 "explicit_priority": true,
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "file103"
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host111",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "log_rotate_frequency": 45,
#         "routing_instance": "inst11",
#         "source_address": "33.33.33.33",
#         "time_format": {
#             "millisecond": true,
#             "year": true
#         },
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#             "<nc:syslog delete="delete"/><nc:syslog><nc:file><nc:name>file104</nc:name>"
#             "<nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name><nc:allow-duplicates/>"
#             "<nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/></nc:file>"
#             "<nc:host><nc:name>host222</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name>"
#             "<nc:any/></nc:contents><nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
#             "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match>"
#             "<nc:match-strings>^delete</nc:match-strings>"
#             "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
#             "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
#             "<nc:structured-data><nc:brief/></nc:structured-data></nc:host><nc:user><nc:name>user1</nc:name>"
#             "<nc:allow-duplicates/></nc:user><nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents>"
#             "<nc:name>any</nc:name><nc:any/></nc:contents>"
#             "<nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system syslog
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host222 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# file file104 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show system syslog
# archive size 65578 files 10 no-world-readable no-binary-data;
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host111 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# allow-duplicates;
# file file101 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
# file file103 {
#     match "^set*";
#     archive size 65578 files 10 no-world-readable no-binary-data;
#     explicit-priority;
#     match-strings [ "^delete" "^prompt" ];
# }
# console {
#     any info;
#     authorization any;
#     ftp none;
#     change-log critical;
# }
# time-format year millisecond;
# source-address 33.33.33.33;
# routing-instance inst11;
# log-rotate-frequency 45;
- name: Override running logging global configuration with provided configuration
  junipernetworks.junos.junos_logging_global:
    config:
      files:
        - name: "file104"
          allow_duplicates: true
        - name: "file102"
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
      hosts:
        - name: host222
          exclude_hostname: true
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
            brief: true
          facility_override: "ftp"
          log_prefix: "field"
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
          port: 1231
          routing_instance: "inst11"
          source_address: "11.1.1.11"
      users:
        - name: "user1"
          allow_duplicates: true
        - name: "user2"
          allow_duplicates: true
          any:
            level: "any"
          user:
            level: info
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file104"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host222",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "before": {
#         "allow_duplicates": true,
#         "archive": {
#             "file_size": 65578,
#             "files": 10,
#             "no_binary_data": true,
#             "no_world_readable": true
#         },
#         "console": {
#             "any": {
#                 "level": "info"
#             },
#             "authorization": {
#                 "level": "any"
#             },
#             "change_log": {
#                 "level": "critical"
#             },
#             "ftp": {
#                 "level": "none"
#             }
#         },
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file101"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             },
#             {
#                 "archive": {
#                     "file_size": 65578,
#                     "files": 10,
#                     "no_binary_data": true,
#                     "no_world_readable": true
#                 },
#                 "explicit_priority": true,
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "file103"
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host111",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "log_rotate_frequency": 45,
#         "routing_instance": "inst11",
#         "source_address": "33.33.33.33",
#         "time_format": {
#             "millisecond": true,
#             "year": true
#         },
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#             "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#             "<nc:syslog delete="delete"/><nc:syslog><nc:file><nc:name>file104</nc:name>"
#             "<nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name><nc:allow-duplicates/>"
#             "<nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/></nc:file>"
#             "<nc:host><nc:name>host222</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name>"
#             "<nc:any/></nc:contents><nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
#             "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match>"
#             "<nc:match-strings>^delete</nc:match-strings>"
#             "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
#             "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
#             "<nc:structured-data><nc:brief/></nc:structured-data></nc:host><nc:user><nc:name>user1</nc:name>"
#             "<nc:allow-duplicates/></nc:user><nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents>"
#             "<nc:name>any</nc:name><nc:any/></nc:contents>"
#             "<nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system syslog
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host222 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# file file104 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show system syslog
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host222 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# file file104 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
- name: Delete running logging global configuration
  junipernetworks.junos.junos_logging_global:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#     "after": {},
#     "before": {
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file104"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host222",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#               "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#               "<nc:syslog delete="delete"/></nc:system>"
#     ]
# After state
# -----------
#
# vagrant@vsrx# show system syslog
#
# [edit]
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show system syslog
# user user1 {
#     allow-duplicates;
# }
# user user2 {
#     any any;
#     user info;
#     allow-duplicates;
# }
# host host222 {
#     any any;
#     match "^set*";
#     allow-duplicates;
#     port 1231;
#     facility-override ftp;
#     log-prefix field;
#     source-address 11.1.1.11;
#     routing-instance inst11;
#     exclude-hostname;
#     match-strings [ "^delete" "^prompt" ];
#     structured-data {
#         brief;
#     }
# }
# file file104 {
#     allow-duplicates;
# }
# file file102 {
#     any any;
#     allow-duplicates;
#     structured-data;
# }
- name: Gather running logging global configuration
  junipernetworks.junos.junos_logging_global:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "gathered": {
#         "files": [
#             {
#                 "allow_duplicates": true,
#                 "name": "file104"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "file102",
#                 "structured_data": {
#                     "set": true
#                 }
#             }
#         ],
#         "hosts": [
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "exclude_hostname": true,
#                 "facility_override": "ftp",
#                 "log_prefix": "field",
#                 "match": "^set*",
#                 "match_strings": [
#                     "^delete",
#                     "^prompt"
#                 ],
#                 "name": "host222",
#                 "port": 1231,
#                 "routing_instance": "inst11",
#                 "source_address": "11.1.1.11",
#                 "structured_data": {
#                     "brief": true
#                 }
#             }
#         ],
#         "users": [
#             {
#                 "allow_duplicates": true,
#                 "name": "user1"
#             },
#             {
#                 "allow_duplicates": true,
#                 "any": {
#                     "level": "any"
#                 },
#                 "name": "user2",
#                 "user": {
#                     "level": "info"
#                 }
#             }
#         ]
#     },
#     "changed": false,
# Using rendered
#
# Before state
# ------------
#
- name: Render xml for provided facts.
  junipernetworks.junos.junos_logging_global:
    config:
      allow_duplicates: true
      archive:
        set: true
        no_binary_data: true
        files: 10
        file_size: 65578
        no_world_readable: true
      console:
        any:
          level: "info"
        authorization:
          level: "any"
        change_log:
          level: "critical"
        ftp:
          level: "none"
      files:
        - name: "file101"
          allow_duplicates: true
        - name: "file102"
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
        - name: "file103"
          archive:
            set: true
            no_binary_data: true
            files: 10
            file_size: 65578
            no_world_readable: true
          explicit_priority: true
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
      hosts:
        - name: host111
          exclude_hostname: true
          allow_duplicates: true
          any:
            level: "any"
          structured_data:
            set: true
            brief: true
          facility_override: "ftp"
          log_prefix: "field"
          match: "^set*"
          match_strings:
            - "^delete"
            - "^prompt"
          port: 1231
          routing_instance: "inst11"
          source_address: "11.1.1.11"
      routing_instance: "inst11"
      log_rotate_frequency: 45
      source_address: "33.33.33.33"
      time_format:
        millisecond: true
        year: true
      users:
        - name: "user1"
          allow_duplicates: true
        - name: "user2"
          allow_duplicates: true
          any:
            level: "any"
          user:
            level: info
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": [
#         "<nc:system xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">"
#         "<nc:syslog><nc:allow-duplicates/><nc:archive><nc:files>10</nc:files>"
#         "<nc:no-binary-data/><nc:size>65578</nc:size><nc:no-world-readable/></nc:archive>"
#         "<nc:console><nc:name>change-log</nc:name><nc:critical/></nc:console><nc:console>"
#         "<nc:name>any</nc:name><nc:info/></nc:console><nc:console><nc:name>authorization</nc:name>"
#         "<nc:any/></nc:console><nc:console><nc:name>ftp</nc:name><nc:none/></nc:console><nc:file>"
#         "<nc:name>file101</nc:name><nc:allow-duplicates/></nc:file><nc:file><nc:name>file102</nc:name>"
#         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents><nc:structured-data/>"
#         "</nc:file><nc:file><nc:name>file103</nc:name><nc:archive><nc:files>10</nc:files><nc:no-binary-data/>"
#         "<nc:size>65578</nc:size><nc:no-world-readable/></nc:archive><nc:explicit-priority/>"
#         "<nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
#         "<nc:match-strings>^prompt</nc:match-strings></nc:file><nc:host><nc:name>host111</nc:name>"
#         "<nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/></nc:contents>"
#         "<nc:exclude-hostname/><nc:facility-override>ftp</nc:facility-override>"
#         "<nc:log-prefix>field</nc:log-prefix><nc:match>^set*</nc:match><nc:match-strings>^delete</nc:match-strings>"
#         "<nc:match-strings>^prompt</nc:match-strings><nc:port>1231</nc:port>"
#         "<nc:routing-instance>inst11</nc:routing-instance><nc:source-address>11.1.1.11</nc:source-address>"
#         "<nc:structured-data><nc:brief/></nc:structured-data></nc:host>"
#         "<nc:log-rotate-frequency>45</nc:log-rotate-frequency><nc:routing-instance>inst11</nc:routing-instance>"
#         "<nc:source-address>33.33.33.33</nc:source-address><nc:time-format><nc:millisecond/>"
#         "<nc:year/></nc:time-format><nc:user><nc:name>user1</nc:name><nc:allow-duplicates/></nc:user>"
#         "<nc:user><nc:name>user2</nc:name><nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/>"
#         "</nc:contents><nc:contents><nc:name>user</nc:name><nc:info/></nc:contents></nc:user></nc:syslog></nc:system>"
#     ]
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <system xmlns="http://yang.juniper.net/junos-es/conf/system">
#         <syslog>
#             <user>
#                 <name>*</name>
#                 <contents>
#                     <name>any</name>
#                     <emergency/>
#                 </contents>
#             </user>
#             <file>
#                 <name>messages</name>
#                 <contents>
#                     <name>any</name>
#                     <any/>
#                 </contents>
#                 <contents>
#                     <name>authorization</name>
#                     <info/>
#                 </contents>
#             </file>
#             <file>
#                 <name>interactive-commands</name>
#                 <contents>
#                     <name>interactive-commands</name>
#                     <any/>
#                 </contents>
#             </file>
#         </syslog>
#     </system>
#     </configuration>
# </rpc-reply>
- name: Parse logging global running config
  junipernetworks.junos.junos_routing_instances:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "files": [
#             {
#                 "any": {
#                     "level": "any"
#                 },
#                 "authorization": {
#                     "level": "info"
#                 },
#                 "name": "messages"
#             },
#             {
#                 "interactive_commands": {
#                     "level": "any"
#                 },
#                 "name": "interactive-commands"
#             }
#         ],
#         "users": [
#             {
#                 "any": {
#                     "level": "emergency"
#                 },
#                 "name": "*"
#             }
#         ]
#     }
#
#
```

## [Return Values](junos_logging_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:allow-duplicates/></nc:user><nc:user><nc:name>user2</nc:name> <nc:allow-duplicates/><nc:contents><nc:name>any</nc:name><nc:any/> </nc:contents><nc:contents><nc:name>user</nc:name><nc:info/></nc:contents> </nc:user></nc:syslog></nc:system>\"", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
