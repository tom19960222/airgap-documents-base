---
collection: kernel
version: "6.8"
title: "SuperH Interfaces Guide"
source_url: https://www.kernel.org/doc/html/v6.8/arch/sh/index.html
fetched_at: 2026-08-21T03:29:03+00:00
---
# SuperH Interfaces Guide

Author
:   Paul Mundt

- [DeviceTree Booting](booting.md)
- [Adding a new board to LinuxSH](new-machine.md)
- [Notes on register bank usage in the kernel](register-banks.md)
- [Feature status on sh architecture](features.md)

## Memory Management

### SH-4

#### Store Queue API

void sq_flush_range(unsigned long start, unsigned int len)
:   Flush (prefetch) a specific SQ range

**Parameters**

`unsigned long start`
:   the store queue address to start flushing from

`unsigned int len`
:   the length to flush

**Description**

Flushes the store queue cache from **start** to **start** + **len** in a
linear fashion.

unsigned long sq_remap(unsigned long phys, unsigned int size, const char \*name, pgprot_t prot)
:   Map a physical address through the Store Queues

**Parameters**

`unsigned long phys`
:   Physical address of mapping.

`unsigned int size`
:   Length of mapping.

`const char *name`
:   User invoking mapping.

`pgprot_t prot`
:   Protection bits.

**Description**

Remaps the physical address **phys** through the next available store queue
address of **size** length. **name** is logged at boot time as well as through
the sysfs interface.

void sq_unmap(unsigned long vaddr)
:   Unmap a Store Queue allocation

**Parameters**

`unsigned long vaddr`
:   Pre-allocated Store Queue mapping.

**Description**

Unmaps the store queue allocation **map** that was previously created by
[`sq_remap()`](index.md#c.sq_remap "sq_remap"). Also frees up the pte that was previously inserted into
the kernel page table and discards the UTLB translation.

## Machine Specific Interfaces

### mach-dreamcast

int aica_rtc_gettimeofday(struct [device](../../driver-api/infrastructure.md#c.device "device") \*dev, struct rtc_time \*tm)
:   Get the time from the AICA RTC

**Parameters**

`struct device *dev`
:   the RTC device (ignored)

`struct rtc_time *tm`
:   pointer to resulting RTC time structure

**Description**

Grabs the current RTC seconds counter and adjusts it to the Unix Epoch.

int aica_rtc_settimeofday(struct [device](../../driver-api/infrastructure.md#c.device "device") \*dev, struct rtc_time \*tm)
:   Set the AICA RTC to the current time

**Parameters**

`struct device *dev`
:   the RTC device (ignored)

`struct rtc_time *tm`
:   pointer to new RTC time structure

**Description**

Adjusts the given **tv** to the AICA Epoch and sets the RTC seconds counter.

### mach-x3proto

int ilsel_enable(ilsel_source_t set)
:   Enable an ILSEL set.

**Parameters**

`ilsel_source_t set`
:   ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).

**Description**

Enables a given non-aliased ILSEL source (<= ILSEL_KEY) at the highest
available interrupt level. Callers should take care to order callsites
noting descending interrupt levels. Aliasing FPGA and external board
IRQs need to use [`ilsel_enable_fixed()`](index.md#c.ilsel_enable_fixed "ilsel_enable_fixed").

The return value is an IRQ number that can later be taken down with
[`ilsel_disable()`](index.md#c.ilsel_disable "ilsel_disable").

int ilsel_enable_fixed(ilsel_source_t set, unsigned int level)
:   Enable an ILSEL set at a fixed interrupt level

**Parameters**

`ilsel_source_t set`
:   ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).

`unsigned int level`
:   Interrupt level (1 - 15)

**Description**

Enables a given ILSEL source at a fixed interrupt level. Necessary
both for level reservation as well as for aliased sources that only
exist on special ILSEL#s.

Returns an IRQ number (as [`ilsel_enable()`](index.md#c.ilsel_enable "ilsel_enable")).

void ilsel_disable(unsigned int irq)
:   Disable an ILSEL set

**Parameters**

`unsigned int irq`
:   Bit position for ILSEL set value (retval from enable routines)

**Description**

Disable a previously enabled ILSEL set.

## Busses

### Maple

int maple_driver_register(struct maple_driver \*drv)
:   register a maple driver

**Parameters**

`struct maple_driver *drv`
:   maple driver to be registered.

**Description**

Registers the passed in **drv**, while updating the bus type.
Devices with matching function IDs will be automatically probed.

void maple_driver_unregister(struct maple_driver \*drv)
:   unregister a maple driver.

**Parameters**

`struct maple_driver *drv`
:   maple driver to unregister.

**Description**

Cleans up after [`maple_driver_register()`](index.md#c.maple_driver_register "maple_driver_register"). To be invoked in the exit
path of any module drivers.

void maple_getcond_callback(struct maple_device \*dev, void (\*callback)(struct mapleq \*mq), unsigned long interval, unsigned long function)
:   setup handling MAPLE_COMMAND_GETCOND

**Parameters**

`struct maple_device *dev`
:   device responding

`void (*callback) (struct mapleq *mq)`
:   handler callback

`unsigned long interval`
:   interval in jiffies between callbacks

`unsigned long function`
:   the function code for the device

int maple_add_packet(struct maple_device \*mdev, u32 function, u32 command, size_t length, void \*data)
:   add a single instruction to the maple bus queue

**Parameters**

`struct maple_device *mdev`
:   maple device

`u32 function`
:   function on device being queried

`u32 command`
:   maple command to add

`size_t length`
:   length of command string (in 32 bit words)

`void *data`
:   remainder of command string
