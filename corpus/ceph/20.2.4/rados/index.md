---
collection: ceph
version: "20.2.4"
title: "Ceph Storage Cluster"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="rados-index"></a>

# Ceph Storage Cluster

The Ceph Storage Cluster is the foundation for all Ceph deployments.
Based upon RADOS (Reliable Autonomic Distributed Object Store), Ceph
Storage Clusters consist of several types of daemons:

  1. a Ceph OSD Daemon (OSD) stores data as objects on a storage node
  2. a Ceph Monitor (MON) maintains a master copy of the cluster map.
  3. a Ceph Manager  manager daemon

A Ceph Storage Cluster might contain thousands of storage nodes. A
minimal system has at least one Ceph Monitor and two Ceph OSD
Daemons for data replication.

The Ceph File System, Ceph Object Storage and Ceph Block Devices read data from
and write data to the Ceph Storage Cluster.

.. container:: columns-3

   .. container:: column

      .. raw:: html

          <h3>Config and Deploy</h3>

      Ceph Storage Clusters have a few required settings, but most configuration
      settings have default values. A typical deployment uses a deployment tool
      to define a cluster and bootstrap a monitor. See [cephadm](../cephadm/index.md#cephadm) for details.

      .. toctree::
         :maxdepth: 2

         Configuration <configuration/index>

   .. container:: column

      .. raw:: html

          <h3>Operations</h3>

      Once you have deployed a Ceph Storage Cluster, you may begin operating
      your cluster.

      .. toctree::
         :maxdepth: 2

         Operations <operations/index>

      .. toctree::
         :maxdepth: 1

         Man Pages <man/index>

      .. toctree::
         :hidden:

         troubleshooting/index

   .. container:: column

      .. raw:: html

          <h3>APIs</h3>

      Most Ceph deployments use [Ceph Block Devices](../rbd/index.md), [Ceph Object Storage](../radosgw/index.md) and/or the
      [Ceph File System](../cephfs/index.md). You  may also develop applications that talk directly to
      the Ceph Storage Cluster.

      .. toctree::
         :maxdepth: 2

         APIs <api/index>
