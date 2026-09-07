---
collection: ceph
version: "20.2.4"
title: "README"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/scripts/README.md
fetched_at: 2026-08-18T01:32:45Z
---
Script Usage
============

Peering State Model: gen_state_diagram.py
------------------------------------------
    $ git clone https://github.com/ceph/ceph.git
    $ cd ceph
    $ cat src/osd/PeeringState.h src/osd/PeeringState.cc | doc/scripts/gen_state_diagram.py > doc/dev/peering_graph.generated.dot
    $ sed -i 's/7,7/1080,1080/' doc/dev/peering_graph.generated.dot
    $ dot -Tsvg doc/dev/peering_graph.generated.dot > doc/dev/peering_graph.generated.svg
