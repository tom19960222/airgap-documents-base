---
collection: kernel
version: "6.8"
title: "2.4. Indexed Format"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-indexed.html
fetched_at: 2026-08-21T03:56:57+00:00
---
# 2.4. Indexed Format

In this format each pixel is represented by an 8 bit index into a 256
entry ARGB palette. It is intended for
[Video Output Overlays](dev-osd.md#osd) only. There are no ioctls to access
the palette, this must be done with ioctls of the Linux framebuffer API.

Indexed Image Format

| Identifier | Code |  | Byte 0 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | Bit | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| `V4L2_PIX_FMT_PAL8` | 'PAL8' |  | i7 | i6 | i5 | i4 | i3 | i2 | i1 | i0 |
