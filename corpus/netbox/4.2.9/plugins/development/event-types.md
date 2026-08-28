---
collection: netbox
version: "4.2.9"
title: "Event Types"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/plugins/development/event-types.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Event Types

Plugins can register their own custom event types for use with NetBox [event rules](../../models/extras/eventrule.md). This is accomplished by calling the `register()` method on an instance of the `EventType` class. This can be done anywhere within the plugin. An example is provided below.

```python
from django.utils.translation import gettext_lazy as _
from netbox.events import EventType, EVENT_TYPE_KIND_SUCCESS

EventType(
    name='ticket_opened',
    text=_('Ticket opened'),
    kind=EVENT_TYPE_KIND_SUCCESS
).register()
```

::: netbox.events.EventType
