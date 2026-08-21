---
collection: kernel
version: "6.8"
title: "2.11.2. V4L2_SDR_FMT_CU16LE ('CU16')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-sdr-cu16le.html
fetched_at: 2026-08-21T03:57:15+00:00
---
# 2.11.2. V4L2_SDR_FMT_CU16LE ('CU16')

Complex unsigned 16-bit little endian IQ sample

## 2.11.2.1. Description

This format contains sequence of complex number samples. Each complex
number consist two parts, called In-phase and Quadrature (IQ). Both I
and Q are represented as a 16 bit unsigned little endian number. I value
comes first and Q value after that.

**Byte Order.**
Each cell is one byte.

|  |  |  |
| --- | --- | --- |
| start + 0: | I'0[7:0] | I'0[15:8] |
| start + 2: | Q'0[7:0] | Q'0[15:8] |
