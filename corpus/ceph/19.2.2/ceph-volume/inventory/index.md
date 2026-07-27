---
collection: ceph
version: "19.2.2"
title: "inventory"
source_url: https://docs.ceph.com/en/squid/ceph-volume/inventory/
fetched_at: 2026-07-27T16:41:38+00:00
---
# `inventory`

The `inventory` subcommand queries a host’s disc inventory and provides
hardware information and metadata on every physical device.

By default the command returns a short, human-readable report of all physical disks.

For programmatic consumption of this report pass `--format json` to generate a
JSON formatted report. This report includes extensive information on the
physical drives such as disk metadata (like model and size), logical volumes
and whether they are used by ceph, and if the disk is usable by ceph and
reasons why not.

A device path can be specified to report extensive information on a device in
both plain and json format.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
