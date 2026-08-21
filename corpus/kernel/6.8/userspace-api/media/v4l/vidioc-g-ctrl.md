---
collection: kernel
version: "6.8"
title: "7.25. ioctl VIDIOC_G_CTRL, VIDIOC_S_CTRL"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-g-ctrl.html
fetched_at: 2026-08-21T03:40:32+00:00
---
# 7.25. ioctl VIDIOC_G_CTRL, VIDIOC_S_CTRL

## 7.25.1. Name

VIDIOC_G_CTRL - VIDIOC_S_CTRL - Get or set the value of a control

## 7.25.2. Synopsis

VIDIOC_G_CTRL

`int ioctl(int fd, VIDIOC_G_CTRL, struct v4l2_control *argp)`

VIDIOC_S_CTRL

`int ioctl(int fd, VIDIOC_S_CTRL, struct v4l2_control *argp)`

## 7.25.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_control`](vidioc-g-ctrl.md#c.V4L.v4l2_control "v4l2_control").

## 7.25.4. Description

To get the current value of a control applications initialize the `id`
field of a struct [`v4l2_control`](vidioc-g-ctrl.md#c.V4L.v4l2_control "v4l2_control") and call the
[VIDIOC_G_CTRL](vidioc-g-ctrl.md#vidioc-g-ctrl) ioctl with a pointer to this structure. To change the
value of a control applications initialize the `id` and `value`
fields of a struct [`v4l2_control`](vidioc-g-ctrl.md#c.V4L.v4l2_control "v4l2_control") and call the
[VIDIOC_S_CTRL](vidioc-g-ctrl.md#vidioc-g-ctrl) ioctl.

When the `id` is invalid drivers return an `EINVAL` error code. When the
`value` is out of bounds drivers can choose to take the closest valid
value or return an `ERANGE` error code, whatever seems more appropriate.
However, [VIDIOC_S_CTRL](vidioc-g-ctrl.md#vidioc-g-ctrl) is a write-only ioctl, it does not return the
actual new value. If the `value` is inappropriate for the control
(e.g. if it refers to an unsupported menu index of a menu control), then
EINVAL error code is returned as well.

These ioctls work only with user controls. For other control classes the
[VIDIOC_G_EXT_CTRLS](vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls),
[VIDIOC_S_EXT_CTRLS](vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) or
[VIDIOC_TRY_EXT_CTRLS](vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) must be used.

type v4l2_control

struct v4l2_control

|  |  |  |
| --- | --- | --- |
| __u32 | `id` | Identifies the control, set by the application. |
| __s32 | `value` | New value or current value. |

## 7.25.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The struct [`v4l2_control`](vidioc-g-ctrl.md#c.V4L.v4l2_control "v4l2_control") `id` is invalid
    or the `value` is inappropriate for the given control (i.e. if a
    menu item is selected that is not supported by the driver according
    to [VIDIOC_QUERYMENU](vidioc-queryctrl.md#vidioc-queryctrl)).

ERANGE
:   The struct [`v4l2_control`](vidioc-g-ctrl.md#c.V4L.v4l2_control "v4l2_control") `value` is out of
    bounds.

EBUSY
:   The control is temporarily not changeable, possibly because another
    applications took over control of the device function this control
    belongs to.

EACCES
:   Attempt to set a read-only control or to get a write-only control.

    Or if there is an attempt to set an inactive control and the driver is
    not capable of caching the new value until the control is active again.
