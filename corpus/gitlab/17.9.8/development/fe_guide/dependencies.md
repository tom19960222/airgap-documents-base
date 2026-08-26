---
collection: gitlab
version: "17.9.8"
title: "Frontend dependencies"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/fe_guide/dependencies.md
fetched_at: 2025-05-07T10:05:15Z
---
We use [yarn@1](https://classic.yarnpkg.com/lang/en/) to manage frontend dependencies.

There are a few exceptions in the GitLab repository, stored in `vendor/assets/`.

## What are production and development dependencies?

These dependencies are defined in two groups within `package.json`, `dependencies` and `devDependencies`.
For our purposes, we consider anything that is required to compile our production assets a "production" dependency.
That is, anything required to run the `webpack` script with `NODE_ENV=production`.
Tools like `eslint`, `jest`, and various plugins and tools used in development are considered `devDependencies`.
This distinction is used by omnibus to determine which dependencies it requires when building GitLab.

Exceptions are made for some tools that we require in the
`compile-production-assets` CI job such as `webpack-bundle-analyzer` to analyze our
production assets post-compile.

## Updating dependencies

See the main [Dependencies](../dependencies.md) page for general information about dependency updates.
