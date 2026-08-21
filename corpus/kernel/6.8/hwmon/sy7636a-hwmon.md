---
collection: kernel
version: "6.8"
title: "Kernel driver sy7636a-hwmon"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/sy7636a-hwmon.html
fetched_at: 2026-08-21T03:53:40+00:00
---
# Kernel driver sy7636a-hwmon

Supported chips:

> - Silergy SY7636A PMIC

## Description

This driver adds hardware temperature reading support for
the Silergy SY7636A PMIC.

The following sensors are supported

> - Temperature
>   :   - SoC on-die temperature in milli-degree C

## sysfs-Interface

temp0_input
:   - SoC on-die temperature (milli-degree C)
