---
collection: netbox
version: "4.2.9"
title: "Notification"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/notification.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Notification

A notification alerts a user that a specific action has taken place in NetBox, such as an object being modified or a background job completing. A notification may be generated via a user's [subscription](./subscription.md) to a particular object, or by an event rule targeting a [notification group](./notificationgroup.md) of which the user is a member.

## Fields

### User

The recipient of the notification.

### Object

The object to which the notification relates.

### Event Type

The type of event indicated by the notification.
