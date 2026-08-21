---
collection: k8s
version: "1.31.6"
title: "Kubernetes API"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/kubernetes-api.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The application that serves Kubernetes functionality through a RESTful interface and stores the state of the cluster.

<!--more--> 

Kubernetes resources and "records of intent" are all stored as API objects, and modified via RESTful calls to the API. The API allows configuration to be managed in a declarative way. Users can interact with the Kubernetes API directly, or via tools like `kubectl`. The core Kubernetes API is flexible and can also be extended to support custom resources.
