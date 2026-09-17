---
collection: cilium
version: "1.16.7"
title: "upgrade-warning"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/operations/upgrade-warning.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

> **Warning:**
> Read the full upgrade guide to understand all the necessary steps before
> performing them.
>
> Do not upgrade to \ |NEXT_RELEASE| before reading the section
> [current_release_required_changes](upgrade.md#current_release_required_changes) and completing the required steps.
> Skipping this step may lead to an non-functional upgrade.
>
> The only tested rollback and upgrade path is between consecutive minor releases.
> Always perform rollbacks and upgrades between one minor release at a time.
> This means that going from (a hypothetical) 1.1 to 1.2 and back is supported
> while going from 1.1 to 1.3 and back is not.
>
> Always update to the latest patch release of your current version before
> attempting an upgrade.
