---
collection: netbox
version: "4.2.9"
title: "User Preferences"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/development/user-preferences.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# User Preferences

The `users.UserConfig` model holds individual preferences for each user in the form of JSON data. This page serves as a manifest of all recognized user preferences in NetBox.

## Available Preferences

| Name                     | Description                                                   |
|--------------------------|---------------------------------------------------------------|
| data_format              | Preferred format when rendering raw data (JSON or YAML)       |
| pagination.per_page      | The number of items to display per page of a paginated table  |
| pagination.placement     | Where to display the paginator controls relative to the table |
| tables.${table}.columns  | The ordered list of columns to display when viewing the table |
| tables.${table}.ordering | A list of column names by which the table should be ordered   |
