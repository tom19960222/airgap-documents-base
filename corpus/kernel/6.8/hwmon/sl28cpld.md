---
collection: kernel
version: "6.8"
title: "Kernel driver sl28cpld"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/sl28cpld.html
fetched_at: 2026-08-21T03:53:38+00:00
---
# Kernel driver sl28cpld

Supported chips:

> - Kontron sl28cpld
>
>   Prefix: 'sl28cpld'
>
>   Datasheet: not available

Authors: Michael Walle <[michael@walle.cc](mailto:michael%40walle.cc)>

## Description

The sl28cpld is a board management controller which also exposes a hardware
monitoring controller. At the moment this controller supports a single fan
supervisor. In the future there might be other flavours and additional
hardware monitoring might be supported.

The fan supervisor has a 7 bit counter register and a counter period of 1
second. If the 7 bit counter overflows, the supervisor will automatically
switch to x8 mode to support a wider input range at the loss of
granularity.

## Sysfs entries

The following attributes are supported.

|  |  |
| --- | --- |
| fan1_input | Fan RPM. Assuming 2 pulses per revolution. |
