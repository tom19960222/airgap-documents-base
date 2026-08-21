---
collection: kernel
version: "6.8"
title: "PCI Peer-to-Peer DMA Support"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/pci/p2pdma.html
fetched_at: 2026-08-21T03:31:54+00:00
---
# PCI Peer-to-Peer DMA Support

The PCI bus has pretty decent support for performing DMA transfers
between two devices on the bus. This type of transaction is henceforth
called Peer-to-Peer (or P2P). However, there are a number of issues that
make P2P transactions tricky to do in a perfectly safe way.

One of the biggest issues is that PCI doesn't require forwarding
transactions between hierarchy domains, and in PCIe, each Root Port
defines a separate hierarchy domain. To make things worse, there is no
simple way to determine if a given Root Complex supports this or not.
(See PCIe r4.0, sec 1.3.1). Therefore, as of this writing, the kernel
only supports doing P2P when the endpoints involved are all behind the
same PCI bridge, as such devices are all in the same PCI hierarchy
domain, and the spec guarantees that all transactions within the
hierarchy will be routable, but it does not require routing
between hierarchies.

The second issue is that to make use of existing interfaces in Linux,
memory that is used for P2P transactions needs to be backed by struct
pages. However, PCI BARs are not typically cache coherent so there are
a few corner case gotchas with these pages so developers need to
be careful about what they do with them.

## Driver Writer's Guide

In a given P2P implementation there may be three or more different
types of kernel drivers in play:

- Provider - A driver which provides or publishes P2P resources like
  memory or doorbell registers to other drivers.
- Client - A driver which makes use of a resource by setting up a
  DMA transaction to or from it.
- Orchestrator - A driver which orchestrates the flow of data between
  clients and providers.

In many cases there could be overlap between these three types (i.e.,
it may be typical for a driver to be both a provider and a client).

For example, in the NVMe Target Copy Offload implementation:

- The NVMe PCI driver is both a client, provider and orchestrator
  in that it exposes any CMB (Controller Memory Buffer) as a P2P memory
  resource (provider), it accepts P2P memory pages as buffers in requests
  to be used directly (client) and it can also make use of the CMB as
  submission queue entries (orchestrator).
- The RDMA driver is a client in this arrangement so that an RNIC
  can DMA directly to the memory exposed by the NVMe device.
- The NVMe Target driver (nvmet) can orchestrate the data from the RNIC
  to the P2P memory (CMB) and then to the NVMe device (and vice versa).

This is currently the only arrangement supported by the kernel but
one could imagine slight tweaks to this that would allow for the same
functionality. For example, if a specific RNIC added a BAR with some
memory behind it, its driver could add support as a P2P provider and
then the NVMe Target could use the RNIC's memory instead of the CMB
in cases where the NVMe cards in use do not have CMB support.

### Provider Drivers

A provider simply needs to register a BAR (or a portion of a BAR)
as a P2P DMA resource using [`pci_p2pdma_add_resource()`](p2pdma.md#c.pci_p2pdma_add_resource "pci_p2pdma_add_resource").
This will register struct pages for all the specified memory.

After that it may optionally publish all of its resources as
P2P memory using [`pci_p2pmem_publish()`](p2pdma.md#c.pci_p2pmem_publish "pci_p2pmem_publish"). This will allow
any orchestrator drivers to find and use the memory. When marked in
this way, the resource must be regular memory with no side effects.

For the time being this is fairly rudimentary in that all resources
are typically going to be P2P memory. Future work will likely expand
this to include other types of resources like doorbells.

### Client Drivers

A client driver only has to use the mapping API `dma_map_sg()`
and `dma_unmap_sg()` functions as usual, and the implementation
will do the right thing for the P2P capable memory.

### Orchestrator Drivers

The first task an orchestrator driver must do is compile a list of
all client devices that will be involved in a given transaction. For
example, the NVMe Target driver creates a list including the namespace
block device and the RNIC in use. If the orchestrator has access to
a specific P2P provider to use it may check compatibility using
`pci_p2pdma_distance()` otherwise it may find a memory provider
that's compatible with all clients using `pci_p2pmem_find()`.
If more than one provider is supported, the one nearest to all the clients will
be chosen first. If more than one provider is an equal distance away, the
one returned will be chosen at random (it is not an arbitrary but
truly random). This function returns the PCI device to use for the provider
with a reference taken and therefore when it's no longer needed it should be
returned with [`pci_dev_put()`](pci.md#c.pci_dev_put "pci_dev_put").

Once a provider is selected, the orchestrator can then use
[`pci_alloc_p2pmem()`](p2pdma.md#c.pci_alloc_p2pmem "pci_alloc_p2pmem") and [`pci_free_p2pmem()`](p2pdma.md#c.pci_free_p2pmem "pci_free_p2pmem") to
allocate P2P memory from the provider. [`pci_p2pmem_alloc_sgl()`](p2pdma.md#c.pci_p2pmem_alloc_sgl "pci_p2pmem_alloc_sgl")
and [`pci_p2pmem_free_sgl()`](p2pdma.md#c.pci_p2pmem_free_sgl "pci_p2pmem_free_sgl") are convenience functions for
allocating scatter-gather lists with P2P memory.

### Struct Page Caveats

Driver writers should be very careful about not passing these special
struct pages to code that isn't prepared for it. At this time, the kernel
interfaces do not have any checks for ensuring this. This obviously
precludes passing these pages to userspace.

P2P memory is also technically IO memory but should never have any side
effects behind it. Thus, the order of loads and stores should not be important
and ioreadX(), iowriteX() and friends should not be necessary.

## P2P DMA Support Library

int pci_p2pdma_add_resource(struct pci_dev \*pdev, int bar, size_t size, u64 offset)
:   add memory for use as p2p memory

**Parameters**

`struct pci_dev *pdev`
:   the device to add the memory to

`int bar`
:   PCI BAR to add

`size_t size`
:   size of the memory to add, may be zero to use the whole BAR

`u64 offset`
:   offset into the PCI BAR

**Description**

The memory will be given ZONE_DEVICE struct pages so that it may
be used with any DMA request.

int pci_p2pdma_distance_many(struct pci_dev \*provider, struct [device](../infrastructure.md#c.device "device") \*\*clients, int num_clients, bool verbose)
:   Determine the cumulative distance between a p2pdma provider and the clients in use.

**Parameters**

`struct pci_dev *provider`
:   p2pdma provider to check against the client list

`struct device **clients`
:   array of devices to check (NULL-terminated)

`int num_clients`
:   number of clients in the array

`bool verbose`
:   if true, print warnings for devices when we return -1

**Description**

Returns -1 if any of the clients are not compatible, otherwise returns a
positive number where a lower number is the preferable choice. (If there's
one client that's the same as the provider it will return 0, which is best
choice).

"compatible" means the provider and the clients are either all behind
the same PCI root port or the host bridges connected to each of the devices
are listed in the 'pci_p2pdma_whitelist'.

bool pci_has_p2pmem(struct pci_dev \*pdev)
:   check if a given PCI device has published any p2pmem

**Parameters**

`struct pci_dev *pdev`
:   PCI device to check

struct pci_dev \*pci_p2pmem_find_many(struct [device](../infrastructure.md#c.device "device") \*\*clients, int num_clients)
:   find a peer-to-peer DMA memory device compatible with the specified list of clients and shortest distance

**Parameters**

`struct device **clients`
:   array of devices to check (NULL-terminated)

`int num_clients`
:   number of client devices in the list

**Description**

If multiple devices are behind the same switch, the one "closest" to the
client devices in use will be chosen first. (So if one of the providers is
the same as one of the clients, that provider will be used ahead of any
other providers that are unrelated). If multiple providers are an equal
distance away, one will be chosen at random.

Returns a pointer to the PCI device with a reference taken (use pci_dev_put
to return the reference) or NULL if no compatible device is found. The
found provider will also be assigned to the client list.

void \*pci_alloc_p2pmem(struct pci_dev \*pdev, size_t size)
:   allocate peer-to-peer DMA memory

**Parameters**

`struct pci_dev *pdev`
:   the device to allocate memory from

`size_t size`
:   number of bytes to allocate

**Description**

Returns the allocated memory or NULL on error.

void pci_free_p2pmem(struct pci_dev \*pdev, void \*addr, size_t size)
:   free peer-to-peer DMA memory

**Parameters**

`struct pci_dev *pdev`
:   the device the memory was allocated from

`void *addr`
:   address of the memory that was allocated

`size_t size`
:   number of bytes that were allocated

pci_bus_addr_t pci_p2pmem_virt_to_bus(struct pci_dev \*pdev, void \*addr)
:   return the PCI bus address for a given virtual address obtained with [`pci_alloc_p2pmem()`](p2pdma.md#c.pci_alloc_p2pmem "pci_alloc_p2pmem")

**Parameters**

`struct pci_dev *pdev`
:   the device the memory was allocated from

`void *addr`
:   address of the memory that was allocated

struct scatterlist \*pci_p2pmem_alloc_sgl(struct pci_dev \*pdev, unsigned int \*nents, u32 length)
:   allocate peer-to-peer DMA memory in a scatterlist

**Parameters**

`struct pci_dev *pdev`
:   the device to allocate memory from

`unsigned int *nents`
:   the number of SG entries in the list

`u32 length`
:   number of bytes to allocate

**Return**

`NULL` on error or `struct scatterlist` pointer and **nents** on success

void pci_p2pmem_free_sgl(struct pci_dev \*pdev, struct scatterlist \*sgl)
:   free a scatterlist allocated by [`pci_p2pmem_alloc_sgl()`](p2pdma.md#c.pci_p2pmem_alloc_sgl "pci_p2pmem_alloc_sgl")

**Parameters**

`struct pci_dev *pdev`
:   the device to allocate memory from

`struct scatterlist *sgl`
:   the allocated scatterlist

void pci_p2pmem_publish(struct pci_dev \*pdev, bool publish)
:   publish the peer-to-peer DMA memory for use by other devices with pci_p2pmem_find()

**Parameters**

`struct pci_dev *pdev`
:   the device with peer-to-peer DMA memory to publish

`bool publish`
:   set to true to publish the memory, false to unpublish it

**Description**

Published memory can be used by other PCI device drivers for
peer-2-peer DMA operations. Non-published memory is reserved for
exclusive use of the device driver that registers the peer-to-peer
memory.

int pci_p2pdma_enable_store(const char \*page, struct pci_dev \*\*p2p_dev, bool \*use_p2pdma)
:   parse a configfs/sysfs attribute store to enable p2pdma

**Parameters**

`const char *page`
:   contents of the value to be stored

`struct pci_dev **p2p_dev`
:   returns the PCI device that was selected to be used
    (if one was specified in the stored value)

`bool *use_p2pdma`
:   returns whether to enable p2pdma or not

**Description**

Parses an attribute value to decide whether to enable p2pdma.
The value can select a PCI device (using its full BDF device
name) or a boolean (in any format [`kstrtobool()`](../../core-api/kernel-api.md#c.kstrtobool "kstrtobool") accepts). A false
value disables p2pdma, a true value expects the caller
to automatically find a compatible device and specifying a PCI device
expects the caller to use the specific provider.

[`pci_p2pdma_enable_show()`](p2pdma.md#c.pci_p2pdma_enable_show "pci_p2pdma_enable_show") should be used as the show operation for
the attribute.

Returns 0 on success

ssize_t pci_p2pdma_enable_show(char \*page, struct pci_dev \*p2p_dev, bool use_p2pdma)
:   show a configfs/sysfs attribute indicating whether p2pdma is enabled

**Parameters**

`char *page`
:   contents of the stored value

`struct pci_dev *p2p_dev`
:   the selected p2p device (NULL if no device is selected)

`bool use_p2pdma`
:   whether p2pdma has been enabled

**Description**

Attributes that use [`pci_p2pdma_enable_store()`](p2pdma.md#c.pci_p2pdma_enable_store "pci_p2pdma_enable_store") should use this function
to show the value of the attribute.

Returns 0 on success
