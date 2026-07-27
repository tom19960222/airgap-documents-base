---
collection: ceph
version: "19.2.2"
title: "Library architecture"
source_url: https://docs.ceph.com/en/squid/dev/libs/
fetched_at: 2026-07-27T16:41:23+00:00
---
# Library architecture

Ceph is structured into libraries which are built and then combined together to
make executables and other libraries.

- libcommon: a collection of utilities which are available to nearly every ceph
  library and executable. In general, libcommon should not contain global
  variables, because it is intended to be linked into libraries such as
  libcephfs.so.
- libglobal: a collection of utilities focused on the needs of Ceph daemon
  programs. In here you will find pidfile management functions, signal
  handlers, and so forth.

> **Todo:**
>
> document other libraries

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
