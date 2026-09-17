---
collection: kernel
version: "6.17"
title: "Kernel driver qnap-mcu-hwmon"
source_url: https://www.kernel.org/doc/html/v6.17/hwmon/qnap-mcu-hwmon.html
fetched_at: 2026-09-16T16:45:16+00:00
---
# Kernel driver qnap-mcu-hwmon

This driver enables the use of the hardware monitoring and fan control
of the MCU used on some QNAP network attached storage devices.

Author: Heiko Stuebner <[heiko@sntech.de](mailto:heiko%40sntech.de)>

## Description

The driver implements a simple interface for driving the fan controlled by
setting its PWM output value and exposes the fan rpm and case-temperature
to user space through hwmon’s sysfs interface.

The fan rotation speed returned via the optional ‘fan1_input’ is calculated
inside the MCU device.

The driver provides the following sensor accesses in sysfs:

|  |  |  |
| --- | --- | --- |
| fan1_input | ro | fan tachometer speed in RPM |
| pwm1 | rw | relative speed (0-255), 255=max. speed. |
| temp1_input | ro | Measured temperature in millicelsius |
