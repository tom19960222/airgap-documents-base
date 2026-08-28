---
collection: netbox
version: "4.2.9"
title: "Synchronized Data"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/integrations/synchronized-data.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Synchronized Data

Some NetBox models support automatic synchronization of certain attributes from remote [data sources](../models/core/datasource.md), such as a git repository hosted on GitHub or GitLab. Data from the authoritative remote source is synchronized locally in NetBox as [data files](../models/core/datafile.md).

!!! note "Permissions"
    A user must be assigned the `core.sync_datasource` permission in order to synchronize local files from a remote data source. This is accomplished by creating a permission for the "Core > Data Source" object type with the `sync` action, and assigning it to the desired user and/or group.

The following features support the use of synchronized data:

* [Configuration templates](../features/configuration-rendering.md)
* [Configuration context data](../features/context-data.md)
* [Export templates](../customization/export-templates.md)
