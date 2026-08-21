---
collection: kernel
version: "6.8"
title: "7.62. ioctl VIDIOC_SUBDEV_G_SELECTION, VIDIOC_SUBDEV_S_SELECTION"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subdev-g-selection.html
fetched_at: 2026-08-21T03:40:57+00:00
---
# 7.62. ioctl VIDIOC_SUBDEV_G_SELECTION, VIDIOC_SUBDEV_S_SELECTION

## 7.62.1. Name

VIDIOC_SUBDEV_G_SELECTION - VIDIOC_SUBDEV_S_SELECTION - Get or set selection rectangles on a subdev pad

## 7.62.2. Synopsis

VIDIOC_SUBDEV_G_SELECTION

`int ioctl(int fd, VIDIOC_SUBDEV_G_SELECTION, struct v4l2_subdev_selection *argp)`

VIDIOC_SUBDEV_S_SELECTION

`int ioctl(int fd, VIDIOC_SUBDEV_S_SELECTION, struct v4l2_subdev_selection *argp)`

## 7.62.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_subdev_selection`](vidioc-subdev-g-selection.md#c.V4L.v4l2_subdev_selection "v4l2_subdev_selection").

## 7.62.4. Description

The selections are used to configure various image processing
functionality performed by the subdevs which affect the image size. This
currently includes cropping, scaling and composition.

The selection API replaces
[the old subdev crop API](vidioc-subdev-g-crop.md#vidioc-subdev-g-crop). All the
function of the crop API, and more, are supported by the selections API.

See [Sub-device Interface](dev-subdev.md#subdev) for more information on how each selection target
affects the image processing pipeline inside the subdevice.

If the subdev device node has been registered in read-only mode, calls to
`VIDIOC_SUBDEV_S_SELECTION` are only valid if the `which` field is set to
`V4L2_SUBDEV_FORMAT_TRY`, otherwise an error is returned and the errno
variable is set to `-EPERM`.

### 7.62.4.1. Types of selection targets

There are two types of selection targets: actual and bounds. The actual
targets are the targets which configure the hardware. The BOUNDS target
will return a rectangle that contain all possible actual rectangles.

### 7.62.4.2. Discovering supported features

To discover which targets are supported, the user can perform
`VIDIOC_SUBDEV_G_SELECTION` on them. Any unsupported target will
return `EINVAL`.

Selection targets and flags are documented in
[Common selection definitions](selections-common.md#v4l2-selections-common).

type v4l2_subdev_selection

struct v4l2_subdev_selection

|  |  |  |
| --- | --- | --- |
| __u32 | `which` | Active or try selection, from enum [v4l2_subdev_format_whence](vidioc-subdev-g-fmt.md#v4l2-subdev-format-whence). |
| __u32 | `pad` | Pad number as reported by the media framework. |
| __u32 | `target` | Target selection rectangle. See [Common selection definitions](selections-common.md#v4l2-selections-common). |
| __u32 | `flags` | Flags. See [Selection flags](v4l2-selection-flags.md#v4l2-selection-flags). |
| struct [`v4l2_rect`](dev-overlay.md#c.v4l2_rect "v4l2_rect") | `r` | Selection rectangle, in pixels. |
| __u32 | `stream` | Stream identifier. |
| __u32 | `reserved`[7] | Reserved for future extensions. Applications and drivers must set the array to zero. |

## 7.62.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EBUSY
:   The selection rectangle can't be changed because the pad is
    currently busy. This can be caused, for instance, by an active video
    stream on the pad. The ioctl must not be retried without performing
    another action to fix the problem first. Only returned by
    `VIDIOC_SUBDEV_S_SELECTION`

EINVAL
:   The struct [`v4l2_subdev_selection`](vidioc-subdev-g-selection.md#c.V4L.v4l2_subdev_selection "v4l2_subdev_selection") `pad` references a
    non-existing pad, the `which` field has an unsupported value, or the
    selection target is not supported on the given subdev pad.

EPERM
:   The `VIDIOC_SUBDEV_S_SELECTION` ioctl has been called on a read-only
    subdevice and the `which` field is set to `V4L2_SUBDEV_FORMAT_ACTIVE`.
