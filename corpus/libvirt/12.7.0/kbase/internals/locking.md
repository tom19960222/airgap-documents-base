---
collection: libvirt
version: "12.7.0"
title: "Resource Lock Manager"
source_url: https://libvirt.org/kbase/internals/locking.html
fetched_at: 2026-08-21T04:10:02+00:00
---
# Resource Lock Manager

Contents

- [Goals](locking.md#goals)
- [Requirements](locking.md#requirements)
- [Design](locking.md#design)
- [Plugin Implementations](locking.md#plugin-implementations)
- [QEMU Driver integration](locking.md#qemu-driver-integration)
- [Lock usage patterns](locking.md#lock-usage-patterns)

  - [Lock acquisition](locking.md#lock-acquisition)
  - [Lock release](locking.md#lock-release)

This page describes the design of the resource lock manager that is used for
locking disk images, to ensure exclusive access to content.

# [Goals](locking.md#id1)

The high level goal is to prevent the same disk image being used by more than
one QEMU instance at a time (unless the disk is marked as shareable, or
readonly). The scenarios to be prevented are thus:

1. Two different guests running configured to point at the same disk image.
2. One guest being started more than once on two different machines due to admin
   mistake
3. One guest being started more than once on a single machine due to libvirt
   driver bug on a single machine.

# [Requirements](locking.md#id2)

The high level goal leads to a set of requirements for the lock manager design

1. A lock must be held on a disk whenever a QEMU process has the disk open
2. The lock scheme must allow QEMU to be configured with readonly, shared write,
   or exclusive writable disks
3. A lock handover must be performed during the migration process where 2 QEMU
   processes will have the same disk open concurrently.
4. The lock manager must be able to identify and kill the process accessing the
   resource if the lock is revoked.
5. Locks can be acquired for arbitrary VM related resources, as determined by
   the management application.

# [Design](locking.md#id3)

Within a lock manager the following series of operations will need to be
supported.

- **Register object** Register the identity of an object against which locks
  will be acquired
- **Add resource** Associate a resource with an object for future lock
  acquisition / release
- **Acquire locks** Acquire the locks for all resources associated with the
  object
- **Release locks** Release the locks for all resources associated with the
  object
- **Inquire locks** Get a representation of the state of the locks for all
  resources associated with the object

# [Plugin Implementations](locking.md#id4)

Lock manager implementations are provided as LGPLv2+ licensed, dlopen()able
library modules. The plugins will be loadable from the following location:

```
/usr/{lib,lib64}/libvirt/lock_manager/$NAME.so
```

The lock manager plugin must export a single ELF symbol named
virLockDriverImpl, which is a static instance of the virLockDriver
struct. The struct is defined in the header file

```
#include <libvirt/plugins/lock_manager.h>
```

All callbacks in the struct must be initialized to non-NULL pointers. The
semantics of each callback are defined in the API docs embedded in the
previously mentioned header file

# [QEMU Driver integration](locking.md#id5)

With the QEMU driver, the lock plugin will be set in the
/etc/libvirt/qemu.conf configuration file by specifying the lock manager
name.

```
lockManager="sanlock"
```

By default the lock manager will be a 'no op' implementation for backwards
compatibility

# [Lock usage patterns](locking.md#id6)

The following pseudo code illustrates the common patterns of operations invoked
on the lock manager plugin callbacks.

## [Lock acquisition](locking.md#id7)

Initial lock acquisition will be performed from the process that is to own the
lock. This is typically the QEMU child process, in between the fork+exec
pairing. When adding further resources on the fly, to an existing object holding
locks, this will be done from the libvirtd process.

```
virLockManagerParam params[] = {
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UUID,
    .key = "uuid",
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_STRING,
    .key = "name",
    .value = { .str = dom->def->name },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UINT,
    .key = "id",
    .value = { .i = dom->def->id },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UINT,
    .key = "pid",
    .value = { .i = dom->pid },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_CSTRING,
    .key = "uri",
    .value = { .cstr = driver->uri },
  },
};
mgr = virLockManagerNew(lockPlugin,
                        VIR_LOCK_MANAGER_TYPE_DOMAIN,
                        G_N_ELEMENTS(params),
                        params,
                        0)));

foreach (initial disks)
    virLockManagerAddResource(mgr,
                              VIR_LOCK_MANAGER_RESOURCE_TYPE_DISK,
                              $path, 0, NULL, $flags);

if (virLockManagerAcquire(lock, NULL, 0) < 0);
  ...abort...
```

## [Lock release](locking.md#id8)

The locks are all implicitly released when the process that acquired them exits,
however, a process may voluntarily give up the lock by running

```
char *state = NULL;
virLockManagerParam params[] = {
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UUID,
    .key = "uuid",
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_STRING,
    .key = "name",
    .value = { .str = dom->def->name },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UINT,
    .key = "id",
    .value = { .i = dom->def->id },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_UINT,
    .key = "pid",
    .value = { .i = dom->pid },
  },
  { .type = VIR_LOCK_MANAGER_PARAM_TYPE_CSTRING,
    .key = "uri",
    .value = { .cstr = driver->uri },
  },
};
mgr = virLockManagerNew(lockPlugin,
                        VIR_LOCK_MANAGER_TYPE_DOMAIN,
                        G_N_ELEMENTS(params),
                        params,
                        0)));

foreach (initial disks)
    virLockManagerAddResource(mgr,
                              VIR_LOCK_MANAGER_RESOURCE_TYPE_DISK,
                              $path, 0, NULL, $flags);

virLockManagerRelease(mgr, & state, 0);
```

The returned state string can be passed to the virLockManagerAcquire method
to later re-acquire the exact same locks. This state transfer is commonly used
when performing live migration of virtual machines. By validating the state the
lock manager can ensure no other VM has re-acquire the same locks on a different
host. The state can also be obtained without releasing the locks, by calling the
virLockManagerInquire method.
