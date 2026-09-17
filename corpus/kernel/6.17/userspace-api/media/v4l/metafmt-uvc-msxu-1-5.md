---
collection: kernel
version: "6.17"
title: "2.13.10. V4L2_META_FMT_UVC_MSXU_1_5 (‘UVCM’)"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/metafmt-uvc-msxu-1-5.html
fetched_at: 2026-09-16T16:35:11+00:00
---
# 2.13.10. V4L2_META_FMT_UVC_MSXU_1_5 (‘UVCM’)

Microsoft(R)’s UVC Payload Metadata.

## 2.13.10.1. Description

V4L2_META_FMT_UVC_MSXU_1_5 buffers follow the metadata buffer layout of
V4L2_META_FMT_UVC with the only difference that it includes all the UVC
metadata in the buffer[] field, not just the first 2-12 bytes.

The metadata format follows the specification from Microsoft(R) [1].

[1] <https://docs.microsoft.com/en-us/windows-hardware/drivers/stream/uvc-extensions-1-5>
