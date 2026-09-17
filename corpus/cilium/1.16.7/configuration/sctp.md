---
collection: cilium
version: "1.16.7"
title: "SCTP support (beta)"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/configuration/sctp.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="sctp"></a>

# SCTP support (beta)

Included file `Documentation/beta.rst`:

> **Note:**
> This is a beta feature. Please provide feedback and file a GitHub issue if
> you experience any problems.

## Enabling
Pass ``--set sctp.enabled=true`` to helm.

.. admonition:: Video
   :class: attention

    You can also watch a video explanation of Cilium's SCTP support in [eCHO episode 78: Stream Control Transmission Protocol (SCTP)](https://www.youtube.com/watch?v=2lD86qNHXXI).

## Limitations
Cilium supports basic SCTP support. Specifically, the following is supported:
 - Pod <-> Pod communication
 - Pod <-> Service communication [*]
 - Pod <-> Pod communication with network policies applied to SCTP traffic [*]

> **Note:**
> [*] SCTP support does not support rewriting ports for SCTP packets. This means
> that when defining services, the targetPort **MUST** equal the port, otherwise
> the packet will be dropped.

> **Warning:**
> Cilium does not support the following for SCTP:
>  - Multihoming
>  - Policies for pod-to-VIP
>  - KPR
>  - BPF masquerading
>  - Egress gateway
