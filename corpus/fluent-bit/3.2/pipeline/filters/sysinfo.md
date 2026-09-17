---
collection: fluent-bit
version: "3.2"
title: "Sysinfo"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/filters/sysinfo.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Sysinfo

The _Sysinfo Filter_ plugin allows to append system information like fluent-bit version or hostname.

## Configuration Prameters

The plugin supports the following configuration parameters:

|Key|Description|Supported platform|
|---|---|---|
|fluentbit_version_key|Specify the key name for fluent-bit version.| All |
|os_name_key|Specify the key name for os name. e.g. linux, win64 or macos.| All |
|hostname_key|Specify the key name for hostname.| All|
|os_version_key|Specify the key name for os version. It is not supported on some platforms. | Linux |
|kernel_version_key|Specify the key name for kernel version. It is not supported on some platforms.| Linux |

Some properties are supported by specific platform.

## Getting Started

In order to start filtering records, you can run the filter from the command line or through the configuration file.

The following configuration file is to append fluent-bit version and OS name.

**Tab: fluent-bit.conf**

```
[INPUT]
    Name dummy
    Tag test

[FILTER]
    Name sysinfo
    Match *
    Fluentbit_version_key flb_ver
    Os_name_key os_name

[OUTPUT]
    name stdout
    match *
```

**Tab: fluent-bit.yaml**

```yaml
pipeline:
    inputs:
        - name: dummy
          tag: test
    filters:
        - name: sysinfo
          match: '*'
          Fluentbit_version_key: flb_ver
          Os_name_key: os_name
    outputs:
        - name: stdout
          match: '*'
```

You can also run the filter from command line.

```
fluent-bit -i dummy -o stdout -F sysinfo -m '*' -p fluentbit_version_key=flb_ver -p os_name_key=os_name
```

The output will be
```
[0] dummy.0: [[1699172858.989654355, {}], {"message"=>"dummy", "flb_ver"=>"2.2.0", "os_name"=>"linux"}]
```
