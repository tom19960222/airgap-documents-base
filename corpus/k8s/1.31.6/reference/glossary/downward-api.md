---
collection: k8s
version: "1.31.6"
title: "Downward API"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/downward-api.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Kubernetes' mechanism to expose Pod and container field values to code running in a container.
<!--more-->
It is sometimes useful for a container to have information about itself, without
needing to make changes to the container code that directly couple it to Kubernetes.

The Kubernetes downward API allows containers to consume information about themselves
or their context in a Kubernetes cluster. Applications in containers can have
access to that information, without the application needing to act as a client of
the Kubernetes API.

There are two ways to expose Pod and container fields to a running container:

- using [environment variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/)
- using [a `downwardAPI` volume](/docs/tasks/inject-data-application/downward-api-volume-expose-pod-information/)

Together, these two ways of exposing Pod and container fields are called the _downward API_.
