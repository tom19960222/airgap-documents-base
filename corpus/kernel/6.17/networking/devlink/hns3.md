---
collection: kernel
version: "6.17"
title: "hns3 devlink support"
source_url: https://www.kernel.org/doc/html/v6.17/networking/devlink/hns3.html
fetched_at: 2026-09-16T16:52:57+00:00
---
# hns3 devlink support

This document describes the devlink features implemented by the `hns3`
device driver.

The `hns3` driver supports reloading via `DEVLINK_CMD_RELOAD`.

## Info versions

The `hns3` driver reports the following versions

devlink info versions implemented

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| `fw` | running | Used to represent the firmware version. |
| `fw.scc` | running | Used to represent the Soft Congestion Control (SSC) firmware version. SCC is a firmware component which provides multiple RDMA congestion control algorithms, including DCQCN. |
