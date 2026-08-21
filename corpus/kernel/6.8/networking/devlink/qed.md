---
collection: kernel
version: "6.8"
title: "qed devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/qed.html
fetched_at: 2026-08-21T04:00:14+00:00
---
# qed devlink support

This document describes the devlink features implemented by the `qed` core
device driver.

## Parameters

The `qed` driver implements the following driver-specific parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `iwarp_cmt` | Boolean | runtime | Enable iWARP functionality for 100g devices. Note that this impacts L2 performance, and is therefore not enabled by default. |
