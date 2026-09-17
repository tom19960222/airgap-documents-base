---
collection: "opensearch"
version: "2.19"
title: "Tokenizers"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/tokenizers/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/tokenizers/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/tokenizers/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/tokenizers/index/"
canonical_route: "/analyzers/tokenizers/"
redirect_from: ["/analyzers/tokenizers/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 60
---
# Tokenizers

A tokenizer receives a stream of characters and splits the text into individual _tokens_. A token consists of a term (usually, a word) and metadata about this term. For example, a tokenizer can split text on white space so that the text `Actions speak louder than words.` becomes [`Actions`, `speak`, `louder`, `than`, `words.`].

The output of a tokenizer is a stream of tokens. Tokenizers also maintain the following metadata about tokens:

- The **order** or **position** of each token: This information is used for word and phrase proximity queries.
- The starting and ending positions (**offsets**) of the tokens in the text: This information is used for highlighting search terms.
- The token **type**: Some tokenizers (for example, `standard`) classify tokens by type, for example, `<ALPHANUM>` or `<NUM>`. Simpler tokenizers (for example, `letter`) only classify tokens as type `word`.

You can use tokenizers to define custom analyzers.

## Built-in tokenizers

The following tables list the built-in tokenizers that OpenSearch provides.

### Word tokenizers

Word tokenizers parse full text into words.

Tokenizer | Description | Example
:--- | :--- | :---
[`standard`](standard/index.md) | - Parses strings into tokens at word boundaries <br> - Removes most punctuation | `It’s fun to contribute a brand-new PR or 2 to OpenSearch!` <br>becomes<br> [`It’s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `PR`, `or`, `2`, `to`, `OpenSearch`]
[`letter`](letter/index.md) | - Parses strings into tokens on any non-letter character <br> - Removes non-letter characters | `It’s fun to contribute a brand-new PR or 2 to OpenSearch!` <br>becomes<br> [`It`, `s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `PR`, `or`, `to`, `OpenSearch`]
[`lowercase`](lowercase/index.md) | - Parses strings into tokens on any non-letter character <br> - Removes non-letter characters <br> - Converts terms to lowercase | `It’s fun to contribute a brand-new PR or 2 to OpenSearch!` <br>becomes<br> [`it`, `s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `pr`, `or`, `to`, `opensearch`]
[`whitespace`](whitespace/index.md) | - Parses strings into tokens at white space characters | `It’s fun to contribute a brand-new PR or 2 to OpenSearch!` <br>becomes<br> [`It’s`, `fun`, `to`, `contribute`, `a`,`brand-new`, `PR`, `or`, `2`, `to`, `OpenSearch!`]
[`uax_url_email`](uax-url-email/index.md) | - Similar to the standard tokenizer <br> - Unlike the standard tokenizer, leaves URLs and email addresses as single terms | `It’s fun to contribute a brand-new PR or 2 to OpenSearch opensearch-project@github.com!` <br>becomes<br> [`It’s`, `fun`, `to`, `contribute`, `a`,`brand`, `new`, `PR`, `or`, `2`, `to`, `OpenSearch`, `opensearch-project@github.com`]
[`classic`](classic/index.md) | - Parses strings into tokens on: <br> &emsp; - Punctuation characters that are followed by a white space character <br> &emsp; - Hyphens if the term does not contain numbers <br> - Removes punctuation <br>  - Leaves URLs and email addresses as single terms | `Part number PA-35234, single-use product (128.32)` <br>becomes<br> [`Part`, `number`, `PA-35234`, `single`, `use`, `product`, `128.32`]
[`thai`](thai/index.md) | - Parses Thai text into terms | `สวัสดีและยินดีต` <br>becomes<br> [`สวัสด`, `และ`, `ยินดี`, `ต`]

### Partial word tokenizers

Partial word tokenizers parse text into words and generate fragments of those words for partial word matching.

Tokenizer | Description | Example
:--- | :--- | :---
[`ngram`](ngram/index.md)| - Parses strings into words on specified characters (for example, punctuation or white space characters) and generates n-grams of each word | `My repo` <br>becomes<br> [`M`, `My`, `y`, `y `, <code>&nbsp;</code>, <code>&nbsp;r</code>, `r`, `re`, `e`, `ep`, `p`, `po`, `o`] <br> because the default n-gram length is 1--2 characters
[`edge_ngram`](edge-n-gram/index.md) | - Parses strings into words on specified characters (for example, punctuation or white space characters) and generates edge n-grams of each word (n-grams that start at the beginning of the word) | `My repo` <br>becomes<br> [`M`, `My`] <br> because the default n-gram length is 1--2 characters

### Structured text tokenizers

Structured text tokenizers parse structured text, such as identifiers, email addresses, paths, or ZIP Codes.

Tokenizer | Description | Example
:--- | :--- | :---
[`keyword`](keyword/index.md) | - No-op tokenizer <br> - Outputs the entire string unchanged <br> - Can be combined with token filters, like lowercase, to normalize terms | `My repo` <br>becomes<br> `My repo`
[`pattern`](pattern/index.md) | - Uses a regular expression pattern to parse text into terms on a word separator or to capture matching text as terms <br> - Uses [Java regular expressions](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html) | `https://opensearch.org/forum` <br>becomes<br> [`https`, `opensearch`, `org`, `forum`] because by default the tokenizer splits terms at word boundaries (`\W+`)<br>  Can be configured with a regex pattern
[`simple_pattern`](simple-pattern/index.md) | - Uses a regular expression pattern to return matching text as terms <br>  - Uses [Lucene regular expressions](https://lucene.apache.org/core/8_7_0/core/org/apache/lucene/util/automaton/RegExp.html)  <br> - Faster than the `pattern` tokenizer because it uses a subset of the `pattern` tokenizer regular expressions |  Returns an empty array by default <br> Must be configured with a pattern because the pattern defaults to an empty string
[`simple_pattern_split`](simple-pattern-split/index.md) | - Uses a regular expression pattern to split the text on matches rather than returning the matches as terms  <br>  - Uses [Lucene regular expressions](https://lucene.apache.org/core/8_7_0/core/org/apache/lucene/util/automaton/RegExp.html)  <br> - Faster than the `pattern` tokenizer because it uses a subset of the `pattern` tokenizer regular expressions | No-op by default<br> Must be configured with a pattern
[`char_group`](character-group/index.md) | - Parses on a set of configurable characters <br> - Faster than tokenizers that run regular expressions | No-op by default<br> Must be configured with a list of characters
[`path_hierarchy`](path-hierarchy/index.md) | - Parses text on the path separator (by default, `/`) and returns a full path to each component in the tree hierarchy | `one/two/three` <br>becomes<br> [`one`, `one/two`, `one/two/three`]
