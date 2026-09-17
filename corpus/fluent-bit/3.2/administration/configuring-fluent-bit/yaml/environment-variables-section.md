---
collection: fluent-bit
version: "3.2"
title: "Environment Variables Section"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/administration/configuring-fluent-bit/yaml/environment-variables-section.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Environment Variables Section

The `env` section allows you to define environment variables directly within the configuration file. These variables can then be used to dynamically replace values throughout your configuration using the `${VARIABLE_NAME}` syntax.

Values set in the `env` section are case-sensitive. However, as a best practice, we recommend using uppercase names for environment variables. The example below defines two variables, `FLUSH_INTERVAL` and `STDOUT_FMT`, which can be accessed in the configuration using `${FLUSH_INTERVAL}` and `${STDOUT_FMT}`:

```yaml
env:
  FLUSH_INTERVAL: 1
  STDOUT_FMT: 'json_lines'

service:
  flush: ${FLUSH_INTERVAL}
  log_level: info

pipeline:
  inputs:
    - name: random

  outputs:
    - name: stdout
      match: '*'
      format: ${STDOUT_FMT}
```

## Predefined Variables

Fluent Bit provides a set of predefined environment variables that can be used in your configuration:

| Name | Description |
|--|--|
| `${HOSTNAME}` | The system’s hostname. |

## External Variables

In addition to variables defined in the configuration file or the predefined ones, Fluent Bit can access system environment variables set in the user space. These external variables can be referenced in the configuration using the same ${VARIABLE_NAME} pattern.

For example, to set the FLUSH_INTERVAL system environment variable to 2 and use it in your configuration:

```bash
export FLUSH_INTERVAL=2
```

In the configuration file, you can then access this value as follows:

```yaml
service:
  flush: ${FLUSH_INTERVAL}
  log_level: info

pipeline:
  inputs:
    - name: random

  outputs:
    - name: stdout
      match: '*'
      format: json_lines
```

This approach allows you to easily manage and override configuration values using environment variables, providing flexibility in various deployment environments.
