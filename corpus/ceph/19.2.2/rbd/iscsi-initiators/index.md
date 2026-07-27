---
collection: ceph
version: "19.2.2"
title: "Configuring the iSCSI Initiators"
source_url: https://docs.ceph.com/en/squid/rbd/iscsi-initiators/
fetched_at: 2026-07-27T16:41:55+00:00
---
# Configuring the iSCSI Initiators

- [iSCSI Initiator for Linux](../iscsi-initiator-linux.md)
- [iSCSI Initiator for Microsoft Windows](../iscsi-initiator-win.md)
- [iSCSI Initiator for VMware ESX](../iscsi-initiator-esx.md)

  > > **Warning:**
  > >
  > > Applications that use SCSI persistent group reservations (PGR) and
  > > SCSI 2 based reservations are not supported when exporting a RBD image
  > > through more than one iSCSI gateway.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
