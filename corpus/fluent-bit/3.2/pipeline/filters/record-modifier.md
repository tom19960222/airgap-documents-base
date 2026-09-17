---
collection: fluent-bit
version: "3.2"
title: "Record Modifier"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/filters/record-modifier.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Record Modifier

The _Record Modifier_ [filter](pipeline/filters.md) <!-- unresolved-source-link: target=pipeline/filters.md --> plugin lets you append
fields to a record, or exclude specific fields.

## Configuration parameters

The plugin supports the following configuration parameters:

| Key | Description |
| :--- | :--- |
| `Record` | Append fields. This parameter needs a key/value pair. |
| `Remove_key` | If the key is matched, that field is removed. You can this or `Allowlist_key`.|
| `Allowlist_key` | If the key isn't matched, that field is removed. You can this or `Remove_key`. |
| `Whitelist_key` | An alias of `Allowlist_key` for backwards compatibility. |
| `Uuid_key` | If set, the plugin appends Uuid to each record. The value assigned becomes the key in the map. |

## Get started

To start filtering records, run the filter from the command line or through a
configuration file.

This is a sample `in_mem` record to filter.

```text
{"Mem.total"=>1016024, "Mem.used"=>716672, "Mem.free"=>299352, "Swap.total"=>2064380, "Swap.used"=>32656, "Swap.free"=>2031724}
```

### Append fields

The following configuration file appends a product name and hostname to a record
using an environment variable:

**Tab: fluent-bit.conf**

```python copy
[INPUT]
    Name mem
    Tag  mem.local

[OUTPUT]
    Name  stdout
    Match *

[FILTER]
    Name record_modifier
    Match *
    Record hostname ${HOSTNAME}
    Record product Awesome_Tool
```

**Tab: fluent-bit.yaml**

```yaml copy
pipeline:
    inputs:
        - name: mem
          tag: mem.local
    filters:
        - name: record_modifier
          match: '*'
          record:
             - hostname ${HOSTNAME}
             - product Awesome_Tool
    outputs:
        - name: stdout
          match: '*'
```

You can run the filter from command line:

```shell copy
fluent-bit -i mem -o stdout -F record_modifier -p 'Record=hostname ${HOSTNAME}' -p 'Record=product Awesome_Tool' -m '*'
```

The output looks something like:

```python copy
[0] mem.local: [1492436882.000000000, {"Mem.total"=>1016024, "Mem.used"=>716672, "Mem.free"=>299352, "Swap.total"=>2064380, "Swap.used"=>32656, "Swap.free"=>2031724, "hostname"=>"localhost.localdomain", "product"=>"Awesome_Tool"}]
```

### Remove fields with `Remove_key`

The following configuration file removes `Swap.*` fields:

**Tab: fluent-bit.conf**

```python copy
[INPUT]
    Name mem
    Tag  mem.local

[OUTPUT]
    Name  stdout
    Match *

[FILTER]
    Name record_modifier
    Match *
    Remove_key Swap.total
    Remove_key Swap.used
    Remove_key Swap.free
```

**Tab: fluent-bit.yaml**

```yaml copy
pipeline:
    inputs:
        - name: mem
          tag: mem.local
    filters:
        - name: record_modifier
          match: '*'
          remove_key:
             - Swap.total
             - Swap.used
             - Swap.free
    outputs:
        - name: stdout
          match: '*'
```

You can also run the filter from command line.

```shell copy
fluent-bit -i mem -o stdout -F  record_modifier -p 'Remove_key=Swap.total' -p 'Remove_key=Swap.free' -p 'Remove_key=Swap.used' -m '*'
```

The output looks something like:

```python
[0] mem.local: [1492436998.000000000, {"Mem.total"=>1016024, "Mem.used"=>716672, "Mem.free"=>295332}]
```

### Retain fields with `Allowlist_key`

The following configuration file retains `Mem.*` fields.

**Tab: fluent-bit.conf**

```python copy
[INPUT]
    Name mem
    Tag  mem.local

[OUTPUT]
    Name  stdout
    Match *

[FILTER]
    Name record_modifier
    Match *
    Allowlist_key Mem.total
    Allowlist_key Mem.used
    Allowlist_key Mem.free
```

**Tab: fluent-bit.yaml**

```yaml copy
pipeline:
    inputs:
        - name: mem
          tag: mem.local
    filters:
        - name: record_modifier
          match: '*'
          Allowlist_key:
             - Mem.total
             - Mem.used
             - Mem.free
    outputs:
        - name: stdout
          match: '*'
```

You can also run the filter from command line:

```shell copy
fluent-bit -i mem -o stdout -F record_modifier -p 'Allowlist_key=Mem.total' -p 'Allowlist_key=Mem.free' -p 'Allowlist_key=Mem.used' -m '*'
```

The output looks something like:

```python
[0] mem.local: [1492436998.000000000, {"Mem.total"=>1016024, "Mem.used"=>716672, "Mem.free"=>295332}]
```
