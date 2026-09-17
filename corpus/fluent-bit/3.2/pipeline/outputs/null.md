---
collection: fluent-bit
version: "3.2"
title: "NULL"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/outputs/null.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# NULL

The **null** output plugin just throws away events.

## Configuration Parameters

The plugin doesn't support configuration parameters.

## Getting Started

You can run the plugin from the command line or through the configuration file:

### Command Line

From the command line you can let Fluent Bit throws away events with the following options:

```bash
$ fluent-bit -i cpu -o null
```

### Configuration File

In your main configuration file append the following Input & Output sections:

```python
[INPUT]
    Name cpu
    Tag  cpu

[OUTPUT]
    Name null
    Match *
```
