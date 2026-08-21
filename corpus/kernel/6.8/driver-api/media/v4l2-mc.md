---
collection: kernel
version: "6.8"
title: "2.19. V4L2 Media Controller functions and data structures"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-mc.html
fetched_at: 2026-08-21T03:41:12+00:00
---
# 2.19. V4L2 Media Controller functions and data structures

int v4l2_mc_create_media_graph(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   create Media Controller links at the graph.

**Parameters**

`struct media_device *mdev`
:   pointer to the [`media_device`](mc-core.md#c.media_device "media_device") struct.

**Description**

Add links between the entities commonly found on PC customer's hardware at
the V4L2 side: camera sensors, audio and video PLL-IF decoders, tuners,
analog TV decoder and I/O entities (video, VBI and Software Defined Radio).

> **Note:**
>
> Webcams are modelled on a very simple way: the sensor is
> connected directly to the I/O entity. All dirty details, like
> scaler and crop HW are hidden. While such mapping is enough for v4l2
> interface centric PC-consumer's hardware, V4L2 subdev centric camera
> hardware should not use this routine, as it will not build the right graph.

int v4l_enable_media_source(struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev)
:   Hold media source for exclusive use if free

**Parameters**

`struct video_device *vdev`
:   pointer to [`struct video_device`](v4l2-dev.md#c.video_device "video_device")

**Description**

This interface calls enable_source handler to determine if
media source is free for use. The enable_source handler is
responsible for checking is the media source is free and
start a pipeline between the media source and the media
entity associated with the video device. This interface
should be called from v4l2-core and dvb-core interfaces
that change the source configuration.

**Return**

returns zero on success or a negative error code.

void v4l_disable_media_source(struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev)
:   Release media source

**Parameters**

`struct video_device *vdev`
:   pointer to [`struct video_device`](v4l2-dev.md#c.video_device "video_device")

**Description**

This interface calls disable_source handler to release
the media source. The disable_source handler stops the
active media pipeline between the media source and the
media entity associated with the video device.

**Return**

returns zero on success or a negative error code.

int v4l2_create_fwnode_links_to_pad(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*src_sd, struct [media_pad](mc-core.md#c.media_pad "media_pad") \*sink, u32 flags)
:   Create fwnode-based links from a source subdev to a sink pad.

**Parameters**

`struct v4l2_subdev *src_sd`
:   pointer to a source subdev

`struct media_pad *sink`
:   pointer to a sink pad

`u32 flags`
:   the link flags

**Description**

This function searches for fwnode endpoint connections from a source
subdevice to a single sink pad, and if suitable connections are found,
translates them into media links to that pad. The function can be
called by the sink, in its v4l2-async notifier bound callback, to create
links from a bound source subdevice.

The **flags** argument specifies the link flags. The caller shall ensure that
the flags are valid regardless of the number of links that may be created.
For instance, setting the MEDIA_LNK_FL_ENABLED flag will cause all created
links to be enabled, which isn't valid if more than one link is created.

> **Note:**
>
> Any sink subdevice that calls this function must implement the
> .get_fwnode_pad media operation in order to verify endpoints passed
> to the sink are owned by the sink.

Return 0 on success or a negative error code on failure.

int v4l2_create_fwnode_links(struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*src_sd, struct [v4l2_subdev](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") \*sink_sd)
:   Create fwnode-based links from a source subdev to a sink subdev.

**Parameters**

`struct v4l2_subdev *src_sd`
:   pointer to a source subdevice

`struct v4l2_subdev *sink_sd`
:   pointer to a sink subdevice

**Description**

This function searches for any and all fwnode endpoint connections
between source and sink subdevices, and translates them into media
links. The function can be called by the sink subdevice, in its
v4l2-async notifier subdev bound callback, to create all links from
a bound source subdevice.

> **Note:**
>
> Any sink subdevice that calls this function must implement the
> .get_fwnode_pad media operation in order to verify endpoints passed
> to the sink are owned by the sink.

Return 0 on success or a negative error code on failure.

int v4l2_pipeline_pm_get(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Increase the use count of a pipeline

**Parameters**

`struct media_entity *entity`
:   The root entity of a pipeline

**Description**

THIS FUNCTION IS DEPRECATED. DO NOT USE IN NEW DRIVERS. USE RUNTIME PM
ON SUB-DEVICE DRIVERS INSTEAD.

Update the use count of all entities in the pipeline and power entities on.

This function is intended to be called in video node open. It uses
[`struct media_entity`](mc-core.md#c.media_entity "media_entity").use_count to track the power status. The use
of this function should be paired with [`v4l2_pipeline_link_notify()`](v4l2-mc.md#c.v4l2_pipeline_link_notify "v4l2_pipeline_link_notify").

Return 0 on success or a negative error code on failure.

void v4l2_pipeline_pm_put(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Decrease the use count of a pipeline

**Parameters**

`struct media_entity *entity`
:   The root entity of a pipeline

**Description**

THIS FUNCTION IS DEPRECATED. DO NOT USE IN NEW DRIVERS. USE RUNTIME PM
ON SUB-DEVICE DRIVERS INSTEAD.

Update the use count of all entities in the pipeline and power entities off.

This function is intended to be called in video node release. It uses
[`struct media_entity`](mc-core.md#c.media_entity "media_entity").use_count to track the power status. The use
of this function should be paired with [`v4l2_pipeline_link_notify()`](v4l2-mc.md#c.v4l2_pipeline_link_notify "v4l2_pipeline_link_notify").

int v4l2_pipeline_link_notify(struct [media_link](mc-core.md#c.media_link "media_link") \*link, u32 flags, unsigned int notification)
:   Link management notification callback

**Parameters**

`struct media_link *link`
:   The link

`u32 flags`
:   New link flags that will be applied

`unsigned int notification`
:   The link's state change notification type (MEDIA_DEV_NOTIFY_\*)

**Description**

React to link management on powered pipelines by updating the use count of
all entities in the source and sink sides of the link. Entities are powered
on or off accordingly. The use of this function should be paired
with v4l2_pipeline_pm_{get,put}().

Return 0 on success or a negative error code on failure. Powering entities
off is assumed to never fail. This function will not fail for disconnection
events.
