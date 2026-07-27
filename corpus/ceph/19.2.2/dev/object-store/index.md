---
collection: ceph
version: "19.2.2"
title: "Object Store Architecture Overview"
source_url: https://docs.ceph.com/en/squid/dev/object-store/
fetched_at: 2026-07-27T16:41:28+00:00
---
# Object Store Architecture Overview

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

> **Todo:**
>
> write more here

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
