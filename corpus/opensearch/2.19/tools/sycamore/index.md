---
collection: "opensearch"
version: "2.19"
title: "Sycamore"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tools/sycamore.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tools/sycamore.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tools/sycamore/"
canonical_url: "https://docs.opensearch.org/latest/tools/sycamore/"
canonical_route: "/tools/sycamore/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 210
---
# Sycamore

[Sycamore](https://github.com/aryn-ai/sycamore) is an open-source, AI-powered document processing engine designed to prepare unstructured data for retrieval-augmented generation (RAG) and semantic search using Python. Sycamore supports chunking and enriching a wide range of complex document types, including reports, presentations, transcripts, and manuals. Additionally, Sycamore can extract and process embedded elements, such as tables, figures, graphs, and other infographics. It can then load the data into target indexes, including vector and keyword indexes, using a connector like the [OpenSearch connector](https://sycamore.readthedocs.io/en/stable/sycamore/connectors/opensearch.html).

To get started, visit the [Sycamore documentation](https://sycamore.readthedocs.io/en/stable/sycamore/get_started.html).

## Sycamore ETL pipeline structure

A Sycamore extract, transform, load (ETL) pipeline applies a series of transformations to a [DocSet](https://sycamore.readthedocs.io/en/stable/sycamore/get_started/concepts.html#docsets), which is a collection of documents and their constituent elements (for example, tables, blocks of text, or headers). At the end of the pipeline, the DocSet is loaded into OpenSearch vector and keyword indexes.

A typical pipeline for preparing unstructured data for vector or hybrid search in OpenSearch consists of the following steps:

* Read documents into a [DocSet](https://sycamore.readthedocs.io/en/stable/sycamore/get_started/concepts.html#docsets).
* [Partition documents](https://sycamore.readthedocs.io/en/stable/sycamore/transforms/partition.html) into structured JSON elements.
* Extract metadata and filter and clean data using [transforms](https://sycamore.readthedocs.io/en/stable/sycamore/APIs/docset.html).
* Create [chunks](https://sycamore.readthedocs.io/en/stable/sycamore/transforms/merge.html) from groups of elements.
* Embed the chunks using the model of your choice.
* [Load](https://sycamore.readthedocs.io/en/stable/sycamore/connectors/opensearch.html) the embeddings, metadata, and text into OpenSearch vector and keyword indexes.

For an example pipeline that uses this workflow, see [this notebook](https://github.com/aryn-ai/sycamore/blob/main/notebooks/opensearch_docs_etl.ipynb).

## Install Sycamore

We recommend installing the Sycamore library using `pip`. The connector for OpenSearch can be specified and installed using extras. For example:

```bash
pip install sycamore-ai[opensearch]
```

By default, Sycamore works with the Aryn Partitioning Service to process PDFs. To run inference locally for partitioning or embedding, install Sycamore with the `local-inference` extra as follows:

```bash
pip install sycamore-ai[opensearch,local-inference]
```

## Next steps

For more information, visit the [Sycamore documentation](https://sycamore.readthedocs.io/en/stable/sycamore/get_started.html).
