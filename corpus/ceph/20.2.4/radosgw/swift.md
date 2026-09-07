---
collection: ceph
version: "20.2.4"
title: "Ceph Object Gateway Swift API"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/radosgw/swift.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _radosgw swift:

# Ceph Object Gateway Swift API

Ceph supports a RESTful API that is compatible with the basic data access model of the Swift API.

## API

.. toctree::
   :maxdepth: 1

   Authentication <swift/auth>
   Service Ops <swift/serviceops>
   Container Ops <swift/containerops>
   Object Ops <swift/objectops>
   Temp URL Ops <swift/tempurl>
   Tutorial <swift/tutorial>
   Java <swift/java>
   Python <swift/python>
   Ruby <swift/ruby>

## Features Support

The following table describes the support status for current Swift functional features:

+---------------------------------+-----------------+----------------------------------------+
| Feature                         | Status          | Remarks                                |
+=================================+=================+========================================+
| **Authentication**              | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Get Account Metadata**        | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Swift ACLs**                  | Supported       | Supports a subset of Swift ACLs        |
+---------------------------------+-----------------+----------------------------------------+
| **List Containers**             | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Delete Container**            | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Create Container**            | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Get Container Metadata**      | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Update Container Metadata**   | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Delete Container Metadata**   | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **List Objects**                | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Static Website**              | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Create Object**               | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Create Large Object**         | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Delete Object**               | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Get Object**                  | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Copy Object**                 | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Get Object Metadata**         | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Update Object Metadata**      | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Expiring Objects**            | Supported       |                                        |
+---------------------------------+-----------------+----------------------------------------+
| **Temporary URLs**              | Partial Support | No support for container-level keys    |
+---------------------------------+-----------------+----------------------------------------+
| **Object Versioning**           | Partial Support | No support for `X-History-Location`  |
+---------------------------------+-----------------+----------------------------------------+
| **CORS**                        | Not Supported   |                                        |
+---------------------------------+-----------------+----------------------------------------+

.. _Swift API: https://developer.openstack.org/api-ref/object-store/index.html
