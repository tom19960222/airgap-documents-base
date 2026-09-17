---
collection: "opensearch"
version: "2.19"
title: "Phone number analyzers"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/phone-analyzers.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/phone-analyzers.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/phone-analyzers/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/phone-analyzers/"
canonical_route: "/analyzers/supported-analyzers/phone-analyzers/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 140
parent: "Analyzers"
---
# Phone number analyzers

The `analysis-phonenumber` plugin provides analyzers and tokenizers for parsing phone numbers. A dedicated analyzer is required because parsing phone numbers is a non-trivial task (even though it might seem trivial at first glance). For common misconceptions regarding phone number parsing, see [Falsehoods programmers believe about phone numbers](https://github.com/google/libphonenumber/blob/master/FALSEHOODS.md).

OpenSearch supports the following phone number analyzers:

* [`phone`](#the-phone-analyzer): An [index analyzer](../../index-analyzers/index.md) to use at indexing time.
* [`phone-search`](#the-phone-search-analyzer): A [search analyzer](../../search-analyzers/index.md) to use at search time.

Internally, the plugin uses the [`libphonenumber`](https://github.com/google/libphonenumber) library and follows its parsing rules.

The phone number analyzers are not meant to find phone numbers in larger texts. Instead, you should use them on fields that only contain phone numbers.
{: .note}

## Installing the plugin

Before you can use the phone number analyzers, you must install the `analysis-phonenumber` plugin by running the following command:

```sh
./bin/opensearch-plugin install analysis-phonenumber
```

## Specifying a default region

You can optionally specify a default region for parsing phone numbers by providing the `phone-region` parameter within the analyzer. Valid phone regions are represented by ISO 3166 country codes. For more information, see [List of ISO 3166 country codes](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes).

When tokenizing phone numbers containing the international calling prefix `+`, the default region is irrelevant. However, for phone numbers that use a national prefix for international numbers (for example, `001` instead of `+1` to dial Northern America from most European countries), the region needs to be provided. You can also properly index local phone numbers with no international prefix by specifying the region.

## Example

The following request creates an index containing one field that ingests phone numbers for Switzerland (region code `CH`):

```json
PUT /example-phone
{
  "settings": {
    "analysis": {
      "analyzer": {
        "phone-ch": {
          "type": "phone",
          "phone-region": "CH"
        },
        "phone-search-ch": {
          "type": "phone-search",
          "phone-region": "CH"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "phone_number": {
        "type": "text",
        "analyzer": "phone-ch",
        "search_analyzer": "phone-search-ch"
      }
    }
  }
}
```

## The phone analyzer

The `phone` analyzer generates n-grams based on the given phone number. A (fictional) Swiss phone number containing an international calling prefix can be parsed with or without the Swiss-specific phone region. Thus, the following two requests will produce the same result:

```json
GET /example-phone/_analyze
{
  "analyzer" : "phone-ch",
  "text" : "+41 60 555 12 34"
}
```

```json
GET /example-phone/_analyze
{
  "analyzer" : "phone",
  "text" : "+41 60 555 12 34"
}
```

The response contains the generated n-grams:

```json
["+41 60 555 12 34", "6055512", "41605551", "416055512", "6055", "41605551234", ...]
```

However, if you specify the phone number without the international calling prefix `+` (either by using `0041` or omitting
the international calling prefix altogether), then only the analyzer configured with the correct phone region can parse the number:

```json
GET /example-phone/_analyze
{
  "analyzer" : "phone-ch",
  "text" : "060 555 12 34"
}
```

## The phone-search analyzer

In contrast, the `phone-search` analyzer does not create n-grams and only issues some basic tokens. For example, send the following request and specify the `phone-search` analyzer:

```json
GET /example-phone/_analyze
{
  "analyzer" : "phone-search",
  "text" : "+41 60 555 12 34"
}
```

The response contains the following tokens:

```json
["+41 60 555 12 34", "41 60 555 12 34", "41605551234", "605551234", "41"]
```
