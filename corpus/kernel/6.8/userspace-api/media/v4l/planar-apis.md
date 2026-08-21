---
collection: kernel
version: "6.8"
title: "1.26. Single- and multi-planar APIs"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/planar-apis.html
fetched_at: 2026-08-21T03:56:51+00:00
---
# 1.26. Single- and multi-planar APIs

Some devices require data for each input or output video frame to be
placed in discontiguous memory buffers. In such cases, one video frame
has to be addressed using more than one memory address, i.e. one pointer
per "plane". A plane is a sub-buffer of the current frame. For examples
of such formats see [Image Formats](pixfmt.md#pixfmt).

Initially, V4L2 API did not support multi-planar buffers and a set of
extensions has been introduced to handle them. Those extensions
constitute what is being referred to as the "multi-planar API".

Some of the V4L2 API calls and structures are interpreted differently,
depending on whether single- or multi-planar API is being used. An
application can choose whether to use one or the other by passing a
corresponding buffer type to its ioctl calls. Multi-planar versions of
buffer types are suffixed with an `_MPLANE` string. For a list of
available multi-planar buffer types see enum
`v4l2_buf_type`.

## 1.26.1. Multi-planar formats

Multi-planar API introduces new multi-planar formats. Those formats use
a separate set of FourCC codes. It is important to distinguish between
the multi-planar API and a multi-planar format. Multi-planar API calls
can handle all single-planar formats as well (as long as they are passed
in multi-planar API structures), while the single-planar API cannot
handle multi-planar formats.

## 1.26.2. Calls that distinguish between single and multi-planar APIs

[VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap)
:   Two additional multi-planar capabilities are added. They can be set
    together with non-multi-planar ones for devices that handle both
    single- and multi-planar formats.

[VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt), [VIDIOC_S_FMT](vidioc-g-fmt.md#vidioc-g-fmt), [VIDIOC_TRY_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
:   New structures for describing multi-planar formats are added: struct
    [`v4l2_pix_format_mplane`](pixfmt-v4l2-mplane.md#c.v4l2_pix_format_mplane "v4l2_pix_format_mplane") and
    struct [`v4l2_plane_pix_format`](pixfmt-v4l2-mplane.md#c.v4l2_plane_pix_format "v4l2_plane_pix_format").
    Drivers may define new multi-planar formats, which have distinct
    FourCC codes from the existing single-planar ones.

[VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf), [VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf), [VIDIOC_QUERYBUF](vidioc-querybuf.md#vidioc-querybuf)
:   A new struct `v4l2_plane` structure for
    describing planes is added. Arrays of this structure are passed in
    the new `m.planes` field of struct
    `v4l2_buffer`.

[VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs)
:   Will allocate multi-planar buffers as requested.
