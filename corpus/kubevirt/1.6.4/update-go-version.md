---
collection: kubevirt
version: "1.6.4"
title: "How to update Go version"
source_url: https://github.com/kubevirt/kubevirt/blob/ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f/docs/update-go-version.md
fetched_at: 2026-03-16T09:25:18Z
---
# How to update Go version
A quick guide to update KubeVirt's Go version.

To update the Go version we need to update the builder image so that it uses the new version,
push it to the registry and finally let KubeVirt use the new builder image.

In addition, [go rules for bazel](https://github.com/bazelbuild/rules_go) have to be updated if the current version does not support the target Go version.

## Updating Go Version
### Updating builder image

* Change the `GIMME_GO_VERSION` in the [hack/builder/Dockerfile](../hack/builder/Dockerfile) <!-- unresolved-source-link: target=../hack/builder/Dockerfile --> to the desired Go version.
* Rebuild the builder image by executing `make builder-build`.

### Publishing builder image
* Publish new builder image with `make builder-publish`.
  * Note: Proper access rights are required in order to publish builder image.
  * When publish is finished, the builder image tag will be presented. For instance, if the output of `make builder-publish` is:
    ```shell
    2103210933-9be558add-amd64: digest: sha256:cc83534b5d99da35643f8a2a87830b0dabcb4f130c1db181a835dc8def09174b size: 3271
    + TMP_IMAGES=' quay.io/kubevirt/builder:2103210933-9be558add-amd64'
    + export DOCKER_CLI_EXPERIMENTAL=enabled
    + DOCKER_CLI_EXPERIMENTAL=enabled
    + docker manifest create --amend quay.io/kubevirt/builder:2103210933-9be558add quay.io/kubevirt/builder:2103210933-9be558add-amd64
      Created manifest list quay.io/kubevirt/builder:2103210933-9be558add
    + docker manifest push quay.io/kubevirt/builder:2103210933-9be558add
      sha256:d828eb647e7ef3115f39ff4cb2d5d41da39b4134056e429be16c3a019b521957
    + cleanup
    + rm manifests/ -rf
    ```
  * The image tag is `2103210933-9be558add`
* Change `KUBEVIRT_BUILDER_IMAGE` variable in [hack/dockerized](../hack/dockerized) <!-- unresolved-source-link: target=../hack/dockerized --> to the tag from the previous step.
* In [WORKSPACE](../WORKSPACE) <!-- unresolved-source-link: target=../WORKSPACE --> change `go_version` to the desired Go version.
  * Should look similar to:
    ```shell
    go_register_toolchains(
        go_version = "1.14.14",
        nogo = "@//:nogo_vet",
    )
    ```

## Update go rules for bazel
* In [WORKSPACE](../WORKSPACE) <!-- unresolved-source-link: target=../WORKSPACE --> find current Bazel release's SHA ID which can be found under `io_bazel_rules_go`.
  * Should look similar to:
    ```shell
    http_archive(
      name = "io_bazel_rules_go",
      sha256 = "52d0a57ea12139d727883c2fef03597970b89f2cc2a05722c42d1d7d41ec065b",
      urls = [
        ...
      ],
    )
    ```
* Visit [Bazel's releases page](https://github.com/bazelbuild/rules_go/releases) and check whether the current Bazel version supports the new Go version.
  * If it is not supported, replace the `io_bazel_rules_go` definition with the one provided in Bazel's page.
