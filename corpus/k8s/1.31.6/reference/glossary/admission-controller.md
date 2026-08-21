---
collection: k8s
version: "1.31.6"
title: "Admission Controller"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/admission-controller.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A piece of code that intercepts requests to the Kubernetes API server prior to persistence of the object.

<!--more-->

Admission controllers are configurable for the Kubernetes API server and may be "validating", "mutating", or
both. Any admission controller may reject the request. Mutating controllers may modify the objects they admit;
validating controllers may not.

* [Admission controllers in the Kubernetes documentation](/docs/reference/access-authn-authz/admission-controllers/)
