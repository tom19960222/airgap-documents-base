---
collection: istio
version: "1.24"
title: "MisplacedAnnotation"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0107/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when an Istio annotation is attached to an invalid resource,
or to a resource in the wrong location.

For example, this could occur if you create a deployment and attach the
annotation to the deployment instead of attaching the annotation to the pods it
creates.

To resolve this problem, verify that your annotations are correctly placed and
try again.
