---
collection: kernel
version: "6.8"
title: "2.13.4. V4L2_META_FMT_UVC ('UVCH')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/metafmt-uvc.html
fetched_at: 2026-08-21T03:57:22+00:00
---
# 2.13.4. V4L2_META_FMT_UVC ('UVCH')

UVC Payload Header Data

## 2.13.4.1. Description

This format describes standard UVC metadata, extracted from UVC packet headers
and provided by the UVC driver through metadata video nodes. That data includes
exact copies of the standard part of UVC Payload Header contents and auxiliary
timing information, required for precise interpretation of timestamps, contained
in those headers. See section "2.4.3.3 Video and Still Image Payload Headers" of
the "UVC 1.5 Class specification" for details.

Each UVC payload header can be between 2 and 12 bytes large. Buffers can
contain multiple headers, if multiple such headers have been transmitted by the
camera for the respective frame. However, the driver may drop headers when the
buffer is full, when they contain no useful information (e.g. those without the
SCR field or with that field identical to the previous header), or generally to
perform rate limiting when the device sends a large number of headers.

Each individual block contains the following fields:

UVC Metadata Block

| Field | Description |
| --- | --- |
| __u64 ts; | system timestamp in host byte order, measured by the driver upon reception of the payload |
| __u16 sof; | USB Frame Number in host byte order, also obtained by the driver as close as possible to the above timestamp to enable correlation between them |
| *The rest is an exact copy of the UVC payload header:* | |
| __u8 length; | length of the rest of the block, including this field |
| __u8 flags; | Flags, indicating presence of other standard UVC fields |
| __u8 buf[]; | The rest of the header, possibly including UVC PTS and SCR fields |
