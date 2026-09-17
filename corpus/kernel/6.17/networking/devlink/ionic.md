---
collection: kernel
version: "6.17"
title: "ionic devlink support"
source_url: https://www.kernel.org/doc/html/v6.17/networking/devlink/ionic.html
fetched_at: 2026-09-16T16:51:44+00:00
---
# ionic devlink support

This document describes the devlink features implemented by the `ionic`
device driver.

## Info versions

The `ionic` driver reports the following versions

devlink info versions implemented

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| `fw` | running | Version of firmware running on the device |
| `asic.id` | fixed | The ASIC type for this device |
| `asic.rev` | fixed | The revision of the ASIC for this device |
