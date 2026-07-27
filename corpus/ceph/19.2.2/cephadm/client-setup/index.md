---
collection: ceph
version: "19.2.2"
title: "Basic Ceph Client Setup"
source_url: https://docs.ceph.com/en/squid/cephadm/client-setup/
fetched_at: 2026-07-27T16:39:02+00:00
---
# Basic Ceph Client Setup

Client hosts require basic configuration to interact with
Ceph clusters. This section describes how to perform this configuration.

> **Note:**
>
> Most client hosts need to install only the `ceph-common` package
> and its dependencies. Such an installation supplies the basic `ceph` and
> `rados` commands, as well as other commands including `mount.ceph`
> and `rbd`.

## Config File Setup

Client hosts usually require smaller configuration files (here
sometimes called “config files”) than do back-end cluster hosts.
To generate a minimal config file, log into a host that has been
configured as a client or that is running a cluster daemon, then
run the following command:

```
ceph config generate-minimal-conf
```

This command generates a minimal config file that tells the client how
to reach the Ceph Monitors. This file should usually
be copied to `/etc/ceph/ceph.conf` on each client host.

## Keyring Setup

Most Ceph clusters run with authentication enabled. This means that
the client needs keys in order to communicate with Ceph daemons.
To generate a keyring file with credentials for `client.fs`,
log into an running cluster member and run the following command:

```
ceph auth get-or-create client.fs
```

The resulting output is directed into a keyring file, typically
`/etc/ceph/ceph.keyring`.

To gain a broader understanding of client keyring distribution and administration,
you should read [Client keyrings and configs](../operations/index.md#client-keyrings-and-configs).

To see an example that explains how to distribute `ceph.conf` configuration
files to hosts that are tagged with the `bare_config` label, you should read
the subsection named “Distributing ceph.conf to hosts tagged with bare_config”
under the heading [/etc/ceph/ceph.conf](../operations/index.md#etc-ceph-conf-distribution).

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
