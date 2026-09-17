---
collection: "opensearch"
version: "2.19"
title: "Match phrase prefix"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/full-text/match-phrase-prefix.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/full-text/match-phrase-prefix.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/full-text/match-phrase-prefix/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/full-text/match-phrase-prefix/"
canonical_route: "/query-dsl/full-text/match-phrase-prefix/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Full-text queries"
---
# Match phrase prefix query

Use the `match_phrase_prefix` query to specify a phrase to match in order. The documents that contain the phrase you specify will be returned. The last partial term in the phrase is interpreted as a prefix, so any documents that contain phrases that begin with the phrase and prefix of the last term will be returned.

Similar to [match phrase](../match-phrase/index.md), but creates a [prefix query](https://lucene.apache.org/core/8_9_0/core/org/apache/lucene/search/PrefixQuery.html) out of the last term in the query string.

For differences between the `match_phrase_prefix` and the `match_bool_prefix` queries, see [The `match_bool_prefix` and `match_phrase_prefix` queries](../match-bool-prefix/index.md#the-match_bool_prefix-and-match_phrase_prefix-queries).

The following example shows a basic `match_phrase_prefix` query:

```json
GET _search
{
  "query": {
    "match_phrase_prefix": {
      "title": "the wind"
    }
  }
}
```

To pass additional parameters, you can use the expanded syntax:

```json
GET _search
{
  "query": {
    "match_phrase_prefix": {
      "title": {
        "query": "the wind",
        "analyzer": "stop"
      }
    }
  }
}
```

## Example

For example, consider an index with the following documents:

```json
PUT testindex/_doc/1
{
  "title": "The wind rises"
}
```

```json
PUT testindex/_doc/2
{
  "title": "Gone with the wind"

}
```

The following `match_phrase_prefix` query searches for the whole word `wind`, followed by a word that starts with `ri`:

```json
GET testindex/_search
{
  "query": {
    "match_phrase_prefix": {
      "title": "wind ri"
    }
  }
}
```

The response contains the matching document:

<details markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "took": 6,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 0.92980814,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": 0.92980814,
        "_source": {
          "title": "The wind rises"
        }
      }
    ]
  }
}
```
</details>

## Parameters

The query accepts the name of the field (`<field>`) as a top-level parameter:

```json
GET _search
{
  "query": {
    "match_phrase": {
      "<field>": {
        "query": "text to search for",
        ...
      }
    }
  }
}
```

The `<field>` accepts the following parameters. All parameters except `query` are optional.

Parameter | Data type | Description
:--- | :--- | :---
`query` | String | The query string to use for search. Required.
`analyzer` | String | The [analyzer](../../../analyzers/index.md) used to tokenize the query.
`max_expansions` | Positive integer |  The maximum number of terms to which the query can expand. Fuzzy queries “expand to” a number of matching terms that are within the distance specified in `fuzziness`. Then OpenSearch tries to match those terms. Default is `50`.
`slop` | `0` (default) or a positive integer | Controls the degree to which words in a query can be misordered and still be considered a match. From the [Lucene documentation](https://lucene.apache.org/core/8_9_0/core/org/apache/lucene/search/PhraseQuery.html#getSlop--): "The number of other words permitted between words in query phrase. For example, to switch the order of two words requires two moves (the first move places the words atop one another), so to permit reorderings of phrases, the slop must be at least two. A value of zero requires an exact match."
