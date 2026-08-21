---
collection: libvirt
version: "12.7.0"
title: "XML Format"
source_url: https://libvirt.org/format.html
fetched_at: 2026-08-21T04:09:21+00:00
---
# XML Format

Objects in the libvirt API are configured using XML documents to allow for ease
of extension in future releases. Each XML document has an associated Relax-NG
schema that can be used to validate documents prior to usage.

- [Domains](formatdomain.md)
- [Networks](formatnetwork.md)
- [Network filtering](formatnwfilter.md)
- [Network ports](formatnetworkport.md)
- [Storage](formatstorage.md)
- [Storage encryption](formatstorageencryption.md)
- [Capabilities](formatcaps.md)
- [Domain capabilities](formatdomaincaps.md)
- [Storage Pool capabilities](formatstoragecaps.md)
- [Node devices](formatnode.md)
- [Secrets](formatsecret.md)
- [Snapshots](formatsnapshot.md)
- [Checkpoints](formatcheckpoint.md)
- [Backup jobs](formatbackup.md)

# Command line validation

The virt-xml-validate tool provides a simple command line for validating XML
documents prior to giving them to libvirt. It uses the locally installed RNG
schema documents. It will auto-detect which schema to use for validation based
on the name of the top level element in the input document. Thus it merely
requires the XML document filename to be passed on the command line

```
$ virt-xml-validate /path/to/XML/file
```
