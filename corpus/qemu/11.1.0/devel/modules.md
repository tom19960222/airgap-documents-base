---
collection: qemu
version: "11.1.0"
title: "QEMU modules"
source_url: https://www.qemu.org/docs/master/devel/modules.html
fetched_at: 2026-08-21T03:25:54+00:00
---
# QEMU modules

**module info annotation macros**

`scripts/modinfo-collect.py` will collect module info,
using the preprocessor and -DQEMU_MODINFO.

`scripts/modinfo-generate.py` will create a module meta-data database
from the collected information so qemu knows about module
dependencies and QOM objects implemented by modules.

See `*.modinfo` and `modinfo.c` in the build directory to check the
script results.

module_obj

`module_obj (name)`

**Parameters**

`name`
:   QOM type.

**Description**

This module implements QOM type **name**.

module_dep

`module_dep (name)`

**Parameters**

`name`
:   module name

**Description**

This module depends on module **name**.

module_arch

`module_arch (name)`

**Parameters**

`name`
:   target architecture

**Description**

This module is for target architecture **arch**.

Note that target-dependent modules are tagged automatically, so
this is only needed in case target-independent modules should be
restricted. Use case example: the ccw bus is implemented by s390x
only.

module_opts

`module_opts (name)`

**Parameters**

`name`
:   QemuOpts name

**Description**

This module registers QemuOpts **name**.

module_kconfig

`module_kconfig (name)`

**Parameters**

`name`
:   Kconfig requirement necessary to load the module

**Description**

This module requires a core module that should be implemented and
enabled in Kconfig.
