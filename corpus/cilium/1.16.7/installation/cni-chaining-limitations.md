---
collection: cilium
version: "1.16.7"
title: "cni-chaining-limitations"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cni-chaining-limitations.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

> **Note:**
> Some advanced Cilium features may be limited when chaining with other
> CNI plugins, such as:
>
> * [Layer 7 Policy](../security/policy/language.md#l7_policy) (see 12454)
> * [encryption_ipsec](../security/network/encryption-ipsec.md#encryption_ipsec) (see 15596)
