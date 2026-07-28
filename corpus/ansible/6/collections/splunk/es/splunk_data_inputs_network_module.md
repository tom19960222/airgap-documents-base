---
collection: ansible
version: "6"
title: "splunk.es.splunk_data_inputs_network module – Manage Splunk Data Inputs of type TCP or UDP resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/splunk/es/splunk_data_inputs_network_module.html
fetched_at: 2026-07-28T00:20:01+00:00
---
# splunk.es.splunk_data_inputs_network module – Manage Splunk Data Inputs of type TCP or UDP resource module

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/splunk/es) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.splunk_data_inputs_network`.

New in splunk.es 2.1.0

- [Synopsis](splunk_data_inputs_network_module.md#synopsis)
- [Parameters](splunk_data_inputs_network_module.md#parameters)
- [Examples](splunk_data_inputs_network_module.md#examples)
- [Return Values](splunk_data_inputs_network_module.md#return-values)

## [Synopsis](splunk_data_inputs_network_module.md#id1)

- Module that allows to add/update or delete of TCP and UDP Data Inputs in Splunk.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](splunk_data_inputs_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Manage and preview protocol input data. |
| **cipher_suite**  string | Specifies list of acceptable ciphers to use in ssl.  Only obtained for TCP SSL configuration present on device. |
| **connection_host**  string | Set the host for the remote server that is sending data.  `ip` sets the host to the IP address of the remote server sending data.  `dns` sets the host to the reverse DNS entry for the IP address of the remote server sending data.  `none` leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.  Choices:   - `"ip"` - `"dns"` - `"none"` |
| **datatype**  string | `cooked` lets one access cooked TCP input information and create new containers for managing cooked data.  `raw` lets one manage raw tcp inputs from forwarders.  `splunktcptoken` lets one manage receiver access using tokens.  `ssl` Provides access to the SSL configuration of a Splunk server. This option does not support states *deleted* and *replaced*.  Choices:   - `"cooked"` - `"raw"` - `"splunktcptoken"` - `"ssl"` |
| **disabled**  boolean | Indicates whether the input is disabled.  Choices:   - `false` - `true` |
| **host**  string | Host from which the indexer gets data. |
| **index**  string | default Index to store generated events. |
| **name**  string / required | The input port which receives raw data. |
| **no_appending_timestamp**  boolean | If set to true, prevents Splunk software from prepending a timestamp and hostname to incoming events.  Only for UDP data input configuration.  Choices:   - `false` - `true` |
| **no_priority_stripping**  boolean | If set to true, Splunk software does not remove the priority field from incoming syslog events.  Only for UDP data input configuration.  Choices:   - `false` - `true` |
| **password**  string | Server certificate password, if any.  Only for TCP SSL configuration. |
| **protocol**  string / required | Choose whether to manage TCP or UDP inputs  Choices:   - `"tcp"` - `"udp"` |
| **queue**  string | Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.  Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at “Monitor files and directories with inputs.conf”  Set queue to indexQueue to send your data directly into the index.  Only applicable for “/tcp/raw” and “/udp” APIs  Choices:   - `"parsingQueue"` - `"indexQueue"` |
| **raw_tcp_done_timeout**  integer | Specifies in seconds the timeout value for adding a Done-key.  If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.  Only for TCP raw input configuration. |
| **require_client_cert**  string | Determines whether a client must authenticate.  Only for TCP SSL configuration. |
| **restrict_to_host**  string | Allows for restricting this input to only accept data from the host specified here. |
| **root_ca**  string | Certificate authority list (root file).  Only for TCP SSL configuration. |
| **server_cert**  string | Full path to the server certificate.  Only for TCP SSL configuration. |
| **source**  string | Sets the source key/field for events from this input. Defaults to the input file path.  Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with ‘source::’.  Note that Overriding the source key is generally not recommended. Typically, the input layer provides a more accurate string to aid in problem analysis and investigation, accurately recording the file from which the data was retrieved. Consider use of source types, tagging, and search wildcards before overriding this value. |
| **sourcetype**  string | Set the source type for events from this input.  “sourcetype=” is automatically prepended to <string>.  Defaults to audittrail (if signedaudit=True) or fschange (if signedaudit=False). |
| **ssl**  boolean | Enable or disble ssl for the data stream  Choices:   - `false` - `true` |
| **token**  string | Token value to use for SplunkTcpToken. If unspecified, a token is generated automatically. |
| **running_config**  string | The module, by default, will connect to the remote device and retrieve the current running-config to use as a base for comparing against the contents of source. There are times when it is not desirable to have the task get the current running-config for every task in a playbook. The *running_config* argument allows the implementer to pass in the configuration to use as the base config for comparison. This value of this option should be the output received from device by executing command. |
| **state**  string | The state the configuration should be left in  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` |

## [Examples](splunk_data_inputs_network_module.md#id3)

```yaml+jinja
# Using gathered
# --------------

- name: Gathering information about TCP Cooked Inputs
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: cooked
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "connection_host": "ip",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "8101"
#     },
#     {
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "9997"
#     },
#     {
#         "connection_host": "ip",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8101",
#         "restrict_to_host": "default"
#     }
# ]

- name: Gathering information about TCP Cooked Inputs by Name
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: cooked
        name: 9997
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "datatype": "cooked",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "name": "9997",
#         "protocol": "tcp"
#     }
# ]

- name: Gathering information about TCP Raw Inputs
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: raw
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "connection_host": "ip",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "8099",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 10
#     },
#     {
#         "connection_host": "ip",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 10,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ]

- name: Gathering information about TCP Raw inputs by Name
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: raw
        name: 8099
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "8099",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 10
#     }
# ]

- name: Gathering information about TCP SSL configuration
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: ssl
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "cipher_suite": <cipher-suites>,
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "test_host"
#     }
# ]

- name: Gathering information about TCP SplunkTcpTokens
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: splunktcptoken
    state: gathered

# RUN output:
# -----------

# "gathered": [
#     {
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "splunktcptoken://test_token1",
#         "token": <token1>
#     },
#     {
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "splunktcptoken://test_token2",
#         "token": <token2>
#     }
# ]

# Using merged
# ------------

- name: To add the TCP raw config
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: raw
        name: 8100
        connection_host: ip
        disabled: True
        raw_tcp_done_timeout: 9
        restrict_to_host: default
        queue: parsingQueue
        source: test_source
        sourcetype: test_source_type
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 9,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ],
# "before": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 10,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ]

- name: To add the TCP cooked config
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: cooked
        name: 8101
        connection_host: ip
        disabled: False
        restrict_to_host: default
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "connection_host": "ip",
#         "datatype": "cooked",
#         "disabled": false,
#         "host": "$decideOnStartup",
#         "name": "default:8101",
#         "protocol": "tcp",
#         "restrict_to_host": "default"
#     }
# ],
# "before": [
#     {
#         "connection_host": "ip",
#         "datatype": "cooked",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "name": "default:8101",
#         "protocol": "tcp",
#         "restrict_to_host": "default"
#     }
# ],

- name: To add the Splunk TCP token
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: splunktcptoken
        name: test_token
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "datatype": "splunktcptoken",
#         "name": "splunktcptoken://test_token",
#         "protocol": "tcp",
#         "token": <token>
#     }
# ],
# "before": [],

- name:  To add the Splunk SSL
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: ssl
        name: test_host
        root_ca: {root CA directory}
        server_cert: {server cretificate directory}
    state: merged

# RUN output:
# -----------

# "after": [
#     {
#         "cipher_suite": <cipher suite>,
#         "datatype": "ssl",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "test_host",
#         "protocol": "tcp"
#     }
# ],
# "before": []

# Using deleted
# -------------

- name: To Delete TCP Raw
  splunk.es.splunk_data_inputs_network:
    config:
      - protocol: tcp
        datatype: raw
        name: default:8100
    state: deleted

# RUN output:
# -----------

# "after": [],
# "before": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 9,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ]

# Using replaced
# --------------

- name: Replace existing data inputs networks configuration
  register: result
  splunk.es.splunk_data_inputs_network:
    state: replaced
    config:
      - protocol: tcp
        datatype: raw
        name: 8100
        connection_host: ip
        disabled: True
        host: "$decideOnStartup"
        index: default
        queue: parsingQueue
        raw_tcp_done_timeout: 10
        restrict_to_host: default
        source: test_source
        sourcetype: test_source_type

# RUN output:
# -----------

# "after": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 9,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ],
# "before": [
#     {
#         "connection_host": "ip",
#         "datatype": "raw",
#         "disabled": true,
#         "host": "$decideOnStartup",
#         "index": "default",
#         "name": "default:8100",
#         "protocol": "tcp",
#         "queue": "parsingQueue",
#         "raw_tcp_done_timeout": 10,
#         "restrict_to_host": "default",
#         "source": "test_source",
#         "sourcetype": "test_source_type"
#     }
# ],
```

## [Return Values](splunk_data_inputs_network_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration after module execution.  Returned: when changed  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **before**  list / elements=string | The configuration prior to the module execution.  Returned: when state is *merged*, *replaced*, *deleted*  Sample: `["This output will always be in the same format as the module argspec.\n"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  Returned: when state is *gathered*  Sample: `"This output will always be in the same format as the module argspec.\n"` |

### Authors

- Ansible Security Automation Team (@pranav-bhatt) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
[Repository (Sources)](https://github.com/ansible-collections/splunk.es)
