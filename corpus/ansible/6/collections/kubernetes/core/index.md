---
collection: ansible
version: "6"
title: "Kubernetes.Core"
source_url: https://docs.ansible.com/projects/ansible/6/collections/kubernetes/core/index.html
fetched_at: 2026-07-27T16:42:01+00:00
---
# Kubernetes.Core

Collection version 2.3.2

- [Description](index.md#description)
- [Scenario Guide](index.md#scenario-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Kubernetes Collection for Ansible.

**Authors:**

- chouseknecht (<https://github.com/chouseknecht>)
- geerlingguy (<https://www.jeffgeerling.com/>)
- maxamillion (<https://github.com/maxamillion>)
- jmontleon (<https://github.com/jmontleon>)
- fabianvf (<https://github.com/fabianvf>)
- willthames (<https://github.com/willthames>)
- mmazur (<https://github.com/mmazur>)
- jamescassell (<https://github.com/jamescassell>)

**Supported ansible-core versions:**

- 2.9.17 or newer

[Issue Tracker](https://github.com/ansible-collections/kubernetes.core/issues)
[Repository (Sources)](https://github.com/ansible-collections/kubernetes.core)

## [Scenario Guide](index.md#id2)

- [Kubernetes Guide](docsite/scenario_guide.md)

## [Plugin Index](index.md#id3)

These are the plugins in the kubernetes.core collection:

### Modules

- [helm module](helm_module.md#ansible-collections-kubernetes-core-helm-module) – Manages Kubernetes packages with the Helm package manager
- [helm_info module](helm_info_module.md#ansible-collections-kubernetes-core-helm-info-module) – Get information from Helm package deployed inside the cluster
- [helm_plugin module](helm_plugin_module.md#ansible-collections-kubernetes-core-helm-plugin-module) – Manage Helm plugins
- [helm_plugin_info module](helm_plugin_info_module.md#ansible-collections-kubernetes-core-helm-plugin-info-module) – Gather information about Helm plugins
- [helm_repository module](helm_repository_module.md#ansible-collections-kubernetes-core-helm-repository-module) – Manage Helm repositories.
- [helm_template module](helm_template_module.md#ansible-collections-kubernetes-core-helm-template-module) – Render chart templates
- [k8s module](k8s_module.md#ansible-collections-kubernetes-core-k8s-module) – Manage Kubernetes (K8s) objects
- [k8s_cluster_info module](k8s_cluster_info_module.md#ansible-collections-kubernetes-core-k8s-cluster-info-module) – Describe Kubernetes (K8s) cluster, APIs available and their respective versions
- [k8s_cp module](k8s_cp_module.md#ansible-collections-kubernetes-core-k8s-cp-module) – Copy files and directories to and from pod.
- [k8s_drain module](k8s_drain_module.md#ansible-collections-kubernetes-core-k8s-drain-module) – Drain, Cordon, or Uncordon node in k8s cluster
- [k8s_exec module](k8s_exec_module.md#ansible-collections-kubernetes-core-k8s-exec-module) – Execute command in Pod
- [k8s_info module](k8s_info_module.md#ansible-collections-kubernetes-core-k8s-info-module) – Describe Kubernetes (K8s) objects
- [k8s_json_patch module](k8s_json_patch_module.md#ansible-collections-kubernetes-core-k8s-json-patch-module) – Apply JSON patch operations to existing objects
- [k8s_log module](k8s_log_module.md#ansible-collections-kubernetes-core-k8s-log-module) – Fetch logs from Kubernetes resources
- [k8s_rollback module](k8s_rollback_module.md#ansible-collections-kubernetes-core-k8s-rollback-module) – Rollback Kubernetes (K8S) Deployments and DaemonSets
- [k8s_scale module](k8s_scale_module.md#ansible-collections-kubernetes-core-k8s-scale-module) – Set a new size for a Deployment, ReplicaSet, Replication Controller, or Job.
- [k8s_service module](k8s_service_module.md#ansible-collections-kubernetes-core-k8s-service-module) – Manage Services on Kubernetes
- [k8s_taint module](k8s_taint_module.md#ansible-collections-kubernetes-core-k8s-taint-module) – Taint a node in a Kubernetes/OpenShift cluster

### Connection Plugins

- [kubectl connection](kubectl_connection.md#ansible-collections-kubernetes-core-kubectl-connection) – Execute tasks in pods running on Kubernetes.

### Inventory Plugins

- [k8s inventory](k8s_inventory.md#ansible-collections-kubernetes-core-k8s-inventory) – Kubernetes (K8s) inventory source

### Lookup Plugins

- [k8s lookup](k8s_lookup.md#ansible-collections-kubernetes-core-k8s-lookup) – Query the K8s API
- [kustomize lookup](kustomize_lookup.md#ansible-collections-kubernetes-core-kustomize-lookup) – Build a set of kubernetes resources using a ‘kustomization.yaml’ file.

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
