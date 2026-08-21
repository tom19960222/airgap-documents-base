---
collection: rook
version: "1.17.2"
title: "Performance Profiling"
source_url: https://rook.io/docs/rook/v1.17/Troubleshooting/performance-profiling/
fetched_at: 2026-08-21T02:34:45+00:00
---
# Performance Profiling

## Collect perf data of a ceph process at runtime

> **Warn:**
>
> This is an advanced topic please be aware of the steps you're performing or reach out to the experts for further guidance.

There are some cases where the debug logs are not sufficient to investigate issues like high CPU utilization of a Ceph process. In that situation, coredump and perf information of a Ceph process is useful to be collected which can be shared with the Ceph team in an issue.

To collect this information, please follow these steps:

- Edit the rook-ceph-operator deployment and set `ROOK_HOSTPATH_REQUIRES_PRIVILEGED` to `true`.
- Wait for the pods to get reinitialized:

```
# watch kubectl -n rook-ceph get pods
```

- Enter the respective pod of the Ceph process which needs to be investigated. For example:

```
# kubectl -n rook-ceph exec -it deploy/rook-ceph-mon-a -- bash
```

- Install `gdb` , `perf` and `git` inside the pod. For example:

```
# dnf install gdb git perf -y
```

- Capture perf data of the respective Ceph process:

```
# perf record -e cycles --call-graph dwarf -p <pid of the process>
# perf report > perf_report_<process/thread>
```

- Grab the `pid` of the respective Ceph process to collect its backtrace at multiple time instances, attach `gdb` to it and share the output `gdb.txt`:

```
# gdb -p <pid_of_the_process>

- set pag off
- set log on
- thr a a bt full # This captures the complete backtrace of the process
- backtrace
- Ctrl+C
- backtrace
- Ctrl+C
- backtrace
- Ctrl+C
- backtrace
- set log off
- q (to exit out of gdb)
```

- Grab the live coredump of the respective process using `gcore`:

```
# gcore <pid_of_the_process>
```

- Capture the [Wallclock Profiler](https://github.com/markhpc/gdbpmp) data for the respective Ceph process and share the output `gdbpmp.data` generated:

```
# git clone https://github.com/markhpc/gdbpmp
# cd gdbpmp
# ./gdbpmp.py -p <pid_of_the_process> -n 100 -o gdbpmp.data
```

- Collect the `perf.data`, `perf_report`, backtrace of the process `gdb.txt` , `core` file and profiler data `gdbpmp.data` and upload it to the tracker issue for troubleshooting purposes.
