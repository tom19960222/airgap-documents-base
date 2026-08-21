---
collection: kernel
version: "6.8"
title: "Error Detection And Correction (EDAC) Devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/edac.html
fetched_at: 2026-08-21T03:30:48+00:00
---
# Error Detection And Correction (EDAC) Devices

## Main Concepts used at the EDAC subsystem

There are several things to be aware of that aren't at all obvious, like
*sockets, \*socket sets*, *banks*, *rows*, *chip-select rows*, *channels*,
etc...

These are some of the many terms that are thrown about that don't always
mean what people think they mean (Inconceivable!). In the interest of
creating a common ground for discussion, terms and their definitions
will be established.

- Memory devices

The individual DRAM chips on a memory stick. These devices commonly
output 4 and 8 bits each (x4, x8). Grouping several of these in parallel
provides the number of bits that the memory controller expects:
typically 72 bits, in order to provide 64 bits + 8 bits of ECC data.

- Memory Stick

A printed circuit board that aggregates multiple memory devices in
parallel. In general, this is the Field Replaceable Unit (FRU) which
gets replaced, in the case of excessive errors. Most often it is also
called DIMM (Dual Inline Memory Module).

- Memory Socket

A physical connector on the motherboard that accepts a single memory
stick. Also called as "slot" on several datasheets.

- Channel

A memory controller channel, responsible to communicate with a group of
DIMMs. Each channel has its own independent control (command) and data
bus, and can be used independently or grouped with other channels.

- Branch

It is typically the highest hierarchy on a Fully-Buffered DIMM memory
controller. Typically, it contains two channels. Two channels at the
same branch can be used in single mode or in lockstep mode. When
lockstep is enabled, the cacheline is doubled, but it generally brings
some performance penalty. Also, it is generally not possible to point to
just one memory stick when an error occurs, as the error correction code
is calculated using two DIMMs instead of one. Due to that, it is capable
of correcting more errors than on single mode.

- Single-channel

The data accessed by the memory controller is contained into one dimm
only. E. g. if the data is 64 bits-wide, the data flows to the CPU using
one 64 bits parallel access. Typically used with SDR, DDR, DDR2 and DDR3
memories. FB-DIMM and RAMBUS use a different concept for channel, so
this concept doesn't apply there.

- Double-channel

The data size accessed by the memory controller is interlaced into two
dimms, accessed at the same time. E. g. if the DIMM is 64 bits-wide (72
bits with ECC), the data flows to the CPU using a 128 bits parallel
access.

- Chip-select row

This is the name of the DRAM signal used to select the DRAM ranks to be
accessed. Common chip-select rows for single channel are 64 bits, for
dual channel 128 bits. It may not be visible by the memory controller,
as some DIMM types have a memory buffer that can hide direct access to
it from the Memory Controller.

- Single-Ranked stick

A Single-ranked stick has 1 chip-select row of memory. Motherboards
commonly drive two chip-select pins to a memory stick. A single-ranked
stick, will occupy only one of those rows. The other will be unused.

- Double-Ranked stick

A double-ranked stick has two chip-select rows which access different
sets of memory devices. The two rows cannot be accessed concurrently.

- Double-sided stick

**DEPRECATED TERM**, see [Double-Ranked stick](edac.md#doubleranked).

A double-sided stick has two chip-select rows which access different sets
of memory devices. The two rows cannot be accessed concurrently.
"Double-sided" is irrespective of the memory devices being mounted on
both sides of the memory stick.

- Socket set

All of the memory sticks that are required for a single memory access or
all of the memory sticks spanned by a chip-select row. A single socket
set has two chip-select rows and if double-sided sticks are used these
will occupy those chip-select rows.

- Bank

This term is avoided because it is unclear when needing to distinguish
between chip-select rows and socket sets.

- High Bandwidth Memory (HBM)

HBM is a new memory type with low power consumption and ultra-wide
communication lanes. It uses vertically stacked memory chips (DRAM dies)
interconnected by microscopic wires called "through-silicon vias," or
TSVs.

Several stacks of HBM chips connect to the CPU or GPU through an ultra-fast
interconnect called the "interposer". Therefore, HBM's characteristics
are nearly indistinguishable from on-chip integrated RAM.

## Memory Controllers

Most of the EDAC core is focused on doing Memory Controller error detection.
The [`edac_mc_alloc()`](edac.md#c.edac_mc_alloc "edac_mc_alloc"). It uses internally the struct `mem_ctl_info`
to describe the memory controllers, with is an opaque struct for the EDAC
drivers. Only the EDAC core is allowed to touch it.

enum dev_type
:   describe the type of memory DRAM chips used at the stick

**Constants**

`DEV_UNKNOWN`
:   Can't be determined, or MC doesn't support detect it

`DEV_X1`
:   1 bit for data

`DEV_X2`
:   2 bits for data

`DEV_X4`
:   4 bits for data

`DEV_X8`
:   8 bits for data

`DEV_X16`
:   16 bits for data

`DEV_X32`
:   32 bits for data

`DEV_X64`
:   64 bits for data

**Description**

Typical values are x4 and x8.

enum hw_event_mc_err_type
:   type of the detected error

**Constants**

`HW_EVENT_ERR_CORRECTED`
:   Corrected Error - Indicates that an ECC
    corrected error was detected

`HW_EVENT_ERR_UNCORRECTED`
:   Uncorrected Error - Indicates an error that
    can't be corrected by ECC, but it is not
    fatal (maybe it is on an unused memory area,
    or the memory controller could recover from
    it for example, by re-trying the operation).

`HW_EVENT_ERR_DEFERRED`
:   Deferred Error - Indicates an uncorrectable
    error whose handling is not urgent. This could
    be due to hardware data poisoning where the
    system can continue operation until the poisoned
    data is consumed. Preemptive measures may also
    be taken, e.g. offlining pages, etc.

`HW_EVENT_ERR_FATAL`
:   Fatal Error - Uncorrected error that could not
    be recovered.

`HW_EVENT_ERR_INFO`
:   Informational - The CPER spec defines a forth
    type of error: informational logs.

enum mem_type
:   memory types. For a more detailed reference, please see <http://en.wikipedia.org/wiki/DRAM>

**Constants**

`MEM_EMPTY`
:   Empty csrow

`MEM_RESERVED`
:   Reserved csrow type

`MEM_UNKNOWN`
:   Unknown csrow type

`MEM_FPM`
:   FPM - Fast Page Mode, used on systems up to 1995.

`MEM_EDO`
:   EDO - Extended data out, used on systems up to 1998.

`MEM_BEDO`
:   BEDO - Burst Extended data out, an EDO variant.

`MEM_SDR`
:   SDR - Single data rate SDRAM
    <http://en.wikipedia.org/wiki/Synchronous_dynamic_random-access_memory>
    They use 3 pins for chip select: Pins 0 and 2 are
    for rank 0; pins 1 and 3 are for rank 1, if the memory
    is dual-rank.

`MEM_RDR`
:   Registered SDR SDRAM

`MEM_DDR`
:   Double data rate SDRAM
    <http://en.wikipedia.org/wiki/DDR_SDRAM>

`MEM_RDDR`
:   Registered Double data rate SDRAM
    This is a variant of the DDR memories.
    A registered memory has a buffer inside it, hiding
    part of the memory details to the memory controller.

`MEM_RMBS`
:   Rambus DRAM, used on a few Pentium III/IV controllers.

`MEM_DDR2`
:   DDR2 RAM, as described at JEDEC JESD79-2F.
    Those memories are labeled as "PC2-" instead of "PC" to
    differentiate from DDR.

`MEM_FB_DDR2`
:   Fully-Buffered DDR2, as described at JEDEC Std No. 205
    and JESD206.
    Those memories are accessed per DIMM slot, and not by
    a chip select signal.

`MEM_RDDR2`
:   Registered DDR2 RAM
    This is a variant of the DDR2 memories.

`MEM_XDR`
:   Rambus XDR
    It is an evolution of the original RAMBUS memories,
    created to compete with DDR2. Weren't used on any
    x86 arch, but cell_edac PPC memory controller uses it.

`MEM_DDR3`
:   DDR3 RAM

`MEM_RDDR3`
:   Registered DDR3 RAM
    This is a variant of the DDR3 memories.

`MEM_LRDDR3`
:   Load-Reduced DDR3 memory.

`MEM_LPDDR3`
:   Low-Power DDR3 memory.

`MEM_DDR4`
:   Unbuffered DDR4 RAM

`MEM_RDDR4`
:   Registered DDR4 RAM
    This is a variant of the DDR4 memories.

`MEM_LRDDR4`
:   Load-Reduced DDR4 memory.

`MEM_LPDDR4`
:   Low-Power DDR4 memory.

`MEM_DDR5`
:   Unbuffered DDR5 RAM

`MEM_RDDR5`
:   Registered DDR5 RAM

`MEM_LRDDR5`
:   Load-Reduced DDR5 memory.

`MEM_NVDIMM`
:   Non-volatile RAM

`MEM_WIO2`
:   Wide I/O 2.

`MEM_HBM2`
:   High bandwidth Memory Gen 2.

`MEM_HBM3`
:   High bandwidth Memory Gen 3.

enum edac_type
:   Error Detection and Correction capabilities and mode

**Constants**

`EDAC_UNKNOWN`
:   Unknown if ECC is available

`EDAC_NONE`
:   Doesn't support ECC

`EDAC_RESERVED`
:   Reserved ECC type

`EDAC_PARITY`
:   Detects parity errors

`EDAC_EC`
:   Error Checking - no correction

`EDAC_SECDED`
:   Single bit error correction, Double detection

`EDAC_S2ECD2ED`
:   Chipkill x2 devices - do these exist?

`EDAC_S4ECD4ED`
:   Chipkill x4 devices

`EDAC_S8ECD8ED`
:   Chipkill x8 devices

`EDAC_S16ECD16ED`
:   Chipkill x16 devices

enum scrub_type
:   scrubbing capabilities

**Constants**

`SCRUB_UNKNOWN`
:   Unknown if scrubber is available

`SCRUB_NONE`
:   No scrubber

`SCRUB_SW_PROG`
:   SW progressive (sequential) scrubbing

`SCRUB_SW_SRC`
:   Software scrub only errors

`SCRUB_SW_PROG_SRC`
:   Progressive software scrub from an error

`SCRUB_SW_TUNABLE`
:   Software scrub frequency is tunable

`SCRUB_HW_PROG`
:   HW progressive (sequential) scrubbing

`SCRUB_HW_SRC`
:   Hardware scrub only errors

`SCRUB_HW_PROG_SRC`
:   Progressive hardware scrub from an error

`SCRUB_HW_TUNABLE`
:   Hardware scrub frequency is tunable

enum edac_mc_layer_type
:   memory controller hierarchy layer

**Constants**

`EDAC_MC_LAYER_BRANCH`
:   memory layer is named "branch"

`EDAC_MC_LAYER_CHANNEL`
:   memory layer is named "channel"

`EDAC_MC_LAYER_SLOT`
:   memory layer is named "slot"

`EDAC_MC_LAYER_CHIP_SELECT`
:   memory layer is named "chip select"

`EDAC_MC_LAYER_ALL_MEM`
:   memory layout is unknown. All memory is mapped
    as a single memory area. This is used when
    retrieving errors from a firmware driven driver.

**Description**

This enum is used by the drivers to tell edac_mc_sysfs what name should
be used when describing a memory stick location.

struct edac_mc_layer
:   describes the memory controller hierarchy

**Definition**:

```
struct edac_mc_layer {
    enum edac_mc_layer_type type;
    unsigned size;
    bool is_virt_csrow;
};
```

**Members**

`type`
:   layer type

`size`
:   number of components per layer. For example,
    if the channel layer has two channels, size = 2

`is_virt_csrow`
:   This layer is part of the "csrow" when old API
    compatibility mode is enabled. Otherwise, it is
    a channel

struct rank_info
:   contains the information for one DIMM rank

**Definition**:

```
struct rank_info {
    int chan_idx;
    struct csrow_info *csrow;
    struct dimm_info *dimm;
    u32 ce_count;
};
```

**Members**

`chan_idx`
:   channel number where the rank is (typically, 0 or 1)

`csrow`
:   A pointer to the chip select row structure (the parent
    structure). The location of the rank is given by
    the (csrow->csrow_idx, chan_idx) vector.

`dimm`
:   A pointer to the DIMM structure, where the DIMM label
    information is stored.

`ce_count`
:   number of correctable errors for this rank

**Description**

FIXME: Currently, the EDAC core model will assume one DIMM per rank.
:   This is a bad assumption, but it makes this patch easier. Later
    patches in this series will fix this issue.

struct edac_raw_error_desc
:   Raw error report structure

**Definition**:

```
struct edac_raw_error_desc {
    char location[LOCATION_SIZE];
    char label[(EDAC_MC_LABEL_LEN + 1 + sizeof(OTHER_LABEL)) * EDAC_MAX_LABELS];
    long grain;
    u16 error_count;
    enum hw_event_mc_err_type type;
    int top_layer;
    int mid_layer;
    int low_layer;
    unsigned long page_frame_number;
    unsigned long offset_in_page;
    unsigned long syndrome;
    const char *msg;
    const char *other_detail;
};
```

**Members**

`location`
:   location of the error

`label`
:   label of the affected DIMM(s)

`grain`
:   minimum granularity for an error report, in bytes

`error_count`
:   number of errors of the same type

`type`
:   severity of the error (CE/UE/Fatal)

`top_layer`
:   top layer of the error (layer[0])

`mid_layer`
:   middle layer of the error (layer[1])

`low_layer`
:   low layer of the error (layer[2])

`page_frame_number`
:   page where the error happened

`offset_in_page`
:   page offset

`syndrome`
:   syndrome of the error (or 0 if unknown or if
    the syndrome is not applicable)

`msg`
:   error message

`other_detail`
:   other driver-specific detail about the error

struct dimm_info \*edac_get_dimm(struct mem_ctl_info \*mci, int layer0, int layer1, int layer2)
:   Get DIMM info from a memory controller given by [layer0,layer1,layer2] position

**Parameters**

`struct mem_ctl_info *mci`
:   MC descriptor struct mem_ctl_info

`int layer0`
:   layer0 position

`int layer1`
:   layer1 position. Unused if n_layers < 2

`int layer2`
:   layer2 position. Unused if n_layers < 3

**Description**

For 1 layer, this function returns "dimms[layer0]";

For 2 layers, this function is similar to allocating a two-dimensional
array and returning "dimms[layer0][layer1]";

For 3 layers, this function is similar to allocating a tri-dimensional
array and returning "dimms[layer0][layer1][layer2]";

struct mem_ctl_info \*edac_mc_alloc(unsigned int mc_num, unsigned int n_layers, struct [edac_mc_layer](edac.md#c.edac_mc_layer "edac_mc_layer") \*layers, unsigned int sz_pvt)
:   Allocate and partially fill a struct `mem_ctl_info`.

**Parameters**

`unsigned int mc_num`
:   Memory controller number

`unsigned int n_layers`
:   Number of MC hierarchy layers

`struct edac_mc_layer *layers`
:   Describes each layer as seen by the Memory Controller

`unsigned int sz_pvt`
:   size of private storage needed

**Description**

Everything is kmalloc'ed as one big chunk - more efficient.
Only can be used if all structures have the same lifetime - otherwise
you have to allocate and initialize your own structures.

Use [`edac_mc_free()`](edac.md#c.edac_mc_free "edac_mc_free") to free mc structures allocated by this function.

> **Note:**
>
> drivers handle multi-rank memories in different ways: in some
> drivers, one multi-rank memory stick is mapped as one entry, while, in
> others, a single multi-rank memory stick would be mapped into several
> entries. Currently, this function will allocate multiple struct dimm_info
> on such scenarios, as grouping the multiple ranks require drivers change.

**Return**

> On success, return a pointer to struct mem_ctl_info pointer;
> `NULL` otherwise

const char \*edac_get_owner(void)
:   Return the owner's mod_name of EDAC MC

**Parameters**

`void`
:   no arguments

**Return**

> Pointer to mod_name string when EDAC MC is owned. NULL otherwise.

void edac_mc_free(struct mem_ctl_info \*mci)
:   Frees a previously allocated **mci** structure

**Parameters**

`struct mem_ctl_info *mci`
:   pointer to a struct mem_ctl_info structure

bool edac_has_mcs(void)
:   Check if any MCs have been allocated.

**Parameters**

`void`
:   no arguments

**Return**

> True if MC instances have been registered successfully.
> False otherwise.

struct mem_ctl_info \*edac_mc_find(int idx)
:   Search for a mem_ctl_info structure whose index is **idx**.

**Parameters**

`int idx`
:   index to be seek

**Description**

If found, return a pointer to the structure.
Else return NULL.

struct mem_ctl_info \*find_mci_by_dev(struct [device](infrastructure.md#c.device "device") \*dev)
:   Scan list of controllers looking for the one that manages the **dev** device.

**Parameters**

`struct device *dev`
:   pointer to a [`struct device`](infrastructure.md#c.device "device") related with the MCI

**Return**

on success, returns a pointer to struct `mem_ctl_info`;
`NULL` otherwise.

struct mem_ctl_info \*edac_mc_del_mc(struct [device](infrastructure.md#c.device "device") \*dev)
:   Remove sysfs entries for mci structure associated with **dev** and remove mci structure from global list.

**Parameters**

`struct device *dev`
:   Pointer to struct [`device`](infrastructure.md#c.device "device") representing mci structure to remove.

**Return**

pointer to removed mci structure, or `NULL` if device not found.

int edac_mc_find_csrow_by_page(struct mem_ctl_info \*mci, unsigned long page)
:   Ancillary routine to identify what csrow contains a memory page.

**Parameters**

`struct mem_ctl_info *mci`
:   pointer to a struct mem_ctl_info structure

`unsigned long page`
:   memory page to find

**Return**

on success, returns the csrow. -1 if not found.

void edac_raw_mc_handle_error(struct [edac_raw_error_desc](edac.md#c.edac_raw_error_desc "edac_raw_error_desc") \*e)
:   Reports a memory event to userspace without doing anything to discover the error location.

**Parameters**

`struct edac_raw_error_desc *e`
:   error description

**Description**

This raw function is used internally by [`edac_mc_handle_error()`](edac.md#c.edac_mc_handle_error "edac_mc_handle_error"). It should
only be called directly when the hardware error come directly from BIOS,
like in the case of APEI GHES driver.

void edac_mc_handle_error(const enum [hw_event_mc_err_type](edac.md#c.hw_event_mc_err_type "hw_event_mc_err_type") type, struct mem_ctl_info \*mci, const u16 error_count, const unsigned long page_frame_number, const unsigned long offset_in_page, const unsigned long syndrome, const int top_layer, const int mid_layer, const int low_layer, const char \*msg, const char \*other_detail)
:   Reports a memory event to userspace.

**Parameters**

`const enum hw_event_mc_err_type type`
:   severity of the error (CE/UE/Fatal)

`struct mem_ctl_info *mci`
:   a struct mem_ctl_info pointer

`const u16 error_count`
:   Number of errors of the same type

`const unsigned long page_frame_number`
:   mem page where the error occurred

`const unsigned long offset_in_page`
:   offset of the error inside the page

`const unsigned long syndrome`
:   ECC syndrome

`const int top_layer`
:   Memory layer[0] position

`const int mid_layer`
:   Memory layer[1] position

`const int low_layer`
:   Memory layer[2] position

`const char *msg`
:   Message meaningful to the end users that
    explains the event

`const char *other_detail`
:   Technical details about the event that
    may help hardware manufacturers and
    EDAC developers to analyse the event

## PCI Controllers

The EDAC subsystem provides a mechanism to handle PCI controllers by calling
the [`edac_pci_alloc_ctl_info()`](edac.md#c.edac_pci_alloc_ctl_info "edac_pci_alloc_ctl_info"). It will use the struct
`edac_pci_ctl_info` to describe the PCI controllers.

struct edac_pci_ctl_info \*edac_pci_alloc_ctl_info(unsigned int sz_pvt, const char \*edac_pci_name)
:   The alloc() function for the 'edac_pci' control info structure.

**Parameters**

`unsigned int sz_pvt`
:   size of the private info at struct `edac_pci_ctl_info`

`const char *edac_pci_name`
:   name of the PCI device

**Description**

The chip driver will allocate one of these for each
edac_pci it is going to control/register with the EDAC CORE.

**Return**

a pointer to struct `edac_pci_ctl_info` on success; `NULL` otherwise.

void edac_pci_free_ctl_info(struct edac_pci_ctl_info \*pci)
:   Last action on the pci control structure.

**Parameters**

`struct edac_pci_ctl_info *pci`
:   pointer to struct `edac_pci_ctl_info`

**Description**

Calls the remove sysfs information, which will unregister
this control struct's kobj. When that kobj's ref count
goes to zero, its release function will be call and then
[`kfree()`](../core-api/mm-api.md#c.kfree "kfree") the memory.

int edac_pci_alloc_index(void)
:   Allocate a unique PCI index number

**Parameters**

`void`
:   no arguments

**Return**

> allocated index number

int edac_pci_add_device(struct edac_pci_ctl_info \*pci, int edac_idx)
:   Insert the 'edac_dev' structure into the edac_pci global list and create sysfs entries associated with edac_pci structure.

**Parameters**

`struct edac_pci_ctl_info *pci`
:   pointer to the edac_device structure to be added to the list

`int edac_idx`
:   A unique numeric identifier to be assigned to the
    'edac_pci' structure.

**Return**

> 0 on Success, or an error code on failure

struct edac_pci_ctl_info \*edac_pci_del_device(struct [device](infrastructure.md#c.device "device") \*dev)

**Parameters**

`struct device *dev`

> Pointer to '[`struct device`](infrastructure.md#c.device "device")' representing edac_pci structure
> to remove

**Description**

> Remove sysfs entries for specified edac_pci structure and
> then remove edac_pci structure from global list

**Return**

> Pointer to removed edac_pci structure,
> or `NULL` if device not found

struct edac_pci_ctl_info \*edac_pci_create_generic_ctl(struct [device](infrastructure.md#c.device "device") \*dev, const char \*mod_name)

**Parameters**

`struct device *dev`
:   pointer to struct [`device`](infrastructure.md#c.device "device");

`const char *mod_name`
:   name of the PCI device

**Description**

> A generic constructor for a PCI parity polling device
> Some systems have more than one domain of PCI busses.
> For systems with one domain, then this API will
> provide for a generic poller.

This routine calls the [`edac_pci_alloc_ctl_info()`](edac.md#c.edac_pci_alloc_ctl_info "edac_pci_alloc_ctl_info") for
the generic device, with default values

**Return**

Pointer to struct `edac_pci_ctl_info` on success, `NULL` on
:   failure.

void edac_pci_release_generic_ctl(struct edac_pci_ctl_info \*pci)

**Parameters**

`struct edac_pci_ctl_info *pci`
:   pointer to struct `edac_pci_ctl_info`

**Description**

> The release function of a generic EDAC PCI polling device

int edac_pci_create_sysfs(struct edac_pci_ctl_info \*pci)

**Parameters**

`struct edac_pci_ctl_info *pci`
:   pointer to struct `edac_pci_ctl_info`

**Description**

> Create the controls/attributes for the specified EDAC PCI device

void edac_pci_remove_sysfs(struct edac_pci_ctl_info \*pci)

**Parameters**

`struct edac_pci_ctl_info *pci`
:   pointer to struct `edac_pci_ctl_info`

**Description**

> remove the controls and attributes for this EDAC PCI device

## EDAC Blocks

The EDAC subsystem also provides a generic mechanism to report errors on
other parts of the hardware via `edac_device_alloc_ctl_info()` function.

The structures `edac_dev_sysfs_block_attribute`,
`edac_device_block`, `edac_device_instance` and
`edac_device_ctl_info` provide a generic or abstract 'edac_device'
representation at sysfs.

This set of structures and the code that implements the APIs for the same, provide for registering EDAC type devices which are NOT standard memory or
PCI, like:

- CPU caches (L1 and L2)
- DMA engines
- Core CPU switches
- Fabric switch units
- PCIe interface controllers
- other EDAC/ECC type devices that can be monitored for
  errors, etc.

It allows for a 2 level set of hierarchy.

For example, a cache could be composed of L1, L2 and L3 levels of cache.
Each CPU core would have its own L1 cache, while sharing L2 and maybe L3
caches. On such case, those can be represented via the following sysfs
nodes:

```
/sys/devices/system/edac/..

pci/            <existing pci directory (if available)>
mc/             <existing memory device directory>
cpu/cpu0/..     <L1 and L2 block directory>
        /L1-cache/ce_count
                 /ue_count
        /L2-cache/ce_count
                 /ue_count
cpu/cpu1/..     <L1 and L2 block directory>
        /L1-cache/ce_count
                 /ue_count
        /L2-cache/ce_count
                 /ue_count
...

the L1 and L2 directories would be "edac_device_block's"
```

int edac_device_add_device(struct edac_device_ctl_info \*edac_dev)
:   Insert the 'edac_dev' structure into the edac_device global list and create sysfs entries associated with edac_device structure.

**Parameters**

`struct edac_device_ctl_info *edac_dev`
:   pointer to edac_device structure to be added to the list
    'edac_device' structure.

**Return**

> 0 on Success, or an error code on failure

struct edac_device_ctl_info \*edac_device_del_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   Remove sysfs entries for specified edac_device structure and then remove edac_device structure from global list

**Parameters**

`struct device *dev`

> Pointer to struct [`device`](infrastructure.md#c.device "device") representing the edac device
> structure to remove.

**Return**

> Pointer to removed edac_device structure,
> or `NULL` if device not found.

void edac_device_handle_ce_count(struct edac_device_ctl_info \*edac_dev, unsigned int count, int inst_nr, int block_nr, const char \*msg)
:   Log correctable errors.

**Parameters**

`struct edac_device_ctl_info *edac_dev`
:   pointer to struct `edac_device_ctl_info`

`unsigned int count`
:   Number of errors to log.

`int inst_nr`
:   number of the instance where the CE error happened

`int block_nr`
:   number of the block where the CE error happened

`const char *msg`
:   message to be printed

void edac_device_handle_ue_count(struct edac_device_ctl_info \*edac_dev, unsigned int count, int inst_nr, int block_nr, const char \*msg)
:   Log uncorrectable errors.

**Parameters**

`struct edac_device_ctl_info *edac_dev`
:   pointer to struct `edac_device_ctl_info`

`unsigned int count`
:   Number of errors to log.

`int inst_nr`
:   number of the instance where the CE error happened

`int block_nr`
:   number of the block where the CE error happened

`const char *msg`
:   message to be printed

void edac_device_handle_ce(struct edac_device_ctl_info \*edac_dev, int inst_nr, int block_nr, const char \*msg)
:   Log a single correctable error

**Parameters**

`struct edac_device_ctl_info *edac_dev`
:   pointer to struct `edac_device_ctl_info`

`int inst_nr`
:   number of the instance where the CE error happened

`int block_nr`
:   number of the block where the CE error happened

`const char *msg`
:   message to be printed

void edac_device_handle_ue(struct edac_device_ctl_info \*edac_dev, int inst_nr, int block_nr, const char \*msg)
:   Log a single uncorrectable error

**Parameters**

`struct edac_device_ctl_info *edac_dev`
:   pointer to struct `edac_device_ctl_info`

`int inst_nr`
:   number of the instance where the UE error happened

`int block_nr`
:   number of the block where the UE error happened

`const char *msg`
:   message to be printed

int edac_device_alloc_index(void)
:   Allocate a unique device index number

**Parameters**

`void`
:   no arguments

**Return**

> allocated index number

## Heterogeneous system support

An AMD heterogeneous system is built by connecting the data fabrics of
both CPUs and GPUs via custom xGMI links. Thus, the data fabric on the
GPU nodes can be accessed the same way as the data fabric on CPU nodes.

The MI200 accelerators are data center GPUs. They have 2 data fabrics,
and each GPU data fabric contains four Unified Memory Controllers (UMC).
Each UMC contains eight channels. Each UMC channel controls one 128-bit
HBM2e (2GB) channel (equivalent to 8 X 2GB ranks). This creates a total
of 4096-bits of DRAM data bus.

While the UMC is interfacing a 16GB (8high X 2GB DRAM) HBM stack, each UMC
channel is interfacing 2GB of DRAM (represented as rank).

Memory controllers on AMD GPU nodes can be represented in EDAC thusly:

> GPU DF / GPU Node -> EDAC MC
> GPU UMC -> EDAC CSROW
> GPU UMC channel -> EDAC CHANNEL

For example: a heterogeneous system with 1 AMD CPU is connected to
4 MI200 (Aldebaran) GPUs using xGMI.

Some more heterogeneous hardware details:

- The CPU UMC (Unified Memory Controller) is mostly the same as the GPU UMC.
  They have chip selects (csrows) and channels. However, the layouts are different
  for performance, physical layout, or other reasons.
- CPU UMCs use 1 channel, In this case UMC = EDAC channel. This follows the
  marketing speak. CPU has X memory channels, etc.
- CPU UMCs use up to 4 chip selects, So UMC chip select = EDAC CSROW.
- GPU UMCs use 1 chip select, So UMC = EDAC CSROW.
- GPU UMCs use 8 channels, So UMC channel = EDAC channel.

The EDAC subsystem provides a mechanism to handle AMD heterogeneous
systems by calling system specific ops for both CPUs and GPUs.

AMD GPU nodes are enumerated in sequential order based on the PCI
hierarchy, and the first GPU node is assumed to have a Node ID value
following those of the CPU nodes after latter are fully populated:

```
$ ls /sys/devices/system/edac/mc/
        mc0   - CPU MC node 0
        mc1  |
        mc2  |- GPU card[0] => node 0(mc1), node 1(mc2)
        mc3  |
        mc4  |- GPU card[1] => node 0(mc3), node 1(mc4)
        mc5  |
        mc6  |- GPU card[2] => node 0(mc5), node 1(mc6)
        mc7  |
        mc8  |- GPU card[3] => node 0(mc7), node 1(mc8)
```

For example, a heterogeneous system with one AMD CPU is connected to
four MI200 (Aldebaran) GPUs using xGMI. This topology can be represented
via the following sysfs entries:

```
/sys/devices/system/edac/mc/..

CPU                     # CPU node
├── mc 0

GPU Nodes are enumerated sequentially after CPU nodes have been populated
GPU card 1              # Each MI200 GPU has 2 nodes/mcs
├── mc 1                # GPU node 0 == mc1, Each MC node has 4 UMCs/CSROWs
│   ├── csrow 0         # UMC 0
│   │   ├── channel 0   # Each UMC has 8 channels
│   │   ├── channel 1   # size of each channel is 2 GB, so each UMC has 16 GB
│   │   ├── channel 2
│   │   ├── channel 3
│   │   ├── channel 4
│   │   ├── channel 5
│   │   ├── channel 6
│   │   ├── channel 7
│   ├── csrow 1         # UMC 1
│   │   ├── channel 0
│   │   ├── ..
│   │   ├── channel 7
│   ├── ..              ..
│   ├── csrow 3         # UMC 3
│   │   ├── channel 0
│   │   ├── ..
│   │   ├── channel 7
│   ├── rank 0
│   ├── ..              ..
│   ├── rank 31         # total 32 ranks/dimms from 4 UMCs
├
├── mc 2                # GPU node 1 == mc2
│   ├── ..              # each GPU has total 64 GB

GPU card 2
├── mc 3
│   ├── ..
├── mc 4
│   ├── ..

GPU card 3
├── mc 5
│   ├── ..
├── mc 6
│   ├── ..

GPU card 4
├── mc 7
│   ├── ..
├── mc 8
│   ├── ..
```
