---
collection: libvirt
version: "12.7.0"
title: "Control Groups Resource Management"
source_url: https://libvirt.org/cgroups.html
fetched_at: 2026-08-21T04:09:33+00:00
---
# Control Groups Resource Management

Contents

- [Required controllers](cgroups.md#required-controllers)
- [Current cgroups layout](cgroups.md#current-cgroups-layout)

  - [Systemd cgroups integration](cgroups.md#systemd-cgroups-integration)

    - [Systemd scope naming](cgroups.md#systemd-scope-naming)
    - [Systemd slice naming](cgroups.md#systemd-slice-naming)
    - [Systemd cgroup layout](cgroups.md#systemd-cgroup-layout)
  - [Non-systemd cgroups layout](cgroups.md#non-systemd-cgroups-layout)
- [Using custom partitions](cgroups.md#using-custom-partitions)

  - [Creating custom partitions (systemd)](cgroups.md#creating-custom-partitions-systemd)
  - [Creating custom partitions (non-systemd)](cgroups.md#creating-custom-partitions-non-systemd)
- [Resource management APIs/commands](cgroups.md#resource-management-apis-commands)

  - [Scheduler tuning](cgroups.md#scheduler-tuning)
  - [Block I/O tuning](cgroups.md#block-i-o-tuning)
  - [Memory tuning](cgroups.md#memory-tuning)
  - [Network tuning](cgroups.md#network-tuning)
- [Legacy cgroups layout](cgroups.md#legacy-cgroups-layout)

The QEMU and LXC drivers make use of the Linux "Control Groups" facility for
applying resource management to their virtual machines and containers.

# [Required controllers](cgroups.md#id1)

The control groups filesystem supports multiple "controllers". By default the
init system (such as systemd) should mount all controllers compiled into the
kernel at /sys/fs/cgroup/$CONTROLLER-NAME. Libvirt will never attempt to
mount any controllers itself, merely detect where they are mounted.

The QEMU driver is capable of using the cpuset, cpu, cpuacct,
memory, blkio and devices controllers. None of them are compulsory.
If any controller is not mounted, the resource management APIs which use it will
cease to operate. It is possible to explicitly turn off use of a controller,
even when mounted, via the /etc/libvirt/qemu.conf configuration file.

The LXC driver is capable of using the cpuset, cpu, cpuacct,
freezer, memory, blkio and devices controllers. The cpuacct,
devices and memory controllers are compulsory. Without them mounted, no
containers can be started. If any of the other controllers are not mounted, the
resource management APIs which use them will cease to operate.

# [Current cgroups layout](cgroups.md#id2)

As of libvirt 1.0.5 or later, the cgroups layout created by libvirt has been
simplified, in order to facilitate the setup of resource control policies by
administrators / management applications. The new layout is based on the
concepts of "partitions" and "consumers". A "consumer" is a cgroup which holds
the processes for a single virtual machine or container. A "partition" is a
cgroup which does not contain any processes, but can have resource controls
applied. A "partition" will have zero or more child directories which may be
either "consumer" or "partition".

As of libvirt 1.1.1 or later, the cgroups layout will have some slight
differences when running on a host with systemd 205 or later. The overall tree
structure is the same, but there are some differences in the naming conventions
for the cgroup directories. Thus the following docs split in two, one describing
systemd hosts and the other non-systemd hosts.

## [Systemd cgroups integration](cgroups.md#id3)

On hosts which use systemd, each consumer maps to a systemd scope unit, while
partitions map to a system slice unit.

### [Systemd scope naming](cgroups.md#id4)

The systemd convention is for the scope name of virtual machines / containers to
be of the general format machine-$NAME.scope. Libvirt forms the $NAME
part of this by concatenating the driver type with the id and truncated name of
the guest, and then escaping any systemd reserved characters. So for a guest
demo running under the lxc driver, we get a $NAME of
lxc-12345-demo which when escaped is lxc\x2d12345\x2ddemo. So the
complete scope name is machine-lxc\x2d12345\x2ddemo.scope. The scope names
map directly to the cgroup directory names.

### [Systemd slice naming](cgroups.md#id5)

The systemd convention for slice naming is that a slice should include the name
of all of its parents prepended on its own name. So for a libvirt partition
/machine/engineering/testing, the slice name will be
machine-engineering-testing.slice. Again the slice names map directly to the
cgroup directory names. Systemd creates three top level slices by default,
system.slice user.slice and machine.slice. All virtual machines or
containers created by libvirt will be associated with machine.slice by
default.

### [Systemd cgroup layout](cgroups.md#id6)

Given this, a possible systemd cgroups layout involving 3 qemu guests, 3 lxc
containers and 3 custom child slices, would be:

```
$ROOT
  |
  +- system.slice
  |   |
  |   +- libvirtd.service
  |
  +- machine.slice
      |
      +- machine-qemu\x2d1\x2dvm1.scope
      |   |
      |   +- libvirt
      |       |
      |       +- emulator
      |       +- vcpu0
      |       +- vcpu1
      |
      +- machine-qemu\x2d2\x2dvm2.scope
      |   |
      |   +- libvirt
      |       |
      |       +- emulator
      |       +- vcpu0
      |       +- vcpu1
      |
      +- machine-qemu\x2d3\x2dvm3.scope
      |   |
      |   +- libvirt
      |       |
      |       +- emulator
      |       +- vcpu0
      |       +- vcpu1
      |
      +- machine-engineering.slice
      |   |
      |   +- machine-engineering-testing.slice
      |   |   |
      |   |   +- machine-lxc\x2d11111\x2dcontainer1.scope
      |   |
      |   +- machine-engineering-production.slice
      |       |
      |       +- machine-lxc\x2d22222\x2dcontainer2.scope
      |
      +- machine-marketing.slice
          |
          +- machine-lxc\x2d33333\x2dcontainer3.scope
```

Prior libvirt 7.1.0 the topology doesn't have extra libvirt directory.

## [Non-systemd cgroups layout](cgroups.md#id7)

On hosts which do not use systemd, each consumer has a corresponding cgroup
named $VMNAME.libvirt-{qemu,lxc}. Each consumer is associated with exactly
one partition, which also have a corresponding cgroup usually named
$PARTNAME.partition. The exceptions to this naming rule is the top level
default partition for virtual machines and containers /machine.

Given this, a possible non-systemd cgroups layout involving 3 qemu guests, 3 lxc
containers and 2 custom child slices, would be:

```
$ROOT
  |
  +- machine
      |
      +- qemu-1-vm1.libvirt-qemu
      |   |
      |   +- emulator
      |   +- vcpu0
      |   +- vcpu1
      |
      +- qeme-2-vm2.libvirt-qemu
      |   |
      |   +- emulator
      |   +- vcpu0
      |   +- vcpu1
      |
      +- qemu-3-vm3.libvirt-qemu
      |   |
      |   +- emulator
      |   +- vcpu0
      |   +- vcpu1
      |
      +- engineering.partition
      |   |
      |   +- testing.partition
      |   |   |
      |   |   +- lxc-11111-container1.libvirt-lxc
      |   |
      |   +- production.partition
      |       |
      |       +- lxc-22222-container2.libvirt-lxc
      |
      +- marketing.partition
          |
          +- lxc-33333-container3.libvirt-lxc
```

# [Using custom partitions](cgroups.md#id8)

If there is a need to apply resource constraints to groups of virtual machines
or containers, then the single default partition /machine may not be
sufficiently flexible. The administrator may wish to sub-divide the default
partition, for example into "testing" and "production" partitions, and then
assign each guest to a specific sub-partition. This is achieved via a small
element addition to the guest domain XML config, just below the main domain
element

```
...
<resource>
  <partition>/machine/production</partition>
</resource>
...
```

Note that the partition names in the guest XML are using a generic naming
format, not the low level naming convention required by the underlying host OS.
That is, you should not include any of the .partition or .slice suffixes
in the XML config. Given a partition name /machine/production, libvirt will
automatically apply the platform specific translation required to get
/machine/production.partition (non-systemd) or
/machine.slice/machine-production.slice (systemd) as the underlying cgroup
name

Libvirt will not auto-create the cgroups directory to back this partition. In
the future, libvirt / virsh will provide APIs / commands to create custom
partitions, but currently this is left as an exercise for the administrator.

**Note:** the ability to place guests in custom partitions is only available
with libvirt >= 1.0.5, using the new cgroup layout. The legacy cgroups layout
described later in this document did not support customization per guest.

## [Creating custom partitions (systemd)](cgroups.md#id9)

Given the XML config above, the admin on a systemd based host would need to
create a unit file /etc/systemd/system/machine-production.slice

```
# cat > /etc/systemd/system/machine-testing.slice <<EOF
[Unit]
Description=VM testing slice
Before=slices.target
Wants=machine.slice
EOF
# systemctl start machine-testing.slice
```

## [Creating custom partitions (non-systemd)](cgroups.md#id10)

Given the XML config above, the admin on a non-systemd based host would need to
create a cgroup named '/machine/production.partition'

```
# cd /sys/fs/cgroup
# for i in blkio cpu,cpuacct cpuset devices freezer memory net_cls perf_event
  do
    mkdir $i/machine/production.partition
  done
# for i in cpuset.cpus  cpuset.mems
  do
    cat cpuset/machine/$i > cpuset/machine/production.partition/$i
  done
```

# [Resource management APIs/commands](cgroups.md#id11)

Since libvirt aims to provide an API which is portable across hypervisors, the
concept of cgroups is not exposed directly in the API or XML configuration. It
is considered to be an internal implementation detail. Instead libvirt provides
a set of APIs for applying resource controls, which are then mapped to
corresponding cgroup tunables

## [Scheduler tuning](cgroups.md#id12)

Parameters from the "cpu" controller are exposed via the schedinfo command
in virsh.

```
# virsh schedinfo demo
Scheduler      : posix
cpu_shares     : 1024
vcpu_period    : 100000
vcpu_quota     : -1
emulator_period: 100000
emulator_quota : -1
```

## [Block I/O tuning](cgroups.md#id13)

Parameters from the "blkio" controller are exposed via the bkliotune command
in virsh.

```
# virsh blkiotune demo
weight         : 500
device_weight  :
```

## [Memory tuning](cgroups.md#id14)

Parameters from the "memory" controller are exposed via the memtune command
in virsh.

```
# virsh memtune demo
hard_limit     : 580192
soft_limit     : unlimited
swap_hard_limit: unlimited
```

## [Network tuning](cgroups.md#id15)

The net_cls is not currently used. Instead traffic filter policies are set
directly against individual virtual network interfaces.

# [Legacy cgroups layout](cgroups.md#id16)

Prior to libvirt 1.0.5, the cgroups layout created by libvirt was different from
that described above, and did not allow for administrator customization. Libvirt
used a fixed, 3-level hierarchy libvirt/{qemu,lxc}/$VMNAME which was rooted
at the point in the hierarchy where libvirtd itself was located. So if libvirtd
was placed at /system/libvirtd.service by systemd, the groups for each
virtual machine / container would be located at
/system/libvirtd.service/libvirt/{qemu,lxc}/$VMNAME. In addition to this,
the QEMU drivers further child groups for each vCPU thread and the emulator
thread(s). This leads to a hierarchy that looked like

```
$ROOT
  |
  +- system
      |
      +- libvirtd.service
           |
           +- libvirt
               |
               +- qemu
               |   |
               |   +- vm1
               |   |   |
               |   |   +- emulator
               |   |   +- vcpu0
               |   |   +- vcpu1
               |   |
               |   +- vm2
               |   |   |
               |   |   +- emulator
               |   |   +- vcpu0
               |   |   +- vcpu1
               |   |
               |   +- vm3
               |       |
               |       +- emulator
               |       +- vcpu0
               |       +- vcpu1
               |
               +- lxc
                   |
                   +- container1
                   |
                   +- container2
                   |
                   +- container3
```

Although current releases are much improved, historically the use of deep
hierarchies has had a significant negative impact on the kernel scalability. The
legacy libvirt cgroups layout highlighted these problems, to the detriment of
the performance of virtual machines and containers.
