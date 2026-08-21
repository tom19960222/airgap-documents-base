---
collection: k8s
version: "1.31.6"
title: "KubeletCgroupDriverFromCRI"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/kubelet-cgroup-driver-from-cri.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable detection of the kubelet cgroup driver
configuration option from the CRI.
You can use this feature gate on nodes with a kubelet that supports the feature gate
and where there is a CRI container runtime that supports the `RuntimeConfig`
CRI call. If both CRI and kubelet support this feature, the kubelet ignores the
`cgroupDriver` configuration setting (or deprecated `--cgroup-driver` command
line argument). If you enable this feature gate and the container runtime
doesn't support it, the kubelet falls back to using the driver configured using
the `cgroupDriver` configuration setting.
See [Configuring a cgroup driver](/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver)
for more details.
