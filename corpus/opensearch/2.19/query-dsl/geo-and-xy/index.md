---
collection: "opensearch"
version: "2.19"
title: "Geographic and xy queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/geo-and-xy/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/geo-and-xy/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/geo-and-xy/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/geo-and-xy/index/"
canonical_route: "/query-dsl/geo-and-xy/"
redirect_from: ["/opensearch/query-dsl/geo-and-xy/index/","/query-dsl/query-dsl/geo-and-xy/","/query-dsl/geo-and-xy/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 50
---
# Geographic and xy queries

Geographic and xy queries let you search fields that contain points and shapes on a map or coordinate plane. Geographic queries work on geospatial data, while xy queries work on two-dimensional coordinate data. Out of all geographic queries, the geoshape query is very similar to the xy query, but the former searches [geographic fields](../../field-types/supported-field-types/geographic/index.md), while the latter searches [Cartesian fields](../../field-types/supported-field-types/xy/index.md).

## xy queries

[xy queries](xy/index.md) search for documents that contain geometries in a Cartesian coordinate system. These geometries can be specified in [`xy_point`](../../field-types/supported-field-types/xy-point/index.md) fields, which support points, and [`xy_shape`](../../field-types/supported-field-types/xy-shape/index.md) fields, which support points, lines, circles, and polygons.

xy queries return documents that contain:
- xy shapes and xy points that have one of four spatial relations to the provided shape: `INTERSECTS`, `DISJOINT`, `WITHIN`, or `CONTAINS`.
- xy points that intersect the provided shape.

## Geographic queries

Geographic queries search for documents that contain geospatial geometries. These geometries can be specified in [`geo_point`](../../field-types/supported-field-types/geo-point/index.md) fields, which support points on a map, and [`geo_shape`](../../field-types/supported-field-types/geo-shape/index.md) fields, which support points, lines, circles, and polygons.

OpenSearch provides the following geographic query types:

- [**Geo-bounding box queries**](geo-bounding-box/index.md): Return documents with geopoint field values that are within a bounding box.
- [**Geodistance queries**](geodistance/index.md): Return documents with geopoints that are within a specified distance from the provided geopoint.
- [**Geopolygon queries**](geopolygon/index.md): Return documents containing geopoints that are within a polygon.
- [**Geoshape queries**](geoshape/index.md): Return documents that contain:
    - Geoshapes and geopoints that have one of four spatial relations to the provided shape: `INTERSECTS`, `DISJOINT`, `WITHIN`, or `CONTAINS`.
    - Geopoints that intersect the provided shape.
