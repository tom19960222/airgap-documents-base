---
collection: cilium
version: "1.16.7"
title: "Introduction"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/network/intro.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Introduction

Cilium provides security on multiple levels. Each can be used individually or
combined together.

* [arch_id_security](identity.md#arch_id_security): Connectivity policies between endpoints (Layer 3),
  e.g. any endpoint with label ``role=frontend`` can connect to any endpoint with
  label ``role=backend``.
* Restriction of accessible ports (Layer 4) for both incoming and outgoing
  connections, e.g. endpoint with label ``role=frontend`` can only make outgoing
  connections on port 443 (https) and endpoint ``role=backend`` can only accept
  connections on port 443 (https).
* Fine grained access control on application protocol level to secure HTTP and
  remote procedure call (RPC) protocols, e.g the endpoint with label
  ``role=frontend`` can only perform the REST API call ``GET /userdata/[0-9]+``,
  all other API interactions with ``role=backend`` are restricted.
