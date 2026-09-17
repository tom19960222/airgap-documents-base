---
collection: cilium
version: "1.16.7"
title: "Verifying Image Signatures"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/configuration/verify-image-signatures.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="verify_image_signatures"></a>

# Verifying Image Signatures

## Prerequisites

You will need to [install cosign](https://docs.sigstore.dev/cosign/installation/).

## Verify Signed Container Images

Since version 1.13, all Cilium container images are signed using cosign.

Let's verify a Cilium image's signature using the ``cosign verify`` command:

```shell-session
$ TAG=v1.13.0
$ cosign verify --certificate-github-workflow-repository cilium/cilium \
--certificate-oidc-issuer https://token.actions.githubusercontent.com \
--certificate-github-workflow-name "Image Release Build" \
--certificate-github-workflow-ref refs/tags/${TAG} \
--certificate-identity "https://github.com/cilium/cilium/.github/workflows/build-images-releases.yaml@refs/tags/${TAG}" \
"quay.io/cilium/cilium:${TAG}" | jq
```

> **Note:**
> ``cosign`` is used to verify images signed in ``KEYLESS`` mode. To learn
> more about keyless signing, please refer to [Keyless Signatures](https://docs.sigstore.dev/cosign/overview/#keyless-signing-of-a-container).
>
> ``--certificate-github-workflow-name string`` contains the workflow claim
> from the GitHub OIDC Identity token that contains the name of the executed
> workflow. For the names of workflows used to build Cilium images, see the
> ``build-images`` workflows under [Cilium workflows](https://github.com/cilium/cilium/tree/2ab5f8da5915992a1e548c290105dbc08f4be52d/.github/workflows).
>
> ``--certificate-github-workflow-ref string`` contains the ref claim from
> the GitHub OIDC Identity token that contains the git ref that the workflow
> run was based upon.
>
> ``--certificate-identity`` is used to verify the identity of the certificate
> from the Github build images release workflow.
