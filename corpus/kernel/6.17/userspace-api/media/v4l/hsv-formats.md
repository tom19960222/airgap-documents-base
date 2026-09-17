---
collection: kernel
version: "6.17"
title: "2.8. HSV Formats"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/v4l/hsv-formats.html
fetched_at: 2026-09-16T16:51:30+00:00
---
# 2.8. HSV Formats

These formats store the color information of the image
in a geometrical representation. The colors are mapped into a
cylinder, where the angle is the HUE, the height is the VALUE
and the distance to the center is the SATURATION. This is a very
useful format for image segmentation algorithms.

- [2.8.1. Packed HSV formats](pixfmt-packed-hsv.md)
