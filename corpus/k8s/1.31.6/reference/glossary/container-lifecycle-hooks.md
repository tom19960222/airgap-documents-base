---
collection: k8s
version: "1.31.6"
title: "Container Lifecycle Hooks"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/container-lifecycle-hooks.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The lifecycle hooks expose events in the Container management lifecycle and let the user run code when the events occur.

<!--more-->

Two hooks are exposed to Containers: PostStart which executes immediately after a container is created and PreStop which is blocking and is called immediately before a container is terminated.
