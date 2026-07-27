---
collection: ceph
version: "19.2.2"
title: "Ceph Storage Cluster APIs"
source_url: https://docs.ceph.com/en/squid/rados/api/
fetched_at: 2026-07-27T16:39:29+00:00
---
# Ceph Storage Cluster APIs

The [Ceph Storage Cluster](../../glossary/index.md#term-Ceph-Storage-Cluster) has a messaging layer protocol that enables
clients to interact with a [Ceph Monitor](../../glossary/index.md#term-Ceph-Monitor) and a [Ceph OSD Daemon](../../glossary/index.md#term-Ceph-OSD-Daemon).
`librados` provides this functionality to [Ceph Client](../../glossary/index.md#term-Ceph-Client)s in the form of
a library. All Ceph Clients either use `librados` or the same functionality
encapsulated in `librados` to interact with the object store. For example,
`librbd` and `libcephfs` leverage this functionality. You may use
`librados` to interact with Ceph directly (e.g., an application that talks to
Ceph, your own interface to Ceph, etc.).

- [Introduction to librados](librados-intro/index.md)
  - [Step 1: Getting librados](librados-intro/index.md#step-1-getting-librados)
  - [Step 2: Configuring a Cluster Handle](librados-intro/index.md#step-2-configuring-a-cluster-handle)
  - [Step 3: Creating an I/O Context](librados-intro/index.md#step-3-creating-an-i-o-context)
  - [Step 4: Closing Sessions](librados-intro/index.md#step-4-closing-sessions)
- [librados (C)](librados/index.md)
  - [Example: connecting and writing an object](librados/index.md#example-connecting-and-writing-an-object)
  - [Asynchronous IO](librados/index.md#asynchronous-io)
  - [API calls](librados/index.md#api-calls)
- [librados (C++)](libradospp/index.md)
- [librados (Python)](python/index.md)
  - [Installation](python/index.md#installation)
  - [Getting Started](python/index.md#getting-started)
  - [Cluster Handle API](python/index.md#cluster-handle-api)
  - [Input/Output Context API](python/index.md#input-output-context-api)
  - [Object Interface](python/index.md#object-interface)
- [libcephsqlite (SQLite)](libcephsqlite/index.md)
  - [Usage](libcephsqlite/index.md#usage)
  - [User](libcephsqlite/index.md#user)
  - [Page Size](libcephsqlite/index.md#page-size)
  - [Cache](libcephsqlite/index.md#cache)
  - [Journal Persistence](libcephsqlite/index.md#journal-persistence)
  - [Exclusive Lock Mode](libcephsqlite/index.md#exclusive-lock-mode)
  - [WAL Journal](libcephsqlite/index.md#wal-journal)
  - [Performance Notes](libcephsqlite/index.md#performance-notes)
  - [Recommended Use-Cases](libcephsqlite/index.md#recommended-use-cases)
  - [Parallel Access](libcephsqlite/index.md#parallel-access)
  - [Export or Extract Database out of RADOS](libcephsqlite/index.md#export-or-extract-database-out-of-rados)
  - [Temporary Tables](libcephsqlite/index.md#temporary-tables)
  - [Breaking Locks](libcephsqlite/index.md#breaking-locks)
  - [How to Corrupt Your Database](libcephsqlite/index.md#how-to-corrupt-your-database)
  - [Performance Statistics](libcephsqlite/index.md#performance-statistics)
  - [Debugging](libcephsqlite/index.md#debugging)
- [object class](objclass-sdk/index.md)
  - [Installing objclass.h](objclass-sdk/index.md#installing-objclass-h)
  - [Using the SDK example](objclass-sdk/index.md#using-the-sdk-example)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
