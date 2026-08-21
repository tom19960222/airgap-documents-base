---
collection: kernel
version: "6.8"
title: "Device drivers infrastructure"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/infrastructure.html
fetched_at: 2026-08-21T03:30:28+00:00
---
# Device drivers infrastructure

## The Basic Device Driver-Model Structures

struct subsys_interface
:   interfaces to device functions

**Definition**:

```
struct subsys_interface {
    const char *name;
    const struct bus_type *subsys;
    struct list_head node;
    int (*add_dev)(struct device *dev, struct subsys_interface *sif);
    void (*remove_dev)(struct device *dev, struct subsys_interface *sif);
};
```

**Members**

`name`
:   name of the device function

`subsys`
:   subsystem of the devices to attach to

`node`
:   the list of functions registered at the subsystem

`add_dev`
:   device hookup to device function handler

`remove_dev`
:   device hookup to device function handler

**Description**

Simple interfaces attached to a subsystem. Multiple interfaces can
attach to a subsystem and its devices. Unlike drivers, they do not
exclusively claim or control devices. Interfaces usually represent
a specific functionality of a subsystem/class of devices.

struct device_attribute
:   Interface for exporting device attributes.

**Definition**:

```
struct device_attribute {
    struct attribute        attr;
    ssize_t (*show)(struct device *dev, struct device_attribute *attr, char *buf);
    ssize_t (*store)(struct device *dev, struct device_attribute *attr, const char *buf, size_t count);
};
```

**Members**

`attr`
:   sysfs attribute definition.

`show`
:   Show handler.

`store`
:   Store handler.

struct dev_ext_attribute
:   Exported device attribute with extra context.

**Definition**:

```
struct dev_ext_attribute {
    struct device_attribute attr;
    void *var;
};
```

**Members**

`attr`
:   Exported device attribute.

`var`
:   Pointer to context.

DEVICE_ATTR

`DEVICE_ATTR (_name, _mode, _show, _store)`

> Define a device attribute.

**Parameters**

`_name`
:   Attribute name.

`_mode`
:   File mode.

`_show`
:   Show handler. Optional, but mandatory if attribute is readable.

`_store`
:   Store handler. Optional, but mandatory if attribute is writable.

**Description**

Convenience macro for defining a [`struct device_attribute`](infrastructure.md#c.device_attribute "device_attribute").

For example, `DEVICE_ATTR(foo, 0644, foo_show, foo_store);` expands to:

```c
struct device_attribute dev_attr_foo = {
        .attr   = { .name = "foo", .mode = 0644 },
        .show   = foo_show,
        .store  = foo_store,
};
```

DEVICE_ATTR_PREALLOC

`DEVICE_ATTR_PREALLOC (_name, _mode, _show, _store)`

> Define a preallocated device attribute.

**Parameters**

`_name`
:   Attribute name.

`_mode`
:   File mode.

`_show`
:   Show handler. Optional, but mandatory if attribute is readable.

`_store`
:   Store handler. Optional, but mandatory if attribute is writable.

**Description**

Like [`DEVICE_ATTR()`](infrastructure.md#c.DEVICE_ATTR "DEVICE_ATTR"), but `SYSFS_PREALLOC` is set on **_mode**.

DEVICE_ATTR_RW

`DEVICE_ATTR_RW (_name)`

> Define a read-write device attribute.

**Parameters**

`_name`
:   Attribute name.

**Description**

Like [`DEVICE_ATTR()`](infrastructure.md#c.DEVICE_ATTR "DEVICE_ATTR"), but **_mode** is 0644, **_show** is <_name>_show,
and **_store** is <_name>_store.

DEVICE_ATTR_ADMIN_RW

`DEVICE_ATTR_ADMIN_RW (_name)`

> Define an admin-only read-write device attribute.

**Parameters**

`_name`
:   Attribute name.

**Description**

Like [`DEVICE_ATTR_RW()`](infrastructure.md#c.DEVICE_ATTR_RW "DEVICE_ATTR_RW"), but **_mode** is 0600.

DEVICE_ATTR_RO

`DEVICE_ATTR_RO (_name)`

> Define a readable device attribute.

**Parameters**

`_name`
:   Attribute name.

**Description**

Like [`DEVICE_ATTR()`](infrastructure.md#c.DEVICE_ATTR "DEVICE_ATTR"), but **_mode** is 0444 and **_show** is <_name>_show.

DEVICE_ATTR_ADMIN_RO

`DEVICE_ATTR_ADMIN_RO (_name)`

> Define an admin-only readable device attribute.

**Parameters**

`_name`
:   Attribute name.

**Description**

Like [`DEVICE_ATTR_RO()`](infrastructure.md#c.DEVICE_ATTR_RO "DEVICE_ATTR_RO"), but **_mode** is 0400.

DEVICE_ATTR_WO

`DEVICE_ATTR_WO (_name)`

> Define an admin-only writable device attribute.

**Parameters**

`_name`
:   Attribute name.

**Description**

Like [`DEVICE_ATTR()`](infrastructure.md#c.DEVICE_ATTR "DEVICE_ATTR"), but **_mode** is 0200 and **_store** is <_name>_store.

DEVICE_ULONG_ATTR

`DEVICE_ULONG_ATTR (_name, _mode, _var)`

> Define a device attribute backed by an unsigned long.

**Parameters**

`_name`
:   Attribute name.

`_mode`
:   File mode.

`_var`
:   Identifier of unsigned long.

**Description**

Like [`DEVICE_ATTR()`](infrastructure.md#c.DEVICE_ATTR "DEVICE_ATTR"), but **_show** and **_store** are automatically provided
such that reads and writes to the attribute from userspace affect **_var**.

DEVICE_INT_ATTR

`DEVICE_INT_ATTR (_name, _mode, _var)`

> Define a device attribute backed by an int.

**Parameters**

`_name`
:   Attribute name.

`_mode`
:   File mode.

`_var`
:   Identifier of int.

**Description**

Like [`DEVICE_ULONG_ATTR()`](infrastructure.md#c.DEVICE_ULONG_ATTR "DEVICE_ULONG_ATTR"), but **_var** is an int.

DEVICE_BOOL_ATTR

`DEVICE_BOOL_ATTR (_name, _mode, _var)`

> Define a device attribute backed by a bool.

**Parameters**

`_name`
:   Attribute name.

`_mode`
:   File mode.

`_var`
:   Identifier of bool.

**Description**

Like [`DEVICE_ULONG_ATTR()`](infrastructure.md#c.DEVICE_ULONG_ATTR "DEVICE_ULONG_ATTR"), but **_var** is a bool.

devm_alloc_percpu

`devm_alloc_percpu (dev, type)`

> Resource-managed alloc_percpu

**Parameters**

`dev`
:   Device to allocate per-cpu memory for

`type`
:   Type to allocate per-cpu memory for

**Description**

Managed alloc_percpu. Per-cpu memory allocated with this function is
automatically freed on driver detach.

**Return**

Pointer to allocated memory on success, NULL on failure.

enum dl_dev_state
:   Device driver presence tracking information.

**Constants**

`DL_DEV_NO_DRIVER`
:   There is no driver attached to the device.

`DL_DEV_PROBING`
:   A driver is probing.

`DL_DEV_DRIVER_BOUND`
:   The driver has been bound to the device.

`DL_DEV_UNBINDING`
:   The driver is unbinding from the device.

enum device_removable
:   Whether the device is removable. The criteria for a device to be classified as removable is determined by its subsystem or bus.

**Constants**

`DEVICE_REMOVABLE_NOT_SUPPORTED`
:   This attribute is not supported for this
    device (default).

`DEVICE_REMOVABLE_UNKNOWN`
:   Device location is Unknown.

`DEVICE_FIXED`
:   Device is not removable by the user.

`DEVICE_REMOVABLE`
:   Device is removable by the user.

struct dev_links_info
:   Device data related to device links.

**Definition**:

```
struct dev_links_info {
    struct list_head suppliers;
    struct list_head consumers;
    struct list_head defer_sync;
    enum dl_dev_state status;
};
```

**Members**

`suppliers`
:   List of links to supplier devices.

`consumers`
:   List of links to consumer devices.

`defer_sync`
:   Hook to global list of devices that have deferred sync_state.

`status`
:   Driver status information.

struct dev_msi_info
:   Device data related to MSI

**Definition**:

```
struct dev_msi_info {
#ifdef CONFIG_GENERIC_MSI_IRQ;
    struct irq_domain       *domain;
    struct msi_device_data  *data;
#endif;
};
```

**Members**

`domain`
:   The MSI interrupt domain associated to the device

`data`
:   Pointer to MSI device data

enum device_physical_location_panel
:   Describes which panel surface of the system's housing the device connection point resides on.

**Constants**

`DEVICE_PANEL_TOP`
:   Device connection point is on the top panel.

`DEVICE_PANEL_BOTTOM`
:   Device connection point is on the bottom panel.

`DEVICE_PANEL_LEFT`
:   Device connection point is on the left panel.

`DEVICE_PANEL_RIGHT`
:   Device connection point is on the right panel.

`DEVICE_PANEL_FRONT`
:   Device connection point is on the front panel.

`DEVICE_PANEL_BACK`
:   Device connection point is on the back panel.

`DEVICE_PANEL_UNKNOWN`
:   The panel with device connection point is unknown.

enum device_physical_location_vertical_position
:   Describes vertical position of the device connection point on the panel surface.

**Constants**

`DEVICE_VERT_POS_UPPER`
:   Device connection point is at upper part of panel.

`DEVICE_VERT_POS_CENTER`
:   Device connection point is at center part of panel.

`DEVICE_VERT_POS_LOWER`
:   Device connection point is at lower part of panel.

enum device_physical_location_horizontal_position
:   Describes horizontal position of the device connection point on the panel surface.

**Constants**

`DEVICE_HORI_POS_LEFT`
:   Device connection point is at left part of panel.

`DEVICE_HORI_POS_CENTER`
:   Device connection point is at center part of panel.

`DEVICE_HORI_POS_RIGHT`
:   Device connection point is at right part of panel.

struct device_physical_location
:   Device data related to physical location of the device connection point.

**Definition**:

```
struct device_physical_location {
    enum device_physical_location_panel panel;
    enum device_physical_location_vertical_position vertical_position;
    enum device_physical_location_horizontal_position horizontal_position;
    bool dock;
    bool lid;
};
```

**Members**

`panel`
:   Panel surface of the system's housing that the device connection
    point resides on.

`vertical_position`
:   Vertical position of the device connection point within
    the panel.

`horizontal_position`
:   Horizontal position of the device connection point
    within the panel.

`dock`
:   Set if the device connection point resides in a docking station or
    port replicator.

`lid`
:   Set if this device connection point resides on the lid of laptop
    system.

struct device
:   The basic device structure

**Definition**:

```
struct device {
    struct kobject kobj;
    struct device           *parent;
    struct device_private   *p;
    const char              *init_name;
    const struct device_type *type;
    const struct bus_type   *bus;
    struct device_driver *driver;
    void *platform_data;
    void *driver_data;
    struct mutex            mutex;
    struct dev_links_info   links;
    struct dev_pm_info      power;
    struct dev_pm_domain    *pm_domain;
#ifdef CONFIG_ENERGY_MODEL;
    struct em_perf_domain   *em_pd;
#endif;
#ifdef CONFIG_PINCTRL;
    struct dev_pin_info     *pins;
#endif;
    struct dev_msi_info     msi;
#ifdef CONFIG_DMA_OPS;
    const struct dma_map_ops *dma_ops;
#endif;
    u64 *dma_mask;
    u64 coherent_dma_mask;
    u64 bus_dma_limit;
    const struct bus_dma_region *dma_range_map;
    struct device_dma_parameters *dma_parms;
    struct list_head        dma_pools;
#ifdef CONFIG_DMA_DECLARE_COHERENT;
    struct dma_coherent_mem *dma_mem;
#endif;
#ifdef CONFIG_DMA_CMA;
    struct cma *cma_area;
#endif;
#ifdef CONFIG_SWIOTLB;
    struct io_tlb_mem *dma_io_tlb_mem;
#endif;
#ifdef CONFIG_SWIOTLB_DYNAMIC;
    struct list_head dma_io_tlb_pools;
    spinlock_t dma_io_tlb_lock;
    bool dma_uses_io_tlb;
#endif;
    struct dev_archdata     archdata;
    struct device_node      *of_node;
    struct fwnode_handle    *fwnode;
#ifdef CONFIG_NUMA;
    int numa_node;
#endif;
    dev_t devt;
    u32 id;
    spinlock_t devres_lock;
    struct list_head        devres_head;
    const struct class      *class;
    const struct attribute_group **groups;
    void (*release)(struct device *dev);
    struct iommu_group      *iommu_group;
    struct dev_iommu        *iommu;
    struct device_physical_location *physical_location;
    enum device_removable   removable;
    bool offline_disabled:1;
    bool offline:1;
    bool of_node_reused:1;
    bool state_synced:1;
    bool can_match:1;
#if defined(CONFIG_ARCH_HAS_SYNC_DMA_FOR_DEVICE) ||     defined(CONFIG_ARCH_HAS_SYNC_DMA_FOR_CPU) ||     defined(CONFIG_ARCH_HAS_SYNC_DMA_FOR_CPU_ALL);
    bool dma_coherent:1;
#endif;
#ifdef CONFIG_DMA_OPS_BYPASS;
    bool dma_ops_bypass : 1;
#endif;
};
```

**Members**

`kobj`
:   A top-level, abstract class from which other classes are derived.

`parent`
:   The device's "parent" device, the device to which it is attached.
    In most cases, a parent device is some sort of bus or host
    controller. If parent is NULL, the device, is a top-level device,
    which is not usually what you want.

`p`
:   Holds the private data of the driver core portions of the device.
    See the comment of the struct device_private for detail.

`init_name`
:   Initial name of the device.

`type`
:   The type of device.
    This identifies the device type and carries type-specific
    information.

`bus`
:   Type of bus device is on.

`driver`
:   Which driver has allocated this

`platform_data`
:   Platform data specific to the device.

`driver_data`
:   Private pointer for driver specific info.

`mutex`
:   Mutex to synchronize calls to its driver.

`links`
:   Links to suppliers and consumers of this device.

`power`
:   For device power management.
    See [Device Power Management Basics](pm/devices.md) for details.

`pm_domain`
:   Provide callbacks that are executed during system suspend,
    hibernation, system resume and during runtime PM transitions
    along with subsystem-level and driver-level callbacks.

`em_pd`
:   device's energy model performance domain

`pins`
:   For device pin management.
    See [PINCTRL (PIN CONTROL) subsystem](pin-control.md) for details.

`msi`
:   MSI related data

`dma_ops`
:   DMA mapping operations for this device.

`dma_mask`
:   Dma mask (if dma'ble device).

`coherent_dma_mask`
:   Like dma_mask, but for alloc_coherent mapping as not all
    hardware supports 64-bit addresses for consistent allocations
    such descriptors.

`bus_dma_limit`
:   Limit of an upstream bridge or bus which imposes a smaller
    DMA limit than the device itself supports.

`dma_range_map`
:   map for DMA memory ranges relative to that of RAM

`dma_parms`
:   A low level driver may set these to teach IOMMU code about
    segment limitations.

`dma_pools`
:   Dma pools (if dma'ble device).

`dma_mem`
:   Internal for coherent mem override.

`cma_area`
:   Contiguous memory area for dma allocations

`dma_io_tlb_mem`
:   Software IO TLB allocator. Not for driver use.

`dma_io_tlb_pools`
:   List of transient swiotlb memory pools.

`dma_io_tlb_lock`
:   Protects changes to the list of active pools.

`dma_uses_io_tlb`
:   `true` if device has used the software IO TLB.

`archdata`
:   For arch-specific additions.

`of_node`
:   Associated device tree node.

`fwnode`
:   Associated device node supplied by platform firmware.

`numa_node`
:   NUMA node this device is close to.

`devt`
:   For creating the sysfs "dev".

`id`
:   device instance

`devres_lock`
:   Spinlock to protect the resource of the device.

`devres_head`
:   The resources list of the device.

`class`
:   The class of the device.

`groups`
:   Optional attribute groups.

`release`
:   Callback to free the device after all references have
    gone away. This should be set by the allocator of the
    device (i.e. the bus driver that discovered the device).

`iommu_group`
:   IOMMU group the device belongs to.

`iommu`
:   Per device generic IOMMU runtime data

`physical_location`
:   Describes physical location of the device connection
    point in the system housing.

`removable`
:   Whether the device can be removed from the system. This
    should be set by the subsystem / bus driver that discovered
    the device.

`offline_disabled`
:   If set, the device is permanently online.

`offline`
:   Set after successful invocation of bus type's .offline().

`of_node_reused`
:   Set if the device-tree node is shared with an ancestor
    device.

`state_synced`
:   The hardware state of this device has been synced to match
    the software state of this device by calling the driver/bus
    sync_state() callback.

`can_match`
:   The device has matched with a driver at least once or it is in
    a bus (like AMBA) which can't check for matching drivers until
    other devices probe successfully.

`dma_coherent`
:   this particular device is dma coherent, even if the
    architecture supports non-coherent devices.

`dma_ops_bypass`
:   If set to `true` then the dma_ops are bypassed for the
    streaming DMA operations (->map_\* / ->unmap_\* / ->sync_\*),
    and optionall (if the coherent mask is large enough) also
    for dma allocations. This flag is managed by the dma ops
    instance from ->dma_supported.

**Example**

For devices on custom boards, as typical of embedded
:   and SOC based hardware, Linux often uses platform_data to point
    to board-specific structures describing devices and how they
    are wired. That can include what ports are available, chip
    variants, which GPIO pins act in what additional roles, and so
    on. This shrinks the "Board Support Packages" (BSPs) and
    minimizes board-specific #ifdefs in drivers.

**Description**

At the lowest level, every device in a Linux system is represented by an
instance of [`struct device`](infrastructure.md#c.device "device"). The device structure contains the information
that the device model core needs to model the system. Most subsystems,
however, track additional information about the devices they host. As a
result, it is rare for devices to be represented by bare device structures;
instead, that structure, like kobject structures, is usually embedded within
a higher-level representation of the device.

struct device_link
:   Device link representation.

**Definition**:

```
struct device_link {
    struct device *supplier;
    struct list_head s_node;
    struct device *consumer;
    struct list_head c_node;
    struct device link_dev;
    enum device_link_state status;
    u32 flags;
    refcount_t rpm_active;
    struct kref kref;
    struct work_struct rm_work;
    bool supplier_preactivated;
};
```

**Members**

`supplier`
:   The device on the supplier end of the link.

`s_node`
:   Hook to the supplier device's list of links to consumers.

`consumer`
:   The device on the consumer end of the link.

`c_node`
:   Hook to the consumer device's list of links to suppliers.

`link_dev`
:   device used to expose link details in sysfs

`status`
:   The state of the link (with respect to the presence of drivers).

`flags`
:   Link flags.

`rpm_active`
:   Whether or not the consumer device is runtime-PM-active.

`kref`
:   Count repeated addition of the same link.

`rm_work`
:   Work structure used for removing the link.

`supplier_preactivated`
:   Supplier has been made active before consumer probe.

bool device_iommu_mapped(struct [device](infrastructure.md#c.device "device") \*dev)
:   Returns true when the device DMA is translated by an IOMMU

**Parameters**

`struct device *dev`
:   Device to perform the check on

const char \*dev_name(const struct [device](infrastructure.md#c.device "device") \*dev)
:   Return a device's name.

**Parameters**

`const struct device *dev`
:   Device with name to get.

**Return**

The kobject name of the device, or its initial name if unavailable.

const char \*dev_bus_name(const struct [device](infrastructure.md#c.device "device") \*dev)
:   Return a device's bus/class name, if at all possible

**Parameters**

`const struct device *dev`
:   [`struct device`](infrastructure.md#c.device "device") to get the bus/class name of

**Description**

Will return the name of the bus/class the device is attached to. If it is
not attached to a bus/class, an empty string will be returned.

device_lock_set_class

`device_lock_set_class (dev, key)`

> Specify a temporary lock class while a device is attached to a driver

**Parameters**

`dev`
:   device to modify

`key`
:   lock class key data

**Description**

This must be called with the device_lock() already held, for example
from driver ->probe(). Take care to only override the default
lockdep_no_validate class.

device_lock_reset_class

`device_lock_reset_class (dev)`

> Return a device to the default lockdep novalidate state

**Parameters**

`dev`
:   device to modify

**Description**

This must be called with the device_lock() already held, for example
from driver ->remove().

struct bus_type
:   The bus type of the device

**Definition**:

```
struct bus_type {
    const char              *name;
    const char              *dev_name;
    const struct attribute_group **bus_groups;
    const struct attribute_group **dev_groups;
    const struct attribute_group **drv_groups;
    int (*match)(struct device *dev, struct device_driver *drv);
    int (*uevent)(const struct device *dev, struct kobj_uevent_env *env);
    int (*probe)(struct device *dev);
    void (*sync_state)(struct device *dev);
    void (*remove)(struct device *dev);
    void (*shutdown)(struct device *dev);
    int (*online)(struct device *dev);
    int (*offline)(struct device *dev);
    int (*suspend)(struct device *dev, pm_message_t state);
    int (*resume)(struct device *dev);
    int (*num_vf)(struct device *dev);
    int (*dma_configure)(struct device *dev);
    void (*dma_cleanup)(struct device *dev);
    const struct dev_pm_ops *pm;
    bool need_parent_lock;
};
```

**Members**

`name`
:   The name of the bus.

`dev_name`
:   Used for subsystems to enumerate devices like ("foo``u``", dev->id).

`bus_groups`
:   Default attributes of the bus.

`dev_groups`
:   Default attributes of the devices on the bus.

`drv_groups`
:   Default attributes of the device drivers on the bus.

`match`
:   Called, perhaps multiple times, whenever a new device or driver
    is added for this bus. It should return a positive value if the
    given device can be handled by the given driver and zero
    otherwise. It may also return error code if determining that
    the driver supports the device is not possible. In case of
    -EPROBE_DEFER it will queue the device for deferred probing.

`uevent`
:   Called when a device is added, removed, or a few other things
    that generate uevents to add the environment variables.

`probe`
:   Called when a new device or driver add to this bus, and callback
    the specific driver's probe to initial the matched device.

`sync_state`
:   Called to sync device state to software state after all the
    state tracking consumers linked to this device (present at
    the time of late_initcall) have successfully bound to a
    driver. If the device has no consumers, this function will
    be called at late_initcall_sync level. If the device has
    consumers that are never bound to a driver, this function
    will never get called until they do.

`remove`
:   Called when a device removed from this bus.

`shutdown`
:   Called at shut-down time to quiesce the device.

`online`
:   Called to put the device back online (after offlining it).

`offline`
:   Called to put the device offline for hot-removal. May fail.

`suspend`
:   Called when a device on this bus wants to go to sleep mode.

`resume`
:   Called to bring a device on this bus out of sleep mode.

`num_vf`
:   Called to find out how many virtual functions a device on this
    bus supports.

`dma_configure`
:   Called to setup DMA configuration on a device on
    this bus.

`dma_cleanup`
:   Called to cleanup DMA configuration on a device on
    this bus.

`pm`
:   Power management operations of this bus, callback the specific
    device driver's pm-ops.

`need_parent_lock`
:   When probing or removing a device on this bus, the
    device core should lock the device's parent.

**Description**

A bus is a channel between the processor and one or more devices. For the
purposes of the device model, all devices are connected via a bus, even if
it is an internal, virtual, "platform" bus. Buses can plug into each other.
A USB controller is usually a PCI device, for example. The device model
represents the actual connections between buses and the devices they control.
A bus is represented by the bus_type structure. It contains the name, the
default attributes, the bus' methods, PM operations, and the driver core's
private data.

enum bus_notifier_event
:   Bus Notifier events that have happened

**Constants**

`BUS_NOTIFY_ADD_DEVICE`
:   device is added to this bus

`BUS_NOTIFY_DEL_DEVICE`
:   device is about to be removed from this bus

`BUS_NOTIFY_REMOVED_DEVICE`
:   device is successfully removed from this bus

`BUS_NOTIFY_BIND_DRIVER`
:   a driver is about to be bound to this device on this bus

`BUS_NOTIFY_BOUND_DRIVER`
:   a driver is successfully bound to this device on this bus

`BUS_NOTIFY_UNBIND_DRIVER`
:   a driver is about to be unbound from this device on this bus

`BUS_NOTIFY_UNBOUND_DRIVER`
:   a driver is successfully unbound from this device on this bus

`BUS_NOTIFY_DRIVER_NOT_BOUND`
:   a driver failed to be bound to this device on this bus

**Description**

These are the value passed to a bus notifier when a specific event happens.

Note that bus notifiers are likely to be called with the device lock already
held by the driver core, so be careful in any notifier callback as to what
you do with the device structure.

All bus notifiers are called with the target [`struct device`](infrastructure.md#c.device "device") \* as an argument.

struct class
:   device classes

**Definition**:

```
struct class {
    const char              *name;
    const struct attribute_group    **class_groups;
    const struct attribute_group    **dev_groups;
    int (*dev_uevent)(const struct device *dev, struct kobj_uevent_env *env);
    char *(*devnode)(const struct device *dev, umode_t *mode);
    void (*class_release)(const struct class *class);
    void (*dev_release)(struct device *dev);
    int (*shutdown_pre)(struct device *dev);
    const struct kobj_ns_type_operations *ns_type;
    const void *(*namespace)(const struct device *dev);
    void (*get_ownership)(const struct device *dev, kuid_t *uid, kgid_t *gid);
    const struct dev_pm_ops *pm;
};
```

**Members**

`name`
:   Name of the class.

`class_groups`
:   Default attributes of this class.

`dev_groups`
:   Default attributes of the devices that belong to the class.

`dev_uevent`
:   Called when a device is added, removed from this class, or a
    few other things that generate uevents to add the environment
    variables.

`devnode`
:   Callback to provide the devtmpfs.

`class_release`
:   Called to release this class.

`dev_release`
:   Called to release the device.

`shutdown_pre`
:   Called at shut-down time before driver shutdown.

`ns_type`
:   Callbacks so sysfs can detemine namespaces.

`namespace`
:   Namespace of the device belongs to this class.

`get_ownership`
:   Allows class to specify uid/gid of the sysfs directories
    for the devices belonging to the class. Usually tied to
    device's namespace.

`pm`
:   The default device power management operations of this class.

**Description**

A class is a higher-level view of a device that abstracts out low-level
implementation details. Drivers may see a SCSI disk or an ATA disk, but,
at the class level, they are all simply disks. Classes allow user space
to work with devices based on what they do, rather than how they are
connected or how they work.

enum probe_type
:   device driver probe type to try Device drivers may opt in for special handling of their respective probe routines. This tells the core what to expect and prefer.

**Constants**

`PROBE_DEFAULT_STRATEGY`
:   Used by drivers that work equally well
    whether probed synchronously or asynchronously.

`PROBE_PREFER_ASYNCHRONOUS`
:   Drivers for "slow" devices which
    probing order is not essential for booting the system may
    opt into executing their probes asynchronously.

`PROBE_FORCE_SYNCHRONOUS`
:   Use this to annotate drivers that need
    their probe routines to run synchronously with driver and
    device registration (with the exception of -EPROBE_DEFER
    handling - re-probing always ends up being done asynchronously).

**Description**

Note that the end goal is to switch the kernel to use asynchronous
probing by default, so annotating drivers with
`PROBE_PREFER_ASYNCHRONOUS` is a temporary measure that allows us
to speed up boot process while we are validating the rest of the
drivers.

struct device_driver
:   The basic device driver structure

**Definition**:

```
struct device_driver {
    const char              *name;
    const struct bus_type   *bus;
    struct module           *owner;
    const char              *mod_name;
    bool suppress_bind_attrs;
    enum probe_type probe_type;
    const struct of_device_id       *of_match_table;
    const struct acpi_device_id     *acpi_match_table;
    int (*probe) (struct device *dev);
    void (*sync_state)(struct device *dev);
    int (*remove) (struct device *dev);
    void (*shutdown) (struct device *dev);
    int (*suspend) (struct device *dev, pm_message_t state);
    int (*resume) (struct device *dev);
    const struct attribute_group **groups;
    const struct attribute_group **dev_groups;
    const struct dev_pm_ops *pm;
    void (*coredump) (struct device *dev);
    struct driver_private *p;
};
```

**Members**

`name`
:   Name of the device driver.

`bus`
:   The bus which the device of this driver belongs to.

`owner`
:   The module owner.

`mod_name`
:   Used for built-in modules.

`suppress_bind_attrs`
:   Disables bind/unbind via sysfs.

`probe_type`
:   Type of the probe (synchronous or asynchronous) to use.

`of_match_table`
:   The open firmware table.

`acpi_match_table`
:   The ACPI match table.

`probe`
:   Called to query the existence of a specific device,
    whether this driver can work with it, and bind the driver
    to a specific device.

`sync_state`
:   Called to sync device state to software state after all the
    state tracking consumers linked to this device (present at
    the time of late_initcall) have successfully bound to a
    driver. If the device has no consumers, this function will
    be called at late_initcall_sync level. If the device has
    consumers that are never bound to a driver, this function
    will never get called until they do.

`remove`
:   Called when the device is removed from the system to
    unbind a device from this driver.

`shutdown`
:   Called at shut-down time to quiesce the device.

`suspend`
:   Called to put the device to sleep mode. Usually to a
    low power state.

`resume`
:   Called to bring a device from sleep mode.

`groups`
:   Default attributes that get created by the driver core
    automatically.

`dev_groups`
:   Additional attributes attached to device instance once
    it is bound to the driver.

`pm`
:   Power management operations of the device which matched
    this driver.

`coredump`
:   Called when sysfs entry is written to. The device driver
    is expected to call the dev_coredump API resulting in a
    uevent.

`p`
:   Driver core's private data, no one other than the driver
    core can touch this.

**Description**

The device driver-model tracks all of the drivers known to the system.
The main reason for this tracking is to enable the driver core to match
up drivers with new devices. Once drivers are known objects within the
system, however, a number of other things become possible. Device drivers
can export information and configuration variables that are independent
of any specific device.

## Device Drivers Base

void driver_init(void)
:   initialize driver model.

**Parameters**

`void`
:   no arguments

**Description**

Call the driver model init functions to initialize their
subsystems. Called early from init/main.c.

struct [device](infrastructure.md#c.device "device") \*driver_find_device_by_name(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const char \*name)
:   device iterator for locating a particular device of a specific name.

**Parameters**

`struct device_driver *drv`
:   the driver we're iterating

`const char *name`
:   name of the device to match

struct [device](infrastructure.md#c.device "device") \*driver_find_device_by_of_node(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const struct device_node \*np)
:   device iterator for locating a particular device by of_node pointer.

**Parameters**

`struct device_driver *drv`
:   the driver we're iterating

`const struct device_node *np`
:   of_node pointer to match.

struct [device](infrastructure.md#c.device "device") \*driver_find_device_by_fwnode(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const struct fwnode_handle \*fwnode)
:   device iterator for locating a particular device by fwnode pointer.

**Parameters**

`struct device_driver *drv`
:   the driver we're iterating

`const struct fwnode_handle *fwnode`
:   fwnode pointer to match.

struct [device](infrastructure.md#c.device "device") \*driver_find_device_by_devt(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, dev_t devt)
:   device iterator for locating a particular device by devt.

**Parameters**

`struct device_driver *drv`
:   the driver we're iterating

`dev_t devt`
:   devt pointer to match.

struct [device](infrastructure.md#c.device "device") \*driver_find_device_by_acpi_dev(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const struct acpi_device \*adev)
:   device iterator for locating a particular device matching the ACPI_COMPANION device.

**Parameters**

`struct device_driver *drv`
:   the driver we're iterating

`const struct acpi_device *adev`
:   ACPI_COMPANION device to match.

module_driver

`module_driver (__driver, __register, __unregister, ...)`

> Helper macro for drivers that don't do anything special in module init/exit. This eliminates a lot of boilerplate. Each module may only use this macro once, and calling it replaces [`module_init()`](basics.md#c.module_init "module_init") and [`module_exit()`](basics.md#c.module_exit "module_exit").

**Parameters**

`__driver`
:   driver name

`__register`
:   register function for this driver type

`__unregister`
:   unregister function for this driver type

`...`
:   Additional arguments to be passed to __register and __unregister.

**Description**

Use this macro to construct bus specific macros for registering
drivers, and do not use it on its own.

builtin_driver

`builtin_driver (__driver, __register, ...)`

> Helper macro for drivers that don't do anything special in init and have no exit. This eliminates some boilerplate. Each driver may only use this macro once, and calling it replaces device_initcall (or in some cases, the legacy __initcall). This is meant to be a direct parallel of [`module_driver()`](infrastructure.md#c.module_driver "module_driver") above but without the __exit stuff that is not used for builtin cases.

**Parameters**

`__driver`
:   driver name

`__register`
:   register function for this driver type

`...`
:   Additional arguments to be passed to __register

**Description**

Use this macro to construct bus specific macros for registering
drivers, and do not use it on its own.

int driver_set_override(struct [device](infrastructure.md#c.device "device") \*dev, const char \*\*override, const char \*s, size_t len)
:   Helper to set or clear driver override.

**Parameters**

`struct device *dev`
:   Device to change

`const char **override`
:   Address of string to change (e.g. [`device->driver_override`](infrastructure.md#c.device "device"));
    The contents will be freed and hold newly allocated override.

`const char *s`
:   NUL-terminated string, new driver name to force a match, pass empty
    string to clear it ("" or "n", where the latter is only for sysfs
    interface).

`size_t len`
:   length of **s**

**Description**

Helper to set or clear driver override in a device, intended for the cases
when the driver_override field is allocated by driver/bus code.

**Return**

0 on success or a negative error code on failure.

int driver_for_each_device(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, struct [device](infrastructure.md#c.device "device") \*start, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device")\*, void\*))
:   Iterator for devices bound to a driver.

**Parameters**

`struct device_driver *drv`
:   Driver we're iterating.

`struct device *start`
:   Device to begin with

`void *data`
:   Data to pass to the callback.

`int (*fn)(struct device *, void *)`
:   Function to call for each device.

**Description**

Iterate over the **drv**'s list of devices calling **fn** for each one.

struct [device](infrastructure.md#c.device "device") \*driver_find_device(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, struct [device](infrastructure.md#c.device "device") \*start, const void \*data, int (\*match)(struct [device](infrastructure.md#c.device "device") \*dev, const void \*data))
:   device iterator for locating a particular device.

**Parameters**

`struct device_driver *drv`
:   The device's driver

`struct device *start`
:   Device to begin with

`const void *data`
:   Data to pass to match function

`int (*match)(struct device *dev, const void *data)`
:   Callback function to check device

**Description**

This is similar to the [`driver_for_each_device()`](infrastructure.md#c.driver_for_each_device "driver_for_each_device") function above, but
it returns a reference to a device that is 'found' for later use, as
determined by the **match** callback.

The callback should return 0 if the device doesn't match and non-zero
if it does. If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

int driver_create_file(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const struct driver_attribute \*attr)
:   create sysfs file for driver.

**Parameters**

`struct device_driver *drv`
:   driver.

`const struct driver_attribute *attr`
:   driver attribute descriptor.

void driver_remove_file(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, const struct driver_attribute \*attr)
:   remove sysfs file for driver.

**Parameters**

`struct device_driver *drv`
:   driver.

`const struct driver_attribute *attr`
:   driver attribute descriptor.

int driver_register(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv)
:   register driver with bus

**Parameters**

`struct device_driver *drv`
:   driver to register

**Description**

We pass off most of the work to the bus_add_driver() call,
since most of the things we have to do deal with the bus
structures.

void driver_unregister(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv)
:   remove driver from system.

**Parameters**

`struct device_driver *drv`
:   driver.

**Description**

Again, we pass off most of the work to the bus-level call.

struct [device_link](infrastructure.md#c.device_link "device_link") \*device_link_add(struct [device](infrastructure.md#c.device "device") \*consumer, struct [device](infrastructure.md#c.device "device") \*supplier, u32 flags)
:   Create a link between two devices.

**Parameters**

`struct device *consumer`
:   Consumer end of the link.

`struct device *supplier`
:   Supplier end of the link.

`u32 flags`
:   Link flags.

**Description**

The caller is responsible for the proper synchronization of the link creation
with runtime PM. First, setting the DL_FLAG_PM_RUNTIME flag will cause the
runtime PM framework to take the link into account. Second, if the
DL_FLAG_RPM_ACTIVE flag is set in addition to it, the supplier devices will
be forced into the active meta state and reference-counted upon the creation
of the link. If DL_FLAG_PM_RUNTIME is not set, DL_FLAG_RPM_ACTIVE will be
ignored.

If DL_FLAG_STATELESS is set in **flags**, the caller of this function is
expected to release the link returned by it directly with the help of either
[`device_link_del()`](infrastructure.md#c.device_link_del "device_link_del") or [`device_link_remove()`](infrastructure.md#c.device_link_remove "device_link_remove").

If that flag is not set, however, the caller of this function is handing the
management of the link over to the driver core entirely and its return value
can only be used to check whether or not the link is present. In that case,
the DL_FLAG_AUTOREMOVE_CONSUMER and DL_FLAG_AUTOREMOVE_SUPPLIER device link
flags can be used to indicate to the driver core when the link can be safely
deleted. Namely, setting one of them in **flags** indicates to the driver core
that the link is not going to be used (by the given caller of this function)
after unbinding the consumer or supplier driver, respectively, from its
device, so the link can be deleted at that point. If none of them is set,
the link will be maintained until one of the devices pointed to by it (either
the consumer or the supplier) is unregistered.

Also, if DL_FLAG_STATELESS, DL_FLAG_AUTOREMOVE_CONSUMER and
DL_FLAG_AUTOREMOVE_SUPPLIER are not set in **flags** (that is, a persistent
managed device link is being added), the DL_FLAG_AUTOPROBE_CONSUMER flag can
be used to request the driver core to automatically probe for a consumer
driver after successfully binding a driver to the supplier device.

The combination of DL_FLAG_STATELESS and one of DL_FLAG_AUTOREMOVE_CONSUMER,
DL_FLAG_AUTOREMOVE_SUPPLIER, or DL_FLAG_AUTOPROBE_CONSUMER set in **flags** at
the same time is invalid and will cause NULL to be returned upfront.
However, if a device link between the given **consumer** and **supplier** pair
exists already when this function is called for them, the existing link will
be returned regardless of its current type and status (the link's flags may
be modified then). The caller of this function is then expected to treat
the link as though it has just been created, so (in particular) if
DL_FLAG_STATELESS was passed in **flags**, the link needs to be released
explicitly when not needed any more (as stated above).

A side effect of the link creation is re-ordering of dpm_list and the
devices_kset list by moving the consumer device and all devices depending
on it to the ends of these lists (that does not happen to devices that have
not been registered when this function is called).

The supplier device is required to be registered when this function is called
and NULL will be returned if that is not the case. The consumer device need
not be registered, however.

void device_link_del(struct [device_link](infrastructure.md#c.device_link "device_link") \*link)
:   Delete a stateless link between two devices.

**Parameters**

`struct device_link *link`
:   Device link to delete.

**Description**

The caller must ensure proper synchronization of this function with runtime
PM. If the link was added multiple times, it needs to be deleted as often.
Care is required for hotplugged devices: Their links are purged on removal
and calling [`device_link_del()`](infrastructure.md#c.device_link_del "device_link_del") is then no longer allowed.

void device_link_remove(void \*consumer, struct [device](infrastructure.md#c.device "device") \*supplier)
:   Delete a stateless link between two devices.

**Parameters**

`void *consumer`
:   Consumer end of the link.

`struct device *supplier`
:   Supplier end of the link.

**Description**

The caller must ensure proper synchronization of this function with runtime
PM.

const char \*dev_driver_string(const struct [device](infrastructure.md#c.device "device") \*dev)
:   Return a device's driver name, if at all possible

**Parameters**

`const struct device *dev`
:   [`struct device`](infrastructure.md#c.device "device") to get the name of

**Description**

Will return the device's driver's name if it is bound to a device. If
the device is not bound to a driver, it will return the name of the bus
it is attached to. If it is not attached to a bus either, an empty
string will be returned.

int devm_device_add_group(struct [device](infrastructure.md#c.device "device") \*dev, const struct attribute_group \*grp)
:   given a device, create a managed attribute group

**Parameters**

`struct device *dev`
:   The device to create the group for

`const struct attribute_group *grp`
:   The attribute group to create

**Description**

This function creates a group for the first time. It will explicitly
warn and error if any of the attribute files being created already exist.

Returns 0 on success or error code on failure.

int devm_device_add_groups(struct [device](infrastructure.md#c.device "device") \*dev, const struct attribute_group \*\*groups)
:   create a bunch of managed attribute groups

**Parameters**

`struct device *dev`
:   The device to create the group for

`const struct attribute_group **groups`
:   The attribute groups to create, NULL terminated

**Description**

This function creates a bunch of managed attribute groups. If an error
occurs when creating a group, all previously created groups will be
removed, unwinding everything back to the original state when this
function was called. It will explicitly warn and error if any of the
attribute files being created already exist.

Returns 0 on success or error code from sysfs_create_group on failure.

int device_create_file(struct [device](infrastructure.md#c.device "device") \*dev, const struct [device_attribute](infrastructure.md#c.device_attribute "device_attribute") \*attr)
:   create sysfs attribute file for device.

**Parameters**

`struct device *dev`
:   device.

`const struct device_attribute *attr`
:   device attribute descriptor.

void device_remove_file(struct [device](infrastructure.md#c.device "device") \*dev, const struct [device_attribute](infrastructure.md#c.device_attribute "device_attribute") \*attr)
:   remove sysfs attribute file.

**Parameters**

`struct device *dev`
:   device.

`const struct device_attribute *attr`
:   device attribute descriptor.

bool device_remove_file_self(struct [device](infrastructure.md#c.device "device") \*dev, const struct [device_attribute](infrastructure.md#c.device_attribute "device_attribute") \*attr)
:   remove sysfs attribute file from its own method.

**Parameters**

`struct device *dev`
:   device.

`const struct device_attribute *attr`
:   device attribute descriptor.

**Description**

See kernfs_remove_self() for details.

int device_create_bin_file(struct [device](infrastructure.md#c.device "device") \*dev, const struct bin_attribute \*attr)
:   create sysfs binary attribute file for device.

**Parameters**

`struct device *dev`
:   device.

`const struct bin_attribute *attr`
:   device binary attribute descriptor.

void device_remove_bin_file(struct [device](infrastructure.md#c.device "device") \*dev, const struct bin_attribute \*attr)
:   remove sysfs binary attribute file

**Parameters**

`struct device *dev`
:   device.

`const struct bin_attribute *attr`
:   device binary attribute descriptor.

void device_initialize(struct [device](infrastructure.md#c.device "device") \*dev)
:   init device structure.

**Parameters**

`struct device *dev`
:   device.

**Description**

This prepares the device for use by other layers by initializing
its fields.
It is the first half of [`device_register()`](infrastructure.md#c.device_register "device_register"), if called by
that function, though it can also be called separately, so one
may use **dev**'s fields. In particular, [`get_device()`](infrastructure.md#c.get_device "get_device")/[`put_device()`](infrastructure.md#c.put_device "put_device")
may be used for reference counting of **dev** after calling this
function.

All fields in **dev** must be initialized by the caller to 0, except
for those explicitly set to some other value. The simplest
approach is to use [`kzalloc()`](../core-api/mm-api.md#c.kzalloc "kzalloc") to allocate the structure containing
**dev**.

**NOTE**

Use [`put_device()`](infrastructure.md#c.put_device "put_device") to give up your reference instead of freeing
**dev** directly once you have called this function.

int dev_set_name(struct [device](infrastructure.md#c.device "device") \*dev, const char \*fmt, ...)
:   set a device name

**Parameters**

`struct device *dev`
:   device

`const char *fmt`
:   format string for the device's name

`...`
:   variable arguments

int device_add(struct [device](infrastructure.md#c.device "device") \*dev)
:   add device to device hierarchy.

**Parameters**

`struct device *dev`
:   device.

**Description**

This is part 2 of [`device_register()`](infrastructure.md#c.device_register "device_register"), though may be called
separately _iff_ [`device_initialize()`](infrastructure.md#c.device_initialize "device_initialize") has been called separately.

This adds **dev** to the kobject hierarchy via [`kobject_add()`](basics.md#c.kobject_add "kobject_add"), adds it
to the global and sibling lists for the device, then
adds it to the other relevant subsystems of the driver model.

Do not call this routine or [`device_register()`](infrastructure.md#c.device_register "device_register") more than once for
any device structure. The driver model core is not designed to work
with devices that get unregistered and then spring back to life.
(Among other things, it's very hard to guarantee that all references
to the previous incarnation of **dev** have been dropped.) Allocate
and register a fresh new [`struct device`](infrastructure.md#c.device "device") instead.

Rule of thumb is: if [`device_add()`](infrastructure.md#c.device_add "device_add") succeeds, you should call
[`device_del()`](infrastructure.md#c.device_del "device_del") when you want to get rid of it. If [`device_add()`](infrastructure.md#c.device_add "device_add") has
*not* succeeded, use *only* [`put_device()`](infrastructure.md#c.put_device "put_device") to drop the reference
count.

**NOTE**

_Never_ directly free **dev** after calling this function, even
if it returned an error! Always use [`put_device()`](infrastructure.md#c.put_device "put_device") to give up your
reference instead.

int device_register(struct [device](infrastructure.md#c.device "device") \*dev)
:   register a device with the system.

**Parameters**

`struct device *dev`
:   pointer to the device structure

**Description**

This happens in two clean steps - initialize the device
and add it to the system. The two steps can be called
separately, but this is the easiest and most common.
I.e. you should only call the two helpers separately if
have a clearly defined need to use and refcount the device
before it is added to the hierarchy.

For more information, see the kerneldoc for [`device_initialize()`](infrastructure.md#c.device_initialize "device_initialize")
and [`device_add()`](infrastructure.md#c.device_add "device_add").

**NOTE**

_Never_ directly free **dev** after calling this function, even
if it returned an error! Always use [`put_device()`](infrastructure.md#c.put_device "put_device") to give up the
reference initialized in this function instead.

struct [device](infrastructure.md#c.device "device") \*get_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   increment reference count for device.

**Parameters**

`struct device *dev`
:   device.

**Description**

This simply forwards the call to [`kobject_get()`](basics.md#c.kobject_get "kobject_get"), though
we do take care to provide for the case that we get a NULL
pointer passed in.

void put_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   decrement reference count.

**Parameters**

`struct device *dev`
:   device in question.

void device_del(struct [device](infrastructure.md#c.device "device") \*dev)
:   delete device from system.

**Parameters**

`struct device *dev`
:   device.

**Description**

This is the first part of the device unregistration
sequence. This removes the device from the lists we control
from here, has it removed from the other driver model
subsystems it was added to in [`device_add()`](infrastructure.md#c.device_add "device_add"), and removes it
from the kobject hierarchy.

**NOTE**

this should be called manually _iff_ [`device_add()`](infrastructure.md#c.device_add "device_add") was
also called manually.

void device_unregister(struct [device](infrastructure.md#c.device "device") \*dev)
:   unregister device from system.

**Parameters**

`struct device *dev`
:   device going away.

**Description**

We do this in two parts, like we do [`device_register()`](infrastructure.md#c.device_register "device_register"). First,
we remove it from all the subsystems with [`device_del()`](infrastructure.md#c.device_del "device_del"), then
we decrement the reference count via [`put_device()`](infrastructure.md#c.put_device "put_device"). If that
is the final reference count, the device will be cleaned up
via device_release() above. Otherwise, the structure will
stick around until the final reference to the device is dropped.

int device_for_each_child(struct [device](infrastructure.md#c.device "device") \*parent, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device") \*dev, void \*data))
:   device child iterator.

**Parameters**

`struct device *parent`
:   parent [`struct device`](infrastructure.md#c.device "device").

`void *data`
:   data for the callback.

`int (*fn)(struct device *dev, void *data)`
:   function to be called for each device.

**Description**

Iterate over **parent**'s child devices, and call **fn** for each,
passing it **data**.

We check the return of **fn** each time. If it returns anything
other than 0, we break out and return that value.

int device_for_each_child_reverse(struct [device](infrastructure.md#c.device "device") \*parent, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device") \*dev, void \*data))
:   device child iterator in reversed order.

**Parameters**

`struct device *parent`
:   parent [`struct device`](infrastructure.md#c.device "device").

`void *data`
:   data for the callback.

`int (*fn)(struct device *dev, void *data)`
:   function to be called for each device.

**Description**

Iterate over **parent**'s child devices, and call **fn** for each,
passing it **data**.

We check the return of **fn** each time. If it returns anything
other than 0, we break out and return that value.

struct [device](infrastructure.md#c.device "device") \*device_find_child(struct [device](infrastructure.md#c.device "device") \*parent, void \*data, int (\*match)(struct [device](infrastructure.md#c.device "device") \*dev, void \*data))
:   device iterator for locating a particular device.

**Parameters**

`struct device *parent`
:   parent [`struct device`](infrastructure.md#c.device "device")

`void *data`
:   Data to pass to match function

`int (*match)(struct device *dev, void *data)`
:   Callback function to check device

**Description**

This is similar to the [`device_for_each_child()`](infrastructure.md#c.device_for_each_child "device_for_each_child") function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the **match** callback.

The callback should return 0 if the device doesn't match and non-zero
if it does. If the callback returns non-zero and a reference to the
current device can be obtained, this function will return to the caller
and not iterate over any more devices.

**NOTE**

you will need to drop the reference with [`put_device()`](infrastructure.md#c.put_device "put_device") after use.

struct [device](infrastructure.md#c.device "device") \*device_find_child_by_name(struct [device](infrastructure.md#c.device "device") \*parent, const char \*name)
:   device iterator for locating a child device.

**Parameters**

`struct device *parent`
:   parent [`struct device`](infrastructure.md#c.device "device")

`const char *name`
:   name of the child device

**Description**

This is similar to the [`device_find_child()`](infrastructure.md#c.device_find_child "device_find_child") function above, but it
returns a reference to a device that has the name **name**.

**NOTE**

you will need to drop the reference with [`put_device()`](infrastructure.md#c.put_device "put_device") after use.

struct [device](infrastructure.md#c.device "device") \*device_find_any_child(struct [device](infrastructure.md#c.device "device") \*parent)
:   device iterator for locating a child device, if any.

**Parameters**

`struct device *parent`
:   parent [`struct device`](infrastructure.md#c.device "device")

**Description**

This is similar to the [`device_find_child()`](infrastructure.md#c.device_find_child "device_find_child") function above, but it
returns a reference to a child device, if any.

**NOTE**

you will need to drop the reference with [`put_device()`](infrastructure.md#c.put_device "put_device") after use.

struct [device](infrastructure.md#c.device "device") \*__root_device_register(const char \*name, struct module \*owner)
:   allocate and register a root device

**Parameters**

`const char *name`
:   root device name

`struct module *owner`
:   owner module of the root device, usually THIS_MODULE

**Description**

This function allocates a root device and registers it
using [`device_register()`](infrastructure.md#c.device_register "device_register"). In order to free the returned
device, use [`root_device_unregister()`](infrastructure.md#c.root_device_unregister "root_device_unregister").

Root devices are dummy devices which allow other devices
to be grouped under /sys/devices. Use this function to
allocate a root device and then use it as the parent of
any device which should appear under /sys/devices/{name}

The /sys/devices/{name} directory will also contain a
'module' symlink which points to the **owner** directory
in sysfs.

Returns [`struct device`](infrastructure.md#c.device "device") pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

**Note**

You probably want to use root_device_register().

void root_device_unregister(struct [device](infrastructure.md#c.device "device") \*dev)
:   unregister and free a root device

**Parameters**

`struct device *dev`
:   device going away

**Description**

This function unregisters and cleans up a device that was created by
root_device_register().

struct [device](infrastructure.md#c.device "device") \*device_create(const struct [class](infrastructure.md#c.device_create "class") \*class, struct [device](infrastructure.md#c.device "device") \*parent, dev_t devt, void \*drvdata, const char \*fmt, ...)
:   creates a device and registers it with sysfs

**Parameters**

`const struct class *class`
:   pointer to the [`struct class`](infrastructure.md#c.class "class") that this device should be registered to

`struct device *parent`
:   pointer to the parent [`struct device`](infrastructure.md#c.device "device") of this new device, if any

`dev_t devt`
:   the dev_t for the char device to be added

`void *drvdata`
:   the data to be added to the device for callbacks

`const char *fmt`
:   string for the device's name

`...`
:   variable arguments

**Description**

This function can be used by char device classes. A [`struct device`](infrastructure.md#c.device "device")
will be created in sysfs, registered to the specified class.

A "dev" file will be created, showing the dev_t for the device, if
the dev_t is not 0,0.
If a pointer to a parent [`struct device`](infrastructure.md#c.device "device") is passed in, the newly created
[`struct device`](infrastructure.md#c.device "device") will be a child of that device in sysfs.
The pointer to the [`struct device`](infrastructure.md#c.device "device") will be returned from the call.
Any further sysfs files that might be required can be created using this
pointer.

Returns [`struct device`](infrastructure.md#c.device "device") pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

struct [device](infrastructure.md#c.device "device") \*device_create_with_groups(const struct [class](infrastructure.md#c.device_create_with_groups "class") \*class, struct [device](infrastructure.md#c.device "device") \*parent, dev_t devt, void \*drvdata, const struct attribute_group \*\*groups, const char \*fmt, ...)
:   creates a device and registers it with sysfs

**Parameters**

`const struct class *class`
:   pointer to the [`struct class`](infrastructure.md#c.class "class") that this device should be registered to

`struct device *parent`
:   pointer to the parent [`struct device`](infrastructure.md#c.device "device") of this new device, if any

`dev_t devt`
:   the dev_t for the char device to be added

`void *drvdata`
:   the data to be added to the device for callbacks

`const struct attribute_group **groups`
:   NULL-terminated list of attribute groups to be created

`const char *fmt`
:   string for the device's name

`...`
:   variable arguments

**Description**

This function can be used by char device classes. A [`struct device`](infrastructure.md#c.device "device")
will be created in sysfs, registered to the specified class.
Additional attributes specified in the groups parameter will also
be created automatically.

A "dev" file will be created, showing the dev_t for the device, if
the dev_t is not 0,0.
If a pointer to a parent [`struct device`](infrastructure.md#c.device "device") is passed in, the newly created
[`struct device`](infrastructure.md#c.device "device") will be a child of that device in sysfs.
The pointer to the [`struct device`](infrastructure.md#c.device "device") will be returned from the call.
Any further sysfs files that might be required can be created using this
pointer.

Returns [`struct device`](infrastructure.md#c.device "device") pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

void device_destroy(const struct [class](infrastructure.md#c.device_destroy "class") \*class, dev_t devt)
:   removes a device that was created with [`device_create()`](infrastructure.md#c.device_create "device_create")

**Parameters**

`const struct class *class`
:   pointer to the [`struct class`](infrastructure.md#c.class "class") that this device was registered with

`dev_t devt`
:   the dev_t of the device that was previously registered

**Description**

This call unregisters and cleans up a device that was created with a
call to [`device_create()`](infrastructure.md#c.device_create "device_create").

int device_rename(struct [device](infrastructure.md#c.device "device") \*dev, const char \*new_name)
:   renames a device

**Parameters**

`struct device *dev`
:   the pointer to the [`struct device`](infrastructure.md#c.device "device") to be renamed

`const char *new_name`
:   the new name of the device

**Description**

It is the responsibility of the caller to provide mutual
exclusion between two different calls of device_rename
on the same device to ensure that new_name is valid and
won't conflict with other devices.

However, if you're writing new code, do not call this function. The following
text from Kay Sievers offers some insight:

Renaming devices is racy at many levels, symlinks and other stuff are not
replaced atomically, and you get a "move" uevent, but it's not easy to
connect the event to the old and new device. Device nodes are not renamed at
all, there isn't even support for that in the kernel now.

In the meantime, during renaming, your target name might be taken by another
driver, creating conflicts. Or the old name is taken directly after you
renamed it -- then you get events for the same DEVPATH, before you even see
the "move" event. It's just a mess, and nothing new should ever rely on
kernel device renaming. Besides that, it's not even implemented now for
other things than (driver-core wise very simple) network devices.

Make up a "real" name in the driver before you register anything, or add
some other attributes for userspace to find the device, or use udev to add
symlinks -- but never rename kernel devices later, it's a complete mess. We
don't even want to get into that and try to implement the missing pieces in
the core. We really have other pieces to fix in the driver core mess. :)

**Note**

given that some subsystems (networking and infiniband) use this
function, with no immediate plans for this to change, we cannot assume or
require that this function not be called at all.

int device_move(struct [device](infrastructure.md#c.device "device") \*dev, struct [device](infrastructure.md#c.device "device") \*new_parent, enum [dpm_order](infrastructure.md#c.device_move "dpm_order") dpm_order)
:   moves a device to a new parent

**Parameters**

`struct device *dev`
:   the pointer to the [`struct device`](infrastructure.md#c.device "device") to be moved

`struct device *new_parent`
:   the new parent of the device (can be NULL)

`enum dpm_order dpm_order`
:   how to reorder the dpm_list

int device_change_owner(struct [device](infrastructure.md#c.device "device") \*dev, kuid_t kuid, kgid_t kgid)
:   change the owner of an existing device.

**Parameters**

`struct device *dev`
:   device.

`kuid_t kuid`
:   new owner's kuid

`kgid_t kgid`
:   new owner's kgid

**Description**

This changes the owner of **dev** and its corresponding sysfs entries to
**kuid**/**kgid**. This function closely mirrors how **dev** was added via driver
core.

Returns 0 on success or error code on failure.

int dev_err_probe(const struct [device](infrastructure.md#c.device "device") \*dev, int err, const char \*fmt, ...)
:   probe error check and log helper

**Parameters**

`const struct device *dev`
:   the pointer to the [`struct device`](infrastructure.md#c.device "device")

`int err`
:   error value to test

`const char *fmt`
:   printf-style format string

`...`
:   arguments as specified in the format string

**Description**

This helper implements common pattern present in probe functions for error
checking: print debug or error message depending if the error value is
-EPROBE_DEFER and propagate error upwards.
In case of -EPROBE_DEFER it sets also defer probe reason, which can be
checked later by reading devices_deferred debugfs attribute.
It replaces code sequence:

```
if (err != -EPROBE_DEFER)
        dev_err(dev, ...);
else
        dev_dbg(dev, ...);
return err;
```

with:

```
return dev_err_probe(dev, err, ...);
```

Using this helper in your probe function is totally fine even if **err** is
known to never be -EPROBE_DEFER.
The benefit compared to a normal dev_err() is the standardized format
of the error code, it being emitted symbolically (i.e. you get "EAGAIN"
instead of "-35") and the fact that the error code is returned which allows
more compact error paths.

Returns **err**.

void set_primary_fwnode(struct [device](infrastructure.md#c.device "device") \*dev, struct fwnode_handle \*fwnode)
:   Change the primary firmware node of a given device.

**Parameters**

`struct device *dev`
:   Device to handle.

`struct fwnode_handle *fwnode`
:   New primary firmware node of the device.

**Description**

Set the device's firmware node pointer to **fwnode**, but if a secondary
firmware node of the device is present, preserve it.

Valid fwnode cases are:
:   - primary --> secondary --> -ENODEV
    - primary --> NULL
    - secondary --> -ENODEV
    - NULL

void set_secondary_fwnode(struct [device](infrastructure.md#c.device "device") \*dev, struct fwnode_handle \*fwnode)
:   Change the secondary firmware node of a given device.

**Parameters**

`struct device *dev`
:   Device to handle.

`struct fwnode_handle *fwnode`
:   New secondary firmware node of the device.

**Description**

If a primary firmware node of the device is present, set its secondary
pointer to **fwnode**. Otherwise, set the device's firmware node pointer to
**fwnode**.

void device_set_of_node_from_dev(struct [device](infrastructure.md#c.device "device") \*dev, const struct [device](infrastructure.md#c.device "device") \*dev2)
:   reuse device-tree node of another device

**Parameters**

`struct device *dev`
:   device whose device-tree node is being set

`const struct device *dev2`
:   device whose device-tree node is being reused

**Description**

Takes another reference to the new device-tree node after first dropping
any reference held to the old node.

void register_syscore_ops(struct syscore_ops \*ops)
:   Register a set of system core operations.

**Parameters**

`struct syscore_ops *ops`
:   System core operations to register.

void unregister_syscore_ops(struct syscore_ops \*ops)
:   Unregister a set of system core operations.

**Parameters**

`struct syscore_ops *ops`
:   System core operations to unregister.

int syscore_suspend(void)
:   Execute all the registered system core suspend callbacks.

**Parameters**

`void`
:   no arguments

**Description**

This function is executed with one CPU on-line and disabled interrupts.

void syscore_resume(void)
:   Execute all the registered system core resume callbacks.

**Parameters**

`void`
:   no arguments

**Description**

This function is executed with one CPU on-line and disabled interrupts.

struct [device](infrastructure.md#c.device "device") \*class_find_device_by_name(const struct [class](infrastructure.md#c.class_find_device_by_name "class") \*class, const char \*name)
:   device iterator for locating a particular device of a specific name.

**Parameters**

`const struct class *class`
:   class type

`const char *name`
:   name of the device to match

struct [device](infrastructure.md#c.device "device") \*class_find_device_by_of_node(const struct [class](infrastructure.md#c.class_find_device_by_of_node "class") \*class, const struct device_node \*np)
:   device iterator for locating a particular device matching the of_node.

**Parameters**

`const struct class *class`
:   class type

`const struct device_node *np`
:   of_node of the device to match.

struct [device](infrastructure.md#c.device "device") \*class_find_device_by_fwnode(const struct [class](infrastructure.md#c.class_find_device_by_fwnode "class") \*class, const struct fwnode_handle \*fwnode)
:   device iterator for locating a particular device matching the fwnode.

**Parameters**

`const struct class *class`
:   class type

`const struct fwnode_handle *fwnode`
:   fwnode of the device to match.

struct [device](infrastructure.md#c.device "device") \*class_find_device_by_devt(const struct [class](infrastructure.md#c.class_find_device_by_devt "class") \*class, dev_t devt)
:   device iterator for locating a particular device matching the device type.

**Parameters**

`const struct class *class`
:   class type

`dev_t devt`
:   device type of the device to match.

struct [device](infrastructure.md#c.device "device") \*class_find_device_by_acpi_dev(const struct [class](infrastructure.md#c.class_find_device_by_acpi_dev "class") \*class, const struct acpi_device \*adev)
:   device iterator for locating a particular device matching the ACPI_COMPANION device.

**Parameters**

`const struct class *class`
:   class type

`const struct acpi_device *adev`
:   ACPI_COMPANION device to match.

struct [class](infrastructure.md#c.class "class") \*class_create(const char \*name)
:   create a [`struct class`](infrastructure.md#c.class "class") structure

**Parameters**

`const char *name`
:   pointer to a string for the name of this class.

**Description**

This is used to create a [`struct class`](infrastructure.md#c.class "class") pointer that can then be used
in calls to [`device_create()`](infrastructure.md#c.device_create "device_create").

Returns [`struct class`](infrastructure.md#c.class "class") pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

Note, the pointer created here is to be destroyed when finished by
making a call to [`class_destroy()`](infrastructure.md#c.class_destroy "class_destroy").

void class_destroy(const struct [class](infrastructure.md#c.class "class") \*cls)
:   destroys a [`struct class`](infrastructure.md#c.class "class") structure

**Parameters**

`const struct class *cls`
:   pointer to the [`struct class`](infrastructure.md#c.class "class") that is to be destroyed

**Description**

Note, the pointer to be destroyed must have been created with a call
to [`class_create()`](infrastructure.md#c.class_create "class_create").

void class_dev_iter_init(struct class_dev_iter \*iter, const struct [class](infrastructure.md#c.class_dev_iter_init "class") \*class, const struct [device](infrastructure.md#c.device "device") \*start, const struct device_type \*type)
:   initialize class device iterator

**Parameters**

`struct class_dev_iter *iter`
:   class iterator to initialize

`const struct class *class`
:   the class we wanna iterate over

`const struct device *start`
:   the device to start iterating from, if any

`const struct device_type *type`
:   device_type of the devices to iterate over, NULL for all

**Description**

Initialize class iterator **iter** such that it iterates over devices
of **class**. If **start** is set, the list iteration will start there,
otherwise if it is NULL, the iteration starts at the beginning of
the list.

struct [device](infrastructure.md#c.device "device") \*class_dev_iter_next(struct class_dev_iter \*iter)
:   iterate to the next device

**Parameters**

`struct class_dev_iter *iter`
:   class iterator to proceed

**Description**

Proceed **iter** to the next device and return it. Returns NULL if
iteration is complete.

The returned device is referenced and won't be released till
iterator is proceed to the next device or exited. The caller is
free to do whatever it wants to do with the device including
calling back into class code.

void class_dev_iter_exit(struct class_dev_iter \*iter)
:   finish iteration

**Parameters**

`struct class_dev_iter *iter`
:   class iterator to finish

**Description**

Finish an iteration. Always call this function after iteration is
complete whether the iteration ran till the end or not.

int class_for_each_device(const struct [class](infrastructure.md#c.class_for_each_device "class") \*class, const struct [device](infrastructure.md#c.device "device") \*start, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device")\*, void\*))
:   device iterator

**Parameters**

`const struct class *class`
:   the class we're iterating

`const struct device *start`
:   the device to start with in the list, if any.

`void *data`
:   data for the callback

`int (*fn)(struct device *, void *)`
:   function to be called for each device

**Description**

Iterate over **class**'s list of devices, and call **fn** for each,
passing it **data**. If **start** is set, the list iteration will start
there, otherwise if it is NULL, the iteration starts at the
beginning of the list.

We check the return of **fn** each time. If it returns anything
other than 0, we break out and return that value.

**fn** is allowed to do anything including calling back into class
code. There's no locking restriction.

struct [device](infrastructure.md#c.device "device") \*class_find_device(const struct [class](infrastructure.md#c.class_find_device "class") \*class, const struct [device](infrastructure.md#c.device "device") \*start, const void \*data, int (\*match)(struct [device](infrastructure.md#c.device "device")\*, const void\*))
:   device iterator for locating a particular device

**Parameters**

`const struct class *class`
:   the class we're iterating

`const struct device *start`
:   Device to begin with

`const void *data`
:   data for the match function

`int (*match)(struct device *, const void *)`
:   function to check device

**Description**

This is similar to the class_for_each_dev() function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the **match** callback.

The callback should return 0 if the device doesn't match and non-zero
if it does. If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

Note, you will need to drop the reference with [`put_device()`](infrastructure.md#c.put_device "put_device") after use.

**match** is allowed to do anything including calling back into class
code. There's no locking restriction.

struct class_compat \*class_compat_register(const char \*name)
:   register a compatibility class

**Parameters**

`const char *name`
:   the name of the class

**Description**

Compatibility class are meant as a temporary user-space compatibility
workaround when converting a family of class devices to a bus devices.

void class_compat_unregister(struct class_compat \*cls)
:   unregister a compatibility class

**Parameters**

`struct class_compat *cls`
:   the class to unregister

int class_compat_create_link(struct class_compat \*cls, struct [device](infrastructure.md#c.device "device") \*dev, struct [device](infrastructure.md#c.device "device") \*device_link)
:   create a compatibility class device link to a bus device

**Parameters**

`struct class_compat *cls`
:   the compatibility class

`struct device *dev`
:   the target bus device

`struct device *device_link`
:   an optional device to which a "device" link should be created

void class_compat_remove_link(struct class_compat \*cls, struct [device](infrastructure.md#c.device "device") \*dev, struct [device](infrastructure.md#c.device "device") \*device_link)
:   remove a compatibility class device link to a bus device

**Parameters**

`struct class_compat *cls`
:   the compatibility class

`struct device *dev`
:   the target bus device

`struct device *device_link`
:   an optional device to which a "device" link was previously
    created

bool class_is_registered(const struct [class](infrastructure.md#c.class_is_registered "class") \*class)
:   determine if at this moment in time, a class is registered in the driver core or not.

**Parameters**

`const struct class *class`
:   the class to check

**Description**

Returns a boolean to state if the class is registered in the driver core
or not. Note that the value could switch right after this call is made,
so only use this in places where you "know" it is safe to do so (usually
to determine if the specific class has been registered yet or not).

Be careful in using this.

struct node_access_nodes
:   Access class device to hold user visible relationships to other nodes.

**Definition**:

```
struct node_access_nodes {
    struct device           dev;
    struct list_head        list_node;
    unsigned int            access;
#ifdef CONFIG_HMEM_REPORTING;
    struct access_coordinate        coord;
#endif;
};
```

**Members**

`dev`
:   Device for this memory access class

`list_node`
:   List element in the node's access list

`access`
:   The access class rank

`coord`
:   Heterogeneous memory performance coordinates

void node_set_perf_attrs(unsigned int nid, struct access_coordinate \*coord, unsigned int access)
:   Set the performance values for given access class

**Parameters**

`unsigned int nid`
:   Node identifier to be set

`struct access_coordinate *coord`
:   Heterogeneous memory performance coordinates

`unsigned int access`
:   The access class the for the given attributes

struct node_cache_info
:   Internal tracking for memory node caches

**Definition**:

```
struct node_cache_info {
    struct device dev;
    struct list_head node;
    struct node_cache_attrs cache_attrs;
};
```

**Members**

`dev`
:   Device represeting the cache level

`node`
:   List element for tracking in the node

`cache_attrs`
:   Attributes for this cache level

void node_add_cache(unsigned int nid, struct node_cache_attrs \*cache_attrs)
:   add cache attribute to a memory node

**Parameters**

`unsigned int nid`
:   Node identifier that has new cache attributes

`struct node_cache_attrs *cache_attrs`
:   Attributes for the cache being added

void unregister_node(struct [node](infrastructure.md#c.unregister_node "node") \*node)
:   unregister a node device

**Parameters**

`struct node *node`
:   node going away

**Description**

Unregisters a node device **node**. All the devices on the node must be
unregistered before calling this function.

int register_memory_node_under_compute_node(unsigned int mem_nid, unsigned int cpu_nid, unsigned int access)
:   link memory node to its compute node for a given access class.

**Parameters**

`unsigned int mem_nid`
:   Memory node number

`unsigned int cpu_nid`
:   Cpu node number

`unsigned int access`
:   Access class to register

**Description**

> For use with platforms that may have separate memory and compute nodes.
> This function will export node relationships linking which memory
> initiator nodes can access memory targets at a given ranked access
> class.

int transport_class_register(struct transport_class \*tclass)
:   register an initial transport class

**Parameters**

`struct transport_class *tclass`
:   a pointer to the transport class structure to be initialised

**Description**

The transport class contains an embedded class which is used to
identify it. The caller should initialise this structure with
zeros and then generic class must have been initialised with the
actual transport class unique name. There's a macro
DECLARE_TRANSPORT_CLASS() to do this (declared classes still must
be registered).

Returns 0 on success or error on failure.

void transport_class_unregister(struct transport_class \*tclass)
:   unregister a previously registered class

**Parameters**

`struct transport_class *tclass`
:   The transport class to unregister

**Description**

Must be called prior to deallocating the memory for the transport
class.

int anon_transport_class_register(struct anon_transport_class \*atc)
:   register an anonymous class

**Parameters**

`struct anon_transport_class *atc`
:   The anon transport class to register

**Description**

The anonymous transport class contains both a transport class and a
container. The idea of an anonymous class is that it never
actually has any device attributes associated with it (and thus
saves on container storage). So it can only be used for triggering
events. Use prezero and then use DECLARE_ANON_TRANSPORT_CLASS() to
initialise the anon transport class storage.

void anon_transport_class_unregister(struct anon_transport_class \*atc)
:   unregister an anon class

**Parameters**

`struct anon_transport_class *atc`
:   Pointer to the anon transport class to unregister

**Description**

Must be called prior to deallocating the memory for the anon
transport class.

void transport_setup_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   declare a new dev for transport class association but don't make it visible yet.

**Parameters**

`struct device *dev`
:   the generic device representing the entity being added

**Description**

Usually, dev represents some component in the HBA system (either
the HBA itself or a device remote across the HBA bus). This
routine is simply a trigger point to see if any set of transport
classes wishes to associate with the added device. This allocates
storage for the class device and initialises it, but does not yet
add it to the system or add attributes to it (you do this with
transport_add_device). If you have no need for a separate setup
and add operations, use transport_register_device (see
transport_class.h).

int transport_add_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   declare a new dev for transport class association

**Parameters**

`struct device *dev`
:   the generic device representing the entity being added

**Description**

Usually, dev represents some component in the HBA system (either
the HBA itself or a device remote across the HBA bus). This
routine is simply a trigger point used to add the device to the
system and register attributes for it.

void transport_configure_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   configure an already set up device

**Parameters**

`struct device *dev`
:   generic device representing device to be configured

**Description**

The idea of configure is simply to provide a point within the setup
process to allow the transport class to extract information from a
device after it has been setup. This is used in SCSI because we
have to have a setup device to begin using the HBA, but after we
send the initial inquiry, we use configure to extract the device
parameters. The device need not have been added to be configured.

void transport_remove_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   remove the visibility of a device

**Parameters**

`struct device *dev`
:   generic device to remove

**Description**

This call removes the visibility of the device (to the user from
sysfs), but does not destroy it. To eliminate a device entirely
you must also call transport_destroy_device. If you don't need to
do remove and destroy as separate operations, use
transport_unregister_device() (see transport_class.h) which will
perform both calls for you.

void transport_destroy_device(struct [device](infrastructure.md#c.device "device") \*dev)
:   destroy a removed device

**Parameters**

`struct device *dev`
:   device to eliminate from the transport class.

**Description**

This call triggers the elimination of storage associated with the
transport classdev. Note: all it really does is relinquish a
reference to the classdev. The memory will not be freed until the
last reference goes to zero. Note also that the classdev retains a
reference count on dev, so dev too will remain for as long as the
transport class device remains around.

int driver_deferred_probe_check_state(struct [device](infrastructure.md#c.device "device") \*dev)
:   Check deferred probe state

**Parameters**

`struct device *dev`
:   device to check

**Return**

- -ENODEV if initcalls have completed and modules are disabled.
- -ETIMEDOUT if the deferred probe timeout was set and has expired
  and modules are enabled.
- -EPROBE_DEFER in other cases.

**Description**

Drivers or subsystems can opt-in to calling this function instead of directly
returning -EPROBE_DEFER.

int device_bind_driver(struct [device](infrastructure.md#c.device "device") \*dev)
:   bind a driver to one device.

**Parameters**

`struct device *dev`
:   device.

**Description**

Allow manual attachment of a driver to a device.
Caller must have already set **dev->driver**.

Note that this does not modify the bus reference count.
Please verify that is accounted for before calling this.
(It is ok to call with no other effort from a driver's probe() method.)

This function must be called with the device lock held.

Callers should prefer to use [`device_driver_attach()`](infrastructure.md#c.device_driver_attach "device_driver_attach") instead.

void wait_for_device_probe(void)

**Parameters**

`void`
:   no arguments

**Description**

Wait for device probing to be completed.

int device_attach(struct [device](infrastructure.md#c.device "device") \*dev)
:   try to attach device to a driver.

**Parameters**

`struct device *dev`
:   device.

**Description**

Walk the list of drivers that the bus has and call
driver_probe_device() for each pair. If a compatible
pair is found, break out and return.

Returns 1 if the device was bound to a driver;
0 if no matching driver was found;
-ENODEV if the device is not registered.

When called for a USB interface, **dev->parent** lock must be held.

int device_driver_attach(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv, struct [device](infrastructure.md#c.device "device") \*dev)
:   attach a specific driver to a specific device

**Parameters**

`struct device_driver *drv`
:   Driver to attach

`struct device *dev`
:   Device to attach it to

**Description**

Manually attach driver to a device. Will acquire both **dev** lock and
**dev->parent** lock if needed. Returns 0 on success, -ERR on failure.

int driver_attach(struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv)
:   try to bind driver to devices.

**Parameters**

`struct device_driver *drv`
:   driver.

**Description**

Walk the list of devices that the bus has on it and try to
match the driver with each one. If driver_probe_device()
returns 0 and the **dev->driver** is set, we've found a
compatible pair.

void device_release_driver(struct [device](infrastructure.md#c.device "device") \*dev)
:   manually detach device from driver.

**Parameters**

`struct device *dev`
:   device.

**Description**

Manually detach device from driver.
When called for a USB interface, **dev->parent** lock must be held.

If this function is to be called with **dev->parent** lock held, ensure that
the device's consumers are unbound in advance or that their locks can be
acquired under the **dev->parent** lock.

struct platform_device \*platform_device_register_resndata(struct [device](infrastructure.md#c.device "device") \*parent, const char \*name, int id, const struct resource \*res, unsigned int num, const void \*data, size_t size)
:   add a platform-level device with resources and platform-specific data

**Parameters**

`struct device *parent`
:   parent device for the device we're adding

`const char *name`
:   base name of the device we're adding

`int id`
:   instance id

`const struct resource *res`
:   set of resources that needs to be allocated for the device

`unsigned int num`
:   number of resources

`const void *data`
:   platform specific data for this platform device

`size_t size`
:   size of platform specific data

**Description**

Returns `struct platform_device` pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

struct platform_device \*platform_device_register_simple(const char \*name, int id, const struct resource \*res, unsigned int num)
:   add a platform-level device and its resources

**Parameters**

`const char *name`
:   base name of the device we're adding

`int id`
:   instance id

`const struct resource *res`
:   set of resources that needs to be allocated for the device

`unsigned int num`
:   number of resources

**Description**

This function creates a simple platform device that requires minimal
resource and memory management. Canned release function freeing memory
allocated for the device allows drivers using such devices to be
unloaded without waiting for the last reference to the device to be
dropped.

This interface is primarily intended for use with legacy drivers which
probe hardware directly. Because such drivers create sysfs device nodes
themselves, rather than letting system infrastructure handle such device
enumeration tasks, they don't fully conform to the Linux driver model.
In particular, when such drivers are built as modules, they can't be
"hotplugged".

Returns `struct platform_device` pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

struct platform_device \*platform_device_register_data(struct [device](infrastructure.md#c.device "device") \*parent, const char \*name, int id, const void \*data, size_t size)
:   add a platform-level device with platform-specific data

**Parameters**

`struct device *parent`
:   parent device for the device we're adding

`const char *name`
:   base name of the device we're adding

`int id`
:   instance id

`const void *data`
:   platform specific data for this platform device

`size_t size`
:   size of platform specific data

**Description**

This function creates a simple platform device that requires minimal
resource and memory management. Canned release function freeing memory
allocated for the device allows drivers using such devices to be
unloaded without waiting for the last reference to the device to be
dropped.

Returns `struct platform_device` pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

struct resource \*platform_get_resource(struct platform_device \*dev, unsigned int type, unsigned int num)
:   get a resource for a device

**Parameters**

`struct platform_device *dev`
:   platform device

`unsigned int type`
:   resource type

`unsigned int num`
:   resource index

**Return**

a pointer to the resource or NULL on failure.

void __iomem \*devm_platform_get_and_ioremap_resource(struct platform_device \*pdev, unsigned int index, struct resource \*\*res)
:   call devm_ioremap_resource() for a platform device and get resource

**Parameters**

`struct platform_device *pdev`
:   platform device to use both for memory resource lookup as well as
    resource management

`unsigned int index`
:   resource index

`struct resource **res`
:   optional output parameter to store a pointer to the obtained resource.

**Return**

a pointer to the remapped memory or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") encoded error code
on failure.

void __iomem \*devm_platform_ioremap_resource(struct platform_device \*pdev, unsigned int index)
:   call devm_ioremap_resource() for a platform device

**Parameters**

`struct platform_device *pdev`
:   platform device to use both for memory resource lookup as well as
    resource management

`unsigned int index`
:   resource index

**Return**

a pointer to the remapped memory or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") encoded error code
on failure.

void __iomem \*devm_platform_ioremap_resource_byname(struct platform_device \*pdev, const char \*name)
:   call devm_ioremap_resource for a platform device, retrieve the resource by name

**Parameters**

`struct platform_device *pdev`
:   platform device to use both for memory resource lookup as well as
    resource management

`const char *name`
:   name of the resource

**Return**

a pointer to the remapped memory or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") encoded error code
on failure.

int platform_get_irq_optional(struct platform_device \*dev, unsigned int num)
:   get an optional IRQ for a device

**Parameters**

`struct platform_device *dev`
:   platform device

`unsigned int num`
:   IRQ number index

**Description**

Gets an IRQ for a platform device. Device drivers should check the return
value for errors so as to not pass a negative integer value to the
[`request_irq()`](../core-api/genericirq.md#c.request_irq "request_irq") APIs. This is the same as [`platform_get_irq()`](infrastructure.md#c.platform_get_irq "platform_get_irq"), except that it
does not print an error message if an IRQ can not be obtained.

For example:

```
int irq = platform_get_irq_optional(pdev, 0);
if (irq < 0)
        return irq;
```

**Return**

non-zero IRQ number on success, negative error number on failure.

int platform_get_irq(struct platform_device \*dev, unsigned int num)
:   get an IRQ for a device

**Parameters**

`struct platform_device *dev`
:   platform device

`unsigned int num`
:   IRQ number index

**Description**

Gets an IRQ for a platform device and prints an error message if finding the
IRQ fails. Device drivers should check the return value for errors so as to
not pass a negative integer value to the [`request_irq()`](../core-api/genericirq.md#c.request_irq "request_irq") APIs.

For example:

```
int irq = platform_get_irq(pdev, 0);
if (irq < 0)
        return irq;
```

**Return**

non-zero IRQ number on success, negative error number on failure.

int platform_irq_count(struct platform_device \*dev)
:   Count the number of IRQs a platform device uses

**Parameters**

`struct platform_device *dev`
:   platform device

**Return**

Number of IRQs a platform device uses or EPROBE_DEFER

int devm_platform_get_irqs_affinity(struct platform_device \*dev, struct [irq_affinity](../core-api/genericirq.md#c.irq_affinity "irq_affinity") \*affd, unsigned int minvec, unsigned int maxvec, int \*\*irqs)
:   devm method to get a set of IRQs for a device using an interrupt affinity descriptor

**Parameters**

`struct platform_device *dev`
:   platform device pointer

`struct irq_affinity *affd`
:   affinity descriptor

`unsigned int minvec`
:   minimum count of interrupt vectors

`unsigned int maxvec`
:   maximum count of interrupt vectors

`int **irqs`
:   pointer holder for IRQ numbers

**Description**

Gets a set of IRQs for a platform device, and updates IRQ afffinty according
to the passed affinity descriptor

**Return**

Number of vectors on success, negative error number on failure.

struct resource \*platform_get_resource_byname(struct platform_device \*dev, unsigned int type, const char \*name)
:   get a resource for a device by name

**Parameters**

`struct platform_device *dev`
:   platform device

`unsigned int type`
:   resource type

`const char *name`
:   resource name

int platform_get_irq_byname(struct platform_device \*dev, const char \*name)
:   get an IRQ for a device by name

**Parameters**

`struct platform_device *dev`
:   platform device

`const char *name`
:   IRQ name

**Description**

Get an IRQ like [`platform_get_irq()`](infrastructure.md#c.platform_get_irq "platform_get_irq"), but then by name rather then by index.

**Return**

non-zero IRQ number on success, negative error number on failure.

int platform_get_irq_byname_optional(struct platform_device \*dev, const char \*name)
:   get an optional IRQ for a device by name

**Parameters**

`struct platform_device *dev`
:   platform device

`const char *name`
:   IRQ name

**Description**

Get an optional IRQ by name like [`platform_get_irq_byname()`](infrastructure.md#c.platform_get_irq_byname "platform_get_irq_byname"). Except that it
does not print an error message if an IRQ can not be obtained.

**Return**

non-zero IRQ number on success, negative error number on failure.

int platform_add_devices(struct platform_device \*\*devs, int num)
:   add a numbers of platform devices

**Parameters**

`struct platform_device **devs`
:   array of platform devices to add

`int num`
:   number of platform devices in array

**Return**

0 on success, negative error number on failure.

void platform_device_put(struct platform_device \*pdev)
:   destroy a platform device

**Parameters**

`struct platform_device *pdev`
:   platform device to free

**Description**

Free all memory associated with a platform device. This function must
_only_ be externally called in error cases. All other usage is a bug.

struct platform_device \*platform_device_alloc(const char \*name, int id)
:   create a platform device

**Parameters**

`const char *name`
:   base name of the device we're adding

`int id`
:   instance id

**Description**

Create a platform device object which can have other objects attached
to it, and which will have attached objects freed when it is released.

int platform_device_add_resources(struct platform_device \*pdev, const struct resource \*res, unsigned int num)
:   add resources to a platform device

**Parameters**

`struct platform_device *pdev`
:   platform device allocated by platform_device_alloc to add resources to

`const struct resource *res`
:   set of resources that needs to be allocated for the device

`unsigned int num`
:   number of resources

**Description**

Add a copy of the resources to the platform device. The memory
associated with the resources will be freed when the platform device is
released.

int platform_device_add_data(struct platform_device \*pdev, const void \*data, size_t size)
:   add platform-specific data to a platform device

**Parameters**

`struct platform_device *pdev`
:   platform device allocated by platform_device_alloc to add resources to

`const void *data`
:   platform specific data for this platform device

`size_t size`
:   size of platform specific data

**Description**

Add a copy of platform specific data to the platform device's
platform_data pointer. The memory associated with the platform data
will be freed when the platform device is released.

int platform_device_add(struct platform_device \*pdev)
:   add a platform device to device hierarchy

**Parameters**

`struct platform_device *pdev`
:   platform device we're adding

**Description**

This is part 2 of [`platform_device_register()`](infrastructure.md#c.platform_device_register "platform_device_register"), though may be called
separately _iff_ pdev was allocated by [`platform_device_alloc()`](infrastructure.md#c.platform_device_alloc "platform_device_alloc").

void platform_device_del(struct platform_device \*pdev)
:   remove a platform-level device

**Parameters**

`struct platform_device *pdev`
:   platform device we're removing

**Description**

Note that this function will also release all memory- and port-based
resources owned by the device (**dev->resource**). This function must
_only_ be externally called in error cases. All other usage is a bug.

int platform_device_register(struct platform_device \*pdev)
:   add a platform-level device

**Parameters**

`struct platform_device *pdev`
:   platform device we're adding

**NOTE**

_Never_ directly free **pdev** after calling this function, even if it
returned an error! Always use [`platform_device_put()`](infrastructure.md#c.platform_device_put "platform_device_put") to give up the
reference initialised in this function instead.

void platform_device_unregister(struct platform_device \*pdev)
:   unregister a platform-level device

**Parameters**

`struct platform_device *pdev`
:   platform device we're unregistering

**Description**

Unregistration is done in 2 steps. First we release all resources
and remove it from the subsystem, then we drop reference count by
calling [`platform_device_put()`](infrastructure.md#c.platform_device_put "platform_device_put").

struct platform_device \*platform_device_register_full(const struct platform_device_info \*pdevinfo)
:   add a platform-level device with resources and platform-specific data

**Parameters**

`const struct platform_device_info *pdevinfo`
:   data used to create device

**Description**

Returns `struct platform_device` pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

int __platform_driver_register(struct platform_driver \*drv, struct module \*owner)
:   register a driver for platform-level devices

**Parameters**

`struct platform_driver *drv`
:   platform driver structure

`struct module *owner`
:   owning module/driver

void platform_driver_unregister(struct platform_driver \*drv)
:   unregister a driver for platform-level devices

**Parameters**

`struct platform_driver *drv`
:   platform driver structure

int __platform_driver_probe(struct platform_driver \*drv, int (\*probe)(struct platform_device\*), struct [module](infrastructure.md#c.__platform_driver_probe "module") \*module)
:   register driver for non-hotpluggable device

**Parameters**

`struct platform_driver *drv`
:   platform driver structure

`int (*probe)(struct platform_device *)`
:   the driver probe routine, probably from an __init section

`struct module *module`
:   module which will be the owner of the driver

**Description**

Use this instead of platform_driver_register() when you know the device
is not hotpluggable and has already been registered, and you want to
remove its run-once probe() infrastructure from memory after the driver
has bound to the device.

One typical use for this would be with drivers for controllers integrated
into system-on-chip processors, where the controller devices have been
configured as part of board setup.

Note that this is incompatible with deferred probing.

Returns zero if the driver registered and bound to a device, else returns
a negative error code and with the driver not registered.

struct platform_device \*__platform_create_bundle(struct platform_driver \*driver, int (\*probe)(struct platform_device\*), struct resource \*res, unsigned int n_res, const void \*data, size_t size, struct [module](infrastructure.md#c.__platform_create_bundle "module") \*module)
:   register driver and create corresponding device

**Parameters**

`struct platform_driver *driver`
:   platform driver structure

`int (*probe)(struct platform_device *)`
:   the driver probe routine, probably from an __init section

`struct resource *res`
:   set of resources that needs to be allocated for the device

`unsigned int n_res`
:   number of resources

`const void *data`
:   platform specific data for this platform device

`size_t size`
:   size of platform specific data

`struct module *module`
:   module which will be the owner of the driver

**Description**

Use this in legacy-style modules that probe hardware directly and
register a single platform device and corresponding platform driver.

Returns `struct platform_device` pointer on success, or [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error.

int __platform_register_drivers(struct platform_driver \*const \*drivers, unsigned int count, struct module \*owner)
:   register an array of platform drivers

**Parameters**

`struct platform_driver * const *drivers`
:   an array of drivers to register

`unsigned int count`
:   the number of drivers to register

`struct module *owner`
:   module owning the drivers

**Description**

Registers platform drivers specified by an array. On failure to register a
driver, all previously registered drivers will be unregistered. Callers of
this API should use [`platform_unregister_drivers()`](infrastructure.md#c.platform_unregister_drivers "platform_unregister_drivers") to unregister drivers in
the reverse order.

**Return**

0 on success or a negative error code on failure.

void platform_unregister_drivers(struct platform_driver \*const \*drivers, unsigned int count)
:   unregister an array of platform drivers

**Parameters**

`struct platform_driver * const *drivers`
:   an array of drivers to unregister

`unsigned int count`
:   the number of drivers to unregister

**Description**

Unregisters platform drivers specified by an array. This is typically used
to complement an earlier call to platform_register_drivers(). Drivers are
unregistered in the reverse order in which they were registered.

struct [device](infrastructure.md#c.device "device") \*platform_find_device_by_driver(struct [device](infrastructure.md#c.device "device") \*start, const struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*drv)
:   Find a platform device with a given driver.

**Parameters**

`struct device *start`
:   The device to start the search from.

`const struct device_driver *drv`
:   The device driver to look for.

struct [device](infrastructure.md#c.device "device") \*bus_find_device_by_name(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, struct [device](infrastructure.md#c.device "device") \*start, const char \*name)
:   device iterator for locating a particular device of a specific name.

**Parameters**

`const struct bus_type *bus`
:   bus type

`struct device *start`
:   Device to begin with

`const char *name`
:   name of the device to match

struct [device](infrastructure.md#c.device "device") \*bus_find_device_by_of_node(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, const struct device_node \*np)
:   device iterator for locating a particular device matching the of_node.

**Parameters**

`const struct bus_type *bus`
:   bus type

`const struct device_node *np`
:   of_node of the device to match.

struct [device](infrastructure.md#c.device "device") \*bus_find_device_by_fwnode(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, const struct fwnode_handle \*fwnode)
:   device iterator for locating a particular device matching the fwnode.

**Parameters**

`const struct bus_type *bus`
:   bus type

`const struct fwnode_handle *fwnode`
:   fwnode of the device to match.

struct [device](infrastructure.md#c.device "device") \*bus_find_device_by_devt(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, dev_t devt)
:   device iterator for locating a particular device matching the device type.

**Parameters**

`const struct bus_type *bus`
:   bus type

`dev_t devt`
:   device type of the device to match.

struct [device](infrastructure.md#c.device "device") \*bus_find_next_device(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, struct [device](infrastructure.md#c.device "device") \*cur)
:   Find the next device after a given device in a given bus.

**Parameters**

`const struct bus_type *bus`
:   bus type

`struct device *cur`
:   device to begin the search with.

struct [device](infrastructure.md#c.device "device") \*bus_find_device_by_acpi_dev(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, const struct acpi_device \*adev)
:   device iterator for locating a particular device matching the ACPI COMPANION device.

**Parameters**

`const struct bus_type *bus`
:   bus type

`const struct acpi_device *adev`
:   ACPI COMPANION device to match.

int bus_for_each_dev(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, struct [device](infrastructure.md#c.device "device") \*start, void \*data, int (\*fn)(struct [device](infrastructure.md#c.device "device")\*, void\*))
:   device iterator.

**Parameters**

`const struct bus_type *bus`
:   bus type.

`struct device *start`
:   device to start iterating from.

`void *data`
:   data for the callback.

`int (*fn)(struct device *, void *)`
:   function to be called for each device.

**Description**

Iterate over **bus**'s list of devices, and call **fn** for each,
passing it **data**. If **start** is not NULL, we use that device to
begin iterating from.

We check the return of **fn** each time. If it returns anything
other than 0, we break out and return that value.

**NOTE**

The device that returns a non-zero value is not retained
in any way, nor is its refcount incremented. If the caller needs
to retain this data, it should do so, and increment the reference
count in the supplied callback.

struct [device](infrastructure.md#c.device "device") \*bus_find_device(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, struct [device](infrastructure.md#c.device "device") \*start, const void \*data, int (\*match)(struct [device](infrastructure.md#c.device "device") \*dev, const void \*data))
:   device iterator for locating a particular device.

**Parameters**

`const struct bus_type *bus`
:   bus type

`struct device *start`
:   Device to begin with

`const void *data`
:   Data to pass to match function

`int (*match)(struct device *dev, const void *data)`
:   Callback function to check device

**Description**

This is similar to the [`bus_for_each_dev()`](infrastructure.md#c.bus_for_each_dev "bus_for_each_dev") function above, but it
returns a reference to a device that is 'found' for later use, as
determined by the **match** callback.

The callback should return 0 if the device doesn't match and non-zero
if it does. If the callback returns non-zero, this function will
return to the caller and not iterate over any more devices.

int bus_for_each_drv(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus, struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*start, void \*data, int (\*fn)(struct [device_driver](infrastructure.md#c.device_driver "device_driver")\*, void\*))
:   driver iterator

**Parameters**

`const struct bus_type *bus`
:   bus we're dealing with.

`struct device_driver *start`
:   driver to start iterating on.

`void *data`
:   data to pass to the callback.

`int (*fn)(struct device_driver *, void *)`
:   function to call for each driver.

**Description**

This is nearly identical to the device iterator above.
We iterate over each driver that belongs to **bus**, and call
**fn** for each. If **fn** returns anything but 0, we break out
and return it. If **start** is not NULL, we use it as the head
of the list.

**NOTE**

we don't return the driver that returns a non-zero
value, nor do we leave the reference count incremented for that
driver. If the caller needs to know that info, it must set it
in the callback. It must also be sure to increment the refcount
so it doesn't disappear before returning to the caller.

int bus_rescan_devices(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus)
:   rescan devices on the bus for possible drivers

**Parameters**

`const struct bus_type *bus`
:   the bus to scan.

**Description**

This function will look for devices on the bus with no driver
attached and rescan it against existing drivers to see if it matches
any by calling [`device_attach()`](infrastructure.md#c.device_attach "device_attach") for the unbound devices.

int device_reprobe(struct [device](infrastructure.md#c.device "device") \*dev)
:   remove driver for a device and probe for a new driver

**Parameters**

`struct device *dev`
:   the device to reprobe

**Description**

This function detaches the attached driver (if any) for the given
device and restarts the driver probing process. It is intended
to use if probing criteria changed during a devices lifetime and
driver attachment should change accordingly.

int bus_register(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus)
:   register a driver-core subsystem

**Parameters**

`const struct bus_type *bus`
:   bus to register

**Description**

Once we have that, we register the bus with the kobject
infrastructure, then register the children subsystems it has:
the devices and drivers that belong to the subsystem.

void bus_unregister(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus)
:   remove a bus from the system

**Parameters**

`const struct bus_type *bus`
:   bus.

**Description**

Unregister the child subsystems and the bus itself.
Finally, we call bus_put() to release the refcount

int subsys_system_register(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*subsys, const struct attribute_group \*\*groups)
:   register a subsystem at /sys/devices/system/

**Parameters**

`const struct bus_type *subsys`
:   system subsystem

`const struct attribute_group **groups`
:   default attributes for the root device

**Description**

All 'system' subsystems have a /sys/devices/system/<name> root device
with the name of the subsystem. The root device can carry subsystem-
wide attributes. All registered devices are below this single root
device and are named after the subsystem with a simple enumeration
number appended. The registered devices are not explicitly named;
only 'id' in the device needs to be set.

Do not use this interface for anything new, it exists for compatibility
with bad ideas only. New subsystems should use plain subsystems; and
add the subsystem-wide attributes should be added to the subsystem
directory itself and not some create fake root-device placed in
/sys/devices/system/<name>.

int subsys_virtual_register(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*subsys, const struct attribute_group \*\*groups)
:   register a subsystem at /sys/devices/virtual/

**Parameters**

`const struct bus_type *subsys`
:   virtual subsystem

`const struct attribute_group **groups`
:   default attributes for the root device

**Description**

All 'virtual' subsystems have a /sys/devices/system/<name> root device
with the name of the subystem. The root device can carry subsystem-wide
attributes. All registered devices are below this single root device.
There's no restriction on device naming. This is for kernel software
constructs which need sysfs interface.

struct [device_driver](infrastructure.md#c.device_driver "device_driver") \*driver_find(const char \*name, const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus)
:   locate driver on a bus by its name.

**Parameters**

`const char *name`
:   name of the driver.

`const struct bus_type *bus`
:   bus to scan for the driver.

**Description**

Call [`kset_find_obj()`](basics.md#c.kset_find_obj "kset_find_obj") to iterate over list of drivers on
a bus to find driver by name. Return driver if found.

This routine provides no locking to prevent the driver it returns
from being unregistered or unloaded while the caller is using it.
The caller is responsible for preventing this.

struct [device](infrastructure.md#c.device "device") \*bus_get_dev_root(const struct [bus_type](infrastructure.md#c.bus_type "bus_type") \*bus)
:   return a pointer to the "device root" of a bus

**Parameters**

`const struct bus_type *bus`
:   bus to return the device root of.

**Description**

If a bus has a "device root" structure, return it, WITH THE REFERENCE
COUNT INCREMENTED.

Note, when finished with the device, a call to [`put_device()`](infrastructure.md#c.put_device "put_device") is required.

If the device root is not present (or bus is not a valid pointer), NULL
will be returned.

## Device Drivers DMA Management

void dmam_free_coherent(struct [device](infrastructure.md#c.device "device") \*dev, size_t size, void \*vaddr, dma_addr_t dma_handle)
:   Managed dma_free_coherent()

**Parameters**

`struct device *dev`
:   Device to free coherent memory for

`size_t size`
:   Size of allocation

`void *vaddr`
:   Virtual address of the memory to free

`dma_addr_t dma_handle`
:   DMA handle of the memory to free

**Description**

Managed dma_free_coherent().

void \*dmam_alloc_attrs(struct [device](infrastructure.md#c.device "device") \*dev, size_t size, dma_addr_t \*dma_handle, gfp_t gfp, unsigned long attrs)
:   Managed dma_alloc_attrs()

**Parameters**

`struct device *dev`
:   Device to allocate non_coherent memory for

`size_t size`
:   Size of allocation

`dma_addr_t *dma_handle`
:   Out argument for allocated DMA handle

`gfp_t gfp`
:   Allocation flags

`unsigned long attrs`
:   Flags in the DMA_ATTR_\* namespace.

**Description**

Managed dma_alloc_attrs(). Memory allocated using this function will be
automatically released on driver detach.

**Return**

Pointer to allocated memory on success, NULL on failure.

unsigned int dma_map_sg_attrs(struct [device](infrastructure.md#c.device "device") \*dev, struct scatterlist \*sg, int nents, enum dma_data_direction dir, unsigned long attrs)
:   Map the given buffer for DMA

**Parameters**

`struct device *dev`
:   The device for which to perform the DMA operation

`struct scatterlist *sg`
:   The sg_table object describing the buffer

`int nents`
:   Number of entries to map

`enum dma_data_direction dir`
:   DMA direction

`unsigned long attrs`
:   Optional DMA attributes for the map operation

**Description**

Maps a buffer described by a scatterlist passed in the sg argument with
nents segments for the **dir** DMA operation by the **dev** device.

Returns the number of mapped entries (which can be less than nents)
on success. Zero is returned for any error.

dma_unmap_sg_attrs() should be used to unmap the buffer with the
original sg and original nents (not the value returned by this funciton).

int dma_map_sgtable(struct [device](infrastructure.md#c.device "device") \*dev, struct sg_table \*sgt, enum dma_data_direction dir, unsigned long attrs)
:   Map the given buffer for DMA

**Parameters**

`struct device *dev`
:   The device for which to perform the DMA operation

`struct sg_table *sgt`
:   The sg_table object describing the buffer

`enum dma_data_direction dir`
:   DMA direction

`unsigned long attrs`
:   Optional DMA attributes for the map operation

**Description**

Maps a buffer described by a scatterlist stored in the given sg_table
object for the **dir** DMA operation by the **dev** device. After success, the
ownership for the buffer is transferred to the DMA domain. One has to
call dma_sync_sgtable_for_cpu() or dma_unmap_sgtable() to move the
ownership of the buffer back to the CPU domain before touching the
buffer by the CPU.

Returns 0 on success or a negative error code on error. The following
error codes are supported with the given meaning:

> `-EINVAL`
> :   An invalid argument, unaligned access or other error
>     in usage. Will not succeed if retried.
>
> `-ENOMEM`
> :   Insufficient resources (like memory or IOVA space) to
>     complete the mapping. Should succeed if retried later.
>
> `-EIO`
> :   Legacy error code with an unknown meaning. eg. this is
>     returned if a lower level call returned
>     DMA_MAPPING_ERROR.
>
> `-EREMOTEIO`
> :   The DMA device cannot access P2PDMA memory specified
>     in the sg_table. This will not succeed if retried.

bool dma_can_mmap(struct [device](infrastructure.md#c.device "device") \*dev)
:   check if a given device supports dma_mmap_\*

**Parameters**

`struct device *dev`
:   device to check

**Description**

Returns `true` if **dev** supports dma_mmap_coherent() and [`dma_mmap_attrs()`](infrastructure.md#c.dma_mmap_attrs "dma_mmap_attrs") to
map DMA allocations to userspace.

int dma_mmap_attrs(struct [device](infrastructure.md#c.device "device") \*dev, struct vm_area_struct \*vma, void \*cpu_addr, dma_addr_t dma_addr, size_t size, unsigned long attrs)
:   map a coherent DMA allocation into user space

**Parameters**

`struct device *dev`
:   valid [`struct device`](infrastructure.md#c.device "device") pointer, or NULL for ISA and EISA-like devices

`struct vm_area_struct *vma`
:   vm_area_struct describing requested user mapping

`void *cpu_addr`
:   kernel CPU-view address returned from dma_alloc_attrs

`dma_addr_t dma_addr`
:   device-view address returned from dma_alloc_attrs

`size_t size`
:   size of memory originally requested in dma_alloc_attrs

`unsigned long attrs`
:   attributes of mapping properties requested in dma_alloc_attrs

**Description**

Map a coherent DMA buffer previously allocated by dma_alloc_attrs into user
space. The coherent DMA buffer must not be freed by the driver until the
user space mapping has been released.

bool dma_addressing_limited(struct [device](infrastructure.md#c.device "device") \*dev)
:   return if the device is addressing limited

**Parameters**

`struct device *dev`
:   device to check

**Description**

Return `true` if the devices DMA mask is too small to address all memory in
the system, else `false`. Lack of addressing bits is the prime reason for
bounce buffering, but might not be the only one.

## Device drivers PnP support

int pnp_register_protocol(struct pnp_protocol \*protocol)
:   adds a pnp protocol to the pnp layer

**Parameters**

`struct pnp_protocol *protocol`
:   pointer to the corresponding pnp_protocol structure

    Ex protocols: ISAPNP, PNPBIOS, etc

void pnp_unregister_protocol(struct pnp_protocol \*protocol)
:   removes a pnp protocol from the pnp layer

**Parameters**

`struct pnp_protocol *protocol`
:   pointer to the corresponding pnp_protocol structure

struct pnp_dev \*pnp_request_card_device(struct pnp_card_link \*clink, const char \*id, struct pnp_dev \*from)
:   Searches for a PnP device under the specified card

**Parameters**

`struct pnp_card_link *clink`
:   pointer to the card link, cannot be NULL

`const char *id`
:   pointer to a PnP ID structure that explains the rules for finding the device

`struct pnp_dev *from`
:   Starting place to search from. If NULL it will start from the beginning.

void pnp_release_card_device(struct pnp_dev \*dev)
:   call this when the driver no longer needs the device

**Parameters**

`struct pnp_dev *dev`
:   pointer to the PnP device structure

int pnp_register_card_driver(struct pnp_card_driver \*drv)
:   registers a PnP card driver with the PnP Layer

**Parameters**

`struct pnp_card_driver *drv`
:   pointer to the driver to register

void pnp_unregister_card_driver(struct pnp_card_driver \*drv)
:   unregisters a PnP card driver from the PnP Layer

**Parameters**

`struct pnp_card_driver *drv`
:   pointer to the driver to unregister

struct pnp_id \*pnp_add_id(struct pnp_dev \*dev, const char \*id)
:   adds an EISA id to the specified device

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired device

`const char *id`
:   pointer to an EISA id string

int pnp_start_dev(struct pnp_dev \*dev)
:   low-level start of the PnP device

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired device

**Description**

assumes that resources have already been allocated

int pnp_stop_dev(struct pnp_dev \*dev)
:   low-level disable of the PnP device

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired device

**Description**

does not free resources

int pnp_activate_dev(struct pnp_dev \*dev)
:   activates a PnP device for use

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired device

**Description**

does not validate or set resources so be careful.

int pnp_disable_dev(struct pnp_dev \*dev)
:   disables device

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired device

**Description**

inform the correct pnp protocol so that resources can be used by other devices

int pnp_is_active(struct pnp_dev \*dev)
:   Determines if a device is active based on its current resources

**Parameters**

`struct pnp_dev *dev`
:   pointer to the desired PnP device

## Userspace IO devices

void uio_event_notify(struct [uio_info](infrastructure.md#c.uio_info "uio_info") \*info)
:   trigger an interrupt event

**Parameters**

`struct uio_info *info`
:   UIO device capabilities

int __uio_register_device(struct module \*owner, struct [device](infrastructure.md#c.device "device") \*parent, struct [uio_info](infrastructure.md#c.uio_info "uio_info") \*info)
:   register a new userspace IO device

**Parameters**

`struct module *owner`
:   module that creates the new device

`struct device *parent`
:   parent device

`struct uio_info *info`
:   UIO device capabilities

**Description**

returns zero on success or a negative error code.

int __devm_uio_register_device(struct module \*owner, struct [device](infrastructure.md#c.device "device") \*parent, struct [uio_info](infrastructure.md#c.uio_info "uio_info") \*info)
:   Resource managed [`uio_register_device()`](infrastructure.md#c.uio_register_device "uio_register_device")

**Parameters**

`struct module *owner`
:   module that creates the new device

`struct device *parent`
:   parent device

`struct uio_info *info`
:   UIO device capabilities

**Description**

returns zero on success or a negative error code.

void uio_unregister_device(struct [uio_info](infrastructure.md#c.uio_info "uio_info") \*info)
:   unregister a industrial IO device

**Parameters**

`struct uio_info *info`
:   UIO device capabilities

struct uio_mem
:   description of a UIO memory region

**Definition**:

```
struct uio_mem {
    const char              *name;
    phys_addr_t addr;
    unsigned long           offs;
    resource_size_t size;
    int memtype;
    void __iomem            *internal_addr;
    struct uio_map          *map;
};
```

**Members**

`name`
:   name of the memory region for identification

`addr`
:   address of the device's memory rounded to page
    size (phys_addr is used since addr can be
    logical, virtual, or physical & phys_addr_t
    should always be large enough to handle any of
    the address types)

`offs`
:   offset of device memory within the page

`size`
:   size of IO (multiple of page size)

`memtype`
:   type of memory addr points to

`internal_addr`
:   ioremap-ped version of addr, for driver internal use

`map`
:   for use by the UIO core only.

struct uio_port
:   description of a UIO port region

**Definition**:

```
struct uio_port {
    const char              *name;
    unsigned long           start;
    unsigned long           size;
    int porttype;
    struct uio_portio       *portio;
};
```

**Members**

`name`
:   name of the port region for identification

`start`
:   start of port region

`size`
:   size of port region

`porttype`
:   type of port (see UIO_PORT_\* below)

`portio`
:   for use by the UIO core only.

struct uio_info
:   UIO device capabilities

**Definition**:

```
struct uio_info {
    struct uio_device       *uio_dev;
    const char              *name;
    const char              *version;
    struct uio_mem          mem[MAX_UIO_MAPS];
    struct uio_port         port[MAX_UIO_PORT_REGIONS];
    long irq;
    unsigned long           irq_flags;
    void *priv;
    irqreturn_t (*handler)(int irq, struct uio_info *dev_info);
    int (*mmap)(struct uio_info *info, struct vm_area_struct *vma);
    int (*open)(struct uio_info *info, struct inode *inode);
    int (*release)(struct uio_info *info, struct inode *inode);
    int (*irqcontrol)(struct uio_info *info, s32 irq_on);
};
```

**Members**

`uio_dev`
:   the UIO device this info belongs to

`name`
:   device name

`version`
:   device driver version

`mem`
:   list of mappable memory regions, size==0 for end of list

`port`
:   list of port regions, size==0 for end of list

`irq`
:   interrupt number or UIO_IRQ_CUSTOM

`irq_flags`
:   flags for [`request_irq()`](../core-api/genericirq.md#c.request_irq "request_irq")

`priv`
:   optional private data

`handler`
:   the device's irq handler

`mmap`
:   mmap operation for this uio device

`open`
:   open operation for this uio device

`release`
:   release operation for this uio device

`irqcontrol`
:   disable/enable irqs when 0/1 is written to /dev/uioX

uio_register_device

`uio_register_device (parent, info)`

> register a new userspace IO device

**Parameters**

`parent`
:   parent device

`info`
:   UIO device capabilities

**Description**

returns zero on success or a negative error code.

devm_uio_register_device

`devm_uio_register_device (parent, info)`

> Resource managed [`uio_register_device()`](infrastructure.md#c.uio_register_device "uio_register_device")

**Parameters**

`parent`
:   parent device

`info`
:   UIO device capabilities

**Description**

returns zero on success or a negative error code.
