---
collection: ceph
version: "19.2.2"
title: "Journal Config Reference"
source_url: https://docs.ceph.com/en/squid/rados/configuration/journal-ref/
fetched_at: 2026-07-27T16:39:35+00:00
---
# Journal Config Reference

> **Warning:**
>
> Filestore has been deprecated in the Reef release and is no longer supported.

Filestore OSDs use a journal for two reasons: speed and consistency. Note
that since Luminous, the BlueStore OSD back end has been preferred and default.
This information is provided for pre-existing OSDs and for rare situations where
Filestore is preferred for new deployments.

- **Speed:** The journal enables the Ceph OSD Daemon to commit small writes
  quickly. Ceph writes small, random i/o to the journal sequentially, which
  tends to speed up bursty workloads by allowing the backing file system more
  time to coalesce writes. The Ceph OSD Daemon’s journal, however, can lead
  to spiky performance with short spurts of high-speed writes followed by
  periods without any write progress as the file system catches up to the
  journal.
- **Consistency:** Ceph OSD Daemons require a file system interface that
  guarantees atomic compound operations. Ceph OSD Daemons write a description
  of the operation to the journal and apply the operation to the file system.
  This enables atomic updates to an object (for example, placement group
  metadata). Every few seconds--between `filestore max sync interval` and
  `filestore min sync interval`--the Ceph OSD Daemon stops writes and
  synchronizes the journal with the file system, allowing Ceph OSD Daemons to
  trim operations from the journal and reuse the space. On failure, Ceph
  OSD Daemons replay the journal starting after the last synchronization
  operation.

Ceph OSD Daemons recognize the following journal settings:

journal_dio
:   > Enables direct i/o to the journal. Requires `journal block align`
    > set to `true`.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

journal_aio
:   > Enables using `libaio` for asynchronous writes to the journal.
    > Requires `journal dio` set to `true`. Version 0.61 and later,
    > `true`. Version 0.60 and earlier, `false`.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

journal_block_align
:   > Block aligns write operations. Required for `dio` and `aio`.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `true`

journal_max_write_bytes
:   > The maximum number of bytes the journal will write at any one time.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `10Mi`

journal_max_write_entries
:   > The maximum number of entries the journal will write at any one time.
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `100`

journal_align_min_size
:   > Align data payloads greater than the specified minimum.
    >
    > type:
    > :   `size`
    >
    > default:
    > :   `64Ki`

journal_zero_on_create
:   > Causes the file store to overwrite the entire journal with
    > `0`’s during `mkfs`.
    >
    > type:
    > :   `bool`
    >
    > default:
    > :   `false`

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
