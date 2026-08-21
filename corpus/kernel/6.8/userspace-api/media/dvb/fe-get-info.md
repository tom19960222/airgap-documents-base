---
collection: kernel
version: "6.8"
title: "2.4.3. ioctl FE_GET_INFO"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-get-info.html
fetched_at: 2026-08-21T03:39:27+00:00
---
# 2.4.3. ioctl FE_GET_INFO

## 2.4.3.1. Name

FE_GET_INFO - Query Digital TV frontend capabilities and returns information
about the - front-end. This call only requires read-only access to the device.

## 2.4.3.2. Synopsis

FE_GET_INFO

`int ioctl(int fd, FE_GET_INFO, struct dvb_frontend_info *argp)`

## 2.4.3.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`argp`
:   pointer to struct [`dvb_frontend_info`](frontend-header.md#c.dvb_frontend_info "dvb_frontend_info")

## 2.4.3.4. Description

All Digital TV frontend devices support the [ioctl FE_GET_INFO](fe-get-info.md#fe-get-info) ioctl. It is
used to identify kernel devices compatible with this specification and to
obtain information about driver and hardware capabilities. The ioctl
takes a pointer to dvb_frontend_info which is filled by the driver.
When the driver is not compatible with this specification the ioctl
returns an error.

## 2.4.3.5. frontend capabilities

Capabilities describe what a frontend can do. Some capabilities are
supported only on some specific frontend types.

The frontend capabilities are described at [`fe_caps`](frontend-header.md#c.fe_caps "fe_caps").

## 2.4.3.6. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
