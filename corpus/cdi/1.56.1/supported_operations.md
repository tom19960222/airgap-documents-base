---
collection: cdi
version: "1.56.1"
title: "Containerized Data Importer supported operations"
source_url: https://github.com/kubevirt/containerized-data-importer/blob/ee9a06635eed17f8a635915bbb2f354ce38c8f72/doc/supported_operations.md
fetched_at: 2023-07-31T07:56:04-05:00
---
# Containerized Data Importer supported operations
The Containerized Data Importer (CDI) supports importing data/disk images.

Supported formats: qcow2, VMDK, VDI, VHD, VHDX, raw XZ-compressed, gzip-compressed, and uncompressed raw files can be imported.
They will all be converted to the raw format.

Supported sources: http, https, http with basic auth, docker registry, S3 buckets, upload.

Note: Some of these operations require [scratch space](scratch-space.md), doubling the storage space requirement of the import and the writes.
This is done with some misbehaving servers (not supporting HEAD requests), custom CAs, and during upload.

Additionally, tar archives are supported for a few scenarios: importing from HTTP/S servers, and only to Filesystem mode DataVolumes.
