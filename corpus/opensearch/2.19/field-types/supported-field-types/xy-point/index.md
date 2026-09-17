---
collection: "opensearch"
version: "2.19"
title: "xy point"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/xy-point.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/xy-point.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/xy-point/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/xy-point/"
canonical_route: "/mappings/supported-field-types/xy-point/"
redirect_from: ["/opensearch/supported-field-types/xy-point/","/field-types/xy-point/","/mappings/supported-field-types/xy-point/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Supported field types"
has_children: false
layout: "default"
nav_order: 58
parent: "Cartesian field types"
---
# xy point field type
**Introduced 2.4**
{: .label .label-purple }

An xy point field type contains a point in a two-dimensional Cartesian coordinate system, specified by x and y coordinates. It is based on the Lucene [XYPoint](https://lucene.apache.org/core/9_3_0/core/org/apache/lucene/geo/XYPoint.html) field type. The xy point field type is similar to the [geopoint](../geo-point/index.md) field type, but does not have the range limitations of geopoint. The coordinates of an xy point are single-precision floating-point values. For information about the range and precision of floating-point values, see [Numeric field types](../numeric/index.md).

## Example

Create a mapping with an xy point field type:

```json
PUT testindex1
{
  "mappings": {
    "properties": {
      "point": {
        "type": "xy_point"
      }
    }
  }
}
```

## Formats

xy points can be indexed in the following formats:

- An object with x and y coordinates

```json
PUT testindex1/_doc/1
{
  "point": {
    "x": 0.5,
    "y": 4.5
  }
}
```

- A string in the "`x`, `y`" format

```json
PUT testindex1/_doc/2
{
  "point": "0.5, 4.5"
}
```

- An array in the [`x`, `y`] format

```json
PUT testindex1/_doc/3
{
  "point": [0.5, 4.5]
}
```

- A [well-known text (WKT)](https://docs.opengeospatial.org/is/12-063r5/12-063r5.html) POINT in the "POINT(`x` `y`)" format

```json
PUT testindex1/_doc/4
{
  "point": "POINT (0.5 4.5)"
}
```

- GeoJSON format

```json
PUT testindex1/_doc/5
{
  "point" : {
    "type" : "Point",
    "coordinates" : [0.5, 4.5]
  }
}
```

In all xy point formats, the coordinates must be specified in the `x, y` order.
{: .note}

## Parameters

The following table lists the parameters accepted by xy point field types. All parameters are optional.

Parameter | Description
:--- | :---
`ignore_malformed` | A Boolean value that specifies to ignore malformed values and not to throw an exception. Default is `false`.
`ignore_z_value` | Specific to points with three coordinates. If `ignore_z_value` is `true`, the third coordinate is not indexed but is still stored in the _source field. If `ignore_z_value` is `false`, an exception is thrown.
[`null_value`](../index.md#null-value) | A  value to be used in place of `null`. The value must be of the same type as the field. If this parameter is not specified, the field is treated as missing when its value is `null`. Default is `null`.
