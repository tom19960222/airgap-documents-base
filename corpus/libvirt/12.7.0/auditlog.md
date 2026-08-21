---
collection: libvirt
version: "12.7.0"
title: "Audit log"
source_url: https://libvirt.org/auditlog.html
fetched_at: 2026-08-21T04:10:08+00:00
---
# Audit log

Contents

- [Introduction](auditlog.md#introduction)
- [Configuration](auditlog.md#configuration)
- [Message types](auditlog.md#message-types)

  - [VIRT_CONTROL](auditlog.md#virt-control)
  - [VIRT_MACHINE_ID](auditlog.md#virt-machine-id)
  - [VIRT_RESOURCE](auditlog.md#virt-resource)

    - [Virtual CPU](auditlog.md#virtual-cpu)
    - [Memory](auditlog.md#memory)
    - [Disk](auditlog.md#disk)
    - [Network interface](auditlog.md#network-interface)
    - [Filesystem](auditlog.md#filesystem)
    - [Host device](auditlog.md#host-device)
    - [TPM](auditlog.md#tpm)
    - [RNG](auditlog.md#rng)
    - [console/serial/parallel/channel](auditlog.md#console-serial-parallel-channel)
    - [smartcard](auditlog.md#smartcard)
    - [Redirected device](auditlog.md#redirected-device)
    - [Control group](auditlog.md#control-group)
    - [Shared memory](auditlog.md#shared-memory)

# [Introduction](auditlog.md#id1)

A number of the libvirt virtualization drivers (QEMU/KVM and LXC)
include support for logging details of important operations to the
host's audit subsystem. This provides administrators / auditors with a
canonical historical record of changes to virtual machines' /
containers' lifecycle states and their configuration. On hosts which are
running the Linux audit daemon, the logs will usually end up in
/var/log/audit/audit.log

# [Configuration](auditlog.md#id2)

The libvirt audit integration is enabled by default on any host which
has the Linux audit subsystem active, and disabled otherwise. It is
possible to alter this behaviour in the /etc/libvirt/libvirtd.conf
configuration file, via the audit_level parameter

- audit_level=0 - libvirt auditing is disabled regardless of host
  audit subsystem enablement.
- audit_level=1 - libvirt auditing is enabled if the host audit
  subsystem is enabled, otherwise it is disabled. This is the default
  behaviour.
- audit_level=2 - libvirt auditing is enabled regardless of host
  audit subsystem enablement. If the host audit subsystem is disabled,
  then libvirtd will refuse to complete startup and exit with an error.

In addition to have formal messages sent to the audit subsystem it is
possible to tell libvirt to inject messages into its own logging layer.
This will result in messages ending up in the systemd journal or
/var/log/libvirt/libvirtd.log on non-systemd hosts. This is disabled
by default, but can be requested by setting the audit_logging=1
configuration parameter in the same file mentioned above.

# [Message types](auditlog.md#id3)

Libvirt defines three core audit message types each of which will be
described below. There are a number of common fields that will be
reported for all message types.

pid
:   Process ID of the libvirtd daemon generating the audit record.

uid
:   User ID of the libvirtd daemon process generating the audit record.

subj
:   Security context of the libvirtd daemon process generating the audit
    record.

msg
:   String containing a list of key=value pairs specific to the type of
    audit record being reported.

Some fields in the msg string are common to audit records

virt
:   Type of virtualization driver used. One of qemu or lxc

vm
:   Host driver unique name of the guest

uuid
:   Globally unique identifier for the guest

exe
:   Path of the libvirtd daemon

hostname
:   Currently unused

addr
:   Currently unused

terminal
:   Currently unused

res
:   Result of the action, either success or failed

## [VIRT_CONTROL](auditlog.md#id4)

Reports change in the lifecycle state of a virtual machine. The msg
field will include the following sub-fields

op
:   Type of operation performed. One of start, stop or init

reason
:   The reason which caused the operation to happen

vm-pid
:   ID of the primary/leading process associated with the guest

init-pid
:   ID of the init process in a container. Only if op=init and
    virt=lxc

pid-ns
:   Namespace ID of the init process in a container. Only if
    op=init and virt=lxc

## [VIRT_MACHINE_ID](auditlog.md#id5)

Reports the association of a security context with a guest. The msg
field will include the following sub-fields

model
:   The security driver type. One of selinux or apparmor

vm-ctx
:   Security context for the guest process

img-ctx
:   Security context for the guest disk images and other assigned host
    resources

## [VIRT_RESOURCE](auditlog.md#id6)

Reports the usage of a host resource by a guest. The fields include will
vary according to the type of device being reported. When the guest is
initially booted records will be generated for all assigned resources.
If any changes are made to the running guest configuration, for example
hotplug devices, or adjust resources allocation, further records will be
generated.

### [Virtual CPU](auditlog.md#id7)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to vcpu

old-vcpu
:   Original vCPU count, or 0

new-vcpu
:   Updated vCPU count

### [Memory](auditlog.md#id8)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to mem

old-mem
:   Original memory size in bytes, or 0

new-mem
:   Updated memory size in bytes

### [Disk](auditlog.md#id9)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to disk

old-disk
:   Original host file or device path acting as the disk backing file

new-disk
:   Updated host file or device path acting as the disk backing file

### [Network interface](auditlog.md#id10)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to net

old-net
:   Original MAC address of the guest network interface

new-net
:   Updated MAC address of the guest network interface

If there is a host network interface associated with the guest NIC then
further records may be generated

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to net

net
:   MAC address of the host network interface

rdev
:   Name of the host network interface

### [Filesystem](auditlog.md#id11)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to fs

old-fs
:   Original host directory, file or device path backing the filesystem

new-fs
:   Updated host directory, file or device path backing the filesystem

### [Host device](auditlog.md#id12)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to hostdev or dev

dev
:   The unique bus identifier of the USB, PCI or SCSI device, if
    resrc=dev

disk
:   The path of the block device assigned to the guest, if
    resrc=hostdev

chardev
:   The path of the character device assigned to the guest, if
    resrc=hostdev

### [TPM](auditlog.md#id13)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to tpm or tpm-emulator

device
:   The path of the host TPM device assigned to the guest

### [RNG](auditlog.md#id14)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to rng

old-rng
:   Original path of the host entropy source for the RNG

new-rng
:   Updated path of the host entropy source for the RNG

### [console/serial/parallel/channel](auditlog.md#id15)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to chardev

old-chardev
:   Original path of the backing character device for given emulated
    device

new-chardev
:   Updated path of the backing character device for given emulated
    device

### [smartcard](auditlog.md#id16)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to smartcard

old-smartcard
:   Original path of the backing character device, certificate store or
    "nss-smartcard-device" for host smartcard passthrough.

new-smartcard
:   Updated path of the backing character device, certificate store or
    "nss-smartcard-device" for host smartcard passthrough.

### [Redirected device](auditlog.md#id17)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to redir

bus
:   The bus type, only usb allowed

device
:   The device type, only USB redir allowed

### [Control group](auditlog.md#id18)

The msg field will include the following sub-fields

reason
:   The reason which caused the resource to be assigned to happen

resrc
:   The type of resource assigned. Set to cgroup

cgroup
:   The name of the cgroup controller

### [Shared memory](auditlog.md#id19)

The msg field will include the following sub-fields

resrc
:   The type of resource assigned. Set to shmem

reason
:   The reason which caused the resource to be assigned to happen

size
:   The size of the shared memory region

shmem
:   Name of the shared memory region

source
:   Path of the backing character device for given emulated device
