---
collection: istio
version: "1.24"
title: "Trust Domain"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/glossary/trust-domain.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
[Trust domain](https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/#trust-domain) corresponds to the trust root of a system and is part of a workload identity.

Istio uses a trust domain to create all [identities](index.md#identity) within a mesh.
For example in `spiffe://mytrustdomain.com/ns/default/sa/myname` the substring `mytrustdomain.com` specifies that the workload is from a trust domain called `mytrustdomain.com`.

You can have one or more trust domains in a multicluster mesh, as long as the clusters share the same root of trust.
