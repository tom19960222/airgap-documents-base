---
collection: kernel
version: "6.8"
title: "7.36. ioctl VIDIOC_G_OUTPUT, VIDIOC_S_OUTPUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-output.html
fetched_at: 2026-08-21T03:41:01+00:00
---
# 7.36. ioctl VIDIOC_G_OUTPUT, VIDIOC_S_OUTPUT

## 7.36.1. Name

VIDIOC_G_OUTPUT - VIDIOC_S_OUTPUT - Query or select the current video output

## 7.36.2. Synopsis

VIDIOC_G_OUTPUT

`int ioctl(int fd, VIDIOC_G_OUTPUT, int *argp)`

VIDIOC_S_OUTPUT

`int ioctl(int fd, VIDIOC_S_OUTPUT, int *argp)`

## 7.36.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to an integer with output index.

## 7.36.4. Description

To query the current video output applications call the
[VIDIOC_G_OUTPUT](vidioc-g-output.md#vidioc-g-output) ioctl with a pointer to an integer where the driver
stores the number of the output, as in the struct
[`v4l2_output`](vidioc-enumoutput.md#c.V4L.v4l2_output "v4l2_output") `index` field. This ioctl will
fail only when there are no video outputs, returning the `EINVAL` error
code.

To select a video output applications store the number of the desired
output in an integer and call the [VIDIOC_S_OUTPUT](vidioc-g-output.md#vidioc-g-output) ioctl with a
pointer to this integer. Side effects are possible. For example outputs
may support different video standards, so the driver may implicitly
switch the current standard. Because of these possible side
effects applications must select an output before querying or
negotiating any other parameters.

Information about video outputs is available using the
[ioctl VIDIOC_ENUMOUTPUT](vidioc-enumoutput.md#vidioc-enumoutput) ioctl.

## 7.36.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The number of the video output is out of bounds, or there are no
    video outputs at all.
