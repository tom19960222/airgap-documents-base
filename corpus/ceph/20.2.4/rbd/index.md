---
collection: ceph
version: "20.2.4"
title: "Ceph Block Device"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rbd/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Ceph Block Device

.. index:: Ceph Block Device; introduction

A block is a sequence of bytes (often 512).
Block-based storage interfaces are a mature and common way to store data on
media including HDDs, SSDs, CDs, floppy disks, and even tape.
The ubiquity of block device interfaces is a perfect fit for interacting
with mass data storage including Ceph.

Ceph block devices are thin-provisioned, resizable, and store data striped over
multiple OSDs.  Ceph block devices leverage
RADOS (Reliable Autonomic Distributed Object Store) capabilities
including snapshotting, replication and strong consistency. Ceph block
storage clients communicate with Ceph clusters through kernel modules or
the `librbd` library.

.. ditaa::

   +------------------------+ +------------------------+
   |     Kernel Module      | |        librbd          |
   +------------------------+-+------------------------+
   |                   RADOS Protocol                  |
   +------------------------+-+------------------------+
   |          OSDs          | |        Monitors        |
   +------------------------+ +------------------------+

> **Note:** Kernel modules can use Linux page caching. For `librbd`-based
> applications, Ceph supports RBD Caching.

Ceph's block devices deliver high performance with vast scalability to
kernel modules, or to KVMs (kernel virtual machines) such as QEMU, and
cloud-based computing systems like OpenStack, OpenNebula and CloudStack
that rely on libvirt and QEMU to integrate with Ceph block devices. You can use
the same cluster to operate the Ceph RADOS Gateway, the
Ceph File System, and Ceph block devices simultaneously.

> **Important:** To use Ceph Block Devices, you must have access to a running
> Ceph cluster.

.. toctree::
   :maxdepth: 1

	Basic Commands <rados-rbd-cmds>

.. toctree::
   :maxdepth: 2

   Operations <rbd-operations>

.. toctree::

	:maxdepth: 2

        Integrations <rbd-integrations>

.. toctree::

	:maxdepth: 2

	Manpages <man/index>

.. toctree::

	:maxdepth: 2

	APIs <api/index>

.. _RBD Caching: ./rbd-config-ref/
.. _kernel modules: ./rbd-ko/
.. _QEMU: ./qemu-rbd/
.. _OpenStack: ./rbd-openstack
.. _OpenNebula: https://docs.opennebula.io/stable/open_cluster_deployment/storage_setup/ceph_ds.html
.. _CloudStack: ./rbd-cloudstack
