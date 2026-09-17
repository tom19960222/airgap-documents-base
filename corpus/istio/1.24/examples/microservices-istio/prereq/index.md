---
collection: istio
version: "1.24"
title: "Prerequisites"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/prereq/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
---
---

> **Warning:**
>
> This is work in progress. We will add its sections in pieces. Your feedback is welcome at [discuss.istio.io](https://discuss.istio.io).

For this tutorial you need a Kubernetes cluster with a namespace for the
tutorial's modules and a local computer to run the commands. If you have your
own cluster, ensure your cluster satisfies the prerequisites.

If you are in a workshop and the instructors provide a cluster, let
them handle the cluster prerequisites, while you skip ahead to set up your local
computer.

## Kubernetes cluster

Ensure the following conditions are met:

- You have administrator privileges to the virtual machine running a Kubernetes cluster named
  `tutorial-cluster` and administrator privileges to the virtual machine it runs on.
- You can create a namespace in the cluster for each participant.

## Local computer

Ensure the following conditions are met:

- You have write access to the local computer's `/etc/hosts` file.
- You have the ability and permission to download, install and run command line tools on the local computer.
- You have Internet connectivity for the duration of the tutorial.
