---
collection: gitlab
version: "17.9.8"
title: "Syntax options"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/drawers/exact_code_search_syntax.md
fetched_at: 2025-05-07T10:05:15Z
---
<!-- Remember to also update the table in `doc/user/search/exact_code_search.md` -->

| Query                | Exact match mode                                        | Regular expression mode |
| -------------------- | ------------------------------------------------------- | ----------------------- |
| `"foo"`              | `"foo"`                                                 | `foo` |
| `foo file:^doc/`     | `foo` in directories that start with `/doc`             | `foo` in directories that start with `/doc` |
| `"class foo"`        | `"class foo"`                                           | `class foo` |
| `class foo`          | `class foo`                                             | `class` and `foo` |
| `foo or bar`         | `foo or bar`                                            | `foo` or `bar` |
| `class Foo`          | `class Foo` (case sensitive)                            | `class` (case insensitive) and `Foo` (case sensitive) |
| `class Foo case:yes` | `class Foo` (case sensitive)                            | `class` and `Foo` (both case sensitive) |
| `foo -bar`           | `foo -bar`                                              | `foo` but not `bar` |
| `foo file:js`        | `foo` in files with names that contain `js`             | `foo` in files with names that contain `js` |
| `foo -file:test`     | `foo` in files with names that do not contain `test`    | `foo` in files with names that do not contain `test` |
| `foo lang:ruby`      | `foo` in Ruby source code                               | `foo` in Ruby source code |
| `foo file:\.js$`     | `foo` in files with names that end with `.js`           | `foo` in files with names that end with `.js` |
| `foo.*bar`           | `foo.*bar` (literal)                                    | `foo.*bar` (regular expression) |
| `sym:foo`            | `foo` in symbols like class, method, and variable names | `foo` in symbols like class, method, and variable names |
