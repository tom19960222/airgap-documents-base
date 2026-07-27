---
collection: ceph
version: "19.2.2"
title: "Hello World Module"
source_url: https://docs.ceph.com/en/squid/mgr/hello/
fetched_at: 2026-07-27T16:40:53+00:00
---
# Hello World Module

This is a simple module skeleton for documentation purposes.

## Enabling

Run the following command to enable the `hello` module:

```
ceph mgr module enable hello
```

Run the following command to ensure that the `hello` module is enabled:

```
ceph mgr module ls
```

After editing the module file (found in `src/pybind/mgr/hello/module.py`),
reload the module in order to pick up the changes by running the following
commands:

```
ceph mgr module disable hello
ceph mgr module enable hello
```

Alternatively, run the following command to reload the `hello` module and pick up changes to its settings:

```
init-ceph restart mgr
```

Run the following command to run the module:

```
ceph hello
```

The log is found in the following file:

```
build/out/mgr.x.log
```

## Documenting

After adding a new mgr module, be sure to add its documentation to
`doc/mgr/module_name.rst`. Also, add a link to your new module into
`doc/mgr/index.rst`.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
