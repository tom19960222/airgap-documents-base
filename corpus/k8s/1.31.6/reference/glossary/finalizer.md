---
collection: k8s
version: "1.31.6"
title: "Finalizer"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/finalizer.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Finalizers are namespaced keys that tell Kubernetes to wait until specific
conditions are met before it fully deletes resources marked for deletion.
Finalizers alert controllers
to clean up resources the deleted object owned.

<!--more-->

When you tell Kubernetes to delete an object that has finalizers specified for
it, the Kubernetes API marks the object for deletion by populating `.metadata.deletionTimestamp`,
and returns a `202` status code (HTTP "Accepted"). The target object remains in a terminating state while the
control plane, or other components, take the actions defined by the finalizers.
After these actions are complete, the controller removes the relevant finalizers
from the target object. When the `metadata.finalizers` field is empty,
Kubernetes considers the deletion complete and deletes the object.

You can use finalizers to control garbage collection
of resources. For example, you can define a finalizer to clean up related resources or
infrastructure before the controller deletes the target resource.
