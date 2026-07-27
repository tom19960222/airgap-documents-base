---
collection: ceph
version: "19.2.2"
title: "CPU Profiling"
source_url: https://docs.ceph.com/en/squid/rados/troubleshooting/cpu-profiling/
fetched_at: 2026-07-27T16:39:48+00:00
---
# CPU Profiling

If you built Ceph from source and compiled Ceph for use with [oprofile](http://oprofile.sourceforge.net/about/)
you can profile Ceph’s CPU usage. See [Installing Oprofile](../../../dev/cpu-profiler.md) for details.

## Initializing oprofile

`oprofile` must be initalized the first time it is used. Locate the
`vmlinux` image that corresponds to the kernel you are running:

```
ls /boot
sudo opcontrol --init
sudo opcontrol --setup --vmlinux={path-to-image} --separate=library --callgraph=6
```

## Starting oprofile

Run the following command to start `oprofile`:

```
opcontrol --start
```

## Stopping oprofile

Run the following command to stop `oprofile`:

```
opcontrol --stop
```

## Retrieving oprofile Results

Run the following command to retrieve the top `cmon` results:

```
opreport -gal ./cmon | less
```

Run the following command to retrieve the top `cmon` results, with call
graphs attached:

```
opreport -cal ./cmon | less
```

> **Important:**
>
> After you have reviewed the results, reset `oprofile` before
> running it again. The act of resetting `oprofile` removes data from the
> session directory.

## Resetting oprofile

Run the following command to reset `oprofile`:

```
sudo opcontrol --reset
```

> **Important:**
>
> Reset `oprofile` after analyzing data. This ensures that
> results from prior tests do not get mixed in with the results of the current
> test.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
