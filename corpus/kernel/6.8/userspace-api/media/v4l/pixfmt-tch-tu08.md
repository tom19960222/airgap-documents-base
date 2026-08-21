---
collection: kernel
version: "6.8"
title: "2.12.4. V4L2_TCH_FMT_TU08 ('TU08')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-tch-tu08.html
fetched_at: 2026-08-21T03:57:20+00:00
---
# 2.12.4. V4L2_TCH_FMT_TU08 ('TU08')

*man V4L2_TCH_FMT_TU08(2)*

8-bit unsigned raw touch data

## 2.12.4.1. Description

This format represents unsigned 8-bit data from a touch controller.

This may be used for output for raw and reference data. Values may range from
0 to 255.

**Byte Order.**
Each cell is one byte.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| start + 0: | R'00 | R'01 | R'02 | R'03 |
| start + 4: | R'10 | R'11 | R'12 | R'13 |
| start + 8: | R'20 | R'21 | R'22 | R'23 |
| start + 12: | R'30 | R'31 | R'32 | R'33 |
