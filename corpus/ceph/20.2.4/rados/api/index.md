---
collection: ceph
version: "20.2.4"
title: "Ceph Storage Cluster APIs"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/api/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _rados api:

# Ceph Storage Cluster APIs

The Ceph Storage Cluster has a messaging layer protocol that enables
clients to interact with a Ceph Monitor and a Ceph OSD Daemon.
`librados` provides this functionality to Ceph Client\s in the form of
a library.  All Ceph Clients either use `librados` or the same functionality
encapsulated in `librados` to interact with the object store.  For example,
`librbd` and `libcephfs` leverage this functionality. You may use
`librados` to interact with Ceph directly (e.g., an application that talks to
Ceph, your own interface to Ceph, etc.).

.. toctree::
   :maxdepth: 2

   Introduction to librados <librados-intro>
   librados (C) <librados>
   librados (C++) <libradospp>
   librados (Python) <python>
   libcephsqlite (SQLite) <libcephsqlite>
   object class <objclass-sdk>
