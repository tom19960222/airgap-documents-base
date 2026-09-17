---
collection: kernel
version: "6.17"
title: "The irq_domain Interrupt Number Mapping Library"
source_url: https://www.kernel.org/doc/html/v6.17/core-api/irq/irq-domain.html
fetched_at: 2026-09-16T16:26:51+00:00
---
English

- [Chinese (Simplified)](../../translations/zh_CN/core-api/irq/irq-domain.md)

# The irq_domain Interrupt Number Mapping Library

The current design of the Linux kernel uses a single large number
space where each separate IRQ source is assigned a unique number.
This is simple when there is only one interrupt controller. But in
systems with multiple interrupt controllers, the kernel must ensure
that each one gets assigned non-overlapping allocations of Linux
IRQ numbers.

The number of interrupt controllers registered as unique irqchips
shows a rising tendency. For example, subdrivers of different kinds
such as GPIO controllers avoid reimplementing identical callback
mechanisms as the IRQ core system by modelling their interrupt
handlers as irqchips. I.e. in effect cascading interrupt controllers.

So in the past, IRQ numbers could be chosen so that they match the
hardware IRQ line into the root interrupt controller (i.e. the
component actually firing the interrupt line to the CPU). Nowadays,
this number is just a number and the number loose all kind of
correspondence to hardware interrupt numbers.

For this reason, we need a mechanism to separate controller-local
interrupt numbers, called hardware IRQs, from Linux IRQ numbers.

The irq_alloc_desc\*() and irq_free_desc\*() APIs provide allocation of
IRQ numbers, but they don’t provide any support for reverse mapping of
the controller-local IRQ (hwirq) number into the Linux IRQ number
space.

The irq_domain library adds a mapping between hwirq and IRQ numbers on
top of the irq_alloc_desc\*() API. An irq_domain to manage the mapping
is preferred over interrupt controller drivers open coding their own
reverse mapping scheme.

irq_domain also implements a translation from an abstract [`struct
irq_fwspec`](irq-domain.md#c.irq_fwspec "irq_fwspec") to hwirq numbers (Device Tree, non-DT firmware node, ACPI
GSI, and software node so far), and can be easily extended to support
other IRQ topology data sources. The implementation is performed
without any extra platform support code.

## irq_domain Usage

[`struct irq_domain`](irq-domain.md#c.irq_domain "irq_domain") could be defined as an irq domain controller. That
is, it handles the mapping between hardware and virtual interrupt
numbers for a given interrupt domain. The domain structure is
generally created by the PIC code for a given PIC instance (though a
domain can cover more than one PIC if they have a flat number model).
It is the domain callbacks that are responsible for setting the
irq_chip on a given irq_desc after it has been mapped.

The host code and data structures use a fwnode_handle pointer to
identify the domain. In some cases, and in order to preserve source
code compatibility, this fwnode pointer is “upgraded” to a DT
device_node. For those firmware infrastructures that do not provide a
unique identifier for an interrupt controller, the irq_domain code
offers a fwnode allocator.

An interrupt controller driver creates and registers a [`struct irq_domain`](irq-domain.md#c.irq_domain "irq_domain")
by calling one of the irq_domain_create_\*() functions (each mapping
method has a different allocator function, more on that later). The
function will return a pointer to the [`struct irq_domain`](irq-domain.md#c.irq_domain "irq_domain") on success. The
caller must provide the allocator function with a [`struct irq_domain_ops`](irq-domain.md#c.irq_domain_ops "irq_domain_ops")
pointer.

In most cases, the irq_domain will begin empty without any mappings
between hwirq and IRQ numbers. Mappings are added to the irq_domain
by calling [`irq_create_mapping()`](irq-domain.md#c.irq_create_mapping "irq_create_mapping") which accepts the irq_domain and a
hwirq number as arguments. If a mapping for the hwirq doesn’t already
exist, [`irq_create_mapping()`](irq-domain.md#c.irq_create_mapping "irq_create_mapping") allocates a new Linux irq_desc, associates
it with the hwirq, and calls the `irq_domain_ops.map()`
callback. In there, the driver can perform any required hardware
setup.

Once a mapping has been established, it can be retrieved or used via a
variety of methods:

- [`irq_resolve_mapping()`](irq-domain.md#c.irq_resolve_mapping "irq_resolve_mapping") returns a pointer to the irq_desc structure
  for a given domain and hwirq number, and NULL if there was no
  mapping.
- [`irq_find_mapping()`](irq-domain.md#c.irq_find_mapping "irq_find_mapping") returns a Linux IRQ number for a given domain and
  hwirq number, and 0 if there was no mapping
- [`generic_handle_domain_irq()`](../genericirq.md#c.generic_handle_domain_irq "generic_handle_domain_irq") handles an interrupt described by a
  domain and a hwirq number

Note that irq domain lookups must happen in contexts that are
compatible with a RCU read-side critical section.

The [`irq_create_mapping()`](irq-domain.md#c.irq_create_mapping "irq_create_mapping") function must be called *at least once*
before any call to [`irq_find_mapping()`](irq-domain.md#c.irq_find_mapping "irq_find_mapping"), lest the descriptor will not
be allocated.

If the driver has the Linux IRQ number or the irq_data pointer, and
needs to know the associated hwirq number (such as in the irq_chip
callbacks) then it can be directly obtained from
`irq_data.hwirq`.

## Types of irq_domain Mappings

There are several mechanisms available for reverse mapping from hwirq
to Linux irq, and each mechanism uses a different allocation function.
Which reverse map type should be used depends on the use case. Each
of the reverse map types are described below:

### Linear

```
irq_domain_create_linear()
```

The linear reverse map maintains a fixed size table indexed by the
hwirq number. When a hwirq is mapped, an irq_desc is allocated for
the hwirq, and the IRQ number is stored in the table.

The Linear map is a good choice when the maximum number of hwirqs is
fixed and a relatively small number (~ < 256). The advantages of this
map are fixed time lookup for IRQ numbers, and irq_descs are only
allocated for in-use IRQs. The disadvantage is that the table must be
as large as the largest possible hwirq number.

The majority of drivers should use the Linear map.

### Tree

```
irq_domain_create_tree()
```

The irq_domain maintains a radix tree map from hwirq numbers to Linux
IRQs. When an hwirq is mapped, an irq_desc is allocated and the
hwirq is used as the lookup key for the radix tree.

The tree map is a good choice if the hwirq number can be very large
since it doesn’t need to allocate a table as large as the largest
hwirq number. The disadvantage is that hwirq to IRQ number lookup is
dependent on how many entries are in the table.

Very few drivers should need this mapping.

### No Map

```
irq_domain_create_nomap()
```

The No Map mapping is to be used when the hwirq number is
programmable in the hardware. In this case it is best to program the
Linux IRQ number into the hardware itself so that no mapping is
required. Calling [`irq_create_direct_mapping()`](irq-domain.md#c.irq_create_direct_mapping "irq_create_direct_mapping") will allocate a Linux
IRQ number and call the .`map()` callback so that driver can program the
Linux IRQ number into the hardware.

Most drivers cannot use this mapping, and it is now gated on the
CONFIG_IRQ_DOMAIN_NOMAP option. Please refrain from introducing new
users of this API.

### Legacy

```
irq_domain_create_simple()
irq_domain_create_legacy()
```

The Legacy mapping is a special case for drivers that already have a
range of irq_descs allocated for the hwirqs. It is used when the
driver cannot be immediately converted to use the linear mapping. For
example, many embedded system board support files use a set of #defines
for IRQ numbers that are passed to [`struct device`](../../driver-api/infrastructure.md#c.device "device") registrations. In that
case the Linux IRQ numbers cannot be dynamically assigned and the legacy
mapping should be used.

As the name implies, the \*`_legacy()` functions are deprecated and only
exist to ease the support of ancient platforms. No new users should be
added. Same goes for the \*`_simple()` functions when their use results
in the legacy behaviour.

The legacy map assumes a contiguous range of IRQ numbers has already
been allocated for the controller and that the IRQ number can be
calculated by adding a fixed offset to the hwirq number, and
visa-versa. The disadvantage is that it requires the interrupt
controller to manage IRQ allocations and it requires an irq_desc to be
allocated for every hwirq, even if it is unused.

The legacy map should only be used if fixed IRQ mappings must be
supported. For example, ISA controllers would use the legacy map for
mapping Linux IRQs 0-15 so that existing ISA drivers get the correct IRQ
numbers.

Most users of legacy mappings should use [`irq_domain_create_simple()`](irq-domain.md#c.irq_domain_create_simple "irq_domain_create_simple")
which will use a legacy domain only if an IRQ range is supplied by the
system and will otherwise use a linear domain mapping. The semantics of
this call are such that if an IRQ range is specified then descriptors
will be allocated on-the-fly for it, and if no range is specified it
will fall through to [`irq_domain_create_linear()`](irq-domain.md#c.irq_domain_create_linear "irq_domain_create_linear") which means *no* irq
descriptors will be allocated.

A typical use case for simple domains is where an irqchip provider
is supporting both dynamic and static IRQ assignments.

In order to avoid ending up in a situation where a linear domain is
used and no descriptor gets allocated it is very important to make sure
that the driver using the simple domain call [`irq_create_mapping()`](irq-domain.md#c.irq_create_mapping "irq_create_mapping")
before any [`irq_find_mapping()`](irq-domain.md#c.irq_find_mapping "irq_find_mapping") since the latter will actually work
for the static IRQ assignment case.

### Hierarchy IRQ Domain

On some architectures, there may be multiple interrupt controllers
involved in delivering an interrupt from the device to the target CPU.
Let’s look at a typical interrupt delivering path on x86 platforms:

```
Device --> IOAPIC -> Interrupt remapping Controller -> Local APIC -> CPU
```

There are three interrupt controllers involved:

1. IOAPIC controller
2. Interrupt remapping controller
3. Local APIC controller

To support such a hardware topology and make software architecture match
hardware architecture, an irq_domain data structure is built for each
interrupt controller and those irq_domains are organized into hierarchy.
When building irq_domain hierarchy, the irq_domain near to the device is
child and the irq_domain near to CPU is parent. So a hierarchy structure
as below will be built for the example above:

```
CPU Vector irq_domain (root irq_domain to manage CPU vectors)
        ^
        |
Interrupt Remapping irq_domain (manage irq_remapping entries)
        ^
        |
IOAPIC irq_domain (manage IOAPIC delivery entries/pins)
```

There are four major interfaces to use hierarchy irq_domain:

1. [`irq_domain_alloc_irqs()`](irq-domain.md#c.irq_domain_alloc_irqs "irq_domain_alloc_irqs"): allocate IRQ descriptors and interrupt
   controller related resources to deliver these interrupts.
2. [`irq_domain_free_irqs()`](irq-domain.md#c.irq_domain_free_irqs "irq_domain_free_irqs"): free IRQ descriptors and interrupt controller
   related resources associated with these interrupts.
3. [`irq_domain_activate_irq()`](irq-domain.md#c.irq_domain_activate_irq "irq_domain_activate_irq"): activate interrupt controller hardware to
   deliver the interrupt.
4. [`irq_domain_deactivate_irq()`](irq-domain.md#c.irq_domain_deactivate_irq "irq_domain_deactivate_irq"): deactivate interrupt controller hardware
   to stop delivering the interrupt.

The following is needed to support hierarchy irq_domain:

1. The `parent` field in [`struct irq_domain`](irq-domain.md#c.irq_domain "irq_domain") is used to
   maintain irq_domain hierarchy information.
2. The `parent_data` field in [`struct irq_data`](../genericirq.md#c.irq_data "irq_data") is used to
   build hierarchy irq_data to match hierarchy irq_domains. The
   irq_data is used to store irq_domain pointer and hardware irq
   number.
3. The `alloc()`, `free()`, and other callbacks in
   [`struct irq_domain_ops`](irq-domain.md#c.irq_domain_ops "irq_domain_ops") to support hierarchy irq_domain operations.

With the support of hierarchy irq_domain and hierarchy irq_data ready,
an irq_domain structure is built for each interrupt controller, and an
irq_data structure is allocated for each irq_domain associated with an
IRQ.

For an interrupt controller driver to support hierarchy irq_domain, it
needs to:

1. Implement irq_domain_ops.`alloc()` and irq_domain_ops.`free()`
2. Optionally, implement irq_domain_ops.`activate()` and
   irq_domain_ops.`deactivate()`.
3. Optionally, implement an irq_chip to manage the interrupt controller
   hardware.
4. There is no need to implement irq_domain_ops.`map()` and
   irq_domain_ops.`unmap()`. They are unused with hierarchy irq_domain.

Note the hierarchy irq_domain is in no way x86-specific, and is
heavily used to support other architectures, such as ARM, ARM64 etc.

#### Stacked irq_chip

Now, we could go one step further to support stacked (hierarchy)
irq_chip. That is, an irq_chip is associated with each irq_data along
the hierarchy. A child irq_chip may implement a required action by
itself or by cooperating with its parent irq_chip.

With stacked irq_chip, interrupt controller driver only needs to deal
with the hardware managed by itself and may ask for services from its
parent irq_chip when needed. So we could achieve a much cleaner
software architecture.

## Debugging

Most of the internals of the IRQ subsystem are exposed in debugfs by
turning CONFIG_GENERIC_IRQ_DEBUGFS on.

## Structures and Public Functions Provided

This chapter contains the autogenerated documentation of the structures
and exported kernel API functions which are used for IRQ domains.

struct irq_fwspec
:   generic IRQ specifier structure

**Definition**:

```
struct irq_fwspec {
    struct fwnode_handle    *fwnode;
    int param_count;
    u32 param[IRQ_DOMAIN_IRQ_SPEC_PARAMS];
};
```

**Members**

`fwnode`
:   Pointer to a firmware-specific descriptor

`param_count`
:   Number of device-specific parameters

`param`
:   Device-specific parameters

**Description**

This structure, directly modeled after of_phandle_args, is used to
pass a device-specific description of an interrupt.

struct irq_domain_ops
:   Methods for irq_domain objects

**Definition**:

```
struct irq_domain_ops {
    int (*match)(struct irq_domain *d, struct device_node *node, enum irq_domain_bus_token bus_token);
    int (*select)(struct irq_domain *d, struct irq_fwspec *fwspec, enum irq_domain_bus_token bus_token);
    int (*map)(struct irq_domain *d, unsigned int virq, irq_hw_number_t hw);
    void (*unmap)(struct irq_domain *d, unsigned int virq);
    int (*xlate)(struct irq_domain *d, struct device_node *node, const u32 *intspec, unsigned int intsize, unsigned long *out_hwirq, unsigned int *out_type);
#ifdef CONFIG_IRQ_DOMAIN_HIERARCHY;
    int (*alloc)(struct irq_domain *d, unsigned int virq, unsigned int nr_irqs, void *arg);
    void (*free)(struct irq_domain *d, unsigned int virq, unsigned int nr_irqs);
    int (*activate)(struct irq_domain *d, struct irq_data *irqd, bool reserve);
    void (*deactivate)(struct irq_domain *d, struct irq_data *irq_data);
    int (*translate)(struct irq_domain *d, struct irq_fwspec *fwspec, unsigned long *out_hwirq, unsigned int *out_type);
#endif;
#ifdef CONFIG_GENERIC_IRQ_DEBUGFS;
    void (*debug_show)(struct seq_file *m, struct irq_domain *d, struct irq_data *irqd, int ind);
#endif;
};
```

**Members**

`match`
:   Match an interrupt controller device node to a domain, returns
    1 on a match

`select`
:   Match an interrupt controller fw specification. It is more generic
    than **match** as it receives a complete [`struct irq_fwspec`](irq-domain.md#c.irq_fwspec "irq_fwspec"). Therefore,
    **select** is preferred if provided. Returns 1 on a match.

`map`
:   Create or update a mapping between a virtual irq number and a hw
    irq number. This is called only once for a given mapping.

`unmap`
:   Dispose of such a mapping

`xlate`
:   Given a device tree node and interrupt specifier, decode
    the hardware irq number and linux irq type value.

`alloc`
:   Allocate **nr_irqs** interrupts starting from **virq**.

`free`
:   Free **nr_irqs** interrupts starting from **virq**.

`activate`
:   Activate one interrupt in HW (**irqd**). If **reserve** is set, only
    reserve the vector. If unset, assign the vector (called from
    [`request_irq()`](../genericirq.md#c.request_irq "request_irq")).

`deactivate`
:   Disarm one interrupt (**irqd**).

`translate`
:   Given **fwspec**, decode the hardware irq number (**out_hwirq**) and
    linux irq type value (**out_type**). This is a generalised **xlate**
    (over [`struct irq_fwspec`](irq-domain.md#c.irq_fwspec "irq_fwspec")) and is preferred if provided.

`debug_show`
:   For domains to show specific data for an interrupt in debugfs.

**Description**

Functions below are provided by the driver and called whenever a new mapping
is created or an old mapping is disposed. The driver can then proceed to
whatever internal data structures management is required. It also needs
to setup the irq_desc when returning from `map()`.

struct irq_domain
:   Hardware interrupt number translation object

**Definition**:

```
struct irq_domain {
    struct list_head                link;
    const char                      *name;
    const struct irq_domain_ops     *ops;
    void *host_data;
    unsigned int                    flags;
    unsigned int                    mapcount;
    struct mutex                    mutex;
    struct irq_domain               *root;
    struct fwnode_handle            *fwnode;
    enum irq_domain_bus_token       bus_token;
    struct irq_domain_chip_generic  *gc;
    struct device                   *dev;
    struct device                   *pm_dev;
#ifdef CONFIG_IRQ_DOMAIN_HIERARCHY;
    struct irq_domain               *parent;
#endif;
#ifdef CONFIG_GENERIC_MSI_IRQ;
    const struct msi_parent_ops     *msi_parent_ops;
#endif;
    void (*exit)(struct irq_domain *d);
    irq_hw_number_t hwirq_max;
    unsigned int                    revmap_size;
    struct radix_tree_root          revmap_tree;
    struct irq_data __rcu           *revmap[] ;
};
```

**Members**

`link`
:   Element in global irq_domain list.

`name`
:   Name of interrupt domain

`ops`
:   Pointer to irq_domain methods

`host_data`
:   Private data pointer for use by owner. Not touched by irq_domain
    core code.

`flags`
:   Per irq_domain flags

`mapcount`
:   The number of mapped interrupts

`mutex`
:   Domain lock, hierarchical domains use root domain’s lock

`root`
:   Pointer to root domain, or containing structure if non-hierarchical

`fwnode`
:   Pointer to firmware node associated with the irq_domain. Pretty easy
    to swap it for the of_node via the irq_domain_get_of_node accessor

`bus_token`
:   **fwnode**’s device_node might be used for several irq domains. But
    in connection with **bus_token**, the pair shall be unique in a
    system.

`gc`
:   Pointer to a list of generic chips. There is a helper function for
    setting up one or more generic chips for interrupt controllers
    drivers using the generic chip library which uses this pointer.

`dev`
:   Pointer to the device which instantiated the irqdomain
    With per device irq domains this is not necessarily the same
    as **pm_dev**.

`pm_dev`
:   Pointer to a device that can be utilized for power management
    purposes related to the irq domain.

`parent`
:   Pointer to parent irq_domain to support hierarchy irq_domains

`msi_parent_ops`
:   Pointer to MSI parent domain methods for per device domain init

`exit`
:   Function called when the domain is destroyed

`hwirq_max`
:   Top limit for the HW irq number. Especially to avoid
    conflicts/failures with reserved HW irqs. Can be ~0.

`revmap_size`
:   Size of the linear map table **revmap**

`revmap_tree`
:   Radix map tree for hwirqs that don’t fit in the linear map

`revmap`
:   Linear table of irq_data pointers

**Description**

Optional elements:

Revmap data, used internally by the irq domain code:

struct irq_domain_info
:   Domain information structure

**Definition**:

```
struct irq_domain_info {
    struct fwnode_handle                    *fwnode;
    unsigned int                            domain_flags;
    unsigned int                            size;
    irq_hw_number_t hwirq_max;
    int direct_max;
    unsigned int                            hwirq_base;
    unsigned int                            virq_base;
    enum irq_domain_bus_token               bus_token;
    const char                              *name_suffix;
    const struct irq_domain_ops             *ops;
    void *host_data;
    struct device                           *dev;
#ifdef CONFIG_IRQ_DOMAIN_HIERARCHY;
    struct irq_domain                       *parent;
#endif;
    struct irq_domain_chip_generic_info     *dgc_info;
    int (*init)(struct irq_domain *d);
    void (*exit)(struct irq_domain *d);
};
```

**Members**

`fwnode`
:   firmware node for the interrupt controller

`domain_flags`
:   Additional flags to add to the domain flags

`size`
:   Size of linear map; 0 for radix mapping only

`hwirq_max`
:   Maximum number of interrupts supported by controller

`direct_max`
:   Maximum value of direct maps;
    Use ~0 for no limit; 0 for no direct mapping

`hwirq_base`
:   The first hardware interrupt number (legacy domains only)

`virq_base`
:   The first Linux interrupt number for legacy domains to
    immediately associate the interrupts after domain creation

`bus_token`
:   Domain bus token

`name_suffix`
:   Optional name suffix to avoid collisions when multiple
    domains are added using same fwnode

`ops`
:   Domain operation callbacks

`host_data`
:   Controller private data pointer

`dev`
:   Device which creates the domain

`parent`
:   Pointer to the parent irq domain used in a hierarchy domain

`dgc_info`
:   Geneneric chip information structure pointer used to
    create generic chips for the domain if not NULL.

`init`
:   Function called when the domain is created.
    Allow to do some additional domain initialisation.

`exit`
:   Function called when the domain is destroyed.
    Allow to do some additional cleanup operation.

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_domain_create_linear(struct fwnode_handle \*fwnode, unsigned int size, const struct [irq_domain_ops](irq-domain.md#c.irq_domain_ops "irq_domain_ops") \*ops, void \*host_data)
:   Allocate and register a linear revmap irq_domain.

**Parameters**

`struct fwnode_handle *fwnode`
:   pointer to interrupt controller’s FW node.

`unsigned int size`
:   Number of interrupts in the domain.

`const struct irq_domain_ops *ops`
:   map/unmap domain callbacks

`void *host_data`
:   Controller private data pointer

**Return**

Newly created irq_domain

unsigned int irq_create_mapping(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, irq_hw_number_t hwirq)
:   Map a hardware interrupt into linux irq space

**Parameters**

`struct irq_domain *domain`
:   domain owning this hardware interrupt or NULL for default domain

`irq_hw_number_t hwirq`
:   hardware irq number in that domain space

**Description**

Only one mapping per hardware interrupt is permitted.

If the sense/trigger is to be specified, `set_irq_type()` should be called
on the number returned from that call.

**Return**

Linux irq number or 0 on error

struct irq_desc \*irq_resolve_mapping(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, irq_hw_number_t hwirq)
:   Find a linux irq from a hw irq number.

**Parameters**

`struct irq_domain *domain`
:   domain owning this hardware interrupt

`irq_hw_number_t hwirq`
:   hardware irq number in that domain space

**Return**

Interrupt descriptor

unsigned int irq_find_mapping(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, irq_hw_number_t hwirq)
:   Find a linux irq from a hw irq number.

**Parameters**

`struct irq_domain *domain`
:   domain owning this hardware interrupt

`irq_hw_number_t hwirq`
:   hardware irq number in that domain space

**Return**

Linux irq number or 0 if not found

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_domain_create_hierarchy(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*parent, unsigned int flags, unsigned int size, struct fwnode_handle \*fwnode, const struct [irq_domain_ops](irq-domain.md#c.irq_domain_ops "irq_domain_ops") \*ops, void \*host_data)
:   Add a irqdomain into the hierarchy

**Parameters**

`struct irq_domain *parent`
:   Parent irq domain to associate with the new domain

`unsigned int flags`
:   Irq domain flags associated to the domain

`unsigned int size`
:   Size of the domain. See below

`struct fwnode_handle *fwnode`
:   Optional fwnode of the interrupt controller

`const struct irq_domain_ops *ops`
:   Pointer to the interrupt domain callbacks

`void *host_data`
:   Controller private data pointer

**Description**

If **size** is 0 a tree domain is created, otherwise a linear domain.

If successful the parent is associated to the new domain and the
domain flags are set.

**Return**

A pointer to IRQ domain, or `NULL` on failure.

int irq_domain_alloc_irqs(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int nr_irqs, int node, void \*arg)
:   Allocate IRQs from domain

**Parameters**

`struct irq_domain *domain`
:   domain to allocate from

`unsigned int nr_irqs`
:   number of IRQs to allocate

`int node`
:   NUMA node id for memory allocation

`void *arg`
:   domain specific argument

**Description**

See [`__irq_domain_alloc_irqs()`](irq-domain.md#c.__irq_domain_alloc_irqs "__irq_domain_alloc_irqs")’ documentation.

struct fwnode_handle \*__irq_domain_alloc_fwnode(unsigned int type, int id, const char \*name, phys_addr_t \*pa)
:   Allocate a fwnode_handle suitable for identifying an irq domain

**Parameters**

`unsigned int type`
:   Type of irqchip_fwnode. See linux/irqdomain.h

`int id`
:   Optional user provided id if name != NULL

`const char *name`
:   Optional user provided domain name

`phys_addr_t *pa`
:   Optional user-provided physical address

**Description**

Allocate a `struct irqchip_fwid`, and return a pointer to the embedded
fwnode_handle (or NULL on failure).

**Note**

The types IRQCHIP_FWNODE_NAMED and IRQCHIP_FWNODE_NAMED_ID are
solely to transport name information to irqdomain creation code. The
node is not stored. For other types the pointer is kept in the irq
domain struct.

void irq_domain_free_fwnode(struct fwnode_handle \*fwnode)
:   Free a non-OF-backed fwnode_handle

**Parameters**

`struct fwnode_handle *fwnode`
:   fwnode_handle to free

**Description**

Free a fwnode_handle allocated with irq_domain_alloc_fwnode.

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_domain_instantiate(const struct [irq_domain_info](irq-domain.md#c.irq_domain_info "irq_domain_info") \*info)
:   Instantiate a new irq domain data structure

**Parameters**

`const struct irq_domain_info *info`
:   Domain information pointer pointing to the information for this domain

**Return**

A pointer to the instantiated irq domain or an ERR_PTR value.

void irq_domain_remove(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain)
:   Remove an irq domain.

**Parameters**

`struct irq_domain *domain`
:   domain to remove

**Description**

This routine is used to remove an irq domain. The caller must ensure
that all mappings within the domain have been disposed of prior to
use, depending on the revmap type.

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_domain_create_simple(struct fwnode_handle \*fwnode, unsigned int size, unsigned int first_irq, const struct [irq_domain_ops](irq-domain.md#c.irq_domain_ops "irq_domain_ops") \*ops, void \*host_data)
:   Register an irq_domain and optionally map a range of irqs

**Parameters**

`struct fwnode_handle *fwnode`
:   firmware node for the interrupt controller

`unsigned int size`
:   total number of irqs in mapping

`unsigned int first_irq`
:   first number of irq block assigned to the domain,
    pass zero to assign irqs on-the-fly. If first_irq is non-zero, then
    pre-map all of the irqs in the domain to virqs starting at first_irq.

`const struct irq_domain_ops *ops`
:   domain callbacks

`void *host_data`
:   Controller private data pointer

**Description**

Allocates an irq_domain, and optionally if first_irq is positive then also
allocate irq_descs and map all of the hwirqs to virqs starting at first_irq.

This is intended to implement the expected behaviour for most
interrupt controllers. If device tree is used, then first_irq will be 0 and
irqs get mapped dynamically on the fly. However, if the controller requires
static virq assignments (non-DT boot) then it will set that up correctly.

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_find_matching_fwspec(struct [irq_fwspec](irq-domain.md#c.irq_fwspec "irq_fwspec") \*fwspec, enum irq_domain_bus_token bus_token)
:   Locates a domain for a given fwspec

**Parameters**

`struct irq_fwspec *fwspec`
:   FW specifier for an interrupt

`enum irq_domain_bus_token bus_token`
:   domain-specific data

void irq_set_default_domain(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain)
:   Set a “default” irq domain

**Parameters**

`struct irq_domain *domain`
:   default domain pointer

**Description**

For convenience, it’s possible to set a “default” domain that will be used
whenever NULL is passed to [`irq_create_mapping()`](irq-domain.md#c.irq_create_mapping "irq_create_mapping"). It makes life easier for
platforms that want to manipulate a few hard coded interrupt numbers that
aren’t properly represented in the device-tree.

struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*irq_get_default_domain(void)
:   Retrieve the “default” irq domain

**Parameters**

`void`
:   no arguments

**Return**

the default domain, if any.

**Description**

Modern code should never use this. This should only be used on
systems that cannot implement a firmware->fwnode mapping (which
both DT and ACPI provide).

unsigned int irq_create_direct_mapping(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain)
:   Allocate an irq for direct mapping

**Parameters**

`struct irq_domain *domain`
:   domain to allocate the irq for or NULL for default domain

**Description**

This routine is used for irq controllers which can choose the hardware
interrupt numbers they generate. In such a case it’s simplest to use
the linux irq as the hardware interrupt number. It still uses the linear
or radix tree to store the mapping, but the irq controller can optimize
the revmap path by using the hwirq directly.

unsigned int irq_create_mapping_affinity(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, irq_hw_number_t hwirq, const struct [irq_affinity_desc](../genericirq.md#c.irq_affinity_desc "irq_affinity_desc") \*affinity)
:   Map a hardware interrupt into linux irq space

**Parameters**

`struct irq_domain *domain`
:   domain owning this hardware interrupt or NULL for default domain

`irq_hw_number_t hwirq`
:   hardware irq number in that domain space

`const struct irq_affinity_desc *affinity`
:   irq affinity

**Description**

Only one mapping per hardware interrupt is permitted. Returns a linux
irq number.
If the sense/trigger is to be specified, `set_irq_type()` should be called
on the number returned from that call.

void irq_dispose_mapping(unsigned int virq)
:   Unmap an interrupt

**Parameters**

`unsigned int virq`
:   linux irq number of the interrupt to unmap

struct irq_desc \*__irq_resolve_mapping(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, irq_hw_number_t hwirq, unsigned int \*irq)
:   Find a linux irq from a hw irq number.

**Parameters**

`struct irq_domain *domain`
:   domain owning this hardware interrupt

`irq_hw_number_t hwirq`
:   hardware irq number in that domain space

`unsigned int *irq`
:   optional pointer to return the Linux irq if required

**Description**

Returns the interrupt descriptor.

int irq_domain_xlate_onecell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct device_node \*ctrlr, const u32 \*intspec, unsigned int intsize, unsigned long \*out_hwirq, unsigned int \*out_type)
:   Generic xlate for direct one cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct device_node *ctrlr`
:   The device tree node for the device whose interrupt is translated

`const u32 *intspec`
:   The interrupt specifier data from the device tree

`unsigned int intsize`
:   The number of entries in **intspec**

`unsigned long *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Device Tree IRQ specifier translation function which works with one cell
bindings where the cell value maps directly to the hwirq number.

int irq_domain_xlate_twocell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct device_node \*ctrlr, const u32 \*intspec, unsigned int intsize, irq_hw_number_t \*out_hwirq, unsigned int \*out_type)
:   Generic xlate for direct two cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct device_node *ctrlr`
:   The device tree node for the device whose interrupt is translated

`const u32 *intspec`
:   The interrupt specifier data from the device tree

`unsigned int intsize`
:   The number of entries in **intspec**

`irq_hw_number_t *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Device Tree IRQ specifier translation function which works with two cell
bindings where the cell values map directly to the hwirq number
and linux irq flags.

int irq_domain_xlate_twothreecell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct device_node \*ctrlr, const u32 \*intspec, unsigned int intsize, irq_hw_number_t \*out_hwirq, unsigned int \*out_type)
:   Generic xlate for direct two or three cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct device_node *ctrlr`
:   The device tree node for the device whose interrupt is translated

`const u32 *intspec`
:   The interrupt specifier data from the device tree

`unsigned int intsize`
:   The number of entries in **intspec**

`irq_hw_number_t *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Device Tree interrupt specifier translation function for two or three
cell bindings, where the cell values map directly to the hardware
interrupt number and the type specifier.

int irq_domain_xlate_onetwocell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct device_node \*ctrlr, const u32 \*intspec, unsigned int intsize, unsigned long \*out_hwirq, unsigned int \*out_type)
:   Generic xlate for one or two cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct device_node *ctrlr`
:   The device tree node for the device whose interrupt is translated

`const u32 *intspec`
:   The interrupt specifier data from the device tree

`unsigned int intsize`
:   The number of entries in **intspec**

`unsigned long *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Device Tree IRQ specifier translation function which works with either one
or two cell bindings where the cell values map directly to the hwirq number
and linux irq flags.

**Note**

don’t use this function unless your interrupt controller explicitly
supports both one and two cell bindings. For the majority of controllers
the `_onecell()` or `_twocell()` variants above should be used.

int irq_domain_translate_onecell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct [irq_fwspec](irq-domain.md#c.irq_fwspec "irq_fwspec") \*fwspec, unsigned long \*out_hwirq, unsigned int \*out_type)
:   Generic translate for direct one cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct irq_fwspec *fwspec`
:   The firmware interrupt specifier to translate

`unsigned long *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

int irq_domain_translate_twocell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct [irq_fwspec](irq-domain.md#c.irq_fwspec "irq_fwspec") \*fwspec, unsigned long \*out_hwirq, unsigned int \*out_type)
:   Generic translate for direct two cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct irq_fwspec *fwspec`
:   The firmware interrupt specifier to translate

`unsigned long *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Device Tree IRQ specifier translation function which works with two cell
bindings where the cell values map directly to the hwirq number
and linux irq flags.

int irq_domain_translate_twothreecell(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*d, struct [irq_fwspec](irq-domain.md#c.irq_fwspec "irq_fwspec") \*fwspec, unsigned long \*out_hwirq, unsigned int \*out_type)
:   Generic translate for direct two or three cell bindings

**Parameters**

`struct irq_domain *d`
:   Interrupt domain involved in the translation

`struct irq_fwspec *fwspec`
:   The firmware interrupt specifier to translate

`unsigned long *out_hwirq`
:   Pointer to storage for the hardware interrupt number

`unsigned int *out_type`
:   Pointer to storage for the interrupt type

**Description**

Firmware interrupt specifier translation function for two or three cell
specifications, where the parameter values map directly to the hardware
interrupt number and the type specifier.

void irq_domain_reset_irq_data(struct [irq_data](irq-domain.md#c.irq_domain_reset_irq_data "irq_data") \*irq_data)
:   Clear hwirq, chip and chip_data in **irq_data**

**Parameters**

`struct irq_data *irq_data`
:   The pointer to irq_data

int irq_domain_disconnect_hierarchy(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq)
:   Mark the first unused level of a hierarchy

**Parameters**

`struct irq_domain *domain`
:   IRQ domain from which the hierarchy is to be disconnected

`unsigned int virq`
:   IRQ number where the hierarchy is to be trimmed

**Description**

Marks the **virq** level belonging to **domain** as disconnected.
Returns -EINVAL if **virq** doesn’t have a valid irq_data pointing
to **domain**.

Its only use is to be able to trim levels of hierarchy that do not
have any real meaning for this interrupt, and that the driver marks
as such from its .`alloc()` callback.

struct [irq_data](../genericirq.md#c.irq_data "irq_data") \*irq_domain_get_irq_data(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq)
:   Get irq_data associated with **virq** and **domain**

**Parameters**

`struct irq_domain *domain`
:   domain to match

`unsigned int virq`
:   IRQ number to get irq_data

int irq_domain_set_hwirq_and_chip(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq, irq_hw_number_t hwirq, const struct [irq_chip](../genericirq.md#c.irq_chip "irq_chip") \*chip, void \*chip_data)
:   Set hwirq and irqchip of **virq** at **domain**

**Parameters**

`struct irq_domain *domain`
:   Interrupt domain to match

`unsigned int virq`
:   IRQ number

`irq_hw_number_t hwirq`
:   The hwirq number

`const struct irq_chip *chip`
:   The associated interrupt chip

`void *chip_data`
:   The associated chip data

void irq_domain_set_info(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq, irq_hw_number_t hwirq, const struct [irq_chip](../genericirq.md#c.irq_chip "irq_chip") \*chip, void \*chip_data, irq_flow_handler_t handler, void \*handler_data, const char \*handler_name)
:   Set the complete data for a **virq** in **domain**

**Parameters**

`struct irq_domain *domain`
:   Interrupt domain to match

`unsigned int virq`
:   IRQ number

`irq_hw_number_t hwirq`
:   The hardware interrupt number

`const struct irq_chip *chip`
:   The associated interrupt chip

`void *chip_data`
:   The associated interrupt chip data

`irq_flow_handler_t handler`
:   The interrupt flow handler

`void *handler_data`
:   The interrupt flow handler data

`const char *handler_name`
:   The interrupt handler name

void irq_domain_free_irqs_common(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq, unsigned int nr_irqs)
:   Clear irq_data and free the parent

**Parameters**

`struct irq_domain *domain`
:   Interrupt domain to match

`unsigned int virq`
:   IRQ number to start with

`unsigned int nr_irqs`
:   The number of irqs to free

void irq_domain_free_irqs_top(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int virq, unsigned int nr_irqs)
:   Clear handler and handler data, clear irqdata and free parent

**Parameters**

`struct irq_domain *domain`
:   Interrupt domain to match

`unsigned int virq`
:   IRQ number to start with

`unsigned int nr_irqs`
:   The number of irqs to free

int __irq_domain_alloc_irqs(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, int irq_base, unsigned int nr_irqs, int node, void \*arg, bool realloc, const struct [irq_affinity_desc](../genericirq.md#c.irq_affinity_desc "irq_affinity_desc") \*affinity)
:   Allocate IRQs from domain

**Parameters**

`struct irq_domain *domain`
:   domain to allocate from

`int irq_base`
:   allocate specified IRQ number if irq_base >= 0

`unsigned int nr_irqs`
:   number of IRQs to allocate

`int node`
:   NUMA node id for memory allocation

`void *arg`
:   domain specific argument

`bool realloc`
:   IRQ descriptors have already been allocated if true

`const struct irq_affinity_desc *affinity`
:   Optional irq affinity mask for multiqueue devices

**Description**

Allocate IRQ numbers and initialized all data structures to support
hierarchy IRQ domains.
Parameter **realloc** is mainly to support legacy IRQs.
Returns error code or allocated IRQ number

The whole process to setup an IRQ has been split into two steps.
The first step, [`__irq_domain_alloc_irqs()`](irq-domain.md#c.__irq_domain_alloc_irqs "__irq_domain_alloc_irqs"), is to allocate IRQ
descriptor and required hardware resources. The second step,
[`irq_domain_activate_irq()`](irq-domain.md#c.irq_domain_activate_irq "irq_domain_activate_irq"), is to program the hardware with preallocated
resources. In this way, it’s easier to rollback when failing to
allocate resources.

int irq_domain_push_irq(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, int virq, void \*arg)
:   Push a domain in to the top of a hierarchy.

**Parameters**

`struct irq_domain *domain`
:   Domain to push.

`int virq`
:   Irq to push the domain in to.

`void *arg`
:   Passed to the irq_domain_ops `alloc()` function.

**Description**

For an already existing irqdomain hierarchy, as might be obtained
via a call to `pci_enable_msix()`, add an additional domain to the
head of the processing chain. Must be called before [`request_irq()`](../genericirq.md#c.request_irq "request_irq")
has been called.

int irq_domain_pop_irq(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, int virq)
:   Remove a domain from the top of a hierarchy.

**Parameters**

`struct irq_domain *domain`
:   Domain to remove.

`int virq`
:   Irq to remove the domain from.

**Description**

Undo the effects of a call to [`irq_domain_push_irq()`](irq-domain.md#c.irq_domain_push_irq "irq_domain_push_irq"). Must be
called either before [`request_irq()`](../genericirq.md#c.request_irq "request_irq") or after [`free_irq()`](../genericirq.md#c.free_irq "free_irq").

int irq_domain_alloc_irqs_parent(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int irq_base, unsigned int nr_irqs, void \*arg)
:   Allocate interrupts from parent domain

**Parameters**

`struct irq_domain *domain`
:   Domain below which interrupts must be allocated

`unsigned int irq_base`
:   Base IRQ number

`unsigned int nr_irqs`
:   Number of IRQs to allocate

`void *arg`
:   Allocation data (arch/domain specific)

void irq_domain_free_irqs_parent(struct [irq_domain](irq-domain.md#c.irq_domain "irq_domain") \*domain, unsigned int irq_base, unsigned int nr_irqs)
:   Free interrupts from parent domain

**Parameters**

`struct irq_domain *domain`
:   Domain below which interrupts must be freed

`unsigned int irq_base`
:   Base IRQ number

`unsigned int nr_irqs`
:   Number of IRQs to free

## Internal Functions Provided

This chapter contains the autogenerated documentation of the internal
functions.

void irq_domain_free_irqs(unsigned int virq, unsigned int nr_irqs)
:   Free IRQ number and associated data structures

**Parameters**

`unsigned int virq`
:   base IRQ number

`unsigned int nr_irqs`
:   number of IRQs to free

int irq_domain_activate_irq(struct [irq_data](irq-domain.md#c.irq_domain_activate_irq "irq_data") \*irq_data, bool reserve)
:   Call domain_ops->activate recursively to activate interrupt

**Parameters**

`struct irq_data *irq_data`
:   Outermost irq_data associated with interrupt

`bool reserve`
:   If set only reserve an interrupt vector instead of assigning one

**Description**

This is the second step to call domain_ops->activate to program interrupt
controllers, so the interrupt could actually get delivered.

void irq_domain_deactivate_irq(struct [irq_data](irq-domain.md#c.irq_domain_deactivate_irq "irq_data") \*irq_data)
:   Call domain_ops->deactivate recursively to deactivate interrupt

**Parameters**

`struct irq_data *irq_data`
:   outermost irq_data associated with interrupt

**Description**

It calls domain_ops->deactivate to program interrupt controllers to disable
interrupt delivery.
