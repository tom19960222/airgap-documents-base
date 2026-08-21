---
collection: k8s
version: "1.31.6"
title: "Event"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/event.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Event is a Kubernetes object that describes state change/notable occurrences in the system.

<!--more-->
Events have a limited retention time and triggers and messages may evolve with time. 
Event consumers should not rely on the timing of an event with a given reason reflecting a consistent underlying trigger, 
or the continued existence of events with that reason. 

Events should be treated as informative, best-effort, supplemental data.

In Kubernetes, [auditing](/docs/tasks/debug/debug-cluster/audit/) generates a different kind of
Event record (API group `audit.k8s.io`).
