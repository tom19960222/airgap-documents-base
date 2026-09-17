---
collection: kernel
version: "6.17"
title: "2.13.11. V4L2_META_FMT_VIVID (‘VIVD’)"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/metafmt-vivid.html
fetched_at: 2026-09-16T16:55:44+00:00
---
# 2.13.11. V4L2_META_FMT_VIVID (‘VIVD’)

VIVID Metadata Format

## 2.13.11.1. Description

This describes metadata format used by the vivid driver.

It sets Brightness, Saturation, Contrast and Hue, each of which maps to
corresponding controls of the vivid driver with respect to the range and default values.

It contains the following fields:

VIVID Metadata

| Field | Description |
| --- | --- |
| u16 brightness; | Image brightness, the value is in the range 0 to 255, with the default value as 128. |
| u16 contrast; | Image contrast, the value is in the range 0 to 255, with the default value as 128. |
| u16 saturation; | Image color saturation, the value is in the range 0 to 255, with the default value as 128. |
| s16 hue; | Image color balance, the value is in the range -128 to 128, with the default value as 0. |
