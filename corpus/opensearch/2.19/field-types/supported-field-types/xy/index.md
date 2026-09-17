---
collection: "opensearch"
version: "2.19"
title: "Cartesian field types"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/xy.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/xy.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/xy/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/xy/"
canonical_route: "/mappings/supported-field-types/xy/"
redirect_from: ["/opensearch/supported-field-types/xy/","/field-types/xy/","/mappings/supported-field-types/xy/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 57
parent: "Supported field types"
---
# Cartesian field types

Cartesian field types facilitate indexing and searching of points and shapes in a two-dimensional Cartesian coordinate system. Cartesian field types are similar to [geographic](../geographic/index.md) field types, except they represent points and shapes on the Cartesian plane, which is not based on the Earth-fixed terrestrial reference system. Calculating distances on a plane is more efficient than calculating distances on a sphere, so distance sorting is faster for Cartesian field types.

Cartesian field types work well for spatial applications like virtual reality, computer-aided design (CAD), and amusement park and sporting venue mapping.

The coordinates for the Cartesian field types are single-precision floating-point values. For information about the range and precision of floating-point values, see [Numeric field types](../numeric/index.md).

The following table lists all Cartesian field types that OpenSearch supports.

Field Data type | Description
:--- | :---
[`xy_point`](../xy-point/index.md) | A point in a two-dimensional Cartesian coordinate system, specified by x and y coordinates.
[`xy_shape`](../xy-shape/index.md) | A shape, such as a polygon or a collection of xy points, in a two-dimensional Cartesian coordinate system.

Currently, OpenSearch supports indexing and searching of Cartesian field types but not aggregations on Cartesian field types. If you'd like to see aggregations implemented, open a [GitHub issue](https://github.com/opensearch-project/geospatial).
{: .note}
