---
collection: k8s
version: "1.31.6"
title: "Node Resource Managers"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/concepts/policy/node-resource-managers.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

In order to support latency-critical and high-throughput workloads, Kubernetes offers a suite of Resource Managers. The managers aim to co-ordinate and optimise node's resources alignment for pods configured with a specific requirement for CPUs, devices, and memory (hugepages) resources. 

<!-- body -->

The main manager, the Topology Manager, is a Kubelet component that co-ordinates the overall resource management process through its [policy](/docs/tasks/administer-cluster/topology-manager/).

The configuration of individual managers is elaborated in dedicated documents:

- [CPU Manager Policies](/docs/tasks/administer-cluster/cpu-management-policies/)
- [Device Manager](/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/#device-plugin-integration-with-the-topology-manager)
- [Memory Manager Policies](/docs/tasks/administer-cluster/memory-manager/)
