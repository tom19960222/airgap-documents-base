---
collection: kernel
version: "6.8"
title: "nfp devlink support"
source_url: https://www.kernel.org/doc/html/v6.8/networking/devlink/nfp.html
fetched_at: 2026-08-21T04:00:13+00:00
---
# nfp devlink support

This document describes the devlink features implemented by the `nfp`
device driver.

## Parameters

Generic parameters implemented

|  |  |
| --- | --- |
| Name | Mode |
| `fw_load_policy` | permanent |
| `reset_dev_on_drv_probe` | permanent |

## Info versions

The `nfp` driver reports the following versions

devlink info versions implemented

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| `board.id` | fixed | Part number identifying the board design |
| `board.rev` | fixed | Revision of the board design |
| `board.manufacture` | fixed | Vendor of the board design |
| `board.model` | fixed | Model name of the board design |
| `fw.bundle_id` | stored, running | Firmware bundle id |
| `fw.mgmt` | stored, running | Version of the management firmware |
| `fw.cpld` | stored, running | The CPLD firmware component version |
| `fw.app` | stored, running | The APP firmware component version |
| `fw.undi` | stored, running | The UNDI firmware component version |
| `fw.ncsi` | stored, running | The NSCI firmware component version |
| `chip.init` | stored, running | The CFGR firmware component version |
