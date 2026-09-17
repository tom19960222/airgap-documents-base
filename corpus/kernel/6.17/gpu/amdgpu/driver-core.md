---
collection: kernel
version: "6.17"
title: "Core Driver Infrastructure"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/amdgpu/driver-core.html
fetched_at: 2026-09-16T16:27:10+00:00
---
# Core Driver Infrastructure

## GPU Hardware Structure

Each ASIC is a collection of hardware blocks. We refer to them as
“IPs” (Intellectual Property blocks). Each IP encapsulates certain
functionality. IPs are versioned and can also be mixed and matched.
E.g., you might have two different ASICs that both have System DMA (SDMA) 5.x IPs.
The driver is arranged by IPs. There are driver components to handle
the initialization and operation of each IP. There are also a bunch
of smaller IPs that don’t really need much if any driver interaction.
Those end up getting lumped into the common stuff in the soc files.
The soc files (e.g., vi.c, soc15.c nv.c) contain code for aspects of
the SoC itself rather than specific IPs. E.g., things like GPU resets
and register access functions are SoC dependent.

An APU contains more than just CPU and GPU, it also contains all of
the platform stuff (audio, usb, gpio, etc.). Also, a lot of
components are shared between the CPU, platform, and the GPU (e.g.,
SMU, PSP, etc.). Specific components (CPU, GPU, etc.) usually have
their interface to interact with those common components. For things
like S0i3 there is a ton of coordination required across all the
components, but that is probably a bit beyond the scope of this
section.

With respect to the GPU, we have the following major IPs:

GMC (Graphics Memory Controller)
:   This was a dedicated IP on older pre-vega chips, but has since
    become somewhat decentralized on vega and newer chips. They now
    have dedicated memory hubs for specific IPs or groups of IPs. We
    still treat it as a single component in the driver however since
    the programming model is still pretty similar. This is how the
    different IPs on the GPU get the memory (VRAM or system memory).
    It also provides the support for per process GPU virtual address
    spaces.

IH (Interrupt Handler)
:   This is the interrupt controller on the GPU. All of the IPs feed
    their interrupts into this IP and it aggregates them into a set of
    ring buffers that the driver can parse to handle interrupts from
    different IPs.

PSP (Platform Security Processor)
:   This handles security policy for the SoC and executes trusted
    applications, and validates and loads firmwares for other blocks.

SMU (System Management Unit)
:   This is the power management microcontroller. It manages the entire
    SoC. The driver interacts with it to control power management
    features like clocks, voltages, power rails, etc.

DCN (Display Controller Next)
:   This is the display controller. It handles the display hardware.
    It is described in more details in [Display Core](display/index.md#amdgpu-display-core).

SDMA (System DMA)
:   This is a multi-purpose DMA engine. The kernel driver uses it for
    various things including paging and GPU page table updates. It’s also
    exposed to userspace for use by user mode drivers (OpenGL, Vulkan,
    etc.)

GC (Graphics and Compute)
:   This is the graphics and compute engine, i.e., the block that
    encompasses the 3D pipeline and and shader blocks. This is by far the
    largest block on the GPU. The 3D pipeline has tons of sub-blocks. In
    addition to that, it also contains the CP microcontrollers (ME, PFP, CE,
    MEC) and the RLC microcontroller. It’s exposed to userspace for user mode
    drivers (OpenGL, Vulkan, OpenCL, etc.). More details in [Graphics (GFX)
    and Compute](gc/index.md#amdgpu-gc).

VCN (Video Core Next)
:   This is the multi-media engine. It handles video and image encode and
    decode. It’s exposed to userspace for user mode drivers (VA-API,
    OpenMAX, etc.)

## GFX, Compute, and SDMA Overall Behavior

> **Note:**
>
> For simplicity, whenever the term block is used in this section, it
> means GFX, Compute, and SDMA.

GFX, Compute and SDMA share a similar form of operation that can be abstracted
to facilitate understanding of the behavior of these blocks. See the figure
below illustrating the common components of these blocks:

![../../_images/pipe_and_queue_abstraction.svg](../../_images/pipe_and_queue_abstraction.svg)

In the central part of this figure, you can see two hardware elements, one called
**Pipes** and another called **Queues**; it is important to highlight that Queues
must be associated with a Pipe and vice-versa. Every specific hardware IP may have
a different number of Pipes and, in turn, a different number of Queues; for
example, GFX 11 has two Pipes and two Queues per Pipe for the GFX front end.

Pipe is the hardware that processes the instructions available in the Queues;
in other words, it is a thread executing the operations inserted in the Queue.
One crucial characteristic of Pipes is that they can only execute one Queue at
a time; no matter if the hardware has multiple Queues in the Pipe, it only runs
one Queue per Pipe.

Pipes have the mechanics of swapping between queues at the hardware level.
Nonetheless, they only make use of Queues that are considered mapped. Pipes can
switch between queues based on any of the following inputs:

1. Command Stream;
2. Packet by Packet;
3. Other hardware requests the change (e.g., MES).

Queues within Pipes are defined by the Hardware Queue Descriptors (HQD).
Associated with the HQD concept, we have the Memory Queue Descriptor (MQD),
which is responsible for storing information about the state of each of the
available Queues in the memory. The state of a Queue contains information such
as the GPU virtual address of the queue itself, save areas, doorbell, etc. The
MQD also stores the HQD registers, which are vital for activating or
deactivating a given Queue. The scheduling firmware (e.g., MES) is responsible
for loading HQDs from MQDs and vice versa.

The Queue-switching process can also happen with the firmware requesting the
preemption or unmapping of a Queue. The firmware waits for the HQD_ACTIVE bit
to change to low before saving the state into the MQD. To make a different
Queue become active, the firmware copies the MQD state into the HQD registers
and loads any additional state. Finally, it sets the HQD_ACTIVE bit to high to
indicate that the queue is active. The Pipe will then execute work from active
Queues.

## Driver Structure

In general, the driver has a list of all of the IPs on a particular
SoC and for things like init/fini/suspend/resume, more or less just
walks the list and handles each IP.

Some useful constructs:

KIQ (Kernel Interface Queue)
:   This is a control queue used by the kernel driver to manage other gfx
    and compute queues on the GFX/compute engine. You can use it to
    map/unmap additional queues, etc. This is replaced by MES on
    GFX 11 and newer hardware.

IB (Indirect Buffer)
:   A command buffer for a particular engine. Rather than writing
    commands directly to the queue, you can write the commands into a
    piece of memory and then put a pointer to the memory into the queue.
    The hardware will then follow the pointer and execute the commands in
    the memory, then returning to the rest of the commands in the ring.

## Memory Domains

`AMDGPU_GEM_DOMAIN_CPU` System memory that is not GPU accessible.
Memory in this pool could be swapped out to disk if there is pressure.

`AMDGPU_GEM_DOMAIN_GTT` GPU accessible system memory, mapped into the
GPU’s virtual address space via gart. Gart memory linearizes non-contiguous
pages of system memory, allows GPU access system memory in a linearized
fashion.

`AMDGPU_GEM_DOMAIN_VRAM` Local video memory. For APUs, it is memory
carved out by the BIOS.

`AMDGPU_GEM_DOMAIN_GDS` Global on-chip data storage used to share data
across shader threads.

`AMDGPU_GEM_DOMAIN_GWS` Global wave sync, used to synchronize the
execution of all the waves on a device.

`AMDGPU_GEM_DOMAIN_OA` Ordered append, used by 3D or Compute engines
for appending data.

`AMDGPU_GEM_DOMAIN_DOORBELL` Doorbell. It is an MMIO region for
signalling user mode queues.

## Buffer Objects

This defines the interfaces to operate on an `amdgpu_bo` buffer object which
represents memory used by driver (VRAM, system memory, etc.). The driver
provides DRM/GEM APIs to userspace. DRM/GEM APIs then use these interfaces
to create/destroy/set buffer object which are then managed by the kernel TTM
memory manager.
The interfaces are also used internally by kernel clients, including gfx,
uvd, etc. for kernel managed allocations used by the GPU.

bool amdgpu_bo_is_amdgpu_bo(struct ttm_buffer_object \*bo)
:   check if the buffer object is an `amdgpu_bo`

**Parameters**

`struct ttm_buffer_object *bo`
:   buffer object to be checked

**Description**

Uses destroy function associated with the object to determine if this is
an `amdgpu_bo`.

**Return**

true if the object belongs to `amdgpu_bo`, false if not.

void amdgpu_bo_placement_from_domain(struct amdgpu_bo \*abo, u32 domain)
:   set buffer’s placement

**Parameters**

`struct amdgpu_bo *abo`
:   `amdgpu_bo` buffer object whose placement is to be set

`u32 domain`
:   requested domain

**Description**

Sets buffer’s placement according to requested domain and the buffer’s
flags.

int amdgpu_bo_create_reserved(struct amdgpu_device \*adev, unsigned long size, int align, u32 domain, struct amdgpu_bo \*\*bo_ptr, u64 \*gpu_addr, void \*\*cpu_addr)
:   create reserved BO for kernel use

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`unsigned long size`
:   size for the new BO

`int align`
:   alignment for the new BO

`u32 domain`
:   where to place it

`struct amdgpu_bo **bo_ptr`
:   used to initialize BOs in structures

`u64 *gpu_addr`
:   GPU addr of the pinned BO

`void **cpu_addr`
:   optional CPU address mapping

**Description**

Allocates and pins a BO for kernel internal use, and returns it still
reserved.

**Note**

For bo_ptr new BO is only created if bo_ptr points to NULL.

**Return**

0 on success, negative error code otherwise.

int amdgpu_bo_create_kernel(struct amdgpu_device \*adev, unsigned long size, int align, u32 domain, struct amdgpu_bo \*\*bo_ptr, u64 \*gpu_addr, void \*\*cpu_addr)
:   create BO for kernel use

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`unsigned long size`
:   size for the new BO

`int align`
:   alignment for the new BO

`u32 domain`
:   where to place it

`struct amdgpu_bo **bo_ptr`
:   used to initialize BOs in structures

`u64 *gpu_addr`
:   GPU addr of the pinned BO

`void **cpu_addr`
:   optional CPU address mapping

**Description**

Allocates and pins a BO for kernel internal use.

This function is exported to allow the V4L2 isp device
external to drm device to create and access the kernel BO.

**Note**

For bo_ptr new BO is only created if bo_ptr points to NULL.

**Return**

0 on success, negative error code otherwise.

int amdgpu_bo_create_isp_user(struct amdgpu_device \*adev, struct [dma_buf](driver-core.md#c.amdgpu_bo_create_isp_user "dma_buf") \*dma_buf, u32 domain, struct amdgpu_bo \*\*bo, u64 \*gpu_addr)
:   create user BO for isp

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`struct dma_buf *dma_buf`
:   DMABUF handle for isp buffer

`u32 domain`
:   where to place it

`struct amdgpu_bo **bo`
:   used to initialize BOs in structures

`u64 *gpu_addr`
:   GPU addr of the pinned BO

**Description**

Imports isp DMABUF to allocate and pin a user BO for isp internal use. It does
GART alloc to generate gpu_addr for BO to make it accessible through the
GART aperture for ISP HW.

This function is exported to allow the V4L2 isp device external to drm device
to create and access the isp user BO.

**Return**

0 on success, negative error code otherwise.

int amdgpu_bo_create_kernel_at(struct amdgpu_device \*adev, uint64_t offset, uint64_t size, struct amdgpu_bo \*\*bo_ptr, void \*\*cpu_addr)
:   create BO for kernel use at specific location

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`uint64_t offset`
:   offset of the BO

`uint64_t size`
:   size of the BO

`struct amdgpu_bo **bo_ptr`
:   used to initialize BOs in structures

`void **cpu_addr`
:   optional CPU address mapping

**Description**

Creates a kernel BO at a specific offset in VRAM.

**Return**

0 on success, negative error code otherwise.

void amdgpu_bo_free_kernel(struct amdgpu_bo \*\*bo, u64 \*gpu_addr, void \*\*cpu_addr)
:   free BO for kernel use

**Parameters**

`struct amdgpu_bo **bo`
:   amdgpu BO to free

`u64 *gpu_addr`
:   pointer to where the BO’s GPU memory space address was stored

`void **cpu_addr`
:   pointer to where the BO’s CPU memory space address was stored

**Description**

unmaps and unpin a BO for kernel internal use.

This function is exported to allow the V4L2 isp device
external to drm device to free the kernel BO.

void amdgpu_bo_free_isp_user(struct amdgpu_bo \*bo)
:   free BO for isp use

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu isp user BO to free

**Description**

unpin and unref BO for isp internal use.

This function is exported to allow the V4L2 isp device
external to drm device to free the isp user BO.

int amdgpu_bo_create(struct amdgpu_device \*adev, struct amdgpu_bo_param \*bp, struct amdgpu_bo \*\*bo_ptr)
:   create an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`struct amdgpu_bo_param *bp`
:   parameters to be used for the buffer object

`struct amdgpu_bo **bo_ptr`
:   pointer to the buffer object pointer

**Description**

Creates an `amdgpu_bo` buffer object.

**Return**

0 for success or a negative error code on failure.

int amdgpu_bo_create_user(struct amdgpu_device \*adev, struct amdgpu_bo_param \*bp, struct amdgpu_bo_user \*\*ubo_ptr)
:   create an `amdgpu_bo_user` buffer object

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`struct amdgpu_bo_param *bp`
:   parameters to be used for the buffer object

`struct amdgpu_bo_user **ubo_ptr`
:   pointer to the buffer object pointer

**Description**

Create a BO to be used by user application;

**Return**

0 for success or a negative error code on failure.

int amdgpu_bo_create_vm(struct amdgpu_device \*adev, struct amdgpu_bo_param \*bp, struct amdgpu_bo_vm \*\*vmbo_ptr)
:   create an `amdgpu_bo_vm` buffer object

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`struct amdgpu_bo_param *bp`
:   parameters to be used for the buffer object

`struct amdgpu_bo_vm **vmbo_ptr`
:   pointer to the buffer object pointer

**Description**

Create a BO to be for GPUVM.

**Return**

0 for success or a negative error code on failure.

int amdgpu_bo_kmap(struct amdgpu_bo \*bo, void \*\*ptr)
:   map an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object to be mapped

`void **ptr`
:   kernel virtual address to be returned

**Description**

Calls `ttm_bo_kmap()` to set up the kernel virtual mapping; calls
[`amdgpu_bo_kptr()`](driver-core.md#c.amdgpu_bo_kptr "amdgpu_bo_kptr") to get the kernel virtual address.

**Return**

0 for success or a negative error code on failure.

void \*amdgpu_bo_kptr(struct amdgpu_bo \*bo)
:   returns a kernel virtual address of the buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

**Description**

Calls `ttm_kmap_obj_virtual()` to get the kernel virtual address

**Return**

the virtual address of a buffer object area.

void amdgpu_bo_kunmap(struct amdgpu_bo \*bo)
:   unmap an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object to be unmapped

**Description**

Unmaps a kernel map set up by [`amdgpu_bo_kmap()`](driver-core.md#c.amdgpu_bo_kmap "amdgpu_bo_kmap").

struct amdgpu_bo \*amdgpu_bo_ref(struct amdgpu_bo \*bo)
:   reference an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

**Description**

References the contained `ttm_buffer_object`.

**Return**

a refcounted pointer to the `amdgpu_bo` buffer object.

void amdgpu_bo_unref(struct amdgpu_bo \*\*bo)
:   unreference an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo **bo`
:   `amdgpu_bo` buffer object

**Description**

Unreferences the contained `ttm_buffer_object` and clear the pointer

int amdgpu_bo_pin(struct amdgpu_bo \*bo, u32 domain)
:   pin an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object to be pinned

`u32 domain`
:   domain to be pinned to

**Description**

Pins the buffer object according to requested domain. If the memory is
unbound gart memory, binds the pages into gart table. Adjusts pin_count and
pin_size accordingly.

Pinning means to lock pages in memory along with keeping them at a fixed
offset. It is required when a buffer can not be moved, for example, when
a display buffer is being scanned out.

**Return**

0 for success or a negative error code on failure.

void amdgpu_bo_unpin(struct amdgpu_bo \*bo)
:   unpin an `amdgpu_bo` buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object to be unpinned

**Description**

Decreases the pin_count, and clears the flags if pin_count reaches 0.
Changes placement and pin size accordingly.

**Return**

0 for success or a negative error code on failure.

int amdgpu_bo_init(struct amdgpu_device \*adev)
:   initialize memory manager

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

**Description**

Calls `amdgpu_ttm_init()` to initialize amdgpu memory manager.

**Return**

0 for success or a negative error code on failure.

void amdgpu_bo_fini(struct amdgpu_device \*adev)
:   tear down memory manager

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

**Description**

Reverses [`amdgpu_bo_init()`](driver-core.md#c.amdgpu_bo_init "amdgpu_bo_init") to tear down memory manager.

int amdgpu_bo_set_tiling_flags(struct amdgpu_bo \*bo, u64 tiling_flags)
:   set tiling flags

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

`u64 tiling_flags`
:   new flags

**Description**

Sets buffer object’s tiling flags with the new one. Used by GEM ioctl or
kernel driver to set the tiling flags on a buffer.

**Return**

0 for success or a negative error code on failure.

void amdgpu_bo_get_tiling_flags(struct amdgpu_bo \*bo, u64 \*tiling_flags)
:   get tiling flags

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

`u64 *tiling_flags`
:   returned flags

**Description**

Gets buffer object’s tiling flags. Used by GEM ioctl or kernel driver to
set the tiling flags on a buffer.

int amdgpu_bo_set_metadata(struct amdgpu_bo \*bo, void \*metadata, u32 metadata_size, uint64_t flags)
:   set metadata

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

`void *metadata`
:   new metadata

`u32 metadata_size`
:   size of the new metadata

`uint64_t flags`
:   flags of the new metadata

**Description**

Sets buffer object’s metadata, its size and flags.
Used via GEM ioctl.

**Return**

0 for success or a negative error code on failure.

int amdgpu_bo_get_metadata(struct amdgpu_bo \*bo, void \*buffer, size_t buffer_size, uint32_t \*metadata_size, uint64_t \*flags)
:   get metadata

**Parameters**

`struct amdgpu_bo *bo`
:   `amdgpu_bo` buffer object

`void *buffer`
:   returned metadata

`size_t buffer_size`
:   size of the buffer

`uint32_t *metadata_size`
:   size of the returned metadata

`uint64_t *flags`
:   flags of the returned metadata

**Description**

Gets buffer object’s metadata, its size and flags. buffer_size shall not be
less than metadata_size.
Used via GEM ioctl.

**Return**

0 for success or a negative error code on failure.

void amdgpu_bo_move_notify(struct ttm_buffer_object \*bo, bool evict, struct [ttm_resource](../drm-mm.md#c.ttm_resource "ttm_resource") \*new_mem)
:   notification about a memory move

**Parameters**

`struct ttm_buffer_object *bo`
:   pointer to a buffer object

`bool evict`
:   if this move is evicting the buffer from the graphics address space

`struct ttm_resource *new_mem`
:   new resource for backing the BO

**Description**

Marks the corresponding `amdgpu_bo` buffer object as invalid, also performs
bookkeeping.
TTM driver callback which is called when ttm moves a buffer.

void amdgpu_bo_release_notify(struct ttm_buffer_object \*bo)
:   notification about a BO being released

**Parameters**

`struct ttm_buffer_object *bo`
:   pointer to a buffer object

**Description**

Wipes VRAM buffers whose contents should not be leaked before the
memory is released.

[vm_fault_t](../../core-api/mm-api.md#c.vm_fault_t "vm_fault_t") amdgpu_bo_fault_reserve_notify(struct ttm_buffer_object \*bo)
:   notification about a memory fault

**Parameters**

`struct ttm_buffer_object *bo`
:   pointer to a buffer object

**Description**

Notifies the driver we are taking a fault on this BO and have reserved it,
also performs bookkeeping.
TTM driver callback for dealing with vm faults.

**Return**

0 for success or a negative error code on failure.

void amdgpu_bo_fence(struct amdgpu_bo \*bo, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*fence, bool shared)
:   add fence to buffer object

**Parameters**

`struct amdgpu_bo *bo`
:   buffer object in question

`struct dma_fence *fence`
:   fence to add

`bool shared`
:   true if fence should be added shared

int amdgpu_bo_sync_wait_resv(struct amdgpu_device \*adev, struct [dma_resv](../../driver-api/dma-buf.md#c.dma_resv "dma_resv") \*resv, enum amdgpu_sync_mode sync_mode, void \*owner, bool intr)
:   Wait for BO reservation fences

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct dma_resv *resv`
:   reservation object to sync to

`enum amdgpu_sync_mode sync_mode`
:   synchronization mode

`void *owner`
:   fence owner

`bool intr`
:   Whether the wait is interruptible

**Description**

Extract the fences from the reservation object and waits for them to finish.

**Return**

0 on success, errno otherwise.

int amdgpu_bo_sync_wait(struct amdgpu_bo \*bo, void \*owner, bool intr)
:   Wrapper for amdgpu_bo_sync_wait_resv

**Parameters**

`struct amdgpu_bo *bo`
:   buffer object to wait for

`void *owner`
:   fence owner

`bool intr`
:   Whether the wait is interruptible

**Description**

Wrapper to wait for fences in a BO.

**Return**

0 on success, errno otherwise.

u64 amdgpu_bo_gpu_offset(struct amdgpu_bo \*bo)
:   return GPU offset of bo

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu object for which we query the offset

**Note**

object should either be pinned or reserved when calling this
function, it might be useful to add check for this for debugging.

**Return**

current GPU offset of the object.

u64 amdgpu_bo_fb_aper_addr(struct amdgpu_bo \*bo)
:   return FB aperture GPU offset of the VRAM bo

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu VRAM buffer object for which we query the offset

**Return**

current FB aperture GPU offset of the object.

u64 amdgpu_bo_gpu_offset_no_check(struct amdgpu_bo \*bo)
:   return GPU offset of bo

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu object for which we query the offset

**Return**

current GPU offset of the object without raising warnings.

uint32_t amdgpu_bo_mem_stats_placement(struct amdgpu_bo \*bo)
:   bo placement for memory accounting

**Parameters**

`struct amdgpu_bo *bo`
:   the buffer object we should look at

**Description**

BO can have multiple preferred placements, to avoid double counting we want
to file it under a single placement for memory stats.
Luckily, if we take the highest set bit in preferred_domains the result is
quite sensible.

**Return**

Which of the placements should the BO be accounted under.

uint32_t amdgpu_bo_get_preferred_domain(struct amdgpu_device \*adev, uint32_t domain)
:   get preferred domain

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device object

`uint32_t domain`
:   allowed [memory domains](driver-core.md#amdgpu-memory-domains)

**Return**

Which of the allowed domains is preferred for allocating the BO.

u64 amdgpu_bo_print_info(int id, struct amdgpu_bo \*bo, struct seq_file \*m)
:   print BO info in debugfs file

**Parameters**

`int id`
:   Index or Id of the BO

`struct amdgpu_bo *bo`
:   Requested BO for printing info

`struct seq_file *m`
:   debugfs file

**Description**

Print BO information in debugfs file

**Return**

Size of the BO in bytes.

## PRIME Buffer Sharing

The following callback implementations are used for [sharing GEM buffer
objects between different devices via PRIME](../drm-mm.md#prime-buffer-sharing).

struct amdgpu_device \*dma_buf_attach_adev(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach)
:   Helper to get adev of an attachment

**Parameters**

`struct dma_buf_attachment *attach`
:   attachment

**Return**

A `struct amdgpu_device` \* if the attaching device is an amdgpu device or
partition, NULL otherwise.

int amdgpu_dma_buf_attach(struct [dma_buf](../../driver-api/dma-buf.md#c.dma_buf "dma_buf") \*dmabuf, struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach)
:   [`dma_buf_ops.attach`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf *dmabuf`
:   DMA-buf where we attach to

`struct dma_buf_attachment *attach`
:   attachment to add

**Description**

Add the attachment as user to the exported DMA-buf.

int amdgpu_dma_buf_pin(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach)
:   [`dma_buf_ops.pin`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf_attachment *attach`
:   attachment to pin down

**Description**

Pin the BO which is backing the DMA-buf so that it can’t move any more.

void amdgpu_dma_buf_unpin(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach)
:   [`dma_buf_ops.unpin`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf_attachment *attach`
:   attachment to unpin

**Description**

Unpin a previously pinned BO to make it movable again.

struct sg_table \*amdgpu_dma_buf_map(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach, enum dma_data_direction dir)
:   [`dma_buf_ops.map_dma_buf`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf_attachment *attach`
:   DMA-buf attachment

`enum dma_data_direction dir`
:   DMA direction

**Description**

Makes sure that the shared DMA buffer can be accessed by the target device.
For now, simply pins it to the GTT domain, where it should be accessible by
all DMA devices.

**Return**

sg_table filled with the DMA addresses to use or ERR_PRT with negative error
code.

void amdgpu_dma_buf_unmap(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach, struct sg_table \*sgt, enum dma_data_direction dir)
:   [`dma_buf_ops.unmap_dma_buf`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf_attachment *attach`
:   DMA-buf attachment

`struct sg_table *sgt`
:   sg_table to unmap

`enum dma_data_direction dir`
:   DMA direction

**Description**

This is called when a shared DMA buffer no longer needs to be accessible by
another device. For now, simply unpins the buffer from GTT.

int amdgpu_dma_buf_begin_cpu_access(struct [dma_buf](driver-core.md#c.amdgpu_dma_buf_begin_cpu_access "dma_buf") \*dma_buf, enum dma_data_direction direction)
:   [`dma_buf_ops.begin_cpu_access`](../../driver-api/dma-buf.md#c.dma_buf_ops "dma_buf_ops") implementation

**Parameters**

`struct dma_buf *dma_buf`
:   Shared DMA buffer

`enum dma_data_direction direction`
:   Direction of DMA transfer

**Description**

This is called before CPU access to the shared DMA buffer’s memory. If it’s
a read access, the buffer is moved to the GTT domain if possible, for optimal
CPU read performance.

**Return**

0 on success or a negative error code on failure.

struct [dma_buf](../../driver-api/dma-buf.md#c.dma_buf "dma_buf") \*amdgpu_gem_prime_export(struct [drm_gem_object](../drm-mm.md#c.drm_gem_object "drm_gem_object") \*gobj, int flags)
:   [`drm_driver.gem_prime_export`](../drm-internals.md#c.drm_driver "drm_driver") implementation

**Parameters**

`struct drm_gem_object *gobj`
:   GEM BO

`int flags`
:   Flags such as DRM_CLOEXEC and DRM_RDWR.

**Description**

The main work is done by the [`drm_gem_prime_export`](../drm-mm.md#c.drm_gem_prime_export "drm_gem_prime_export") helper.

**Return**

Shared DMA buffer representing the GEM BO from the given device.

struct [drm_gem_object](../drm-mm.md#c.drm_gem_object "drm_gem_object") \*amdgpu_dma_buf_create_obj(struct [drm_device](../drm-internals.md#c.drm_device "drm_device") \*dev, struct [dma_buf](driver-core.md#c.amdgpu_dma_buf_create_obj "dma_buf") \*dma_buf)
:   create BO for DMA-buf import

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct dma_buf *dma_buf`
:   DMA-buf

**Description**

Creates an empty SG BO for DMA-buf import.

**Return**

A new GEM BO of the given DRM device, representing the memory
described by the given DMA-buf attachment and scatter/gather table.

void amdgpu_dma_buf_move_notify(struct [dma_buf_attachment](../../driver-api/dma-buf.md#c.dma_buf_attachment "dma_buf_attachment") \*attach)
:   [`attach.move_notify`](driver-core.md#c.amdgpu_dma_buf_move_notify "attach") implementation

**Parameters**

`struct dma_buf_attachment *attach`
:   the DMA-buf attachment

**Description**

Invalidate the DMA-buf attachment, making sure that the we re-create the
mapping before the next use.

struct [drm_gem_object](../drm-mm.md#c.drm_gem_object "drm_gem_object") \*amdgpu_gem_prime_import(struct [drm_device](../drm-internals.md#c.drm_device "drm_device") \*dev, struct [dma_buf](driver-core.md#c.amdgpu_gem_prime_import "dma_buf") \*dma_buf)
:   [`drm_driver.gem_prime_import`](../drm-internals.md#c.drm_driver "drm_driver") implementation

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct dma_buf *dma_buf`
:   Shared DMA buffer

**Description**

Import a dma_buf into a the driver and potentially create a new GEM object.

**Return**

GEM BO representing the shared DMA buffer for the given device.

bool amdgpu_dmabuf_is_xgmi_accessible(struct amdgpu_device \*adev, struct amdgpu_bo \*bo)
:   Check if xgmi available for P2P transfer

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer of the importer

`struct amdgpu_bo *bo`
:   amdgpu buffer object

**Return**

True if dmabuf accessible over xgmi, false otherwise.

## MMU Notifier

For coherent userptr handling registers an MMU notifier to inform the driver
about updates on the page tables of a process.

When somebody tries to invalidate the page tables we block the update until
all operations on the pages in question are completed, then those pages are
marked as accessed and also dirty if it wasn’t a read only access.

New command submissions using the userptrs in question are delayed until all
page table invalidation are completed and we once more see a coherent process
address space.

bool amdgpu_hmm_invalidate_gfx(struct mmu_interval_notifier \*mni, const struct mmu_notifier_range \*range, unsigned long cur_seq)
:   callback to notify about mm change

**Parameters**

`struct mmu_interval_notifier *mni`
:   the range (mm) is about to update

`const struct mmu_notifier_range *range`
:   details on the invalidation

`unsigned long cur_seq`
:   Value to pass to `mmu_interval_set_seq()`

**Description**

Block for operations on BOs to finish and mark pages as accessed and
potentially dirty.

bool amdgpu_hmm_invalidate_hsa(struct mmu_interval_notifier \*mni, const struct mmu_notifier_range \*range, unsigned long cur_seq)
:   callback to notify about mm change

**Parameters**

`struct mmu_interval_notifier *mni`
:   the range (mm) is about to update

`const struct mmu_notifier_range *range`
:   details on the invalidation

`unsigned long cur_seq`
:   Value to pass to `mmu_interval_set_seq()`

**Description**

We temporarily evict the BO attached to this range. This necessitates
evicting all user-mode queues of the process.

int amdgpu_hmm_register(struct amdgpu_bo \*bo, unsigned long addr)
:   register a BO for notifier updates

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu buffer object

`unsigned long addr`
:   userptr addr we should monitor

**Description**

Registers a mmu_notifier for the given BO at the specified address.
Returns 0 on success, -ERRNO if anything goes wrong.

void amdgpu_hmm_unregister(struct amdgpu_bo \*bo)
:   unregister a BO for notifier updates

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu buffer object

**Description**

Remove any registration of mmu notifier updates from the buffer object.

## AMDGPU Virtual Memory

GPUVM is the MMU functionality provided on the GPU.
GPUVM is similar to the legacy GART on older asics, however
rather than there being a single global GART table
for the entire GPU, there can be multiple GPUVM page tables active
at any given time. The GPUVM page tables can contain a mix
VRAM pages and system pages (both memory and MMIO) and system pages
can be mapped as snooped (cached system pages) or unsnooped
(uncached system pages).

Each active GPUVM has an ID associated with it and there is a page table
linked with each VMID. When executing a command buffer,
the kernel tells the engine what VMID to use for that command
buffer. VMIDs are allocated dynamically as commands are submitted.
The userspace drivers maintain their own address space and the kernel
sets up their pages tables accordingly when they submit their
command buffers and a VMID is assigned.
The hardware supports up to 16 active GPUVMs at any given time.

Each GPUVM is represented by a 1-2 or 1-5 level page table, depending
on the ASIC family. GPUVM supports RWX attributes on each page as well
as other features such as encryption and caching attributes.

VMID 0 is special. It is the GPUVM used for the kernel driver. In
addition to an aperture managed by a page table, VMID 0 also has
several other apertures. There is an aperture for direct access to VRAM
and there is a legacy AGP aperture which just forwards accesses directly
to the matching system physical addresses (or IOVAs when an IOMMU is
present). These apertures provide direct access to these memories without
incurring the overhead of a page table. VMID 0 is used by the kernel
driver for tasks like memory management.

GPU clients (i.e., engines on the GPU) use GPUVM VMIDs to access memory.
For user applications, each application can have their own unique GPUVM
address space. The application manages the address space and the kernel
driver manages the GPUVM page tables for each process. If an GPU client
accesses an invalid page, it will generate a GPU page fault, similar to
accessing an invalid page on a CPU.

struct amdgpu_prt_cb
:   Helper to disable partial resident texture feature from a fence callback

**Definition**:

```
struct amdgpu_prt_cb {
    struct amdgpu_device *adev;
    struct dma_fence_cb cb;
};
```

**Members**

`adev`
:   amdgpu device

`cb`
:   callback

struct amdgpu_vm_tlb_seq_struct
:   Helper to increment the TLB flush sequence

**Definition**:

```
struct amdgpu_vm_tlb_seq_struct {
    struct amdgpu_vm *vm;
    struct dma_fence_cb cb;
};
```

**Members**

`vm`
:   pointer to the amdgpu_vm structure to set the fence sequence on

`cb`
:   callback

int amdgpu_vm_set_pasid(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, u32 pasid)
:   manage pasid and vm ptr mapping

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   amdgpu_vm pointer

`u32 pasid`
:   the pasid the VM is using on this GPU

**Description**

Set the pasid this VM is using on this GPU, can also be used to remove the
pasid by passing in zero.

void amdgpu_vm_bo_evicted(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is evicted

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is evicted

**Description**

State for PDs/PTs and per VM BOs which are not at the location they should
be.

void amdgpu_vm_bo_moved(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is moved

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is moved

**Description**

State for per VM BOs which are moved, but that change is not yet reflected
in the page tables.

void amdgpu_vm_bo_idle(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is idle

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is now idle

**Description**

State for PDs/PTs and per VM BOs which have gone through the state machine
and are now idle.

void amdgpu_vm_bo_invalidated(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is invalidated

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is now invalidated

**Description**

State for normal BOs which are invalidated and that change not yet reflected
in the PTs.

void amdgpu_vm_bo_evicted_user(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is evicted

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is evicted

**Description**

State for BOs used by user mode queues which are not at the location they
should be.

void amdgpu_vm_bo_relocated(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is reloacted

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is relocated

**Description**

State for PDs/PTs which needs to update their parent PD.
For the root PD, just move to idle state.

void amdgpu_vm_bo_done(struct amdgpu_vm_bo_base \*vm_bo)
:   vm_bo is done

**Parameters**

`struct amdgpu_vm_bo_base *vm_bo`
:   vm_bo which is now done

**Description**

State for normal BOs which are invalidated and that change has been updated
in the PTs.

void amdgpu_vm_bo_reset_state_machine(struct amdgpu_vm \*vm)
:   reset the vm_bo state machine

**Parameters**

`struct amdgpu_vm *vm`
:   the VM which state machine to reset

**Description**

Move all vm_bo object in the VM into a state where they will be updated
again during validation.

void amdgpu_vm_update_shared(struct amdgpu_vm_bo_base \*base)
:   helper to update shared memory stat

**Parameters**

`struct amdgpu_vm_bo_base *base`
:   base structure for tracking BO usage in a VM

**Description**

Takes the vm status_lock and updates the shared memory stat. If the basic
stat changed (e.g. buffer was moved) amdgpu_vm_update_stats need to be called
as well.

void amdgpu_vm_bo_update_shared(struct amdgpu_bo \*bo)
:   callback when bo gets shared/unshared

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu buffer object

**Description**

Update the per VM stats for all the vm if needed from private to shared or
vice versa.

void amdgpu_vm_update_stats_locked(struct amdgpu_vm_bo_base \*base, struct [ttm_resource](../drm-mm.md#c.ttm_resource "ttm_resource") \*res, int sign)
:   helper to update normal memory stat

**Parameters**

`struct amdgpu_vm_bo_base *base`
:   base structure for tracking BO usage in a VM

`struct ttm_resource *res`
:   the ttm_resource to use for the purpose of accounting, may or may not
    be bo->tbo.resource

`int sign`
:   if we should add (+1) or subtract (-1) from the stat

**Description**

Caller need to have the vm status_lock held. Useful for when multiple update
need to happen at the same time.

void amdgpu_vm_update_stats(struct amdgpu_vm_bo_base \*base, struct [ttm_resource](../drm-mm.md#c.ttm_resource "ttm_resource") \*res, int sign)
:   helper to update normal memory stat

**Parameters**

`struct amdgpu_vm_bo_base *base`
:   base structure for tracking BO usage in a VM

`struct ttm_resource *res`
:   the ttm_resource to use for the purpose of accounting, may or may not
    be bo->tbo.resource

`int sign`
:   if we should add (+1) or subtract (-1) from the stat

**Description**

Updates the basic memory stat when bo is added/deleted/moved.

void amdgpu_vm_bo_base_init(struct amdgpu_vm_bo_base \*base, struct amdgpu_vm \*vm, struct amdgpu_bo \*bo)
:   Adds bo to the list of bos associated with the vm

**Parameters**

`struct amdgpu_vm_bo_base *base`
:   base structure for tracking BO usage in a VM

`struct amdgpu_vm *vm`
:   vm to which bo is to be added

`struct amdgpu_bo *bo`
:   amdgpu buffer object

**Description**

Initialize a bo_va_base structure and add it to the appropriate lists

int amdgpu_vm_lock_pd(struct amdgpu_vm \*vm, struct [drm_exec](../drm-mm.md#c.drm_exec "drm_exec") \*exec, unsigned int num_fences)
:   lock PD in drm_exec

**Parameters**

`struct amdgpu_vm *vm`
:   vm providing the BOs

`struct drm_exec *exec`
:   drm execution context

`unsigned int num_fences`
:   number of extra fences to reserve

**Description**

Lock the VM root PD in the DRM execution context.

void amdgpu_vm_move_to_lru_tail(struct amdgpu_device \*adev, struct amdgpu_vm \*vm)
:   move all BOs to the end of LRU

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_vm *vm`
:   vm providing the BOs

**Description**

Move all BOs to the end of LRU and remember their positions to put them
together.

uint64_t amdgpu_vm_generation(struct amdgpu_device \*adev, struct amdgpu_vm \*vm)
:   return the page table re-generation counter

**Parameters**

`struct amdgpu_device *adev`
:   the amdgpu_device

`struct amdgpu_vm *vm`
:   optional VM to check, might be NULL

**Description**

Returns a page table re-generation token to allow checking if submissions
are still valid to use this VM. The VM parameter might be NULL in which case
just the VRAM lost counter will be used.

int amdgpu_vm_validate(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, struct ww_acquire_ctx \*ticket, int (\*validate)(void \*p, struct amdgpu_bo \*bo), void \*param)
:   validate evicted BOs tracked in the VM

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_vm *vm`
:   vm providing the BOs

`struct ww_acquire_ctx *ticket`
:   optional reservation ticket used to reserve the VM

`int (*validate)(void *p, struct amdgpu_bo *bo)`
:   callback to do the validation

`void *param`
:   parameter for the validation callback

**Description**

Validate the page table BOs and per-VM BOs on command submission if
necessary. If a ticket is given, also try to validate evicted user queue
BOs. They must already be reserved with the given ticket.

**Return**

Validation result.

bool amdgpu_vm_ready(struct amdgpu_vm \*vm)
:   check VM is ready for updates

**Parameters**

`struct amdgpu_vm *vm`
:   VM to check

**Description**

Check if all VM PDs/PTs are ready for updates

**Return**

True if VM is not evicting and all VM entities are not stopped

void amdgpu_vm_check_compute_bug(struct amdgpu_device \*adev)
:   check whether asic has compute vm bug

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

bool amdgpu_vm_need_pipeline_sync(struct amdgpu_ring \*ring, struct amdgpu_job \*job)
:   Check if pipe sync is needed for job.

**Parameters**

`struct amdgpu_ring *ring`
:   ring on which the job will be submitted

`struct amdgpu_job *job`
:   job to submit

**Return**

True if sync is needed.

int amdgpu_vm_flush(struct amdgpu_ring \*ring, struct amdgpu_job \*job, bool need_pipe_sync)
:   hardware flush the vm

**Parameters**

`struct amdgpu_ring *ring`
:   ring to use for flush

`struct amdgpu_job *job`
:   related job

`bool need_pipe_sync`
:   is pipe sync needed

**Description**

Emit a VM flush when it is necessary.

**Return**

0 on success, errno otherwise.

struct amdgpu_bo_va \*amdgpu_vm_bo_find(struct amdgpu_vm \*vm, struct amdgpu_bo \*bo)
:   find the bo_va for a specific vm & bo

**Parameters**

`struct amdgpu_vm *vm`
:   requested vm

`struct amdgpu_bo *bo`
:   requested buffer object

**Description**

Find **bo** inside the requested vm.
Search inside the **bos** vm list for the requested vm
Returns the found bo_va or NULL if none is found

Object has to be reserved!

**Return**

Found bo_va or NULL.

uint64_t amdgpu_vm_map_gart(const dma_addr_t \*pages_addr, uint64_t addr)
:   Resolve gart mapping of addr

**Parameters**

`const dma_addr_t *pages_addr`
:   optional DMA address to use for lookup

`uint64_t addr`
:   the unmapped addr

**Description**

Look up the physical address of the page that the pte resolves
to.

**Return**

The pointer for the page table entry.

int amdgpu_vm_update_pdes(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, bool immediate)
:   make sure that all directories are valid

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`bool immediate`
:   submit immediately to the paging queue

**Description**

Makes sure all directories are up to date.

**Return**

0 for success, error for failure.

void amdgpu_vm_tlb_seq_cb(struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*fence, struct [dma_fence_cb](../../driver-api/dma-buf.md#c.dma_fence_cb "dma_fence_cb") \*cb)
:   make sure to increment tlb sequence

**Parameters**

`struct dma_fence *fence`
:   unused

`struct dma_fence_cb *cb`
:   the callback structure

**Description**

Increments the tlb sequence to make sure that future CS execute a VM flush.

void amdgpu_vm_tlb_flush(struct amdgpu_vm_update_params \*params, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*\*fence, struct [amdgpu_vm_tlb_seq_struct](driver-core.md#c.amdgpu_vm_tlb_seq_struct "amdgpu_vm_tlb_seq_struct") \*tlb_cb)
:   prepare TLB flush

**Parameters**

`struct amdgpu_vm_update_params *params`
:   parameters for update

`struct dma_fence **fence`
:   input fence to sync TLB flush with

`struct amdgpu_vm_tlb_seq_struct *tlb_cb`
:   the callback structure

**Description**

Increments the tlb sequence to make sure that future CS execute a VM flush.

int amdgpu_vm_update_range(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, bool immediate, bool unlocked, bool flush_tlb, bool allow_override, struct amdgpu_sync \*sync, uint64_t start, uint64_t last, uint64_t flags, uint64_t offset, uint64_t vram_base, struct [ttm_resource](../drm-mm.md#c.ttm_resource "ttm_resource") \*res, dma_addr_t \*pages_addr, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*\*fence)
:   update a range in the vm page table

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer to use for commands

`struct amdgpu_vm *vm`
:   the VM to update the range

`bool immediate`
:   immediate submission in a page fault

`bool unlocked`
:   unlocked invalidation during MM callback

`bool flush_tlb`
:   trigger tlb invalidation after update completed

`bool allow_override`
:   change MTYPE for local NUMA nodes

`struct amdgpu_sync *sync`
:   fences we need to sync to

`uint64_t start`
:   start of mapped range

`uint64_t last`
:   last mapped entry

`uint64_t flags`
:   flags for the entries

`uint64_t offset`
:   offset into nodes and pages_addr

`uint64_t vram_base`
:   base for vram mappings

`struct ttm_resource *res`
:   ttm_resource to map

`dma_addr_t *pages_addr`
:   DMA addresses to use for mapping

`struct dma_fence **fence`
:   optional resulting fence

**Description**

Fill in the page table entries between **start** and **last**.

**Return**

0 for success, negative erro code for failure.

int amdgpu_vm_bo_update(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va, bool clear)
:   update all BO mappings in the vm page table

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   requested BO and VM object

`bool clear`
:   if true clear the entries

**Description**

Fill in the page table entries for **bo_va**.

**Return**

0 for success, -EINVAL for failure.

void amdgpu_vm_update_prt_state(struct amdgpu_device \*adev)
:   update the global PRT state

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

void amdgpu_vm_prt_get(struct amdgpu_device \*adev)
:   add a PRT user

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

void amdgpu_vm_prt_put(struct amdgpu_device \*adev)
:   drop a PRT user

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

void amdgpu_vm_prt_cb(struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*fence, struct [dma_fence_cb](../../driver-api/dma-buf.md#c.dma_fence_cb "dma_fence_cb") \*_cb)
:   callback for updating the PRT status

**Parameters**

`struct dma_fence *fence`
:   fence for the callback

`struct dma_fence_cb *_cb`
:   the callback function

void amdgpu_vm_add_prt_cb(struct amdgpu_device \*adev, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*fence)
:   add callback for updating the PRT status

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct dma_fence *fence`
:   fence for the callback

void amdgpu_vm_free_mapping(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, struct amdgpu_bo_va_mapping \*mapping, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*fence)
:   free a mapping

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`struct amdgpu_bo_va_mapping *mapping`
:   mapping to be freed

`struct dma_fence *fence`
:   fence of the unmap operation

**Description**

Free a mapping and make sure we decrease the PRT usage count if applicable.

void amdgpu_vm_prt_fini(struct amdgpu_device \*adev, struct amdgpu_vm \*vm)
:   finish all prt mappings

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

**Description**

Register a cleanup callback to disable PRT support after VM dies.

int amdgpu_vm_clear_freed(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, struct [dma_fence](../../driver-api/dma-buf.md#c.dma_fence "dma_fence") \*\*fence)
:   clear freed BOs in the PT

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`struct dma_fence **fence`
:   optional resulting fence (unchanged if no work needed to be done
    or if an error occurred)

**Description**

Make sure all freed BOs are cleared in the PT.
PTs have to be reserved and mutex must be locked!

**Return**

0 for success.

int amdgpu_vm_handle_moved(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, struct ww_acquire_ctx \*ticket)
:   handle moved BOs in the PT

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`struct ww_acquire_ctx *ticket`
:   optional reservation ticket used to reserve the VM

**Description**

Make sure all BOs which are moved are updated in the PTs.

PTs have to be reserved!

**Return**

0 for success.

int amdgpu_vm_flush_compute_tlb(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, uint32_t flush_type, uint32_t xcc_mask)
:   Flush TLB on compute VM

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`uint32_t flush_type`
:   flush type

`uint32_t xcc_mask`
:   mask of XCCs that belong to the compute partition in need of a TLB flush.

**Description**

Flush TLB if needed for a compute VM.

**Return**

0 for success.

struct amdgpu_bo_va \*amdgpu_vm_bo_add(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, struct amdgpu_bo \*bo)
:   add a bo to a specific vm

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`struct amdgpu_bo *bo`
:   amdgpu buffer object

**Description**

Add **bo** into the requested vm.
Add **bo** to the list of bos associated with the vm

Object has to be reserved!

**Return**

Newly added bo_va or NULL for failure

void amdgpu_vm_bo_insert_map(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va, struct amdgpu_bo_va_mapping \*mapping)
:   insert a new mapping

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   bo_va to store the address

`struct amdgpu_bo_va_mapping *mapping`
:   the mapping to insert

**Description**

Insert a new mapping into all structures.

int amdgpu_vm_bo_map(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)
:   map bo inside a vm

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   bo_va to store the address

`uint64_t saddr`
:   where to map the BO

`uint64_t offset`
:   requested offset in the BO

`uint64_t size`
:   BO size in bytes

`uint64_t flags`
:   attributes of pages (read/write/valid/etc.)

**Description**

Add a mapping of the BO at the specefied addr into the VM.

Object has to be reserved and unreserved outside!

**Return**

0 for success, error for failure.

int amdgpu_vm_bo_replace_map(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va, uint64_t saddr, uint64_t offset, uint64_t size, uint64_t flags)
:   map bo inside a vm, replacing existing mappings

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   bo_va to store the address

`uint64_t saddr`
:   where to map the BO

`uint64_t offset`
:   requested offset in the BO

`uint64_t size`
:   BO size in bytes

`uint64_t flags`
:   attributes of pages (read/write/valid/etc.)

**Description**

Add a mapping of the BO at the specefied addr into the VM. Replace existing
mappings as we do so.

Object has to be reserved and unreserved outside!

**Return**

0 for success, error for failure.

int amdgpu_vm_bo_unmap(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va, uint64_t saddr)
:   remove bo mapping from vm

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   bo_va to remove the address from

`uint64_t saddr`
:   where to the BO is mapped

**Description**

Remove a mapping of the BO at the specefied addr from the VM.

Object has to be reserved and unreserved outside!

**Return**

0 for success, error for failure.

int amdgpu_vm_bo_clear_mappings(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, uint64_t saddr, uint64_t size)
:   remove all mappings in a specific range

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   VM structure to use

`uint64_t saddr`
:   start of the range

`uint64_t size`
:   size of the range

**Description**

Remove all mappings in a range, split them as appropriate.

**Return**

0 for success, error for failure.

struct amdgpu_bo_va_mapping \*amdgpu_vm_bo_lookup_mapping(struct amdgpu_vm \*vm, uint64_t addr)
:   find mapping by address

**Parameters**

`struct amdgpu_vm *vm`
:   the requested VM

`uint64_t addr`
:   the address

**Description**

Find a mapping by it’s address.

**Return**

The amdgpu_bo_va_mapping matching for addr or NULL

void amdgpu_vm_bo_trace_cs(struct amdgpu_vm \*vm, struct ww_acquire_ctx \*ticket)
:   trace all reserved mappings

**Parameters**

`struct amdgpu_vm *vm`
:   the requested vm

`struct ww_acquire_ctx *ticket`
:   CS ticket

**Description**

Trace all mappings of BOs reserved during a command submission.

void amdgpu_vm_bo_del(struct amdgpu_device \*adev, struct amdgpu_bo_va \*bo_va)
:   remove a bo from a specific vm

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_bo_va *bo_va`
:   requested bo_va

**Description**

Remove **bo_va->bo** from the requested vm.

Object have to be reserved!

bool amdgpu_vm_evictable(struct amdgpu_bo \*bo)
:   check if we can evict a VM

**Parameters**

`struct amdgpu_bo *bo`
:   A page table of the VM.

**Description**

Check if it is possible to evict a VM.

void amdgpu_vm_bo_invalidate(struct amdgpu_bo \*bo, bool evicted)
:   mark the bo as invalid

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu buffer object

`bool evicted`
:   is the BO evicted

**Description**

Mark **bo** as invalid.

void amdgpu_vm_bo_move(struct amdgpu_bo \*bo, struct [ttm_resource](../drm-mm.md#c.ttm_resource "ttm_resource") \*new_mem, bool evicted)
:   handle BO move

**Parameters**

`struct amdgpu_bo *bo`
:   amdgpu buffer object

`struct ttm_resource *new_mem`
:   the new placement of the BO move

`bool evicted`
:   is the BO evicted

**Description**

Update the memory stats for the new placement and mark **bo** as invalid.

uint32_t amdgpu_vm_get_block_size(uint64_t vm_size)
:   calculate VM page table size as power of two

**Parameters**

`uint64_t vm_size`
:   VM size

**Return**

VM page table as power of two

void amdgpu_vm_adjust_size(struct amdgpu_device \*adev, uint32_t min_vm_size, uint32_t fragment_size_default, unsigned max_level, unsigned max_bits)
:   adjust vm size, block size and fragment size

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`uint32_t min_vm_size`
:   the minimum vm size in GB if it’s set auto

`uint32_t fragment_size_default`
:   Default PTE fragment size

`unsigned max_level`
:   max VMPT level

`unsigned max_bits`
:   max address space size in bits

long amdgpu_vm_wait_idle(struct amdgpu_vm \*vm, long timeout)
:   wait for the VM to become idle

**Parameters**

`struct amdgpu_vm *vm`
:   VM object to wait for

`long timeout`
:   timeout to wait for VM to become idle

void amdgpu_vm_put_task_info(struct amdgpu_task_info \*task_info)
:   reference down the vm task_info ptr

**Parameters**

`struct amdgpu_task_info *task_info`
:   task_info `struct under` discussion.

**Description**

frees the vm task_info ptr at the last put

struct amdgpu_task_info \*amdgpu_vm_get_task_info_vm(struct amdgpu_vm \*vm)
:   Extracts task info for a vm.

**Parameters**

`struct amdgpu_vm *vm`
:   VM to get info from

**Description**

Returns the reference counted task_info structure, which must be
referenced down with amdgpu_vm_put_task_info.

struct amdgpu_task_info \*amdgpu_vm_get_task_info_pasid(struct amdgpu_device \*adev, u32 pasid)
:   Extracts task info for a PASID.

**Parameters**

`struct amdgpu_device *adev`
:   drm device pointer

`u32 pasid`
:   PASID identifier for VM

**Description**

Returns the reference counted task_info structure, which must be
referenced down with amdgpu_vm_put_task_info.

void amdgpu_vm_set_task_info(struct amdgpu_vm \*vm)
:   Sets VMs task info.

**Parameters**

`struct amdgpu_vm *vm`
:   vm for which to set the info

int amdgpu_vm_init(struct amdgpu_device \*adev, struct amdgpu_vm \*vm, int32_t xcp_id)
:   initialize a vm instance

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

`int32_t xcp_id`
:   GPU partition selection id

**Description**

Init **vm** fields.

**Return**

0 for success, error for failure.

int amdgpu_vm_make_compute(struct amdgpu_device \*adev, struct amdgpu_vm \*vm)
:   Turn a GFX VM into a compute VM

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

**Description**

This only works on GFX VMs that don’t have any BOs added and no
page tables allocated yet.

Changes the following VM parameters:
- use_cpu_for_update
- pte_supports_ats

Reinitializes the page directory to reflect the changed ATS
setting.

**Return**

0 for success, -errno for errors.

void amdgpu_vm_fini(struct amdgpu_device \*adev, struct amdgpu_vm \*vm)
:   tear down a vm instance

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

`struct amdgpu_vm *vm`
:   requested vm

**Description**

Tear down **vm**.
Unbind the VM and remove all bos from the vm bo list

void amdgpu_vm_manager_init(struct amdgpu_device \*adev)
:   init the VM manager

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

**Description**

Initialize the VM manager structures

void amdgpu_vm_manager_fini(struct amdgpu_device \*adev)
:   cleanup VM manager

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu_device pointer

**Description**

Cleanup the VM manager and free resources.

int amdgpu_vm_ioctl(struct [drm_device](../drm-internals.md#c.drm_device "drm_device") \*dev, void \*data, struct [drm_file](../drm-internals.md#c.drm_file "drm_file") \*filp)
:   Manages VMID reservation for vm hubs.

**Parameters**

`struct drm_device *dev`
:   drm device pointer

`void *data`
:   drm_amdgpu_vm

`struct drm_file *filp`
:   drm file pointer

**Return**

0 for success, -errno for errors.

bool amdgpu_vm_handle_fault(struct amdgpu_device \*adev, u32 pasid, u32 vmid, u32 node_id, uint64_t addr, uint64_t ts, bool write_fault)
:   graceful handling of VM faults.

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`u32 pasid`
:   PASID of the VM

`u32 vmid`
:   VMID, only used for GFX 9.4.3.

`u32 node_id`
:   Node_id received in IH cookie. Only applicable for
    GFX 9.4.3.

`uint64_t addr`
:   Address of the fault

`uint64_t ts`
:   Timestamp of the fault

`bool write_fault`
:   true is write fault, false is read fault

**Description**

Try to gracefully handle a VM fault. Return true if the fault was handled and
shouldn’t be reported any more.

void amdgpu_debugfs_vm_bo_info(struct amdgpu_vm \*vm, struct seq_file \*m)
:   print BO info for the VM

**Parameters**

`struct amdgpu_vm *vm`
:   Requested VM for printing BO info

`struct seq_file *m`
:   debugfs file

**Description**

Print BO information in debugfs file for the VM

void amdgpu_vm_update_fault_cache(struct amdgpu_device \*adev, unsigned int pasid, uint64_t addr, uint32_t status, unsigned int vmhub)
:   update cached fault into.

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`unsigned int pasid`
:   PASID of the VM

`uint64_t addr`
:   Address of the fault

`uint32_t status`
:   GPUVM fault status register

`unsigned int vmhub`
:   which vmhub got the fault

**Description**

Cache the fault info for later use by userspace in debugging.

bool amdgpu_vm_is_bo_always_valid(struct amdgpu_vm \*vm, struct amdgpu_bo \*bo)
:   check if the BO is VM always valid

**Parameters**

`struct amdgpu_vm *vm`
:   VM to test against.

`struct amdgpu_bo *bo`
:   BO to be tested.

**Description**

Returns true if the BO shares the dma_resv object with the root PD and is
always guaranteed to be valid inside the VM.

## Interrupt Handling

Interrupts generated within GPU hardware raise interrupt requests that are
passed to amdgpu IRQ handler which is responsible for detecting source and
type of the interrupt and dispatching matching handlers. If handling an
interrupt requires calling kernel functions that may sleep processing is
dispatched to work handlers.

If MSI functionality is not disabled by module parameter then MSI
support will be enabled.

For GPU interrupt sources that may be driven by another driver, IRQ domain
support is used (with mapping between virtual and hardware IRQs).

void amdgpu_irq_disable_all(struct amdgpu_device \*adev)
:   disable *all* interrupts

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Disable all types of interrupts from all sources.

irqreturn_t amdgpu_irq_handler(int irq, void \*arg)
:   IRQ handler

**Parameters**

`int irq`
:   IRQ number (unused)

`void *arg`
:   pointer to DRM device

**Description**

IRQ handler for amdgpu driver (all ASICs).

**Return**

result of handling the IRQ, as defined by `irqreturn_t`

void amdgpu_irq_handle_ih1(struct work_struct \*work)
:   kick of processing for IH1

**Parameters**

`struct work_struct *work`
:   work structure in `struct amdgpu_irq`

**Description**

Kick of processing IH ring 1.

void amdgpu_irq_handle_ih2(struct work_struct \*work)
:   kick of processing for IH2

**Parameters**

`struct work_struct *work`
:   work structure in `struct amdgpu_irq`

**Description**

Kick of processing IH ring 2.

void amdgpu_irq_handle_ih_soft(struct work_struct \*work)
:   kick of processing for ih_soft

**Parameters**

`struct work_struct *work`
:   work structure in `struct amdgpu_irq`

**Description**

Kick of processing IH soft ring.

bool amdgpu_msi_ok(struct amdgpu_device \*adev)
:   check whether MSI functionality is enabled

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer (unused)

**Description**

Checks whether MSI functionality has been disabled via module parameter
(all ASICs).

**Return**

*true* if MSIs are allowed to be enabled or *false* otherwise

int amdgpu_irq_init(struct amdgpu_device \*adev)
:   initialize interrupt handling

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Sets up work functions for hotplug and reset interrupts, enables MSI
functionality, initializes vblank, hotplug and reset interrupt handling.

**Return**

0 on success or error code on failure

void amdgpu_irq_fini_sw(struct amdgpu_device \*adev)
:   shut down interrupt handling

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Tears down work functions for hotplug and reset interrupts, disables MSI
functionality, shuts down vblank, hotplug and reset interrupt handling,
turns off interrupts from all sources (all ASICs).

int amdgpu_irq_add_id(struct amdgpu_device \*adev, unsigned int client_id, unsigned int src_id, struct amdgpu_irq_src \*source)
:   register IRQ source

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`unsigned int client_id`
:   client id

`unsigned int src_id`
:   source id

`struct amdgpu_irq_src *source`
:   IRQ source pointer

**Description**

Registers IRQ source on a client.

**Return**

0 on success or error code otherwise

void amdgpu_irq_dispatch(struct amdgpu_device \*adev, struct amdgpu_ih_ring \*ih)
:   dispatch IRQ to IP blocks

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_ih_ring *ih`
:   interrupt ring instance

**Description**

Dispatches IRQ to IP blocks.

void amdgpu_irq_delegate(struct amdgpu_device \*adev, struct amdgpu_iv_entry \*entry, unsigned int num_dw)
:   delegate IV to soft IH ring

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_iv_entry *entry`
:   IV entry

`unsigned int num_dw`
:   size of IV

**Description**

Delegate the IV to the soft IH ring and schedule processing of it. Used
if the hardware delegation to IH1 or IH2 doesn’t work for some reason.

int amdgpu_irq_update(struct amdgpu_device \*adev, struct amdgpu_irq_src \*src, unsigned int type)
:   update hardware interrupt state

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_irq_src *src`
:   interrupt source pointer

`unsigned int type`
:   type of interrupt

**Description**

Updates interrupt state for the specific source (all ASICs).

void amdgpu_irq_gpu_reset_resume_helper(struct amdgpu_device \*adev)
:   update interrupt states on all sources

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Updates state of all types of interrupts on all sources on resume after
reset.

int amdgpu_irq_get(struct amdgpu_device \*adev, struct amdgpu_irq_src \*src, unsigned int type)
:   enable interrupt

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_irq_src *src`
:   interrupt source pointer

`unsigned int type`
:   type of interrupt

**Description**

Enables specified type of interrupt on the specified source (all ASICs).

**Return**

0 on success or error code otherwise

int amdgpu_irq_put(struct amdgpu_device \*adev, struct amdgpu_irq_src \*src, unsigned int type)
:   disable interrupt

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_irq_src *src`
:   interrupt source pointer

`unsigned int type`
:   type of interrupt

**Description**

Enables specified type of interrupt on the specified source (all ASICs).

**Return**

0 on success or error code otherwise

bool amdgpu_irq_enabled(struct amdgpu_device \*adev, struct amdgpu_irq_src \*src, unsigned int type)
:   check whether interrupt is enabled or not

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`struct amdgpu_irq_src *src`
:   interrupt source pointer

`unsigned int type`
:   type of interrupt

**Description**

Checks whether the given type of interrupt is enabled on the given source.

**Return**

*true* if interrupt is enabled, *false* if interrupt is disabled or on
invalid parameters

int amdgpu_irqdomain_map(struct [irq_domain](../../core-api/irq/irq-domain.md#c.irq_domain "irq_domain") \*d, unsigned int irq, irq_hw_number_t hwirq)
:   create mapping between virtual and hardware IRQ numbers

**Parameters**

`struct irq_domain *d`
:   amdgpu IRQ domain pointer (unused)

`unsigned int irq`
:   virtual IRQ number

`irq_hw_number_t hwirq`
:   hardware irq number

**Description**

Current implementation assigns simple interrupt handler to the given virtual
IRQ.

**Return**

0 on success or error code otherwise

int amdgpu_irq_add_domain(struct amdgpu_device \*adev)
:   create a linear IRQ domain

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Creates an IRQ domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

**Return**

0 on success or error code otherwise

void amdgpu_irq_remove_domain(struct amdgpu_device \*adev)
:   remove the IRQ domain

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

**Description**

Removes the IRQ domain for GPU interrupt sources
that may be driven by another driver (e.g., ACP).

unsigned int amdgpu_irq_create_mapping(struct amdgpu_device \*adev, unsigned int src_id)
:   create mapping between domain Linux IRQs

**Parameters**

`struct amdgpu_device *adev`
:   amdgpu device pointer

`unsigned int src_id`
:   IH source id

**Description**

Creates mapping between a domain IRQ (GPU IH src id) and a Linux IRQ
Use this for components that generate a GPU interrupt, but are driven
by a different driver (e.g., ACP).

**Return**

Linux IRQ

## IP Blocks

GPUs are composed of IP (intellectual property) blocks. These
IP blocks provide various functionalities: display, graphics,
video decode, etc. The IP blocks that comprise a particular GPU
are listed in the GPU’s respective SoC file. amdgpu_device.c
acquires the list of IP blocks for the GPU in use on initialization.
It can then operate on this list to perform standard driver operations
such as: init, fini, suspend, resume, etc.

IP block implementations are named using the following convention:
<functionality>_v<version> (E.g.: gfx_v6_0).

enum amd_ip_block_type
:   Used to classify IP blocks by functionality.

**Constants**

`AMD_IP_BLOCK_TYPE_COMMON`
:   GPU Family

`AMD_IP_BLOCK_TYPE_GMC`
:   Graphics Memory Controller

`AMD_IP_BLOCK_TYPE_IH`
:   Interrupt Handler

`AMD_IP_BLOCK_TYPE_SMC`
:   System Management Controller

`AMD_IP_BLOCK_TYPE_PSP`
:   Platform Security Processor

`AMD_IP_BLOCK_TYPE_DCE`
:   Display and Compositing Engine

`AMD_IP_BLOCK_TYPE_GFX`
:   Graphics and Compute Engine

`AMD_IP_BLOCK_TYPE_SDMA`
:   System DMA Engine

`AMD_IP_BLOCK_TYPE_UVD`
:   Unified Video Decoder

`AMD_IP_BLOCK_TYPE_VCE`
:   Video Compression Engine

`AMD_IP_BLOCK_TYPE_ACP`
:   Audio Co-Processor

`AMD_IP_BLOCK_TYPE_VCN`
:   Video Core/Codec Next

`AMD_IP_BLOCK_TYPE_MES`
:   Micro-Engine Scheduler

`AMD_IP_BLOCK_TYPE_JPEG`
:   JPEG Engine

`AMD_IP_BLOCK_TYPE_VPE`
:   Video Processing Engine

`AMD_IP_BLOCK_TYPE_UMSCH_MM`
:   User Mode Scheduler for Multimedia

`AMD_IP_BLOCK_TYPE_ISP`
:   Image Signal Processor

`AMD_IP_BLOCK_TYPE_NUM`
:   Total number of IP block types

enum DC_DEBUG_MASK
:   Bits that are useful for debugging the Display Core IP

**Constants**

`DC_DISABLE_PIPE_SPLIT`
:   If set, disable pipe-splitting

`DC_DISABLE_STUTTER`
:   If set, disable memory stutter mode

`DC_DISABLE_DSC`
:   If set, disable display stream compression

`DC_DISABLE_CLOCK_GATING`
:   If set, disable clock gating optimizations

`DC_DISABLE_PSR`
:   If set, disable Panel self refresh v1 and PSR-SU

`DC_FORCE_SUBVP_MCLK_SWITCH`
:   If set, force mclk switch in subvp, even
    if mclk switch in vblank is possible

`DC_DISABLE_MPO`
:   If set, disable multi-plane offloading

`DC_ENABLE_DPIA_TRACE`
:   If set, enable trace logging for DPIA

`DC_ENABLE_DML2`
:   If set, force usage of DML2, even if the DCN version
    does not default to it.

`DC_DISABLE_PSR_SU`
:   If set, disable PSR SU

`DC_DISABLE_REPLAY`
:   If set, disable Panel Replay

`DC_DISABLE_IPS`
:   If set, disable all Idle Power States, all the time.
    If more than one IPS debug bit is set, the lowest bit takes
    precedence. For example, if DC_FORCE_IPS_ENABLE and
    DC_DISABLE_IPS_DYNAMIC are set, then DC_DISABLE_IPS_DYNAMIC takes
    precedence.

`DC_DISABLE_IPS_DYNAMIC`
:   If set, disable all IPS, all the time,
    *except* when driver goes into suspend.

`DC_DISABLE_IPS2_DYNAMIC`
:   If set, disable IPS2 (IPS1 allowed) if
    there is an enabled display. Otherwise, enable all IPS.

`DC_FORCE_IPS_ENABLE`
:   If set, force enable all IPS, all the time.

`DC_DISABLE_ACPI_EDID`
:   If set, don’t attempt to fetch EDID for
    eDP display from ACPI _DDC method.

`DC_DISABLE_HDMI_CEC`
:   If set, disable HDMI-CEC feature in amdgpu driver.

`DC_DISABLE_SUBVP_FAMS`
:   If set, disable DCN Sub-Viewport & Firmware Assisted
    Memory Clock Switching (FAMS) feature in amdgpu driver.

`DC_DISABLE_CUSTOM_BRIGHTNESS_CURVE`
:   If set, disable support for custom brightness curves

`DC_HDCP_LC_FORCE_FW_ENABLE`
:   If set, use HDCP Locality Check FW
    path regardless of reported HW capabilities.

`DC_HDCP_LC_ENABLE_SW_FALLBACK`
:   If set, upon HDCP Locality Check FW
    path failure, retry using legacy SW path.

`DC_SKIP_DETECTION_LT`
:   If set, skip detection link training

struct amd_ip_funcs
:   general hooks for managing amdgpu IP Blocks

**Definition**:

```
struct amd_ip_funcs {
    char *name;
    int (*early_init)(struct amdgpu_ip_block *ip_block);
    int (*late_init)(struct amdgpu_ip_block *ip_block);
    int (*sw_init)(struct amdgpu_ip_block *ip_block);
    int (*sw_fini)(struct amdgpu_ip_block *ip_block);
    int (*early_fini)(struct amdgpu_ip_block *ip_block);
    int (*hw_init)(struct amdgpu_ip_block *ip_block);
    int (*hw_fini)(struct amdgpu_ip_block *ip_block);
    void (*late_fini)(struct amdgpu_ip_block *ip_block);
    int (*prepare_suspend)(struct amdgpu_ip_block *ip_block);
    int (*suspend)(struct amdgpu_ip_block *ip_block);
    int (*resume)(struct amdgpu_ip_block *ip_block);
    void (*complete)(struct amdgpu_ip_block *ip_block);
    bool (*is_idle)(struct amdgpu_ip_block *ip_block);
    int (*wait_for_idle)(struct amdgpu_ip_block *ip_block);
    bool (*check_soft_reset)(struct amdgpu_ip_block *ip_block);
    int (*pre_soft_reset)(struct amdgpu_ip_block *ip_block);
    int (*soft_reset)(struct amdgpu_ip_block *ip_block);
    int (*post_soft_reset)(struct amdgpu_ip_block *ip_block);
    int (*set_clockgating_state)(struct amdgpu_ip_block *ip_block, enum amd_clockgating_state state);
    int (*set_powergating_state)(struct amdgpu_ip_block *ip_block, enum amd_powergating_state state);
    void (*get_clockgating_state)(struct amdgpu_ip_block *ip_block, u64 *flags);
    void (*dump_ip_state)(struct amdgpu_ip_block *ip_block);
    void (*print_ip_state)(struct amdgpu_ip_block *ip_block, struct drm_printer *p);
};
```

**Members**

`name`
:   Name of IP block

`early_init`
:   sets up early driver state (pre sw_init),
    does not configure hw - Optional

`late_init`
:   sets up late driver/hw state (post hw_init) - Optional

`sw_init`
:   sets up driver state, does not configure hw

`sw_fini`
:   tears down driver state, does not configure hw

`early_fini`
:   tears down stuff before dev detached from driver

`hw_init`
:   sets up the hw state

`hw_fini`
:   tears down the hw state

`late_fini`
:   final cleanup

`prepare_suspend`
:   handle IP specific changes to prepare for suspend
    (such as allocating any required memory)

`suspend`
:   handles IP specific hw/sw changes for suspend

`resume`
:   handles IP specific hw/sw changes for resume

`complete`
:   handles IP specific changes after resume

`is_idle`
:   returns current IP block idle status

`wait_for_idle`
:   poll for idle

`check_soft_reset`
:   check soft reset the IP block

`pre_soft_reset`
:   pre soft reset the IP block

`soft_reset`
:   soft reset the IP block

`post_soft_reset`
:   post soft reset the IP block

`set_clockgating_state`
:   enable/disable cg for the IP block

`set_powergating_state`
:   enable/disable pg for the IP block

`get_clockgating_state`
:   get current clockgating status

`dump_ip_state`
:   dump the IP state of the ASIC during a gpu hang

`print_ip_state`
:   print the IP state in devcoredump for each IP of the ASIC

**Description**

These hooks provide an interface for controlling the operational state
of IP blocks. After acquiring a list of IP blocks for the GPU in use,
the driver can make chip-wide state changes by walking this list and
making calls to hooks from each IP block. This list is ordered to ensure
that the driver initializes the IP blocks in a safe sequence.
