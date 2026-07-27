---
collection: ceph
version: "19.2.2"
title: "Ceph Internals"
source_url: https://docs.ceph.com/en/squid/dev/internals/
fetched_at: 2026-07-27T16:38:49+00:00
---
# Ceph Internals

> **Note:**
>
> For information on how to use Ceph as a library (from your own
> software), see [API Documentation](../../api/index.md).

## Starting a Development-mode Ceph Cluster

Compile the source and then run the following commands to start a
development-mode Ceph cluster:

```
cd build
OSD=3 MON=3 MGR=3 ../src/vstart.sh -n -x
# check that it's there
bin/ceph health
```

Mailing list

The `dev@ceph.io` list is for discussion about the development of Ceph,
its interoperability with other technology, and the operations of the
project itself. Subscribe by sending a message to `dev-join@ceph.io`
with the word subscribe in the subject.

Alternatively you can visit <https://lists.ceph.io> and register.

The [ceph-devel@vger.kernel.org](mailto:ceph-devel%40vger.kernel.org) list is for discussion
and patch review for the Linux kernel Ceph client component.
Subscribe by sending a message to `majordomo@vger.kernel.org` with the line:

```
subscribe ceph-devel
```

in the body of the message.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
