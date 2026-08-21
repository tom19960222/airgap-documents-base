---
collection: kernel
version: "6.8"
title: "7.33. ioctl VIDIOC_G_INPUT, VIDIOC_S_INPUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-input.html
fetched_at: 2026-08-21T03:41:01+00:00
---
# 7.33. ioctl VIDIOC_G_INPUT, VIDIOC_S_INPUT

## 7.33.1. Name

VIDIOC_G_INPUT - VIDIOC_S_INPUT - Query or select the current video input

## 7.33.2. Synopsis

VIDIOC_G_INPUT

`int ioctl(int fd, VIDIOC_G_INPUT, int *argp)`

VIDIOC_S_INPUT

`int ioctl(int fd, VIDIOC_S_INPUT, int *argp)`

## 7.33.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer an integer with input index.

## 7.33.4. Description

To query the current video input applications call the
[VIDIOC_G_INPUT](vidioc-g-input.md#vidioc-g-input) ioctl with a pointer to an integer where the driver
stores the number of the input, as in the struct
[`v4l2_input`](vidioc-enuminput.md#c.V4L.v4l2_input "v4l2_input") `index` field. This ioctl will fail
only when there are no video inputs, returning `EINVAL`.

To select a video input applications store the number of the desired
input in an integer and call the [VIDIOC_S_INPUT](vidioc-g-input.md#vidioc-g-input) ioctl with a pointer
to this integer. Side effects are possible. For example inputs may
support different video standards, so the driver may implicitly switch
the current standard. Because of these possible side effects
applications must select an input before querying or negotiating any
other parameters.

Information about video inputs is available using the
[ioctl VIDIOC_ENUMINPUT](vidioc-enuminput.md#vidioc-enuminput) ioctl.

## 7.33.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The number of the video input is out of bounds.
