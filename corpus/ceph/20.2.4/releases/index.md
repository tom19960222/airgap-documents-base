---
collection: ceph
version: "20.2.4"
title: "Ceph Releases (index)"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/releases/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="ceph-releases-index"></a>

# Ceph Releases (index)

.. toctree::
   :maxdepth: 1

.. ceph_releases_gantt:: releases.yml

<a id="active-releases"></a>

## Active Releases

The following Ceph releases are actively maintained and receive periodic backports and
security fixes.

.. toctree::
   :maxdepth: 1
   :hidden:

   Squid (v19.2.*) <squid>
   Reef (v18.2.*) <reef>

.. ceph_releases:: releases.yml current

## Archived Releases

The following older Ceph releases are no longer maintained (do not
receive bug fixes or backports).

.. ceph_releases:: releases.yml eol

.. toctree::
   :maxdepth: 1
   :hidden:

   Quincy (v17.2.*) <quincy>
   Pacific (v16.2.*) <pacific>
   Octopus (v15.2.*) <octopus>
   Nautilus (v14.2.*) <nautilus>
   Mimic (v13.2.*) <mimic>
   Luminous (v12.2.*) <luminous>
   Kraken (v11.2.*) <kraken>
   Jewel (v10.2.*) <jewel>
   Infernalis (v9.2.*) <infernalis>
   Hammer (v0.94.*) <hammer>
   Giant (v0.87.*) <giant>
   Firefly (v0.80.*) <firefly>
   Emperor (v0.72.*) <emperor>
   Dumpling (v0.67.*) <dumpling>
   Cuttlefish (v0.61.*) <cuttlefish>
   Bobtail (v0.56.*) <bobtail>
   Argonaut (v0.48.*) <argonaut>

## Release timeline

.. ceph_timeline_gantt:: releases.yml squid reef quincy

.. ceph_timeline:: releases.yml squid reef quincy
