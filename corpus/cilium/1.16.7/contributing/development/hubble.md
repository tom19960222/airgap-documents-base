---
collection: cilium
version: "1.16.7"
title: "Hubble"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/contributing/development/hubble.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="hubble_contributing"></a>

# Hubble

This section is specific to Hubble contributions.

## Bumping the vendored Cilium dependency

Hubble vendors Cilium using Go modules. You can bump the dependency by first
running:

```shell-session
go get github.com/cilium/cilium@main
```

However, Cilium's ``go.mod`` contains ``replace`` directives, which are ignored
by ``go get`` and ``go mod``. Therefore you must also manually copy any updated
``replace`` directives from Cilium's ``go.mod`` to Hubble's ``go.mod``.

Once you have done this you can tidy up, vendor the modules, and verify them:

```shell-session
go mod tidy
go mod vendor
go mod verify
```

The bumped dependency should be committed as a single commit containing all the
changes to ``go.mod``, ``go.sum``, and the ``vendor`` directory.
