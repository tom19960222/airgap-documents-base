---
collection: kernel
version: "6.17"
title: "Kernel driver cros_ec_hwmon"
source_url: https://www.kernel.org/doc/html/v6.17/hwmon/cros_ec_hwmon.html
fetched_at: 2026-09-16T16:32:31+00:00
---
# Kernel driver cros_ec_hwmon

Supported chips:

> - ChromeOS embedded controllers.
>
>   Prefix: ‘cros_ec’
>
>   Addresses scanned: -

Author:

> - Thomas Weißschuh <[linux@weissschuh.net](mailto:linux%40weissschuh.net)>

## Description

This driver implements support for hardware monitoring commands exposed by the
ChromeOS embedded controller used in Chromebooks and other devices.

The channel labels exposed via hwmon are retrieved from the EC itself.

Fan and temperature readings are supported.
