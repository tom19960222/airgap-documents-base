---
collection: qemu
version: "11.1.0"
title: "PCI subsystem"
source_url: https://www.qemu.org/docs/master/devel/pci.html
fetched_at: 2026-08-21T03:25:55+00:00
---
# PCI subsystem

## API Reference

struct PCIIOMMUOps
:   callbacks structure for specific IOMMU handlers of a PCIBus

**Definition**:

```
struct PCIIOMMUOps {
    bool (*supports_address_space)(PCIBus *bus, void *opaque, int devfn, Error **errp);
    AddressSpace * (*get_address_space)(PCIBus *bus, void *opaque, int devfn);
    bool (*set_iommu_device)(PCIBus *bus, void *opaque, int devfn, HostIOMMUDevice *dev, Error **errp);
    void (*unset_iommu_device)(PCIBus *bus, void *opaque, int devfn);
    uint64_t (*get_viommu_flags)(void *opaque);
    uint64_t (*get_host_iommu_quirks)(uint32_t type, void *caps, uint32_t size);
    void (*get_iotlb_info)(void *opaque, uint8_t *addr_width, uint32_t *min_page_size);
    void (*init_iotlb_notifier)(PCIBus *bus, void *opaque, int devfn, IOMMUNotifier *n, IOMMUNotify fn, void *user_opaque);
    void (*register_iotlb_notifier)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid, IOMMUNotifier *n);
    void (*unregister_iotlb_notifier)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid, IOMMUNotifier *n);
    ssize_t (*ats_request_translation)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid, bool priv_req, bool exec_req, hwaddr addr, size_t length, bool no_write, IOMMUTLBEntry *result, size_t result_length, uint32_t *err_count);
    void (*pri_register_notifier)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid, IOMMUPRINotifier *notifier);
    void (*pri_unregister_notifier)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid);
    int (*pri_request_page)(PCIBus *bus, void *opaque, int devfn, uint32_t pasid, bool priv_req, bool exec_req, hwaddr addr, bool lpig, uint16_t prgi, bool is_read, bool is_write);
    uint64_t (*get_msi_direct_gpa)(PCIBus *bus, void *opaque, int devfn);
};
```

**Members**

`supports_address_space`
:   Optional pre-check to determine whether a PCI
    device can be associated with an IOMMU. If this callback returns true,
    the IOMMU accepts the device association and get_address_space() can be
    called to obtain the address_space to be used.

    **bus**: the `PCIBus` being accessed.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number.

    **errp**: pass an Error out only when return false

    Returns: true if the device can be associated with an IOMMU, false
    otherwise with errp set.

`get_address_space`
:   get the address space for a set of devices
    on a PCI bus.

    Mandatory callback which returns a pointer to an [`AddressSpace`](memory.md#c.AddressSpace "AddressSpace")

    **bus**: the `PCIBus` being accessed.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number

`set_iommu_device`
:   attach a HostIOMMUDevice to a vIOMMU

    Optional callback, if not implemented in vIOMMU, then vIOMMU can’t
    retrieve host information from the associated HostIOMMUDevice.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **dev**: the `HostIOMMUDevice` to attach.

    **errp**: pass an Error out only when return false

    Returns: true if HostIOMMUDevice is attached or else false with errp set.

`unset_iommu_device`
:   detach a HostIOMMUDevice from a vIOMMU

    Optional callback.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

`get_viommu_flags`
:   get vIOMMU flags

    Optional callback, if not implemented, then vIOMMU doesn’t support
    exposing flags to other sub-system, e.g., VFIO.

    **opaque**: the data passed to pci_setup_iommu().

    Returns: bitmap with each bit representing a vIOMMU flag defined in
    enum viommu_flags.

`get_host_iommu_quirks`
:   get host IOMMU quirks

    Optional callback, if not implemented, then vIOMMU doesn’t support
    converting **type** specific hardware information data into a standard
    bitmap format.

    **type**: IOMMU hardware info type

    **caps**: IOMMU **type** specific hardware information data

    **size**: size of **caps**

    Returns: bitmap with each bit representing a host IOMMU quirk defined in
    enum host_iommu_quirks

`get_iotlb_info`
:   get properties required to initialize a device IOTLB.

    Callback required if devices are allowed to cache translations.

    **opaque**: the data passed to pci_setup_iommu().

    **addr_width**: the address width of the IOMMU (output parameter).

    **min_page_size**: the page size of the IOMMU (output parameter).

`init_iotlb_notifier`
:   initialize an IOMMU notifier.

    Optional callback.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **n**: the notifier to be initialized.

    **fn**: the callback to be installed.

    **user_opaque**: a user pointer that can be used to track a state.

`register_iotlb_notifier`
:   setup an IOTLB invalidation notifier.

    Callback required if devices are allowed to cache translations.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to watch.

    **n**: the notifier to register.

`unregister_iotlb_notifier`
:   remove an IOTLB invalidation notifier.

    Callback required if devices are allowed to cache translations.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to stop watching.

    **n**: the notifier to unregister.

`ats_request_translation`
:   issue an ATS request.

    Callback required if devices are allowed to use the address
    translation service.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to use for the request.

    **priv_req**: privileged mode bit (PASID TLP).

    **exec_req**: execute request bit (PASID TLP).

    **addr**: start address of the memory range to be translated.

    **length**: length of the memory range in bytes.

    **no_write**: request a read-only translation (if supported).

    **result**: buffer in which the TLB entries will be stored.

    **result_length**: result buffer length.

    **err_count**: number of untranslated subregions.

    Returns: the number of translations stored in the result buffer, or
    -ENOMEM if the buffer is not large enough.

`pri_register_notifier`
:   setup the PRI completion callback.

    Callback required if devices are allowed to use the page request
    interface.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to track.

    **notifier**: the notifier to register.

`pri_unregister_notifier`
:   remove the PRI completion callback.

    Callback required if devices are allowed to use the page request
    interface.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to stop tracking.

`pri_request_page`
:   issue a PRI request.

    Callback required if devices are allowed to use the page request
    interface.

    **bus**: the `PCIBus` of the PCI device.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number of the PCI device.

    **pasid**: the pasid of the address space to use for the request.

    **priv_req**: privileged mode bit (PASID TLP).

    **exec_req**: execute request bit (PASID TLP).

    **addr**: untranslated address of the requested page.

    **lpig**: last page in group.

    **prgi**: page request group index.

    **is_read**: request read access.

    **is_write**: request write access.

`get_msi_direct_gpa`
:   get the guest physical address of MSI doorbell
    for the device on a PCI bus.

    Optional callback. If implemented, it must return a valid guest
    physical address for the MSI doorbell

    **bus**: the `PCIBus` being accessed.

    **opaque**: the data passed to pci_setup_iommu().

    **devfn**: device and function number

    Returns: the guest physical address of the MSI doorbell.

**Description**

Allows to modify the behavior of some IOMMU operations of the PCI
framework for a set of devices on a PCI bus.

uint64_t pci_device_get_viommu_flags(PCIDevice \*dev)
:   get vIOMMU flags.

**Parameters**

`PCIDevice *dev`
:   PCI device pointer.

**Return**

bitmap with each bit representing a vIOMMU flag defined in
enum viommu_flags. Or 0 if vIOMMU doesn’t report any.

uint64_t pci_device_get_host_iommu_quirks(PCIDevice \*dev, uint32_t type, void \*caps, uint32_t size)
:   get host IOMMU quirks.

**Parameters**

`PCIDevice *dev`
:   PCI device pointer.

`uint32_t type`
:   IOMMU hardware info type

`void *caps`
:   IOMMU **type** specific hardware information data

`uint32_t size`
:   size of **caps**

**Return**

bitmap with each bit representing a host IOMMU quirk defined in
enum host_iommu_quirks. Or 0 if vIOMMU doesn’t convert any.

int pci_iommu_get_iotlb_info(PCIDevice \*dev, uint8_t \*addr_width, uint32_t \*min_page_size)
:   get properties required to initialize a device IOTLB.

**Parameters**

`PCIDevice *dev`
:   the device that wants to get the information.

`uint8_t *addr_width`
:   the address width of the IOMMU (output parameter).

`uint32_t *min_page_size`
:   the page size of the IOMMU (output parameter).

**Description**

Returns 0 on success, or a negative errno otherwise.

int pci_iommu_init_iotlb_notifier(PCIDevice \*dev, IOMMUNotifier \*n, IOMMUNotify fn, void \*opaque)
:   initialize an IOMMU notifier.

**Parameters**

`PCIDevice *dev`
:   the device.

`IOMMUNotifier *n`
:   the notifier to be initialized.

`IOMMUNotify fn`
:   the callback to be installed.

`void *opaque`
:   a user pointer that can be used to track a state.

**Description**

This function is used by devices before registering an IOTLB notifier.

ssize_t pci_ats_request_translation(PCIDevice \*dev, uint32_t pasid, bool priv_req, bool exec_req, hwaddr addr, size_t length, bool no_write, IOMMUTLBEntry \*result, size_t result_length, uint32_t \*err_count)
:   perform an ATS request.

**Parameters**

`PCIDevice *dev`
:   the ATS-capable PCI device.

`uint32_t pasid`
:   the pasid of the address space in which the translation will be done.

`bool priv_req`
:   privileged mode bit (PASID TLP).

`bool exec_req`
:   execute request bit (PASID TLP).

`hwaddr addr`
:   start address of the memory range to be translated.

`size_t length`
:   length of the memory range in bytes.

`bool no_write`
:   request a read-only translation (if supported).

`IOMMUTLBEntry *result`
:   buffer in which the TLB entries will be stored.

`size_t result_length`
:   result buffer length.

`uint32_t *err_count`
:   number of untranslated subregions.

**Description**

Returns the number of translations stored in **result** in case of success,
a negative error code otherwise.
-ENOMEM is returned when the result buffer is not large enough to store
all the translations.

int pci_pri_request_page(PCIDevice \*dev, uint32_t pasid, bool priv_req, bool exec_req, hwaddr addr, bool lpig, uint16_t prgi, bool is_read, bool is_write)
:   perform a PRI request.

**Parameters**

`PCIDevice *dev`
:   the PRI-capable PCI device.

`uint32_t pasid`
:   the pasid of the address space in which the translation will be done.

`bool priv_req`
:   privileged mode bit (PASID TLP).

`bool exec_req`
:   execute request bit (PASID TLP).

`hwaddr addr`
:   untranslated address of the requested page.

`bool lpig`
:   last page in group.

`uint16_t prgi`
:   page request group index.

`bool is_read`
:   request read access.

`bool is_write`
:   request write access.

**Description**

Returns 0 if the PRI request has been sent to the guest OS,
an error code otherwise.

int pci_pri_register_notifier(PCIDevice \*dev, uint32_t pasid, IOMMUPRINotifier \*notifier)
:   register the PRI callback for a given address space.

**Parameters**

`PCIDevice *dev`
:   the PRI-capable PCI device.

`uint32_t pasid`
:   the pasid of the address space to track.

`IOMMUPRINotifier *notifier`
:   the notifier to register.

**Description**

Returns 0 on success, an error code otherwise.

void pci_pri_unregister_notifier(PCIDevice \*dev, uint32_t pasid)
:   remove the PRI callback from a given address space.

**Parameters**

`PCIDevice *dev`
:   the PRI-capable PCI device.

`uint32_t pasid`
:   the pasid of the address space to stop tracking.

int pci_iommu_register_iotlb_notifier(PCIDevice \*dev, uint32_t pasid, IOMMUNotifier \*n)
:   register a notifier for changes to IOMMU translation entries in a specific address space.

**Parameters**

`PCIDevice *dev`
:   the device that wants to get notified.

`uint32_t pasid`
:   the pasid of the address space to track.

`IOMMUNotifier *n`
:   the notifier to register.

**Description**

Returns 0 on success, or a negative errno otherwise.

int pci_iommu_unregister_iotlb_notifier(PCIDevice \*dev, uint32_t pasid, IOMMUNotifier \*n)
:   unregister a notifier that has been registered with pci_iommu_register_iotlb_notifier.

**Parameters**

`PCIDevice *dev`
:   the device that wants to stop notifications.

`uint32_t pasid`
:   the pasid of the address space to stop tracking.

`IOMMUNotifier *n`
:   the notifier to unregister.

**Description**

Returns 0 on success, or a negative errno otherwise.

void pci_setup_iommu(PCIBus \*bus, const [PCIIOMMUOps](pci.md#c.PCIIOMMUOps "PCIIOMMUOps") \*ops, void \*opaque)
:   Initialize specific IOMMU handlers for a PCIBus

**Parameters**

`PCIBus *bus`
:   the `PCIBus` being updated.

`const PCIIOMMUOps *ops`
:   the [`PCIIOMMUOps`](pci.md#c.PCIIOMMUOps "PCIIOMMUOps")

`void *opaque`
:   passed to callbacks of the **ops** structure.

**Description**

Let PCI host bridges define specific operations.

bool pci_setup_iommu_per_bus(PCIBus \*bus, const [PCIIOMMUOps](pci.md#c.PCIIOMMUOps "PCIIOMMUOps") \*ops, void \*opaque, Error \*\*errp)
:   Initialize specific IOMMU handlers for a PCIBus

**Parameters**

`PCIBus *bus`
:   the `PCIBus` being updated.

`const PCIIOMMUOps *ops`
:   the [`PCIIOMMUOps`](pci.md#c.PCIIOMMUOps "PCIIOMMUOps")

`void *opaque`
:   passed to callbacks of the **ops** structure.

`Error **errp`
:   error handle

**Description**

Similar to pci_setup_iommu but enforces that the iommu only protects
**bus** downstream end points and no other bus hierarchy

Returns false on failure with **errp** set, true on success
