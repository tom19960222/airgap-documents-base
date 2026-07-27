---
collection: ceph
version: "19.2.2"
title: "rbd-ggate -- map rbd images via FreeBSD GEOM Gate"
source_url: https://docs.ceph.com/en/squid/man/8/rbd-ggate/
fetched_at: 2026-07-27T16:40:26+00:00
---
# rbd-ggate -- map rbd images via FreeBSD GEOM Gate

## Synopsis

**rbd-ggate** [--read-only] [--exclusive] [--device *ggate device*] map *image-spec* | *snap-spec*

**rbd-ggate** unmap *ggate device*

**rbd-ggate** list

## Description

**rbd-ggate** is a client for RADOS block device (rbd) images. It will
map a rbd image to a ggate (FreeBSD GEOM Gate class) device, allowing
access it as regular local block device.

## Commands

### map

Spawn a process responsible for the creation of ggate device and
forwarding I/O requests between the GEOM Gate kernel subsystem and
RADOS.

### unmap

Destroy ggate device and terminate the process responsible for it.

### list

List mapped ggate devices.

## Options

--device \*ggate device\*
:   Specify ggate device path.

--read-only
:   Map read-only.

--exclusive
:   Forbid writes by other clients.

## Image and snap specs

*image-spec* is [*pool-name*]/*image-name*

*snap-spec* is [*pool-name*]/*image-name*@*snap-name*

The default for *pool-name* is “rbd”. If an image name contains a slash
character (‘/’), *pool-name* is required.

## Availability

**rbd-ggate** is part of Ceph, a massively scalable, open-source,
distributed storage system. Please refer to the Ceph documentation at
<https://docs.ceph.com> for more information.

## See also

[rbd](../rbd/index.md)(8)
[ceph](../ceph/index.md)(8)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
