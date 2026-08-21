---
collection: kernel
version: "6.8"
title: "mv88e6xxx devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/mv88e6xxx.html
fetched_at: 2026-08-21T03:43:54+00:00
---
# mv88e6xxx devlink support

This document describes the devlink features implemented by the `mv88e6xxx`
device driver.

## Parameters

The `mv88e6xxx` driver implements the following driver-specific parameters.

Driver-specific parameters implemented

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Mode | Description |
| `ATU_hash` | u8 | runtime | Select one of four possible hashing algorithms for MAC addresses in the Address Translation Unit. A value of 3 may work better than the default of 1 when many MAC addresses have the same OUI. Only the values 0 to 3 are valid for this parameter. |
