---
collection: libvirt
version: "12.7.0"
title: "virt-xml-validate"
source_url: https://libvirt.org/manpages/virt-xml-validate.html
fetched_at: 2026-08-21T04:10:32+00:00
---
# virt-xml-validate

validate libvirt XML files against a schema

Manual section
:   1

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virt-xml-validate.md#synopsis)
- [DESCRIPTION](virt-xml-validate.md#description)
- [OPTIONS](virt-xml-validate.md#options)
- [EXIT STATUS](virt-xml-validate.md#exit-status)
- [AUTHOR](virt-xml-validate.md#author)
- [BUGS](virt-xml-validate.md#bugs)
- [COPYRIGHT](virt-xml-validate.md#copyright)
- [LICENSE](virt-xml-validate.md#license)
- [SEE ALSO](virt-xml-validate.md#see-also)

# [SYNOPSIS](virt-xml-validate.md#id1)

virt-xml-validate *XML-FILE* [*SCHEMA-NAME*]

virt-xml-validate *OPTION*

# [DESCRIPTION](virt-xml-validate.md#id2)

Validates a libvirt XML for compliance with the published schema.
The first compulsory argument is the path to the XML file to be
validated. The optional second argument is the name of the schema
to validate against. If omitted, the schema name will be inferred
from the name of the root element in the XML document.

Valid schema names currently include

- cpu

The schema for the XML format of cpu

- domainsnapshot

The schema for the XML format used by domain snapshot configuration

- domaincheckpoint

The schema for the XML format used by domain checkpoint configuration

- domainbackup

The schema for the XML format used by domain backup configuration

- domaincaps

The schema for the XML format of domain capabilities

- domain

The schema for the XML format used by guest domains configuration

- networkport

The schema for the XML format used by network port configuration

- network

The schema for the XML format used by virtual network configuration

- storagepoolcaps

The schema for the XML format of storage pool capabilities

- storagepool

The schema for the XML format used by storage pool configuration

- storagevol

The schema for the XML format used by storage volume descriptions

- nodedev

The schema for the XML format used by node device descriptions

- capability

The schema for the XML format used to declare driver capabilities

- nwfilter

The schema for the XML format used by network traffic filters

- nwfilterbinding

The schema for XML format used by network filter bindings.

- secret

The schema for the XML format used by secrets descriptions

- interface

The schema for the XML format used by physical host interfaces

# [OPTIONS](virt-xml-validate.md#id3)

-h, --help

Display command line help usage then exit.

-V, --version

Display version information then exit.

# [EXIT STATUS](virt-xml-validate.md#id4)

Upon successful validation, an exit status of 0 will be set. Upon
failure a non-zero status will be set.

# [AUTHOR](virt-xml-validate.md#id5)

Daniel P. Berrangé

# [BUGS](virt-xml-validate.md#id6)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [COPYRIGHT](virt-xml-validate.md#id7)

Copyright (C) 2009-2013 by Red Hat, Inc.
Copyright (C) 2009 by Daniel P. Berrangé

# [LICENSE](virt-xml-validate.md#id8)

virt-xml-validate is distributed under the terms of the GNU GPL v2+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virt-xml-validate.md#id9)

virsh(1), [online XML format descriptions](../format.md),
[https://libvirt.org/](../index.md)
