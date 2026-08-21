---
collection: kernel
version: "6.8"
title: "Kernel driver POWERZ"
source_url: https://www.kernel.org/doc/html/v6.8/hwmon/powerz.html
fetched_at: 2026-08-21T03:42:44+00:00
---
# Kernel driver POWERZ

Supported chips:

> - ChargerLAB POWER-Z KM003C
>
>   Prefix: 'powerz'
>
>   Addresses scanned: -

Author:

> - Thomas Weißschuh <[linux@weissschuh.net](mailto:linux%40weissschuh.net)>

## Description

This driver implements support for the ChargerLAB POWER-Z USB-C power testing
family.

The device communicates with the custom protocol over USB.

The channel labels exposed via hwmon match the labels used by the on-device
display and the official POWER-Z PC software.

As current can flow in both directions through the tester the sign of the
channel "curr1_input" (label "IBUS") indicates the direction.
