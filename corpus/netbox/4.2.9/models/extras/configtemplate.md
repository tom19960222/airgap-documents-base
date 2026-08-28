---
collection: netbox
version: "4.2.9"
title: "Configuration Templates"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/configtemplate.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Configuration Templates

Configuration templates can be used to render [device](../dcim/device.md) configurations from [context data](../../features/context-data.md). Templates are written in the [Jinja2 language](https://jinja.palletsprojects.com/) and can be associated with devices roles, platforms, and/or individual devices.

Context data is made available to [devices](../dcim/device.md) and/or [virtual machines](../virtualization/virtualmachine.md) based on their relationships to other objects in NetBox. For example, context data can be associated only with devices assigned to a particular site, or only to virtual machines in a certain cluster.

See the [configuration rendering documentation](../../features/configuration-rendering.md) for more information.

## Fields

### Name

A unique human-friendly name.

### Weight

A numeric value which influences the order in which context data is merged. Contexts with a lower weight are merged before those with a higher weight.

### Data File

Template code may optionally be sourced from a remote [data file](../core/datafile.md), which is synchronized from a remote data source. When designating a data file, there is no need to specify template code: It will be populated automatically from the data file.

### Template Code

Jinja2 template code, if being defined locally rather than replicated from a data file.

### Environment Parameters

A dictionary of any additional parameters to pass when instantiating the [Jinja2 environment](https://jinja.palletsprojects.com/en/3.1.x/api/#jinja2.Environment). Jinja2 supports various optional parameters which can be used to modify its default behavior.
