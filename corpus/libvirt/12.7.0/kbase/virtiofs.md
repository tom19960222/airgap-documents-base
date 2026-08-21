---
collection: libvirt
version: "12.7.0"
title: "Sharing files with Virtiofs"
source_url: https://libvirt.org/kbase/virtiofs.html
fetched_at: 2026-08-21T04:09:46+00:00
---
# Sharing files with Virtiofs

Contents

- [Virtiofs](virtiofs.md#virtiofs)
- [Sharing a host directory with a guest](virtiofs.md#sharing-a-host-directory-with-a-guest)
- [Running unprivileged](virtiofs.md#running-unprivileged)
- [Optional parameters](virtiofs.md#optional-parameters)
- [Externally-launched virtiofsd](virtiofs.md#externally-launched-virtiofsd)
- [Other options for vhost-user memory setup](virtiofs.md#other-options-for-vhost-user-memory-setup)

# [Virtiofs](virtiofs.md#id1)

Virtiofs is a shared file system that lets virtual machines access
a directory tree on the host. Unlike existing approaches, it
is designed to offer local file system semantics and performance.

See <https://virtio-fs.gitlab.io/>

*Note:* Older versions of virtiofsd (prior to 1.11) do not not support
migration so operations such as migration, save/managed-save, or snapshots with
memory may not supported if a VM has a virtiofs filesystem connected.

Additionally snapshot operations managed by libvirt do not snapshot the state
of the files shared via virtiofs, and thus reverting to an earlier state is
not recommended.

# [Sharing a host directory with a guest](virtiofs.md#id2)

1. Add the following domain XML elements to share the host directory /path
   with the guest

   ```
   <domain>
     ...
     <memoryBacking>
       <source type='memfd'/>
       <access mode='shared'/>
     </memoryBacking>
     ...
     <devices>
       ...
       <filesystem type='mount' accessmode='passthrough'>
         <driver type='virtiofs' queue='1024'/>
         <source dir='/path'/>
         <target dir='mount_tag'/>
       </filesystem>
       ...
     </devices>
   </domain>
   ```

   Don't forget the <memoryBacking> elements. They are necessary for the
   vhost-user connection with the virtiofsd daemon.

   Note that despite its name, the target dir is an arbitrary string called
   a mount tag that is used inside the guest to identify the shared file system
   to be mounted. It does not have to correspond to the desired mount point in the
   guest.
2. Boot the guest and mount the filesystem

   ```
   guest# mount -t virtiofs mount_tag /mnt/mount/path
   ```

   Note: this requires virtiofs support in the guest kernel (Linux v5.4 or later)

# [Running unprivileged](virtiofs.md#id3)

In unprivileged mode (qemu:///session), mapping user/group IDs is available
(since libvirt version 10.0.0). The root user (ID 0) in the guest will be mapped
to the current user on the host.

The rest of the IDs will be mapped to the subordinate user IDs specified
in /etc/subuid:

```
$ cat /etc/subuid
jtomko:100000:65536
$ cat /etc/subgid
jtomko:100000:65536
```

To manually tweak the user ID mapping, the idmap element can be used.

# [Optional parameters](virtiofs.md#id4)

More optional elements can be specified

```
<filesystem type='mount' accessmode='passthrough'>
  <driver type='virtiofs' queue='1024'/>
  ...
  <binary path='/usr/libexec/virtiofsd' xattr='on'>
    <cache mode='always'/>
    <lock posix='on' flock='on'/>
  </binary>
</filesystem>
```

# [Externally-launched virtiofsd](virtiofs.md#id5)

Libvirtd can also connect the vhost-user-fs device to a virtiofsd
daemon launched outside of libvirtd. In that case socket permissions,
the mount tag and all the virtiofsd options are out of libvirtd's
control and need to be set by the application running virtiofsd.

```
<filesystem type='mount'>
  <driver type='virtiofs' queue='1024'/>
  <source socket='/var/virtiofsd.sock'/>
  <target dir='tag'/>
</filesystem>
```

# [Other options for vhost-user memory setup](virtiofs.md#id6)

The following information is necessary if you are using older versions of QEMU
and libvirt or have special memory backend requirements.

Almost all virtio devices (all that use virtqueues) require access to
at least certain portions of guest RAM (possibly policed by DMA). In
case of virtiofsd, much like in case of other vhost-user (see
<https://www.qemu.org/docs/master/interop/vhost-user.html>) virtio
devices that are realized by an userspace process, this in practice
means that QEMU needs to allocate the backing memory for all the guest
RAM as shared memory. As of QEMU 4.2, it is possible to explicitly
specify a memory backend when specifying the NUMA topology. This
method is however only viable for machine types that do support
NUMA. As of QEMU 5.0.0 and libvirt 6.9.0, it is possible to
specify the memory backend without NUMA (using the so called
memobject interface).

1. Set up the memory backend

   - Use memfd memory

     No host setup is required when using the Linux memfd memory backend.
   - Use file-backed memory

     Configure the directory where the files backing the memory will be stored
     with the memory_backing_dir option in /etc/libvirt/qemu.conf

     ```
     # This directory is used for memoryBacking source if configured as file.
     # NOTE: big files will be stored here
     memory_backing_dir = "/dev/shm/"
     ```
   - Use hugepage-backed memory

     Make sure there are enough huge pages allocated for the requested guest memory.
     For example, for one guest with 2 GiB of RAM backed by 2 MiB hugepages:

     ```
     # virsh allocpages 2M 1024
     ```
2. Specify the NUMA topology (this step is only required for the NUMA case)

   in the domain XML of the guest.
   For the simplest one-node topology for a guest with 2GiB of RAM and 8 vCPUs:

   ```
   <domain>
     ...
     <cpu ...>
       <numa>
         <cell id='0' cpus='0-7' memory='2' unit='GiB' memAccess='shared'/>
       </numa>
     </cpu>
    ...
   </domain>
   ```

   Note that the CPU element might already be specified and only one is allowed.
3. Specify the memory backend

   One of the following:

   - memfd memory

     ```
     <domain>
       ...
       <memoryBacking>
         <source type='memfd'/>
         <access mode='shared'/>
       </memoryBacking>
       ...
     </domain>
     ```
   - File-backed memory

     ```
     <domain>
       ...
       <memoryBacking>
         <access mode='shared'/>
       </memoryBacking>
       ...
     </domain>
     ```

     This will create a file in the directory specified in qemu.conf
   - Hugepage-backed memory

     ```
     <domain>
       ...
       <memoryBacking>
         <hugepages>
           <page size='2' unit='M'/>
         </hugepages>
         <access mode='shared'/>
       </memoryBacking>
       ...
     </domain>
     ```
