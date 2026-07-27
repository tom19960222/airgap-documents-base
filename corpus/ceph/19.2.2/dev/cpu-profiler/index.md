---
collection: ceph
version: "19.2.2"
title: "Installing Oprofile"
source_url: https://docs.ceph.com/en/squid/dev/cpu-profiler/
fetched_at: 2026-07-27T16:41:16+00:00
---
# Installing Oprofile

The easiest way to profile Ceph’s CPU consumption is to use the [oprofile](http://oprofile.sourceforge.net/about/)
system-wide profiler.

## Installation

If you are using a Debian/Ubuntu distribution, you can install `oprofile` by
executing the following:

```
sudo apt-get install oprofile oprofile-gui
```

## Compiling Ceph for Profiling

To compile Ceph for profiling, first clean everything.

```
git clean -dfx
```

Finally, compile Ceph.

```
    ./do-cmake.sh -DCMAKE_CXX_FLAGS="-fno-omit-frame-pointer -O2 -g"
cd build
cmake --build .
```

In this command, `CMAKE_CXX_FLAGS` is specified. This provides callgraph output.

## Ceph Configuration

Ensure that you disable `lockdep`. Consider setting logging to
levels appropriate for a production cluster. See [Ceph Logging and Debugging](../../rados/troubleshooting/log-and-debug.md)
for details.

See the [CPU Profiling](../../rados/troubleshooting/cpu-profiling.md) section of the RADOS Troubleshooting documentation for details on using Oprofile.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
