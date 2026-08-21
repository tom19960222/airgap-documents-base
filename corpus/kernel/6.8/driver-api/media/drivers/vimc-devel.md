---
collection: kernel
version: "6.8"
title: "9.1.12. The Virtual Media Controller Driver (vimc)"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/drivers/vimc-devel.html
fetched_at: 2026-08-21T03:41:23+00:00
---
# 9.1.12. The Virtual Media Controller Driver (vimc)

## 9.1.12.1. Source code documentation

### 9.1.12.1.1. vimc-streamer

struct vimc_stream
:   struct that represents a stream in the pipeline

**Definition**:

```
struct vimc_stream {
    struct media_pipeline pipe;
    struct vimc_ent_device *ved_pipeline[VIMC_STREAMER_PIPELINE_MAX_SIZE];
    unsigned int pipe_size;
    struct task_struct *kthread;
};
```

**Members**

`pipe`
:   the media pipeline object associated with this stream

`ved_pipeline`
:   array containing all the entities participating in the
    stream. The order is from a video device (usually a
    capture device) where stream_on was called, to the
    entity generating the first base image to be
    processed in the pipeline.

`pipe_size`
:   size of **ved_pipeline**

`kthread`
:   thread that generates the frames of the stream.

**Description**

When the user call stream_on in a video device, [`struct vimc_stream`](vimc-devel.md#c.vimc_stream "vimc_stream") is
used to keep track of all entities and subdevices that generates and
process frames for the stream.

struct [media_entity](../mc-core.md#c.media_entity "media_entity") \*vimc_get_source_entity(struct [media_entity](../mc-core.md#c.media_entity "media_entity") \*ent)
:   get the entity connected with the first sink pad

**Parameters**

`struct media_entity *ent`
:   reference media_entity

**Description**

Helper function that returns the media entity containing the source pad
linked with the first sink pad from the given media entity pad list.

**Return**

The source pad or NULL, if it wasn't found.

void vimc_streamer_pipeline_terminate(struct [vimc_stream](vimc-devel.md#c.vimc_stream "vimc_stream") \*stream)
:   Disable stream in all ved in stream

**Parameters**

`struct vimc_stream *stream`
:   the pointer to the stream structure with the pipeline to be
    disabled.

**Description**

Calls s_stream to disable the stream in each entity of the pipeline

int vimc_streamer_pipeline_init(struct [vimc_stream](vimc-devel.md#c.vimc_stream "vimc_stream") \*stream, struct vimc_ent_device \*ved)
:   Initializes the stream structure

**Parameters**

`struct vimc_stream *stream`
:   the pointer to the stream structure to be initialized

`struct vimc_ent_device *ved`
:   the pointer to the vimc entity initializing the stream

**Description**

Initializes the stream structure. Walks through the entity graph to
construct the pipeline used later on the streamer thread.
Calls [`vimc_streamer_s_stream()`](vimc-devel.md#c.vimc_streamer_s_stream "vimc_streamer_s_stream") to enable stream in all entities of
the pipeline.

**Return**

0 if success, error code otherwise.

int vimc_streamer_thread(void \*data)
:   Process frames through the pipeline

**Parameters**

`void *data`
:   vimc_stream struct of the current stream

**Description**

From the source to the sink, gets a frame from each subdevice and send to
the next one of the pipeline at a fixed framerate.

**Return**

Always zero (created as `int` instead of `void` to comply with
kthread API).

int vimc_streamer_s_stream(struct [vimc_stream](vimc-devel.md#c.vimc_stream "vimc_stream") \*stream, struct vimc_ent_device \*ved, int enable)
:   Start/stop the streaming on the media pipeline

**Parameters**

`struct vimc_stream *stream`
:   the pointer to the stream structure of the current stream

`struct vimc_ent_device *ved`
:   pointer to the vimc entity of the entity of the stream

`int enable`
:   flag to determine if stream should start/stop

**Description**

When starting, check if there is no `stream->kthread` allocated. This
should indicate that a stream is already running. Then, it initializes the
pipeline, creates and runs a kthread to consume buffers through the pipeline.
When stopping, analogously check if there is a stream running, stop the
thread and terminates the pipeline.

**Return**

0 if success, error code otherwise.
