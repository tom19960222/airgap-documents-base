---
collection: k8s
version: "1.31.6"
title: "Network Policy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/network-policy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A specification of how groups of Pods are allowed to communicate with each other and with other network endpoints.

<!--more--> 

Network Policies help you declaratively configure which Pods are allowed to connect to each other, which namespaces are allowed to communicate, and more specifically which port numbers to enforce each policy on. `NetworkPolicy` resources use labels to select Pods and define rules which specify what traffic is allowed to the selected Pods. Network Policies are implemented by a supported network plugin provided by a network provider. Be aware that creating a network resource without a controller to implement it will have no effect.
