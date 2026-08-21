---
collection: kernel
version: "6.8"
title: "2.16. V4L2 videobuf2 functions and data structures"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-videobuf2.html
fetched_at: 2026-08-21T03:41:21+00:00
---
# 2.16. V4L2 videobuf2 functions and data structures

enum vb2_memory
:   type of memory model used to make the buffers visible on userspace.

**Constants**

`VB2_MEMORY_UNKNOWN`
:   Buffer status is unknown or it is not used yet on
    userspace.

`VB2_MEMORY_MMAP`
:   The buffers are allocated by the Kernel and it is
    memory mapped via mmap() ioctl. This model is
    also used when the user is using the buffers via
    read() or write() system calls.

`VB2_MEMORY_USERPTR`
:   The buffers was allocated in userspace and it is
    memory mapped via mmap() ioctl.

`VB2_MEMORY_DMABUF`
:   The buffers are passed to userspace via DMA buffer.

struct vb2_mem_ops
:   memory handling/memory allocator operations.

**Definition**:

```
struct vb2_mem_ops {
    void *(*alloc)(struct vb2_buffer *vb,struct device *dev, unsigned long size);
    void (*put)(void *buf_priv);
    struct dma_buf *(*get_dmabuf)(struct vb2_buffer *vb,void *buf_priv, unsigned long flags);
    void *(*get_userptr)(struct vb2_buffer *vb,struct device *dev,unsigned long vaddr, unsigned long size);
    void (*put_userptr)(void *buf_priv);
    void (*prepare)(void *buf_priv);
    void (*finish)(void *buf_priv);
    void *(*attach_dmabuf)(struct vb2_buffer *vb,struct device *dev,struct dma_buf *dbuf, unsigned long size);
    void (*detach_dmabuf)(void *buf_priv);
    int (*map_dmabuf)(void *buf_priv);
    void (*unmap_dmabuf)(void *buf_priv);
    void *(*vaddr)(struct vb2_buffer *vb, void *buf_priv);
    void *(*cookie)(struct vb2_buffer *vb, void *buf_priv);
    unsigned int    (*num_users)(void *buf_priv);
    int (*mmap)(void *buf_priv, struct vm_area_struct *vma);
};
```

**Members**

`alloc`
:   allocate video memory and, optionally, allocator private data,
    return [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on failure or a pointer to allocator private,
    per-buffer data on success; the returned private structure
    will then be passed as **buf_priv** argument to other ops in this
    structure. The size argument to this function shall be
    *page aligned*.

`put`
:   inform the allocator that the buffer will no longer be used;
    usually will result in the allocator freeing the buffer (if
    no other users of this buffer are present); the **buf_priv**
    argument is the allocator private per-buffer structure
    previously returned from the alloc callback.

`get_dmabuf`
:   acquire userspace memory for a hardware operation; used for
    DMABUF memory types.

`get_userptr`
:   acquire userspace memory for a hardware operation; used for
    USERPTR memory types; vaddr is the address passed to the
    videobuf2 layer when queuing a video buffer of USERPTR type;
    should return an allocator private per-buffer structure
    associated with the buffer on success, [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on failure;
    the returned private structure will then be passed as **buf_priv**
    argument to other ops in this structure.

`put_userptr`
:   inform the allocator that a USERPTR buffer will no longer
    be used.

`prepare`
:   called every time the buffer is passed from userspace to the
    driver, useful for cache synchronisation, optional.

`finish`
:   called every time the buffer is passed back from the driver
    to the userspace, also optional.

`attach_dmabuf`
:   attach a shared [`struct dma_buf`](../dma-buf.md#c.dma_buf "dma_buf") for a hardware operation;
    used for DMABUF memory types; dev is the alloc device
    dbuf is the shared dma_buf; returns [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on failure;
    allocator private per-buffer structure on success;
    this needs to be used for further accesses to the buffer.

`detach_dmabuf`
:   inform the exporter of the buffer that the current DMABUF
    buffer is no longer used; the **buf_priv** argument is the
    allocator private per-buffer structure previously returned
    from the attach_dmabuf callback.

`map_dmabuf`
:   request for access to the dmabuf from allocator; the allocator
    of dmabuf is informed that this driver is going to use the
    dmabuf.

`unmap_dmabuf`
:   releases access control to the dmabuf - allocator is notified
    that this driver is done using the dmabuf for now.

`vaddr`
:   return a kernel virtual address to a given memory buffer
    associated with the passed private structure or NULL if no
    such mapping exists.

`cookie`
:   return allocator specific cookie for a given memory buffer
    associated with the passed private structure or NULL if not
    available.

`num_users`
:   return the current number of users of a memory buffer;
    return 1 if the videobuf2 layer (or actually the driver using
    it) is the only user.

`mmap`
:   setup a userspace mapping for a given memory buffer under
    the provided virtual memory region.

**Description**

Those operations are used by the videobuf2 core to implement the memory
handling/memory allocators for each type of supported streaming I/O method.

> **Note:**
>
> 1. Required ops for USERPTR types: get_userptr, put_userptr.
> 2. Required ops for MMAP types: alloc, put, num_users, mmap.
> 3. Required ops for read/write access types: alloc, put, num_users, vaddr.
> 4. Required ops for DMABUF types: attach_dmabuf, detach_dmabuf,
>    map_dmabuf, unmap_dmabuf.

struct vb2_plane
:   plane information.

**Definition**:

```
struct vb2_plane {
    void *mem_priv;
    struct dma_buf          *dbuf;
    unsigned int            dbuf_mapped;
    unsigned int            bytesused;
    unsigned int            length;
    unsigned int            min_length;
    union {
        unsigned int    offset;
        unsigned long   userptr;
        int fd;
    } m;
    unsigned int            data_offset;
};
```

**Members**

`mem_priv`
:   private data with this plane.

`dbuf`
:   dma_buf - shared buffer object.

`dbuf_mapped`
:   flag to show whether dbuf is mapped or not

`bytesused`
:   number of bytes occupied by data in the plane (payload).

`length`
:   size of this plane (NOT the payload) in bytes. The maximum
    valid size is MAX_UINT - PAGE_SIZE.

`min_length`
:   minimum required size of this plane (NOT the payload) in bytes.
    **length** is always greater or equal to **min_length**, and like
    **length**, it is limited to MAX_UINT - PAGE_SIZE.

`m`
:   Union with memtype-specific data.

`m.offset`
:   when memory in the associated [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") is
    `VB2_MEMORY_MMAP`, equals the offset from the start of
    the device memory for this plane (or is a "cookie" that
    should be passed to mmap() called on the video node).

`m.userptr`
:   when memory is `VB2_MEMORY_USERPTR`, a userspace pointer
    pointing to this plane.

`m.fd`
:   when memory is `VB2_MEMORY_DMABUF`, a userspace file
    descriptor associated with this plane.

`data_offset`
:   offset in the plane to the start of data; usually 0,
    unless there is a header in front of the data.

**Description**

Should contain enough information to be able to cover all the fields
of `struct v4l2_plane` at videodev2.h.

enum vb2_io_modes
:   queue access methods.

**Constants**

`VB2_MMAP`
:   driver supports MMAP with streaming API.

`VB2_USERPTR`
:   driver supports USERPTR with streaming API.

`VB2_READ`
:   driver supports read() style access.

`VB2_WRITE`
:   driver supports write() style access.

`VB2_DMABUF`
:   driver supports DMABUF with streaming API.

enum vb2_buffer_state
:   current video buffer state.

**Constants**

`VB2_BUF_STATE_DEQUEUED`
:   buffer under userspace control.

`VB2_BUF_STATE_IN_REQUEST`
:   buffer is queued in media request.

`VB2_BUF_STATE_PREPARING`
:   buffer is being prepared in videobuf2.

`VB2_BUF_STATE_QUEUED`
:   buffer queued in videobuf2, but not in driver.

`VB2_BUF_STATE_ACTIVE`
:   buffer queued in driver and possibly used
    in a hardware operation.

`VB2_BUF_STATE_DONE`
:   buffer returned from driver to videobuf2, but
    not yet dequeued to userspace.

`VB2_BUF_STATE_ERROR`
:   same as above, but the operation on the buffer
    has ended with an error, which will be reported
    to the userspace when it is dequeued.

struct vb2_buffer
:   represents a video buffer.

**Definition**:

```
struct vb2_buffer {
    struct vb2_queue        *vb2_queue;
    unsigned int            index;
    unsigned int            type;
    unsigned int            memory;
    unsigned int            num_planes;
    u64 timestamp;
    struct media_request    *request;
    struct media_request_object     req_obj;
};
```

**Members**

`vb2_queue`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with the queue to
    which this driver belongs.

`index`
:   id number of the buffer.

`type`
:   buffer type.

`memory`
:   the method, in which the actual data is passed.

`num_planes`
:   number of planes in the buffer
    on an internal driver queue.

`timestamp`
:   frame timestamp in ns.

`request`
:   the request this buffer is associated with.

`req_obj`
:   used to bind this buffer to a request. This
    request object has a refcount.

struct vb2_ops
:   driver-specific callbacks.

**Definition**:

```
struct vb2_ops {
    int (*queue_setup)(struct vb2_queue *q,unsigned int *num_buffers, unsigned int *num_planes, unsigned int sizes[], struct device *alloc_devs[]);
    void (*wait_prepare)(struct vb2_queue *q);
    void (*wait_finish)(struct vb2_queue *q);
    int (*buf_out_validate)(struct vb2_buffer *vb);
    int (*buf_init)(struct vb2_buffer *vb);
    int (*buf_prepare)(struct vb2_buffer *vb);
    void (*buf_finish)(struct vb2_buffer *vb);
    void (*buf_cleanup)(struct vb2_buffer *vb);
    int (*prepare_streaming)(struct vb2_queue *q);
    int (*start_streaming)(struct vb2_queue *q, unsigned int count);
    void (*stop_streaming)(struct vb2_queue *q);
    void (*unprepare_streaming)(struct vb2_queue *q);
    void (*buf_queue)(struct vb2_buffer *vb);
    void (*buf_request_complete)(struct vb2_buffer *vb);
};
```

**Members**

`queue_setup`
:   called from VIDIOC_REQBUFS() and VIDIOC_CREATE_BUFS()
    handlers before memory allocation. It can be called
    twice: if the original number of requested buffers
    could not be allocated, then it will be called a
    second time with the actually allocated number of
    buffers to verify if that is OK.
    The driver should return the required number of buffers
    in \*num_buffers, the required number of planes per
    buffer in \*num_planes, the size of each plane should be
    set in the sizes[] array and optional per-plane
    allocator specific device in the alloc_devs[] array.
    When called from VIDIOC_REQBUFS(), \*num_planes == 0,
    the driver has to use the currently configured format to
    determine the plane sizes and \*num_buffers is the total
    number of buffers that are being allocated. When called
    from VIDIOC_CREATE_BUFS(), \*num_planes != 0 and it
    describes the requested number of planes and sizes[]
    contains the requested plane sizes. In this case
    \*num_buffers are being allocated additionally to
    q->num_buffers. If either \*num_planes or the requested
    sizes are invalid callback must return `-EINVAL`.

`wait_prepare`
:   release any locks taken while calling vb2 functions;
    it is called before an ioctl needs to wait for a new
    buffer to arrive; required to avoid a deadlock in
    blocking access type.

`wait_finish`
:   reacquire all locks released in the previous callback;
    required to continue operation after sleeping while
    waiting for a new buffer to arrive.

`buf_out_validate`
:   called when the output buffer is prepared or queued
    to a request; drivers can use this to validate
    userspace-provided information; this is required only
    for OUTPUT queues.

`buf_init`
:   called once after allocating a buffer (in MMAP case)
    or after acquiring a new USERPTR buffer; drivers may
    perform additional buffer-related initialization;
    initialization failure (return != 0) will prevent
    queue setup from completing successfully; optional.

`buf_prepare`
:   called every time the buffer is queued from userspace
    and from the VIDIOC_PREPARE_BUF() ioctl; drivers may
    perform any initialization required before each
    hardware operation in this callback; drivers can
    access/modify the buffer here as it is still synced for
    the CPU; drivers that support VIDIOC_CREATE_BUFS() must
    also validate the buffer size; if an error is returned,
    the buffer will not be queued in driver; optional.

`buf_finish`
:   called before every dequeue of the buffer back to
    userspace; the buffer is synced for the CPU, so drivers
    can access/modify the buffer contents; drivers may
    perform any operations required before userspace
    accesses the buffer; optional. The buffer state can be
    one of the following: `DONE` and `ERROR` occur while
    streaming is in progress, and the `PREPARED` state occurs
    when the queue has been canceled and all pending
    buffers are being returned to their default `DEQUEUED`
    state. Typically you only have to do something if the
    state is `VB2_BUF_STATE_DONE`, since in all other cases
    the buffer contents will be ignored anyway.

`buf_cleanup`
:   called once before the buffer is freed; drivers may
    perform any additional cleanup; optional.

`prepare_streaming`
:   called once to prepare for 'streaming' state; this is
    where validation can be done to verify everything is
    okay and streaming resources can be claimed. It is
    called when the VIDIOC_STREAMON ioctl is called. The
    actual streaming starts when **start_streaming** is called.
    Optional.

`start_streaming`
:   called once to enter 'streaming' state; the driver may
    receive buffers with **buf_queue** callback
    before **start_streaming** is called; the driver gets the
    number of already queued buffers in count parameter;
    driver can return an error if hardware fails, in that
    case all buffers that have been already given by
    the **buf_queue** callback are to be returned by the driver
    by calling [`vb2_buffer_done()`](v4l2-videobuf2.md#c.vb2_buffer_done "vb2_buffer_done") with `VB2_BUF_STATE_QUEUED`.
    If you need a minimum number of buffers before you can
    start streaming, then set
    [`vb2_queue->min_queued_buffers`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue"). If that is non-zero
    then **start_streaming** won't be called until at least
    that many buffers have been queued up by userspace.

`stop_streaming`
:   called when 'streaming' state must be disabled; driver
    should stop any DMA transactions or wait until they
    finish and give back all buffers it got from `buf_queue`
    callback by calling [`vb2_buffer_done()`](v4l2-videobuf2.md#c.vb2_buffer_done "vb2_buffer_done") with either
    `VB2_BUF_STATE_DONE` or `VB2_BUF_STATE_ERROR`; may use
    [`vb2_wait_for_all_buffers()`](v4l2-videobuf2.md#c.vb2_wait_for_all_buffers "vb2_wait_for_all_buffers") function

`unprepare_streaming`
:   called as counterpart to **prepare_streaming**; any claimed
    streaming resources can be released here. It is
    called when the VIDIOC_STREAMOFF ioctls is called or
    when the streaming filehandle is closed. Optional.

`buf_queue`
:   passes buffer vb to the driver; driver may start
    hardware operation on this buffer; driver should give
    the buffer back by calling [`vb2_buffer_done()`](v4l2-videobuf2.md#c.vb2_buffer_done "vb2_buffer_done") function;
    it is always called after calling VIDIOC_STREAMON()
    ioctl; might be called before **start_streaming** callback
    if user pre-queued buffers before calling
    VIDIOC_STREAMON().

`buf_request_complete`
:   a buffer that was never queued to the driver but is
    associated with a queued request was canceled.
    The driver will have to mark associated objects in the
    request as completed; required if requests are
    supported.

**Description**

These operations are not called from interrupt context except where
mentioned specifically.

struct vb2_buf_ops
:   driver-specific callbacks.

**Definition**:

```
struct vb2_buf_ops {
    int (*verify_planes_array)(struct vb2_buffer *vb, const void *pb);
    void (*init_buffer)(struct vb2_buffer *vb);
    void (*fill_user_buffer)(struct vb2_buffer *vb, void *pb);
    int (*fill_vb2_buffer)(struct vb2_buffer *vb, struct vb2_plane *planes);
    void (*copy_timestamp)(struct vb2_buffer *vb, const void *pb);
};
```

**Members**

`verify_planes_array`
:   Verify that a given user space structure contains
    enough planes for the buffer. This is called
    for each dequeued buffer.

`init_buffer`
:   given a [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") initialize the extra data after
    [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").
    For V4L2 this is a [`struct vb2_v4l2_buffer`](v4l2-videobuf2.md#c.vb2_v4l2_buffer "vb2_v4l2_buffer").

`fill_user_buffer`
:   given a [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") fill in the userspace structure.
    For V4L2 this is a `struct v4l2_buffer`.

`fill_vb2_buffer`
:   given a userspace structure, fill in the [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").
    If the userspace structure is invalid, then this op
    will return an error.

`copy_timestamp`
:   copy the timestamp from a userspace structure to
    the [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

struct vb2_queue
:   a videobuf2 queue.

**Definition**:

```
struct vb2_queue {
    unsigned int                    type;
    unsigned int                    io_modes;
    struct device                   *dev;
    unsigned long                   dma_attrs;
    unsigned int                    bidirectional:1;
    unsigned int                    fileio_read_once:1;
    unsigned int                    fileio_write_immediately:1;
    unsigned int                    allow_zero_bytesused:1;
    unsigned int               quirk_poll_must_check_waiting_for_buffers:1;
    unsigned int                    supports_requests:1;
    unsigned int                    requires_requests:1;
    unsigned int                    uses_qbuf:1;
    unsigned int                    uses_requests:1;
    unsigned int                    allow_cache_hints:1;
    unsigned int                    non_coherent_mem:1;
    struct mutex                    *lock;
    void *owner;
    const struct vb2_ops            *ops;
    const struct vb2_mem_ops        *mem_ops;
    const struct vb2_buf_ops        *buf_ops;
    void *drv_priv;
    u32 subsystem_flags;
    unsigned int                    buf_struct_size;
    u32 timestamp_flags;
    gfp_t gfp_flags;
    u32 min_queued_buffers;
    struct device                   *alloc_devs[VB2_MAX_PLANES];
};
```

**Members**

`type`
:   private buffer type whose content is defined by the vb2-core
    caller. For example, for V4L2, it should match
    the types defined on `enum v4l2_buf_type`.

`io_modes`
:   supported io methods (see [`enum vb2_io_modes`](v4l2-videobuf2.md#c.vb2_io_modes "vb2_io_modes")).

`dev`
:   device to use for the default allocation context if the driver
    doesn't fill in the **alloc_devs** array.

`dma_attrs`
:   DMA attributes to use for the DMA.

`bidirectional`
:   when this flag is set the DMA direction for the buffers of
    this queue will be overridden with `DMA_BIDIRECTIONAL` direction.
    This is useful in cases where the hardware (firmware) writes to
    a buffer which is mapped as read (`DMA_TO_DEVICE`), or reads from
    buffer which is mapped for write (`DMA_FROM_DEVICE`) in order
    to satisfy some internal hardware restrictions or adds a padding
    needed by the processing algorithm. In case the DMA mapping is
    not bidirectional but the hardware (firmware) trying to access
    the buffer (in the opposite direction) this could lead to an
    IOMMU protection faults.

`fileio_read_once`
:   report EOF after reading the first buffer

`fileio_write_immediately`
:   queue buffer after each write() call

`allow_zero_bytesused`
:   allow bytesused == 0 to be passed to the driver

`quirk_poll_must_check_waiting_for_buffers`
:   Return `EPOLLERR` at poll when QBUF
    has not been called. This is a vb1 idiom that has been adopted
    also by vb2.

`supports_requests`
:   this queue supports the Request API.

`requires_requests`
:   this queue requires the Request API. If this is set to 1,
    then supports_requests must be set to 1 as well.

`uses_qbuf`
:   qbuf was used directly for this queue. Set to 1 the first
    time this is called. Set to 0 when the queue is canceled.
    If this is 1, then you cannot queue buffers from a request.

`uses_requests`
:   requests are used for this queue. Set to 1 the first time
    a request is queued. Set to 0 when the queue is canceled.
    If this is 1, then you cannot queue buffers directly.

`allow_cache_hints`
:   when set user-space can pass cache management hints in
    order to skip cache flush/invalidation on ->prepare() or/and
    ->finish().

`non_coherent_mem`
:   when set queue will attempt to allocate buffers using
    non-coherent memory.

`lock`
:   pointer to a mutex that protects the [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue"). The
    driver can set this to a mutex to let the v4l2 core serialize
    the queuing ioctls. If the driver wants to handle locking
    itself, then this should be set to NULL. This lock is not used
    by the videobuf2 core API.

`owner`
:   The filehandle that 'owns' the buffers, i.e. the filehandle
    that called reqbufs, create_buffers or started fileio.
    This field is not used by the videobuf2 core API, but it allows
    drivers to easily associate an owner filehandle with the queue.

`ops`
:   driver-specific callbacks

`mem_ops`
:   memory allocator specific callbacks

`buf_ops`
:   callbacks to deliver buffer information.
    between user-space and kernel-space.

`drv_priv`
:   driver private data.

`subsystem_flags`
:   Flags specific to the subsystem (V4L2/DVB/etc.). Not used
    by the vb2 core.

`buf_struct_size`
:   size of the driver-specific buffer structure;
    "0" indicates the driver doesn't want to use a custom buffer
    structure type. In that case a subsystem-specific struct
    will be used (in the case of V4L2 that is
    `sizeof(struct vb2_v4l2_buffer)`). The first field of the
    driver-specific buffer structure must be the subsystem-specific
    struct (vb2_v4l2_buffer in the case of V4L2).

`timestamp_flags`
:   Timestamp flags; `V4L2_BUF_FLAG_TIMESTAMP_*` and
    `V4L2_BUF_FLAG_TSTAMP_SRC_*`

`gfp_flags`
:   additional gfp flags used when allocating the buffers.
    Typically this is 0, but it may be e.g. `GFP_DMA` or `__GFP_DMA32`
    to force the buffer allocation to a specific memory zone.

`min_queued_buffers`
:   the minimum number of queued buffers needed before
    **start_streaming** can be called. Used when a DMA engine
    cannot be started unless at least this number of buffers
    have been queued into the driver.
    VIDIOC_REQBUFS will ensure at least **min_queued_buffers**
    buffers will be allocated. Note that VIDIOC_CREATE_BUFS will not
    modify the requested buffer count.

`alloc_devs`
:   [`struct device`](../infrastructure.md#c.device "device") memory type/allocator-specific per-plane device

bool vb2_queue_allows_cache_hints(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   Return true if the queue allows cache and memory consistency hints.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue

void \*vb2_plane_vaddr(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane_no)
:   Return a kernel virtual address of a given plane.

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to which the plane in
    question belongs to.

`unsigned int plane_no`
:   plane number for which the address is to be returned.

**Description**

This function returns a kernel virtual address of a given plane if
such a mapping exist, NULL otherwise.

void \*vb2_plane_cookie(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane_no)
:   Return allocator specific cookie for the given plane.

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to which the plane in
    question belongs to.

`unsigned int plane_no`
:   plane number for which the cookie is to be returned.

**Description**

This function returns an allocator specific cookie for a given plane if
available, NULL otherwise. The allocator should provide some simple static
inline function, which would convert this cookie to the allocator specific
type that can be used directly by the driver to access the buffer. This can
be for example physical address, pointer to scatter list or IOMMU mapping.

void vb2_buffer_done(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, enum [vb2_buffer_state](v4l2-videobuf2.md#c.vb2_buffer_state "vb2_buffer_state") state)
:   inform videobuf2 that an operation on a buffer is finished.

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to be used.

`enum vb2_buffer_state state`
:   state of the buffer, as defined by [`enum vb2_buffer_state`](v4l2-videobuf2.md#c.vb2_buffer_state "vb2_buffer_state").
    Either `VB2_BUF_STATE_DONE` if the operation finished
    successfully, `VB2_BUF_STATE_ERROR` if the operation finished
    with an error or `VB2_BUF_STATE_QUEUED`.

**Description**

This function should be called by the driver after a hardware operation on
a buffer is finished and the buffer may be returned to userspace. The driver
cannot use this buffer anymore until it is queued back to it by videobuf
by the means of [`vb2_ops->buf_queue`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback. Only buffers previously queued
to the driver by [`vb2_ops->buf_queue`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") can be passed to this function.

While streaming a buffer can only be returned in state DONE or ERROR.
The [`vb2_ops->start_streaming`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") op can also return them in case the DMA engine
cannot be started for some reason. In that case the buffers should be
returned with state QUEUED to put them back into the queue.

void vb2_discard_done(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   discard all buffers marked as DONE.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This function is intended to be used with suspend/resume operations. It
discards all 'done' buffers as they would be too old to be requested after
resume.

Drivers must stop the hardware and synchronize with interrupt handlers and/or
delayed works before calling this function to make sure no buffer will be
touched by the driver and/or hardware.

int vb2_wait_for_all_buffers(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   wait until all buffers are given back to vb2.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This function will wait until all buffers that have been given to the driver
by [`vb2_ops->buf_queue`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") are given back to vb2 with [`vb2_buffer_done()`](v4l2-videobuf2.md#c.vb2_buffer_done "vb2_buffer_done"). It
doesn't call [`vb2_ops->wait_prepare`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops")/[`vb2_ops->wait_finish`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") pair.
It is intended to be called with all locks taken, for example from
[`vb2_ops->stop_streaming`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback.

void vb2_core_querybuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, void \*pb)
:   query video buffer information.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct vb2_buffer *vb`
:   pointer to struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`void *pb`
:   buffer struct passed from userspace.

**Description**

Videobuf2 core helper to implement VIDIOC_QUERYBUF() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

The passed buffer should have been verified.

This function fills the relevant information for the userspace.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_reqbufs(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, enum [vb2_memory](v4l2-videobuf2.md#c.vb2_memory "vb2_memory") memory, unsigned int flags, unsigned int \*count)
:   Initiate streaming.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`enum vb2_memory memory`
:   memory type, as defined by [`enum vb2_memory`](v4l2-videobuf2.md#c.vb2_memory "vb2_memory").

`unsigned int flags`
:   auxiliary queue/buffer management flags. Currently, the only
    used flag is `V4L2_MEMORY_FLAG_NON_COHERENT`.

`unsigned int *count`
:   requested buffer count.

**Description**

Videobuf2 core helper to implement VIDIOC_REQBUF() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

This function:

1. verifies streaming parameters passed from the userspace;
2. sets up the queue;
3. negotiates number of buffers and planes per buffer with the driver
   to be used during streaming;
4. allocates internal buffer structures ([`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer")), according to
   the agreed parameters;
5. for MMAP memory type, allocates actual video memory, using the
   memory handling/allocation routines provided during queue initialization.

If req->count is 0, all the memory will be freed instead.

If the queue has been allocated previously by a previous [`vb2_core_reqbufs()`](v4l2-videobuf2.md#c.vb2_core_reqbufs "vb2_core_reqbufs")
call and the queue is not busy, memory will be reallocated.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_create_bufs(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, enum [vb2_memory](v4l2-videobuf2.md#c.vb2_memory "vb2_memory") memory, unsigned int flags, unsigned int \*count, unsigned int requested_planes, const unsigned int requested_sizes[])
:   Allocate buffers and any required auxiliary structs

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`enum vb2_memory memory`
:   memory type, as defined by [`enum vb2_memory`](v4l2-videobuf2.md#c.vb2_memory "vb2_memory").

`unsigned int flags`
:   auxiliary queue/buffer management flags.

`unsigned int *count`
:   requested buffer count.

`unsigned int requested_planes`
:   number of planes requested.

`const unsigned int requested_sizes[]`
:   array with the size of the planes.

**Description**

Videobuf2 core helper to implement VIDIOC_CREATE_BUFS() operation. It is
called internally by VB2 by an API-specific handler, like
`videobuf2-v4l2.h`.

This function:

1. verifies parameter sanity;
2. calls the [`vb2_ops->queue_setup`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") queue operation;
3. performs any necessary memory allocations.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_prepare_buf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, void \*pb)
:   Pass ownership of a buffer from userspace to the kernel.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct vb2_buffer *vb`
:   pointer to struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`void *pb`
:   buffer structure passed from userspace to
    [`v4l2_ioctl_ops->vidioc_prepare_buf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

**Description**

Videobuf2 core helper to implement VIDIOC_PREPARE_BUF() operation. It is
called internally by VB2 by an API-specific handler, like
`videobuf2-v4l2.h`.

The passed buffer should have been verified.

This function calls vb2_ops->buf_prepare callback in the driver
(if provided), in which driver-specific buffer initialization can
be performed.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_qbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, void \*pb, struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Queue a buffer from userspace

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct vb2_buffer *vb`
:   pointer to struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`void *pb`
:   buffer structure passed from userspace to
    v4l2_ioctl_ops->vidioc_qbuf handler in driver

`struct media_request *req`
:   pointer to [`struct media_request`](mc-core.md#c.media_request "media_request"), may be NULL.

**Description**

Videobuf2 core helper to implement VIDIOC_QBUF() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

This function:

1. If **req** is non-NULL, then the buffer will be bound to this
   media request and it returns. The buffer will be prepared and
   queued to the driver (i.e. the next two steps) when the request
   itself is queued.
2. if necessary, calls [`vb2_ops->buf_prepare`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback in the driver
   (if provided), in which driver-specific buffer initialization can
   be performed;
3. if streaming is on, queues the buffer in driver by the means of
   [`vb2_ops->buf_queue`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback for processing.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_dqbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned int \*pindex, void \*pb, bool nonblocking)
:   Dequeue a buffer to the userspace

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue

`unsigned int *pindex`
:   pointer to the buffer index. May be NULL

`void *pb`
:   buffer structure passed from userspace to
    v4l2_ioctl_ops->vidioc_dqbuf handler in driver.

`bool nonblocking`
:   if true, this call will not sleep waiting for a buffer if no
    buffers ready for dequeuing are present. Normally the driver
    would be passing (file->f_flags & O_NONBLOCK) here.

**Description**

Videobuf2 core helper to implement VIDIOC_DQBUF() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

This function:

1. calls buf_finish callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync,
2. the buffer struct members are filled with relevant information for
   the userspace.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_streamon(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned int type)
:   Implements VB2 stream ON logic

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue

`unsigned int type`
:   type of the queue to be started.
    For V4L2, this is defined by `enum v4l2_buf_type` type.

**Description**

Videobuf2 core helper to implement VIDIOC_STREAMON() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_streamoff(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned int type)
:   Implements VB2 stream OFF logic

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue

`unsigned int type`
:   type of the queue to be started.
    For V4L2, this is defined by `enum v4l2_buf_type` type.

**Description**

Videobuf2 core helper to implement VIDIOC_STREAMOFF() operation. It is
called internally by VB2 by an API-specific handler, like
`videobuf2-v4l2.h`.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_expbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, int \*fd, unsigned int type, struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane, unsigned int flags)
:   Export a buffer as a file descriptor.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`int *fd`
:   pointer to the file descriptor associated with DMABUF
    (set by driver).

`unsigned int type`
:   buffer type.

`struct vb2_buffer *vb`
:   pointer to struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`unsigned int plane`
:   index of the plane to be exported, 0 for single plane queues

`unsigned int flags`
:   file flags for newly created file, as defined at
    include/uapi/asm-generic/fcntl.h.
    Currently, the only used flag is `O_CLOEXEC`.
    is supported, refer to manual of open syscall for more details.

**Description**

Videobuf2 core helper to implement VIDIOC_EXPBUF() operation. It is called
internally by VB2 by an API-specific handler, like `videobuf2-v4l2.h`.

**Return**

returns zero on success; an error code otherwise.

int vb2_core_queue_init(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   initialize a videobuf2 queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.
    This structure should be allocated in driver

**Description**

The [`vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") structure should be allocated by the driver. The driver is
responsible of clearing it's content and setting initial values for some
required entries before calling this function.

> **Note:**
>
> The following fields at **q** should be set before calling this function:
> [`vb2_queue->ops`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue"), [`vb2_queue->mem_ops`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue"), [`vb2_queue->type`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue").

void vb2_core_queue_release(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   stop streaming, release the queue and free memory

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") itself.

void vb2_queue_error(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   signal a fatal error on the queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

Flag that a fatal unrecoverable error has occurred and wake up all processes
waiting on the queue. Polling will now set `EPOLLERR` and queuing and dequeuing
buffers will return `-EIO`.

The error flag will be cleared when canceling the queue, either from
[`vb2_streamoff()`](v4l2-videobuf2.md#c.vb2_streamoff "vb2_streamoff") or [`vb2_queue_release()`](v4l2-videobuf2.md#c.vb2_queue_release "vb2_queue_release"). Drivers should thus not call this
function before starting the stream, otherwise the error flag will remain set
until the queue is released when closing the device node.

int vb2_mmap(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct vm_area_struct \*vma)
:   map video buffers into application address space.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct vm_area_struct *vma`
:   pointer to `struct vm_area_struct` with the vma passed
    to the mmap file operation handler in the driver.

**Description**

Should be called from mmap file operation handler of a driver.
This function maps one plane of one of the available video buffers to
userspace. To map whole video memory allocated on reqbufs, this function
has to be called once per each plane per each buffer previously allocated.

When the userspace application calls mmap, it passes to it an offset returned
to it earlier by the means of [`v4l2_ioctl_ops->vidioc_querybuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler.
That offset acts as a "cookie", which is then used to identify the plane
to be mapped.

This function finds a plane with a matching offset and a mapping is performed
by the means of a provided memory operation.

The return values from this function are intended to be directly returned
from the mmap handler in driver.

unsigned long vb2_get_unmapped_area(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned long addr, unsigned long len, unsigned long pgoff, unsigned long flags)
:   map video buffers into application address space.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`unsigned long addr`
:   memory address.

`unsigned long len`
:   buffer size.

`unsigned long pgoff`
:   page offset.

`unsigned long flags`
:   memory flags.

**Description**

This function is used in noMMU platforms to propose address mapping
for a given buffer. It's intended to be used as a handler for the
`file_operations->get_unmapped_area` operation.

This is called by the mmap() syscall routines will call this
to get a proposed address for the mapping, when `!CONFIG_MMU`.

__poll_t vb2_core_poll(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [file](v4l2-videobuf2.md#c.vb2_core_poll "file") \*file, poll_table \*wait)
:   implements poll syscall() logic.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct file *file`
:   `struct file` argument passed to the poll
    file operation handler.

`poll_table *wait`
:   `poll_table` wait argument passed to the poll
    file operation handler.

**Description**

This function implements poll file operation handler for a driver.
For CAPTURE queues, if a buffer is ready to be dequeued, the userspace will
be informed that the file descriptor of a video device is available for
reading.
For OUTPUT queues, if a buffer is ready to be dequeued, the file descriptor
will be reported as available for writing.

The return values from this function are intended to be directly returned
from poll handler in driver.

size_t vb2_read(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, char __user \*data, size_t count, loff_t \*ppos, int nonblock)
:   implements read() syscall logic.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`char __user *data`
:   pointed to target userspace buffer

`size_t count`
:   number of bytes to read

`loff_t *ppos`
:   file handle position tracking pointer

`int nonblock`
:   mode selector (1 means blocking calls, 0 means nonblocking)

size_t vb2_write(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, const char __user \*data, size_t count, loff_t \*ppos, int nonblock)
:   implements write() syscall logic.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`const char __user *data`
:   pointed to target userspace buffer

`size_t count`
:   number of bytes to write

`loff_t *ppos`
:   file handle position tracking pointer

`int nonblock`
:   mode selector (1 means blocking calls, 0 means nonblocking)

vb2_thread_fnc
:   **Typedef**: callback function for use with vb2_thread.

**Syntax**

> `int vb2_thread_fnc (struct vb2_buffer *vb, void *priv)`

**Parameters**

`struct vb2_buffer *vb`
:   pointer to struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`void *priv`
:   pointer to a private data.

**Description**

This is called whenever a buffer is dequeued in the thread.

int vb2_thread_start(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, [vb2_thread_fnc](v4l2-videobuf2.md#c.vb2_thread_fnc "vb2_thread_fnc") fnc, void \*priv, const char \*thread_name)
:   start a thread for the given queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`vb2_thread_fnc fnc`
:   [`vb2_thread_fnc`](v4l2-videobuf2.md#c.vb2_thread_fnc "vb2_thread_fnc") callback function.

`void *priv`
:   priv pointer passed to the callback function.

`const char *thread_name`
:   the name of the thread. This will be prefixed with "vb2-".

**Description**

This starts a thread that will queue and dequeue until an error occurs
or [`vb2_thread_stop()`](v4l2-videobuf2.md#c.vb2_thread_stop "vb2_thread_stop") is called.

> **Attention:**
>
> This function should not be used for anything else but the videobuf2-dvb
> support. If you think you have another good use-case for this, then please
> contact the linux-media mailing list first.

int vb2_thread_stop(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   stop the thread for the given queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

bool vb2_is_streaming(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   return streaming status of the queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

bool vb2_fileio_is_active(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   return true if fileio is active.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This returns true if read() or write() is used to stream the data
as opposed to stream I/O. This is almost never an important distinction,
except in rare cases. One such case is that using read() or write() to
stream a format using `V4L2_FIELD_ALTERNATE` is not allowed since there
is no way you can pass the field information of each buffer to/from
userspace. A driver that supports this field format should check for
this in the [`vb2_ops->queue_setup`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") op and reject it if this function returns
true.

unsigned int vb2_get_num_buffers(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   get the number of buffer in a queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

bool vb2_is_busy(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   return busy status of the queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This function checks if queue has any buffers allocated.

void \*vb2_get_drv_priv(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   return driver private data associated with the queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

void vb2_set_plane_payload(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane_no, unsigned long size)
:   set bytesused for the plane **plane_no**.

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to which the plane in
    question belongs to.

`unsigned int plane_no`
:   plane number for which payload should be set.

`unsigned long size`
:   payload in bytes.

unsigned long vb2_get_plane_payload(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane_no)
:   get bytesused for the plane plane_no

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to which the plane in
    question belongs to.

`unsigned int plane_no`
:   plane number for which payload should be set.

unsigned long vb2_plane_size(struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb, unsigned int plane_no)
:   return plane size in bytes.

**Parameters**

`struct vb2_buffer *vb`
:   pointer to [`struct vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") to which the plane in
    question belongs to.

`unsigned int plane_no`
:   plane number for which size should be returned.

bool vb2_start_streaming_called(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   return streaming status of driver.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

void vb2_clear_last_buffer_dequeued(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   clear last buffer dequeued flag of queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb2_get_buffer(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned int index)
:   get a buffer from a queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`unsigned int index`
:   buffer index

**Description**

This function obtains a buffer from a queue, by its index.
Keep in mind that there is no refcounting involved in this
operation, so the buffer lifetime should be taken into
consideration.

bool vb2_buffer_in_use(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb)
:   return true if the buffer is in use and the queue cannot be freed (by the means of VIDIOC_REQBUFS(0)) call.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct vb2_buffer *vb`
:   buffer for which plane size should be returned.

int vb2_verify_memory_type(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, enum [vb2_memory](v4l2-videobuf2.md#c.vb2_memory "vb2_memory") memory, unsigned int type)
:   Check whether the memory type and buffer type passed to a buffer operation are compatible with the queue.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`enum vb2_memory memory`
:   memory model, as defined by enum [`vb2_memory`](v4l2-videobuf2.md#c.vb2_memory "vb2_memory").

`unsigned int type`
:   private buffer type whose content is defined by the vb2-core
    caller. For example, for V4L2, it should match
    the types defined on enum `v4l2_buf_type`.

bool vb2_request_object_is_buffer(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   return true if the object is a buffer

**Parameters**

`struct media_request_object *obj`
:   the request object.

unsigned int vb2_request_buffer_cnt(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   return the number of buffers in the request

**Parameters**

`struct media_request *req`
:   the request.

struct vb2_v4l2_buffer
:   video buffer information for v4l2.

**Definition**:

```
struct vb2_v4l2_buffer {
    struct vb2_buffer       vb2_buf;
    __u32 flags;
    __u32 field;
    struct v4l2_timecode    timecode;
    __u32 sequence;
    __s32 request_fd;
    bool is_held;
    struct vb2_plane        planes[VB2_MAX_PLANES];
};
```

**Members**

`vb2_buf`
:   embedded struct [`vb2_buffer`](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer").

`flags`
:   buffer informational flags.

`field`
:   field order of the image in the buffer, as defined by
    [`enum v4l2_field`](../../userspace-api/media/v4l/field-order.md#c.v4l2_field "v4l2_field").

`timecode`
:   frame timecode.

`sequence`
:   sequence count of this frame.

`request_fd`
:   the request_fd associated with this buffer

`is_held`
:   if true, then this capture buffer was held

`planes`
:   plane information (userptr/fd, length, bytesused, data_offset).

**Description**

Should contain enough information to be able to cover all the fields
of `struct v4l2_buffer` at `videodev2.h`.

struct [vb2_buffer](v4l2-videobuf2.md#c.vb2_buffer "vb2_buffer") \*vb2_find_buffer(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, u64 timestamp)
:   Find a buffer with given timestamp

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`u64 timestamp`
:   the timestamp to find.

**Description**

Returns the buffer with the given **timestamp**, or NULL if not found.

int vb2_reqbufs(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct v4l2_requestbuffers \*req)
:   Wrapper for [`vb2_core_reqbufs()`](v4l2-videobuf2.md#c.vb2_core_reqbufs "vb2_core_reqbufs") that also verifies the memory and type values.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct v4l2_requestbuffers *req`
:   `struct v4l2_requestbuffers` passed from userspace to
    [`v4l2_ioctl_ops->vidioc_reqbufs`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

int vb2_create_bufs(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct v4l2_create_buffers \*create)
:   Wrapper for [`vb2_core_create_bufs()`](v4l2-videobuf2.md#c.vb2_core_create_bufs "vb2_core_create_bufs") that also verifies the memory and type values.

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct v4l2_create_buffers *create`
:   creation parameters, passed from userspace to
    [`v4l2_ioctl_ops->vidioc_create_bufs`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver

int vb2_prepare_buf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct v4l2_buffer \*b)
:   Pass ownership of a buffer from userspace to the kernel

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct media_device *mdev`
:   pointer to [`struct media_device`](mc-core.md#c.media_device "media_device"), may be NULL.

`struct v4l2_buffer *b`
:   buffer structure passed from userspace to
    [`v4l2_ioctl_ops->vidioc_prepare_buf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver

**Description**

Should be called from [`v4l2_ioctl_ops->vidioc_prepare_buf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") ioctl handler
of a driver.

This function:

1. verifies the passed buffer,
2. calls [`vb2_ops->buf_prepare`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback in the driver (if provided),
   in which driver-specific buffer initialization can be performed.
3. if **b->request_fd** is non-zero and **mdev->ops->req_queue** is set,
   then bind the prepared buffer to the request.

The return values from this function are intended to be directly returned
from [`v4l2_ioctl_ops->vidioc_prepare_buf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

int vb2_qbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct v4l2_buffer \*b)
:   Queue a buffer from userspace

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct media_device *mdev`
:   pointer to [`struct media_device`](mc-core.md#c.media_device "media_device"), may be NULL.

`struct v4l2_buffer *b`
:   buffer structure passed from userspace to
    [`v4l2_ioctl_ops->vidioc_qbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver

**Description**

Should be called from [`v4l2_ioctl_ops->vidioc_qbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler of a driver.

This function:

1. verifies the passed buffer;
2. if **b->request_fd** is non-zero and **mdev->ops->req_queue** is set,
   then bind the buffer to the request.
3. if necessary, calls [`vb2_ops->buf_prepare`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback in the driver
   (if provided), in which driver-specific buffer initialization can
   be performed;
4. if streaming is on, queues the buffer in driver by the means of
   [`vb2_ops->buf_queue`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback for processing.

The return values from this function are intended to be directly returned
from [`v4l2_ioctl_ops->vidioc_qbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

int vb2_expbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct v4l2_exportbuffer \*eb)
:   Export a buffer as a file descriptor

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct v4l2_exportbuffer *eb`
:   export buffer structure passed from userspace to
    [`v4l2_ioctl_ops->vidioc_expbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver

**Description**

The return values from this function are intended to be directly returned
from [`v4l2_ioctl_ops->vidioc_expbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

int vb2_dqbuf(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct v4l2_buffer \*b, bool nonblocking)
:   Dequeue a buffer to the userspace

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct v4l2_buffer *b`
:   buffer structure passed from userspace to
    [`v4l2_ioctl_ops->vidioc_dqbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver

`bool nonblocking`
:   if true, this call will not sleep waiting for a buffer if no
    buffers ready for dequeuing are present. Normally the driver
    would be passing (`file->f_flags` & `O_NONBLOCK`) here

**Description**

Should be called from [`v4l2_ioctl_ops->vidioc_dqbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") ioctl handler
of a driver.

This function:

1. verifies the passed buffer;
2. calls [`vb2_ops->buf_finish`](v4l2-videobuf2.md#c.vb2_ops "vb2_ops") callback in the driver (if provided), in which
   driver can perform any additional operations that may be required before
   returning the buffer to userspace, such as cache sync;
3. the buffer struct members are filled with relevant information for
   the userspace.

The return values from this function are intended to be directly returned
from [`v4l2_ioctl_ops->vidioc_dqbuf`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in driver.

int vb2_streamon(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, enum v4l2_buf_type type)
:   start streaming

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`enum v4l2_buf_type type`
:   type argument passed from userspace to vidioc_streamon handler,
    as defined by `enum v4l2_buf_type`.

**Description**

Should be called from [`v4l2_ioctl_ops->vidioc_streamon`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler of a driver.

This function:

1. verifies current state
2. passes any previously queued buffers to the driver and starts streaming

The return values from this function are intended to be directly returned
from [`v4l2_ioctl_ops->vidioc_streamon`](v4l2-common.md#c.v4l2_ioctl_ops "v4l2_ioctl_ops") handler in the driver.

int vb2_streamoff(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, enum v4l2_buf_type type)
:   stop streaming

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`enum v4l2_buf_type type`
:   type argument passed from userspace to vidioc_streamoff handler

**Description**

Should be called from vidioc_streamoff handler of a driver.

This function:

1. verifies current state,
2. stop streaming and dequeues any queued buffers, including those previously
   passed to the driver (after waiting for the driver to finish).

This call can be used for pausing playback.
The return values from this function are intended to be directly returned
from vidioc_streamoff handler in the driver

int vb2_queue_init(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   initialize a videobuf2 queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

The vb2_queue structure should be allocated by the driver. The driver is
responsible of clearing it's content and setting initial values for some
required entries before calling this function.
q->ops, q->mem_ops, q->type and q->io_modes are mandatory. Please refer
to the [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") description in include/media/videobuf2-core.h
for more information.

int vb2_queue_init_name(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, const char \*name)
:   initialize a videobuf2 queue with a name

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`const char *name`
:   the queue name

**Description**

This function initializes the vb2_queue exactly like [`vb2_queue_init()`](v4l2-videobuf2.md#c.vb2_queue_init "vb2_queue_init"),
and additionally sets the queue name. The queue name is used for logging
purpose, and should uniquely identify the queue within the context of the
device it belongs to. This is useful to attribute kernel log messages to the
right queue for m2m devices or other devices that handle multiple queues.

void vb2_queue_release(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q)
:   stop streaming, release the queue and free memory

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

**Description**

This function stops streaming and performs necessary clean ups, including
freeing video buffer memory. The driver is responsible for freeing
the vb2_queue structure itself.

int vb2_queue_change_type(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, unsigned int type)
:   change the type of an inactive vb2_queue

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`unsigned int type`
:   the type to change to (V4L2_BUF_TYPE_VIDEO_\*)

**Description**

This function changes the type of the vb2_queue. This is only possible
if the queue is not busy (i.e. no buffers have been allocated).

[`vb2_queue_change_type()`](v4l2-videobuf2.md#c.vb2_queue_change_type "vb2_queue_change_type") can be used to support multiple buffer types using
the same queue. The driver can implement v4l2_ioctl_ops.vidioc_reqbufs and
v4l2_ioctl_ops.vidioc_create_bufs functions and call [`vb2_queue_change_type()`](v4l2-videobuf2.md#c.vb2_queue_change_type "vb2_queue_change_type")
before calling vb2_ioctl_reqbufs() or vb2_ioctl_create_bufs(), and thus
"lock" the buffer type until the buffers have been released.

__poll_t vb2_poll(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [file](v4l2-videobuf2.md#c.vb2_poll "file") \*file, poll_table \*wait)
:   implements poll userspace operation

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct file *file`
:   file argument passed to the poll file operation handler

`poll_table *wait`
:   wait argument passed to the poll file operation handler

**Description**

This function implements poll file operation handler for a driver.
For CAPTURE queues, if a buffer is ready to be dequeued, the userspace will
be informed that the file descriptor of a video device is available for
reading.
For OUTPUT queues, if a buffer is ready to be dequeued, the file descriptor
will be reported as available for writing.

If the driver uses [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"), then [`vb2_poll()`](v4l2-videobuf2.md#c.vb2_poll "vb2_poll") will also check for any
pending events.

The return values from this function are intended to be directly returned
from poll handler in driver.

bool vb2_queue_is_busy(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*q, struct [file](v4l2-videobuf2.md#c.vb2_queue_is_busy "file") \*file)
:   check if the queue is busy

**Parameters**

`struct vb2_queue *q`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") with videobuf2 queue.

`struct file *file`
:   file through which the vb2 queue access is performed

**Description**

The queue is considered busy if it has an owner and the owner is not the
**file**.

Queue ownership is acquired and checked by some of the v4l2_ioctl_ops helpers
below. Drivers can also use this function directly when they need to
open-code ioctl handlers, for instance to add additional checks between the
queue ownership test and the call to the corresponding vb2 operation.

void vb2_video_unregister_device(struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev)
:   unregister the video device and release queue

**Parameters**

`struct video_device *vdev`
:   pointer to [`struct video_device`](v4l2-dev.md#c.video_device "video_device")

**Description**

If the driver uses vb2_fop_release()/_vb2_fop_release(), then it should use
[`vb2_video_unregister_device()`](v4l2-videobuf2.md#c.vb2_video_unregister_device "vb2_video_unregister_device") instead of [`video_unregister_device()`](v4l2-dev.md#c.video_unregister_device "video_unregister_device").

This function will call [`video_unregister_device()`](v4l2-dev.md#c.video_unregister_device "video_unregister_device") and then release the
vb2_queue if streaming is in progress. This will stop streaming and
this will simplify the unbind sequence since after this call all subdevs
will have stopped streaming as well.

void vb2_ops_wait_prepare(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*vq)
:   helper function to lock a struct [`vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue")

**Parameters**

`struct vb2_queue *vq`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue")

**Description**

..note:: only use if vq->lock is non-NULL.

void vb2_ops_wait_finish(struct [vb2_queue](v4l2-videobuf2.md#c.vb2_queue "vb2_queue") \*vq)
:   helper function to unlock a struct [`vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue")

**Parameters**

`struct vb2_queue *vq`
:   pointer to [`struct vb2_queue`](v4l2-videobuf2.md#c.vb2_queue "vb2_queue")

**Description**

..note:: only use if vq->lock is non-NULL.

struct vb2_vmarea_handler
:   common vma refcount tracking handler.

**Definition**:

```
struct vb2_vmarea_handler {
    refcount_t *refcount;
    void (*put)(void *arg);
    void *arg;
};
```

**Members**

`refcount`
:   pointer to `refcount_t` entry in the buffer.

`put`
:   callback to function that decreases buffer refcount.

`arg`
:   argument for **put** callback.
