---
collection: ceph
version: "20.2.4"
title: "Tutorial"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/radosgw/swift/tutorial.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Tutorial

The Swift-compatible API tutorials follow a simple container-based object
lifecycle. The first step requires you to setup a connection between your
client and the RADOS Gateway server. Then, you may follow a natural
container and object lifecycle, including adding and retrieving object
metadata. See example code for the following languages:

- Java
- Python
- Ruby

.. ditaa::

   +----------------------------+        +-----------------------------+
   |                            |        |                             |
   |    Create a Connection     |------->|      Create a Container     |
   |                            |        |                             |
   +----------------------------+        +-----------------------------+
                                                        |
                 +--------------------------------------+
                 |
                 v
   +----------------------------+        +-----------------------------+
   |                            |        |                             |
   |     Create an Object       |------->| Add/Update Object Metadata  |
   |                            |        |                             |
   +----------------------------+        +-----------------------------+
                                                        |
                 +--------------------------------------+
                 |
                 v
   +----------------------------+        +-----------------------------+
   |                            |        |                             |
   |   List Owned Containers    |------->| List a Container's Contents |
   |                            |        |                             |
   +----------------------------+        +-----------------------------+
                                                        |
                 +--------------------------------------+
                 |
                 v
   +----------------------------+        +-----------------------------+
   |                            |        |                             |
   | Get an Object's Metadata   |------->|     Retrieve an Object      |
   |                            |        |                             |
   +----------------------------+        +-----------------------------+
                                                        |
                 +--------------------------------------+
                 |
                 v
   +----------------------------+        +-----------------------------+
   |                            |        |                             |
   |      Delete an Object      |------->|      Delete a Container     |
   |                            |        |                             |
   +----------------------------+        +-----------------------------+
