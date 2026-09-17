---
collection: "opensearch"
version: "2.19"
title: "Supported units"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/units.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/units.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/units/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/units/"
canonical_route: "/api-reference/units/"
redirect_from: ["/opensearch/units/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 90
---
# Supported units
**Introduced 1.0**
{: .label .label-purple }

OpenSearch supports the following units for all REST operations:

Unit | Description | Example
:--- | :--- | :---
Times | The supported units for time are `d` for days, `h` for hours, `m` for minutes, `s` for seconds, `ms` for milliseconds, `micros` for microseconds, and `nanos` for nanoseconds. | `5d` or `7h`
Bytes | The supported units for byte size are `b` for bytes, `kb` for kibibytes, `mb` for mebibytes, `gb` for gibibytes, `tb` for tebibytes, and `pb` for pebibytes. Despite the base-10 abbreviations, these units are base-2; `1kb` is 1,024 bytes, `1mb` is 1,048,576 bytes, etc. | `7kb` or `6gb`
Distances | The supported units for distance are `mi` for miles, `yd` for yards, `ft` for feet, `in` for inches, `km` for kilometers, `m` for meters, `cm` for centimeters, `mm` for millimeters, and `nmi` or `NM` for nautical miles. | `5mi` or `4ft`
Quantities without units | For large values that don't have a unit, use `k` for kilo, `m` for mega, `g` for giga, `t` for tera, and `p` for peta. | `5k` for 5,000

To convert output units to human-readable values, see [Common REST parameters](../common-parameters/index.md).
