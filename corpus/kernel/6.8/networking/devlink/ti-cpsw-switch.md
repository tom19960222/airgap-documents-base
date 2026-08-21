---
collection: kernel
version: "6.8"
title: "ti-cpsw-switch devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/ti-cpsw-switch.html
fetched_at: 2026-08-21T04:00:14+00:00
---
# ti-cpsw-switch devlink support

This document describes the devlink features implemented by the `ti-cpsw-switch`
device driver.

## Parameters

The `ti-cpsw-switch` driver implements the following driver-specific
parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `ale_bypass` | Boolean | runtime | Enables ALE_CONTROL(4).BYPASS mode for debugging purposes. In this mode, all packets will be sent to the host port only. |
| `switch_mode` | Boolean | runtime | Enable switch mode |
