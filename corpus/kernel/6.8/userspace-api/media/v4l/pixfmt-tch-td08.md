---
collection: kernel
version: "6.8"
title: "2.12.2. V4L2_TCH_FMT_DELTA_TD08 ('TD08')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-tch-td08.html
fetched_at: 2026-08-21T03:57:19+00:00
---
# 2.12.2. V4L2_TCH_FMT_DELTA_TD08 ('TD08')

*man V4L2_TCH_FMT_DELTA_TD08(2)*

8-bit signed Touch Delta

## 2.12.2.1. Description

This format represents delta data from a touch controller.

Delta values may range from -128 to 127. Typically the values will vary through
a small range depending on whether the sensor is touched or not. The full value
may be seen if one of the touchscreen nodes has a fault or the line is not
connected.

**Byte Order.**
Each cell is one byte.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| start + 0: | D'00 | D'01 | D'02 | D'03 |
| start + 4: | D'10 | D'11 | D'12 | D'13 |
| start + 8: | D'20 | D'21 | D'22 | D'23 |
| start + 12: | D'30 | D'31 | D'32 | D'33 |
