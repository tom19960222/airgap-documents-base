---
collection: fluent-bit
version: "3.2"
title: "Changelog"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/stream-processing/changelog.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Changelog

Upon new versions of [Fluent Bit](https://fluentbit.io), the Stream Processor engine gets new improvements. In the following section you will find the details of the new additions in the major release versions.

## Fluent Bit v1.2

> Release date: June 27, 2019

### Sub-key selection and conditionals support

It's pretty common that records contains nested maps or sub-keys. Now we provide the ability to use sub-keys to perform conditionals and keys selection. Consider the following record:

```javascript
{
  "key1": 123,
  "key2": 456,
  "key3": {
    "sub1": {
      "sub2": 789
    }
  }
}
```

Now you can perform queries like:

```sql
SELECT key3['sub1']['sub2'] FROM STREAM:test WHERE key3['sub1']['sub2'] = 789;
```

### New @record functions

On conditionals we have introduced the new _@record_ functions:

| Function | Description |
| :--- | :--- |
| @record.time\(\) | returns the record timestamp |
| @record.contains\(key\) | returns true or false if _key_ exists in the record |

### IS NULL, IS NOT NULL

We currently support different data types such as _strings_, _integers_, _floats_, _maps_ and _null_. In Fluent Bit, a _null_ value is totally valid and is not related to the absence of a value as in normal databases. To compare if an existing key in the record have a _null_ value or not, we have introduced _IS NULL_ and _IS NOT NULL_ statements, e.g:

```sql
SELECT * FROM STREAM:test WHERE key3['sub1'] IS NOT NULL;
```

For more details please review the section [Check Keys and NULL values](getting-started/check-keys-null-values.md)

## Fluent Bit v1.1

> Release date: May 09, 2019

This is the initial version of the Stream Processor into Fluent Bit.
