---
collection: ceph
version: "20.2.4"
title: "General Config Reference"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/configuration/general-config-ref.rst
fetched_at: 2026-08-18T01:32:45Z
---
# General Config Reference

.. confval:: admin_socket
   :default: /var/run/ceph/$cluster-$name.asok

.. confval:: pid_file

.. confval:: chdir

.. confval:: fatal_signal_handlers

.. describe:: max_open_files

   If set, when the :term:`Ceph Storage Cluster` starts, Ceph sets
   the max open FDs at the OS level (i.e., the max # of file
   descriptors). A suitably large value prevents Ceph Daemons from running out
   of file descriptors.

   :Type: 64-bit Integer
   :Required: No
   :Default: ``0``
