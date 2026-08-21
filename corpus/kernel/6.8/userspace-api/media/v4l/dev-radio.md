---
collection: kernel
version: "6.8"
title: "4.8. Radio Interface"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/dev-radio.html
fetched_at: 2026-08-21T03:57:34+00:00
---
# 4.8. Radio Interface

This interface is intended for AM and FM (analog) radio receivers and
transmitters.

Conventionally V4L2 radio devices are accessed through character device
special files named `/dev/radio` and `/dev/radio0` to
`/dev/radio63` with major number 81 and minor numbers 64 to 127.

## 4.8.1. Querying Capabilities

Devices supporting the radio interface set the `V4L2_CAP_RADIO` and
`V4L2_CAP_TUNER` or `V4L2_CAP_MODULATOR` flag in the
`capabilities` field of struct
`v4l2_capability` returned by the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl. Other combinations of
capability flags are reserved for future extensions.

## 4.8.2. Supplemental Functions

Radio devices can support [controls](control.md#control), and must support
the [tuner or modulator](tuner.md#tuner) ioctls.

They do not support the video input or output, audio input or output,
video standard, cropping and scaling, compression and streaming
parameter, or overlay ioctls. All other ioctls and I/O methods are
reserved for future extensions.

## 4.8.3. Programming

Radio devices may have a couple audio controls (as discussed in
[User Controls](control.md#control)) such as a volume control, possibly custom controls.
Further all radio devices have one tuner or modulator (these are
discussed in [Tuners and Modulators](tuner.md#tuner)) with index number zero to select the radio
frequency and to determine if a monaural or FM stereo program is
received/emitted. Drivers switch automatically between AM and FM
depending on the selected frequency. The
[VIDIOC_G_TUNER](vidioc-g-tuner.md#vidioc-g-tuner) or
[VIDIOC_G_MODULATOR](vidioc-g-modulator.md#vidioc-g-modulator) ioctl reports the
supported frequency range.
