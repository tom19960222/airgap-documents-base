---
collection: kernel
version: "6.8"
title: "2.1. Querying frontend information"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/query-dvb-frontend-info.html
fetched_at: 2026-08-21T03:57:47+00:00
---
# 2.1. Querying frontend information

Usually, the first thing to do when the frontend is opened is to check
the frontend capabilities. This is done using
[ioctl FE_GET_INFO](fe-get-info.md#fe-get-info). This ioctl will enumerate the
Digital TV API version and other characteristics about the frontend, and can
be opened either in read only or read/write mode.
