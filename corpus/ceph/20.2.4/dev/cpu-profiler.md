---
collection: ceph
version: "20.2.4"
title: "Installing Oprofile"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/cpu-profiler.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Installing Oprofile

The easiest way to profile Ceph's CPU consumption is to use the oprofile
system-wide profiler.

.. _oprofile: http://oprofile.sourceforge.net/about/

# Installation

If you are using a Debian/Ubuntu distribution, you can install `oprofile` by
executing the following::

	sudo apt-get install oprofile oprofile-gui

# Compiling Ceph for Profiling

To compile Ceph for profiling, first clean everything. :

```
git clean -dfx
```

Finally, compile Ceph. ::

	./do-cmake.sh -DCMAKE_CXX_FLAGS="-fno-omit-frame-pointer -O2 -g"
    cd build
    cmake --build .

In this command, `CMAKE_CXX_FLAGS` is specified. This provides callgraph output.

# Ceph Configuration

Ensure that you disable `lockdep`. Consider setting logging to
levels appropriate for a production cluster. See Ceph Logging and Debugging
for details.

.. _Ceph Logging and Debugging: ../../rados/troubleshooting/log-and-debug

See the CPU Profiling section of the RADOS Troubleshooting documentation for details on using Oprofile.

.. _CPU Profiling: ../../rados/troubleshooting/cpu-profiling
