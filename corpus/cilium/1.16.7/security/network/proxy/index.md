---
collection: cilium
version: "1.16.7"
title: "Proxy Injection"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/network/proxy/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="proxy_injection"></a>

# Proxy Injection

Cilium is capable of transparently injecting a Layer 4 proxy into any network
connection. This is used as the foundation to enforce higher level network
policies (see [DNS based](../../policy/language.md#dns-based) and [l7_policy](../../policy/language.md#l7_policy)).

The following proxies can be injected:

.. toctree::
   :maxdepth: 1
   :glob:

   envoy
