---
collection: ansible
version: "8"
title: "splunk.es.data_input_network module – Manage Splunk Data Inputs of type TCP or UDP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/splunk/es/data_input_network_module.html
fetched_at: 2026-07-28T02:53:50+00:00
---
# splunk.es.data_input_network module – Manage Splunk Data Inputs of type TCP or UDP

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/ui/repo/published/splunk/es/) (version 2.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.data_input_network`.

New in splunk.es 1.0.0

- [DEPRECATED](data_input_network_module.md#deprecated)
- [Synopsis](data_input_network_module.md#synopsis)
- [Parameters](data_input_network_module.md#parameters)
- [Examples](data_input_network_module.md#examples)
- [Status](data_input_network_module.md#status)

## [DEPRECATED](data_input_network_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   splunk_data_inputs_network

## [Synopsis](data_input_network_module.md#id2)

- This module allows for addition or deletion of TCP and UDP Data Inputs in Splunk.

Aliases: splunk_data_input_network

## [Parameters](data_input_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **connection_host**  string | Set the host for the remote server that is sending data.  `ip` sets the host to the IP address of the remote server sending data.  `dns` sets the host to the reverse DNS entry for the IP address of the remote server sending data.  `none` leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.  **Choices:**   - `"ip"` ← (default) - `"dns"` - `"none"` |
| **datatype**  string | Forwarders can transmit three types of data: raw, unparsed, or parsed. `cooked` data refers to parsed and unparsed formats.  **Choices:**   - `"cooked"` - `"raw"` ← (default) |
| **host**  string | Host from which the indexer gets data. |
| **index**  string | default Index to store generated events. |
| **name**  string / required | The input port which receives raw data. |
| **protocol**  string / required | Choose between tcp or udp  **Choices:**   - `"tcp"` - `"udp"` |
| **queue**  string | Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.  Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at “Monitor files and directories with inputs.conf”  Set queue to indexQueue to send your data directly into the index.  **Choices:**   - `"parsingQueue"` ← (default) - `"indexQueue"` |
| **rawTcpDoneTimeout**  integer | Specifies in seconds the timeout value for adding a Done-key.  If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.  **Default:** `10` |
| **restrictToHost**  string | Allows for restricting this input to only accept data from the host specified here. |
| **source**  string | Sets the source key/field for events from this input. Defaults to the input file path.  Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.  Note: Overriding the source key is generally not recommended. Typically, the input layer provides a more accurate string to aid in problem analysis and investigation, accurately recording the file from which the data was retrieved. Consider use of source types, tagging, and search wildcards before overriding this value. |
| **sourcetype**  string | Set the source type for events from this input.  “sourcetype=” is automatically prepended to <string>.  Defaults to audittrail (if signedaudit=True) or fschange (if signedaudit=false). |
| **ssl**  boolean | Enable or disble ssl for the data stream  **Choices:**   - `false` - `true` |
| **state**  string | Enable, disable, create, or destroy  **Choices:**   - `"present"` ← (default) - `"absent"` - `"enabled"` - `"disable"` |

## [Examples](data_input_network_module.md#id4)

```yaml+jinja
- name: Example adding data input network with splunk.es.data_input_network
  splunk.es.data_input_network:
    name: "8099"
    protocol: "tcp"
    state: "present"
```

## [Status](data_input_network_module.md#id5)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](data_input_network_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
- [Repository (Sources)](https://github.com/ansible-collections/splunk.es)
