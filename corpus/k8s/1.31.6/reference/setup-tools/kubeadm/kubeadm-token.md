---
collection: k8s
version: "1.31.6"
title: "kubeadm token"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-token.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

Bootstrap tokens are used for establishing bidirectional trust between a node joining
the cluster and a control-plane node, as described in [authenticating with bootstrap tokens](/docs/reference/access-authn-authz/bootstrap-tokens/).

`kubeadm init` creates an initial token with a 24-hour TTL. The following commands allow you to manage
such a token and also to create and manage new ones.

<!-- body -->
## kubeadm token create {#cmd-token-create}

[Include generated/kubeadm_token/kubeadm_token_create.md]

## kubeadm token delete {#cmd-token-delete}

[Include generated/kubeadm_token/kubeadm_token_delete.md]

## kubeadm token generate {#cmd-token-generate}

[Include generated/kubeadm_token/kubeadm_token_generate.md]

## kubeadm token list {#cmd-token-list}

[Include generated/kubeadm_token/kubeadm_token_list.md]

## What's next

* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes worker node and join it to the cluster
