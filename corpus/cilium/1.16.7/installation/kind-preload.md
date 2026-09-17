---
collection: cilium
version: "1.16.7"
title: "kind-preload"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/kind-preload.rst
fetched_at: 2025-02-13T12:04:31Z
---
Preload the ``cilium`` image into each worker node in the kind cluster:

.. parsed-literal::

   docker pull quay.io/cilium/cilium:|IMAGE_TAG|
   kind load docker-image quay.io/cilium/cilium:|IMAGE_TAG|
