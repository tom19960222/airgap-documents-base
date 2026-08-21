---
collection: kernel
version: "6.8"
title: "3.3. Streaming I/O (User Pointers)"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/userp.html
fetched_at: 2026-08-21T03:57:28+00:00
---
# 3.3. Streaming I/O (User Pointers)

Input and output devices support this I/O method when the
`V4L2_CAP_STREAMING` flag in the `capabilities` field of struct
[`v4l2_capability`](vidioc-querycap.md#c.V4L.v4l2_capability "v4l2_capability") returned by the
[ioctl VIDIOC_QUERYCAP](vidioc-querycap.md#vidioc-querycap) ioctl is set. If the
particular user pointer method (not only memory mapping) is supported
must be determined by calling the [ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) ioctl
with the memory type set to `V4L2_MEMORY_USERPTR`.

This I/O method combines advantages of the read/write and memory mapping
methods. Buffers (planes) are allocated by the application itself, and
can reside for example in virtual or shared memory. Only pointers to
data are exchanged, these pointers and meta-information are passed in
struct [`v4l2_buffer`](buffer.md#c.V4L.v4l2_buffer "v4l2_buffer") (or in struct
[`v4l2_plane`](buffer.md#c.V4L.v4l2_plane "v4l2_plane") in the multi-planar API case). The
driver must be switched into user pointer I/O mode by calling the
[ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) with the desired buffer type.
No buffers (planes) are allocated beforehand, consequently they are not
indexed and cannot be queried like mapped buffers with the
[VIDIOC_QUERYBUF](vidioc-querybuf.md#vidioc-querybuf) ioctl.

## 3.3.1. Example: Initiating streaming I/O with user pointers

```c
struct v4l2_requestbuffers reqbuf;

memset (&reqbuf, 0, sizeof (reqbuf));
reqbuf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
reqbuf.memory = V4L2_MEMORY_USERPTR;

if (ioctl (fd, VIDIOC_REQBUFS, &reqbuf) == -1) {
    if (errno == EINVAL)
        printf ("Video capturing or user pointer streaming is not supported\\n");
    else
        perror ("VIDIOC_REQBUFS");

    exit (EXIT_FAILURE);
}
```

Buffer (plane) addresses and sizes are passed on the fly with the
[VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl. Although buffers are commonly
cycled, applications can pass different addresses and sizes at each
[VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf) call. If required by the hardware the
driver swaps memory pages within physical memory to create a continuous
area of memory. This happens transparently to the application in the
virtual memory subsystem of the kernel. When buffer pages have been
swapped out to disk they are brought back and finally locked in physical
memory for DMA. [1](userp.md#f1)

Filled or displayed buffers are dequeued with the
[VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl. The driver can unlock the
memory pages at any time between the completion of the DMA and this
ioctl. The memory is also unlocked when
[VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) is called,
[ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs), or when the device is closed.
Applications must take care not to free buffers without dequeuing.
Firstly, the buffers remain locked for longer, wasting physical memory.
Secondly the driver will not be notified when the memory is returned to
the application's free list and subsequently reused for other purposes,
possibly completing the requested DMA and overwriting valuable data.

For capturing applications it is customary to enqueue a number of empty
buffers, to start capturing and enter the read loop. Here the
application waits until a filled buffer can be dequeued, and re-enqueues
the buffer when the data is no longer needed. Output applications fill
and enqueue buffers, when enough buffers are stacked up output is
started. In the write loop, when the application runs out of free
buffers it must wait until an empty buffer can be dequeued and reused.
Two methods exist to suspend execution of the application until one or
more buffers can be dequeued. By default [VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) blocks when no buffer is in the outgoing queue. When the
`O_NONBLOCK` flag was given to the [`open()`](func-open.md#c.V4L.open "open") function,
[VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) returns immediately with an `EAGAIN`
error code when no buffer is available. The [select()](func-select.md#func-select) or [`poll()`](func-poll.md#c.V4L.poll "poll") function are always
available.

To start and stop capturing or output applications call the
[VIDIOC_STREAMON](vidioc-streamon.md#vidioc-streamon) and
[VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) ioctl.

> **Note:**
>
> [VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) removes all buffers from
> both queues and unlocks all buffers as a side effect. Since there is no
> notion of doing anything "now" on a multitasking system, if an
> application needs to synchronize with another event it should examine
> the struct [`v4l2_buffer`](buffer.md#c.V4L.v4l2_buffer "v4l2_buffer") `timestamp` of captured or
> outputted buffers.

Drivers implementing user pointer I/O must support the
[VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs), [VIDIOC_QBUF](vidioc-qbuf.md#vidioc-qbuf),
[VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf), [VIDIOC_STREAMON](vidioc-streamon.md#vidioc-streamon)
and [VIDIOC_STREAMOFF](vidioc-streamon.md#vidioc-streamon) ioctls, the
[`select()`](func-select.md#c.V4L.select "select") and [`poll()`](func-poll.md#c.V4L.poll "poll") function. [2](userp.md#f2)

[1](userp.md#id1)
:   We expect that frequently used buffers are typically not swapped out.
    Anyway, the process of swapping, locking or generating scatter-gather
    lists may be time consuming. The delay can be masked by the depth of
    the incoming buffer queue, and perhaps by maintaining caches assuming
    a buffer will be soon enqueued again. On the other hand, to optimize
    memory usage drivers can limit the number of buffers locked in
    advance and recycle the most recently used buffers first. Of course,
    the pages of empty buffers in the incoming queue need not be saved to
    disk. Output buffers must be saved on the incoming and outgoing queue
    because an application may share them with other processes.

[2](userp.md#id2)
:   At the driver level [`select()`](func-select.md#c.V4L.select "select") and [`poll()`](func-poll.md#c.V4L.poll "poll") are
    the same, and [`select()`](func-select.md#c.V4L.select "select") is too important to be optional.
    The rest should be evident.
