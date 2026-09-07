---
collection: ceph
version: "20.2.4"
title: "Configuring the iSCSI Initiators"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rbd/iscsi-initiators.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="configuring-the-iscsi-initiators"></a>

# Configuring the iSCSI Initiators

- [iSCSI Initiator for Linux](iscsi-initiator-linux.md)

- [iSCSI Initiator for Microsoft Windows](iscsi-initiator-win.md)

- [iSCSI Initiator for VMware ESX](iscsi-initiator-esx.md)

> **Warning:**
> Applications that use SCSI persistent group reservations (PGR) and
> SCSI 2 based reservations are not supported when exporting a RBD image
> through more than one iSCSI gateway.

.. toctree::
   :maxdepth: 1
   :hidden:

   Linux <iscsi-initiator-linux>
   Microsoft Windows <iscsi-initiator-win>
   VMware ESX <iscsi-initiator-esx>
