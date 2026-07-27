---
collection: ceph
version: "19.2.2"
title: "GDB - The GNU Project Debugger"
source_url: https://docs.ceph.com/en/squid/dev/developer_guide/debugging-gdb/
fetched_at: 2026-07-27T16:41:11+00:00
---
# GDB - The GNU Project Debugger

[The GNU Project Debugger (GDB)](https://www.sourceware.org/gdb) is
a powerful tool that allows you to analyze the execution flow
of a process.
GDB can help to find bugs, uncover crash errors or track the
source code during execution of a development cluster.
It can also be used to debug Teuthology tests runs.

## GET STARTED WITH GDB

Basic usage with examples can be found [here.](https://geeksforgeeks.org/gdb-command-in-linux-with-examples)
GDB can be attached to a running process. For instance, after deploying a
development cluster, the process number (PID) of a `ceph-osd` daemon can be found in:

```
$ cd build
$ cat out/osd.0.pid
```

Attaching gdb to the process:

```
$ gdb ./bin/ceph-osd -p <pid>
```

> **Note:**
>
> It is recommended to compile without any optimizations (`-O0` gcc flag)
> in order to avoid elimintaion of intermediate values.

Stopping for breakpoints while debugging may cause timeouts, so the following
configuration options are suggested:

```
[osd]
osd_op_thread_timeout = 1500
osd_op_thread_suicide_timeout = 1500
```

### Debugging Teuthology Tests

`src/script/ceph-debug-docker.sh` can be used to analyze Teuthology failures:

```
$ ./ceph-debug-docker.sh <branch-name>
```

Refer to the script header for more information.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
