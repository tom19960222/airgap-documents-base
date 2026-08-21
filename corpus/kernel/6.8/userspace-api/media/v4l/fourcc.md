---
collection: kernel
version: "6.8"
title: "1.24. Guidelines for Video4Linux pixel format 4CCs"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/fourcc.html
fetched_at: 2026-08-21T03:56:50+00:00
---
# 1.24. Guidelines for Video4Linux pixel format 4CCs

Guidelines for Video4Linux 4CC codes defined using v4l2_fourcc() are
specified in this document. First of the characters defines the nature of
the pixel format, compression and colour space. The interpretation of the
other three characters depends on the first one.

Existing 4CCs may not obey these guidelines.

## 1.24.1. Raw bayer

The following first characters are used by raw bayer formats:

- B: raw bayer, uncompressed
- b: raw bayer, DPCM compressed
- a: A-law compressed
- u: u-law compressed

2nd character: pixel order

- B: BGGR
- G: GBRG
- g: GRBG
- R: RGGB

3rd character: uncompressed bits-per-pixel 0--9, A--

4th character: compressed bits-per-pixel 0--9, A--
