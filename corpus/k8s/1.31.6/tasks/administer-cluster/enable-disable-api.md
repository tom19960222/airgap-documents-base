---
collection: k8s
version: "1.31.6"
title: "Enable Or Disable A Kubernetes API"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/administer-cluster/enable-disable-api.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->
This page shows how to enable or disable an API version from your cluster's
control plane.

<!-- steps -->

Specific API versions can be turned on or off by passing `--runtime-config=api/<version>` as a
command line argument to the API server. The values for this argument are a comma-separated
list of API versions. Later values override earlier values.

The `runtime-config` command line argument also supports 2 special keys:

- `api/all`, representing all known APIs
- `api/legacy`, representing only legacy APIs. Legacy APIs are any APIs that have been
   explicitly [deprecated](/docs/reference/using-api/deprecation-policy/).

For example, to turn off all API versions except v1, pass `--runtime-config=api/all=false,api/v1=true`
to the `kube-apiserver`.

## What's next

Read the [full documentation](/docs/reference/command-line-tools-reference/kube-apiserver/)
for the `kube-apiserver` component.
