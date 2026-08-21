---
collection: libvirt
version: "12.7.0"
title: "Knowledge base"
source_url: https://libvirt.org/kbase/index.html
fetched_at: 2026-08-21T04:09:31+00:00
---
# Knowledge base

# Usage

[Secure usage](secureusage.md)
:   Secure usage of the libvirt APIs

[Backing chain management](backing_chains.md)
:   Explanation of how disk backing chain specification impacts libvirt's
    behaviour and basic troubleshooting steps of disk problems.

[Virtiofs](virtiofs.md)
:   Share a filesystem between the guest and the host

[Security with QEMU passthrough](qemu-passthrough-security.md)
:   Examination of the security protections used for QEMU and how they need
    configuring to allow use of QEMU passthrough with host files/devices.

[TLS certificates](tlscerts.md)
:   Generate and deploy x509 certificates for TLS.

[RPM deployment](rpm-deployment.md)
:   Explanation of the different RPM packages and illustration of which to
    pick for installation

[Domain state capture](domainstatecapture.md)
:   Comparison between different methods of capturing domain state

[Disk locking](locking.md)
:   Ensuring exclusive guest access to disks with
    [virtlockd](locking-lockd.md) or
    [Sanlock](locking-sanlock.md)

[Protected virtualization on s390](s390_protected_virt.md)
:   Running secure s390 guests with IBM Secure Execution

[Launch security](launch_security_sev.md)
:   Securely launching VMs with AMD SEV

[Live full disk backup](live_full_disk_backup.md)
:   A walkthrough of how to take effective live full disk backups.

[Merging disk image chains](merging_disk_image_chains.md)
:   Ways to reduce or consolidate disk image chains.

[KVM real time](kvm-realtime.md)
:   Run real time workloads in guests on a KVM hypervisor

[PCI hotplug](../pci-hotplug.md)
:   Effective usage of PCI hotplug

[PCI topology](../pci-addresses.md)
:   Addressing schemes for PCI devices

[Memory devices](memorydevices.md)
:   Memory devices and their use

[Snapshots](snapshots.md)
:   Details about snapshotting a VM

[Secure Boot](secureboot.md)
:   Enable and disable the Secure Boot feature

[Connection fail after installation](failed_connection_after_install.md)
:   Explanation of a common issue users stumble upon after installation

# Debugging

[Debug logs](debuglogs.md)
:   Configuration of logging and tips on how to file a good bug report.

[Systemtap](systemtap.md)
:   Explanation of how to use systemtap for libvirt tracing.

[Capturing core dumps for QEMU](qemu-core-dump.md)
:   How to configure libvirt to enable capture of core dumps from
    QEMU virtual machines

# Internals

[Incremental backup internals](internals/incremental-backup.md)
:   Incremental backup implementation details relevant for users

[VM migration internals](internals/migration.md)
:   VM migration implementation details, complementing the info in
    [migration](../migration.md)

[API call flow overview](internals/overview.md)
:   Overview of how an API call is handled by the libvirt library and passed
    over RPC to the daemon.

[Spawning commands](internals/command.md)
:   Spawning commands from libvirt driver code

[Event loop and worker pool](internals/eventloop.md)
:   Libvirt's event loop and worker pool mode

[Lock managers](internals/locking.md)
:   Use lock managers to protect disk content

[RPC protocol & APIs](internals/rpc.md)
:   RPC protocol information and API / dispatch guide

[QEMU driver threading](internals/qemu-threads.md)
:   Basics of locking and threaded access to qemu driver primitives.

[QEMU migration internals](internals/qemu-migration.md)
:   Description of migration phases in the v2 and v3 migration protocol.

[QEMU monitor event handling](internals/qemu-event-handlers.md)
:   Brief outline how events emitted by qemu on the monitor are handlded.
