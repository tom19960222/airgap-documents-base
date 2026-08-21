---
collection: kernel
version: "6.8"
title: "mISDN Driver"
source_url: https://www.kernel.org/doc/html/v6.8/isdn/m_isdn.html
fetched_at: 2026-08-21T03:50:05+00:00
---
# mISDN Driver

mISDN is a new modular ISDN driver, in the long term it should replace
the old I4L driver architecture for passive ISDN cards.
It was designed to allow a broad range of applications and interfaces
but only have the basic function in kernel, the interface to the user
space is based on sockets with a own address family AF_ISDN.
