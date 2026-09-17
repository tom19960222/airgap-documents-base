---
collection: kernel
version: "6.17"
title: "Kernel driver raspberrypi-hwmon"
source_url: https://www.kernel.org/doc/html/v6.17/hwmon/raspberrypi-hwmon.html
fetched_at: 2026-09-16T16:45:16+00:00
---
# Kernel driver raspberrypi-hwmon

Supported boards:

> - Raspberry Pi A+ (via GPIO on SoC)
> - Raspberry Pi B+ (via GPIO on SoC)
> - Raspberry Pi 2 B (via GPIO on SoC)
> - Raspberry Pi 3 B (via GPIO on port expander)
> - Raspberry Pi 3 B+ (via PMIC)

Author: Stefan Wahren <[stefan.wahren@i2se.com](mailto:stefan.wahren%40i2se.com)>

## Description

This driver periodically polls a mailbox property of the VC4 firmware to detect
undervoltage conditions.

## Sysfs entries

|  |  |
| --- | --- |
| in0_lcrit_alarm | Undervoltage alarm |
