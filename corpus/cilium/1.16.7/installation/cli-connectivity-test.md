---
collection: cilium
version: "1.16.7"
title: "cli-connectivity-test"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/cli-connectivity-test.rst
fetched_at: 2025-02-13T12:04:31Z
---
Run the following command to validate that your cluster has proper network
connectivity:

```shell-session
$ cilium connectivity test
ℹ️  Monitor aggregation detected, will skip some flow validation steps
✨ [k8s-cluster] Creating namespace for connectivity check...
(...)
---------------------------------------------------------------------------------------------------------------------
📋 Test Report
---------------------------------------------------------------------------------------------------------------------
✅ 69/69 tests successful (0 warnings)
```

> **Note:**
> The connectivity test may fail to deploy due to too many open files in one
> or more of the pods. If you notice this error, you can increase the
> ``inotify`` resource limits on your host machine (see
> [Pod errors due to "too many open files"](https://kind.sigs.k8s.io/docs/user/known-issues/#pod-errors-due-to-too-many-open-files)).

Congratulations! You have a fully functional Kubernetes cluster with Cilium. 🎉
