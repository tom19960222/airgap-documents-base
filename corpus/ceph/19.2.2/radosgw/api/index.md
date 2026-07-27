---
collection: ceph
version: "19.2.2"
title: "librgw (Python)"
source_url: https://docs.ceph.com/en/squid/radosgw/api/
fetched_at: 2026-07-27T16:40:35+00:00
---
# librgw (Python)

The rgw python module provides file-like access to rgw.

## API Reference

This module is a thin wrapper around rgw_file.

*class* rgw.LibRGWFS
:   librgwfs python wrapper

    shutdown()
    :   Unmount and destroy the ceph mount handle.

    version()
    :   Get the version number of the `librgwfile` C library.

        Returns:
        :   a tuple of `(major, minor, extra)` components of the
            libcephfs version

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
