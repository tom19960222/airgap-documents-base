---
collection: netbox
version: "4.2.9"
title: "Journal Entries"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/models/extras/journalentry.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Journal Entries

Most objects in NetBox support journaling. This is the ability of users to record chronological notes indicating changes to or work performed on resources in NetBox. For example, a data center technician might add a journal entry for a device when swapping out a failed power supply.

## Fields

### Kind

A general classification for the entry type (info, success, warning, or danger.)

!!! tip
    Additional kinds may be defined by setting `JournalEntry.kind` under the [`FIELD_CHOICES`](../../configuration/data-validation.md#field_choices) configuration parameter.

### Comments

The body of the journal entry. [Markdown](../../reference/markdown.md) rendering is supported.
