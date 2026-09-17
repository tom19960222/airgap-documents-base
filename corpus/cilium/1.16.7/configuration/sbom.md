---
collection: cilium
version: "1.16.7"
title: "Software Bill of Materials"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/configuration/sbom.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="sbom"></a>

# Software Bill of Materials

A Software Bill of Materials (SBOM) is a complete, formally structured list of
components that are required to build a given piece of software. SBOM provides
insight into the software supply chain and any potential concerns related to
license compliance and security that might exist.

The Cilium SBOM is generated using the [syft](https://github.com/anchore/syft) tool. To learn more about SBOM, see
[what an SBOM can do for you](https://www.chainguard.dev/unchained/what-an-sbom-can-do-for-you).

## Prerequisites

- [Install cosign](https://docs.sigstore.dev/cosign/installation/)

## Download SBOM

The SBOM can be downloaded from the supplied Cilium image using the
``cosign download sbom`` command.

```shell-session
$ cosign download sbom --output-file sbom.spdx <Image URL>
```

## Verify SBOM Image Signature

To ensure the SBOM is tamper-proof, its signature can be verified using the
``cosign verify`` command.

```shell-session
$ COSIGN_EXPERIMENTAL=1 cosign verify --certificate-github-workflow-repository cilium/cilium --certificate-oidc-issuer https://token.actions.githubusercontent.com --attachment sbom <Image URL> | jq
```

It can be validated that the image was signed using Github Actions in the Cilium
repository from the ``Issuer`` and ``Subject`` fields of the output.
