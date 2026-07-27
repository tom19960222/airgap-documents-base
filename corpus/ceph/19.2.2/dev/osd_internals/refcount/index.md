---
collection: ceph
version: "19.2.2"
title: "Refcount"
source_url: https://docs.ceph.com/en/squid/dev/osd_internals/refcount/
fetched_at: 2026-07-27T16:43:09+00:00
---
# Refcount

## Introduction

Deduplication, as described in ../deduplication.rst, needs a way to
maintain a target pool of deduplicated chunks with atomic ref
refcounting. To that end, there exists an osd object class
refcount responsible for using the object class machinery to
maintain refcounts on deduped chunks and ultimately remove them
as the refcount hits 0.

## Class Interface

See cls/refcount/cls_refcount_client\*

- cls_refcount_get

  Atomically increments the refcount with specified tag

  ```
  void cls_refcount_get(librados::ObjectWriteOperation& op, const string& tag, bool implicit_ref = false);
  ```
- cls_refcount_put

  Atomically decrements the refcount specified by passed tag

  ```
  void cls_refcount_put(librados::ObjectWriteOperation& op, const string& tag, bool implicit_ref = false);
  ```
- cls_refcount_Set

  Atomically sets the set of refcounts with passed list of tags

  ```
  void cls_refcount_set(librados::ObjectWriteOperation& op, list<string>& refs);
  ```
- cls_refcount_read

  Dumps the current set of ref tags for the object

  ```
  int cls_refcount_read(librados::IoCtx& io_ctx, string& oid, list<string> *refs, bool implicit_ref = false);
  ```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
