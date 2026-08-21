---
collection: kernel
version: "6.8"
title: "Kernel driver sfctemp"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/sfctemp.html
fetched_at: 2026-08-21T03:44:48+00:00
---
# Kernel driver sfctemp

Supported chips:
:   - StarFive JH7100
    - StarFive JH7110

Authors:
:   - Emil Renner Berthing <[kernel@esmil.dk](mailto:kernel%40esmil.dk)>

## Description

This driver adds support for reading the built-in temperature sensor on the
JH7100 and JH7110 RISC-V SoCs by StarFive Technology Co. Ltd.

## `sysfs` interface

The temperature sensor can be enabled, disabled and queried via the standard
hwmon interface in sysfs under `/sys/class/hwmon/hwmonX` for some value of
`X`:

| Name | Perm | Description |
| --- | --- | --- |
| temp1_enable | RW | Enable or disable temperature sensor. Automatically enabled by the driver, but may be disabled to save power. |
| temp1_input | RO | Temperature reading in milli-degrees Celsius. |
