---
collection: ceph
version: "19.2.2"
title: "ceph-post-file -- post files for ceph developers"
source_url: https://docs.ceph.com/en/squid/man/8/ceph-post-file/
fetched_at: 2026-07-27T16:42:04+00:00
---
# ceph-post-file -- post files for ceph developers

## Synopsis

**ceph-post-file** [-d *description] [-u \*user*] *file or dir* …

## Description

**ceph-post-file** will upload files or directories to ceph.com for
later analysis by Ceph developers.

Each invocation uploads files or directories to a separate directory
with a unique tag. That tag can be passed to a developer or
referenced in a bug report (<http://tracker.ceph.com/>). Once the
upload completes, the directory is marked non-readable and
non-writeable to prevent access or modification by other users.

## Warning

Basic measures are taken to make posted data be visible only to
developers with access to ceph.com infrastructure. However, users
should think twice and/or take appropriate precautions before
posting potentially sensitive data (for example, logs or data
directories that contain Ceph secrets).

## Options

-d \*description\*, --description \*description\*
:   Add a short description for the upload. This is a good opportunity
    to reference a bug number. There is no default value.

-u \*user\*
:   Set the user metadata for the upload. This defaults to whoami`@`hostname -f.

## Examples

To upload a single log:

```
ceph-post-file /var/log/ceph/ceph-mon.`hostname`.log
```

To upload several directories:

```
ceph-post-file -d 'mon data directories' /var/log/ceph/mon/*
```

## Availability

**ceph-post-file** is part of Ceph, a massively scalable, open-source, distributed storage system. Please refer to
the Ceph documentation at <https://docs.ceph.com> for more information.

## See also

[ceph](../ceph/index.md)(8),
[ceph-debugpack](../ceph-debugpack/index.md)(8),

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
