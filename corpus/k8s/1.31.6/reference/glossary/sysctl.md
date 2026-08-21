---
collection: k8s
version: "1.31.6"
title: "sysctl"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/sysctl.md
fetched_at: 2026-01-16T10:18:07+05:30
---
`sysctl` is a semi-standardized interface for reading or changing the
 attributes of the running Unix kernel.

<!--more-->

On Unix-like systems, `sysctl` is both the name of the tool that administrators
use to view and modify these settings, and also the system call that the tool
uses.

Container runtimes and
network plugins may rely on `sysctl` values being set a certain way.
