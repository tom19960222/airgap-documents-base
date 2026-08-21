---
collection: k8s
version: "1.31.6"
title: "ControllerManagerLeaderMigration"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/controller-manager-leader-migration.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enables Leader Migration for
[kube-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#initial-leader-migration-configuration) and
[cloud-controller-manager](/docs/tasks/administer-cluster/controller-manager-leader-migration/#deploy-cloud-controller-manager)
which allows a cluster operator to live migrate
controllers from the kube-controller-manager into an external controller-manager
(e.g. the cloud-controller-manager) in an HA cluster without downtime.
