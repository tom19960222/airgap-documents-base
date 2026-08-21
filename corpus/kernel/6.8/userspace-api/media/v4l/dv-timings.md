---
collection: kernel
version: "6.8"
title: "1.8. Digital Video (DV) Timings"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/dv-timings.html
fetched_at: 2026-08-21T03:56:42+00:00
---
# 1.8. Digital Video (DV) Timings

The video standards discussed so far have been dealing with Analog TV
and the corresponding video timings. Today there are many more different
hardware interfaces such as High Definition TV interfaces (HDMI), VGA,
DVI connectors etc., that carry video signals and there is a need to
extend the API to select the video timings for these interfaces. Since
it is not possible to extend the [v4l2_std_id](vidioc-enumstd.md#v4l2-std-id)
due to the limited bits available, a new set of ioctls was added to
set/get video timings at the input and output.

These ioctls deal with the detailed digital video timings that define
each video format. This includes parameters such as the active video
width and height, signal polarities, frontporches, backporches, sync
widths etc. The `linux/v4l2-dv-timings.h` header can be used to get
the timings of the formats in the [CEA-861-E](biblio.md#cea861) and [VESA DMT](biblio.md#vesadmt)
standards.

To enumerate and query the attributes of the DV timings supported by a
device applications use the
[ioctl VIDIOC_ENUM_DV_TIMINGS, VIDIOC_SUBDEV_ENUM_DV_TIMINGS](vidioc-enum-dv-timings.md#vidioc-enum-dv-timings) and
[ioctl VIDIOC_DV_TIMINGS_CAP, VIDIOC_SUBDEV_DV_TIMINGS_CAP](vidioc-dv-timings-cap.md#vidioc-dv-timings-cap) ioctls. To set
DV timings for the device applications use the
[VIDIOC_S_DV_TIMINGS](vidioc-g-dv-timings.md#vidioc-g-dv-timings) ioctl and to get
current DV timings they use the
[VIDIOC_G_DV_TIMINGS](vidioc-g-dv-timings.md#vidioc-g-dv-timings) ioctl. To detect
the DV timings as seen by the video receiver applications use the
[ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings) ioctl.

When the hardware detects a video source change (e.g. the video
signal appears or disappears, or the video resolution changes), then
it will issue a V4L2_EVENT_SOURCE_CHANGE event. Use the
[ioctl VIDIOC_SUBSCRIBE_EVENT](vidioc-subscribe-event.md#vidioc-subscribe-event) and the
[ioctl VIDIOC_DQEVENT](vidioc-dqevent.md#vidioc-dqevent) to check if this event was reported.

If the video signal changed, then the application has to stop
streaming, free all buffers, and call the [ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings)
to obtain the new video timings, and if they are valid, it can set
those by calling the [ioctl VIDIOC_S_DV_TIMINGS](vidioc-g-dv-timings.md#vidioc-g-dv-timings).
This will also update the format, so use the [ioctl VIDIOC_G_FMT](vidioc-g-fmt.md#vidioc-g-fmt)
to obtain the new format. Now the application can allocate new buffers
and start streaming again.

The [ioctl VIDIOC_QUERY_DV_TIMINGS](vidioc-query-dv-timings.md#vidioc-query-dv-timings) will just report what the
hardware detects, it will never change the configuration. If the
currently set timings and the actually detected timings differ, then
typically this will mean that you will not be able to capture any
video. The correct approach is to rely on the V4L2_EVENT_SOURCE_CHANGE
event so you know when something changed.

Applications can make use of the [Input capabilities](vidioc-enuminput.md#input-capabilities) and
[Output capabilities](vidioc-enumoutput.md#output-capabilities) flags to determine whether the digital
video ioctls can be used with the given input or output.
