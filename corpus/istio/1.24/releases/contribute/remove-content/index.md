---
collection: istio
version: "1.24"
title: "Remove Retired Documentation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/releases/contribute/remove-content/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Details how to contribute retired documentation to Istio."
---
To remove documentation from Istio, please follow these simple steps:

1. Remove the page.
1. Reconcile the broken links.
1. Submit your contribution to GitHub.

## Remove the page

Use `git rm -rf` to remove the directory containing the `index.md` page.

## Reconcile broken links

To reconcile broken links, use this flowchart:

![Remove Istio documentation](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/releases/contribute/remove-content/remove-documentation.svg)

## Submit your contribution to GitHub

If you are not familiar with GitHub, see our [working with GitHub guide](../github/index.md)
to learn how to submit documentation changes.

If you want to learn more about how and when your contributions are published,
see the [section on branching](../github/index.md#branching-strategy) to understand
how we use branches and cherry picking to publish our content.
