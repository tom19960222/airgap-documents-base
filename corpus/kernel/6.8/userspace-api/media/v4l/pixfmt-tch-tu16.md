---
collection: kernel
version: "6.8"
title: "2.12.3. V4L2_TCH_FMT_TU16 ('TU16')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-tch-tu16.html
fetched_at: 2026-08-21T03:57:20+00:00
---
# 2.12.3. V4L2_TCH_FMT_TU16 ('TU16')

*man V4L2_TCH_FMT_TU16(2)*

16-bit unsigned little endian raw touch data

## 2.12.3.1. Description

This format represents unsigned 16-bit data from a touch controller.

This may be used for output for raw and reference data. Values may range from
0 to 65535.

**Byte Order.**
Each cell is one byte.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| start + 0: | R'00low | R'00high | R'01low | R'01high | R'02low | R'02high | R'03low | R'03high |
| start + 8: | R'10low | R'10high | R'11low | R'11high | R'12low | R'12high | R'13low | R'13high |
| start + 16: | R'20low | R'20high | R'21low | R'21high | R'22low | R'22high | R'23low | R'23high |
| start + 24: | R'30low | R'30high | R'31low | R'31high | R'32low | R'32high | R'33low | R'33high |
