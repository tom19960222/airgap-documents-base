---
collection: ceph
version: "20.2.4"
title: "Converting an existing cluster to cephadm"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/cephadm/adoption.rst
fetched_at: 2026-08-18T01:32:45Z
---
.. _cephadm-adoption:

# Converting an existing cluster to cephadm

It is possible to convert some existing clusters so that they can be managed
with `cephadm`. This statement applies to some clusters that were deployed
with `ceph-deploy`, `ceph-ansible`, or `DeepSea`.

This section of the documentation explains how to determine whether your
clusters can be converted to a state in which they can be managed by
`cephadm` and how to perform those conversions.

## Limitations

* Cephadm works only with BlueStore OSDs.

## Preparation

1. Make sure that the `cephadm` command line tool is available on each host
   in the existing cluster.  See get-cephadm to learn how.

1. Prepare each host for use by `cephadm` by running this command on that host:

```bash
cephadm prepare-host
```

1. Choose a version of Ceph to use for the conversion. This procedure will work
   with any release of Ceph that is Octopus (15.2.z) or later.  The
   latest stable release of Ceph is the default. You might be upgrading from an
   earlier Ceph release at the same time that you're performing this
   conversion.  If you are upgrading from an earlier release, make sure to
   follow any upgrade-related instructions for that release.

   Pass the Ceph container image to cephadm with the following command:

```bash
cephadm --image $IMAGE <rest of command goes here>
```

   The conversion begins.

1. Confirm that the conversion is underway by running `cephadm ls` and
   making sure that the style of the daemons is changed:

```bash
cephadm ls
```

   Before starting the conversion process, `cephadm ls` reports all existing
   daemons with the style `legacy`. As the adoption process progresses,
   adopted daemons will appear with the style `cephadm:v1`.

## Adoption process

1. Make sure that the ceph configuration has been migrated to use the cluster's
   central config database.  If `/etc/ceph/ceph.conf` is identical on all
   hosts, then the following command can be run on one host and will take
   effect for all hosts:

```bash
ceph config assimilate-conf -i /etc/ceph/ceph.conf
```

   If there are configuration variations between hosts, you will need to repeat
   this command on each host, taking care that if there are conflicting option
   settings across hosts, the values from the last host will be used. During this
   adoption process, view the cluster's central
   configuration to confirm that it is complete by running the following
   command:

```bash
ceph config dump
```

1. Adopt each Monitor:

```bash
cephadm adopt --style legacy --name mon.<hostname>
```

   Each legacy Monitor will stop, quickly restart as a cephadm
   container, and rejoin the quorum.

1. Adopt each Manager:

```bash
cephadm adopt --style legacy --name mgr.<hostname>
```

1. Enable cephadm orchestration:

```bash
ceph mgr module enable cephadm
ceph orch set backend cephadm
```

1. Generate an SSH key for cephadm:

```bash
ceph cephadm generate-key
ceph cephadm get-pub-key > ~/ceph.pub
```

1. Install the cephadm SSH key on each host in the cluster:

```bash
ssh-copy-id -f -i ~/ceph.pub root@<host>
```

> **Note:**
> It is also possible to import an existing SSH key. See
> SSH errors in the troubleshooting
> document for instructions that describe how to import existing
> SSH keys.

> **Note:**
> It is also possible to arrange for cephadm to use a non-root user to SSH
> into cluster hosts. This user needs to have passwordless sudo access.
> Use `ceph cephadm set-user <user>` and copy the SSH key to that user's
> home directory on each host.
> See cephadm-ssh-user

1. Tell cephadm which hosts to manage:

```bash
ceph orch host add <hostname> [ip-address]
```

   This will run `cephadm check-host` on each host before adding it.
   This check ensures that the host is functioning properly. The IP address
   argument is recommended. If the address is not provided, then the host name
   will be resolved via DNS.

1. Verify that the adopted monitor and manager daemons are visible:

```bash
ceph orch ps
```

1. Adopt all OSDs in the cluster:

```bash
cephadm adopt --style legacy --name <name>
```

   For example:

```bash
cephadm adopt --style legacy --name osd.1
cephadm adopt --style legacy --name osd.2
```

1. Redeploy CephFS MDS daemons (if deployed) by telling cephadm how many daemons to run for
   each file system. List CephFS file systems by name with the command ``ceph fs
   ls``. Run the following command on the master nodes to redeploy the MDS
   daemons:

```bash
ceph orch apply mds <fs-name> [--placement=<placement>]
```

   For example, in a cluster with a single file system called `foo`:

```bash
ceph fs ls
```

```bash
name: foo, metadata pool: foo_metadata, data pools: [foo_data ]
```

```bash
ceph orch apply mds foo 2
```

   Confirm that the new MDS daemons have started:

```bash
ceph orch ps --daemon-type mds
```

   Finally, stop and remove the legacy MDS daemons:

```bash
systemctl stop ceph-mds.target
rm -rf /var/lib/ceph/mds/ceph-*
```

1. Redeploy Ceph Object Gateway RGW daemons if deployed. Cephadm manages RGW
   daemons by zone. For each zone, deploy new RGW daemons with cephadm:

```bash
ceph orch apply rgw <svc_id> [--realm=<realm>] [--zone=<zone>] [--port=<port>] [--ssl] [--placement=<placement>]
```

   where *<placement>* can be a simple daemon count, or a list of
   specific hosts (see orchestrator-cli-placement-spec). The
   zone and realm arguments are needed only for a multisite setup.

   After the daemons have started and you have confirmed that they are
   functioning, stop and remove the legacy daemons:

```bash
systemctl stop ceph-rgw.target
rm -rf /var/lib/ceph/radosgw/ceph-*
```

1. Check the output of the command `ceph health detail` for cephadm warnings
   about stray cluster daemons or hosts that are not yet managed by cephadm.
