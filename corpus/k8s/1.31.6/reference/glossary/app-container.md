---
collection: k8s
version: "1.31.6"
title: "App Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/app-container.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Application containers (or app containers) are the containers in a pod that are started after any init containers have completed.

<!--more-->

An init container lets you separate initialization details that are important for the overall 
workload, and that don't need to keep running
once the application container has started.
If a pod doesn't have any init containers configured, all the containers in that pod are app containers.
