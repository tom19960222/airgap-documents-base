---
collection: kernel
version: "6.8"
title: "Microchip SparX-5 SoC"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/sparx5-temp.html
fetched_at: 2026-08-21T03:53:40+00:00
---
# Microchip SparX-5 SoC

Supported chips:

> - VSC7546, VSC7549, VSC755, VSC7556, and VSC7558 (Sparx5 series)
>
>   Prefix: 'sparx5-temp'
>
>   Addresses scanned: -
>
>   Datasheet: Provided by Microchip upon request and under NDA

Author: Lars Povlsen <[lars.povlsen@microchip.com](mailto:lars.povlsen%40microchip.com)>

## Description

The Sparx5 SoC contains a temperature sensor based on the MR74060
Moortec IP.

The sensor has a range of -40°C to +125°C and an accuracy of +/-5°C.

## Sysfs entries

The following attributes are supported.

|  |  |
| --- | --- |
| temp1_input | Die temperature (in millidegree Celsius.) |
