---
collection: kernel
version: "6.8"
title: "5.9. ioctl MEDIA_IOC_REQUEST_ALLOC"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-ioc-request-alloc.html
fetched_at: 2026-08-21T03:39:57+00:00
---
# 5.9. ioctl MEDIA_IOC_REQUEST_ALLOC

## 5.9.1. Name

MEDIA_IOC_REQUEST_ALLOC - Allocate a request

## 5.9.2. Synopsis

MEDIA_IOC_REQUEST_ALLOC

`int ioctl(int fd, MEDIA_IOC_REQUEST_ALLOC, int *argp)`

## 5.9.3. Arguments

`fd`
:   File descriptor returned by [`open()`](media-func-open.md#c.MC.open "open").

`argp`
:   Pointer to an integer.

## 5.9.4. Description

If the media device supports [requests](request-api.md#media-request-api), then
this ioctl can be used to allocate a request. If it is not supported, then
`errno` is set to `ENOTTY`. A request is accessed through a file descriptor
that is returned in `*argp`.

If the request was successfully allocated, then the request file descriptor
can be passed to the [VIDIOC_QBUF](../v4l/vidioc-qbuf.md#vidioc-qbuf),
[VIDIOC_G_EXT_CTRLS](../v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls),
[VIDIOC_S_EXT_CTRLS](../v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) and
[VIDIOC_TRY_EXT_CTRLS](../v4l/vidioc-g-ext-ctrls.md#vidioc-g-ext-ctrls) ioctls.

In addition, the request can be queued by calling
[ioctl MEDIA_REQUEST_IOC_QUEUE](media-request-ioc-queue.md#media-request-ioc-queue) and re-initialized by calling
[ioctl MEDIA_REQUEST_IOC_REINIT](media-request-ioc-reinit.md#media-request-ioc-reinit).

Finally, the file descriptor can be [polled](request-func-poll.md#request-func-poll) to wait
for the request to complete.

The request will remain allocated until all the file descriptors associated
with it are closed by [`close()`](media-func-close.md#c.MC.close "close") and the driver no
longer uses the request internally. See also
[here](request-api.md#media-request-life-time) for more information.

## 5.9.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

ENOTTY
:   The driver has no support for requests.
