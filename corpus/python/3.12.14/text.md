---
collection: python
version: "3.12.14"
title: "Text Processing Services"
source_url: https://docs.python.org/3.12/library/text.html
fetched_at: 2026-09-17T15:32:11+00:00
---
# Text Processing Services

The modules described in this chapter provide a wide range of string
manipulation operations and other text processing services.

The [`codecs`](codecs.md#module-codecs "codecs: Encode and decode data and streams.") module described under [Binary Data Services](binary.md#binaryservices) is also
highly relevant to text processing. In addition, see the documentation for
Python’s built-in string type in [Text Sequence Type — str](stdtypes.md#textseq).

- [`string` — Common string operations](string.md)
  - [String constants](string.md#string-constants)
  - [Custom String Formatting](string.md#custom-string-formatting)
  - [Format String Syntax](string.md#format-string-syntax)
    - [Format Specification Mini-Language](string.md#format-specification-mini-language)
    - [Format examples](string.md#format-examples)
  - [Template strings](string.md#template-strings)
  - [Helper functions](string.md#helper-functions)
- [`re` — Regular expression operations](re.md)
  - [Regular Expression Syntax](re.md#regular-expression-syntax)
  - [Module Contents](re.md#module-contents)
    - [Flags](re.md#flags)
    - [Functions](re.md#functions)
    - [Exceptions](re.md#exceptions)
  - [Regular Expression Objects](re.md#regular-expression-objects)
  - [Match Objects](re.md#match-objects)
  - [Regular Expression Examples](re.md#regular-expression-examples)
    - [Checking for a Pair](re.md#checking-for-a-pair)
    - [Simulating scanf()](re.md#simulating-scanf)
    - [search() vs. match()](re.md#search-vs-match)
    - [Making a Phonebook](re.md#making-a-phonebook)
    - [Text Munging](re.md#text-munging)
    - [Finding all Adverbs](re.md#finding-all-adverbs)
    - [Finding all Adverbs and their Positions](re.md#finding-all-adverbs-and-their-positions)
    - [Raw String Notation](re.md#raw-string-notation)
    - [Writing a Tokenizer](re.md#writing-a-tokenizer)
- [`difflib` — Helpers for computing deltas](difflib.md)
  - [SequenceMatcher Objects](difflib.md#sequencematcher-objects)
  - [SequenceMatcher Examples](difflib.md#sequencematcher-examples)
  - [Differ Objects](difflib.md#differ-objects)
  - [Differ Example](difflib.md#differ-example)
  - [A command-line interface to difflib](difflib.md#a-command-line-interface-to-difflib)
  - [ndiff example](difflib.md#ndiff-example)
- [`textwrap` — Text wrapping and filling](textwrap.md)
- [`unicodedata` — Unicode Database](unicodedata.md)
- [`stringprep` — Internet String Preparation](stringprep.md)
- [`readline` — GNU readline interface](readline.md)
  - [Init file](readline.md#init-file)
  - [Line buffer](readline.md#line-buffer)
  - [History file](readline.md#history-file)
  - [History list](readline.md#history-list)
  - [Startup hooks](readline.md#startup-hooks)
  - [Completion](readline.md#completion)
  - [Example](readline.md#example)
- [`rlcompleter` — Completion function for GNU readline](rlcompleter.md)
