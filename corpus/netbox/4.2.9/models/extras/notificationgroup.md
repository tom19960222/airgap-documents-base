---
collection: netbox
version: "4.2.9"
title: "Notification Group"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/notificationgroup.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Notification Group

A set of NetBox users and/or groups of users identified as recipients for certain [notifications](./notification.md).

## Fields

### Name

The name of the notification group.

### Users

One or more users directly designated as members of the notification group.

### Groups

All users of any selected groups are considered as members of the notification group.
