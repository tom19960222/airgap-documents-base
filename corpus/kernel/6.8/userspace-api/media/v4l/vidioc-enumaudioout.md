---
collection: kernel
version: "6.8"
title: "7.12. ioctl VIDIOC_ENUMAUDOUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-enumaudioout.html
fetched_at: 2026-08-21T03:41:00+00:00
---
# 7.12. ioctl VIDIOC_ENUMAUDOUT

## 7.12.1. Name

VIDIOC_ENUMAUDOUT - Enumerate audio outputs

## 7.12.2. Synopsis

VIDIOC_ENUMAUDOUT

`int ioctl(int fd, VIDIOC_ENUMAUDOUT, struct v4l2_audioout *argp)`

## 7.12.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout").

## 7.12.4. Description

To query the attributes of an audio output applications initialize the
`index` field and zero out the `reserved` array of a struct
[`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout") and call the `VIDIOC_G_AUDOUT`
ioctl with a pointer to this structure. Drivers fill the rest of the
structure or return an `EINVAL` error code when the index is out of
bounds. To enumerate all audio outputs applications shall begin at index
zero, incrementing by one until the driver returns `EINVAL`.

> **Note:**
>
> Connectors on a TV card to loop back the received audio signal
> to a sound card are not audio outputs in this sense.

See [VIDIOC_G_AUDIOout](vidioc-g-audioout.md#vidioc-g-audout) for a description of struct
[`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout").

## 7.12.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The number of the audio output is out of bounds.
