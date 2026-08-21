---
collection: kernel
version: "6.8"
title: "Linux generic IRQ handling"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/genericirq.html
fetched_at: 2026-08-21T03:30:12+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/genericirq.md)

# Linux generic IRQ handling

Copyright
:   © 2005-2010: Thomas Gleixner

Copyright
:   © 2005-2006: Ingo Molnar

## Introduction

The generic interrupt handling layer is designed to provide a complete
abstraction of interrupt handling for device drivers. It is able to
handle all the different types of interrupt controller hardware. Device
drivers use generic API functions to request, enable, disable and free
interrupts. The drivers do not have to know anything about interrupt
hardware details, so they can be used on different platforms without
code changes.

This documentation is provided to developers who want to implement an
interrupt subsystem based for their architecture, with the help of the
generic IRQ handling layer.

## Rationale

The original implementation of interrupt handling in Linux uses the
__do_IRQ() super-handler, which is able to deal with every type of
interrupt logic.

Originally, Russell King identified different types of handlers to build
a quite universal set for the ARM interrupt handler implementation in
Linux 2.5/2.6. He distinguished between:

- Level type
- Edge type
- Simple type

During the implementation we identified another type:

- Fast EOI type

In the SMP world of the __do_IRQ() super-handler another type was
identified:

- Per CPU type

This split implementation of high-level IRQ handlers allows us to
optimize the flow of the interrupt handling for each specific interrupt
type. This reduces complexity in that particular code path and allows
the optimized handling of a given type.

The original general IRQ implementation used hw_interrupt_type
structures and their `->ack`, `->end` [etc.] callbacks to differentiate
the flow control in the super-handler. This leads to a mix of flow logic
and low-level hardware logic, and it also leads to unnecessary code
duplication: for example in i386, there is an `ioapic_level_irq` and an
`ioapic_edge_irq` IRQ-type which share many of the low-level details but
have different flow handling.

A more natural abstraction is the clean separation of the 'irq flow' and
the 'chip details'.

Analysing a couple of architecture's IRQ subsystem implementations
reveals that most of them can use a generic set of 'irq flow' methods
and only need to add the chip-level specific code. The separation is
also valuable for (sub)architectures which need specific quirks in the
IRQ flow itself but not in the chip details - and thus provides a more
transparent IRQ subsystem design.

Each interrupt descriptor is assigned its own high-level flow handler,
which is normally one of the generic implementations. (This high-level
flow handler implementation also makes it simple to provide
demultiplexing handlers which can be found in embedded platforms on
various architectures.)

The separation makes the generic interrupt handling layer more flexible
and extensible. For example, an (sub)architecture can use a generic
IRQ-flow implementation for 'level type' interrupts and add a
(sub)architecture specific 'edge type' implementation.

To make the transition to the new model easier and prevent the breakage
of existing implementations, the __do_IRQ() super-handler is still
available. This leads to a kind of duality for the time being. Over time
the new model should be used in more and more architectures, as it
enables smaller and cleaner IRQ subsystems. It's deprecated for three
years now and about to be removed.

## Known Bugs And Assumptions

None (knock on wood).

## Abstraction layers

There are three main levels of abstraction in the interrupt code:

1. High-level driver API
2. High-level IRQ flow handlers
3. Chip-level hardware encapsulation

### Interrupt control flow

Each interrupt is described by an interrupt descriptor structure
irq_desc. The interrupt is referenced by an 'unsigned int' numeric
value which selects the corresponding interrupt description structure in
the descriptor structures array. The descriptor structure contains
status information and pointers to the interrupt flow method and the
interrupt chip structure which are assigned to this interrupt.

Whenever an interrupt triggers, the low-level architecture code calls
into the generic interrupt code by calling desc->handle_irq(). This
high-level IRQ handling function only uses desc->irq_data.chip
primitives referenced by the assigned chip descriptor structure.

### High-level Driver API

The high-level Driver API consists of following functions:

- [`request_irq()`](genericirq.md#c.request_irq "request_irq")
- [`request_threaded_irq()`](genericirq.md#c.request_threaded_irq "request_threaded_irq")
- [`free_irq()`](genericirq.md#c.free_irq "free_irq")
- [`disable_irq()`](genericirq.md#c.disable_irq "disable_irq")
- [`enable_irq()`](genericirq.md#c.enable_irq "enable_irq")
- [`disable_irq_nosync()`](genericirq.md#c.disable_irq_nosync "disable_irq_nosync") (SMP only)
- [`synchronize_irq()`](genericirq.md#c.synchronize_irq "synchronize_irq") (SMP only)
- [`irq_set_irq_type()`](genericirq.md#c.irq_set_irq_type "irq_set_irq_type")
- [`irq_set_irq_wake()`](genericirq.md#c.irq_set_irq_wake "irq_set_irq_wake")
- [`irq_set_handler_data()`](genericirq.md#c.irq_set_handler_data "irq_set_handler_data")
- [`irq_set_chip()`](genericirq.md#c.irq_set_chip "irq_set_chip")
- [`irq_set_chip_data()`](genericirq.md#c.irq_set_chip_data "irq_set_chip_data")

See the autogenerated function documentation for details.

### High-level IRQ flow handlers

The generic layer provides a set of pre-defined irq-flow methods:

- [`handle_level_irq()`](genericirq.md#c.handle_level_irq "handle_level_irq")
- [`handle_edge_irq()`](genericirq.md#c.handle_edge_irq "handle_edge_irq")
- [`handle_fasteoi_irq()`](genericirq.md#c.handle_fasteoi_irq "handle_fasteoi_irq")
- [`handle_simple_irq()`](genericirq.md#c.handle_simple_irq "handle_simple_irq")
- [`handle_percpu_irq()`](genericirq.md#c.handle_percpu_irq "handle_percpu_irq")
- [`handle_edge_eoi_irq()`](genericirq.md#c.handle_edge_eoi_irq "handle_edge_eoi_irq")
- [`handle_bad_irq()`](genericirq.md#c.handle_bad_irq "handle_bad_irq")

The interrupt flow handlers (either pre-defined or architecture
specific) are assigned to specific interrupts by the architecture either
during bootup or during device initialization.

#### Default flow implementations

##### Helper functions

The helper functions call the chip primitives and are used by the
default flow implementations. The following helper functions are
implemented (simplified excerpt):

```
default_enable(struct irq_data *data)
{
    desc->irq_data.chip->irq_unmask(data);
}

default_disable(struct irq_data *data)
{
    if (!delay_disable(data))
        desc->irq_data.chip->irq_mask(data);
}

default_ack(struct irq_data *data)
{
    chip->irq_ack(data);
}

default_mask_ack(struct irq_data *data)
{
    if (chip->irq_mask_ack) {
        chip->irq_mask_ack(data);
    } else {
        chip->irq_mask(data);
        chip->irq_ack(data);
    }
}

noop(struct irq_data *data))
{
}
```

#### Default flow handler implementations

##### Default Level IRQ flow handler

handle_level_irq provides a generic implementation for level-triggered
interrupts.

The following control flow is implemented (simplified excerpt):

```
desc->irq_data.chip->irq_mask_ack();
handle_irq_event(desc->action);
desc->irq_data.chip->irq_unmask();
```

##### Default Fast EOI IRQ flow handler

handle_fasteoi_irq provides a generic implementation for interrupts,
which only need an EOI at the end of the handler.

The following control flow is implemented (simplified excerpt):

```
handle_irq_event(desc->action);
desc->irq_data.chip->irq_eoi();
```

##### Default Edge IRQ flow handler

handle_edge_irq provides a generic implementation for edge-triggered
interrupts.

The following control flow is implemented (simplified excerpt):

```
if (desc->status & running) {
    desc->irq_data.chip->irq_mask_ack();
    desc->status |= pending | masked;
    return;
}
desc->irq_data.chip->irq_ack();
desc->status |= running;
do {
    if (desc->status & masked)
        desc->irq_data.chip->irq_unmask();
    desc->status &= ~pending;
    handle_irq_event(desc->action);
} while (desc->status & pending);
desc->status &= ~running;
```

##### Default simple IRQ flow handler

handle_simple_irq provides a generic implementation for simple
interrupts.

> **Note:**
>
> The simple flow handler does not call any handler/chip primitives.

The following control flow is implemented (simplified excerpt):

```
handle_irq_event(desc->action);
```

##### Default per CPU flow handler

handle_percpu_irq provides a generic implementation for per CPU
interrupts.

Per CPU interrupts are only available on SMP and the handler provides a
simplified version without locking.

The following control flow is implemented (simplified excerpt):

```
if (desc->irq_data.chip->irq_ack)
    desc->irq_data.chip->irq_ack();
handle_irq_event(desc->action);
if (desc->irq_data.chip->irq_eoi)
    desc->irq_data.chip->irq_eoi();
```

##### EOI Edge IRQ flow handler

handle_edge_eoi_irq provides an abnomination of the edge handler
which is solely used to tame a badly wreckaged irq controller on
powerpc/cell.

##### Bad IRQ flow handler

handle_bad_irq is used for spurious interrupts which have no real
handler assigned..

#### Quirks and optimizations

The generic functions are intended for 'clean' architectures and chips,
which have no platform-specific IRQ handling quirks. If an architecture
needs to implement quirks on the 'flow' level then it can do so by
overriding the high-level irq-flow handler.

#### Delayed interrupt disable

This per interrupt selectable feature, which was introduced by Russell
King in the ARM interrupt implementation, does not mask an interrupt at
the hardware level when [`disable_irq()`](genericirq.md#c.disable_irq "disable_irq") is called. The interrupt is kept
enabled and is masked in the flow handler when an interrupt event
happens. This prevents losing edge interrupts on hardware which does not
store an edge interrupt event while the interrupt is disabled at the
hardware level. When an interrupt arrives while the IRQ_DISABLED flag
is set, then the interrupt is masked at the hardware level and the
IRQ_PENDING bit is set. When the interrupt is re-enabled by
[`enable_irq()`](genericirq.md#c.enable_irq "enable_irq") the pending bit is checked and if it is set, the interrupt
is resent either via hardware or by a software resend mechanism. (It's
necessary to enable CONFIG_HARDIRQS_SW_RESEND when you want to use
the delayed interrupt disable feature and your hardware is not capable
of retriggering an interrupt.) The delayed interrupt disable is not
configurable.

### Chip-level hardware encapsulation

The chip-level hardware descriptor structure [`irq_chip`](genericirq.md#c.irq_chip "irq_chip") contains all
the direct chip relevant functions, which can be utilized by the irq flow
implementations.

- `irq_ack`
- `irq_mask_ack` - Optional, recommended for performance
- `irq_mask`
- `irq_unmask`
- `irq_eoi` - Optional, required for EOI flow handlers
- `irq_retrigger` - Optional
- `irq_set_type` - Optional
- `irq_set_wake` - Optional

These primitives are strictly intended to mean what they say: ack means
ACK, masking means masking of an IRQ line, etc. It is up to the flow
handler(s) to use these basic units of low-level functionality.

## __do_IRQ entry point

The original implementation __do_IRQ() was an alternative entry point
for all types of interrupts. It no longer exists.

This handler turned out to be not suitable for all interrupt hardware
and was therefore reimplemented with split functionality for
edge/level/simple/percpu interrupts. This is not only a functional
optimization. It also shortens code paths for interrupts.

## Locking on SMP

The locking of chip registers is up to the architecture that defines the
chip primitives. The per-irq structure is protected via desc->lock, by
the generic layer.

## Generic interrupt chip

To avoid copies of identical implementations of IRQ chips the core
provides a configurable generic interrupt chip implementation.
Developers should check carefully whether the generic chip fits their
needs before implementing the same functionality slightly differently
themselves.

void irq_gc_noop(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   NOOP function

**Parameters**

`struct irq_data *d`
:   irq_data

void irq_gc_mask_disable_reg(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   Mask chip via disable register

**Parameters**

`struct irq_data *d`
:   irq_data

**Description**

Chip has separate enable/disable registers instead of a single mask
register.

void irq_gc_mask_set_bit(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   Mask chip via setting bit in mask register

**Parameters**

`struct irq_data *d`
:   irq_data

**Description**

Chip has a single mask register. Values of this register are cached
and protected by gc->lock

void irq_gc_mask_clr_bit(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   Mask chip via clearing bit in mask register

**Parameters**

`struct irq_data *d`
:   irq_data

**Description**

Chip has a single mask register. Values of this register are cached
and protected by gc->lock

void irq_gc_unmask_enable_reg(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   Unmask chip via enable register

**Parameters**

`struct irq_data *d`
:   irq_data

**Description**

Chip has separate enable/disable registers instead of a single mask
register.

void irq_gc_ack_set_bit(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d)
:   Ack pending interrupt via setting bit

**Parameters**

`struct irq_data *d`
:   irq_data

int irq_gc_set_wake(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d, unsigned int on)
:   Set/clr wake bit for an interrupt

**Parameters**

`struct irq_data *d`
:   irq_data

`unsigned int on`
:   Indicates whether the wake bit should be set or cleared

**Description**

For chips where the wake from suspend functionality is not
configured in a separate register and the wakeup active state is
just stored in a bitmask.

struct [irq_chip_generic](genericirq.md#c.irq_chip_generic "irq_chip_generic") \*irq_alloc_generic_chip(const char \*name, int num_ct, unsigned int irq_base, void __iomem \*reg_base, irq_flow_handler_t handler)
:   Allocate a generic chip and initialize it

**Parameters**

`const char *name`
:   Name of the irq chip

`int num_ct`
:   Number of irq_chip_type instances associated with this

`unsigned int irq_base`
:   Interrupt base nr for this chip

`void __iomem *reg_base`
:   Register base address (virtual)

`irq_flow_handler_t handler`
:   Default flow handler associated with this chip

**Description**

Returns an initialized irq_chip_generic structure. The chip defaults
to the primary (index 0) irq_chip_type and **handler**

int __irq_alloc_domain_generic_chips(struct irq_domain \*d, int irqs_per_chip, int num_ct, const char \*name, irq_flow_handler_t handler, unsigned int clr, unsigned int set, enum [irq_gc_flags](genericirq.md#c.irq_gc_flags "irq_gc_flags") gcflags)
:   Allocate generic chips for an irq domain

**Parameters**

`struct irq_domain *d`
:   irq domain for which to allocate chips

`int irqs_per_chip`
:   Number of interrupts each chip handles (max 32)

`int num_ct`
:   Number of irq_chip_type instances associated with this

`const char *name`
:   Name of the irq chip

`irq_flow_handler_t handler`
:   Default flow handler associated with these chips

`unsigned int clr`
:   IRQ_\* bits to clear in the mapping function

`unsigned int set`
:   IRQ_\* bits to set in the mapping function

`enum irq_gc_flags gcflags`
:   Generic chip specific setup flags

struct [irq_chip_generic](genericirq.md#c.irq_chip_generic "irq_chip_generic") \*irq_get_domain_generic_chip(struct irq_domain \*d, unsigned int hw_irq)
:   Get a pointer to the generic chip of a hw_irq

**Parameters**

`struct irq_domain *d`
:   irq domain pointer

`unsigned int hw_irq`
:   Hardware interrupt number

void irq_setup_generic_chip(struct [irq_chip_generic](genericirq.md#c.irq_chip_generic "irq_chip_generic") \*gc, u32 msk, enum [irq_gc_flags](genericirq.md#c.irq_gc_flags "irq_gc_flags") flags, unsigned int clr, unsigned int set)
:   Setup a range of interrupts with a generic chip

**Parameters**

`struct irq_chip_generic *gc`
:   Generic irq chip holding all data

`u32 msk`
:   Bitmask holding the irqs to initialize relative to gc->irq_base

`enum irq_gc_flags flags`
:   Flags for initialization

`unsigned int clr`
:   IRQ_\* bits to clear

`unsigned int set`
:   IRQ_\* bits to set

**Description**

Set up max. 32 interrupts starting from gc->irq_base. Note, this
initializes all interrupts to the primary irq_chip_type and its
associated handler.

int irq_setup_alt_chip(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*d, unsigned int type)
:   Switch to alternative chip

**Parameters**

`struct irq_data *d`
:   irq_data for this interrupt

`unsigned int type`
:   Flow type to be initialized

**Description**

Only to be called from chip->irq_set_type() callbacks.

void irq_remove_generic_chip(struct [irq_chip_generic](genericirq.md#c.irq_chip_generic "irq_chip_generic") \*gc, u32 msk, unsigned int clr, unsigned int set)
:   Remove a chip

**Parameters**

`struct irq_chip_generic *gc`
:   Generic irq chip holding all data

`u32 msk`
:   Bitmask holding the irqs to initialize relative to gc->irq_base

`unsigned int clr`
:   IRQ_\* bits to clear

`unsigned int set`
:   IRQ_\* bits to set

**Description**

Remove up to 32 interrupts starting from gc->irq_base.

## Structures

This chapter contains the autogenerated documentation of the structures
which are used in the generic IRQ layer.

struct irq_common_data
:   per irq data shared by all irqchips

**Definition**:

```
struct irq_common_data {
    unsigned int            __private state_use_accessors;
#ifdef CONFIG_NUMA;
    unsigned int            node;
#endif;
    void *handler_data;
    struct msi_desc         *msi_desc;
#ifdef CONFIG_SMP;
    cpumask_var_t affinity;
#endif;
#ifdef CONFIG_GENERIC_IRQ_EFFECTIVE_AFF_MASK;
    cpumask_var_t effective_affinity;
#endif;
#ifdef CONFIG_GENERIC_IRQ_IPI;
    unsigned int            ipi_offset;
#endif;
};
```

**Members**

`state_use_accessors`
:   status information for irq chip functions.
    Use accessor functions to deal with it

`node`
:   node index useful for balancing

`handler_data`
:   per-IRQ data for the irq_chip methods

`msi_desc`
:   MSI descriptor

`affinity`
:   IRQ affinity on SMP. If this is an IPI
    related irq, then this is the mask of the
    CPUs to which an IPI can be sent.

`effective_affinity`
:   The effective IRQ affinity on SMP as some irq
    chips do not allow multi CPU destinations.
    A subset of **affinity**.

`ipi_offset`
:   Offset of first IPI target cpu in **affinity**. Optional.

struct irq_data
:   per irq chip data passed down to chip functions

**Definition**:

```
struct irq_data {
    u32 mask;
    unsigned int            irq;
    unsigned long           hwirq;
    struct irq_common_data  *common;
    struct irq_chip         *chip;
    struct irq_domain       *domain;
#ifdef CONFIG_IRQ_DOMAIN_HIERARCHY;
    struct irq_data         *parent_data;
#endif;
    void *chip_data;
};
```

**Members**

`mask`
:   precomputed bitmask for accessing the chip registers

`irq`
:   interrupt number

`hwirq`
:   hardware interrupt number, local to the interrupt domain

`common`
:   point to data shared by all irqchips

`chip`
:   low level interrupt hardware access

`domain`
:   Interrupt translation domain; responsible for mapping
    between hwirq number and linux irq number.

`parent_data`
:   pointer to parent [`struct irq_data`](genericirq.md#c.irq_data "irq_data") to support hierarchy
    irq_domain

`chip_data`
:   platform-specific per-chip private data for the chip
    methods, to allow shared chip implementations

struct irq_chip
:   hardware interrupt chip descriptor

**Definition**:

```
struct irq_chip {
    const char      *name;
    unsigned int    (*irq_startup)(struct irq_data *data);
    void (*irq_shutdown)(struct irq_data *data);
    void (*irq_enable)(struct irq_data *data);
    void (*irq_disable)(struct irq_data *data);
    void (*irq_ack)(struct irq_data *data);
    void (*irq_mask)(struct irq_data *data);
    void (*irq_mask_ack)(struct irq_data *data);
    void (*irq_unmask)(struct irq_data *data);
    void (*irq_eoi)(struct irq_data *data);
    int (*irq_set_affinity)(struct irq_data *data, const struct cpumask *dest, bool force);
    int (*irq_retrigger)(struct irq_data *data);
    int (*irq_set_type)(struct irq_data *data, unsigned int flow_type);
    int (*irq_set_wake)(struct irq_data *data, unsigned int on);
    void (*irq_bus_lock)(struct irq_data *data);
    void (*irq_bus_sync_unlock)(struct irq_data *data);
#ifdef CONFIG_DEPRECATED_IRQ_CPU_ONOFFLINE;
    void (*irq_cpu_online)(struct irq_data *data);
    void (*irq_cpu_offline)(struct irq_data *data);
#endif;
    void (*irq_suspend)(struct irq_data *data);
    void (*irq_resume)(struct irq_data *data);
    void (*irq_pm_shutdown)(struct irq_data *data);
    void (*irq_calc_mask)(struct irq_data *data);
    void (*irq_print_chip)(struct irq_data *data, struct seq_file *p);
    int (*irq_request_resources)(struct irq_data *data);
    void (*irq_release_resources)(struct irq_data *data);
    void (*irq_compose_msi_msg)(struct irq_data *data, struct msi_msg *msg);
    void (*irq_write_msi_msg)(struct irq_data *data, struct msi_msg *msg);
    int (*irq_get_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool *state);
    int (*irq_set_irqchip_state)(struct irq_data *data, enum irqchip_irq_state which, bool state);
    int (*irq_set_vcpu_affinity)(struct irq_data *data, void *vcpu_info);
    void (*ipi_send_single)(struct irq_data *data, unsigned int cpu);
    void (*ipi_send_mask)(struct irq_data *data, const struct cpumask *dest);
    int (*irq_nmi_setup)(struct irq_data *data);
    void (*irq_nmi_teardown)(struct irq_data *data);
    unsigned long   flags;
};
```

**Members**

`name`
:   name for /proc/interrupts

`irq_startup`
:   start up the interrupt (defaults to ->enable if NULL)

`irq_shutdown`
:   shut down the interrupt (defaults to ->disable if NULL)

`irq_enable`
:   enable the interrupt (defaults to chip->unmask if NULL)

`irq_disable`
:   disable the interrupt

`irq_ack`
:   start of a new interrupt

`irq_mask`
:   mask an interrupt source

`irq_mask_ack`
:   ack and mask an interrupt source

`irq_unmask`
:   unmask an interrupt source

`irq_eoi`
:   end of interrupt

`irq_set_affinity`
:   Set the CPU affinity on SMP machines. If the force
    argument is true, it tells the driver to
    unconditionally apply the affinity setting. Sanity
    checks against the supplied affinity mask are not
    required. This is used for CPU hotplug where the
    target CPU is not yet set in the cpu_online_mask.

`irq_retrigger`
:   resend an IRQ to the CPU

`irq_set_type`
:   set the flow type (IRQ_TYPE_LEVEL/etc.) of an IRQ

`irq_set_wake`
:   enable/disable power-management wake-on of an IRQ

`irq_bus_lock`
:   function to lock access to slow bus (i2c) chips

`irq_bus_sync_unlock`
:   function to sync and unlock slow bus (i2c) chips

`irq_cpu_online`
:   configure an interrupt source for a secondary CPU

`irq_cpu_offline`
:   un-configure an interrupt source for a secondary CPU

`irq_suspend`
:   function called from core code on suspend once per
    chip, when one or more interrupts are installed

`irq_resume`
:   function called from core code on resume once per chip,
    when one ore more interrupts are installed

`irq_pm_shutdown`
:   function called from core code on shutdown once per chip

`irq_calc_mask`
:   Optional function to set irq_data.mask for special cases

`irq_print_chip`
:   optional to print special chip info in show_interrupts

`irq_request_resources`
:   optional to request resources before calling
    any other callback related to this irq

`irq_release_resources`
:   optional to release resources acquired with
    irq_request_resources

`irq_compose_msi_msg`
:   optional to compose message content for MSI

`irq_write_msi_msg`
:   optional to write message content for MSI

`irq_get_irqchip_state`
:   return the internal state of an interrupt

`irq_set_irqchip_state`
:   set the internal state of a interrupt

`irq_set_vcpu_affinity`
:   optional to target a vCPU in a virtual machine

`ipi_send_single`
:   send a single IPI to destination cpus

`ipi_send_mask`
:   send an IPI to destination cpus in cpumask

`irq_nmi_setup`
:   function called from core code before enabling an NMI

`irq_nmi_teardown`
:   function called from core code after disabling an NMI

`flags`
:   chip specific flags

struct irq_chip_regs
:   register offsets for struct irq_gci

**Definition**:

```
struct irq_chip_regs {
    unsigned long           enable;
    unsigned long           disable;
    unsigned long           mask;
    unsigned long           ack;
    unsigned long           eoi;
    unsigned long           type;
    unsigned long           polarity;
};
```

**Members**

`enable`
:   Enable register offset to reg_base

`disable`
:   Disable register offset to reg_base

`mask`
:   Mask register offset to reg_base

`ack`
:   Ack register offset to reg_base

`eoi`
:   Eoi register offset to reg_base

`type`
:   Type configuration register offset to reg_base

`polarity`
:   Polarity configuration register offset to reg_base

struct irq_chip_type
:   Generic interrupt chip instance for a flow type

**Definition**:

```
struct irq_chip_type {
    struct irq_chip         chip;
    struct irq_chip_regs    regs;
    irq_flow_handler_t handler;
    u32 type;
    u32 mask_cache_priv;
    u32 *mask_cache;
};
```

**Members**

`chip`
:   The real interrupt chip which provides the callbacks

`regs`
:   Register offsets for this chip

`handler`
:   Flow handler associated with this chip

`type`
:   Chip can handle these flow types

`mask_cache_priv`
:   Cached mask register private to the chip type

`mask_cache`
:   Pointer to cached mask register

**Description**

A irq_generic_chip can have several instances of irq_chip_type when
it requires different functions and register offsets for different
flow types.

struct irq_chip_generic
:   Generic irq chip data structure

**Definition**:

```
struct irq_chip_generic {
    raw_spinlock_t lock;
    void __iomem            *reg_base;
    u32 (*reg_readl)(void __iomem *addr);
    void (*reg_writel)(u32 val, void __iomem *addr);
    void (*suspend)(struct irq_chip_generic *gc);
    void (*resume)(struct irq_chip_generic *gc);
    unsigned int            irq_base;
    unsigned int            irq_cnt;
    u32 mask_cache;
    u32 type_cache;
    u32 polarity_cache;
    u32 wake_enabled;
    u32 wake_active;
    unsigned int            num_ct;
    void *private;
    unsigned long           installed;
    unsigned long           unused;
    struct irq_domain       *domain;
    struct list_head        list;
    struct irq_chip_type    chip_types[];
};
```

**Members**

`lock`
:   Lock to protect register and cache data access

`reg_base`
:   Register base address (virtual)

`reg_readl`
:   Alternate I/O accessor (defaults to readl if NULL)

`reg_writel`
:   Alternate I/O accessor (defaults to writel if NULL)

`suspend`
:   Function called from core code on suspend once per
    chip; can be useful instead of irq_chip::suspend to
    handle chip details even when no interrupts are in use

`resume`
:   Function called from core code on resume once per chip;
    can be useful instead of irq_chip::suspend to handle
    chip details even when no interrupts are in use

`irq_base`
:   Interrupt base nr for this chip

`irq_cnt`
:   Number of interrupts handled by this chip

`mask_cache`
:   Cached mask register shared between all chip types

`type_cache`
:   Cached type register

`polarity_cache`
:   Cached polarity register

`wake_enabled`
:   Interrupt can wakeup from suspend

`wake_active`
:   Interrupt is marked as an wakeup from suspend source

`num_ct`
:   Number of available irq_chip_type instances (usually 1)

`private`
:   Private data for non generic chip callbacks

`installed`
:   bitfield to denote installed interrupts

`unused`
:   bitfield to denote unused interrupts

`domain`
:   irq domain pointer

`list`
:   List head for keeping track of instances

`chip_types`
:   Array of interrupt irq_chip_types

**Description**

Note, that irq_chip_generic can have multiple irq_chip_type
implementations which can be associated to a particular irq line of
an irq_chip_generic instance. That allows to share and protect
state in an irq_chip_generic instance when we need to implement
different flow mechanisms (level/edge) for it.

enum irq_gc_flags
:   Initialization flags for generic irq chips

**Constants**

`IRQ_GC_INIT_MASK_CACHE`
:   Initialize the mask_cache by reading mask reg

`IRQ_GC_INIT_NESTED_LOCK`
:   Set the lock class of the irqs to nested for
    irq chips which need to call irq_set_wake() on
    the parent irq. Usually GPIO implementations

`IRQ_GC_MASK_CACHE_PER_TYPE`
:   Mask cache is chip type private

`IRQ_GC_NO_MASK`
:   Do not calculate irq_data->mask

`IRQ_GC_BE_IO`
:   Use big-endian register accesses (default: LE)

struct irqaction
:   per interrupt action descriptor

**Definition**:

```
struct irqaction {
    irq_handler_t handler;
    void *dev_id;
    void __percpu           *percpu_dev_id;
    struct irqaction        *next;
    irq_handler_t thread_fn;
    struct task_struct      *thread;
    struct irqaction        *secondary;
    unsigned int            irq;
    unsigned int            flags;
    unsigned long           thread_flags;
    unsigned long           thread_mask;
    const char              *name;
    struct proc_dir_entry   *dir;
};
```

**Members**

`handler`
:   interrupt handler function

`dev_id`
:   cookie to identify the device

`percpu_dev_id`
:   cookie to identify the device

`next`
:   pointer to the next irqaction for shared interrupts

`thread_fn`
:   interrupt handler function for threaded interrupts

`thread`
:   thread pointer for threaded interrupts

`secondary`
:   pointer to secondary irqaction (force threading)

`irq`
:   interrupt number

`flags`
:   flags (see IRQF_\* above)

`thread_flags`
:   flags related to **thread**

`thread_mask`
:   bitmask for keeping track of **thread** activity

`name`
:   name of the device

`dir`
:   pointer to the proc/irq/NN/name entry

int request_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char \*name, void \*dev)
:   Add a handler for an interrupt line

**Parameters**

`unsigned int irq`
:   The interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.
    Primary handler for threaded interrupts
    If NULL, the default primary handler is installed

`unsigned long flags`
:   Handling flags

`const char *name`
:   Name of the device generating this interrupt

`void *dev`
:   A cookie passed to the handler function

**Description**

This call allocates an interrupt and establishes a handler; see
the documentation for [`request_threaded_irq()`](genericirq.md#c.request_threaded_irq "request_threaded_irq") for details.

struct irq_affinity_notify
:   context for notification of IRQ affinity changes

**Definition**:

```
struct irq_affinity_notify {
    unsigned int irq;
    struct kref kref;
    struct work_struct work;
    void (*notify)(struct irq_affinity_notify *, const cpumask_t *mask);
    void (*release)(struct kref *ref);
};
```

**Members**

`irq`
:   Interrupt to which notification applies

`kref`
:   Reference count, for internal use

`work`
:   Work item, for internal use

`notify`
:   Function to be called on change. This will be
    called in process context.

`release`
:   Function to be called on release. This will be
    called in process context. Once registered, the
    structure must only be freed when this function is
    called or later.

struct irq_affinity
:   Description for automatic irq affinity assignements

**Definition**:

```
struct irq_affinity {
    unsigned int    pre_vectors;
    unsigned int    post_vectors;
    unsigned int    nr_sets;
    unsigned int    set_size[IRQ_AFFINITY_MAX_SETS];
    void (*calc_sets)(struct irq_affinity *, unsigned int nvecs);
    void *priv;
};
```

**Members**

`pre_vectors`
:   Don't apply affinity to **pre_vectors** at beginning of
    the MSI(-X) vector space

`post_vectors`
:   Don't apply affinity to **post_vectors** at end of
    the MSI(-X) vector space

`nr_sets`
:   The number of interrupt sets for which affinity
    spreading is required

`set_size`
:   Array holding the size of each interrupt set

`calc_sets`
:   Callback for calculating the number and size
    of interrupt sets

`priv`
:   Private data for usage by **calc_sets**, usually a
    pointer to driver/device specific data.

struct irq_affinity_desc
:   Interrupt affinity descriptor

**Definition**:

```
struct irq_affinity_desc {
    struct cpumask  mask;
    unsigned int    is_managed : 1;
};
```

**Members**

`mask`
:   cpumask to hold the affinity assignment

`is_managed`
:   1 if the interrupt is managed internally

int irq_update_affinity_hint(unsigned int irq, const struct cpumask \*m)
:   Update the affinity hint

**Parameters**

`unsigned int irq`
:   Interrupt to update

`const struct cpumask *m`
:   cpumask pointer (NULL to clear the hint)

**Description**

Updates the affinity hint, but does not change the affinity of the interrupt.

int irq_set_affinity_and_hint(unsigned int irq, const struct cpumask \*m)
:   Update the affinity hint and apply the provided cpumask to the interrupt

**Parameters**

`unsigned int irq`
:   Interrupt to update

`const struct cpumask *m`
:   cpumask pointer (NULL to clear the hint)

**Description**

Updates the affinity hint and if **m** is not NULL it applies it as the
affinity of that interrupt.

## Public Functions Provided

This chapter contains the autogenerated documentation of the kernel API
functions which are exported.

bool synchronize_hardirq(unsigned int irq)
:   wait for pending hard IRQ handlers (on other CPUs)

**Parameters**

`unsigned int irq`
:   interrupt number to wait for

    This function waits for any pending hard IRQ handlers for this
    interrupt to complete before returning. If you use this
    function while holding a resource the IRQ handler may need you
    will deadlock. It does not take associated threaded handlers
    into account.

    Do not use this for shutdown scenarios where you must be sure
    that all parts (hardirq and threaded handler) have completed.

**Return**

false if a threaded handler is active.

> This function may be called - with care - from IRQ context.
>
> It does not check whether there is an interrupt in flight at the
> hardware level, but not serviced yet, as this might deadlock when
> called with interrupts disabled and the target CPU of the interrupt
> is the current CPU.

void synchronize_irq(unsigned int irq)
:   wait for pending IRQ handlers (on other CPUs)

**Parameters**

`unsigned int irq`
:   interrupt number to wait for

    This function waits for any pending IRQ handlers for this interrupt
    to complete before returning. If you use this function while
    holding a resource the IRQ handler may need you will deadlock.

    Can only be called from preemptible code as it might sleep when
    an interrupt thread is associated to **irq**.

    It optionally makes sure (when the irq chip supports that method)
    that the interrupt is not pending in any CPU and waiting for
    service.

int irq_can_set_affinity(unsigned int irq)
:   Check if the affinity of a given irq can be set

**Parameters**

`unsigned int irq`
:   Interrupt to check

bool irq_can_set_affinity_usr(unsigned int irq)
:   Check if affinity of a irq can be set from user space

**Parameters**

`unsigned int irq`
:   Interrupt to check

**Description**

Like [`irq_can_set_affinity()`](genericirq.md#c.irq_can_set_affinity "irq_can_set_affinity") above, but additionally checks for the
AFFINITY_MANAGED flag.

void irq_set_thread_affinity(struct irq_desc \*desc)
:   Notify irq threads to adjust affinity

**Parameters**

`struct irq_desc *desc`
:   irq descriptor which has affinity changed

    We just set IRQTF_AFFINITY and delegate the affinity setting
    to the interrupt thread itself. We can not call
    [`set_cpus_allowed_ptr()`](../driver-api/basics.md#c.set_cpus_allowed_ptr "set_cpus_allowed_ptr") here as we hold desc->lock and this
    code can be called from hard interrupt context.

int irq_update_affinity_desc(unsigned int irq, struct [irq_affinity_desc](genericirq.md#c.irq_affinity_desc "irq_affinity_desc") \*affinity)
:   Update affinity management for an interrupt

**Parameters**

`unsigned int irq`
:   The interrupt number to update

`struct irq_affinity_desc *affinity`
:   Pointer to the affinity descriptor

**Description**

This interface can be used to configure the affinity management of
interrupts which have been allocated already.

There are certain limitations on when it may be used - attempts to use it
for when the kernel is configured for generic IRQ reservation mode (in
config GENERIC_IRQ_RESERVATION_MODE) will fail, as it may conflict with
managed/non-managed interrupt accounting. In addition, attempts to use it on
an interrupt which is already started or which has already been configured
as managed will also fail, as these mean invalid init state or double init.

int irq_set_affinity(unsigned int irq, const struct [cpumask](genericirq.md#c.irq_set_affinity "cpumask") \*cpumask)
:   Set the irq affinity of a given irq

**Parameters**

`unsigned int irq`
:   Interrupt to set affinity

`const struct cpumask *cpumask`
:   cpumask

**Description**

Fails if cpumask does not contain an online CPU

int irq_force_affinity(unsigned int irq, const struct [cpumask](genericirq.md#c.irq_force_affinity "cpumask") \*cpumask)
:   Force the irq affinity of a given irq

**Parameters**

`unsigned int irq`
:   Interrupt to set affinity

`const struct cpumask *cpumask`
:   cpumask

**Description**

Same as irq_set_affinity, but without checking the mask against
online cpus.

Solely for low level cpu hotplug code, where we need to make per
cpu interrupts affine before the cpu becomes online.

int irq_set_affinity_notifier(unsigned int irq, struct [irq_affinity_notify](genericirq.md#c.irq_affinity_notify "irq_affinity_notify") \*notify)
:   control notification of IRQ affinity changes

**Parameters**

`unsigned int irq`
:   Interrupt for which to enable/disable notification

`struct irq_affinity_notify *notify`
:   Context for notification, or `NULL` to disable
    notification. Function pointers must be initialised;
    the other fields will be initialised by this function.

    > Must be called in process context. Notification may only be enabled
    > after the IRQ is allocated and must be disabled before the IRQ is
    > freed using [`free_irq()`](genericirq.md#c.free_irq "free_irq").

int irq_set_vcpu_affinity(unsigned int irq, void \*vcpu_info)
:   Set vcpu affinity for the interrupt

**Parameters**

`unsigned int irq`
:   interrupt number to set affinity

`void *vcpu_info`
:   vCPU specific data or pointer to a percpu array of vCPU
    specific data for percpu_devid interrupts

    > This function uses the vCPU specific data to set the vCPU
    > affinity for an irq. The vCPU specific data is passed from
    > outside, such as KVM. One example code path is as below:
    > KVM -> IOMMU -> [`irq_set_vcpu_affinity()`](genericirq.md#c.irq_set_vcpu_affinity "irq_set_vcpu_affinity").

void disable_irq_nosync(unsigned int irq)
:   disable an irq without waiting

**Parameters**

`unsigned int irq`
:   Interrupt to disable

    Disable the selected interrupt line. Disables and Enables are
    nested.
    Unlike [`disable_irq()`](genericirq.md#c.disable_irq "disable_irq"), this function does not ensure existing
    instances of the IRQ handler have completed before returning.

    This function may be called from IRQ context.

void disable_irq(unsigned int irq)
:   disable an irq and wait for completion

**Parameters**

`unsigned int irq`
:   Interrupt to disable

    Disable the selected interrupt line. Enables and Disables are
    nested.
    This function waits for any pending IRQ handlers for this interrupt
    to complete before returning. If you use this function while
    holding a resource the IRQ handler may need you will deadlock.

    Can only be called from preemptible code as it might sleep when
    an interrupt thread is associated to **irq**.

bool disable_hardirq(unsigned int irq)
:   disables an irq and waits for hardirq completion

**Parameters**

`unsigned int irq`
:   Interrupt to disable

    Disable the selected interrupt line. Enables and Disables are
    nested.
    This function waits for any pending hard IRQ handlers for this
    interrupt to complete before returning. If you use this function while
    holding a resource the hard IRQ handler may need you will deadlock.

    When used to optimistically disable an interrupt from atomic context
    the return value must be checked.

**Return**

false if a threaded handler is active.

> This function may be called - with care - from IRQ context.

void disable_nmi_nosync(unsigned int irq)
:   disable an nmi without waiting

**Parameters**

`unsigned int irq`
:   Interrupt to disable

    Disable the selected interrupt line. Disables and enables are
    nested.
    The interrupt to disable must have been requested through request_nmi.
    Unlike disable_nmi(), this function does not ensure existing
    instances of the IRQ handler have completed before returning.

void enable_irq(unsigned int irq)
:   enable handling of an irq

**Parameters**

`unsigned int irq`
:   Interrupt to enable

    Undoes the effect of one call to [`disable_irq()`](genericirq.md#c.disable_irq "disable_irq"). If this
    matches the last disable, processing of interrupts on this
    IRQ line is re-enabled.

    This function may be called from IRQ context only when
    desc->irq_data.chip->bus_lock and desc->chip->bus_sync_unlock are NULL !

void enable_nmi(unsigned int irq)
:   enable handling of an nmi

**Parameters**

`unsigned int irq`
:   Interrupt to enable

    The interrupt to enable must have been requested through request_nmi.
    Undoes the effect of one call to disable_nmi(). If this
    matches the last disable, processing of interrupts on this
    IRQ line is re-enabled.

int irq_set_irq_wake(unsigned int irq, unsigned int on)
:   control irq power management wakeup

**Parameters**

`unsigned int irq`
:   interrupt to control

`unsigned int on`
:   enable/disable power management wakeup

    Enable/disable power management wakeup mode, which is
    disabled by default. Enables and disables must match,
    just as they match for non-wakeup mode support.

    Wakeup mode lets this IRQ wake the system from sleep
    states like "suspend to RAM".

**Note**

irq enable/disable state is completely orthogonal
:   to the enable/disable state of irq wake. An irq can be
    disabled with [`disable_irq()`](genericirq.md#c.disable_irq "disable_irq") and still wake the system as
    long as the irq has wake enabled. If this does not hold,
    then the underlying irq chip and the related driver need
    to be investigated.

void irq_wake_thread(unsigned int irq, void \*dev_id)
:   wake the irq thread for the action identified by dev_id

**Parameters**

`unsigned int irq`
:   Interrupt line

`void *dev_id`
:   Device identity for which the thread should be woken

const void \*free_irq(unsigned int irq, void \*dev_id)
:   free an interrupt allocated with request_irq

**Parameters**

`unsigned int irq`
:   Interrupt line to free

`void *dev_id`
:   Device identity to free

    Remove an interrupt handler. The handler is removed and if the
    interrupt line is no longer in use by any driver it is disabled.
    On a shared IRQ the caller must ensure the interrupt is disabled
    on the card it drives before calling this function. The function
    does not return until any executing interrupts for this IRQ
    have completed.

    This function must not be called from interrupt context.

    Returns the devname argument passed to request_irq.

int request_threaded_irq(unsigned int irq, irq_handler_t handler, irq_handler_t thread_fn, unsigned long irqflags, const char \*devname, void \*dev_id)
:   allocate an interrupt line

**Parameters**

`unsigned int irq`
:   Interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.
    Primary handler for threaded interrupts.
    If handler is NULL and thread_fn != NULL
    the default primary handler is installed.

`irq_handler_t thread_fn`
:   Function called from the irq handler thread
    If NULL, no irq thread is created

`unsigned long irqflags`
:   Interrupt type flags

`const char *devname`
:   An ascii name for the claiming device

`void *dev_id`
:   A cookie passed back to the handler function

    This call allocates interrupt resources and enables the
    interrupt line and IRQ handling. From the point this
    call is made your handler function may be invoked. Since
    your handler function must clear any interrupt the board
    raises, you must take care both to initialise your hardware
    and to set up the interrupt handler in the right order.

    If you want to set up a threaded irq handler for your device
    then you need to supply **handler** and **thread_fn**. **handler** is
    still called in hard interrupt context and has to check
    whether the interrupt originates from the device. If yes it
    needs to disable the interrupt on the device and return
    IRQ_WAKE_THREAD which will wake up the handler thread and run
    **thread_fn**. This split handler design is necessary to support
    shared interrupts.

    Dev_id must be globally unique. Normally the address of the
    device data structure is used as the cookie. Since the handler
    receives this value it makes sense to use it.

    If your interrupt is shared you must pass a non NULL dev_id
    as this is required when freeing the interrupt.

    Flags:

    IRQF_SHARED Interrupt is shared
    IRQF_TRIGGER_\* Specify active edge(s) or level
    IRQF_ONESHOT Run thread_fn with interrupt line masked

int request_any_context_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char \*name, void \*dev_id)
:   allocate an interrupt line

**Parameters**

`unsigned int irq`
:   Interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.
    Threaded handler for threaded interrupts.

`unsigned long flags`
:   Interrupt type flags

`const char *name`
:   An ascii name for the claiming device

`void *dev_id`
:   A cookie passed back to the handler function

    This call allocates interrupt resources and enables the
    interrupt line and IRQ handling. It selects either a
    hardirq or threaded handling method depending on the
    context.

    On failure, it returns a negative value. On success,
    it returns either IRQC_IS_HARDIRQ or IRQC_IS_NESTED.

int request_nmi(unsigned int irq, irq_handler_t handler, unsigned long irqflags, const char \*name, void \*dev_id)
:   allocate an interrupt line for NMI delivery

**Parameters**

`unsigned int irq`
:   Interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.
    Threaded handler for threaded interrupts.

`unsigned long irqflags`
:   Interrupt type flags

`const char *name`
:   An ascii name for the claiming device

`void *dev_id`
:   A cookie passed back to the handler function

    This call allocates interrupt resources and enables the
    interrupt line and IRQ handling. It sets up the IRQ line
    to be handled as an NMI.

    An interrupt line delivering NMIs cannot be shared and IRQ handling
    cannot be threaded.

    Interrupt lines requested for NMI delivering must produce per cpu
    interrupts and have auto enabling setting disabled.

    Dev_id must be globally unique. Normally the address of the
    device data structure is used as the cookie. Since the handler
    receives this value it makes sense to use it.

    If the interrupt line cannot be used to deliver NMIs, function
    will fail and return a negative value.

bool irq_percpu_is_enabled(unsigned int irq)
:   Check whether the per cpu irq is enabled

**Parameters**

`unsigned int irq`
:   Linux irq number to check for

**Description**

Must be called from a non migratable context. Returns the enable
state of a per cpu interrupt on the current cpu.

void remove_percpu_irq(unsigned int irq, struct [irqaction](genericirq.md#c.irqaction "irqaction") \*act)
:   free a per-cpu interrupt

**Parameters**

`unsigned int irq`
:   Interrupt line to free

`struct irqaction *act`
:   irqaction for the interrupt

**Description**

Used to remove interrupts statically setup by the early boot process.

void free_percpu_irq(unsigned int irq, void __percpu \*dev_id)
:   free an interrupt allocated with request_percpu_irq

**Parameters**

`unsigned int irq`
:   Interrupt line to free

`void __percpu *dev_id`
:   Device identity to free

    Remove a percpu interrupt handler. The handler is removed, but
    the interrupt line is not disabled. This must be done on each
    CPU before calling this function. The function does not return
    until any executing interrupts for this IRQ have completed.

    This function must not be called from interrupt context.

int setup_percpu_irq(unsigned int irq, struct [irqaction](genericirq.md#c.irqaction "irqaction") \*act)
:   setup a per-cpu interrupt

**Parameters**

`unsigned int irq`
:   Interrupt line to setup

`struct irqaction *act`
:   irqaction for the interrupt

**Description**

Used to statically setup per-cpu interrupts in the early boot process.

int __request_percpu_irq(unsigned int irq, irq_handler_t handler, unsigned long flags, const char \*devname, void __percpu \*dev_id)
:   allocate a percpu interrupt line

**Parameters**

`unsigned int irq`
:   Interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.

`unsigned long flags`
:   Interrupt type flags (IRQF_TIMER only)

`const char *devname`
:   An ascii name for the claiming device

`void __percpu *dev_id`
:   A percpu cookie passed back to the handler function

    This call allocates interrupt resources and enables the
    interrupt on the local CPU. If the interrupt is supposed to be
    enabled on other CPUs, it has to be done on each CPU using
    enable_percpu_irq().

    Dev_id must be globally unique. It is a per-cpu variable, and
    the handler gets called with the interrupted CPU's instance of
    that variable.

int request_percpu_nmi(unsigned int irq, irq_handler_t handler, const char \*name, void __percpu \*dev_id)
:   allocate a percpu interrupt line for NMI delivery

**Parameters**

`unsigned int irq`
:   Interrupt line to allocate

`irq_handler_t handler`
:   Function to be called when the IRQ occurs.

`const char *name`
:   An ascii name for the claiming device

`void __percpu *dev_id`
:   A percpu cookie passed back to the handler function

    This call allocates interrupt resources for a per CPU NMI. Per CPU NMIs
    have to be setup on each CPU by calling [`prepare_percpu_nmi()`](genericirq.md#c.prepare_percpu_nmi "prepare_percpu_nmi") before
    being enabled on the same CPU by using enable_percpu_nmi().

    Dev_id must be globally unique. It is a per-cpu variable, and
    the handler gets called with the interrupted CPU's instance of
    that variable.

    Interrupt lines requested for NMI delivering should have auto enabling
    setting disabled.

    If the interrupt line cannot be used to deliver NMIs, function
    will fail returning a negative value.

int prepare_percpu_nmi(unsigned int irq)
:   performs CPU local setup for NMI delivery

**Parameters**

`unsigned int irq`
:   Interrupt line to prepare for NMI delivery

    This call prepares an interrupt line to deliver NMI on the current CPU,
    before that interrupt line gets enabled with enable_percpu_nmi().

    As a CPU local operation, this should be called from non-preemptible
    context.

    If the interrupt line cannot be used to deliver NMIs, function
    will fail returning a negative value.

void teardown_percpu_nmi(unsigned int irq)
:   undoes NMI setup of IRQ line

**Parameters**

`unsigned int irq`
:   Interrupt line from which CPU local NMI configuration should be
    removed

    > This call undoes the setup done by [`prepare_percpu_nmi()`](genericirq.md#c.prepare_percpu_nmi "prepare_percpu_nmi").
    >
    > IRQ line should not be enabled for the current CPU.
    >
    > As a CPU local operation, this should be called from non-preemptible
    > context.

int irq_get_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool \*state)
:   returns the irqchip state of a interrupt.

**Parameters**

`unsigned int irq`
:   Interrupt line that is forwarded to a VM

`enum irqchip_irq_state which`
:   One of IRQCHIP_STATE_\* the caller wants to know about

`bool *state`
:   a pointer to a boolean where the state is to be stored

    This call snapshots the internal irqchip state of an
    interrupt, returning into **state** the bit corresponding to
    stage **which**

    This function should be called with preemption disabled if the
    interrupt controller has per-cpu registers.

int irq_set_irqchip_state(unsigned int irq, enum irqchip_irq_state which, bool val)
:   set the state of a forwarded interrupt.

**Parameters**

`unsigned int irq`
:   Interrupt line that is forwarded to a VM

`enum irqchip_irq_state which`
:   State to be restored (one of IRQCHIP_STATE_\*)

`bool val`
:   Value corresponding to **which**

    This call sets the internal irqchip state of an interrupt,
    depending on the value of **which**.

    This function should be called with migration disabled if the
    interrupt controller has per-cpu registers.

bool irq_has_action(unsigned int irq)
:   Check whether an interrupt is requested

**Parameters**

`unsigned int irq`
:   The linux irq number

**Return**

A snapshot of the current state

bool irq_check_status_bit(unsigned int irq, unsigned int bitmask)
:   Check whether bits in the irq descriptor status are set

**Parameters**

`unsigned int irq`
:   The linux irq number

`unsigned int bitmask`
:   The bitmask to evaluate

**Return**

True if one of the bits in **bitmask** is set

int irq_set_chip(unsigned int irq, const struct [irq_chip](genericirq.md#c.irq_chip "irq_chip") \*chip)
:   set the irq chip for an irq

**Parameters**

`unsigned int irq`
:   irq number

`const struct irq_chip *chip`
:   pointer to irq chip description structure

int irq_set_irq_type(unsigned int irq, unsigned int type)
:   set the irq trigger type for an irq

**Parameters**

`unsigned int irq`
:   irq number

`unsigned int type`
:   IRQ_TYPE_{LEVEL,EDGE}_\* value - see include/linux/irq.h

int irq_set_handler_data(unsigned int irq, void \*data)
:   set irq handler data for an irq

**Parameters**

`unsigned int irq`
:   Interrupt number

`void *data`
:   Pointer to interrupt specific data

    Set the hardware irq controller data for an irq

int irq_set_chip_data(unsigned int irq, void \*data)
:   set irq chip data for an irq

**Parameters**

`unsigned int irq`
:   Interrupt number

`void *data`
:   Pointer to chip specific data

    Set the hardware irq chip data for an irq

void handle_simple_irq(struct irq_desc \*desc)
:   Simple and software-decoded IRQs.

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Simple interrupts are either sent from a demultiplexing interrupt
    handler or come from hardware, where no interrupt hardware control
    is necessary.

**Note**

The caller is expected to handle the ack, clear, mask and
:   unmask issues if necessary.

void handle_untracked_irq(struct irq_desc \*desc)
:   Simple and software-decoded IRQs.

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Untracked interrupts are sent from a demultiplexing interrupt
    handler when the demultiplexer does not know which device it its
    multiplexed irq domain generated the interrupt. IRQ's handled
    through here are not subjected to stats tracking, randomness, or
    spurious interrupt detection.

**Note**

Like handle_simple_irq, the caller is expected to handle
:   the ack, clear, mask and unmask issues if necessary.

void handle_level_irq(struct irq_desc \*desc)
:   Level type irq handler

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Level type interrupts are active as long as the hardware line has
    the active level. This may require to mask the interrupt and unmask
    it after the associated handler has acknowledged the device, so the
    interrupt line is back to inactive.

void handle_fasteoi_irq(struct irq_desc \*desc)
:   irq handler for transparent controllers

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Only a single callback will be issued to the chip: an ->eoi()
    call when the interrupt has been serviced. This enables support
    for modern forms of interrupt handlers, which handle the flow
    details in hardware, transparently.

void handle_fasteoi_nmi(struct irq_desc \*desc)
:   irq handler for NMI interrupt lines

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    A simple NMI-safe handler, considering the restrictions
    from request_nmi.

    Only a single callback will be issued to the chip: an ->eoi()
    call when the interrupt has been serviced. This enables support
    for modern forms of interrupt handlers, which handle the flow
    details in hardware, transparently.

void handle_edge_irq(struct irq_desc \*desc)
:   edge type IRQ handler

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Interrupt occurs on the falling and/or rising edge of a hardware
    signal. The occurrence is latched into the irq controller hardware
    and must be acked in order to be reenabled. After the ack another
    interrupt can happen on the same source even before the first one
    is handled by the associated event handler. If this happens it
    might be necessary to disable (mask) the interrupt depending on the
    controller hardware. This requires to reenable the interrupt inside
    of the loop which handles the interrupts which have arrived while
    the handler was running. If all pending interrupts are handled, the
    loop is left.

void handle_fasteoi_ack_irq(struct irq_desc \*desc)
:   irq handler for edge hierarchy stacked on transparent controllers

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Like [`handle_fasteoi_irq()`](genericirq.md#c.handle_fasteoi_irq "handle_fasteoi_irq"), but for use with hierarchy where
    the irq_chip also needs to have its ->irq_ack() function
    called.

void handle_fasteoi_mask_irq(struct irq_desc \*desc)
:   irq handler for level hierarchy stacked on transparent controllers

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Like [`handle_fasteoi_irq()`](genericirq.md#c.handle_fasteoi_irq "handle_fasteoi_irq"), but for use with hierarchy where
    the irq_chip also needs to have its ->irq_mask_ack() function
    called.

int irq_chip_set_parent_state(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, enum irqchip_irq_state which, bool val)
:   set the state of a parent interrupt.

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`enum irqchip_irq_state which`
:   State to be restored (one of IRQCHIP_STATE_\*)

`bool val`
:   Value corresponding to **which**

**Description**

Conditional success, if the underlying irqchip does not implement it.

int irq_chip_get_parent_state(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, enum irqchip_irq_state which, bool \*state)
:   get the state of a parent interrupt.

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`enum irqchip_irq_state which`
:   one of IRQCHIP_STATE_\* the caller wants to know

`bool *state`
:   a pointer to a boolean where the state is to be stored

**Description**

Conditional success, if the underlying irqchip does not implement it.

void irq_chip_enable_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Enable the parent interrupt (defaults to unmask if NULL)

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_disable_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Disable the parent interrupt (defaults to mask if NULL)

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_ack_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Acknowledge the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_mask_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Mask the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_mask_ack_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Mask and acknowledge the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_unmask_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Unmask the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_eoi_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Invoke EOI on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

int irq_chip_set_affinity_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, const struct cpumask \*dest, bool force)
:   Set affinity on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`const struct cpumask *dest`
:   The affinity mask to set

`bool force`
:   Flag to enforce setting (disable online checks)

**Description**

Conditional, as the underlying parent chip might not implement it.

int irq_chip_set_type_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, unsigned int type)
:   Set IRQ type on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`unsigned int type`
:   IRQ_TYPE_{LEVEL,EDGE}_\* value - see include/linux/irq.h

**Description**

Conditional, as the underlying parent chip might not implement it.

int irq_chip_retrigger_hierarchy(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Retrigger an interrupt in hardware

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

**Description**

Iterate through the domain hierarchy of the interrupt and check
whether a hw retrigger function exists. If yes, invoke it.

int irq_chip_set_vcpu_affinity_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, void \*vcpu_info)
:   Set vcpu affinity on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`void *vcpu_info`
:   The vcpu affinity information

int irq_chip_set_wake_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, unsigned int on)
:   Set/reset wake-up on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`unsigned int on`
:   Whether to set or reset the wake-up capability of this irq

**Description**

Conditional, as the underlying parent chip might not implement it.

int irq_chip_request_resources_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Request resources on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

void irq_chip_release_resources_parent(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Release resources on the parent interrupt

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

## Internal Functions Provided

This chapter contains the autogenerated documentation of the internal
functions.

int generic_handle_irq(unsigned int irq)
:   Invoke the handler for a particular irq

**Parameters**

`unsigned int irq`
:   The irq number to handle

**Return**

0 on success, or -EINVAL if conversion has failed

> This function must be called from an IRQ context with irq regs
> initialized.

int generic_handle_irq_safe(unsigned int irq)
:   Invoke the handler for a particular irq from any context.

**Parameters**

`unsigned int irq`
:   The irq number to handle

**Return**

0 on success, a negative value on error.

**Description**

This function can be called from any context (IRQ or process context). It
will report an error if not invoked from IRQ context and the irq has been
marked to enforce IRQ-context only.

int generic_handle_domain_irq(struct irq_domain \*domain, unsigned int hwirq)
:   Invoke the handler for a HW irq belonging to a domain.

**Parameters**

`struct irq_domain *domain`
:   The domain where to perform the lookup

`unsigned int hwirq`
:   The HW irq number to convert to a logical one

**Return**

0 on success, or -EINVAL if conversion has failed

> This function must be called from an IRQ context with irq regs
> initialized.

int generic_handle_domain_nmi(struct irq_domain \*domain, unsigned int hwirq)
:   Invoke the handler for a HW nmi belonging to a domain.

**Parameters**

`struct irq_domain *domain`
:   The domain where to perform the lookup

`unsigned int hwirq`
:   The HW irq number to convert to a logical one

**Return**

0 on success, or -EINVAL if conversion has failed

> This function must be called from an NMI context with irq regs
> initialized.

void irq_free_descs(unsigned int from, unsigned int cnt)
:   free irq descriptors

**Parameters**

`unsigned int from`
:   Start of descriptor range

`unsigned int cnt`
:   Number of consecutive irqs to free

int __ref __irq_alloc_descs(int irq, unsigned int from, unsigned int cnt, int node, struct module \*owner, const struct [irq_affinity_desc](genericirq.md#c.irq_affinity_desc "irq_affinity_desc") \*affinity)
:   allocate and initialize a range of irq descriptors

**Parameters**

`int irq`
:   Allocate for specific irq number if irq >= 0

`unsigned int from`
:   Start the search from this irq number

`unsigned int cnt`
:   Number of consecutive irqs to allocate.

`int node`
:   Preferred node on which the irq descriptor should be allocated

`struct module *owner`
:   Owning module (can be NULL)

`const struct irq_affinity_desc *affinity`
:   Optional pointer to an affinity mask array of size **cnt** which
    hints where the irq descriptors should be allocated and which
    default affinities to use

**Description**

Returns the first irq number or error code

unsigned int irq_get_next_irq(unsigned int offset)
:   get next allocated irq number

**Parameters**

`unsigned int offset`
:   where to start the search

**Description**

Returns next irq number after offset or nr_irqs if none is found.

unsigned int kstat_irqs_cpu(unsigned int irq, int cpu)
:   Get the statistics for an interrupt on a cpu

**Parameters**

`unsigned int irq`
:   The interrupt number

`int cpu`
:   The cpu number

**Description**

Returns the sum of interrupt counts on **cpu** since boot for
**irq**. The caller must ensure that the interrupt is not removed
concurrently.

unsigned int kstat_irqs_usr(unsigned int irq)
:   Get the statistics for an interrupt from thread context

**Parameters**

`unsigned int irq`
:   The interrupt number

**Description**

Returns the sum of interrupt counts on all cpus since boot for **irq**.

It uses rcu to protect the access since a concurrent removal of an
interrupt descriptor is observing an rcu grace period before
delayed_free_desc()/irq_kobj_release().

void handle_bad_irq(struct irq_desc \*desc)
:   handle spurious and unhandled irqs

**Parameters**

`struct irq_desc *desc`
:   description of the interrupt

**Description**

Handles spurious and unhandled IRQ's. It also prints a debugmessage.

void noinstr generic_handle_arch_irq(struct pt_regs \*regs)
:   root irq handler for architectures which do no entry accounting themselves

**Parameters**

`struct pt_regs *regs`
:   Register file coming from the low-level handling code

int irq_set_msi_desc_off(unsigned int irq_base, unsigned int irq_offset, struct msi_desc \*entry)
:   set MSI descriptor data for an irq at offset

**Parameters**

`unsigned int irq_base`
:   Interrupt number base

`unsigned int irq_offset`
:   Interrupt number offset

`struct msi_desc *entry`
:   Pointer to MSI descriptor data

    Set the MSI descriptor entry for an irq at offset

int irq_set_msi_desc(unsigned int irq, struct msi_desc \*entry)
:   set MSI descriptor data for an irq

**Parameters**

`unsigned int irq`
:   Interrupt number

`struct msi_desc *entry`
:   Pointer to MSI descriptor data

    Set the MSI descriptor entry for an irq

void irq_disable(struct irq_desc \*desc)
:   Mark interrupt disabled

**Parameters**

`struct irq_desc *desc`
:   irq descriptor which should be disabled

**Description**

If the chip does not implement the irq_disable callback, we
use a lazy disable approach. That means we mark the interrupt
disabled, but leave the hardware unmasked. That's an
optimization because we avoid the hardware access for the
common case where no interrupt happens after we marked it
disabled. If an interrupt happens, then the interrupt flow
handler masks the line at the hardware level and marks it
pending.

If the interrupt chip does not implement the irq_disable callback,
a driver can disable the lazy approach for a particular irq line by
calling 'irq_set_status_flags(irq, IRQ_DISABLE_UNLAZY)'. This can
be used for devices which cannot disable the interrupt at the
device level under certain circumstances and have to use
disable_irq[_nosync] instead.

void handle_edge_eoi_irq(struct irq_desc \*desc)
:   edge eoi type IRQ handler

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

**Description**

Similar as the above handle_edge_irq, but using eoi and w/o the
mask/unmask logic.

void handle_percpu_irq(struct irq_desc \*desc)
:   Per CPU local irq handler

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

    Per CPU interrupts on SMP machines without locking requirements

void handle_percpu_devid_irq(struct irq_desc \*desc)
:   Per CPU local irq handler with per cpu dev ids

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

**Description**

Per CPU interrupts on SMP machines without locking requirements. Same as
[`handle_percpu_irq()`](genericirq.md#c.handle_percpu_irq "handle_percpu_irq") above but with the following extras:

action->percpu_dev_id is a pointer to percpu variables which
contain the real device id for the cpu on which this handler is
called

void handle_percpu_devid_fasteoi_nmi(struct irq_desc \*desc)
:   Per CPU local NMI handler with per cpu dev ids

**Parameters**

`struct irq_desc *desc`
:   the interrupt description structure for this irq

**Description**

Similar to handle_fasteoi_nmi, but handling the dev_id cookie
as a percpu pointer.

void irq_cpu_online(void)
:   Invoke all irq_cpu_online functions.

**Parameters**

`void`
:   no arguments

**Description**

> Iterate through all irqs and invoke the chip.[`irq_cpu_online()`](genericirq.md#c.irq_cpu_online "irq_cpu_online")
> for each.

void irq_cpu_offline(void)
:   Invoke all irq_cpu_offline functions.

**Parameters**

`void`
:   no arguments

**Description**

> Iterate through all irqs and invoke the chip.[`irq_cpu_offline()`](genericirq.md#c.irq_cpu_offline "irq_cpu_offline")
> for each.

int irq_chip_compose_msi_msg(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data, struct msi_msg \*msg)
:   Compose msi message for a irq chip

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

`struct msi_msg *msg`
:   Pointer to the MSI message

**Description**

For hierarchical domains we find the first chip in the hierarchy
which implements the irq_compose_msi_msg callback. For non
hierarchical we use the top level chip.

int irq_chip_pm_get(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Enable power for an IRQ chip

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

**Description**

Enable the power to the IRQ chip referenced by the interrupt data
structure.

int irq_chip_pm_put(struct [irq_data](genericirq.md#c.irq_data "irq_data") \*data)
:   Disable power for an IRQ chip

**Parameters**

`struct irq_data *data`
:   Pointer to interrupt specific data

**Description**

Disable the power to the IRQ chip referenced by the interrupt data
structure, belongs. Note that power will only be disabled, once this
function has been called for all IRQs that have called [`irq_chip_pm_get()`](genericirq.md#c.irq_chip_pm_get "irq_chip_pm_get").

## Credits

The following people have contributed to this document:

1. Thomas Gleixner [tglx@linutronix.de](mailto:tglx%40linutronix.de)
2. Ingo Molnar [mingo@elte.hu](mailto:mingo%40elte.hu)
