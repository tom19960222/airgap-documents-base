---
collection: "opensearch"
version: "2.19"
title: "Optimizing vector storage"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_vector-search/optimizing-storage/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_vector-search/optimizing-storage/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/vector-search/optimizing-storage/"
canonical_url: "https://docs.opensearch.org/latest/vector-search/optimizing-storage/index/"
canonical_route: "/vector-search/optimizing-storage/"
redirect_from: ["/vector-search/optimizing-storage/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 60
storage_cards: [{"heading":"Vector quantization","description":"Reduce vector storage space by quantizing vectors","link":"/vector-search/optimizing-storage/knn-vector-quantization/"},{"heading":"Disk-based vector search","description":"Uses binary quantization to reduce the operational costs of vector workloads","link":"/vector-search/optimizing-storage/disk-based-vector-search/"}]
---
# Optimizing vector storage

Vector search operations can be resource intensive, especially when dealing with large-scale vector datasets. OpenSearch provides several optimization techniques for reducing memory usage.

<div class="card-container">

- [Vector quantization](knn-vector-quantization/index.md)
  Reduce vector storage space by quantizing vectors

- [Disk-based vector search](disk-based-vector-search/index.md)
  Uses binary quantization to reduce the operational costs of vector workloads

</div>
