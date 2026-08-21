---
collection: libvirt
version: "12.7.0"
title: "Storage Pool Capabilities XML format"
source_url: https://libvirt.org/formatstoragecaps.html
fetched_at: 2026-08-21T04:09:27+00:00
---
# Storage Pool Capabilities XML format

Contents

- [Overview](formatstoragecaps.md#overview)
- [Element and attribute overview](formatstoragecaps.md#element-and-attribute-overview)

# [Overview](formatstoragecaps.md#id1)

The Storage Pool Capabilities XML will provide the information to determine what
types of Storage Pools exist, whether the pool is supported, and if relevant the
source format types, the required source elements, and the target volume format
types.

# [Element and attribute overview](formatstoragecaps.md#id2)

A query interface was added to the virConnect API's to retrieve the XML listing
of the set of Storage Pool Capabilities ( Since 5.2.0 ):

> virConnectGetStoragePoolCapabilities ([API docs](https://libvirt.org/html/libvirt-libvirt-storage.html#virConnectGetStoragePoolCapabilities))

The root element that emulator capability XML document starts with is named
storagepoolCapabilities. There will be any number of pool child elements
with two attributes type and supported. Each pool element may have a
poolOptions or volOptions subelements to describe the available
features. Sample XML output is:

```
<storagepoolCapabilities>
  <pool type='dir' supported='yes'>
    <volOptions>
      <defaultFormat type='raw'</>
      <enum name='targetFormatType'>
        <value>none</value>
        <value>raw</value>
        ...
      </enum>
    </volOptions>
  </pool>
  <pool type='fs' supported='yes'>
    <poolOptions>
      <defaultFormat type='auto'</>
      <enum name='sourceFormatType'>
        <value>auto</value>
        <value>ext2</value>
        ...
      </enum>
    </poolOptions>
    <volOptions>
      <defaultFormat type='raw'</>
      <enum name='targetFormatType'>
        <value>none</value>
        <value>raw</value>
        ...
      </enum>
    </volOptions>
  </pool>
  ...
</storagepoolCapabilities>
```

The following section describes subelements of the poolOptions and
volOptions subelements

defaultFormat
:   For the poolOptions, the type attribute describes the default format
    name used for the pool source. For the volOptions, the type attribute
    describes the default volume name used for each volume.

enum
:   Each enum uses a name from the list below with any number of value value
    subelements describing the valid values.

    sourceFormatType
    :   Lists all the possible poolOptions source pool format types.

    targetFormatType
    :   Lists all the possible volOptions target volume format types.
