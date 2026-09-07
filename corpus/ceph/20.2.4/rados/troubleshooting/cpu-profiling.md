---
collection: ceph
version: "20.2.4"
title: "CPU Profiling"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/rados/troubleshooting/cpu-profiling.rst
fetched_at: 2026-08-18T01:32:45Z
---
# CPU Profiling

If you built Ceph from source and compiled Ceph for use with [oprofile](http://oprofile.sourceforge.net/about/)
you can profile Ceph's CPU usage. See [Installing Oprofile](../../dev/cpu-profiler.md) for details.

# Initializing oprofile

``oprofile`` must be initalized the first time it is used. Locate the
``vmlinux`` image that corresponds to the kernel you are running:

```bash
ls /boot
sudo opcontrol --init
sudo opcontrol --setup --vmlinux={path-to-image} --separate=library --callgraph=6
```

# Starting oprofile

Run the following command to start ``oprofile``:

```bash
opcontrol --start
```

# Stopping oprofile

Run the following command to stop ``oprofile``:

```bash
opcontrol --stop
```

# Retrieving oprofile Results

Run the following command to retrieve the top ``cmon`` results:

```bash
opreport -gal ./cmon | less
```

Run the following command to retrieve the top ``cmon`` results, with call
graphs attached:

```bash
opreport -cal ./cmon | less
```

> **Important:** After you have reviewed the results, reset ``oprofile`` before
> running it again. The act of resetting ``oprofile`` removes data from the
> session directory.

# Resetting oprofile

Run the following command to reset ``oprofile``:

```bash
sudo opcontrol --reset
```

> **Important:** Reset ``oprofile`` after analyzing data. This ensures that
> results from prior tests do not get mixed in with the results of the current
> test.
