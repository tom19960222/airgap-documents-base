---
collection: ceph
version: "20.2.4"
title: "Install Ceph Storage Cluster"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/install/install-storage-cluster.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Install Ceph Storage Cluster

This guide describes installing Ceph packages manually. This procedure
is only for users who are not installing with a deployment tool such as
`cephadm`, `chef`, `juju`, etc.

# Installing with APT

Once you have added either release or development packages to APT, you should
update APT's database and install Ceph:

```bash
sudo apt-get update && sudo apt-get install ceph ceph-mds
```

# Installing with RPM

To install Ceph with RPMs, execute the following steps:

1. Install `yum-plugin-priorities`:

```bash
sudo yum install yum-plugin-priorities
```

1. Ensure `/etc/yum/pluginconf.d/priorities.conf` exists.

1. Ensure `priorities.conf` enables the plugin:

```
[main]
enabled = 1
```

1. Ensure your YUM `ceph.repo` entry includes `priority=2`. See
   Get Packages for details:

```
[ceph]
name=Ceph packages for $basearch
baseurl=https://download.ceph.com/rpm-{ceph-release}/{distro}/$basearch
enabled=1
priority=2
gpgcheck=1
gpgkey=https://download.ceph.com/keys/release.asc

[ceph-noarch]
name=Ceph noarch packages
baseurl=https://download.ceph.com/rpm-{ceph-release}/{distro}/noarch
enabled=1
priority=2
gpgcheck=1
gpgkey=https://download.ceph.com/keys/release.asc

[ceph-source]
name=Ceph source packages
baseurl=https://download.ceph.com/rpm-{ceph-release}/{distro}/SRPMS
enabled=0
priority=2
gpgcheck=1
gpgkey=https://download.ceph.com/keys/release.asc
```

1. Install pre-requisite packages:

```bash
sudo yum install snappy gdisk python-argparse gperftools-libs
```

Once you have added either release or development packages, or added a
`ceph.repo` file to `/etc/yum.repos.d`, you can install Ceph packages:

```bash
sudo yum install ceph
```

# Installing a Build

If you build Ceph from source code, you may install Ceph in user space by
executing the following:

```bash
sudo ninja install
```

If you install Ceph locally, `ninja` will place the executables in
`usr/local/bin`. You may add the Ceph configuration file to the
`usr/local/bin` directory to run Ceph from a single directory.

.. _Get Packages: ../get-packages
