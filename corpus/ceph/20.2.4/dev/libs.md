---
collection: ceph
version: "20.2.4"
title: "Library architecture"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/libs.rst
fetched_at: 2026-08-18T01:32:45Z
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

.. todo:: document other libraries
