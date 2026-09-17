---
collection: cilium
version: "1.16.7"
title: "Identity-Aware and HTTP-Aware Policy Enforcement"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/http.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_http"></a>

# Identity-Aware and HTTP-Aware Policy Enforcement

Included file `Documentation/security/gsg_requirements.rst`:

If you haven't read the [intro](../overview/intro.md#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->. With Cilium contributors across the globe, there is almost always
someone available to help.

## Setup Cilium

If you have not set up Cilium yet, follow the guide [k8s_install_standard](../gettingstarted/k8s-install-default.md#k8s_install_standard)
for instructions on how to quickly bootstrap a Kubernetes cluster and install
Cilium. If in doubt, pick the minikube route, you will be good to go in less
than 5 minutes.

When you have Cilium installed, follow the [starwars_demo](../gettingstarted/demo.md#starwars_demo) tutorial to walk you through Identity-Aware and HTTP-Aware Policy Enforcement.
