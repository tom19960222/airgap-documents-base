---
collection: kernel
version: "6.8"
title: "7.23. ioctl VIDIOC_G_AUDOUT, VIDIOC_S_AUDOUT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-audioout.html
fetched_at: 2026-08-21T03:40:28+00:00
---
# 7.23. ioctl VIDIOC_G_AUDOUT, VIDIOC_S_AUDOUT

## 7.23.1. Name

VIDIOC_G_AUDOUT - VIDIOC_S_AUDOUT - Query or select the current audio output

## 7.23.2. Synopsis

VIDIOC_G_AUDOUT

`int ioctl(int fd, VIDIOC_G_AUDOUT, struct v4l2_audioout *argp)`

VIDIOC_S_AUDOUT

`int ioctl(int fd, VIDIOC_S_AUDOUT, const struct v4l2_audioout *argp)`

## 7.23.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout").

## 7.23.4. Description

To query the current audio output applications zero out the `reserved`
array of a struct [`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout") and call the
`VIDIOC_G_AUDOUT` ioctl with a pointer to this structure. Drivers fill
the rest of the structure or return an `EINVAL` error code when the device
has no audio inputs, or none which combine with the current video
output.

Audio outputs have no writable properties. Nevertheless, to select the
current audio output applications can initialize the `index` field and
`reserved` array (which in the future may contain writable properties)
of a struct [`v4l2_audioout`](vidioc-g-audioout.md#c.V4L.v4l2_audioout "v4l2_audioout") structure and call the
`VIDIOC_S_AUDOUT` ioctl. Drivers switch to the requested output or
return the `EINVAL` error code when the index is out of bounds. This is a
write-only ioctl, it does not return the current audio output attributes
as `VIDIOC_G_AUDOUT` does.

> **Note:**
>
> Connectors on a TV card to loop back the received audio signal
> to a sound card are not audio outputs in this sense.

type v4l2_audioout

struct v4l2_audioout

|  |  |  |
| --- | --- | --- |
| __u32 | `index` | Identifies the audio output, set by the driver or application. |
| __u8 | `name`[32] | Name of the audio output, a NUL-terminated ASCII string, for example: "Line Out". This information is intended for the user, preferably the connector label on the device itself. |
| __u32 | `capability` | Audio capability flags, none defined yet. Drivers must set this field to zero. |
| __u32 | `mode` | Audio mode, none defined yet. Drivers and applications (on `VIDIOC_S_AUDOUT`) must set this field to zero. |
| __u32 | `reserved`[2] | Reserved for future extensions. Drivers and applications must set the array to zero. |

## 7.23.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   No audio outputs combine with the current video output, or the
    number of the selected audio output is out of bounds or it does not
    combine.
