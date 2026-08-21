---
collection: kernel
version: "6.8"
title: "5.14. ioctl MEDIA_REQUEST_IOC_REINIT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/media-request-ioc-reinit.html
fetched_at: 2026-08-21T03:39:59+00:00
---
# 5.14. ioctl MEDIA_REQUEST_IOC_REINIT

## 5.14.1. Name

MEDIA_REQUEST_IOC_REINIT - Re-initialize a request

## 5.14.2. Synopsis

MEDIA_REQUEST_IOC_REINIT

`int ioctl(int request_fd, MEDIA_REQUEST_IOC_REINIT)`

## 5.14.3. Arguments

`request_fd`
:   File descriptor returned by [ioctl MEDIA_IOC_REQUEST_ALLOC](media-ioc-request-alloc.md#media-ioc-request-alloc).

## 5.14.4. Description

If the media device supports [requests](request-api.md#media-request-api), then
this request ioctl can be used to re-initialize a previously allocated
request.

Re-initializing a request will clear any existing data from the request.
This avoids having to [`close()`](media-func-close.md#c.MC.close "close") a completed
request and allocate a new request. Instead the completed request can just
be re-initialized and it is ready to be used again.

A request can only be re-initialized if it either has not been queued
yet, or if it was queued and completed. Otherwise it will set `errno`
to `EBUSY`. No other error codes can be returned.

## 5.14.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately.

EBUSY
:   The request is queued but not yet completed.
