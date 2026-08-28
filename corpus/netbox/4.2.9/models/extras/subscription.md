---
collection: netbox
version: "4.2.9"
title: "Subscription"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/subscription.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Subscription

A record indicating that a user is to be notified of any changes to a particular NetBox object. A notification maps exactly one user to exactly one object.

When an object to which a user is subscribed changes, a [notification](./notification.md) is generated for the user.

## Fields

### User

The subscribed user.

### Object

The object to which the user is subscribed.
