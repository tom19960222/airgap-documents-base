---
collection: kernel
version: "6.8"
title: "IOMMUFD"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/iommufd.html
fetched_at: 2026-08-21T03:35:26+00:00
---
# IOMMUFD

Author
:   Jason Gunthorpe

Author
:   Kevin Tian

## Overview

IOMMUFD is the user API to control the IOMMU subsystem as it relates to managing
IO page tables from userspace using file descriptors. It intends to be general
and consumable by any driver that wants to expose DMA to userspace. These
drivers are eventually expected to deprecate any internal IOMMU logic
they may already/historically implement (e.g. vfio_iommu_type1.c).

At minimum iommufd provides universal support of managing I/O address spaces and
I/O page tables for all IOMMUs, with room in the design to add non-generic
features to cater to specific hardware functionality.

In this context the capital letter (IOMMUFD) refers to the subsystem while the
small letter (iommufd) refers to the file descriptors created via /dev/iommu for
use by userspace.

## Key Concepts

### User Visible Objects

Following IOMMUFD objects are exposed to userspace:

- IOMMUFD_OBJ_IOAS, representing an I/O address space (IOAS), allowing map/unmap
  of user space memory into ranges of I/O Virtual Address (IOVA).

  The IOAS is a functional replacement for the VFIO container, and like the VFIO
  container it copies an IOVA map to a list of iommu_domains held within it.
- IOMMUFD_OBJ_DEVICE, representing a device that is bound to iommufd by an
  external driver.
- IOMMUFD_OBJ_HW_PAGETABLE, representing an actual hardware I/O page table
  (i.e. a single struct iommu_domain) managed by the iommu driver.

  The IOAS has a list of HW_PAGETABLES that share the same IOVA mapping and
  it will synchronize its mapping with each member HW_PAGETABLE.

All user-visible objects are destroyed via the IOMMU_DESTROY uAPI.

The diagram below shows relationship between user-visible objects and kernel
datastructures (external to iommufd), with numbers referred to operations
creating the objects and links:

```
 _________________________________________________________
|                         iommufd                         |
|       [1]                                               |
|  _________________                                      |
| |                 |                                     |
| |                 |                                     |
| |                 |                                     |
| |                 |                                     |
| |                 |                                     |
| |                 |                                     |
| |                 |        [3]                 [2]      |
| |                 |    ____________         __________  |
| |      IOAS       |<--|            |<------|          | |
| |                 |   |HW_PAGETABLE|       |  DEVICE  | |
| |                 |   |____________|       |__________| |
| |                 |         |                   |       |
| |                 |         |                   |       |
| |                 |         |                   |       |
| |                 |         |                   |       |
| |                 |         |                   |       |
| |_________________|         |                   |       |
|         |                   |                   |       |
|_________|___________________|___________________|_______|
          |                   |                   |
          |              _____v______      _______v_____
          | PFN storage |            |    |             |
          |------------>|iommu_domain|    |struct device|
                        |____________|    |_____________|
```

1. IOMMUFD_OBJ_IOAS is created via the IOMMU_IOAS_ALLOC uAPI. An iommufd can
   hold multiple IOAS objects. IOAS is the most generic object and does not
   expose interfaces that are specific to single IOMMU drivers. All operations
   on the IOAS must operate equally on each of the iommu_domains inside of it.
2. IOMMUFD_OBJ_DEVICE is created when an external driver calls the IOMMUFD kAPI
   to bind a device to an iommufd. The driver is expected to implement a set of
   ioctls to allow userspace to initiate the binding operation. Successful
   completion of this operation establishes the desired DMA ownership over the
   device. The driver must also set the driver_managed_dma flag and must not
   touch the device until this operation succeeds.
3. IOMMUFD_OBJ_HW_PAGETABLE is created when an external driver calls the IOMMUFD
   kAPI to attach a bound device to an IOAS. Similarly the external driver uAPI
   allows userspace to initiate the attaching operation. If a compatible
   pagetable already exists then it is reused for the attachment. Otherwise a
   new pagetable object and iommu_domain is created. Successful completion of
   this operation sets up the linkages among IOAS, device and iommu_domain. Once
   this completes the device could do DMA.

   Every iommu_domain inside the IOAS is also represented to userspace as a
   HW_PAGETABLE object.

   > **Note:**
   >
   > Future IOMMUFD updates will provide an API to create and manipulate the
   > HW_PAGETABLE directly.

A device can only bind to an iommufd due to DMA ownership claim and attach to at
most one IOAS object (no support of PASID yet).

### Kernel Datastructure

User visible objects are backed by following datastructures:

- iommufd_ioas for IOMMUFD_OBJ_IOAS.
- iommufd_device for IOMMUFD_OBJ_DEVICE.
- iommufd_hw_pagetable for IOMMUFD_OBJ_HW_PAGETABLE.

Several terminologies when looking at these datastructures:

- Automatic domain - refers to an iommu domain created automatically when
  attaching a device to an IOAS object. This is compatible to the semantics of
  VFIO type1.
- Manual domain - refers to an iommu domain designated by the user as the
  target pagetable to be attached to by a device. Though currently there are
  no uAPIs to directly create such domain, the datastructure and algorithms
  are ready for handling that use case.
- In-kernel user - refers to something like a VFIO mdev that is using the
  IOMMUFD access interface to access the IOAS. This starts by creating an
  iommufd_access object that is similar to the domain binding a physical device
  would do. The access object will then allow converting IOVA ranges into struct
  page \* lists, or doing direct read/write to an IOVA.

iommufd_ioas serves as the metadata datastructure to manage how IOVA ranges are
mapped to memory pages, composed of:

- struct io_pagetable holding the IOVA map
- struct iopt_area's representing populated portions of IOVA
- struct iopt_pages representing the storage of PFNs
- struct iommu_domain representing the IO page table in the IOMMU
- struct iopt_pages_access representing in-kernel users of PFNs
- [`struct xarray`](../core-api/xarray.md#c.xarray "xarray") pinned_pfns holding a list of pages pinned by in-kernel users

Each iopt_pages represents a logical linear array of full PFNs. The PFNs are
ultimately derived from userspace VAs via an mm_struct. Once they have been
pinned the PFNs are stored in IOPTEs of an iommu_domain or inside the pinned_pfns
xarray if they have been pinned through an iommufd_access.

PFN have to be copied between all combinations of storage locations, depending
on what domains are present and what kinds of in-kernel "software access" users
exist. The mechanism ensures that a page is pinned only once.

An io_pagetable is composed of iopt_areas pointing at iopt_pages, along with a
list of iommu_domains that mirror the IOVA to PFN map.

Multiple io_pagetable-s, through their iopt_area-s, can share a single
iopt_pages which avoids multi-pinning and double accounting of page
consumption.

iommufd_ioas is shareable between subsystems, e.g. VFIO and VDPA, as long as
devices managed by different subsystems are bound to a same iommufd.

## IOMMUFD User API

**General ioctl format**

The ioctl interface follows a general format to allow for extensibility. Each
ioctl is passed in a structure pointer as the argument providing the size of
the structure in the first u32. The kernel checks that any structure space
beyond what it understands is 0. This allows userspace to use the backward
compatible portion while consistently using the newer, larger, structures.

ioctls use a standard meaning for common errnos:

> - ENOTTY: The IOCTL number itself is not supported at all
> - E2BIG: The IOCTL number is supported, but the provided structure has
>   non-zero in a part the kernel does not understand.
> - EOPNOTSUPP: The IOCTL number is supported, and the structure is
>   understood, however a known field has a value the kernel does not
>   understand or support.
> - EINVAL: Everything about the IOCTL was understood, but a field is not
>   correct.
> - ENOENT: An ID or IOVA provided does not exist.
> - ENOMEM: Out of memory.
> - EOVERFLOW: Mathematics overflowed.

As well as additional errnos, within specific ioctls.

struct iommu_destroy
:   ioctl(IOMMU_DESTROY)

**Definition**:

```
struct iommu_destroy {
    __u32 size;
    __u32 id;
};
```

**Members**

`size`
:   sizeof([`struct iommu_destroy`](iommufd.md#c.iommu_destroy "iommu_destroy"))

`id`
:   iommufd object ID to destroy. Can be any destroyable object type.

**Description**

Destroy any object held within iommufd.

struct iommu_ioas_alloc
:   ioctl(IOMMU_IOAS_ALLOC)

**Definition**:

```
struct iommu_ioas_alloc {
    __u32 size;
    __u32 flags;
    __u32 out_ioas_id;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_alloc`](iommufd.md#c.iommu_ioas_alloc "iommu_ioas_alloc"))

`flags`
:   Must be 0

`out_ioas_id`
:   Output IOAS ID for the allocated object

**Description**

Allocate an IO Address Space (IOAS) which holds an IO Virtual Address (IOVA)
to memory mapping.

struct iommu_iova_range
:   ioctl(IOMMU_IOVA_RANGE)

**Definition**:

```
struct iommu_iova_range {
    __aligned_u64 start;
    __aligned_u64 last;
};
```

**Members**

`start`
:   First IOVA

`last`
:   Inclusive last IOVA

**Description**

An interval in IOVA space.

struct iommu_ioas_iova_ranges
:   ioctl(IOMMU_IOAS_IOVA_RANGES)

**Definition**:

```
struct iommu_ioas_iova_ranges {
    __u32 size;
    __u32 ioas_id;
    __u32 num_iovas;
    __u32 __reserved;
    __aligned_u64 allowed_iovas;
    __aligned_u64 out_iova_alignment;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_iova_ranges`](iommufd.md#c.iommu_ioas_iova_ranges "iommu_ioas_iova_ranges"))

`ioas_id`
:   IOAS ID to read ranges from

`num_iovas`
:   Input/Output total number of ranges in the IOAS

`__reserved`
:   Must be 0

`allowed_iovas`
:   Pointer to the output array of [`struct iommu_iova_range`](iommufd.md#c.iommu_iova_range "iommu_iova_range")

`out_iova_alignment`
:   Minimum alignment required for mapping IOVA

**Description**

Query an IOAS for ranges of allowed IOVAs. Mapping IOVA outside these ranges
is not allowed. num_iovas will be set to the total number of iovas and
the allowed_iovas[] will be filled in as space permits.

The allowed ranges are dependent on the HW path the DMA operation takes, and
can change during the lifetime of the IOAS. A fresh empty IOAS will have a
full range, and each attached device will narrow the ranges based on that
device's HW restrictions. Detaching a device can widen the ranges. Userspace
should query ranges after every attach/detach to know what IOVAs are valid
for mapping.

On input num_iovas is the length of the allowed_iovas array. On output it is
the total number of iovas filled in. The ioctl will return -EMSGSIZE and set
num_iovas to the required value if num_iovas is too small. In this case the
caller should allocate a larger output array and re-issue the ioctl.

out_iova_alignment returns the minimum IOVA alignment that can be given
to IOMMU_IOAS_MAP/COPY. IOVA's must satisfy:

```
starting_iova % out_iova_alignment == 0
(starting_iova + length) % out_iova_alignment == 0
```

out_iova_alignment can be 1 indicating any IOVA is allowed. It cannot
be higher than the system PAGE_SIZE.

struct iommu_ioas_allow_iovas
:   ioctl(IOMMU_IOAS_ALLOW_IOVAS)

**Definition**:

```
struct iommu_ioas_allow_iovas {
    __u32 size;
    __u32 ioas_id;
    __u32 num_iovas;
    __u32 __reserved;
    __aligned_u64 allowed_iovas;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_allow_iovas`](iommufd.md#c.iommu_ioas_allow_iovas "iommu_ioas_allow_iovas"))

`ioas_id`
:   IOAS ID to allow IOVAs from

`num_iovas`
:   Input/Output total number of ranges in the IOAS

`__reserved`
:   Must be 0

`allowed_iovas`
:   Pointer to array of [`struct iommu_iova_range`](iommufd.md#c.iommu_iova_range "iommu_iova_range")

**Description**

Ensure a range of IOVAs are always available for allocation. If this call
succeeds then IOMMU_IOAS_IOVA_RANGES will never return a list of IOVA ranges
that are narrower than the ranges provided here. This call will fail if
IOMMU_IOAS_IOVA_RANGES is currently narrower than the given ranges.

When an IOAS is first created the IOVA_RANGES will be maximally sized, and as
devices are attached the IOVA will narrow based on the device restrictions.
When an allowed range is specified any narrowing will be refused, ie device
attachment can fail if the device requires limiting within the allowed range.

Automatic IOVA allocation is also impacted by this call. MAP will only
allocate within the allowed IOVAs if they are present.

This call replaces the entire allowed list with the given list.

enum iommufd_ioas_map_flags
:   Flags for map and copy

**Constants**

`IOMMU_IOAS_MAP_FIXED_IOVA`
:   If clear the kernel will compute an appropriate
    IOVA to place the mapping at

`IOMMU_IOAS_MAP_WRITEABLE`
:   DMA is allowed to write to this mapping

`IOMMU_IOAS_MAP_READABLE`
:   DMA is allowed to read from this mapping

struct iommu_ioas_map
:   ioctl(IOMMU_IOAS_MAP)

**Definition**:

```
struct iommu_ioas_map {
    __u32 size;
    __u32 flags;
    __u32 ioas_id;
    __u32 __reserved;
    __aligned_u64 user_va;
    __aligned_u64 length;
    __aligned_u64 iova;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_map`](iommufd.md#c.iommu_ioas_map "iommu_ioas_map"))

`flags`
:   Combination of [`enum iommufd_ioas_map_flags`](iommufd.md#c.iommufd_ioas_map_flags "iommufd_ioas_map_flags")

`ioas_id`
:   IOAS ID to change the mapping of

`__reserved`
:   Must be 0

`user_va`
:   Userspace pointer to start mapping from

`length`
:   Number of bytes to map

`iova`
:   IOVA the mapping was placed at. If IOMMU_IOAS_MAP_FIXED_IOVA is set
    then this must be provided as input.

**Description**

Set an IOVA mapping from a user pointer. If FIXED_IOVA is specified then the
mapping will be established at iova, otherwise a suitable location based on
the reserved and allowed lists will be automatically selected and returned in
iova.

If IOMMU_IOAS_MAP_FIXED_IOVA is specified then the iova range must currently
be unused, existing IOVA cannot be replaced.

struct iommu_ioas_copy
:   ioctl(IOMMU_IOAS_COPY)

**Definition**:

```
struct iommu_ioas_copy {
    __u32 size;
    __u32 flags;
    __u32 dst_ioas_id;
    __u32 src_ioas_id;
    __aligned_u64 length;
    __aligned_u64 dst_iova;
    __aligned_u64 src_iova;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_copy`](iommufd.md#c.iommu_ioas_copy "iommu_ioas_copy"))

`flags`
:   Combination of [`enum iommufd_ioas_map_flags`](iommufd.md#c.iommufd_ioas_map_flags "iommufd_ioas_map_flags")

`dst_ioas_id`
:   IOAS ID to change the mapping of

`src_ioas_id`
:   IOAS ID to copy from

`length`
:   Number of bytes to copy and map

`dst_iova`
:   IOVA the mapping was placed at. If IOMMU_IOAS_MAP_FIXED_IOVA is
    set then this must be provided as input.

`src_iova`
:   IOVA to start the copy

**Description**

Copy an already existing mapping from src_ioas_id and establish it in
dst_ioas_id. The src iova/length must exactly match a range used with
IOMMU_IOAS_MAP.

This may be used to efficiently clone a subset of an IOAS to another, or as a
kind of 'cache' to speed up mapping. Copy has an efficiency advantage over
establishing equivalent new mappings, as internal resources are shared, and
the kernel will pin the user memory only once.

struct iommu_ioas_unmap
:   ioctl(IOMMU_IOAS_UNMAP)

**Definition**:

```
struct iommu_ioas_unmap {
    __u32 size;
    __u32 ioas_id;
    __aligned_u64 iova;
    __aligned_u64 length;
};
```

**Members**

`size`
:   sizeof([`struct iommu_ioas_unmap`](iommufd.md#c.iommu_ioas_unmap "iommu_ioas_unmap"))

`ioas_id`
:   IOAS ID to change the mapping of

`iova`
:   IOVA to start the unmapping at

`length`
:   Number of bytes to unmap, and return back the bytes unmapped

**Description**

Unmap an IOVA range. The iova/length must be a superset of a previously
mapped range used with IOMMU_IOAS_MAP or IOMMU_IOAS_COPY. Splitting or
truncating ranges is not allowed. The values 0 to U64_MAX will unmap
everything.

enum iommufd_option
:   ioctl(IOMMU_OPTION_RLIMIT_MODE) and ioctl(IOMMU_OPTION_HUGE_PAGES)

**Constants**

`IOMMU_OPTION_RLIMIT_MODE`

> Change how RLIMIT_MEMLOCK accounting works. The caller must have privilege
> to invoke this. Value 0 (default) is user based accouting, 1 uses process
> based accounting. Global option, object_id must be 0

`IOMMU_OPTION_HUGE_PAGES`

> Value 1 (default) allows contiguous pages to be combined when generating
> iommu mappings. Value 0 disables combining, everything is mapped to
> PAGE_SIZE. This can be useful for benchmarking. This is a per-IOAS
> option, the object_id must be the IOAS ID.

enum iommufd_option_ops
:   ioctl(IOMMU_OPTION_OP_SET) and ioctl(IOMMU_OPTION_OP_GET)

**Constants**

`IOMMU_OPTION_OP_SET`
:   Set the option's value

`IOMMU_OPTION_OP_GET`
:   Get the option's value

struct iommu_option
:   iommu option multiplexer

**Definition**:

```
struct iommu_option {
    __u32 size;
    __u32 option_id;
    __u16 op;
    __u16 __reserved;
    __u32 object_id;
    __aligned_u64 val64;
};
```

**Members**

`size`
:   sizeof([`struct iommu_option`](iommufd.md#c.iommu_option "iommu_option"))

`option_id`
:   One of [`enum iommufd_option`](iommufd.md#c.iommufd_option "iommufd_option")

`op`
:   One of [`enum iommufd_option_ops`](iommufd.md#c.iommufd_option_ops "iommufd_option_ops")

`__reserved`
:   Must be 0

`object_id`
:   ID of the object if required

`val64`
:   Option value to set or value returned on get

**Description**

Change a simple option value. This multiplexor allows controlling options
on objects. IOMMU_OPTION_OP_SET will load an option and IOMMU_OPTION_OP_GET
will return the current value.

enum iommufd_vfio_ioas_op
:   IOMMU_VFIO_IOAS_\* ioctls

**Constants**

`IOMMU_VFIO_IOAS_GET`
:   Get the current compatibility IOAS

`IOMMU_VFIO_IOAS_SET`
:   Change the current compatibility IOAS

`IOMMU_VFIO_IOAS_CLEAR`
:   Disable VFIO compatibility

struct iommu_vfio_ioas
:   ioctl(IOMMU_VFIO_IOAS)

**Definition**:

```
struct iommu_vfio_ioas {
    __u32 size;
    __u32 ioas_id;
    __u16 op;
    __u16 __reserved;
};
```

**Members**

`size`
:   sizeof([`struct iommu_vfio_ioas`](iommufd.md#c.iommu_vfio_ioas "iommu_vfio_ioas"))

`ioas_id`
:   For IOMMU_VFIO_IOAS_SET the input IOAS ID to set
    For IOMMU_VFIO_IOAS_GET will output the IOAS ID

`op`
:   One of [`enum iommufd_vfio_ioas_op`](iommufd.md#c.iommufd_vfio_ioas_op "iommufd_vfio_ioas_op")

`__reserved`
:   Must be 0

**Description**

The VFIO compatibility support uses a single ioas because VFIO APIs do not
support the ID field. Set or Get the IOAS that VFIO compatibility will use.
When VFIO_GROUP_SET_CONTAINER is used on an iommufd it will get the
compatibility ioas, either by taking what is already set, or auto creating
one. From then on VFIO will continue to use that ioas and is not effected by
this ioctl. SET or CLEAR does not destroy any auto-created IOAS.

enum iommufd_hwpt_alloc_flags
:   Flags for HWPT allocation

**Constants**

`IOMMU_HWPT_ALLOC_NEST_PARENT`
:   If set, allocate a HWPT that can serve as
    the parent HWPT in a nesting configuration.

`IOMMU_HWPT_ALLOC_DIRTY_TRACKING`
:   Dirty tracking support for device IOMMU is
    enforced on device attachment

enum iommu_hwpt_vtd_s1_flags
:   Intel VT-d stage-1 page table entry attributes

**Constants**

`IOMMU_VTD_S1_SRE`
:   Supervisor request

`IOMMU_VTD_S1_EAFE`
:   Extended access enable

`IOMMU_VTD_S1_WPE`
:   Write protect enable

struct iommu_hwpt_vtd_s1
:   Intel VT-d stage-1 page table info (IOMMU_HWPT_DATA_VTD_S1)

**Definition**:

```
struct iommu_hwpt_vtd_s1 {
    __aligned_u64 flags;
    __aligned_u64 pgtbl_addr;
    __u32 addr_width;
    __u32 __reserved;
};
```

**Members**

`flags`
:   Combination of [`enum iommu_hwpt_vtd_s1_flags`](iommufd.md#c.iommu_hwpt_vtd_s1_flags "iommu_hwpt_vtd_s1_flags")

`pgtbl_addr`
:   The base address of the stage-1 page table.

`addr_width`
:   The address width of the stage-1 page table

`__reserved`
:   Must be 0

enum iommu_hwpt_data_type
:   IOMMU HWPT Data Type

**Constants**

`IOMMU_HWPT_DATA_NONE`
:   no data

`IOMMU_HWPT_DATA_VTD_S1`
:   Intel VT-d stage-1 page table

struct iommu_hwpt_alloc
:   ioctl(IOMMU_HWPT_ALLOC)

**Definition**:

```
struct iommu_hwpt_alloc {
    __u32 size;
    __u32 flags;
    __u32 dev_id;
    __u32 pt_id;
    __u32 out_hwpt_id;
    __u32 __reserved;
    __u32 data_type;
    __u32 data_len;
    __aligned_u64 data_uptr;
};
```

**Members**

`size`
:   sizeof([`struct iommu_hwpt_alloc`](iommufd.md#c.iommu_hwpt_alloc "iommu_hwpt_alloc"))

`flags`
:   Combination of [`enum iommufd_hwpt_alloc_flags`](iommufd.md#c.iommufd_hwpt_alloc_flags "iommufd_hwpt_alloc_flags")

`dev_id`
:   The device to allocate this HWPT for

`pt_id`
:   The IOAS or HWPT to connect this HWPT to

`out_hwpt_id`
:   The ID of the new HWPT

`__reserved`
:   Must be 0

`data_type`
:   One of [`enum iommu_hwpt_data_type`](iommufd.md#c.iommu_hwpt_data_type "iommu_hwpt_data_type")

`data_len`
:   Length of the type specific data

`data_uptr`
:   User pointer to the type specific data

**Description**

Explicitly allocate a hardware page table object. This is the same object
type that is returned by [`iommufd_device_attach()`](iommufd.md#c.iommufd_device_attach "iommufd_device_attach") and represents the
underlying iommu driver's iommu_domain kernel object.

A kernel-managed HWPT will be created with the mappings from the given
IOAS via the **pt_id**. The **data_type** for this allocation must be set to
IOMMU_HWPT_DATA_NONE. The HWPT can be allocated as a parent HWPT for a
nesting configuration by passing IOMMU_HWPT_ALLOC_NEST_PARENT via **flags**.

A user-managed nested HWPT will be created from a given parent HWPT via
**pt_id**, in which the parent HWPT must be allocated previously via the
same ioctl from a given IOAS (**pt_id**). In this case, the **data_type**
must be set to a pre-defined type corresponding to an I/O page table
type supported by the underlying IOMMU hardware.

If the **data_type** is set to IOMMU_HWPT_DATA_NONE, **data_len** and
**data_uptr** should be zero. Otherwise, both **data_len** and **data_uptr**
must be given.

enum iommu_hw_info_vtd_flags
:   Flags for VT-d hw_info

**Constants**

`IOMMU_HW_INFO_VTD_ERRATA_772415_SPR17`
:   If set, disallow read-only mappings
    on a nested_parent domain.
    <https://www.intel.com/content/www/us/en/content-details/772415/content-details.html>

struct iommu_hw_info_vtd
:   Intel VT-d hardware information

**Definition**:

```
struct iommu_hw_info_vtd {
    __u32 flags;
    __u32 __reserved;
    __aligned_u64 cap_reg;
    __aligned_u64 ecap_reg;
};
```

**Members**

`flags`
:   Combination of [`enum iommu_hw_info_vtd_flags`](iommufd.md#c.iommu_hw_info_vtd_flags "iommu_hw_info_vtd_flags")

`__reserved`
:   Must be 0

`cap_reg`
:   Value of Intel VT-d capability register defined in VT-d spec
    section 11.4.2 Capability Register.

`ecap_reg`
:   Value of Intel VT-d capability register defined in VT-d spec
    section 11.4.3 Extended Capability Register.

**Description**

User needs to understand the Intel VT-d specification to decode the
register value.

enum iommu_hw_info_type
:   IOMMU Hardware Info Types

**Constants**

`IOMMU_HW_INFO_TYPE_NONE`
:   Used by the drivers that do not report hardware
    info

`IOMMU_HW_INFO_TYPE_INTEL_VTD`
:   Intel VT-d iommu info type

enum iommufd_hw_capabilities

**Constants**

`IOMMU_HW_CAP_DIRTY_TRACKING`
:   IOMMU hardware support for dirty tracking
    If available, it means the following APIs
    are supported:

    > IOMMU_HWPT_GET_DIRTY_BITMAP
    > IOMMU_HWPT_SET_DIRTY_TRACKING

struct iommu_hw_info
:   ioctl(IOMMU_GET_HW_INFO)

**Definition**:

```
struct iommu_hw_info {
    __u32 size;
    __u32 flags;
    __u32 dev_id;
    __u32 data_len;
    __aligned_u64 data_uptr;
    __u32 out_data_type;
    __u32 __reserved;
    __aligned_u64 out_capabilities;
};
```

**Members**

`size`
:   sizeof([`struct iommu_hw_info`](iommufd.md#c.iommu_hw_info "iommu_hw_info"))

`flags`
:   Must be 0

`dev_id`
:   The device bound to the iommufd

`data_len`
:   Input the length of a user buffer in bytes. Output the length of
    data that kernel supports

`data_uptr`
:   User pointer to a user-space buffer used by the kernel to fill
    the iommu type specific hardware information data

`out_data_type`
:   Output the iommu hardware info type as defined in the [`enum
    iommu_hw_info_type`](iommufd.md#c.iommu_hw_info_type "iommu_hw_info_type").

`__reserved`
:   Must be 0

`out_capabilities`
:   Output the generic iommu capability info type as defined
    in the enum iommu_hw_capabilities.

**Description**

Query an iommu type specific hardware information data from an iommu behind
a given device that has been bound to iommufd. This hardware info data will
be used to sync capabilities between the virtual iommu and the physical
iommu, e.g. a nested translation setup needs to check the hardware info, so
a guest stage-1 page table can be compatible with the physical iommu.

To capture an iommu type specific hardware information data, **data_uptr** and
its length **data_len** must be provided. Trailing bytes will be zeroed if the
user buffer is larger than the data that kernel has. Otherwise, kernel only
fills the buffer using the given length in **data_len**. If the ioctl succeeds,
**data_len** will be updated to the length that kernel actually supports,
**out_data_type** will be filled to decode the data filled in the buffer
pointed by **data_uptr**. Input **data_len** == zero is allowed.

struct iommu_hwpt_set_dirty_tracking
:   ioctl(IOMMU_HWPT_SET_DIRTY_TRACKING)

**Definition**:

```
struct iommu_hwpt_set_dirty_tracking {
    __u32 size;
    __u32 flags;
    __u32 hwpt_id;
    __u32 __reserved;
};
```

**Members**

`size`
:   sizeof([`struct iommu_hwpt_set_dirty_tracking`](iommufd.md#c.iommu_hwpt_set_dirty_tracking "iommu_hwpt_set_dirty_tracking"))

`flags`
:   Combination of enum iommufd_hwpt_set_dirty_tracking_flags

`hwpt_id`
:   HW pagetable ID that represents the IOMMU domain

`__reserved`
:   Must be 0

**Description**

Toggle dirty tracking on an HW pagetable.

enum iommufd_hwpt_get_dirty_bitmap_flags
:   Flags for getting dirty bits

**Constants**

`IOMMU_HWPT_GET_DIRTY_BITMAP_NO_CLEAR`
:   Just read the PTEs without clearing
    any dirty bits metadata. This flag
    can be passed in the expectation
    where the next operation is an unmap
    of the same IOVA range.

struct iommu_hwpt_get_dirty_bitmap
:   ioctl(IOMMU_HWPT_GET_DIRTY_BITMAP)

**Definition**:

```
struct iommu_hwpt_get_dirty_bitmap {
    __u32 size;
    __u32 hwpt_id;
    __u32 flags;
    __u32 __reserved;
    __aligned_u64 iova;
    __aligned_u64 length;
    __aligned_u64 page_size;
    __aligned_u64 data;
};
```

**Members**

`size`
:   sizeof([`struct iommu_hwpt_get_dirty_bitmap`](iommufd.md#c.iommu_hwpt_get_dirty_bitmap "iommu_hwpt_get_dirty_bitmap"))

`hwpt_id`
:   HW pagetable ID that represents the IOMMU domain

`flags`
:   Combination of [`enum iommufd_hwpt_get_dirty_bitmap_flags`](iommufd.md#c.iommufd_hwpt_get_dirty_bitmap_flags "iommufd_hwpt_get_dirty_bitmap_flags")

`__reserved`
:   Must be 0

`iova`
:   base IOVA of the bitmap first bit

`length`
:   IOVA range size

`page_size`
:   page size granularity of each bit in the bitmap

`data`
:   bitmap where to set the dirty bits. The bitmap bits each
    represent a page_size which you deviate from an arbitrary iova.

**Description**

Checking a given IOVA is dirty:

> data[(iova / page_size) / 64] & (1ULL << ((iova / page_size) % 64))

Walk the IOMMU pagetables for a given IOVA range to return a bitmap
with the dirty IOVAs. In doing so it will also by default clear any
dirty bit metadata set in the IOPTE.

enum iommu_hwpt_invalidate_data_type
:   IOMMU HWPT Cache Invalidation Data Type

**Constants**

`IOMMU_HWPT_INVALIDATE_DATA_VTD_S1`
:   Invalidation data for VTD_S1

enum iommu_hwpt_vtd_s1_invalidate_flags
:   Flags for Intel VT-d stage-1 cache invalidation

**Constants**

`IOMMU_VTD_INV_FLAGS_LEAF`
:   Indicates whether the invalidation applies
    to all-levels page structure cache or just
    the leaf PTE cache.

struct iommu_hwpt_vtd_s1_invalidate
:   Intel VT-d cache invalidation (IOMMU_HWPT_INVALIDATE_DATA_VTD_S1)

**Definition**:

```
struct iommu_hwpt_vtd_s1_invalidate {
    __aligned_u64 addr;
    __aligned_u64 npages;
    __u32 flags;
    __u32 __reserved;
};
```

**Members**

`addr`
:   The start address of the range to be invalidated. It needs to
    be 4KB aligned.

`npages`
:   Number of contiguous 4K pages to be invalidated.

`flags`
:   Combination of [`enum iommu_hwpt_vtd_s1_invalidate_flags`](iommufd.md#c.iommu_hwpt_vtd_s1_invalidate_flags "iommu_hwpt_vtd_s1_invalidate_flags")

`__reserved`
:   Must be 0

**Description**

The Intel VT-d specific invalidation data for user-managed stage-1 cache
invalidation in nested translation. Userspace uses this structure to
tell the impacted cache scope after modifying the stage-1 page table.

Invalidating all the caches related to the page table by setting **addr**
to be 0 and **npages** to be U64_MAX.

The device TLB will be invalidated automatically if ATS is enabled.

struct iommu_hwpt_invalidate
:   ioctl(IOMMU_HWPT_INVALIDATE)

**Definition**:

```
struct iommu_hwpt_invalidate {
    __u32 size;
    __u32 hwpt_id;
    __aligned_u64 data_uptr;
    __u32 data_type;
    __u32 entry_len;
    __u32 entry_num;
    __u32 __reserved;
};
```

**Members**

`size`
:   sizeof([`struct iommu_hwpt_invalidate`](iommufd.md#c.iommu_hwpt_invalidate "iommu_hwpt_invalidate"))

`hwpt_id`
:   ID of a nested HWPT for cache invalidation

`data_uptr`
:   User pointer to an array of driver-specific cache invalidation
    data.

`data_type`
:   One of [`enum iommu_hwpt_invalidate_data_type`](iommufd.md#c.iommu_hwpt_invalidate_data_type "iommu_hwpt_invalidate_data_type"), defining the data
    type of all the entries in the invalidation request array. It
    should be a type supported by the hwpt pointed by **hwpt_id**.

`entry_len`
:   Length (in bytes) of a request entry in the request array

`entry_num`
:   Input the number of cache invalidation requests in the array.
    Output the number of requests successfully handled by kernel.

`__reserved`
:   Must be 0.

**Description**

Invalidate the iommu cache for user-managed page table. Modifications on a
user-managed page table should be followed by this operation to sync cache.
Each ioctl can support one or more cache invalidation requests in the array
that has a total size of **entry_len** \* **entry_num**.

An empty invalidation request array by setting **entry_num\*\*==0 is allowed, and
\*\*entry_len** and **data_uptr** would be ignored in this case. This can be used to
check if the given **data_type** is supported or not by kernel.

## IOMMUFD Kernel API

The IOMMUFD kAPI is device-centric with group-related tricks managed behind the
scene. This allows the external drivers calling such kAPI to implement a simple
device-centric uAPI for connecting its device to an iommufd, instead of
explicitly imposing the group semantics in its uAPI as VFIO does.

struct iommufd_device \*iommufd_device_bind(struct iommufd_ctx \*ictx, struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, u32 \*id)
:   Bind a physical device to an iommu fd

**Parameters**

`struct iommufd_ctx *ictx`
:   iommufd file descriptor

`struct device *dev`
:   Pointer to a physical device struct

`u32 *id`
:   Output ID number to return to userspace for this device

**Description**

A successful bind establishes an ownership over the device and returns
struct iommufd_device pointer, otherwise returns error pointer.

A driver using this API must set driver_managed_dma and must not touch
the device until this routine succeeds and establishes ownership.

Binding a PCI device places the entire RID under iommufd control.

The caller must undo this with [`iommufd_device_unbind()`](iommufd.md#c.iommufd_device_unbind "iommufd_device_unbind")

bool iommufd_ctx_has_group(struct iommufd_ctx \*ictx, struct iommu_group \*group)
:   True if any device within the group is bound to the ictx

**Parameters**

`struct iommufd_ctx *ictx`
:   iommufd file descriptor

`struct iommu_group *group`
:   Pointer to a physical iommu_group struct

**Description**

True if any device within the group has been bound to this ictx, ex. via
[`iommufd_device_bind()`](iommufd.md#c.iommufd_device_bind "iommufd_device_bind"), therefore implying ictx ownership of the group.

void iommufd_device_unbind(struct iommufd_device \*idev)
:   Undo [`iommufd_device_bind()`](iommufd.md#c.iommufd_device_bind "iommufd_device_bind")

**Parameters**

`struct iommufd_device *idev`
:   Device returned by [`iommufd_device_bind()`](iommufd.md#c.iommufd_device_bind "iommufd_device_bind")

**Description**

Release the device from iommufd control. The DMA ownership will return back
to unowned with DMA controlled by the DMA API. This invalidates the
iommufd_device pointer, other APIs that consume it must not be called
concurrently.

int iommufd_device_attach(struct iommufd_device \*idev, u32 \*pt_id)
:   Connect a device to an iommu_domain

**Parameters**

`struct iommufd_device *idev`
:   device to attach

`u32 *pt_id`
:   Input a IOMMUFD_OBJ_IOAS, or IOMMUFD_OBJ_HWPT_PAGING
    Output the IOMMUFD_OBJ_HWPT_PAGING ID

**Description**

This connects the device to an iommu_domain, either automatically or manually
selected. Once this completes the device could do DMA.

The caller should return the resulting pt_id back to userspace.
This function is undone by calling [`iommufd_device_detach()`](iommufd.md#c.iommufd_device_detach "iommufd_device_detach").

int iommufd_device_replace(struct iommufd_device \*idev, u32 \*pt_id)
:   Change the device's iommu_domain

**Parameters**

`struct iommufd_device *idev`
:   device to change

`u32 *pt_id`
:   Input a IOMMUFD_OBJ_IOAS, or IOMMUFD_OBJ_HWPT_PAGING
    Output the IOMMUFD_OBJ_HWPT_PAGING ID

**Description**

This is the same as:

```
iommufd_device_detach();
iommufd_device_attach();
```

If it fails then no change is made to the attachment. The iommu driver may
implement this so there is no disruption in translation. This can only be
called if [`iommufd_device_attach()`](iommufd.md#c.iommufd_device_attach "iommufd_device_attach") has already succeeded.

void iommufd_device_detach(struct iommufd_device \*idev)
:   Disconnect a device to an iommu_domain

**Parameters**

`struct iommufd_device *idev`
:   device to detach

**Description**

Undo [`iommufd_device_attach()`](iommufd.md#c.iommufd_device_attach "iommufd_device_attach"). This disconnects the idev from the previously
attached pt_id. The device returns back to a blocked DMA translation.

struct iommufd_access \*iommufd_access_create(struct iommufd_ctx \*ictx, const struct iommufd_access_ops \*ops, void \*data, u32 \*id)
:   Create an iommufd_access

**Parameters**

`struct iommufd_ctx *ictx`
:   iommufd file descriptor

`const struct iommufd_access_ops *ops`
:   Driver's ops to associate with the access

`void *data`
:   Opaque data to pass into ops functions

`u32 *id`
:   Output ID number to return to userspace for this access

**Description**

An iommufd_access allows a driver to read/write to the IOAS without using
DMA. The underlying CPU memory can be accessed using the
[`iommufd_access_pin_pages()`](iommufd.md#c.iommufd_access_pin_pages "iommufd_access_pin_pages") or [`iommufd_access_rw()`](iommufd.md#c.iommufd_access_rw "iommufd_access_rw") functions.

The provided ops are required to use [`iommufd_access_pin_pages()`](iommufd.md#c.iommufd_access_pin_pages "iommufd_access_pin_pages").

void iommufd_access_destroy(struct iommufd_access \*access)
:   Destroy an iommufd_access

**Parameters**

`struct iommufd_access *access`
:   The access to destroy

**Description**

The caller must stop using the access before destroying it.

void iommufd_access_unpin_pages(struct iommufd_access \*access, unsigned long iova, unsigned long length)
:   Undo iommufd_access_pin_pages

**Parameters**

`struct iommufd_access *access`
:   IOAS access to act on

`unsigned long iova`
:   Starting IOVA

`unsigned long length`
:   Number of bytes to access

**Description**

Return the struct page's. The caller must stop accessing them before calling
this. The iova/length must exactly match the one provided to access_pages.

int iommufd_access_pin_pages(struct iommufd_access \*access, unsigned long iova, unsigned long length, struct page \*\*out_pages, unsigned int flags)
:   Return a list of pages under the iova

**Parameters**

`struct iommufd_access *access`
:   IOAS access to act on

`unsigned long iova`
:   Starting IOVA

`unsigned long length`
:   Number of bytes to access

`struct page **out_pages`
:   Output page list

`unsigned int flags`
:   IOPMMUFD_ACCESS_RW_\* flags

**Description**

Reads **length** bytes starting at iova and returns the struct page \* pointers.
These can be kmap'd by the caller for CPU access.

The caller must perform [`iommufd_access_unpin_pages()`](iommufd.md#c.iommufd_access_unpin_pages "iommufd_access_unpin_pages") when done to balance
this.

This API always requires a page aligned iova. This happens naturally if the
ioas alignment is >= PAGE_SIZE and the iova is PAGE_SIZE aligned. However
smaller alignments have corner cases where this API can fail on otherwise
aligned iova.

int iommufd_access_rw(struct iommufd_access \*access, unsigned long iova, void \*data, size_t length, unsigned int flags)
:   Read or write data under the iova

**Parameters**

`struct iommufd_access *access`
:   IOAS access to act on

`unsigned long iova`
:   Starting IOVA

`void *data`
:   Kernel buffer to copy to/from

`size_t length`
:   Number of bytes to access

`unsigned int flags`
:   IOMMUFD_ACCESS_RW_\* flags

**Description**

Copy kernel to/from data into the range given by IOVA/length. If flags
indicates IOMMUFD_ACCESS_RW_KTHREAD then a large copy can be optimized
by changing it into copy_to/from_user().

void iommufd_ctx_get(struct iommufd_ctx \*ictx)
:   Get a context reference

**Parameters**

`struct iommufd_ctx *ictx`
:   Context to get

**Description**

The caller must already hold a valid reference to ictx.

struct iommufd_ctx \*iommufd_ctx_from_file(struct [file](iommufd.md#c.iommufd_ctx_from_file "file") \*file)
:   Acquires a reference to the iommufd context

**Parameters**

`struct file *file`
:   File to obtain the reference from

**Description**

Returns a pointer to the iommufd_ctx, otherwise ERR_PTR. The struct file
remains owned by the caller and the caller must still do fput. On success
the caller is responsible to call [`iommufd_ctx_put()`](iommufd.md#c.iommufd_ctx_put "iommufd_ctx_put").

struct iommufd_ctx \*iommufd_ctx_from_fd(int fd)
:   Acquires a reference to the iommufd context

**Parameters**

`int fd`
:   File descriptor to obtain the reference from

**Description**

Returns a pointer to the iommufd_ctx, otherwise ERR_PTR. On success
the caller is responsible to call [`iommufd_ctx_put()`](iommufd.md#c.iommufd_ctx_put "iommufd_ctx_put").

void iommufd_ctx_put(struct iommufd_ctx \*ictx)
:   Put back a reference

**Parameters**

`struct iommufd_ctx *ictx`
:   Context to put back

### VFIO and IOMMUFD

Connecting a VFIO device to iommufd can be done in two ways.

First is a VFIO compatible way by directly implementing the /dev/vfio/vfio
container IOCTLs by mapping them into io_pagetable operations. Doing so allows
the use of iommufd in legacy VFIO applications by symlinking /dev/vfio/vfio to
/dev/iommufd or extending VFIO to SET_CONTAINER using an iommufd instead of a
container fd.

The second approach directly extends VFIO to support a new set of device-centric
user API based on aforementioned IOMMUFD kernel API. It requires userspace
change but better matches the IOMMUFD API semantics and easier to support new
iommufd features when comparing it to the first approach.

Currently both approaches are still work-in-progress.

There are still a few gaps to be resolved to catch up with VFIO type1, as
documented in iommufd_vfio_check_extension().

## Future TODOs

Currently IOMMUFD supports only kernel-managed I/O page table, similar to VFIO
type1. New features on the radar include:

> - Binding iommu_domain's to PASID/SSID
> - Userspace page tables, for ARM, x86 and S390
> - Kernel bypass'd invalidation of user page tables
> - Re-use of the KVM page table in the IOMMU
> - Dirty page tracking in the IOMMU
> - Runtime Increase/Decrease of IOPTE size
> - PRI support with faults resolved in userspace
