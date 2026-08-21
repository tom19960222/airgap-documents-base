---
collection: kernel
version: "6.8"
title: "2.11.1. V4L2_SDR_FMT_CU8 ('CU08')"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/pixfmt-sdr-cu08.html
fetched_at: 2026-08-21T03:57:14+00:00
---
# 2.11.1. V4L2_SDR_FMT_CU8 ('CU08')

Complex unsigned 8-bit IQ sample

## 2.11.1.1. Description

This format contains sequence of complex number samples. Each complex
number consist two parts, called In-phase and Quadrature (IQ). Both I
and Q are represented as a 8 bit unsigned number. I value comes first
and Q value after that.

**Byte Order.**
Each cell is one byte.

|  |  |
| --- | --- |
| start + 0: | I'0 |
| start + 1: | Q'0 |
