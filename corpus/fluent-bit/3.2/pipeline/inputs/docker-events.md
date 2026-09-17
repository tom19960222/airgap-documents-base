---
collection: fluent-bit
version: "3.2"
title: "Docker Events"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/inputs/docker-events.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Docker Events

The **docker events** input plugin uses the docker API to capture server events. A complete list of possible events returned by this plugin can be found [here](https://docs.docker.com/engine/reference/commandline/events/)

## Configuration Parameters

This plugin supports the following configuration parameters:

| Key | Description | Default |
| :--- | :--- | :--- |
| Unix\_Path | The docker socket unix path | /var/run/docker.sock |
| Buffer\_Size | The size of the buffer used to read docker events \(in bytes\) | 8192 |
| Parser | Specify the name of a parser to interpret the entry as a structured message. | None |
| Key | When a message is unstructured \(no parser applied\), it's appended as a string under the key name _message_. | message |
| Reconnect.Retry_limits| The maximum number of retries allowed. The plugin tries to reconnect with docker socket when EOF is detected. | 5 |
| Reconnect.Retry_interval| The retrying interval. Unit is second. | 1 |
| Threaded | Indicates whether to run this input in its own [thread](../../administration/multithreading.md#inputs). | `false` |

### Command Line

```bash
$ fluent-bit -i docker_events -o stdout
```

### Configuration File

In your main configuration file append the following **Input** & **Output** sections:

**Tab: fluent-bit.conf**

```yaml
[INPUT]
    Name   docker_events

[OUTPUT]
    Name   stdout
    Match  *
```

**Tab: fluent-bit.yaml**

```yaml
pipeline:
    inputs:
        - name: docker_events

    outputs:
        - name: stdout
          match: '*'
```
