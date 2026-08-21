---
collection: kernel
version: "6.8"
title: "6.1.2.6. FE_GET_FRONTEND"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-get-frontend.html
fetched_at: 2026-08-21T03:39:26+00:00
---
# 6.1.2.6. FE_GET_FRONTEND

## 6.1.2.6.1. Name

FE_GET_FRONTEND

> **Attention:**
>
> This ioctl is deprecated.

## 6.1.2.6.2. Synopsis

FE_GET_FRONTEND

`int ioctl(int fd, FE_GET_FRONTEND, struct dvb_frontend_parameters *p)`

## 6.1.2.6.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`p`
:   Points to parameters for tuning operation.

## 6.1.2.6.4. Description

This ioctl call queries the currently effective frontend parameters. For
this command, read-only access to the device is sufficient.

## 6.1.2.6.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

|  |  |
| --- | --- |
| `EINVAL` | Maximum supported symbol rate reached. |

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
