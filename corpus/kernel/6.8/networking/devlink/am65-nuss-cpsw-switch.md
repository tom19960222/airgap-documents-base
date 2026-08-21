---
collection: kernel
version: "6.8"
title: "am65-cpsw-nuss devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/am65-nuss-cpsw-switch.html
fetched_at: 2026-08-21T04:00:15+00:00
---
# am65-cpsw-nuss devlink support

This document describes the devlink features implemented by the `am65-cpsw-nuss`
device driver.

## Parameters

The `am65-cpsw-nuss` driver implements the following driver-specific
parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `switch_mode` | Boolean | runtime | Enable switch mode |
