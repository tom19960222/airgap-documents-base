---
collection: kernel
version: "6.8"
title: "2.11.5. V4L2_SDR_FMT_RU12LE ('RU12')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-sdr-ru12le.html
fetched_at: 2026-08-21T03:57:16+00:00
---
# 2.11.5. V4L2_SDR_FMT_RU12LE ('RU12')

Real unsigned 12-bit little endian sample

## 2.11.5.1. Description

This format contains sequence of real number samples. Each sample is
represented as a 12 bit unsigned little endian number. Sample is stored
in 16 bit space with unused high bits padded with 0.

**Byte Order.**
Each cell is one byte.

|  |  |  |
| --- | --- | --- |
| start + 0: | I'0[7:0] | I'0[11:8] |
