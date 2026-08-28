---
collection: netbox
version: "4.2.9"
title: "Notifications"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/features/notifications.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Notifications

NetBox includes a system for generating user notifications, which can be marked as read or deleted by individual users. There are two built-in mechanisms for generating a notification:

* A user can subscribe to an object. When that object is modified, a notification is created to inform the user of the change.
* An [event rule](./event-rules.md) can be defined to automatically generate a notification for one or more users in response to specific system events.

Additionally, NetBox plugins can generate notifications for their own purposes.
