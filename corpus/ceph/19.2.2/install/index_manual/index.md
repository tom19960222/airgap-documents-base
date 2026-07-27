---
collection: ceph
version: "19.2.2"
title: "Installation (Manual)"
source_url: https://docs.ceph.com/en/squid/install/index_manual/
fetched_at: 2026-07-27T16:38:58+00:00
---
# Installation (Manual)

## Get Software

There are several methods for getting Ceph software. The easiest and most common
method is to [get packages](../get-packages.md) by adding repositories for use with package
management tools such as the Advanced Package Tool (APT) or Yellowdog Updater,
Modified (YUM). You may also retrieve pre-compiled packages from the Ceph
repository. Finally, you can retrieve tarballs or clone the Ceph source code
repository and build Ceph yourself.

- [Get Packages](../get-packages/index.md)
- [Get Tarballs](../get-tarballs/index.md)
- [Clone Source](../clone-source/index.md)
- [Build Ceph](../build-ceph/index.md)
- [Ceph Mirrors](../mirrors/index.md)
- [Ceph Containers](../containers/index.md)

## Install Software

Once you have the Ceph software (or added repositories), installing the software
is easy. To install packages on each [Ceph Node](../../glossary/index.md#term-Ceph-Node) in your cluster, use package
management tools. You should install Yum Priorities for RHEL/CentOS and other
distributions that use Yum if you intend to install the Ceph Object Gateway or
QEMU.

- [Install Ceph Storage Cluster](../install-storage-cluster/index.md)
- [Install Virtualization for Block](../install-vm-cloud/index.md)

## Deploy a Cluster Manually

Once you have Ceph installed on your nodes, you can deploy a cluster manually.
The manual procedure is primarily for exemplary purposes for those developing
deployment scripts with Chef, Juju, Puppet, etc.

- [Manual Deployment](../manual-deployment/index.md)
  - [Monitor Bootstrapping](../manual-deployment/index.md#monitor-bootstrapping)
  - [Manager daemon configuration](../manual-deployment/index.md#manager-daemon-configuration)
  - [Adding OSDs](../manual-deployment/index.md#adding-osds)
    - [Short Form](../manual-deployment/index.md#short-form)
    - [Long Form](../manual-deployment/index.md#long-form)
  - [Adding MDS](../manual-deployment/index.md#adding-mds)
  - [Manually Installing RADOSGW](../manual-deployment/index.md#manually-installing-radosgw)
  - [Summary](../manual-deployment/index.md#summary)
- [Manual Deployment on FreeBSD](../manual-freebsd-deployment/index.md)
  - [Disklayout on FreeBSD](../manual-freebsd-deployment/index.md#disklayout-on-freebsd)
    - [Configuration](../manual-freebsd-deployment/index.md#configuration)
  - [Monitor Bootstrapping](../manual-freebsd-deployment/index.md#monitor-bootstrapping)
  - [Adding OSDs](../manual-freebsd-deployment/index.md#adding-osds)
    - [Long Form](../manual-freebsd-deployment/index.md#long-form)
  - [Adding MDS](../manual-freebsd-deployment/index.md#adding-mds)
  - [Summary](../manual-freebsd-deployment/index.md#summary)

## Upgrade Software

As new versions of Ceph become available, you may upgrade your cluster to take
advantage of new functionality. Read the upgrade documentation before you
upgrade your cluster. Sometimes upgrading Ceph requires you to follow an upgrade
sequence.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
