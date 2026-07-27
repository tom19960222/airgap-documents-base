---
collection: ceph
version: "19.2.2"
title: "NFS CephFS-RGW Developer Guide"
source_url: https://docs.ceph.com/en/squid/dev/vstart-ganesha/
fetched_at: 2026-07-27T16:41:34+00:00
---
# NFS CephFS-RGW Developer Guide

CephFS exports are supported since Octopus and RGW exports are supported since
Quincy.

## Configuring NFS Ganesha to export CephFS with vstart

1. Using `cephadm`

   > ```bash
   > $ MDS=1 MON=1 OSD=3 NFS=1 ../src/vstart.sh -n -d --cephadm
   > ```
   >
   > This will deploy a single NFS Ganesha daemon using `vstart.sh`, where the
   > daemon will listen on the default NFS Ganesha port. Also cephfs export is
   > created.
2. Using test orchestrator

   > ```bash
   > $ MDS=1 MON=1 OSD=3 NFS=1 ../src/vstart.sh -n -d
   > ```
   >
   > Environment variable `NFS` is the number of NFS Ganesha daemons to be
   > deployed, each listening on a random port.
   >
   > > **Note:**
   > >
   > > NFS Ganesha packages must be pre-installed for this to work.

## Configuring NFS Ganesha to export RGW with vstart

1. Using `cephadm`

   > ```bash
   > $ MON=1 OSD=3 RGW=1 NFS=1 ../src/vstart.sh -n -d --cephadm
   > ```
   >
   > This will deploy a single NFS Ganesha daemon using `vstart.sh`, where the
   > daemon will listen on the default NFS Ganesha port. Also rgw export is
   > created.
   >
   > > **Note:**
   > >
   > > boto python module must be pre-installed for this to work.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
