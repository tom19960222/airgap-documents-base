---
collection: "opensearch"
version: "2.19"
title: "Stemming"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/stemming.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/stemming.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/stemming/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/stemming/"
canonical_route: "/analyzers/stemming/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 140
---
# Stemming

Stemming is the process of reducing words to their root or base form, known as the _stem_. This technique ensures that different variations of a word are matched during search operations. For example, the words "running", "runner", and "ran" can all be reduced to the stem "run", allowing searches for any of these terms to return relevant results.

In natural language, words often appear in various forms because of conjugation, pluralization, or derivation. Stemming improves search operations in the following ways:

- **Improves search recall**: By matching different word forms to a common stem, stemming increases the number of relevant documents retrieved.
- **Reduces index size**: Storing only the stemmed versions of words can decrease the overall size of the search index.

Stemming is configured using token filters within [analyzers](../index.md#analyzers). An analyzer comprises the following components:

1. **Character filters**: Modify the stream of characters before tokenization.
2. **Tokenizer**: Splits text into tokens (typically, words).
3. **Token filters**: Modify tokens after tokenization, for example, by applying stemming.

## Stemming example using built-in token filters

To implement stemming, you can configure a built-in token filter such as a [`porter_stem`](../token-filters/porter-stem/index.md) or [`kstem`](../token-filters/kstem/index.md) filter.

The [Porter stemming algorithm](https://snowballstem.org/algorithms/porter/stemmer.html) is a common algorithmic stemmer used for the English language.

### Creating an index with a custom analyzer

The following example request creates a new index named `my_stemming_index` and configures an analyzer with the [`porter_stem`](../token-filters/porter-stem/index.md) token filter:

```json
PUT /my_stemming_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_stemmer_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "porter_stem"
          ]
        }
      }
    }
  }
}
```

This configuration comprises the following:

- The [`standard`](../tokenizers/standard/index.md) tokenizer splits text into terms based on word boundaries.
- The [`lowercase`](../token-filters/lowercase/index.md) filter converts all tokens to lowercase.
- The [`porter_stem`](../token-filters/porter-stem/index.md) filter reduces words to their root form.

### Testing the analyzer

To examine the stemming action, analyze a sample text using the previously configured custom analyzer:

```json
POST /my_stemming_index/_analyze
{
  "analyzer": "my_stemmer_analyzer",
  "text": "The runners are running swiftly."
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "the",
      "start_offset": 0,
      "end_offset": 3,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "runner",
      "start_offset": 4,
      "end_offset": 11,
      "type": "<ALPHANUM>",
      "position": 1
    },
    {
      "token": "ar",
      "start_offset": 12,
      "end_offset": 15,
      "type": "<ALPHANUM>",
      "position": 2
    },
    {
      "token": "run",
      "start_offset": 16,
      "end_offset": 23,
      "type": "<ALPHANUM>",
      "position": 3
    },
    {
      "token": "swiftli",
      "start_offset": 24,
      "end_offset": 31,
      "type": "<ALPHANUM>",
      "position": 4
    }
  ]
}
```

## Stemmer categories

You can configure stemmers belonging to the following two categories:

- [Algorithmic stemmers](index.md#algorithmic-stemmers)
- [Dictionary stemmers](index.md#dictionary-stemmers)

### Algorithmic stemmers

Algorithmic stemmers apply predefined rules to systematically strip affixes (prefixes and suffixes) from words, reducing them to their stems. The following token filters use algorithmic stemmers:

- [`porter_stem`](../token-filters/porter-stem/index.md): Applies the Porter stemming algorithm to remove common suffixes and reduce words to their stems. For example, "running" becomes "run".

- [`kstem`](../token-filters/kstem/index.md): A lightweight stemmer designed for the English langugage that combines algorithmic stemming with a built-in dictionary. It reduces plurals to singulars, converts verb tenses to their base forms, and removes common derivational endings.

- [`stemmer`](../token-filters/stemmer/index.md): Provides algorithmic stemming for various languages, including English, with options for different stemming algorithms like `light_english`, `minimal_english`, and `porter2`.

- [`snowball`](../token-filters/snowball/index.md): Applies the Snowball algorithm to provide efficient and accurate stemming for multiple languages, including English, French, German, and others.

### Dictionary stemmers

Dictionary stemmers rely on extensive dictionaries to map words to their root forms, effectively stemming irregular words. They look up each word in a precompiled list to find its corresponding stem. This operation is more resource intensive but often yields better results for irregular words and words that might appear to have a similar stem but are very different in their meaning.

The most prominent example of a dictionary stemmer is the [`hunspell`](../token-filters/hunspell/index.md) token filter, which uses Hunspell---a spell checker engine used in many open-source applications.

### Considerations
When selecting a stemmer, take note of the following considerations:

- Algorithmic stemmers are suitable when processing speed and memory efficiency are priorities and the language has relatively regular morphological patterns.
- Dictionary stemmers are ideal when accuracy in handling irregular word forms is crucial and resources are available to support the increased memory usage and processing time.

### Additional stemming configuration

Although "organize" and "organic" share a common linguistic root, leading a stemmer to produce "organ" for both, their conceptual differences are significant. In practical search scenarios, this shared root can lead to irrelevant matches being returned in search results.

You can address these challenges by using the following methods:

- **Explicit stemming overrides**: Rather than relying solely on algorithmic stemming, you can define specific stemming rules. Using [`stemmer_override`](../token-filters/stemmer-override/index.md) allows you to ensure that "organize" remains unchanged while "organic" is reduced to "organ." This provides granular control over the final form of terms.

- **Keyword preservation**: To maintain the integrity of important terms, you can use the [`keyword_marker`](../token-filters/keyword-marker/index.md) token filter. This filter designates specific words as keywords, preventing subsequent stemmer filters from altering them. In this example, you can mark "organize" as a keyword, ensuring that it is indexed exactly as it appears.

- **Conditional stemming control**: The [condition](../token-filters/condition/index.md) token filter enables you to establish rules that determine whether a term should be stemmed. These can be based on various criteria, such as the term's presence in a predefined list.

- **Language-specific term exclusion**: For built-in language analyzers, the [`stem_exclusion`](../language-analyzers/english/index.md#stem-exclusion) parameter provides a way to specify words that should be exempt from stemming. For example, you can add "organize" to the `stem_exclusion` list, preventing the analyzer from stemming it. This can be useful for preserving the distinct meaning of specific terms within a given language.
