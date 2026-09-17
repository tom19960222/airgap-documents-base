---
collection: "opensearch"
version: "2.19"
title: "Query DSL"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/"
canonical_route: "/query-dsl/"
redirect_from: ["/opensearch/query-dsl/","/docs/opensearch/query-dsl/","/query-dsl/query-dsl/","/query-dsl/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_exclude: true
nav_order: 2
---
# Query DSL

OpenSearch provides a search language called *query domain-specific language (DSL)* that you can use to search your data. Query DSL is a flexible language with a JSON interface.

With query DSL, you need to specify a query in the `query` parameter of the search. One of the simplest searches in OpenSearch uses the `match_all` query, which matches all documents in an index:

```json
GET testindex/_search
{
  "query": {
     "match_all": {
     }
  }
}
```

A query can consist of many query clauses. You can combine query clauses to produce complex queries.

Broadly, you can classify queries into two categories---*leaf queries* and *compound queries*:

- **Leaf queries**: Leaf queries search for a specified value in a certain field or fields. You can use leaf queries on their own. They include the following query types:

    - [Full-text queries](full-text/index.md): Use full-text queries to search text documents. For an analyzed text field search, full-text queries split the query string into terms using the same analyzer that was used when the field was indexed. For an exact value search, full-text queries look for the specified value without applying text analysis.

    - [Term-level queries](term/index.md): Use term-level queries to search documents for an exact term, such as an ID or value range. Term-level queries do not analyze search terms or sort results by relevance score.

    - [Geographic and xy queries](geo-and-xy/index.md): Use geographic queries to search documents that include geographic data. Use xy queries to search documents that include points and shapes in a two-dimensional coordinate system.

    - Joining queries: Use joining queries to search nested fields or return parent and child documents that match a specific query. Types of joining queries include `nested`, `has_child`, `has_parent`, and `parent_id` queries.

    - [Span queries](span/index.md): Use span queries to perform precise positional searches. Span queries are low-level, specific queries that provide control over the order and proximity of specified query terms. They are primarily used to search legal documents.

    - [Specialized queries](specialized/index.md): Specialized queries include all other query types (`distance_feature`, `more_like_this`, `percolate`, `rank_feature`, `script`, `script_score`, and `wrapper`).

- **Compound queries**: Compound queries serve as wrappers for multiple leaf or compound clauses, either to combine their results or to modify their behavior. They include the Boolean, disjunction max, constant score, function score, and boosting query types. To learn more, see [Compound queries](compound/index.md).

## A note on Unicode special characters in text fields

Because of word boundaries associated with Unicode special characters, the Unicode standard analyzer cannot index a [text field type](../field-types/supported-field-types/text/index.md) value as a whole value when it includes one of these special characters. As a result, a text field value that includes a special character is parsed by the standard analyzer as multiple values separated by the special character, effectively tokenizing the different elements on either side of it. This can lead to unintentional filtering of documents and potentially compromise control over their access.

The following examples illustrate values containing special characters that will be parsed improperly by the standard analyzer. In this example, the existence of the hyphen/minus sign in the value prevents the analyzer from distinguishing between the two different users for `user.id` and interprets them as being one and the same:

```json
{
  "bool": {
    "must": {
      "match": {
        "user.id": "User-1"
      }
    }
  }
}
```

```json
{
  "bool": {
    "must": {
      "match": {
        "user.id": "User-2"
      }
    }
  }
}
```

To avoid this circumstance when using either query DSL or the REST API, you can use a custom analyzer or map the field as `keyword`, which performs an exact-match search. See [Keyword field type](../field-types/supported-field-types/keyword/index.md) for the latter option.

For a list of characters that should be avoided when using `text` field types, see [Word Boundaries](https://unicode.org/reports/tr29/#Word_Boundaries).

## Expensive queries

Expensive queries can consume a lot of memory and lead to a decline in cluster performance. The following queries may be resource consuming:

- [`fuzzy`](term/fuzzy/index.md) queries
- [`prefix`](term/prefix/index.md) queries
- [`range`](term/range/index.md) queries on [`text`](../field-types/supported-field-types/text/index.md) and [`keyword`](../field-types/supported-field-types/keyword/index.md) fields
- [`regexp`](term/regexp/index.md) queries
- [`wildcard`](term/wildcard/index.md) queries
- [`query_string`](full-text/query-string/index.md) queries that are internally transformed into prefix queries

To disallow expensive queries, you can disable the `search.allow_expensive_queries` cluster setting as follows:

```json
PUT _cluster/settings
{
  "persistent": {
    "search.allow_expensive_queries": false
  }
}
```

To track expensive queries, enable [shard slow logs](../install-and-configure/configuring-opensearch/logs/index.md#shard-slow-logs).
{: .tip}
