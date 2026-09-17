---
collection: cilium
version: "1.16.7"
title: "Welcome to Cilium's documentation!"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Welcome to Cilium's documentation!

The documentation is divided into the following sections:

* [k8s_install_quick](gettingstarted/k8s-install-default.md#k8s_install_quick): Provides a simple tutorial for running a small Cilium
  setup on your laptop.  Intended as an easy way to get your hands dirty
  applying Cilium security policies between containers.

* [getting_started](index.md#getting_started) :  Details instructions for installing, configuring, and
  troubleshooting Cilium in different deployment modes.

* [network_policy](security/policy/index.md#network_policy) : Detailed walkthrough of the policy language structure
  and the supported formats.

* [observability](network/kubernetes/kubeproxy-free.md#observability) : Provides instructions on setting up and configuring
  [hubble_intro](observability/hubble/index.md#hubble_intro) and configuring [metrics collection from Cilium and Hubble](configuration/api-rate-limiting.md#metrics).

* [admin_guide](operations/troubleshooting.md#admin_guide) : Describes how to troubleshoot Cilium in different
  deployment modes.

* [bpf_guide](reference-guides/bpf/index.md#bpf_guide) : Provides a technical deep dive of eBPF and XDP technology,
  primarily focused at developers.

* [api_ref](api.md#api_ref) : Details the Cilium agent API for interacting with a local
  Cilium instance.

* [dev_guide](contributing/development/index.md#dev_guide) : Gives background to those looking to develop and contribute
  modifications to the Cilium code or documentation.

* [security_root](security/index.md#security_root) : Provides a one-page resource of best practices for securing Cilium.

A [hands-on tutorial](https://cilium.io/enterprise/#trainings)
in a live environment is also available for users looking for a way to quickly
get started and experiment with Cilium.

.. toctree::
   :maxdepth: 2
   :caption: Overview

   overview/intro
   overview/component-overview

<a id="getting_started"></a>

.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   gettingstarted/k8s-install-default
   gettingstarted/demo
   gettingstarted/terminology
   gettingstarted/gettinghelp

.. toctree::
   :maxdepth: 2
   :caption: Advanced Installation

   installation/taints
   installation/k8s-install-helm
   installation/k8s-install-migration
   installation/k8s-toc
   installation/external-toc

.. toctree::
   :maxdepth: 2
   :caption: Networking

   network/concepts/index
   network/kubernetes/index
   network/bgp-toc
   network/ebpf/index
   network/clustermesh/index
   network/external-toc
   network/egress-gateway-toc
   network/servicemesh/index
   network/vtep
   network/l2-announcements
   network/node-ipam
   network/pod-mac-address
   network/multicast

.. toctree::
   :maxdepth: 2
   :caption: Security

   security/index
   security/network/index
   security/policy/index
   security/restrict-pod-access
   security/threat-model

.. toctree::
   :maxdepth: 2
   :caption: Observability
   :name: observability

   observability/hubble/index
   observability/grafana
   observability/metrics
   observability/visibility

.. toctree::
   :maxdepth: 2
   :caption: Operations

   operations/system_requirements
   operations/upgrade
   configuration/index
   operations/performance/index
   operations/troubleshooting

.. toctree::
   :maxdepth: 2
   :caption: Community

   community/governance
   community/community
   community/roadmap

.. toctree::
   :maxdepth: 2
   :caption: Contributor Guide

   contributing/development/index
   contributing/release/index
   contributing/testing/index
   contributing/docs/index
   api
   grpcapi
   internals/index

.. toctree::
   :maxdepth: 2
   :caption: Reference

   cheatsheet
   cmdref/index
   helm-reference
   kvstore
   further_reading
   glossary

.. toctree::
   :maxdepth: 2
   :caption: Reference Guides

   reference-guides/bpf/index
   reference-guides/xfrm/index
