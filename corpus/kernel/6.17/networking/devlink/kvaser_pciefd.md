---
collection: kernel
version: "6.17"
title: "kvaser_pciefd devlink support"
source_url: https://www.kernel.org/doc/html/v6.17/networking/devlink/kvaser_pciefd.html
fetched_at: 2026-09-16T16:52:59+00:00
---
# kvaser_pciefd devlink support

This document describes the devlink features implemented by the
`kvaser_pciefd` device driver.

## Info versions

The `kvaser_pciefd` driver reports the following versions

devlink info versions implemented

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| `fw` | running | Version of the firmware running on the device. Also available through `ethtool -i` as `firmware-version`. |
