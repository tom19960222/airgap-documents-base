---
collection: fluent-bit
version: "3.2"
title: "Dummy"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/inputs/dummy.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Dummy

The **dummy** input plugin, generates dummy events. It is useful for testing, debugging, benchmarking and getting started with Fluent Bit.

## Configuration Parameters

The plugin supports the following configuration parameters:

| Key                | Description | Default |
| :----------------- | :---------- | :------ |
| Dummy              | Dummy JSON record. | `{"message":"dummy"}` |
| Metadata           | Dummy JSON metadata. | `{}` |
| Start\_time\_sec   | Dummy base timestamp, in seconds. | `0` |
| Start\_time\_nsec  | Dummy base timestamp, in nanoseconds. | `0` |
| Rate               | Rate at which messages are generated expressed in how many times per second. | `1` |
| Interval\_sec      | Set time interval, in seconds, at which every message is generated. If set, `Rate` configuration is ignored. | `0` |
| Interval\_nsec     | Set time interval, in nanoseconds, at which every message is generated. If set, `Rate` configuration is ignored. | `0` |
| Samples            | If set, the events number will be limited. For example, if Samples=3, the plugin generates only three events and stops. | _none_ |
| Copies             | Number of messages to generate each time they are generated. | `1` |
| Flush\_on\_startup | If set to `true`, the first dummy event is generated at startup. | `false` |
| Threaded | Indicates whether to run this input in its own [thread](../../administration/multithreading.md#inputs). | `false` |

## Getting Started

You can run the plugin from the command line or through the configuration file:

### Command Line

```bash
$ fluent-bit -i dummy -o stdout
Fluent Bit v2.x.x
* Copyright (C) 2015-2022 The Fluent Bit Authors
* Fluent Bit is a CNCF sub-project under the umbrella of Fluentd
* https://fluentbit.io

[0] dummy.0: [[1686451466.659962491, {}], {"message"=>"dummy"}]
[0] dummy.0: [[1686451467.659679509, {}], {"message"=>"dummy"}]
```

### Configuration File

In your main configuration file append the following _Input_ & _Output_ sections:

**Tab: fluent-bit.conf**

```text
[INPUT]
    Name   dummy
    Dummy {"message": "custom dummy"}

[OUTPUT]
    Name   stdout
    Match  *
```

**Tab: fluent-bit.yaml**

```yaml
pipeline:
  inputs:
    - name: dummy
      dummy: '{"message": "custom dummy"}'
  outputs:
    - name: stdout
      match: '*'
```
