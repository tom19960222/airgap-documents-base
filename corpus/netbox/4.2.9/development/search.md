---
collection: netbox
version: "4.2.9"
title: "Search"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/development/search.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Search

NetBox v3.4 introduced a new global search mechanism, which employs the `extras.CachedValue` model to store discrete field values from many models in a single table.

## SearchIndex

To enable search support for a model, declare and register a subclass of `netbox.search.SearchIndex` for it. Typically, this will be done within an app's `search.py` module.

```python
from netbox.search import SearchIndex, register_search

@register_search
class MyModelIndex(SearchIndex):
    model = MyModel
    fields = (
        ('name', 100),
        ('description', 500),
        ('comments', 5000),
    )
    display_attrs = ('site', 'device', 'status', 'description')
```

A SearchIndex subclass defines both its model and a list of two-tuples specifying which model fields to be indexed and the weight (precedence) associated with each. Guidance on weight assignment for fields is provided below.

### Field Weight Guidance

| Weight | Field Role                                       | Examples                                           |
|--------|--------------------------------------------------|----------------------------------------------------|
| 50     | Unique serialized attribute                      | Device.asset_tag                                   |
| 60     | Unique serialized attribute (per related object) | Device.serial                                      |
| 100    | Primary human identifier                         | Device.name, Circuit.cid, Cable.label              |
| 110    | Slug                                             | Site.slug                                          |
| 200    | Secondary identifier                             | ProviderAccount.account, DeviceType.part_number    |
| 300    | Highly unique descriptive attribute              | CircuitTermination.xconnect_id, IPAddress.dns_name |
| 500    | Description                                      | Site.description                                   |
| 1000   | Custom field default                             | -                                                  |
| 2000   | Other discrete attribute                         | CircuitTermination.port_speed                      |
| 5000   | Comment field                                    | Site.comments                                      |
