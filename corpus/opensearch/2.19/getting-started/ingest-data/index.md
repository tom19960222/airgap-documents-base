---
collection: "opensearch"
version: "2.19"
title: "Ingest data"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_getting-started/ingest-data.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_getting-started/ingest-data.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/getting-started/ingest-data/"
canonical_url: "https://docs.opensearch.org/latest/getting-started/ingest-data/"
canonical_route: "/getting-started/ingest-data/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
---
# Ingest your data into OpenSearch

There are several ways to ingest data into OpenSearch:

- Ingest individual documents. For more information, see [Indexing documents](../communicate/index.md#indexing-documents).
- Index multiple documents in bulk. For more information, see [Bulk indexing](#bulk-indexing).
- Use Data Prepper---an OpenSearch server-side data collector that can enrich data for downstream analysis and visualization. For more information, see [Data Prepper](https://docs.opensearch.org/latest/data-prepper/) <!-- unresolved-jekyll-link: route=/data-prepper/ -->.
- Use other ingestion tools. For more information, see [OpenSearch tools](../../tools/index.md).

## Bulk indexing

To index documents in bulk, you can use the [Bulk API](../../api-reference/document-apis/bulk/index.md). For example, if you want to index several documents into the `students` index, send the following request:

```json
POST _bulk
{ "create": { "_index": "students", "_id": "2" } }
{ "name": "Jonathan Powers", "gpa": 3.85, "grad_year": 2025 }
{ "create": { "_index": "students", "_id": "3" } }
{ "name": "Jane Doe", "gpa": 3.52, "grad_year": 2024 }
```

## Experiment with sample data

OpenSearch provides a fictitious e-commerce dataset that you can use to experiment with REST API requests and OpenSearch Dashboards visualizations. You can create an index and define field mappings by downloading the corresponding dataset and mapping files.

### Create a sample index

Use the following steps to create a sample index and define field mappings for the document fields:

1. Download [ecommerce-field_mappings.json](https://github.com/opensearch-project/documentation-website/blob/2.19/assets/examples/ecommerce-field_mappings.json). This file defines a [mapping](../../field-types/index.md) for the sample data you will use.

    To use cURL, send the following request:

    ```bash
    curl -O https://raw.githubusercontent.com/opensearch-project/documentation-website/2.19/assets/examples/ecommerce-field_mappings.json
    ```

    To use wget, send the following request:

    ```
    wget https://raw.githubusercontent.com/opensearch-project/documentation-website/2.19/assets/examples/ecommerce-field_mappings.json
    ```

1. Download [ecommerce.ndjson](https://github.com/opensearch-project/documentation-website/blob/2.19/assets/examples/ecommerce.ndjson). This file contains the index data formatted so that it can be ingested by the Bulk API:

    To use cURL, send the following request:

    ```bash
    curl -O https://raw.githubusercontent.com/opensearch-project/documentation-website/2.19/assets/examples/ecommerce.ndjson
    ```

    To use wget, send the following request:

    ```
    wget https://raw.githubusercontent.com/opensearch-project/documentation-website/2.19/assets/examples/ecommerce.ndjson
    ```

1. Define the field mappings provided in the mapping file:
    ```bash
    curl -H "Content-Type: application/json" -X PUT "https://localhost:9200/ecommerce" -ku admin:<custom-admin-password> --data-binary "@ecommerce-field_mappings.json"
    ```

1. Upload the documents using the Bulk API:

    ```bash
    curl -H "Content-Type: application/x-ndjson" -X PUT "https://localhost:9200/ecommerce/_bulk" -ku admin:<custom-admin-password> --data-binary "@ecommerce.ndjson"
    ```

### Query the data

Query the data using the Search API. The following query searches for documents in which `customer_first_name` is `Sonya`:

```json
GET ecommerce/_search
{
  "query": {
    "match": {
      "customer_first_name": "Sonya"
    }
  }
}
```

### Visualize the data

To learn how to use OpenSearch Dashboards to visualize the data, see the [OpenSearch Dashboards quickstart guide](https://docs.opensearch.org/latest/dashboards/quickstart/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/quickstart/ -->.

## Further reading

- For information about Data Prepper, see [Data Prepper](https://docs.opensearch.org/latest/data-prepper/) <!-- unresolved-jekyll-link: route=/data-prepper/ -->.
- For information about ingestion tools, see [OpenSearch tools](../../tools/index.md).
- For information about OpenSearch Dashboards, see [OpenSearch Dashboards quickstart guide](https://docs.opensearch.org/latest/dashboards/quickstart/) <!-- unresolved-cross-corpus-link: collection=opensearch-dashboards route=/dashboards/quickstart/ -->.
- For information about bulk indexing, see [Bulk API](../../api-reference/document-apis/bulk/index.md).

## Next steps

- See [Search your data](../search-data/index.md) to learn about search options.
