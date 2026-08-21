---
collection: kernel
version: "6.8"
title: "7.21. ioctl VIDIOC_EXPBUF"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/vidioc-expbuf.html
fetched_at: 2026-08-21T03:40:40+00:00
---
# 7.21. ioctl VIDIOC_EXPBUF

## 7.21.1. Name

VIDIOC_EXPBUF - Export a buffer as a DMABUF file descriptor.

## 7.21.2. Synopsis

VIDIOC_EXPBUF

`int ioctl(int fd, VIDIOC_EXPBUF, struct v4l2_exportbuffer *argp)`

## 7.21.3. Arguments

`fd`
:   File descriptor returned by [`open()`](func-open.md#c.V4L.open "open").

`argp`
:   Pointer to struct [`v4l2_exportbuffer`](vidioc-expbuf.md#c.V4L.v4l2_exportbuffer "v4l2_exportbuffer").

## 7.21.4. Description

This ioctl is an extension to the [memory mapping](mmap.md#mmap) I/O
method, therefore it is available only for `V4L2_MEMORY_MMAP` buffers.
It can be used to export a buffer as a DMABUF file at any time after
buffers have been allocated with the
[ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) ioctl.

To export a buffer, applications fill struct
[`v4l2_exportbuffer`](vidioc-expbuf.md#c.V4L.v4l2_exportbuffer "v4l2_exportbuffer"). The `type` field is
set to the same buffer type as was previously used with struct
[`v4l2_requestbuffers`](vidioc-reqbufs.md#c.V4L.v4l2_requestbuffers "v4l2_requestbuffers") `type`.
Applications must also set the `index` field. Valid index numbers
range from zero to the number of buffers allocated with
[ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) (struct
[`v4l2_requestbuffers`](vidioc-reqbufs.md#c.V4L.v4l2_requestbuffers "v4l2_requestbuffers") `count`) minus
one. For the multi-planar API, applications set the `plane` field to
the index of the plane to be exported. Valid planes range from zero to
the maximal number of valid planes for the currently active format. For
the single-planar API, applications must set `plane` to zero.
Additional flags may be posted in the `flags` field. Refer to a manual
for [`open()`](func-open.md#c.V4L.open "V4L.open") for details. Currently only O_CLOEXEC, O_RDONLY, O_WRONLY,
and O_RDWR are supported. All other fields must be set to zero. In the
case of multi-planar API, every plane is exported separately using
multiple [ioctl VIDIOC_EXPBUF](vidioc-expbuf.md#vidioc-expbuf) calls.

After calling [ioctl VIDIOC_EXPBUF](vidioc-expbuf.md#vidioc-expbuf) the `fd` field will be set by a
driver. This is a DMABUF file descriptor. The application may pass it to
other DMABUF-aware devices. Refer to [DMABUF importing](dmabuf.md#dmabuf)
for details about importing DMABUF files into V4L2 nodes. It is
recommended to close a DMABUF file when it is no longer used to allow
the associated memory to be reclaimed.

## 7.21.5. Examples

```c
int buffer_export(int v4lfd, enum v4l2_buf_type bt, int index, int *dmafd)
{
    struct v4l2_exportbuffer expbuf;

    memset(&expbuf, 0, sizeof(expbuf));
    expbuf.type = bt;
    expbuf.index = index;
    if (ioctl(v4lfd, VIDIOC_EXPBUF, &expbuf) == -1) {
        perror("VIDIOC_EXPBUF");
        return -1;
    }

    *dmafd = expbuf.fd;

    return 0;
}
```

```c
int buffer_export_mp(int v4lfd, enum v4l2_buf_type bt, int index,
    int dmafd[], int n_planes)
{
    int i;

    for (i = 0; i < n_planes; ++i) {
        struct v4l2_exportbuffer expbuf;

        memset(&expbuf, 0, sizeof(expbuf));
        expbuf.type = bt;
        expbuf.index = index;
        expbuf.plane = i;
        if (ioctl(v4lfd, VIDIOC_EXPBUF, &expbuf) == -1) {
            perror("VIDIOC_EXPBUF");
            while (i)
                close(dmafd[--i]);
            return -1;
        }
        dmafd[i] = expbuf.fd;
    }

    return 0;
}
```

type v4l2_exportbuffer

struct v4l2_exportbuffer

|  |  |  |
| --- | --- | --- |
| __u32 | `type` | Type of the buffer, same as struct [`v4l2_format`](vidioc-g-fmt.md#c.V4L.v4l2_format "v4l2_format") `type` or struct [`v4l2_requestbuffers`](vidioc-reqbufs.md#c.V4L.v4l2_requestbuffers "v4l2_requestbuffers") `type`, set by the application. See [`v4l2_buf_type`](buffer.md#c.V4L.v4l2_buf_type "v4l2_buf_type") |
| __u32 | `index` | Number of the buffer, set by the application. This field is only used for [memory mapping](mmap.md#mmap) I/O and can range from zero to the number of buffers allocated with the [ioctl VIDIOC_REQBUFS](vidioc-reqbufs.md#vidioc-reqbufs) and/or [ioctl VIDIOC_CREATE_BUFS](vidioc-create-bufs.md#vidioc-create-bufs) ioctls. |
| __u32 | `plane` | Index of the plane to be exported when using the multi-planar API. Otherwise this value must be set to zero. |
| __u32 | `flags` | Flags for the newly created file, currently only `O_CLOEXEC`, `O_RDONLY`, `O_WRONLY`, and `O_RDWR` are supported, refer to the manual of [`open()`](func-open.md#c.V4L.open "V4L.open") for more details. |
| __s32 | `fd` | The DMABUF file descriptor associated with a buffer. Set by the driver. |
| __u32 | `reserved[11]` | Reserved field for future use. Drivers and applications must set the array to zero. |

## 7.21.6. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

EINVAL
:   A queue is not in MMAP mode or DMABUF exporting is not supported or
    `flags` or `type` or `index` or `plane` fields are invalid.
