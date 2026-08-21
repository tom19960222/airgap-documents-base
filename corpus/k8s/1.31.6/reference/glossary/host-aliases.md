---
collection: k8s
version: "1.31.6"
title: "HostAliases"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/host-aliases.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A HostAliases is a mapping between the IP address and hostname to be injected into a Pod's hosts file.

<!--more-->

[HostAliases](/docs/reference/generated/kubernetes-api/version/#hostalias-v1-core) is an optional list of hostnames and IP addresses that will be injected into the Pod's hosts file if specified. This is only valid for non-hostNetwork Pods.
