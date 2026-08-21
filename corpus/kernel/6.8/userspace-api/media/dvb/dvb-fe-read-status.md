---
collection: kernel
version: "6.8"
title: "2.2. Querying frontend status and statistics"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/dvb-fe-read-status.html
fetched_at: 2026-08-21T03:57:47+00:00
---
# 2.2. Querying frontend status and statistics

Once [FE_SET_PROPERTY](fe-get-property.md#fe-get-property) is called, the
frontend will run a kernel thread that will periodically check for the
tuner lock status and provide statistics about the quality of the
signal.

The information about the frontend tuner locking status can be queried
using [ioctl FE_READ_STATUS](fe-read-status.md#fe-read-status).

Signal statistics are provided via
[ioctl FE_SET_PROPERTY, FE_GET_PROPERTY](fe-get-property.md#fe-get-property).

> **Note:**
>
> Most statistics require the demodulator to be fully locked
> (e. g. with [`FE_HAS_LOCK`](frontend-header.md#c.fe_status "fe_status") bit set). See
> [Frontend statistics indicators](frontend-stat-properties.md#frontend-stat-properties) for
> more details.
