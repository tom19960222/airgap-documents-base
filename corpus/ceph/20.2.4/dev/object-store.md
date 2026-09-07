---
collection: ceph
version: "20.2.4"
title: "Object Store Architecture Overview"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/object-store.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Object Store Architecture Overview

.. graphviz::

    digraph object_store {
     size="7,7";
     node [color=lightblue2, style=filled, fontname="Serif"];

     "testrados" -> "librados"
     "testradospp" -> "librados"

     "rbd" -> "librados"

     "radostool" -> "librados"

     "radosgw-admin" -> "radosgw"

     "radosgw" -> "librados"

     "radosacl" -> "librados"

     "librados" -> "objecter"

     "ObjectCacher" -> "Filer"

     "dumpjournal" -> "Journaler"

     "Journaler" -> "Filer"

     "SyntheticClient" -> "Filer"
     "SyntheticClient" -> "objecter"

     "Filer" -> "objecter"

     "objecter" -> "OSDMap"

     "ceph-osd" -> "PG"
     "ceph-osd" -> "ObjectStore"

     "crushtool" -> "CrushWrapper"

     "OSDMap" -> "CrushWrapper"

     "OSDMapTool" -> "OSDMap"

     "PG" -> "PrimaryLogPG"
     "PG" -> "ObjectStore"
     "PG" -> "OSDMap"

     "PrimaryLogPG" -> "ObjectStore"
     "PrimaryLogPG" -> "OSDMap"

     "ObjectStore" -> "BlueStore"

     "BlueStore" -> "rocksdb"
   }

.. todo:: write more here
