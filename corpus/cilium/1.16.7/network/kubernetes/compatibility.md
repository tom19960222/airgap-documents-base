---
collection: cilium
version: "1.16.7"
title: "Kubernetes Compatibility"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/kubernetes/compatibility.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k8scompatibility"></a>

# Kubernetes Compatibility

Cilium is compatible with multiple Kubernetes API Groups. Some are deprecated
or beta, and may only be available in specific versions of Kubernetes.

All Kubernetes versions listed are e2e tested and guaranteed to be compatible
with Cilium. Older and newer Kubernetes versions, while not listed, will depend
on the forward / backward compatibility offered by Kubernetes.

| k8s Version | k8s NetworkPolicy API | CiliumNetworkPolicy |
| --- | --- | --- |
| <br> 1.27, 1.28, 1.29, 1.30 | <br> * [networking.k8s.io/v1](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#networkpolicy-v1-networking-k8s-io) | ``cilium.io/v2`` has a <br> CustomResourceDefinition |

As a general rule, Cilium aims to run e2e tests using the latest build from the
development branch against currently supported Kubernetes versions defined in
[Kubernetes Patch Releases](https://kubernetes.io/releases/patch-releases/)
page.

Once a release branch gets created from the development branch, Cilium typically
does not change the Kubernetes versions it uses to run e2e tests for the entire
maintenance period of that particular release.

Additionally, Cilium runs e2e tests against various cloud providers' managed
Kubernetes offerings using multiple Kubernetes versions. See the following links
for the current test matrix for each cloud provider:

- AKS
- EKS
- GKE

## Cilium CRD schema validation

Cilium uses a CRD for its Network Policies in Kubernetes. This CRD might have
changes in its schema validation, which allows it to verify the correctness of
a Cilium Clusterwide Network Policy (CCNP) or a Cilium Network Policy (CNP).

The CRD itself has an annotation, ``io.cilium.k8s.crd.schema.version``, with the
schema definition version. By default, Cilium automatically updates the CRD, and
its validation, with a newer one.

The following table lists all Cilium versions and their expected schema
validation version:

Included file `Documentation/network/kubernetes/compatibility-table.rst`:

| Cilium <br> Version | CNP and CCNP <br> Schema Version |
| --- | --- |
| v1.14.0-pre.2 | 1.26.8 |
| v1.14.0-rc.0 | 1.26.9 |
| v1.14.0-rc.1 | 1.26.10 |
| v1.14.0-snapshot.0 | 1.26.7 |
| v1.14.0-snapshot.1 | 1.26.7 |
| v1.14.0-snapshot.2 | 1.26.8 |
| v1.14.0-snapshot.3 | 1.26.9 |
| v1.14.0-snapshot.4 | 1.26.10 |
| v1.14.0-snapshot.5 | 1.26.9 |
| v1.14.0-snapshot.6 | 1.26.10 |
| v1.14.0 | 1.26.10 |
| v1.14.1 | 1.26.10 |
| v1.14.2 | 1.26.11 |
| v1.14.3 | 1.26.11 |
| v1.14.4 | 1.26.11 |
| v1.14.5 | 1.26.11 |
| v1.14.6 | 1.27.0 |
| v1.14.7 | 1.27.0 |
| v1.14.8 | 1.27.0 |
| v1.14.9 | 1.27.1 |
| v1.14.10 | 1.27.1 |
| v1.14.11 | 1.27.1 |
| v1.14.12 | 1.27.1 |
| v1.14.13 | 1.27.1 |
| v1.14.14 | 1.27.1 |
| v1.14.15 | 1.27.2 |
| v1.14.16 | 1.27.2 |
| v1.14.17 | 1.27.2 |
| v1.14.18 | 1.27.2 |
| v1.14.19 | 1.27.2 |
| v1.14 | 1.27.2 |
| v1.15.0-pre.0 | 1.26.9 |
| v1.15.0-pre.1 | 1.26.10 |
| v1.15.0-pre.2 | 1.26.11 |
| v1.15.0-pre.3 | 1.26.12 |
| v1.15.0-rc.0 | 1.28.0 |
| v1.15.0-rc.1 | 1.28.0 |
| v1.15.0 | 1.28.1 |
| v1.15.1 | 1.28.1 |
| v1.15.2 | 1.28.1 |
| v1.15.3 | 1.28.2 |
| v1.15.4 | 1.28.2 |
| v1.15.5 | 1.28.2 |
| v1.15.6 | 1.28.2 |
| v1.15.7 | 1.28.2 |
| v1.15.8 | 1.28.2 |
| v1.15.9 | 1.28.3 |
| v1.15.10 | 1.28.3 |
| v1.15.11 | 1.28.3 |
| v1.15.12 | 1.28.3 |
| v1.15.13 | 1.28.3 |
| v1.15 | 1.28.3 |
| v1.16.0-pre.0 | 1.29.2 |
| v1.16.0-pre.1 | 1.29.4 |
| v1.16.0-pre.2 | 1.29.5 |
| v1.16.0-pre.3 | 1.29.7 |
| v1.16.0-rc.0 | 1.29.9 |
| v1.16.0-rc.1 | 1.29.10 |
| v1.16.0-rc.2 | 1.29.11 |
| v1.16.0 | 1.29.11 |
| v1.16.1 | 1.29.12 |
| v1.16.2 | 1.29.13 |
| v1.16.3 | 1.29.13 |
| v1.16.4 | 1.29.13 |
| v1.16.5 | 1.29.14 |
| v1.16.6 | 1.29.14 |
| v1.16 | 1.29.14 |
| latest / main | 1.31.1 |
