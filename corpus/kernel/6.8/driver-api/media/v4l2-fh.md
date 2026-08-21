---
collection: kernel
version: "6.8"
title: "2.6. V4L2 File handlers"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-fh.html
fetched_at: 2026-08-21T03:41:15+00:00
---
# 2.6. V4L2 File handlers

[`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") provides a way to easily keep file handle specific
data that is used by the V4L2 framework.

> **Attention:**
>
> New drivers must use [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")
> since it is also used to implement priority handling
> ([ioctl VIDIOC_G_PRIORITY, VIDIOC_S_PRIORITY](../../userspace-api/media/v4l/vidioc-g-priority.md#vidioc-g-priority)).

The users of [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") (in the V4L2 framework, not the driver) know
whether a driver uses [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") as its `file->private_data` pointer
by testing the `V4L2_FL_USES_V4L2_FH` bit in [`video_device`](v4l2-dev.md#c.video_device "video_device")->flags.
This bit is set whenever [`v4l2_fh_init()`](v4l2-fh.md#c.v4l2_fh_init "v4l2_fh_init") is called.

[`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") is allocated as a part of the driver's own file handle
structure and `file->private_data` is set to it in the driver's `open()`
function by the driver.

In many cases the [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") will be embedded in a larger
structure. In that case you should call:

1. [`v4l2_fh_init()`](v4l2-fh.md#c.v4l2_fh_init "v4l2_fh_init") and [`v4l2_fh_add()`](v4l2-fh.md#c.v4l2_fh_add "v4l2_fh_add") in `open()`
2. [`v4l2_fh_del()`](v4l2-fh.md#c.v4l2_fh_del "v4l2_fh_del") and [`v4l2_fh_exit()`](v4l2-fh.md#c.v4l2_fh_exit "v4l2_fh_exit") in `release()`

Drivers can extract their own file handle structure by using the container_of
macro.

Example:

```c
struct my_fh {
        int blah;
        struct v4l2_fh fh;
};

...

int my_open(struct file *file)
{
        struct my_fh *my_fh;
        struct video_device *vfd;
        int ret;

        ...

        my_fh = kzalloc(sizeof(*my_fh), GFP_KERNEL);

        ...

        v4l2_fh_init(&my_fh->fh, vfd);

        ...

        file->private_data = &my_fh->fh;
        v4l2_fh_add(&my_fh->fh);
        return 0;
}

int my_release(struct file *file)
{
        struct v4l2_fh *fh = file->private_data;
        struct my_fh *my_fh = container_of(fh, struct my_fh, fh);

        ...
        v4l2_fh_del(&my_fh->fh);
        v4l2_fh_exit(&my_fh->fh);
        kfree(my_fh);
        return 0;
}
```

Below is a short description of the [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") functions used:

[`v4l2_fh_init`](v4l2-fh.md#c.v4l2_fh_init "v4l2_fh_init")
([`fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"), [`vdev`](v4l2-dev.md#c.video_device "video_device"))

- Initialise the file handle. This **MUST** be performed in the driver's
  [`v4l2_file_operations`](v4l2-dev.md#c.v4l2_file_operations "v4l2_file_operations")->open() handler.

[`v4l2_fh_add`](v4l2-fh.md#c.v4l2_fh_add "v4l2_fh_add")
([`fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"))

- Add a [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") to [`video_device`](v4l2-dev.md#c.video_device "video_device") file handle list.
  Must be called once the file handle is completely initialized.

[`v4l2_fh_del`](v4l2-fh.md#c.v4l2_fh_del "v4l2_fh_del")
([`fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"))

- Unassociate the file handle from [`video_device`](v4l2-dev.md#c.video_device "video_device"). The file handle
  exit function may now be called.

[`v4l2_fh_exit`](v4l2-fh.md#c.v4l2_fh_exit "v4l2_fh_exit")
([`fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"))

- Uninitialise the file handle. After uninitialisation the [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")
  memory can be freed.

If [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") is not embedded, then you can use these helper functions:

[`v4l2_fh_open`](v4l2-fh.md#c.v4l2_fh_open "v4l2_fh_open")
(struct file \*filp)

- This allocates a [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"), initializes it and adds it to
  the [`struct video_device`](v4l2-dev.md#c.video_device "video_device") associated with the file struct.

[`v4l2_fh_release`](v4l2-fh.md#c.v4l2_fh_release "v4l2_fh_release")
(struct file \*filp)

- This deletes it from the [`struct video_device`](v4l2-dev.md#c.video_device "video_device") associated with the
  file struct, uninitialised the [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") and frees it.

These two functions can be plugged into the v4l2_file_operation's `open()`
and `release()` ops.

Several drivers need to do something when the first file handle is opened and
when the last file handle closes. Two helper functions were added to check
whether the [`v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh") struct is the only open filehandle of the
associated device node:

[`v4l2_fh_is_singular`](v4l2-fh.md#c.v4l2_fh_is_singular "v4l2_fh_is_singular")
([`fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh"))

- Returns 1 if the file handle is the only open file handle, else 0.

[`v4l2_fh_is_singular_file`](v4l2-fh.md#c.v4l2_fh_is_singular_file "v4l2_fh_is_singular_file")
(struct file \*filp)

- Same, but it calls v4l2_fh_is_singular with filp->private_data.

## 2.6.1. V4L2 fh functions and data structures

struct v4l2_fh
:   Describes a V4L2 file handler

**Definition**:

```
struct v4l2_fh {
    struct list_head        list;
    struct video_device     *vdev;
    struct v4l2_ctrl_handler *ctrl_handler;
    enum v4l2_priority      prio;
    wait_queue_head_t wait;
    struct mutex            subscribe_lock;
    struct list_head        subscribed;
    struct list_head        available;
    unsigned int            navailable;
    u32 sequence;
    struct v4l2_m2m_ctx     *m2m_ctx;
};
```

**Members**

`list`
:   list of file handlers

`vdev`
:   pointer to [`struct video_device`](v4l2-dev.md#c.video_device "video_device")

`ctrl_handler`
:   pointer to [`struct v4l2_ctrl_handler`](v4l2-controls.md#c.v4l2_ctrl_handler "v4l2_ctrl_handler")

`prio`
:   priority of the file handler, as defined by `enum v4l2_priority`

`wait`
:   event' s wait queue

`subscribe_lock`
:   serialise changes to the subscribed list; guarantee that
    the add and del event callbacks are orderly called

`subscribed`
:   list of subscribed events

`available`
:   list of events waiting to be dequeued

`navailable`
:   number of available events at **available** list

`sequence`
:   event sequence number

`m2m_ctx`
:   pointer to [`struct v4l2_m2m_ctx`](v4l2-mem2mem.md#c.v4l2_m2m_ctx "v4l2_m2m_ctx")

void v4l2_fh_init(struct [v4l2_fh](v4l2-fh.md#c.v4l2_fh "v4l2_fh") \*fh, struct [video_device](v4l2-dev.md#c.video_device "video_device") \*vdev)
:   Initialise the file handle.

**Parameters**

`struct v4l2_fh *fh`
:   pointer to [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")

`struct video_device *vdev`
:   pointer to [`struct video_device`](v4l2-dev.md#c.video_device "video_device")

**Description**

Parts of the V4L2 framework using the
file handles should be initialised in this function. Must be called
from driver's v4l2_file_operations->open() handler if the driver
uses [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh").

void v4l2_fh_add(struct [v4l2_fh](v4l2-fh.md#c.v4l2_fh "v4l2_fh") \*fh)
:   Add the fh to the list of file handles on a video_device.

**Parameters**

`struct v4l2_fh *fh`
:   pointer to [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")

**Description**

> **Note:**
>
> The **fh** file handle must be initialised first.

int v4l2_fh_open(struct file \*filp)
:   Ancillary routine that can be used as the open() op of v4l2_file_operations.

**Parameters**

`struct file *filp`
:   pointer to struct file

**Description**

It allocates a v4l2_fh and inits and adds it to the [`struct video_device`](v4l2-dev.md#c.video_device "video_device")
associated with the file pointer.

void v4l2_fh_del(struct [v4l2_fh](v4l2-fh.md#c.v4l2_fh "v4l2_fh") \*fh)
:   Remove file handle from the list of file handles.

**Parameters**

`struct v4l2_fh *fh`
:   pointer to [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")

**Description**

On error filp->private_data will be `NULL`, otherwise it will point to
the [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh").

> **Note:**
>
> Must be called in v4l2_file_operations->release() handler if the driver
> uses [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh").

void v4l2_fh_exit(struct [v4l2_fh](v4l2-fh.md#c.v4l2_fh "v4l2_fh") \*fh)
:   Release resources related to a file handle.

**Parameters**

`struct v4l2_fh *fh`
:   pointer to [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")

**Description**

Parts of the V4L2 framework using the v4l2_fh must release their
resources here, too.

> **Note:**
>
> Must be called in v4l2_file_operations->release() handler if the
> driver uses [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh").

int v4l2_fh_release(struct file \*filp)
:   Ancillary routine that can be used as the release() op of v4l2_file_operations.

**Parameters**

`struct file *filp`
:   pointer to struct file

**Description**

It deletes and exits the v4l2_fh associated with the file pointer and
frees it. It will do nothing if filp->private_data (the pointer to the
v4l2_fh struct) is `NULL`.

This function always returns 0.

int v4l2_fh_is_singular(struct [v4l2_fh](v4l2-fh.md#c.v4l2_fh "v4l2_fh") \*fh)
:   Returns 1 if this filehandle is the only filehandle opened for the associated video_device.

**Parameters**

`struct v4l2_fh *fh`
:   pointer to [`struct v4l2_fh`](v4l2-fh.md#c.v4l2_fh "v4l2_fh")

**Description**

If **fh** is NULL, then it returns 0.

int v4l2_fh_is_singular_file(struct file \*filp)
:   Returns 1 if this filehandle is the only filehandle opened for the associated video_device.

**Parameters**

`struct file *filp`
:   pointer to struct file

**Description**

This is a helper function variant of [`v4l2_fh_is_singular()`](v4l2-fh.md#c.v4l2_fh_is_singular "v4l2_fh_is_singular") with uses
struct file as argument.

If filp->private_data is `NULL`, then it will return 0.
