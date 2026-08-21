---
collection: k8s
version: "1.31.6"
title: "Pod Disruption Budget"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/glossary/pod-disruption-budget.md
fetched_at: 2026-01-16T10:18:07+05:30
---
A [Pod Disruption Budget](/docs/concepts/workloads/pods/disruptions/) allows an 
 application owner to create an object for a replicated application, that ensures 
 a certain number or percentage of Pods
 with an assigned label will not be voluntarily evicted at any point in time.

<!--more--> 

Involuntary disruptions cannot be prevented by PDBs; however they 
do count against the budget.
