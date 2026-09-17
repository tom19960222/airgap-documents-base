---
collection: "opensearch"
version: "2.19"
title: "Character filters"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/character-filters/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/character-filters/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/character-filters/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/character-filters/index/"
canonical_route: "/analyzers/character-filters/"
redirect_from: ["/analyzers/character-filters/"]
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
# Character filters

Character filters process text before tokenization to prepare it for further analysis.

Unlike token filters, which operate on tokens (words or terms), character filters process the raw input text before tokenization. They are especially useful for cleaning or transforming structured text containing unwanted characters, such as HTML tags or special symbols. Character filters help to strip or replace these elements so that text is properly formatted for analysis.

Use cases for character filters include:

- **HTML stripping**: The [`html_strip`](html-character-filter/index.md) character filter removes HTML tags from content so that only the plain text is indexed.
- **Pattern replacement**: The [`pattern_replace`](pattern-replace-character-filter/index.md) character filter replaces or removes unwanted characters or patterns in text, for example, converting hyphens to spaces.
- **Custom mappings**: The [`mapping`](mapping-character-filter/index.md) character filter substitutes specific characters or sequences with other values, for example, to convert currency symbols into their textual equivalents.
