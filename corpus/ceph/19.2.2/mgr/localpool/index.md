---
collection: ceph
version: "19.2.2"
title: "Local Pool Module"
source_url: https://docs.ceph.com/en/squid/mgr/localpool/
fetched_at: 2026-07-27T16:40:51+00:00
---
# Local Pool Module

The `localpool` module can automatically create RADOS pools that are
localized to a subset of the overall cluster. For example, by default, it
creates a pool for each distinct `rack` in the cluster. This can be
useful for deployments where it is desirable to distribute some data locally
and other data globally across the cluster. One use case is measuring
performance and testing behavior of specific drive, NIC, or chassis models in
isolation.

## Enabling

To enable the `localpool` module, run the following command:

```
ceph mgr module enable localpool
```

## Configuring

The `localpool` module understands the following options:

subtree
:   > which CRUSH subtree type the module should create a pool for.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `rack`

failure_domain
:   > what failure domain we should separate data replicas across.
    >
    > type:
    > :   `str`
    >
    > default:
    > :   `host`

pg_num
:   > default pg_num for any created local pool
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `128`

num_rep
:   > default replica count for any created local pool
    >
    > type:
    > :   `int`
    >
    > default:
    > :   `3`

min_size
:   > value to set min_size to (unchanged from Ceph’s default if this option
    > is not set)
    >
    > type:
    > :   `int`

prefix
:   > name prefix for any created local pool
    >
    > type:
    > :   `str`
    >
    > default:
    > :   <empty string>

The default is `by-$subtreetype-`.

These options are set via the `config-key` interface. For example, to change
the replication level to 2x with 64 PGs, run the following two commands:

```
ceph config set mgr mgr/localpool/num_rep 2
ceph config set mgr mgr/localpool/pg_num 64
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
