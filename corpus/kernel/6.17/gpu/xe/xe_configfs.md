---
collection: kernel
version: "6.17"
title: "Xe Configfs"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_configfs.html
fetched_at: 2026-09-16T16:30:48+00:00
---
# Xe Configfs

## Overview

Configfs is a filesystem-based manager of kernel objects. XE KMD registers a
configfs subsystem called `'xe'` that creates a directory in the mounted configfs directory
The user can create devices under this directory and configure them as necessary
See [Configfs - Userspace-driven Kernel Object Configuration](../../filesystems/configfs.md) for more information about how configfs works.

## Create devices

In order to create a device, the user has to create a directory inside `'xe'`:

```
mkdir /sys/kernel/config/xe/0000:03:00.0/
```

Every device created is populated by the driver with entries that can be
used to configure it:

```
/sys/kernel/config/xe/
        .. 0000:03:00.0/
                ... survivability_mode
```

## Configure Attributes

### Survivability mode:

Enable survivability mode on supported cards. This setting only takes
effect when probing the device. Example to enable it:

```
# echo 1 > /sys/kernel/config/xe/0000:03:00.0/survivability_mode
# echo 0000:03:00.0 > /sys/bus/pci/drivers/xe/bind  (Enters survivability mode if supported)
```

### Allowed engines:

Allow only a set of engine(s) to be available, disabling the other engines
even if they are available in hardware. This is applied after HW fuses are
considered on each tile. Examples:

Allow only one render and one copy engines, nothing else:

```
# echo 'rcs0,bcs0' > /sys/kernel/config/xe/0000:03:00.0/engines_allowed
```

Allow only compute engines and first copy engine:

```
# echo 'ccs*,bcs0' > /sys/kernel/config/xe/0000:03:00.0/engines_allowed
```

Note that the engine names are the per-GT hardware names. On multi-tile
platforms, writing `rcs0,bcs0` to this file would allow the first render
and copy engines on each tile.

The requested configuration may not be supported by the platform and driver
may fail to probe. For example: if at least one copy engine is expected to be
available for migrations, but it’s disabled. This is intended for debugging
purposes only.

## Remove devices

The created device directories can be removed using `rmdir`:

```
rmdir /sys/kernel/config/xe/0000:03:00.0/
```

## Internal API

bool xe_configfs_get_survivability_mode(struct pci_dev \*pdev)
:   get configfs survivability mode attribute

**Parameters**

`struct pci_dev *pdev`
:   pci device

**Description**

find the configfs group that belongs to the pci device and return
the survivability mode attribute

**Return**

survivability mode if config group is found, false otherwise

void xe_configfs_clear_survivability_mode(struct pci_dev \*pdev)
:   clear configfs survivability mode attribute

**Parameters**

`struct pci_dev *pdev`
:   pci device

**Description**

find the configfs group that belongs to the pci device and clear survivability
mode attribute

u64 xe_configfs_get_engines_allowed(struct pci_dev \*pdev)
:   get engine allowed mask from configfs

**Parameters**

`struct pci_dev *pdev`
:   pci device

**Description**

Find the configfs group that belongs to the pci device and return
the mask of engines allowed to be used.

**Return**

engine mask with allowed engines
