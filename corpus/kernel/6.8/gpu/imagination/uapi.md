---
collection: kernel
version: "6.8"
title: "UAPI"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/imagination/uapi.html
fetched_at: 2026-08-21T03:39:04+00:00
---
# UAPI

The sources associated with this section can be found in `pvr_drm.h`.

The PowerVR IOCTL argument structs have a few limitations in place, in
addition to the standard kernel restrictions:

> - All members must be type-aligned.
> - The overall struct must be padded to 64-bit alignment.
> - Explicit padding is almost always required. This takes the form of
>   `_padding_[x]` members of sufficient size to pad to the next power-of-two
>   alignment, where [x] is the offset into the struct in hexadecimal. Arrays
>   are never used for alignment. Padding fields must be zeroed; this is
>   always checked.
> - Unions may only appear as the last member of a struct.
> - Individual union members may grow in the future. The space between the
>   end of a union member and the end of its containing union is considered
>   "implicit padding" and must be zeroed. This is always checked.

In addition to the IOCTL argument structs, the PowerVR UAPI makes use of
DEV_QUERY argument structs. These are used to fetch information about the
device and runtime. These structs are subject to the same rules set out
above.

## OBJECT ARRAYS

struct drm_pvr_obj_array
:   Container used to pass arrays of objects

**Definition**:

```
struct drm_pvr_obj_array {
    __u32 stride;
    __u32 count;
    __u64 array;
};
```

**Members**

`stride`
:   Stride of object struct. Used for versioning.

`count`
:   Number of objects in the array.

`array`
:   User pointer to an array of objects.

**Description**

It is not unusual to have to extend objects to pass new parameters, and the DRM
ioctl infrastructure is supporting that by padding ioctl arguments with zeros
when the data passed by userspace is smaller than the struct defined in the
drm_ioctl_desc, thus keeping things backward compatible. This type is just
applying the same concepts to indirect objects passed through arrays referenced
from the main ioctl arguments structure: the stride basically defines the size
of the object passed by userspace, which allows the kernel driver to pad with
zeros when it's smaller than the size of the object it expects.

Use `DRM_PVR_OBJ_ARRAY()` to fill object array fields, unless you
have a very good reason not to.

DRM_PVR_OBJ_ARRAY

`DRM_PVR_OBJ_ARRAY (cnt, ptr)`

> Helper macro for filling [`struct drm_pvr_obj_array`](uapi.md#c.drm_pvr_obj_array "drm_pvr_obj_array").

**Parameters**

`cnt`
:   Number of elements pointed to py **ptr**.

`ptr`
:   Pointer to start of a C array.

**Return**

Literal of type [`struct drm_pvr_obj_array`](uapi.md#c.drm_pvr_obj_array "drm_pvr_obj_array").

## IOCTLS

PVR_IOCTL

`PVR_IOCTL (_ioctl, _mode, _data)`

> Build a PowerVR IOCTL number

**Parameters**

`_ioctl`
:   An incrementing id for this IOCTL. Added to `DRM_COMMAND_BASE`.

`_mode`
:   Must be one of `DRM_IOR`, `DRM_IOW` or `DRM_IOWR`.

`_data`
:   The type of the args struct passed by this IOCTL.

**Description**

The struct referred to by **_data** must have a `drm_pvr_ioctl_` prefix and an
`_args suffix`. They are therefore omitted from **_data**.

This should only be used to build the constants described below; it should
never be used to call an IOCTL directly.

**Return**

An IOCTL number to be passed to ioctl() from userspace.

### DEV_QUERY

enum drm_pvr_dev_query
:   For use with [`drm_pvr_ioctl_dev_query_args.type`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args") to indicate the type of the receiving container.

**Constants**

`DRM_PVR_DEV_QUERY_GPU_INFO_GET`
:   The dev query args contain a pointer
    to [`struct drm_pvr_dev_query_gpu_info`](uapi.md#c.drm_pvr_dev_query_gpu_info "drm_pvr_dev_query_gpu_info").

`DRM_PVR_DEV_QUERY_RUNTIME_INFO_GET`
:   The dev query args contain a
    pointer to [`struct drm_pvr_dev_query_runtime_info`](uapi.md#c.drm_pvr_dev_query_runtime_info "drm_pvr_dev_query_runtime_info").

`DRM_PVR_DEV_QUERY_QUIRKS_GET`
:   The dev query args contain a pointer
    to [`struct drm_pvr_dev_query_quirks`](uapi.md#c.drm_pvr_dev_query_quirks "drm_pvr_dev_query_quirks").

`DRM_PVR_DEV_QUERY_ENHANCEMENTS_GET`
:   The dev query args contain a
    pointer to [`struct drm_pvr_dev_query_enhancements`](uapi.md#c.drm_pvr_dev_query_enhancements "drm_pvr_dev_query_enhancements").

`DRM_PVR_DEV_QUERY_HEAP_INFO_GET`
:   The dev query args contain a
    pointer to [`struct drm_pvr_dev_query_heap_info`](uapi.md#c.drm_pvr_dev_query_heap_info "drm_pvr_dev_query_heap_info").

`DRM_PVR_DEV_QUERY_STATIC_DATA_AREAS_GET`
:   The dev query args contain
    a pointer to [`struct drm_pvr_dev_query_static_data_areas`](uapi.md#c.drm_pvr_dev_query_static_data_areas "drm_pvr_dev_query_static_data_areas").

**Description**

Append only. Do not reorder.

struct drm_pvr_ioctl_dev_query_args
:   Arguments for `DRM_IOCTL_PVR_DEV_QUERY`.

**Definition**:

```
struct drm_pvr_ioctl_dev_query_args {
    __u32 type;
    __u32 size;
    __u64 pointer;
};
```

**Members**

`type`
:   Type of query and output struct. See [`enum drm_pvr_dev_query`](uapi.md#c.drm_pvr_dev_query "drm_pvr_dev_query").

`size`
:   Size of the receiving struct, see **type**.

    After a successful call this will be updated to the written byte
    length.
    Can also be used to get the minimum byte length (see **pointer**).
    This allows additional fields to be appended to the structs in
    future.

`pointer`
:   Pointer to struct **type**.

    Must be large enough to contain **size** bytes.
    If pointer is NULL, the expected size will be returned in the **size**
    field, but no other data will be written.

struct drm_pvr_dev_query_gpu_info
:   Container used to fetch information about the graphics processor.

**Definition**:

```
struct drm_pvr_dev_query_gpu_info {
    __u64 gpu_id;
    __u32 num_phantoms;
    __u32 _padding_c;
};
```

**Members**

`gpu_id`
:   GPU identifier.

    For all currently supported GPUs this is the BVNC encoded as a 64-bit
    value as follows:

    > | 63..48 | 47..32 | 31..16 | 15..0 |
    > | --- | --- | --- | --- |
    > | B | V | N | C |

`num_phantoms`
:   Number of Phantoms present.

`_padding_c`
:   Reserved. This field must be zeroed.

**Description**

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_QUERY_GPU_INFO_GET`.

struct drm_pvr_dev_query_runtime_info
:   Container used to fetch information about the graphics runtime.

**Definition**:

```
struct drm_pvr_dev_query_runtime_info {
    __u64 free_list_min_pages;
    __u64 free_list_max_pages;
    __u32 common_store_alloc_region_size;
    __u32 common_store_partition_space_size;
    __u32 max_coeffs;
    __u32 cdm_max_local_mem_size_regs;
};
```

**Members**

`free_list_min_pages`
:   Minimum allowed free list size,
    in PM physical pages.

`free_list_max_pages`
:   Maximum allowed free list size,
    in PM physical pages.

`common_store_alloc_region_size`
:   Size of the Allocation
    Region within the Common Store used for coefficient and shared
    registers, in dwords.

`common_store_partition_space_size`
:   Size of the
    Partition Space within the Common Store for output buffers, in
    dwords.

`max_coeffs`
:   Maximum coefficients, in dwords.

`cdm_max_local_mem_size_regs`
:   Maximum amount of local
    memory available to a compute kernel, in dwords.

**Description**

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_QUERY_RUNTIME_INFO_GET`.

struct drm_pvr_dev_query_quirks
:   Container used to fetch information about hardware fixes for which the device may require support in the user mode driver.

**Definition**:

```
struct drm_pvr_dev_query_quirks {
    __u64 quirks;
    __u16 count;
    __u16 musthave_count;
    __u32 _padding_c;
};
```

**Members**

`quirks`
:   A userspace address for the hardware quirks __u32 array.

    The first **musthave_count** items in the list are quirks that the
    client must support for this device. If userspace does not support
    all these quirks then functionality is not guaranteed and client
    initialisation must fail.
    The remaining quirks in the list affect userspace and the kernel or
    firmware. They are disabled by default and require userspace to
    opt-in. The opt-in mechanism depends on the quirk.

`count`
:   Length of **quirks** (number of __u32).

`musthave_count`
:   The number of entries in **quirks** that are
    mandatory, starting at index 0.

`_padding_c`
:   Reserved. This field must be zeroed.

**Description**

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_QUERY_QUIRKS_GET`.

struct drm_pvr_dev_query_enhancements
:   Container used to fetch information about optional enhancements supported by the device that require support in the user mode driver.

**Definition**:

```
struct drm_pvr_dev_query_enhancements {
    __u64 enhancements;
    __u16 count;
    __u16 _padding_a;
    __u32 _padding_c;
};
```

**Members**

`enhancements`
:   A userspace address for the hardware enhancements
    __u32 array.

    These enhancements affect userspace and the kernel or firmware. They
    are disabled by default and require userspace to opt-in. The opt-in
    mechanism depends on the enhancement.

`count`
:   Length of **enhancements** (number of __u32).

`_padding_a`
:   Reserved. This field must be zeroed.

`_padding_c`
:   Reserved. This field must be zeroed.

**Description**

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_ENHANCEMENTS_GET`.

enum drm_pvr_heap_id
:   Array index for heap info data returned by `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

**Constants**

`DRM_PVR_HEAP_GENERAL`
:   General purpose heap.

`DRM_PVR_HEAP_PDS_CODE_DATA`
:   PDS code and data heap.

`DRM_PVR_HEAP_USC_CODE`
:   USC code heap.

`DRM_PVR_HEAP_RGNHDR`
:   Region header heap. Only used if GPU has BRN63142.

`DRM_PVR_HEAP_VIS_TEST`
:   Visibility test heap.

`DRM_PVR_HEAP_TRANSFER_FRAG`
:   Transfer fragment heap.

`DRM_PVR_HEAP_COUNT`
:   The number of heaps returned by
    `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

    More heaps may be added, so this also serves as the copy limit when
    sent by the caller.

**Description**

For compatibility reasons all indices will be present in the returned array,
however some heaps may not be present. These are indicated where
[`struct drm_pvr_heap`](uapi.md#c.drm_pvr_heap "drm_pvr_heap").size is set to zero.

struct drm_pvr_heap
:   Container holding information about a single heap.

**Definition**:

```
struct drm_pvr_heap {
    __u64 base;
    __u64 size;
    __u32 flags;
    __u32 page_size_log2;
};
```

**Members**

`base`
:   Base address of heap.

`size`
:   Size of heap, in bytes. Will be 0 if the heap is not present.

`flags`
:   Flags for this heap. Currently always 0.

`page_size_log2`
:   Log2 of page size.

**Description**

This will always be fetched as an array.

struct drm_pvr_dev_query_heap_info
:   Container used to fetch information about heaps supported by the device driver.

**Definition**:

```
struct drm_pvr_dev_query_heap_info {
    struct drm_pvr_obj_array heaps;
};
```

**Members**

`heaps`
:   Array of [`struct drm_pvr_heap`](uapi.md#c.drm_pvr_heap "drm_pvr_heap"). If pointer is NULL, the count
    and stride will be updated with those known to the driver version, to
    facilitate allocation by the caller.

**Description**

Please note all driver-supported heaps will be returned up to `heaps.count`.
Some heaps will not be present in all devices, which will be indicated by
[`struct drm_pvr_heap`](uapi.md#c.drm_pvr_heap "drm_pvr_heap").size being set to zero.

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

enum drm_pvr_static_data_area_usage
:   Array index for static data area info returned by `DRM_PVR_DEV_QUERY_STATIC_DATA_AREAS_GET`.

**Constants**

`DRM_PVR_STATIC_DATA_AREA_EOT`
:   End of Tile PDS program code segment.

    The End of Tile PDS task runs at completion of a tile during a fragment job, and is
    responsible for emitting the tile to the Pixel Back End.

`DRM_PVR_STATIC_DATA_AREA_FENCE`
:   MCU fence area, used during cache flush and
    invalidation.

    This must point to valid physical memory but the contents otherwise are not used.

`DRM_PVR_STATIC_DATA_AREA_VDM_SYNC`
:   VDM sync program.

    The VDM sync program is used to synchronise multiple areas of the GPU hardware.

`DRM_PVR_STATIC_DATA_AREA_YUV_CSC`
:   YUV coefficients.

    Area contains up to 16 slots with stride of 64 bytes. Each is a 3x4 matrix of u16 fixed
    point numbers, with 1 sign bit, 2 integer bits and 13 fractional bits.

    The slots are :
    0 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_RGB_IDENTITY_KHR
    1 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY_KHR (full range)
    2 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_IDENTITY_KHR (conformant range)
    3 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709_KHR (full range)
    4 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709_KHR (conformant range)
    5 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601_KHR (full range)
    6 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601_KHR (conformant range)
    7 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020_KHR (full range)
    8 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020_KHR (conformant range)
    9 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_601_KHR (conformant range, 10 bit)
    10 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_709_KHR (conformant range, 10 bit)
    11 = VK_SAMPLER_YCBCR_MODEL_CONVERSION_YCBCR_2020_KHR (conformant range, 10 bit)
    14 = Identity (biased)
    15 = Identity

**Description**

For compatibility reasons all indices will be present in the returned array,
however some areas may not be present. These are indicated where
[`struct drm_pvr_static_data_area`](uapi.md#c.drm_pvr_static_data_area "drm_pvr_static_data_area").size is set to zero.

struct drm_pvr_static_data_area
:   Container holding information about a single static data area.

**Definition**:

```
struct drm_pvr_static_data_area {
    __u16 area_usage;
    __u16 location_heap_id;
    __u32 size;
    __u64 offset;
};
```

**Members**

`area_usage`
:   Usage of static data area.
    See [`enum drm_pvr_static_data_area_usage`](uapi.md#c.drm_pvr_static_data_area_usage "drm_pvr_static_data_area_usage").

`location_heap_id`
:   Array index of heap where this of static data
    area is located. This array is fetched using
    `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

`size`
:   Size of static data area. Not present if set to zero.

`offset`
:   Offset of static data area from start of heap.

**Description**

This will always be fetched as an array.

struct drm_pvr_dev_query_static_data_areas
:   Container used to fetch information about the static data areas in heaps supported by the device driver.

**Definition**:

```
struct drm_pvr_dev_query_static_data_areas {
    struct drm_pvr_obj_array static_data_areas;
};
```

**Members**

`static_data_areas`
:   Array of [`struct drm_pvr_static_data_area`](uapi.md#c.drm_pvr_static_data_area "drm_pvr_static_data_area"). If
    pointer is NULL, the count and stride will be updated with those
    known to the driver version, to facilitate allocation by the caller.

**Description**

Please note all driver-supported static data areas will be returned up to
`static_data_areas.count`. Some will not be present for all devices which,
will be indicated by [`struct drm_pvr_static_data_area`](uapi.md#c.drm_pvr_static_data_area "drm_pvr_static_data_area").size being set to zero.

Further, some heaps will not be present either. See [`struct
drm_pvr_dev_query_heap_info`](uapi.md#c.drm_pvr_dev_query_heap_info "drm_pvr_dev_query_heap_info").

When fetching this type [`struct drm_pvr_ioctl_dev_query_args`](uapi.md#c.drm_pvr_ioctl_dev_query_args "drm_pvr_ioctl_dev_query_args").type must be set
to `DRM_PVR_DEV_QUERY_STATIC_DATA_AREAS_GET`.

### CREATE_BO

struct drm_pvr_ioctl_create_bo_args
:   Arguments for `DRM_IOCTL_PVR_CREATE_BO`

**Definition**:

```
struct drm_pvr_ioctl_create_bo_args {
    __u64 size;
    __u32 handle;
    __u32 _padding_c;
    __u64 flags;
};
```

**Members**

`size`
:   [IN] Size of buffer object to create. This must be page size
    aligned.

`handle`
:   [OUT] GEM handle of the new buffer object for use in
    userspace.

`_padding_c`
:   Reserved. This field must be zeroed.

`flags`
:   [IN] Options which will affect the behaviour of this
    creation operation and future mapping operations on the created
    object. This field must be a valid combination of `DRM_PVR_BO_*`
    values, with all bits marked as reserved set to zero.

We use "device" to refer to the GPU here because of the ambiguity between CPU and GPU in some
fonts.

Device mapping options
:   DRM_PVR_BO_BYPASS_DEVICE_CACHE
    :   Specify that device accesses to this memory will bypass the
        cache. This is used for buffers that will either be regularly updated by the CPU (eg free
        lists) or will be accessed only once and therefore isn't worth caching (eg partial render
        buffers).
        By default, the device flushes its memory caches after every job, so this is not normally
        required for coherency.

    DRM_PVR_BO_PM_FW_PROTECT
    :   Specify that only the Parameter Manager (PM) and/or firmware
        processor should be allowed to access this memory when mapped to the device. It is not
        valid to specify this flag with DRM_PVR_BO_ALLOW_CPU_USERSPACE_ACCESS.

CPU mapping options
:   DRM_PVR_BO_ALLOW_CPU_USERSPACE_ACCESS
    :   Allow userspace to map and access the contents of this
        memory. It is not valid to specify this flag with DRM_PVR_BO_PM_FW_PROTECT.

### GET_BO_MMAP_OFFSET

struct drm_pvr_ioctl_get_bo_mmap_offset_args
:   Arguments for `DRM_IOCTL_PVR_GET_BO_MMAP_OFFSET`

**Definition**:

```
struct drm_pvr_ioctl_get_bo_mmap_offset_args {
    __u32 handle;
    __u32 _padding_4;
    __u64 offset;
};
```

**Members**

`handle`
:   [IN] GEM handle of the buffer object to be mapped.

`_padding_4`
:   Reserved. This field must be zeroed.

`offset`
:   [OUT] Fake offset to use in the real mmap call.

**Description**

Like other DRM drivers, the "mmap" IOCTL doesn't actually map any memory.
Instead, it allocates a fake offset which refers to the specified buffer
object. This offset can be used with a real mmap call on the DRM device
itself.

### CREATE_VM_CONTEXT and DESTROY_VM_CONTEXT

struct drm_pvr_ioctl_create_vm_context_args
:   Arguments for `DRM_IOCTL_PVR_CREATE_VM_CONTEXT`

**Definition**:

```
struct drm_pvr_ioctl_create_vm_context_args {
    __u32 handle;
    __u32 _padding_4;
};
```

**Members**

`handle`
:   [OUT] Handle for new VM context.

`_padding_4`
:   Reserved. This field must be zeroed.

struct drm_pvr_ioctl_destroy_vm_context_args
:   Arguments for `DRM_IOCTL_PVR_DESTROY_VM_CONTEXT`

**Definition**:

```
struct drm_pvr_ioctl_destroy_vm_context_args {
    __u32 handle;
    __u32 _padding_4;
};
```

**Members**

`handle`
:   [IN] Handle for VM context to be destroyed.

`_padding_4`
:   Reserved. This field must be zeroed.

### VM_MAP and VM_UNMAP

The VM UAPI allows userspace to create buffer object mappings in GPU virtual address space.

The client is responsible for managing GPU address space. It should allocate mappings within
the heaps returned by `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

`DRM_IOCTL_PVR_VM_MAP` creates a new mapping. The client provides the target virtual address for
the mapping. Size and offset within the mapped buffer object can be specified, so the client can
partially map a buffer.

`DRM_IOCTL_PVR_VM_UNMAP` removes a mapping. The entire mapping will be removed from GPU address
space only if the size of the mapping matches that known to the driver.

struct drm_pvr_ioctl_vm_map_args
:   Arguments for `DRM_IOCTL_PVR_VM_MAP`.

**Definition**:

```
struct drm_pvr_ioctl_vm_map_args {
    __u32 vm_context_handle;
    __u32 flags;
    __u64 device_addr;
    __u32 handle;
    __u32 _padding_14;
    __u64 offset;
    __u64 size;
};
```

**Members**

`vm_context_handle`
:   [IN] Handle for VM context for this mapping to
    exist in.

`flags`
:   [IN] Flags which affect this mapping. Currently always 0.

`device_addr`
:   [IN] Requested device-virtual address for the mapping.
    This must be non-zero and aligned to the device page size for the
    heap containing the requested address. It is an error to specify an
    address which is not contained within one of the heaps returned by
    `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`.

`handle`
:   [IN] Handle of the target buffer object. This must be a
    valid handle returned by `DRM_IOCTL_PVR_CREATE_BO`.

`_padding_14`
:   Reserved. This field must be zeroed.

`offset`
:   [IN] Offset into the target bo from which to begin the
    mapping.

`size`
:   [IN] Size of the requested mapping. Must be aligned to
    the device page size for the heap containing the requested address,
    as well as the host page size. When added to **device_addr**, the
    result must not overflow the heap which contains **device_addr** (i.e.
    the range specified by **device_addr** and **size** must be completely
    contained within a single heap specified by
    `DRM_PVR_DEV_QUERY_HEAP_INFO_GET`).

struct drm_pvr_ioctl_vm_unmap_args
:   Arguments for `DRM_IOCTL_PVR_VM_UNMAP`.

**Definition**:

```
struct drm_pvr_ioctl_vm_unmap_args {
    __u32 vm_context_handle;
    __u32 _padding_4;
    __u64 device_addr;
    __u64 size;
};
```

**Members**

`vm_context_handle`
:   [IN] Handle for VM context that this mapping
    exists in.

`_padding_4`
:   Reserved. This field must be zeroed.

`device_addr`
:   [IN] Device-virtual address at the start of the target
    mapping. This must be non-zero.

`size`
:   Size in bytes of the target mapping. This must be non-zero.

### CREATE_CONTEXT and DESTROY_CONTEXT

struct drm_pvr_ioctl_create_context_args
:   Arguments for `DRM_IOCTL_PVR_CREATE_CONTEXT`

**Definition**:

```
struct drm_pvr_ioctl_create_context_args {
    __u32 type;
    __u32 flags;
    __s32 priority;
    __u32 handle;
    __u64 static_context_state;
    __u32 static_context_state_len;
    __u32 vm_context_handle;
    __u64 callstack_addr;
};
```

**Members**

`type`
:   [IN] Type of context to create.

    This must be one of the values defined by [`enum drm_pvr_ctx_type`](uapi.md#c.drm_pvr_ctx_type "drm_pvr_ctx_type").

`flags`
:   [IN] Flags for context.

`priority`
:   [IN] Priority of new context.

    This must be one of the values defined by [`enum drm_pvr_ctx_priority`](uapi.md#c.drm_pvr_ctx_priority "drm_pvr_ctx_priority").

`handle`
:   [OUT] Handle for new context.

`static_context_state`
:   [IN] Pointer to static context state stream.

`static_context_state_len`
:   [IN] Length of static context state, in bytes.

`vm_context_handle`
:   [IN] Handle for VM context that this context is
    associated with.

`callstack_addr`
:   [IN] Address for initial call stack pointer. Only valid
    if **type** is `DRM_PVR_CTX_TYPE_RENDER`, otherwise must be 0.

enum drm_pvr_ctx_priority
:   Arguments for [`drm_pvr_ioctl_create_context_args.priority`](uapi.md#c.drm_pvr_ioctl_create_context_args "drm_pvr_ioctl_create_context_args")

**Constants**

`DRM_PVR_CTX_PRIORITY_LOW`
:   Priority below normal.

`DRM_PVR_CTX_PRIORITY_NORMAL`
:   Normal priority.

`DRM_PVR_CTX_PRIORITY_HIGH`
:   Priority above normal.
    Note this requires `CAP_SYS_NICE` or `DRM_MASTER`.

enum drm_pvr_ctx_type
:   Arguments for [`struct drm_pvr_ioctl_create_context_args`](uapi.md#c.drm_pvr_ioctl_create_context_args "drm_pvr_ioctl_create_context_args").type

**Constants**

`DRM_PVR_CTX_TYPE_RENDER`
:   Render context.

`DRM_PVR_CTX_TYPE_COMPUTE`
:   Compute context.

`DRM_PVR_CTX_TYPE_TRANSFER_FRAG`
:   Transfer context for fragment data
    master.

struct drm_pvr_ioctl_destroy_context_args
:   Arguments for `DRM_IOCTL_PVR_DESTROY_CONTEXT`

**Definition**:

```
struct drm_pvr_ioctl_destroy_context_args {
    __u32 handle;
    __u32 _padding_4;
};
```

**Members**

`handle`
:   [IN] Handle for context to be destroyed.

`_padding_4`
:   Reserved. This field must be zeroed.

### CREATE_FREE_LIST and DESTROY_FREE_LIST

struct drm_pvr_ioctl_create_free_list_args
:   Arguments for `DRM_IOCTL_PVR_CREATE_FREE_LIST`

**Definition**:

```
struct drm_pvr_ioctl_create_free_list_args {
    __u64 free_list_gpu_addr;
    __u32 initial_num_pages;
    __u32 max_num_pages;
    __u32 grow_num_pages;
    __u32 grow_threshold;
    __u32 vm_context_handle;
    __u32 handle;
};
```

**Members**

`free_list_gpu_addr`
:   [IN] Address of GPU mapping of buffer object
    containing memory to be used by free list.

    The mapped region of the buffer object must be at least
    **max_num_pages** \* `sizeof(__u32)`.

    The buffer object must have been created with
    `DRM_PVR_BO_DEVICE_PM_FW_PROTECT` set and
    `DRM_PVR_BO_CPU_ALLOW_USERSPACE_ACCESS` not set.

`initial_num_pages`
:   [IN] Pages initially allocated to free list.

`max_num_pages`
:   [IN] Maximum number of pages in free list.

`grow_num_pages`
:   [IN] Pages to grow free list by per request.

`grow_threshold`
:   [IN] Percentage of FL memory used that should
    trigger a new grow request.

`vm_context_handle`
:   [IN] Handle for VM context that the free list buffer
    object is mapped in.

`handle`
:   [OUT] Handle for created free list.

**Description**

Free list arguments have the following constraints :

- **max_num_pages** must be greater than zero.
- **grow_threshold** must be between 0 and 100.
- **grow_num_pages** must be less than or equal to `max_num_pages`.
- **initial_num_pages**, **max_num_pages** and **grow_num_pages** must be multiples
  of 4.
- When `grow_num_pages` is 0, **initial_num_pages** must be equal to
  **max_num_pages**.
- When `grow_num_pages` is non-zero, **initial_num_pages** must be less than
  **max_num_pages**.

struct drm_pvr_ioctl_destroy_free_list_args
:   Arguments for `DRM_IOCTL_PVR_DESTROY_FREE_LIST`

**Definition**:

```
struct drm_pvr_ioctl_destroy_free_list_args {
    __u32 handle;
    __u32 _padding_4;
};
```

**Members**

`handle`
:   [IN] Handle for free list to be destroyed.

`_padding_4`
:   Reserved. This field must be zeroed.

### CREATE_HWRT_DATASET and DESTROY_HWRT_DATASET

struct drm_pvr_ioctl_create_hwrt_dataset_args
:   Arguments for `DRM_IOCTL_PVR_CREATE_HWRT_DATASET`

**Definition**:

```
struct drm_pvr_ioctl_create_hwrt_dataset_args {
    struct drm_pvr_create_hwrt_geom_data_args geom_data_args;
    struct drm_pvr_create_hwrt_rt_data_args rt_data_args[2];
    __u32 free_list_handles[2];
    __u32 width;
    __u32 height;
    __u32 samples;
    __u32 layers;
    __u32 isp_merge_lower_x;
    __u32 isp_merge_lower_y;
    __u32 isp_merge_scale_x;
    __u32 isp_merge_scale_y;
    __u32 isp_merge_upper_x;
    __u32 isp_merge_upper_y;
    __u32 region_header_size;
    __u32 handle;
};
```

**Members**

`geom_data_args`
:   [IN] Geometry data arguments.

`rt_data_args`
:   [IN] Array of render target arguments.

    Each entry in this array represents a render target in a double buffered
    setup.

`free_list_handles`
:   [IN] Array of free list handles.

    free_list_handles[PVR_DRM_HWRT_FREE_LIST_LOCAL] must have initial
    size of at least that reported by
    [`drm_pvr_dev_query_runtime_info.free_list_min_pages`](uapi.md#c.drm_pvr_dev_query_runtime_info "drm_pvr_dev_query_runtime_info").

`width`
:   [IN] Width in pixels.

`height`
:   [IN] Height in pixels.

`samples`
:   [IN] Number of samples.

`layers`
:   [IN] Number of layers.

`isp_merge_lower_x`
:   [IN] Lower X coefficient for triangle merging.

`isp_merge_lower_y`
:   [IN] Lower Y coefficient for triangle merging.

`isp_merge_scale_x`
:   [IN] Scale X coefficient for triangle merging.

`isp_merge_scale_y`
:   [IN] Scale Y coefficient for triangle merging.

`isp_merge_upper_x`
:   [IN] Upper X coefficient for triangle merging.

`isp_merge_upper_y`
:   [IN] Upper Y coefficient for triangle merging.

`region_header_size`
:   [IN] Size of region header array. This common field is used by
    both render targets in this data set.

    The units for this field differ depending on what version of the simple internal
    parameter format the device uses. If format 2 is in use then this is interpreted as the
    number of region headers. For other formats it is interpreted as the size in dwords.

`handle`
:   [OUT] Handle for created HWRT dataset.

struct drm_pvr_create_hwrt_geom_data_args
:   Geometry data arguments used for [`struct drm_pvr_ioctl_create_hwrt_dataset_args`](uapi.md#c.drm_pvr_ioctl_create_hwrt_dataset_args "drm_pvr_ioctl_create_hwrt_dataset_args").geom_data_args.

**Definition**:

```
struct drm_pvr_create_hwrt_geom_data_args {
    __u64 tpc_dev_addr;
    __u32 tpc_size;
    __u32 tpc_stride;
    __u64 vheap_table_dev_addr;
    __u64 rtc_dev_addr;
};
```

**Members**

`tpc_dev_addr`
:   [IN] Tail pointer cache GPU virtual address.

`tpc_size`
:   [IN] Size of TPC, in bytes.

`tpc_stride`
:   [IN] Stride between layers in TPC, in pages

`vheap_table_dev_addr`
:   [IN] VHEAP table GPU virtual address.

`rtc_dev_addr`
:   [IN] Render Target Cache virtual address.

struct drm_pvr_create_hwrt_rt_data_args
:   Render target arguments used for [`struct drm_pvr_ioctl_create_hwrt_dataset_args`](uapi.md#c.drm_pvr_ioctl_create_hwrt_dataset_args "drm_pvr_ioctl_create_hwrt_dataset_args").rt_data_args.

**Definition**:

```
struct drm_pvr_create_hwrt_rt_data_args {
    __u64 pm_mlist_dev_addr;
    __u64 macrotile_array_dev_addr;
    __u64 region_header_dev_addr;
};
```

**Members**

`pm_mlist_dev_addr`
:   [IN] PM MLIST GPU virtual address.

`macrotile_array_dev_addr`
:   [IN] Macrotile array GPU virtual address.

`region_header_dev_addr`
:   [IN] Region header array GPU virtual address.

struct drm_pvr_ioctl_destroy_hwrt_dataset_args
:   Arguments for `DRM_IOCTL_PVR_DESTROY_HWRT_DATASET`

**Definition**:

```
struct drm_pvr_ioctl_destroy_hwrt_dataset_args {
    __u32 handle;
    __u32 _padding_4;
};
```

**Members**

`handle`
:   [IN] Handle for HWRT dataset to be destroyed.

`_padding_4`
:   Reserved. This field must be zeroed.

### SUBMIT_JOBS

DRM_PVR_SYNC_OP_HANDLE_TYPE_MASK
:   Handle type mask for the drm_pvr_sync_op::flags field.

DRM_PVR_SYNC_OP_FLAG_HANDLE_TYPE_SYNCOBJ
:   Indicates the handle passed in drm_pvr_sync_op::handle is a syncobj handle.
    This is the default type.

DRM_PVR_SYNC_OP_FLAG_HANDLE_TYPE_TIMELINE_SYNCOBJ
:   Indicates the handle passed in drm_pvr_sync_op::handle is a timeline syncobj handle.

DRM_PVR_SYNC_OP_FLAG_SIGNAL
:   Signal operation requested. The out-fence bound to the job will be attached to
    the syncobj whose handle is passed in drm_pvr_sync_op::handle.

DRM_PVR_SYNC_OP_FLAG_WAIT
:   Wait operation requested. The job will wait for this particular syncobj or syncobj
    point to be signaled before being started.
    This is the default operation.

struct drm_pvr_ioctl_submit_jobs_args
:   Arguments for `DRM_IOCTL_PVR_SUBMIT_JOB`

**Definition**:

```
struct drm_pvr_ioctl_submit_jobs_args {
    struct drm_pvr_obj_array jobs;
};
```

**Members**

`jobs`
:   [IN] Array of jobs to submit.

**Description**

If the syscall returns an error it is important to check the value of
**jobs.count**. This indicates the index into **jobs.array** where the
error occurred.

DRM_PVR_SUBMIT_JOB_GEOM_CMD_FIRST
:   Indicates if this the first command to be issued for a render.

DRM_PVR_SUBMIT_JOB_GEOM_CMD_LAST
:   Indicates if this the last command to be issued for a render.

DRM_PVR_SUBMIT_JOB_GEOM_CMD_SINGLE_CORE
:   Forces to use single core in a multi core device.

DRM_PVR_SUBMIT_JOB_GEOM_CMD_FLAGS_MASK
:   Logical OR of all the geometry cmd flags.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_SINGLE_CORE
:   Use single core in a multi core setup.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_DEPTHBUFFER
:   Indicates whether a depth buffer is present.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_STENCILBUFFER
:   Indicates whether a stencil buffer is present.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_PREVENT_CDM_OVERLAP
:   Disallow compute overlapped with this render.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_GET_VIS_RESULTS
:   Indicates whether this render produces visibility results.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_SCRATCHBUFFER
:   Indicates whether partial renders write to a scratch buffer instead of
    the final surface. It also forces the full screen copy expected to be
    present on the last render after all partial renders have completed.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_DISABLE_PIXELMERGE
:   Disable pixel merging for this render.

DRM_PVR_SUBMIT_JOB_FRAG_CMD_FLAGS_MASK
:   Logical OR of all the fragment cmd flags.

DRM_PVR_SUBMIT_JOB_COMPUTE_CMD_PREVENT_ALL_OVERLAP
:   Disallow other jobs overlapped with this compute.

DRM_PVR_SUBMIT_JOB_COMPUTE_CMD_SINGLE_CORE
:   Forces to use single core in a multi core device.

DRM_PVR_SUBMIT_JOB_COMPUTE_CMD_FLAGS_MASK
:   Logical OR of all the compute cmd flags.

DRM_PVR_SUBMIT_JOB_TRANSFER_CMD_SINGLE_CORE
:   Forces job to use a single core in a multi core device.

DRM_PVR_SUBMIT_JOB_TRANSFER_CMD_FLAGS_MASK
:   Logical OR of all the transfer cmd flags.

struct drm_pvr_sync_op
:   Object describing a sync operation

**Definition**:

```
struct drm_pvr_sync_op {
    __u32 handle;
    __u32 flags;
    __u64 value;
};
```

**Members**

`handle`
:   Handle of sync object.

`flags`
:   Combination of `DRM_PVR_SYNC_OP_FLAG_` flags.

`value`
:   Timeline value for this drm_syncobj. MBZ for a binary syncobj.

enum drm_pvr_job_type
:   Arguments for [`struct drm_pvr_job`](uapi.md#c.drm_pvr_job "drm_pvr_job").job_type

**Constants**

`DRM_PVR_JOB_TYPE_GEOMETRY`
:   Job type is geometry.

`DRM_PVR_JOB_TYPE_FRAGMENT`
:   Job type is fragment.

`DRM_PVR_JOB_TYPE_COMPUTE`
:   Job type is compute.

`DRM_PVR_JOB_TYPE_TRANSFER_FRAG`
:   Job type is a fragment transfer.

struct drm_pvr_hwrt_data_ref
:   Reference HWRT data

**Definition**:

```
struct drm_pvr_hwrt_data_ref {
    __u32 set_handle;
    __u32 data_index;
};
```

**Members**

`set_handle`
:   HWRT data set handle.

`data_index`
:   Index of the HWRT data inside the data set.

struct drm_pvr_job
:   Job arguments passed to the `DRM_IOCTL_PVR_SUBMIT_JOBS` ioctl

**Definition**:

```
struct drm_pvr_job {
    __u32 type;
    __u32 context_handle;
    __u32 flags;
    __u32 cmd_stream_len;
    __u64 cmd_stream;
    struct drm_pvr_obj_array sync_ops;
    struct drm_pvr_hwrt_data_ref hwrt;
};
```

**Members**

`type`
:   [IN] Type of job being submitted

    This must be one of the values defined by [`enum drm_pvr_job_type`](uapi.md#c.drm_pvr_job_type "drm_pvr_job_type").

`context_handle`
:   [IN] Context handle.

    When **job_type** is `DRM_PVR_JOB_TYPE_RENDER`, `DRM_PVR_JOB_TYPE_COMPUTE` or
    `DRM_PVR_JOB_TYPE_TRANSFER_FRAG`, this must be a valid handle returned by
    `DRM_IOCTL_PVR_CREATE_CONTEXT`. The type of context must be compatible
    with the type of job being submitted.

    When **job_type** is `DRM_PVR_JOB_TYPE_NULL`, this must be zero.

`flags`
:   [IN] Flags for command.

    Those are job-dependent. See all `DRM_PVR_SUBMIT_JOB_*`.

`cmd_stream_len`
:   [IN] Length of command stream, in bytes.

`cmd_stream`
:   [IN] Pointer to command stream for command.

    The command stream must be u64-aligned.

`sync_ops`
:   [IN] Fragment sync operations.

`hwrt`
:   [IN] HWRT data used by render jobs (geometry or fragment).

    Must be zero for non-render jobs.

## Internal notes

To validate the constraints imposed on IOCTL argument structs, a collection
of macros and helper functions exist in `pvr_device.h`.

Of the current helpers, it should only be necessary to call
[`PVR_IOCTL_UNION_PADDING_CHECK()`](uapi.md#c.PVR_IOCTL_UNION_PADDING_CHECK "PVR_IOCTL_UNION_PADDING_CHECK") directly. This macro should be used once in
every code path which extracts a union member from a struct passed from
userspace.

bool pvr_ioctl_union_padding_check(void \*instance, size_t union_offset, size_t union_size, size_t member_size)
:   Validate that the implicit padding between the end of a union member and the end of the union itself is zeroed.

**Parameters**

`void *instance`
:   Pointer to the instance of the struct to validate.

`size_t union_offset`
:   Offset into the type of **instance** of the target union. Must
    be 64-bit aligned.

`size_t union_size`
:   Size of the target union in the type of **instance**. Must be
    64-bit aligned.

`size_t member_size`
:   Size of the target member in the target union specified by
    **union_offset** and **union_size**. It is assumed that the offset of the target
    member is zero relative to **union_offset**. Must be 64-bit aligned.

**Description**

You probably want to use [`PVR_IOCTL_UNION_PADDING_CHECK()`](uapi.md#c.PVR_IOCTL_UNION_PADDING_CHECK "PVR_IOCTL_UNION_PADDING_CHECK") instead of calling
this function directly, since that macro abstracts away much of the setup,
and also provides some static validation. See its docs for details.

**Return**

> - `true` if every byte between the end of the used member of the union and
>   the end of that union is zeroed, or
> - `false` otherwise.

PVR_STATIC_ASSERT_64BIT_ALIGNED

`PVR_STATIC_ASSERT_64BIT_ALIGNED (static_expr_)`

> Inline assertion for 64-bit alignment.

**Parameters**

`static_expr_`
:   Target expression to evaluate.

**Description**

If **static_expr_** does not evaluate to a constant integer which would be a
64-bit aligned address (i.e. a multiple of 8), compilation will fail.

**Return**

The value of **static_expr_**.

PVR_IOCTL_UNION_PADDING_CHECK

`PVR_IOCTL_UNION_PADDING_CHECK (struct_instance_, union_, member_)`

> Validate that the implicit padding between the end of a union member and the end of the union itself is zeroed.

**Parameters**

`struct_instance_`
:   An expression which evaluates to a pointer to a UAPI data
    struct.

`union_`
:   The name of the union member of **struct_instance_** to check. If the
    union member is nested within the type of **struct_instance_**, this may
    contain the member access operator (".").

`member_`
:   The name of the member of **union_** to assess.

**Description**

This is a wrapper around [`pvr_ioctl_union_padding_check()`](uapi.md#c.pvr_ioctl_union_padding_check "pvr_ioctl_union_padding_check") which performs
alignment checks and simplifies things for the caller.

**Return**

> - `true` if every byte in **struct_instance_** between the end of **member_** and
>   the end of **union_** is zeroed, or
> - `false` otherwise.
