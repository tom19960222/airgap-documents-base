---
collection: netbox
version: "4.2.9"
title: "Contacts"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/tenancy/contact.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Contacts

A contact represents an individual or group that has been associated with an object in NetBox for administrative reasons. For example, you might assign one or more operational contacts to each site.

## Fields

### Group

The [contact group](./contactgroup.md) to which this contact is assigned (if any).

### Name

The name of the contact. This may be an individual or a team/department. (This is the only required contact detail; all others are optional.)

### Title

The contact's title or role.

### Phone

The contact's phone number. (Note that NetBox does _not_ enforce a particular numbering format.)

### Email

The contact's email address.

### Address

The contact's physical or mailing address.

### Link

A URL to reach the contact via some other means.
