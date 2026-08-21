---
collection: k8s
version: "1.31.6"
title: "Control Plane"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/control-plane.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers.

 <!--more--> 
 
 This layer is composed by many different components, such as (but not restricted to):

 * etcd
 * API Server
 * Scheduler
 * Controller Manager
 * Cloud Controller Manager

 These components can be run as traditional operating system services (daemons) or as containers. The hosts running these components were historically called masters.
