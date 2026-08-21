---
collection: k8s
version: "1.31.6"
title: "kubeadm init phase"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-init-phase.md
fetched_at: 2026-01-16T10:18:07+05:30
---
`kubeadm init phase` enables you to invoke atomic steps of the bootstrap process.
Hence, you can let kubeadm do some of the work and you can fill in the gaps
if you wish to apply customization.

`kubeadm init phase` is consistent with the [kubeadm init workflow](/docs/reference/setup-tools/kubeadm/kubeadm-init/#init-workflow),
and behind the scene both use the same code.

## kubeadm init phase preflight {#cmd-phase-preflight}

Using this command you can execute preflight checks on a control-plane node.

**Tab: preflight**

## kubeadm init phase kubelet-start {#cmd-phase-kubelet-start}

This phase will write the kubelet configuration file and environment file and then start the kubelet.

**Tab: kubelet-start**

## kubeadm init phase certs {#cmd-phase-certs}

Can be used to create all required certificates by kubeadm.

**Tab: certs**

**Tab: all**

**Tab: ca**

**Tab: apiserver**

**Tab: apiserver-kubelet-client**

**Tab: front-proxy-ca**

**Tab: front-proxy-client**

**Tab: etcd-ca**

**Tab: etcd-server**

**Tab: etcd-peer**

**Tab: healthcheck-client**

**Tab: apiserver-etcd-client**

**Tab: sa**

## kubeadm init phase kubeconfig {#cmd-phase-kubeconfig}

You can create all required kubeconfig files by calling the `all` subcommand or call them individually.

**Tab: kubeconfig**

**Tab: all**

**Tab: admin**

**Tab: kubelet**

**Tab: controller-manager**

**Tab: scheduler**

**Tab: super-admin**

## kubeadm init phase control-plane {#cmd-phase-control-plane}

Using this phase you can create all required static Pod files for the control plane components.

**Tab: control-plane**

**Tab: all**

**Tab: apiserver**

**Tab: controller-manager**

**Tab: scheduler**

## kubeadm init phase etcd {#cmd-phase-etcd}

Use the following phase to create a local etcd instance based on a static Pod file.

**Tab: etcd**

**Tab: local**

## kubeadm init phase upload-config {#cmd-phase-upload-config}

You can use this command to upload the kubeadm configuration to your cluster.
Alternatively, you can use [kubeadm config](/docs/reference/setup-tools/kubeadm/kubeadm-config/).

**Tab: upload-config**

**Tab: all**

**Tab: kubeadm**

**Tab: kubelet**

## kubeadm init phase upload-certs {#cmd-phase-upload-certs}

Use the following phase to upload control-plane certificates to the cluster.
By default the certs and encryption key expire after two hours.

**Tab: upload-certs**

## kubeadm init phase mark-control-plane {#cmd-phase-mark-control-plane}

Use the following phase to label and taint the node as a control plane node.

**Tab: mark-control-plane**

## kubeadm init phase bootstrap-token {#cmd-phase-bootstrap-token}

Use the following phase to configure bootstrap tokens.

**Tab: bootstrap-token**

## kubeadm init phase kubelet-finalize {#cmd-phase-kubelet-finalize-all}

Use the following phase to update settings relevant to the kubelet after TLS
bootstrap. You can use the `all` subcommand to run all `kubelet-finalize`
phases.

**Tab: kubelet-finalize**

**Tab: kubelet-finalize-all**

**Tab: kubelet-finalize-cert-rotation**

## kubeadm init phase addon {#cmd-phase-addon}

You can install all the available addons with the `all` subcommand, or
install them selectively.

**Tab: addon**

**Tab: all**

**Tab: coredns**

**Tab: kube-proxy**

For more details on each field in the `v1beta4` configuration you can navigate to our
[API reference pages.](/docs/reference/config-api/kubeadm-config.v1beta4/)

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to connect a node to the cluster
* [kubeadm reset](/docs/reference/setup-tools/kubeadm/kubeadm-reset/) to revert any changes made to this host by `kubeadm init` or `kubeadm join`
* [kubeadm alpha](/docs/reference/setup-tools/kubeadm/kubeadm-alpha/) to try experimental functionality
