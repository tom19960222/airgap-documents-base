---
collection: ceph
version: "19.2.2"
title: "CephContext"
source_url: https://docs.ceph.com/en/squid/dev/context/
fetched_at: 2026-07-27T16:41:15+00:00
---
# CephContext

A CephContext represents a single view of the Ceph cluster. It comes complete
with a configuration, a set of performance counters (PerfCounters), and a
heartbeat map. You can find more information about CephContext in
src/common/ceph_context.h.

Generally, you will have only one CephContext in your application, called
g_ceph_context. However, in library code, it is possible that the library user
will initialize multiple CephContexts. For example, this would happen if he
called rados_create more than once.

A ceph context is required to issue log messages. Why is this? Well, without
the CephContext, we would not know which log messages were disabled and which
were enabled. The dout() macro implicitly references g_ceph_context, so it
can’t be used in library code. It is fine to use dout and derr in daemons, but
in library code, you must use ldout and lderr, and pass in your own CephContext
object. The compiler will enforce this restriction.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
