---
collection: thanos
version: "0.37.1"
title: "Changing Golang version"
source_url: https://github.com/thanos-io/thanos/blob/e0812e2f46f81af3324686d910d885d8f2751d46/docs/contributing/how-to-change-go-version.md
fetched_at: 2024-12-04T08:22:07Z
---
# Changing Golang version

Thanos build system is pinned to certain Golang version. This is to ensure that Golang version changes is done by us in controlled, traceable way.

To update Thanos build system to newer Golang:

1. Edit [.promu.yaml](../../.promu.yml) <!-- unresolved-source-link: target=../../.promu.yml --> and edit `go: version: <go version>` in YAML to desired version. This will ensure that all artifacts are built with desired Golang version. How to verify? Download tarball, unpack and invoke `thanos --version`
2. Edit [.circleci/config.yaml](../../.circleci/config.yml) <!-- unresolved-source-link: target=../../.circleci/config.yml --> and update ` - image: cimg/go:<go version>-node` to desired Golang version. This will ensure that all docker images and go tests are using desired Golang version. How to verify? Invoke `docker pull quay.io/thanos/thanos:<version> --version`
3. Edit [.github/workflows/docs.yaml](../../.github/workflows/docs.yaml) <!-- unresolved-source-link: target=../../.github/workflows/docs.yaml --> [.github/workflows/go.yaml](../../.github/workflows/go.yaml) <!-- unresolved-source-link: target=../../.github/workflows/go.yaml --> and update Go version.
4. Edit [Dockerfile.e2e-tests](../../Dockerfile.e2e-tests) <!-- unresolved-source-link: target=../../Dockerfile.e2e-tests --> and update Go version.
