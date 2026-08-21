---
collection: kernel
version: "6.8"
title: "7.54. ioctl VIDIOC_STREAMON, VIDIOC_STREAMOFF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-streamon.html
fetched_at: 2026-08-21T03:41:06+00:00
---
# 7.54. ioctl VIDIOC_STREAMON, VIDIOC_STREAMOFF

## 7.54.1. Name

VIDIOC_STREAMON - VIDIOC_STREAMOFF - Start or stop streaming I/O

## 7.54.2. Synopsis

VIDIOC_STREAMON

`int ioctl(int fd, VIDIOC_STREAMON, const int *argp)`

VIDIOC_STREAMOFF

`int ioctl(int fd, VIDIOC_STREAMOFF, const int *argp)`

## 7.54.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to an integer.

## 7.54.4. Description

The `VIDIOC_STREAMON` and `VIDIOC_STREAMOFF` ioctl start and stop
the capture or output process during streaming
([memory mapping](mmap.md#mmap), [user pointer](userp.md#userp) or
[DMABUF](dmabuf.md#dmabuf)) I/O.

Capture hardware is disabled and no input buffers are filled (if there
are any empty buffers in the incoming queue) until `VIDIOC_STREAMON`
has been called. Output hardware is disabled and no video signal is
produced until `VIDIOC_STREAMON` has been called.

Memory-to-memory devices will not start until `VIDIOC_STREAMON` has
been called for both the capture and output stream types.

If `VIDIOC_STREAMON` fails then any already queued buffers will remain
queued.

The `VIDIOC_STREAMOFF` ioctl, apart of aborting or finishing any DMA
in progress, unlocks any user pointer buffers locked in physical memory,
and it removes all buffers from the incoming and outgoing queues. That
means all images captured but not dequeued yet will be lost, likewise
all images enqueued for output but not transmitted yet. I/O returns to
the same state as after calling
[ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) and can be restarted
accordingly.

If buffers have been queued with [ioctl VIDIOC_QBUF, VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) and
`VIDIOC_STREAMOFF` is called without ever having called
`VIDIOC_STREAMON`, then those queued buffers will also be removed from
the incoming queue and all are returned to the same state as after
calling [ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) and can be restarted
accordingly.

Both ioctls take a pointer to an integer, the desired buffer or stream
type. This is the same as struct
[`v4l2_requestbuffers`](vidioc-reqbufs.md#c.V4L.v4l2_requestbuffers "v4l2_requestbuffers") `type`.

If `VIDIOC_STREAMON` is called when streaming is already in progress,
or if `VIDIOC_STREAMOFF` is called when streaming is already stopped,
then 0 is returned. Nothing happens in the case of `VIDIOC_STREAMON`,
but `VIDIOC_STREAMOFF` will return queued buffers to their starting
state as mentioned above.

> **Note:**
>
> Applications can be preempted for unknown periods right before
> or after the `VIDIOC_STREAMON` or `VIDIOC_STREAMOFF` calls, there is
> no notion of starting or stopping "now". Buffer timestamps can be used
> to synchronize with other events.

## 7.54.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   The buffer `type` is not supported, or no buffers have been
    allocated (memory mapping) or enqueued (output) yet.

EPIPE
:   The driver implements
    [pad-level format configuration](dev-subdev.md#pad-level-formats) and the
    pipeline configuration is invalid.

ENOLINK
:   The driver implements Media Controller interface and the pipeline
    link configuration is invalid.
