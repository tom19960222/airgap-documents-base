---
collection: "opensearch"
version: "2.19"
title: "ISM Error Prevention"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/ism/error-prevention/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/ism/error-prevention/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/ism/error-prevention/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/ism/error-prevention/index/"
canonical_route: "/im-plugin/ism/error-prevention/"
redirect_from: ["/im-plugin/ism/error-prevention/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 90
---
# ISM error prevention

Error prevention validates Index State Management (ISM) actions before they are performed in order to prevent actions from failing. It also outputs additional information from the action validation results in the response of the [Index Explain API](../api/index.md#explain-index). Validation rules and troubleshooting of each action are listed in the following sections.

---

#### Table of contents
1. TOC
<!-- local-toc -->
---

## rollover

ISM does not perform a `rollover` action for an index under any of these conditions:

- [The index is not the write index](resolutions/index.md#the-index-is-not-the-write-index).
- [The index does not have an alias](resolutions/index.md#the-index-does-not-have-an-alias).
- [The rollover policy does not contain a rollover_alias index setting](resolutions/index.md#the-rollover-policy-misses-rollover_alias-index-setting).
- [Skipping of a rollover action has occured](resolutions/index.md#skipping-rollover-action-is-true).
- [The index has already been rolled over using the alias successfully](resolutions/index.md#this-index-has-already-been-rolled-over-successfully).

## delete

ISM does not perform a `delete` action for an index under any of these conditions:

- The index does not exist.
- The index name is invalid.
- The index is the write index for a data stream.

## force_merge

ISM does not perform a `force_merge` action for an index if its dataset is too large and exceeds the threshold.

## replica_count

ISM does not perform a `replica_count` action for an index under any of these conditions:

- The amount of data exceeds the threshold.
- The number of shards exceeds the maximum.

## open

ISM does not perform an `open` action for an index under any of these conditions:

- The index is blocked.
- The number of shards exceeds the maximum.

## read_only

ISM does not perform a `read_only` action for an index under any of these conditions:

- The index is blocked.
- The amount of data exceeds the threshold.

## read_write

ISM does not perform a `read_write` action for an index if the index is blocked.

## close

ISM does not perform a `close` action for an index under any of these conditions:

- The index does not exist.
- The index name is invalid.

## index_priority

ISM does not perform an `index_priority` action for an index that does not have `read-only-allow-delete` permission.

## snapshot

ISM does not perform a `snapshot` action for an index under any of these conditions:

- The index does not exist.
- The index name is invalid.

## transition

ISM does not perform a `transition` action for an index under any of these conditions:

- The index does not exist.
- The index name is invalid.
