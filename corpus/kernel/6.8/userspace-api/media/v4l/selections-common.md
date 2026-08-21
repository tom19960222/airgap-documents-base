---
collection: kernel
version: "6.8"
title: "8.1. Common selection definitions"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/selections-common.html
fetched_at: 2026-08-21T03:57:40+00:00
---
# 8.1. Common selection definitions

While the [V4L2 selection API](selection-api.md#selection-api) and
[V4L2 subdev selection APIs](dev-subdev.md#v4l2-subdev-selections) are very
similar, there's one fundamental difference between the two. On
sub-device API, the selection rectangle refers to the media bus format,
and is bound to a sub-device's pad. On the V4L2 interface the selection
rectangles refer to the in-memory pixel format.

This section defines the common definitions of the selection interfaces
on the two APIs.

- [8.1.1. Selection targets](v4l2-selection-targets.md)
- [8.1.2. Selection flags](v4l2-selection-flags.md)
