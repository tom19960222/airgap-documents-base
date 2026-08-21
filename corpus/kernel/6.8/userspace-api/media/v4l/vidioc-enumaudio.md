---
collection: kernel
version: "6.8"
title: "7.11. ioctl VIDIOC_ENUMAUDIO"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-enumaudio.html
fetched_at: 2026-08-21T03:40:59+00:00
---
# 7.11. ioctl VIDIOC_ENUMAUDIO

## 7.11.1. Name

VIDIOC_ENUMAUDIO - Enumerate audio inputs

## 7.11.2. Synopsis

VIDIOC_ENUMAUDIO

`int ioctl(int fd, VIDIOC_ENUMAUDIO, struct v4l2_audio *argp)`

## 7.11.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_audio`](vidioc-g-audio.md#c.V4L.v4l2_audio "v4l2_audio").

## 7.11.4. Description

To query the attributes of an audio input applications initialize the
`index` field and zero out the `reserved` array of a struct
[`v4l2_audio`](vidioc-g-audio.md#c.V4L.v4l2_audio "v4l2_audio") and call the [ioctl VIDIOC_ENUMAUDIO](vidioc-enumaudio.md#vidioc-enumaudio)
ioctl with a pointer to this structure. Drivers fill the rest of the
structure or return an `EINVAL` error code when the index is out of
bounds. To enumerate all audio inputs applications shall begin at index
zero, incrementing by one until the driver returns `EINVAL`.

See [VIDIOC_G_AUDIO](vidioc-g-audio.md#vidioc-g-audio) for a description of struct
[`v4l2_audio`](vidioc-g-audio.md#c.V4L.v4l2_audio "v4l2_audio").

## 7.11.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The number of the audio input is out of bounds.
