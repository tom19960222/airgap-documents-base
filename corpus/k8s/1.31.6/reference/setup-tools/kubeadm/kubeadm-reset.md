---
collection: k8s
version: "1.31.6"
title: "kubeadm reset"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/setup-tools/kubeadm/kubeadm-reset.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->
Performs a best effort revert of changes made by `kubeadm init` or `kubeadm join`.

<!-- body -->

[Include generated/kubeadm_reset/_index.md]

### Reset workflow {#reset-workflow}

`kubeadm reset` is responsible for cleaning up a node local file system from files that were created using
the `kubeadm init` or `kubeadm join` commands. For control-plane nodes `reset` also removes the local stacked
etcd member of this node from the etcd cluster.

`kubeadm reset phase` can be used to execute the separate phases of the above workflow.
To skip a list of phases you can use the `--skip-phases` flag, which works in a similar way to
the `kubeadm join` and `kubeadm init` phase runners.

### External etcd clean up

`kubeadm reset` will not delete any etcd data if external etcd is used. This means that if you run `kubeadm init` again using the same etcd endpoints, you will see state from previous clusters.

To wipe etcd data it is recommended you use a client like etcdctl, such as:

```bash
etcdctl del "" --prefix
```

See the [etcd documentation](https://github.com/coreos/etcd/tree/master/etcdctl) for more information.

### Graceful kube-apiserver shutdown

If you have your `kube-apiserver` configured with the `--shutdown-delay-duration` flag,
you can run the following commands to attempt a graceful shutdown for the running API server Pod,
before you run `kubeadm reset`:

```bash
yq eval -i '.spec.containers[0].command = []' /etc/kubernetes/manifests/kube-apiserver.yaml
timeout 60 sh -c 'while pgrep kube-apiserver >/dev/null; do sleep 1; done' || true
```

## What's next

* [kubeadm init](/docs/reference/setup-tools/kubeadm/kubeadm-init/) to bootstrap a Kubernetes control-plane node
* [kubeadm join](/docs/reference/setup-tools/kubeadm/kubeadm-join/) to bootstrap a Kubernetes worker node and join it to the cluster
