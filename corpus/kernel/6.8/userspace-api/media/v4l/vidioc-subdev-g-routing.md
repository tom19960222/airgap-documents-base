---
collection: kernel
version: "6.8"
title: "7.61. ioctl VIDIOC_SUBDEV_G_ROUTING, VIDIOC_SUBDEV_S_ROUTING"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-subdev-g-routing.html
fetched_at: 2026-08-21T03:40:57+00:00
---
# 7.61. ioctl VIDIOC_SUBDEV_G_ROUTING, VIDIOC_SUBDEV_S_ROUTING

## 7.61.1. Name

VIDIOC_SUBDEV_G_ROUTING - VIDIOC_SUBDEV_S_ROUTING - Get or set routing between streams of media pads in a media entity.

## 7.61.2. Synopsis

VIDIOC_SUBDEV_G_ROUTING

`int ioctl(int fd, VIDIOC_SUBDEV_G_ROUTING, struct v4l2_subdev_routing *argp)`

VIDIOC_SUBDEV_S_ROUTING

`int ioctl(int fd, VIDIOC_SUBDEV_S_ROUTING, struct v4l2_subdev_routing *argp)`

## 7.61.3. Arguments

`fd`
:   File descriptor returned by [open()](func-open.md#func-open).

`argp`
:   Pointer to struct [`v4l2_subdev_routing`](vidioc-subdev-g-routing.md#c.V4L.v4l2_subdev_routing "v4l2_subdev_routing").

## 7.61.4. Description

These ioctls are used to get and set the routing in a media entity.
The routing configuration determines the flows of data inside an entity.

Drivers report their current routing tables using the
`VIDIOC_SUBDEV_G_ROUTING` ioctl and application may enable or disable routes
with the `VIDIOC_SUBDEV_S_ROUTING` ioctl, by adding or removing routes and
setting or clearing flags of the `flags` field of a
struct [`v4l2_subdev_route`](vidioc-subdev-g-routing.md#c.V4L.v4l2_subdev_route "v4l2_subdev_route").

All stream configurations are reset when `VIDIOC_SUBDEV_S_ROUTING` is called. This
means that the userspace must reconfigure all streams after calling the ioctl
with e.g. `VIDIOC_SUBDEV_S_FMT`.

Only subdevices which have both sink and source pads can support routing.

When inspecting routes through `VIDIOC_SUBDEV_G_ROUTING` and the application
provided `num_routes` is not big enough to contain all the available routes
the subdevice exposes, drivers return the ENOSPC error code and adjust the
value of the `num_routes` field. Application should then reserve enough memory
for all the route entries and call `VIDIOC_SUBDEV_G_ROUTING` again.

On a successful `VIDIOC_SUBDEV_G_ROUTING` call the driver updates the
`num_routes` field to reflect the actual number of routes returned.

type v4l2_subdev_routing

struct v4l2_subdev_routing

|  |  |  |
| --- | --- | --- |
| __u32 | `which` | Routing table to be accessed, from enum [v4l2_subdev_format_whence](vidioc-subdev-g-fmt.md#v4l2-subdev-format-whence). |
| struct [`v4l2_subdev_route`](vidioc-subdev-g-routing.md#c.V4L.v4l2_subdev_route "v4l2_subdev_route") | `routes[]` | Array of struct [`v4l2_subdev_route`](vidioc-subdev-g-routing.md#c.V4L.v4l2_subdev_route "v4l2_subdev_route") entries |
| __u32 | `num_routes` | Number of entries of the routes array |
| __u32 | `reserved`[5] | Reserved for future extensions. Applications and drivers must set the array to zero. |

type v4l2_subdev_route

struct v4l2_subdev_route

|  |  |  |
| --- | --- | --- |
| __u32 | `sink_pad` | Sink pad number. |
| __u32 | `sink_stream` | Sink pad stream number. |
| __u32 | `source_pad` | Source pad number. |
| __u32 | `source_stream` | Source pad stream number. |
| __u32 | `flags` | Route enable/disable flags [v4l2_subdev_routing_flags](vidioc-subdev-g-routing.md#v4l2-subdev-routing-flags). |
| __u32 | `reserved`[5] | Reserved for future extensions. Applications and drivers must set the array to zero. |

enum v4l2_subdev_routing_flags

|  |  |  |
| --- | --- | --- |
| V4L2_SUBDEV_ROUTE_FL_ACTIVE | 0x0001 | The route is enabled. Set by applications. |

## 7.61.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

ENOSPC
:   The application provided `num_routes` is not big enough to contain
    all the available routes the subdevice exposes.

EINVAL
:   The sink or source pad identifiers reference a non-existing pad or reference
    pads of different types (ie. the sink_pad identifiers refers to a source
    pad), or the `which` field has an unsupported value.

E2BIG
:   The application provided `num_routes` for `VIDIOC_SUBDEV_S_ROUTING` is
    larger than the number of routes the driver can handle.
