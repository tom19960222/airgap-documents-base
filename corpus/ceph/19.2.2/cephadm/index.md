---
collection: ceph
version: "19.2.2"
title: "Cephadm"
source_url: https://docs.ceph.com/en/squid/cephadm/
fetched_at: 2026-07-27T16:38:45+00:00
---
# Cephadm

`cephadm` is a utility that is used to manage a Ceph cluster.

Here is a list of some of the things that `cephadm` can do:

- `cephadm` can add a Ceph container to the cluster.
- `cephadm` can remove a Ceph container from the cluster.
- `cephadm` can update Ceph containers.

`cephadm` does not rely on external configuration tools like Ansible, Rook,
or Salt. However, those external configuration tools can be used to automate
operations not performed by cephadm itself. To learn more about these external
configuration tools, visit their pages:

> - <https://github.com/ceph/cephadm-ansible>
> - <https://rook.io/docs/rook/v1.10/Getting-Started/intro/>
> - <https://github.com/ceph/ceph-salt>

`cephadm` manages the full lifecycle of a Ceph cluster. This lifecycle starts
with the bootstrapping process, when `cephadm` creates a tiny Ceph cluster on
a single node. This cluster consists of one monitor and one manager.
`cephadm` then uses the orchestration interface to expand the cluster, adding
hosts and provisioning Ceph daemons and services. Management of this lifecycle
can be performed either via the Ceph command-line interface (CLI) or via the
dashboard (GUI).

To use `cephadm` to get started with Ceph, follow the instructions in
[Using cephadm to Deploy a New Ceph Cluster](install/index.md#cephadm-deploying-new-cluster).

`cephadm` was introduced in Ceph release v15.2.0 (Octopus) and does not
support older versions of Ceph.

- [Compatibility and Stability](compatibility/index.md)
  - [Compatibility with Podman Versions](compatibility/index.md#compatibility-with-podman-versions)
  - [Stability](compatibility/index.md#stability)
- [Using cephadm to Deploy a New Ceph Cluster](install/index.md)
  - [Requirements](install/index.md#requirements)
  - [Install cephadm](install/index.md#install-cephadm)
  - [Bootstrap a new cluster](install/index.md#bootstrap-a-new-cluster)
  - [Enable Ceph CLI](install/index.md#enable-ceph-cli)
  - [Adding Hosts](install/index.md#adding-hosts)
  - [Adding additional MONs](install/index.md#adding-additional-mons)
  - [Adding Storage](install/index.md#adding-storage)
  - [Using Ceph](install/index.md#using-ceph)
  - [Different deployment scenarios](install/index.md#different-deployment-scenarios)
- [Converting an existing cluster to cephadm](adoption/index.md)
  - [Limitations](adoption/index.md#limitations)
  - [Preparation](adoption/index.md#preparation)
  - [Adoption process](adoption/index.md#adoption-process)
- [Host Management](host-management/index.md)
  - [Listing Hosts](host-management/index.md#listing-hosts)
  - [Adding Hosts](host-management/index.md#adding-hosts)
  - [Removing Hosts](host-management/index.md#removing-hosts)
  - [Host labels](host-management/index.md#host-labels)
  - [Maintenance Mode](host-management/index.md#maintenance-mode)
  - [Rescanning Host Devices](host-management/index.md#rescanning-host-devices)
  - [Creating many hosts at once](host-management/index.md#creating-many-hosts-at-once)
  - [Setting the initial CRUSH location of host](host-management/index.md#setting-the-initial-crush-location-of-host)
  - [Removing a host from the CRUSH map](host-management/index.md#removing-a-host-from-the-crush-map)
  - [OS Tuning Profiles](host-management/index.md#os-tuning-profiles)
  - [SSH Configuration](host-management/index.md#ssh-configuration)
  - [Fully qualified domain names vs bare host names](host-management/index.md#fully-qualified-domain-names-vs-bare-host-names)
- [Service Management](services/index.md)
  - [MON Service](services/mon/index.md)
  - [MGR Service](services/mgr/index.md)
  - [OSD Service](services/osd/index.md)
  - [RGW Service](services/rgw/index.md)
  - [MDS Service](services/mds/index.md)
  - [NFS Service](services/nfs/index.md)
  - [iSCSI Service](services/iscsi/index.md)
  - [Custom Container Service](services/custom-container/index.md)
  - [Monitoring Services](services/monitoring/index.md)
  - [SNMP Gateway Service](services/snmp-gateway/index.md)
  - [Tracing Services](services/tracing/index.md)
  - [SMB Service](services/smb/index.md)
  - [Service Status](services/index.md#service-status)
  - [Daemon Status](services/index.md#daemon-status)
  - [Service Specification](services/index.md#service-specification)
  - [Daemon Placement](services/index.md#daemon-placement)
  - [Extra Container Arguments](services/index.md#extra-container-arguments)
  - [Extra Entrypoint Arguments](services/index.md#extra-entrypoint-arguments)
  - [Custom Config Files](services/index.md#custom-config-files)
  - [Removing a Service](services/index.md#removing-a-service)
  - [Disabling automatic deployment of daemons](services/index.md#disabling-automatic-deployment-of-daemons)
- [Upgrading Ceph](upgrade/index.md)
  - [Starting the upgrade](upgrade/index.md#starting-the-upgrade)
  - [Monitoring the upgrade](upgrade/index.md#monitoring-the-upgrade)
  - [Canceling an upgrade](upgrade/index.md#canceling-an-upgrade)
  - [Post upgrade actions](upgrade/index.md#post-upgrade-actions)
  - [Potential problems](upgrade/index.md#potential-problems)
  - [Using customized container images](upgrade/index.md#using-customized-container-images)
  - [Staggered Upgrade](upgrade/index.md#staggered-upgrade)
- [Cephadm operations](operations/index.md)
  - [Watching cephadm log messages](operations/index.md#watching-cephadm-log-messages)
  - [Ceph daemon control](operations/index.md#ceph-daemon-control)
  - [Ceph daemon logs](operations/index.md#ceph-daemon-logs)
  - [Per-node cephadm logs](operations/index.md#per-node-cephadm-logs)
  - [Data location](operations/index.md#data-location)
  - [Health checks](operations/index.md#health-checks)
  - [Client keyrings and configs](operations/index.md#client-keyrings-and-configs)
  - [/etc/ceph/ceph.conf](operations/index.md#etc-ceph-ceph-conf)
  - [Limiting Password-less sudo Access](operations/index.md#limiting-password-less-sudo-access)
  - [Purging a cluster](operations/index.md#purging-a-cluster)
  - [Replacing a device](operations/index.md#replacing-a-device)
- [Client Setup](client-setup/index.md)
  - [Config File Setup](client-setup/index.md#config-file-setup)
  - [Keyring Setup](client-setup/index.md#keyring-setup)
- [Troubleshooting](troubleshooting/index.md)
  - [Pausing or Disabling cephadm](troubleshooting/index.md#pausing-or-disabling-cephadm)
  - [Per-service and Per-daemon Events](troubleshooting/index.md#per-service-and-per-daemon-events)
  - [Checking Cephadm Logs](troubleshooting/index.md#checking-cephadm-logs)
  - [Gathering Log Files](troubleshooting/index.md#gathering-log-files)
  - [Collecting Systemd Status](troubleshooting/index.md#collecting-systemd-status)
  - [List all Downloaded Container Images](troubleshooting/index.md#list-all-downloaded-container-images)
  - [Manually Running Containers](troubleshooting/index.md#manually-running-containers)
  - [SSH Errors](troubleshooting/index.md#ssh-errors)
  - [Failed to Infer CIDR network error](troubleshooting/index.md#failed-to-infer-cidr-network-error)
  - [Accessing the Admin Socket](troubleshooting/index.md#accessing-the-admin-socket)
  - [Running Various Ceph Tools](troubleshooting/index.md#running-various-ceph-tools)
  - [Restoring the Monitor Quorum](troubleshooting/index.md#restoring-the-monitor-quorum)
  - [Manually Deploying a Manager Daemon](troubleshooting/index.md#manually-deploying-a-manager-daemon)
  - [Capturing Core Dumps](troubleshooting/index.md#capturing-core-dumps)
  - [Running the Debugger with cephadm](troubleshooting/index.md#running-the-debugger-with-cephadm)
- [Cephadm Feature Planning](../dev/cephadm/index.md)
  - [Developing with cephadm](../dev/cephadm/developing-cephadm/index.md)
  - [Host Maintenance](../dev/cephadm/host-maintenance/index.md)
  - [Compliance Check](../dev/cephadm/compliance-check/index.md)
  - [Storage devices and OSDs management](../dev/cephadm/design/storage_devices_and_osds/index.md)
  - [Notes and Thoughts on Cephadm’s scalability](../dev/cephadm/scalability-notes/index.md)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
