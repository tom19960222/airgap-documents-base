---
collection: k8s
version: "1.31.6"
title: "Workload"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/workload.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A workload is an application running on Kubernetes.

<!--more--> 

Various core objects that represent different types or parts of a workload
include the DaemonSet, Deployment, Job, ReplicaSet, and StatefulSet objects.

For example, a workload that has a web server and a database might run the
database in one StatefulSet and the web server
in a Deployment.
