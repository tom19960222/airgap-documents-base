---
collection: cilium
version: "1.16.7"
title: "Testing"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/contributing/testing/index.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="testing_guide"></a>

# Testing

There are multiple ways to test Cilium functionality, including unit-testing
and integration testing. In order to improve developer throughput, we provide
ways to run both the unit and integration tests in your own workspace as opposed
to being fully reliant on the Cilium CI infrastructure. We encourage all PRs to
add unit tests and if necessary, integration tests. Consult the following pages
to see how to run the variety of tests that have been written for Cilium, and
information about Cilium's CI infrastructure.

<a id="testing_root"></a>

.. toctree::
   :maxdepth: 2
   :glob:

   ci
   e2e
   e2e_legacy
   unit
   bpf

The best way to get help if you get stuck is to ask a question on the Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->. With Cilium contributors across the globe, there is almost always
someone available to help.
