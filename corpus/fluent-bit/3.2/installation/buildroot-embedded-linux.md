---
collection: fluent-bit
version: "3.2"
title: "Buildroot / Embedded Linux"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/installation/buildroot-embedded-linux.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Buildroot / Embedded Linux

Install Fluent Bit in your embedded Linux system.

## Install

To install, select Fluent Bit in your `defconfig`.
See the `Config.in` file for all configuration options.

```text
BR2_PACKAGE_FLUENT_BIT=y
```

## Run

The default configuration file is written to:

```text
/etc/fluent-bit/fluent-bit.conf
```

Fluent Bit is started by the `S99fluent-bit` script.

## Support

All configurations with a toolchain that supports threads and dynamic library
linking are supported.
