---
collection: kernel
version: "6.8"
title: "6.1.2.7. FE_GET_EVENT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-get-event.html
fetched_at: 2026-08-21T03:39:25+00:00
---
# 6.1.2.7. FE_GET_EVENT

## 6.1.2.7.1. Name

FE_GET_EVENT

> **Attention:**
>
> This ioctl is deprecated.

## 6.1.2.7.2. Synopsis

FE_GET_EVENT

`int ioctl(int fd, FE_GET_EVENT, struct dvb_frontend_event *ev)`

## 6.1.2.7.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`ev`
:   Points to the location where the event, if any, is to be stored.

## 6.1.2.7.4. Description

This ioctl call returns a frontend event if available. If an event is
not available, the behavior depends on whether the device is in blocking
or non-blocking mode. In the latter case, the call fails immediately
with errno set to `EWOULDBLOCK`. In the former case, the call blocks until
an event becomes available.

## 6.1.2.7.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EWOULDBLOCK` | There is no event pending, and the device is in non-blocking mode. |
| `EOVERFLOW` | Overflow in event queue - one or more events were lost. |

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
