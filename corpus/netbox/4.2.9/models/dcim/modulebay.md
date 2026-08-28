---
collection: netbox
version: "4.2.9"
title: "Module Bays"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/dcim/modulebay.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Module Bays

Module bays represent a space or slot within a device in which a field-replaceable [module](./module.md) may be installed. A common example is that of a chassis-based switch such as the Cisco Nexus 9000 or Juniper EX9200. Modules in turn hold additional components that become available to the parent device.

!!! note
    If you need to model child devices rather than modules, use a [device bay](./devicebay.md) instead.

!!! tip
    Like most device components, module bays are instantiated automatically from [module bay templates](./modulebaytemplate.md) assigned to the selected device type when a device is created.

## Fields

### Device

The device to which this module bay belongs.

### Module

The module to which this bay belongs (optional).

### Name

The module bay's name. Must be unique to the parent device.

### Label

An alternative physical label identifying the module bay.

### Position

The numeric position in which this module bay is situated. For example, this would be the number assigned to a slot within a chassis-based switch.
