---
collection: netbox
version: "4.2.9"
title: "Search"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/plugins/development/search.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Search

Plugins can define and register their own models to extend NetBox's core search functionality. Typically, a plugin will include a file named `search.py`, which holds all search indexes for its models (see the example below).

```python
# search.py
from netbox.search import SearchIndex
from .models import MyModel

class MyModelIndex(SearchIndex):
    model = MyModel
    fields = (
        ('name', 100),
        ('description', 500),
        ('comments', 5000),
    )
    display_attrs = ('site', 'device', 'status', 'description')
```

Fields listed in `display_attrs` will not be cached for search, but will be displayed alongside the object when it appears in global search results. This is helpful for conveying to the user additional information about an object.

To register one or more indexes with NetBox, define a list named `indexes` at the end of this file:

```python
indexes = [MyModelIndex]
```

!!! tip
    The path to the list of search indexes can be modified by setting `search_indexes` in the PluginConfig instance.

::: netbox.search.SearchIndex
