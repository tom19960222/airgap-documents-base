---
collection: kernel
version: "6.8"
title: "2.21. V4L2 Memory to Memory functions and data structures"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-mem2mem.html
fetched_at: 2026-08-21T03:41:17+00:00
---
# 2.21. V4L2 Memory to Memory functions and data structures

struct v4l2_m2m_ops
:   mem-to-mem device driver callbacks

**Definition**:

```
struct v4l2_m2m_ops {
    void (*device_run)(void *priv);
    int (*job_ready)(void *priv);
    void (*job_abort)(void *priv);
};
```

**Members**

`device_run`
:   required. Begin the actual job (transaction) inside this
    callback.
    The job does NOT have to end before this callback returns
    (and it will be the usual case). When the job finishes,
    [`v4l2_m2m_job_finish()`](v4l2-mem2mem.md#c.v4l2_m2m_job_finish "v4l2_m2m_job_finish") or [`v4l2_m2m_buf_done_and_job_finish()`](v4l2-mem2mem.md#c.v4l2_m2m_buf_done_and_job_finish "v4l2_m2m_buf_done_and_job_finish")
    has to be called.

`job_ready`
:   optional. Should return 0 if the driver does not have a job
    fully prepared to run yet (i.e. it will not be able to finish a
    transaction without sleeping). If not provided, it will be
    assumed that one source and one destination buffer are all
    that is required for the driver to perform one full transaction.
    This method may not sleep.

`job_abort`
:   optional. Informs the driver that it has to abort the currently
    running transaction as soon as possible (i.e. as soon as it can
    stop the device safely; e.g. in the next interrupt handler),
    even if the transaction would not have been finished by then.
    After the driver performs the necessary steps, it has to call
    [`v4l2_m2m_job_finish()`](v4l2-mem2mem.md#c.v4l2_m2m_job_finish "v4l2_m2m_job_finish") or [`v4l2_m2m_buf_done_and_job_finish()`](v4l2-mem2mem.md#c.v4l2_m2m_buf_done_and_job_finish "v4l2_m2m_buf_done_and_job_finish") as
    if the transaction ended normally.
    This function does not have to (and will usually not) wait
    until the device enters a state when it can be stopped.

struct v4l2_m2m_queue_ctx
:   represents a queue for buffers ready to be processed

**Definition**:

```
struct v4l2_m2m_queue_ctx {
    struct vb2_queue        q;
    struct list_head        rdy_queue;
    spinlock_t rdy_spinlock;
    u8 num_rdy;
    bool buffered;
};
```

**Members**

`q`
:   pointer to struct [`vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue")

`rdy_queue`
:   List of V4L2 mem-to-mem queues

`rdy_spinlock`
:   spin lock to protect the struct usage

`num_rdy`
:   number of buffers ready to be processed

`buffered`
:   is the queue buffered?

**Description**

Queue for buffers ready to be processed as soon as this
instance receives access to the device.

struct v4l2_m2m_ctx
:   Memory to memory context structure

**Definition**:

```
struct v4l2_m2m_ctx {
    struct mutex                    *q_lock;
    bool new_frame;
    bool is_draining;
    struct vb2_v4l2_buffer          *last_src_buf;
    bool next_buf_last;
    bool has_stopped;
    bool ignore_cap_streaming;
    struct v4l2_m2m_dev             *m2m_dev;
    struct v4l2_m2m_queue_ctx       cap_q_ctx;
    struct v4l2_m2m_queue_ctx       out_q_ctx;
    struct list_head                queue;
    unsigned long                   job_flags;
    wait_queue_head_t finished;
    void *priv;
};
```

**Members**

`q_lock`
:   struct `mutex` lock

`new_frame`
:   valid in the device_run callback: if true, then this
    starts a new frame; if false, then this is a new slice
    for an existing frame. This is always true unless
    V4L2_BUF_CAP_SUPPORTS_M2M_HOLD_CAPTURE_BUF is set, which
    indicates slicing support.

`is_draining`
:   indicates device is in draining phase

`last_src_buf`
:   indicate the last source buffer for draining

`next_buf_last`
:   next capture queud buffer will be tagged as last

`has_stopped`
:   indicate the device has been stopped

`ignore_cap_streaming`
:   If true, job_ready can be called even if the CAPTURE
    queue is not streaming. This allows firmware to
    analyze the bitstream header which arrives on the
    OUTPUT queue. The driver must implement the job_ready
    callback correctly to make sure that the requirements
    for actual decoding are met.

`m2m_dev`
:   opaque pointer to the internal data to handle M2M context

`cap_q_ctx`
:   Capture (output to memory) queue context

`out_q_ctx`
:   Output (input from memory) queue context

`queue`
:   List of memory to memory contexts

`job_flags`
:   Job queue flags, used internally by v4l2-mem2mem.c:
    `TRANS_QUEUED`, `TRANS_RUNNING` and `TRANS_ABORT`.

`finished`
:   Wait queue used to signalize when a job queue finished.

`priv`
:   Instance private data

**Description**

The memory to memory context is specific to a file handle, NOT to e.g.
a device.

struct v4l2_m2m_buffer
:   Memory to memory buffer

**Definition**:

```
struct v4l2_m2m_buffer {
    struct vb2_v4l2_buffer  vb;
    struct list_head        list;
};
```

**Members**

`vb`
:   pointer to struct [`vb2_v4l2_buffer`](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer")

`list`
:   list of m2m buffers

void \*v4l2_m2m_get_curr_priv(struct v4l2_m2m_dev \*m2m_dev)
:   return driver private data for the currently running instance or NULL if no instance is running

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*v4l2_m2m_get_vq(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, enum v4l2_buf_type type)
:   return vb2_queue for the given type

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`enum v4l2_buf_type type`
:   type of the V4L2 buffer, as defined by enum `v4l2_buf_type`

void v4l2_m2m_try_schedule(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   check whether an instance is ready to be added to the pending job queue and add it if so.

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

**Description**

There are three basic requirements an instance has to meet to be able to run:
1) at least one source buffer has to be queued,
2) at least one destination buffer has to be queued,
3) streaming has to be on.

If a queue is buffered (for example a decoder hardware ringbuffer that has
to be drained before doing streamoff), allow scheduling without v4l2 buffers
on that queue.

There may also be additional, custom requirements. In such case the driver
should supply a custom callback (job_ready in v4l2_m2m_ops) that should
return 1 if the instance is ready.
An example of the above could be an instance that requires more than one
src/dst buffer per transaction.

void v4l2_m2m_job_finish(struct v4l2_m2m_dev \*m2m_dev, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   inform the framework that a job has been finished and have it clean up

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

**Description**

Called by a driver to yield back the device after it has finished with it.
Should be called as soon as possible after reaching a state which allows
other instances to take control of the device.

This function has to be called only after [`v4l2_m2m_ops->device_run`](v4l2-mem2mem.md#c.v4l2_m2m_ops "v4l2_m2m_ops")
callback has been called on the driver. To prevent recursion, it should
not be called directly from the [`v4l2_m2m_ops->device_run`](v4l2-mem2mem.md#c.v4l2_m2m_ops "v4l2_m2m_ops") callback though.

void v4l2_m2m_buf_done_and_job_finish(struct v4l2_m2m_dev \*m2m_dev, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, enum [vb2_buffer_state](v4l2-videobuf2.md#c.vb2_buffer_state "vb2_buffer_state") state)
:   return source/destination buffers with state and inform the framework that a job has been finished and have it clean up

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`enum vb2_buffer_state state`
:   vb2 buffer state passed to v4l2_m2m_buf_done().

**Description**

Drivers that set V4L2_BUF_CAP_SUPPORTS_M2M_HOLD_CAPTURE_BUF must use this
function instead of job_finish() to take held buffers into account. It is
optional for other drivers.

This function removes the source buffer from the ready list and returns
it with the given state. The same is done for the destination buffer, unless
it is marked 'held'. In that case the buffer is kept on the ready list.

After that the job is finished (see job_finish()).

This allows for multiple output buffers to be used to fill in a single
capture buffer. This is typically used by stateless decoders where
multiple e.g. H.264 slices contribute to a single decoded frame.

void v4l2_m2m_clear_state(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   clear encoding/decoding state

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

void v4l2_m2m_mark_stopped(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   set current encoding/decoding state as stopped

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

bool v4l2_m2m_dst_buf_is_last(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return the current encoding/decoding session draining management state of next queued capture buffer

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

**Description**

This last capture buffer should be tagged with V4L2_BUF_FLAG_LAST to notify
the end of the capture session.

bool v4l2_m2m_has_stopped(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return the current encoding/decoding session stopped state

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

bool v4l2_m2m_is_last_draining_src_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   return the output buffer draining state in the current encoding/decoding session

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_v4l2_buffer *vbuf`
:   pointer to struct `v4l2_buffer`

**Description**

This will identify the last output buffer queued before a session stop
was required, leading to an actual encoding/decoding session stop state
in the encoding/decoding process after being processed.

void v4l2_m2m_last_buffer_done(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   marks the buffer with LAST flag and DONE

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_v4l2_buffer *vbuf`
:   pointer to struct `v4l2_buffer`

void v4l2_m2m_suspend(struct v4l2_m2m_dev \*m2m_dev)
:   stop new jobs from being run and wait for current job to finish

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

**Description**

Called by a driver in the suspend hook. Stop new jobs from being run, and
wait for current running job to finish.

void v4l2_m2m_resume(struct v4l2_m2m_dev \*m2m_dev)
:   resume job running and try to run a queued job

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

**Description**

Called by a driver in the resume hook. This reverts the operation of
[`v4l2_m2m_suspend()`](v4l2-mem2mem.md#c.v4l2_m2m_suspend "v4l2_m2m_suspend") and allows job to be run. Also try to run a queued job if
there is any.

int v4l2_m2m_reqbufs(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_reqbufs "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_requestbuffers \*reqbufs)
:   multi-queue-aware REQBUFS multiplexer

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_requestbuffers *reqbufs`
:   pointer to struct `v4l2_requestbuffers`

int v4l2_m2m_querybuf(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_querybuf "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_buffer \*buf)
:   multi-queue-aware QUERYBUF multiplexer

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_buffer *buf`
:   pointer to struct `v4l2_buffer`

**Description**

See [`v4l2_m2m_mmap()`](v4l2-mem2mem.md#c.v4l2_m2m_mmap "v4l2_m2m_mmap") documentation for details.

int v4l2_m2m_qbuf(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_qbuf "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_buffer \*buf)
:   enqueue a source or destination buffer, depending on the type

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_buffer *buf`
:   pointer to struct `v4l2_buffer`

int v4l2_m2m_dqbuf(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_dqbuf "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_buffer \*buf)
:   dequeue a source or destination buffer, depending on the type

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_buffer *buf`
:   pointer to struct `v4l2_buffer`

int v4l2_m2m_prepare_buf(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_prepare_buf "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_buffer \*buf)
:   prepare a source or destination buffer, depending on the type

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_buffer *buf`
:   pointer to struct `v4l2_buffer`

int v4l2_m2m_create_bufs(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_create_bufs "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_create_buffers \*create)
:   create a source or destination buffer, depending on the type

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_create_buffers *create`
:   pointer to struct `v4l2_create_buffers`

int v4l2_m2m_expbuf(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_expbuf "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_exportbuffer \*eb)
:   export a source or destination buffer, depending on the type

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_exportbuffer *eb`
:   pointer to struct `v4l2_exportbuffer`

int v4l2_m2m_streamon(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_streamon "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, enum v4l2_buf_type type)
:   turn on streaming for a video queue

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`enum v4l2_buf_type type`
:   type of the V4L2 buffer, as defined by enum `v4l2_buf_type`

int v4l2_m2m_streamoff(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_streamoff "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, enum v4l2_buf_type type)
:   turn off streaming for a video queue

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`enum v4l2_buf_type type`
:   type of the V4L2 buffer, as defined by enum `v4l2_buf_type`

void v4l2_m2m_update_start_streaming_state(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   update the encoding/decoding session state when a start of streaming of a video queue is requested

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_queue *q`
:   queue

void v4l2_m2m_update_stop_streaming_state(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   update the encoding/decoding session state when a stop of streaming of a video queue is requested

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_queue *q`
:   queue

int v4l2_m2m_encoder_cmd(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_encoder_cmd "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_encoder_cmd \*ec)
:   execute an encoder command

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_encoder_cmd *ec`
:   pointer to the encoder command

int v4l2_m2m_decoder_cmd(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_decoder_cmd "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct v4l2_decoder_cmd \*dc)
:   execute a decoder command

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct v4l2_decoder_cmd *dc`
:   pointer to the decoder command

__poll_t v4l2_m2m_poll(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_poll "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct poll_table_struct \*wait)
:   poll replacement, for destination buffers only

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct poll_table_struct *wait`
:   pointer to struct `poll_table_struct`

**Description**

Call from the driver's poll() function. Will poll both queues. If a buffer
is available to dequeue (with dqbuf) from the source queue, this will
indicate that a non-blocking write can be performed, while read will be
returned in case of the destination queue.

int v4l2_m2m_mmap(struct [file](v4l2-mem2mem.md#c.v4l2_m2m_mmap "file") \*file, struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct vm_area_struct \*vma)
:   source and destination queues-aware mmap multiplexer

**Parameters**

`struct file *file`
:   pointer to struct `file`

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vm_area_struct *vma`
:   pointer to struct `vm_area_struct`

**Description**

Call from driver's mmap() function. Will handle mmap() for both queues
seamlessly for the video buffer, which will receive normal per-queue offsets
and proper vb2 queue pointers. The differentiation is made outside
vb2 by adding a predefined offset to buffers from one of the queues
and subtracting it before passing it back to vb2. Only drivers (and
thus applications) receive modified offsets.

struct v4l2_m2m_dev \*v4l2_m2m_init(const struct [v4l2_m2m_ops](v4l2-mem2mem.md#c.v4l2_m2m_ops "v4l2_m2m_ops") \*m2m_ops)
:   initialize per-driver m2m data

**Parameters**

`const struct v4l2_m2m_ops *m2m_ops`
:   pointer to [`struct v4l2_m2m_ops`](v4l2-mem2mem.md#c.v4l2_m2m_ops "v4l2_m2m_ops")

**Description**

Usually called from driver's `probe()` function.

**Return**

returns an opaque pointer to the internal data to handle M2M context

void v4l2_m2m_release(struct v4l2_m2m_dev \*m2m_dev)
:   cleans up and frees a m2m_dev structure

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

**Description**

Usually called from driver's `remove()` function.

struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*v4l2_m2m_ctx_init(struct v4l2_m2m_dev \*m2m_dev, void \*drv_priv, int (\*queue_init)(void \*priv, struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*src_vq, struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*dst_vq))
:   allocate and initialize a m2m context

**Parameters**

`struct v4l2_m2m_dev *m2m_dev`
:   opaque pointer to the internal data to handle M2M context

`void *drv_priv`
:   driver's instance private data

`int (*queue_init)(void *priv, struct vb2_queue *src_vq, struct vb2_queue *dst_vq)`
:   a callback for queue type-specific initialization function
    to be used for initializing vb2_queues

**Description**

Usually called from driver's `open()` function.

void v4l2_m2m_ctx_release(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   release m2m context

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

**Description**

Usually called from driver's release() function.

void v4l2_m2m_buf_queue(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   add a buffer to the proper ready buffers list.

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_v4l2_buffer *vbuf`
:   pointer to struct [`vb2_v4l2_buffer`](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer")

**Description**

Call from vb2_queue_ops->ops->buf_queue, vb2_queue_ops callback.

unsigned int v4l2_m2m_num_src_bufs_ready(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return the number of source buffers ready for use

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

unsigned int v4l2_m2m_num_dst_bufs_ready(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return the number of destination buffers ready for use

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_next_buf(struct [v4l2_m2m_queue_ctx](v4l2-mem2mem.md#c.v4l2_m2m_queue_ctx "v4l2_m2m_queue_ctx") \*q_ctx)
:   return next buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_queue_ctx *q_ctx`
:   pointer to struct **v4l2_m2m_queue_ctx**

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_next_src_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return next source buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_next_dst_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return next destination buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_last_buf(struct [v4l2_m2m_queue_ctx](v4l2-mem2mem.md#c.v4l2_m2m_queue_ctx "v4l2_m2m_queue_ctx") \*q_ctx)
:   return last buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_queue_ctx *q_ctx`
:   pointer to struct **v4l2_m2m_queue_ctx**

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_last_src_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return last source buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_last_dst_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return last destination buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

v4l2_m2m_for_each_dst_buf

`v4l2_m2m_for_each_dst_buf (m2m_ctx, b)`

> iterate over a list of destination ready buffers

**Parameters**

`m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`b`
:   current buffer of type [`struct v4l2_m2m_buffer`](v4l2-mem2mem.md#c.v4l2_m2m_buffer "v4l2_m2m_buffer")

v4l2_m2m_for_each_src_buf

`v4l2_m2m_for_each_src_buf (m2m_ctx, b)`

> iterate over a list of source ready buffers

**Parameters**

`m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`b`
:   current buffer of type [`struct v4l2_m2m_buffer`](v4l2-mem2mem.md#c.v4l2_m2m_buffer "v4l2_m2m_buffer")

v4l2_m2m_for_each_dst_buf_safe

`v4l2_m2m_for_each_dst_buf_safe (m2m_ctx, b, n)`

> iterate over a list of destination ready buffers safely

**Parameters**

`m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`b`
:   current buffer of type [`struct v4l2_m2m_buffer`](v4l2-mem2mem.md#c.v4l2_m2m_buffer "v4l2_m2m_buffer")

`n`
:   used as temporary storage

v4l2_m2m_for_each_src_buf_safe

`v4l2_m2m_for_each_src_buf_safe (m2m_ctx, b, n)`

> iterate over a list of source ready buffers safely

**Parameters**

`m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`b`
:   current buffer of type [`struct v4l2_m2m_buffer`](v4l2-mem2mem.md#c.v4l2_m2m_buffer "v4l2_m2m_buffer")

`n`
:   used as temporary storage

struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*v4l2_m2m_get_src_vq(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return vb2_queue for source buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*v4l2_m2m_get_dst_vq(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   return vb2_queue for destination buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_buf_remove(struct [v4l2_m2m_queue_ctx](v4l2-mem2mem.md#c.v4l2_m2m_queue_ctx "v4l2_m2m_queue_ctx") \*q_ctx)
:   take off a buffer from the list of ready buffers and return it

**Parameters**

`struct v4l2_m2m_queue_ctx *q_ctx`
:   pointer to struct **v4l2_m2m_queue_ctx**

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_src_buf_remove(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   take off a source buffer from the list of ready buffers and return it

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*v4l2_m2m_dst_buf_remove(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx)
:   take off a destination buffer from the list of ready buffers and return it

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

void v4l2_m2m_buf_remove_by_buf(struct [v4l2_m2m_queue_ctx](v4l2-mem2mem.md#c.v4l2_m2m_queue_ctx "v4l2_m2m_queue_ctx") \*q_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   take off exact buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_queue_ctx *q_ctx`
:   pointer to struct **v4l2_m2m_queue_ctx**

`struct vb2_v4l2_buffer *vbuf`
:   the buffer to be removed

void v4l2_m2m_src_buf_remove_by_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   take off exact source buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_v4l2_buffer *vbuf`
:   the buffer to be removed

void v4l2_m2m_dst_buf_remove_by_buf(struct [v4l2_m2m_ctx](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx") \*m2m_ctx, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*vbuf)
:   take off exact destination buffer from the list of ready buffers

**Parameters**

`struct v4l2_m2m_ctx *m2m_ctx`
:   m2m context assigned to the instance given by struct [`v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

`struct vb2_v4l2_buffer *vbuf`
:   the buffer to be removed

void v4l2_m2m_buf_copy_metadata(const struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*out_vb, struct [vb2_v4l2_buffer](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer") \*cap_vb, bool copy_frame_flags)
:   copy buffer metadata from the output buffer to the capture buffer

**Parameters**

`const struct vb2_v4l2_buffer *out_vb`
:   the output buffer that is the source of the metadata.

`struct vb2_v4l2_buffer *cap_vb`
:   the capture buffer that will receive the metadata.

`bool copy_frame_flags`
:   copy the KEY/B/PFRAME flags as well.

**Description**

This helper function copies the timestamp, timecode (if the TIMECODE
buffer flag was set), field and the TIMECODE, KEYFRAME, BFRAME, PFRAME
and TSTAMP_SRC_MASK flags from **out_vb** to **cap_vb**.

If **copy_frame_flags** is false, then the KEYFRAME, BFRAME and PFRAME
flags are not copied. This is typically needed for encoders that
set this bits explicitly.
