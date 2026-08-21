---
collection: kernel
version: "6.8"
title: "Documentation for /proc/sys/sunrpc/"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/sysctl/sunrpc.html
fetched_at: 2026-08-21T03:54:36+00:00
---
# Documentation for /proc/sys/sunrpc/

kernel version 2.2.10

Copyright (c) 1998, 1999, Rik van Riel <[riel@nl.linux.org](mailto:riel%40nl.linux.org)>

For general info and legal blurb, please look in [Documentation for /proc/sys](index.md).

---

This file contains the documentation for the sysctl files in
/proc/sys/sunrpc and is valid for Linux kernel version 2.2.

The files in this directory can be used to (re)set the debug
flags of the SUN Remote Procedure Call (RPC) subsystem in
the Linux kernel. This stuff is used for NFS, KNFSD and
maybe a few other things as well.

The files in there are used to control the debugging flags:
rpc_debug, nfs_debug, nfsd_debug and nlm_debug.

These flags are for kernel hackers only. You should read the
source code in net/sunrpc/ for more information.
