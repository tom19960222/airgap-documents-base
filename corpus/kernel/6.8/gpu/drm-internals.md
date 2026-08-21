---
collection: kernel
version: "6.8"
title: "DRM Internals"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/drm-internals.html
fetched_at: 2026-08-21T03:38:57+00:00
---
# DRM Internals

This chapter documents DRM internals relevant to driver authors and
developers working to add support for the latest features to existing
drivers.

First, we go over some typical driver initialization requirements, like
setting up command buffers, creating an initial output configuration,
and initializing core services. Subsequent sections cover core internals
in more detail, providing implementation notes and examples.

The DRM layer provides several services to graphics drivers, many of
them driven by the application interfaces it provides through libdrm,
the library that wraps most of the DRM ioctls. These include vblank
event handling, memory management, output management, framebuffer
management, command submission & fencing, suspend/resume support, and
DMA services.

## Driver Initialization

At the core of every DRM driver is a [`struct drm_driver`](drm-internals.md#c.drm_driver "drm_driver") structure. Drivers typically statically initialize
a drm_driver structure, and then pass it to
[`drm_dev_alloc()`](drm-internals.md#c.drm_dev_alloc "drm_dev_alloc") to allocate a device instance. After the
device instance is fully initialized it can be registered (which makes
it accessible from userspace) using [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register").

The [`struct drm_driver`](drm-internals.md#c.drm_driver "drm_driver") structure
contains static information that describes the driver and features it
supports, and pointers to methods that the DRM core will call to
implement the DRM API. We will first go through the [`struct
drm_driver`](drm-internals.md#c.drm_driver "drm_driver") static information fields, and will
then describe individual operations in details as they get used in later
sections.

### Driver Information

#### Major, Minor and Patchlevel

int major; int minor; int patchlevel;
The DRM core identifies driver versions by a major, minor and patch
level triplet. The information is printed to the kernel log at
initialization time and passed to userspace through the
DRM_IOCTL_VERSION ioctl.

The major and minor numbers are also used to verify the requested driver
API version passed to DRM_IOCTL_SET_VERSION. When the driver API
changes between minor versions, applications can call
DRM_IOCTL_SET_VERSION to select a specific version of the API. If the
requested major isn't equal to the driver major, or the requested minor
is larger than the driver minor, the DRM_IOCTL_SET_VERSION call will
return an error. Otherwise the driver's set_version() method will be
called with the requested version.

#### Name, Description and Date

char \*name; char \*desc; char \*date;
The driver name is printed to the kernel log at initialization time,
used for IRQ registration and passed to userspace through
DRM_IOCTL_VERSION.

The driver description is a purely informative string passed to
userspace through the DRM_IOCTL_VERSION ioctl and otherwise unused by
the kernel.

The driver date, formatted as YYYYMMDD, is meant to identify the date of
the latest modification to the driver. However, as most drivers fail to
update it, its value is mostly useless. The DRM core prints it to the
kernel log at initialization time and passes it to userspace through the
DRM_IOCTL_VERSION ioctl.

### Module Initialization

This library provides helpers registering DRM drivers during module
initialization and shutdown. The provided helpers act like bus-specific
module helpers, such as module_pci_driver(), but respect additional
parameters that control DRM driver registration.

Below is an example of initializing a DRM driver for a device on the
PCI bus.

```c
struct pci_driver my_pci_drv = {
};

drm_module_pci_driver(my_pci_drv);
```

The generated code will test if DRM drivers are enabled and register
the PCI driver my_pci_drv. For more complex module initialization, you
can still use [`module_init()`](../driver-api/basics.md#c.module_init "module_init") and [`module_exit()`](../driver-api/basics.md#c.module_exit "module_exit") in your driver.

### Managing Ownership of the Framebuffer Aperture

A graphics device might be supported by different drivers, but only one
driver can be active at any given time. Many systems load a generic
graphics drivers, such as EFI-GOP or VESA, early during the boot process.
During later boot stages, they replace the generic driver with a dedicated,
hardware-specific driver. To take over the device the dedicated driver
first has to remove the generic driver. DRM aperture functions manage
ownership of DRM framebuffer memory and hand-over between drivers.

DRM drivers should call [`drm_aperture_remove_conflicting_framebuffers()`](drm-internals.md#c.drm_aperture_remove_conflicting_framebuffers "drm_aperture_remove_conflicting_framebuffers")
at the top of their probe function. The function removes any generic
driver that is currently associated with the given framebuffer memory.
If the framebuffer is located at PCI BAR 0, the rsp code looks as in the
example given below.

```c
static const struct drm_driver example_driver = {
        ...
};

static int remove_conflicting_framebuffers(struct pci_dev *pdev)
{
        resource_size_t base, size;
        int ret;

        base = pci_resource_start(pdev, 0);
        size = pci_resource_len(pdev, 0);

        return drm_aperture_remove_conflicting_framebuffers(base, size,
                                                            &example_driver);
}

static int probe(struct pci_dev *pdev)
{
        int ret;

        // Remove any generic drivers...
        ret = remove_conflicting_framebuffers(pdev);
        if (ret)
                return ret;

        // ... and initialize the hardware.
        ...

        drm_dev_register();

        return 0;
}
```

PCI device drivers should call
[`drm_aperture_remove_conflicting_pci_framebuffers()`](drm-internals.md#c.drm_aperture_remove_conflicting_pci_framebuffers "drm_aperture_remove_conflicting_pci_framebuffers") and let it detect the
framebuffer apertures automatically. Device drivers without knowledge of
the framebuffer's location shall call [`drm_aperture_remove_framebuffers()`](drm-internals.md#c.drm_aperture_remove_framebuffers "drm_aperture_remove_framebuffers"),
which removes all drivers for known framebuffer.

Drivers that are susceptible to being removed by other drivers, such as
generic EFI or VESA drivers, have to register themselves as owners of their
given framebuffer memory. Ownership of the framebuffer memory is achieved
by calling [`devm_aperture_acquire_from_firmware()`](drm-internals.md#c.devm_aperture_acquire_from_firmware "devm_aperture_acquire_from_firmware"). On success, the driver
is the owner of the framebuffer range. The function fails if the
framebuffer is already owned by another driver. See below for an example.

```c
static int acquire_framebuffers(struct drm_device *dev, struct platform_device *pdev)
{
        resource_size_t base, size;

        mem = platform_get_resource(pdev, IORESOURCE_MEM, 0);
        if (!mem)
                return -EINVAL;
        base = mem->start;
        size = resource_size(mem);

        return devm_acquire_aperture_from_firmware(dev, base, size);
}

static int probe(struct platform_device *pdev)
{
        struct drm_device *dev;
        int ret;

        // ... Initialize the device...
        dev = devm_drm_dev_alloc();
        ...

        // ... and acquire ownership of the framebuffer.
        ret = acquire_framebuffers(dev, pdev);
        if (ret)
                return ret;

        drm_dev_register(dev, 0);

        return 0;
}
```

The generic driver is now subject to forced removal by other drivers. This
only works for platform drivers that support hot unplug.
When a driver calls [`drm_aperture_remove_conflicting_framebuffers()`](drm-internals.md#c.drm_aperture_remove_conflicting_framebuffers "drm_aperture_remove_conflicting_framebuffers") et al.
for the registered framebuffer range, the aperture helpers call
[`platform_device_unregister()`](../driver-api/infrastructure.md#c.platform_device_unregister "platform_device_unregister") and the generic driver unloads itself. It
may not access the device's registers, framebuffer memory, ROM, etc
afterwards.

int drm_aperture_remove_framebuffers(const struct [drm_driver](drm-internals.md#c.drm_driver "drm_driver") \*req_driver)
:   remove all existing framebuffers

**Parameters**

`const struct drm_driver *req_driver`
:   requesting DRM driver

**Description**

This function removes all graphics device drivers. Use this function on systems
that can have their framebuffer located anywhere in memory.

**Return**

0 on success, or a negative errno code otherwise

int devm_aperture_acquire_from_firmware(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, resource_size_t base, resource_size_t size)
:   Acquires ownership of a firmware framebuffer on behalf of a DRM driver.

**Parameters**

`struct drm_device *dev`
:   the DRM device to own the framebuffer memory

`resource_size_t base`
:   the framebuffer's byte offset in physical memory

`resource_size_t size`
:   the framebuffer size in bytes

**Description**

Installs the given device as the new owner of the framebuffer. The function
expects the framebuffer to be provided by a platform device that has been
set up by firmware. Firmware can be any generic interface, such as EFI,
VESA, VGA, etc. If the native hardware driver takes over ownership of the
framebuffer range, the firmware state gets lost. Aperture helpers will then
unregister the platform device automatically. Acquired apertures are
released automatically if the underlying device goes away.

The function fails if the framebuffer range, or parts of it, is currently
owned by another driver. To evict current owners, callers should use
[`drm_aperture_remove_conflicting_framebuffers()`](drm-internals.md#c.drm_aperture_remove_conflicting_framebuffers "drm_aperture_remove_conflicting_framebuffers") et al. before calling this
function. The function also fails if the given device is not a platform
device.

**Return**

0 on success, or a negative errno value otherwise.

int drm_aperture_remove_conflicting_framebuffers(resource_size_t base, resource_size_t size, const struct [drm_driver](drm-internals.md#c.drm_driver "drm_driver") \*req_driver)
:   remove existing framebuffers in the given range

**Parameters**

`resource_size_t base`
:   the aperture's base address in physical memory

`resource_size_t size`
:   aperture size in bytes

`const struct drm_driver *req_driver`
:   requesting DRM driver

**Description**

This function removes graphics device drivers which use the memory range described by
**base** and **size**.

**Return**

0 on success, or a negative errno code otherwise

int drm_aperture_remove_conflicting_pci_framebuffers(struct pci_dev \*pdev, const struct [drm_driver](drm-internals.md#c.drm_driver "drm_driver") \*req_driver)
:   remove existing framebuffers for PCI devices

**Parameters**

`struct pci_dev *pdev`
:   PCI device

`const struct drm_driver *req_driver`
:   requesting DRM driver

**Description**

This function removes graphics device drivers using the memory range configured
for any of **pdev**'s memory bars. The function assumes that a PCI device with
shadowed ROM drives a primary display and so kicks out vga16fb.

**Return**

0 on success, or a negative errno code otherwise

### Device Instance and Driver Handling

A device instance for a drm driver is represented by [`struct drm_device`](drm-internals.md#c.drm_device "drm_device"). This
is allocated and initialized with [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc"), usually from
bus-specific ->probe() callbacks implemented by the driver. The driver then
needs to initialize all the various subsystems for the drm device like memory
management, vblank handling, modesetting support and initial output
configuration plus obviously initialize all the corresponding hardware bits.
Finally when everything is up and running and ready for userspace the device
instance can be published using [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register").

There is also deprecated support for initializing device instances using
bus-specific helpers and the [`drm_driver.load`](drm-internals.md#c.drm_driver "drm_driver") callback. But due to
backwards-compatibility needs the device instance have to be published too
early, which requires unpretty global locking to make safe and is therefore
only support for existing drivers not yet converted to the new scheme.

When cleaning up a device instance everything needs to be done in reverse:
First unpublish the device instance with [`drm_dev_unregister()`](drm-internals.md#c.drm_dev_unregister "drm_dev_unregister"). Then clean up
any other resources allocated at device initialization and drop the driver's
reference to [`drm_device`](drm-internals.md#c.drm_device "drm_device") using [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put").

Note that any allocation or resource which is visible to userspace must be
released only when the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") is called, and not when the
driver is unbound from the underlying physical struct [`device`](../driver-api/infrastructure.md#c.device "device"). Best to use
[`drm_device`](drm-internals.md#c.drm_device "drm_device") managed resources with [`drmm_add_action()`](drm-internals.md#c.drmm_add_action "drmm_add_action"), [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc") and
related functions.

devres managed resources like [`devm_kmalloc()`](../driver-api/basics.md#c.devm_kmalloc "devm_kmalloc") can only be used for resources
directly related to the underlying hardware device, and only used in code
paths fully protected by [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter") and [`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit").

#### Display driver example

The following example shows a typical structure of a DRM display driver.
The example focus on the probe() function and the other functions that is
almost always present and serves as a demonstration of [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc").

```c
struct driver_device {
        struct drm_device drm;
        void *userspace_facing;
        struct clk *pclk;
};

static const struct drm_driver driver_drm_driver = {
        [...]
};

static int driver_probe(struct platform_device *pdev)
{
        struct driver_device *priv;
        struct drm_device *drm;
        int ret;

        priv = devm_drm_dev_alloc(&pdev->dev, &driver_drm_driver,
                                  struct driver_device, drm);
        if (IS_ERR(priv))
                return PTR_ERR(priv);
        drm = &priv->drm;

        ret = drmm_mode_config_init(drm);
        if (ret)
                return ret;

        priv->userspace_facing = drmm_kzalloc(..., GFP_KERNEL);
        if (!priv->userspace_facing)
                return -ENOMEM;

        priv->pclk = devm_clk_get(dev, "PCLK");
        if (IS_ERR(priv->pclk))
                return PTR_ERR(priv->pclk);

        // Further setup, display pipeline etc

        platform_set_drvdata(pdev, drm);

        drm_mode_config_reset(drm);

        ret = drm_dev_register(drm);
        if (ret)
                return ret;

        drm_fbdev_generic_setup(drm, 32);

        return 0;
}

// This function is called before the devm_ resources are released
static int driver_remove(struct platform_device *pdev)
{
        struct drm_device *drm = platform_get_drvdata(pdev);

        drm_dev_unregister(drm);
        drm_atomic_helper_shutdown(drm)

        return 0;
}

// This function is called on kernel restart and shutdown
static void driver_shutdown(struct platform_device *pdev)
{
        drm_atomic_helper_shutdown(platform_get_drvdata(pdev));
}

static int __maybe_unused driver_pm_suspend(struct device *dev)
{
        return drm_mode_config_helper_suspend(dev_get_drvdata(dev));
}

static int __maybe_unused driver_pm_resume(struct device *dev)
{
        drm_mode_config_helper_resume(dev_get_drvdata(dev));

        return 0;
}

static const struct dev_pm_ops driver_pm_ops = {
        SET_SYSTEM_SLEEP_PM_OPS(driver_pm_suspend, driver_pm_resume)
};

static struct platform_driver driver_driver = {
        .driver = {
                [...]
                .pm = &driver_pm_ops,
        },
        .probe = driver_probe,
        .remove = driver_remove,
        .shutdown = driver_shutdown,
};
module_platform_driver(driver_driver);
```

Drivers that want to support device unplugging (USB, DT overlay unload) should
use [`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug") instead of [`drm_dev_unregister()`](drm-internals.md#c.drm_dev_unregister "drm_dev_unregister"). The driver must protect
regions that is accessing device resources to prevent use after they're
released. This is done using [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter") and [`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit"). There is one
shortcoming however, [`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug") marks the drm_device as unplugged before
[`drm_atomic_helper_shutdown()`](drm-kms-helpers.md#c.drm_atomic_helper_shutdown "drm_atomic_helper_shutdown") is called. This means that if the disable code
paths are protected, they will not run on regular driver module unload,
possibly leaving the hardware enabled.

enum switch_power_state
:   power state of drm device

**Constants**

`DRM_SWITCH_POWER_ON`
:   Power state is ON

`DRM_SWITCH_POWER_OFF`
:   Power state is OFF

`DRM_SWITCH_POWER_CHANGING`
:   Power state is changing

`DRM_SWITCH_POWER_DYNAMIC_OFF`
:   Suspended

struct drm_device
:   DRM device structure

**Definition**:

```
struct drm_device {
    int if_version;
    struct kref ref;
    struct device *dev;
    struct {
        struct list_head resources;
        void *final_kfree;
        spinlock_t lock;
    } managed;
    const struct drm_driver *driver;
    void *dev_private;
    struct drm_minor *primary;
    struct drm_minor *render;
    struct drm_minor *accel;
    bool registered;
    struct drm_master *master;
    u32 driver_features;
    bool unplugged;
    struct inode *anon_inode;
    char *unique;
    struct mutex struct_mutex;
    struct mutex master_mutex;
    atomic_t open_count;
    struct mutex filelist_mutex;
    struct list_head filelist;
    struct list_head filelist_internal;
    struct mutex clientlist_mutex;
    struct list_head clientlist;
    bool vblank_disable_immediate;
    struct drm_vblank_crtc *vblank;
    spinlock_t vblank_time_lock;
    spinlock_t vbl_lock;
    u32 max_vblank_count;
    struct list_head vblank_event_list;
    spinlock_t event_lock;
    unsigned int num_crtcs;
    struct drm_mode_config mode_config;
    struct mutex object_name_lock;
    struct idr object_name_idr;
    struct drm_vma_offset_manager *vma_offset_manager;
    struct drm_vram_mm *vram_mm;
    enum switch_power_state switch_power_state;
    struct drm_fb_helper *fb_helper;
    struct dentry *debugfs_root;
};
```

**Members**

`if_version`
:   Highest interface version set

`ref`
:   Object ref-count

`dev`
:   Device structure of bus-device

`managed`
:   Managed resources linked to the lifetime of this [`drm_device`](drm-internals.md#c.drm_device "drm_device") as
    tracked by **ref**.

`driver`
:   DRM driver managing the device

`dev_private`
:   DRM driver private data. This is deprecated and should be left set to
    NULL.

    Instead of using this pointer it is recommended that drivers use
    [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc") and embed struct [`drm_device`](drm-internals.md#c.drm_device "drm_device") in their larger
    per-device structure.

`primary`
:   Primary node. Drivers should not interact with this
    directly. debugfs interfaces can be registered with
    [`drm_debugfs_add_file()`](drm-uapi.md#c.drm_debugfs_add_file "drm_debugfs_add_file"), and sysfs should be directly added on the
    hardware (and not character device node) [`struct device`](../driver-api/infrastructure.md#c.device "device") **dev**.

`render`
:   Render node. Drivers should not interact with this directly ever.
    Drivers should not expose any additional interfaces in debugfs or
    sysfs on this node.

`accel`
:   Compute Acceleration node

`registered`
:   Internally used by [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register") and [`drm_connector_register()`](drm-kms.md#c.drm_connector_register "drm_connector_register").

`master`
:   Currently active master for this device.
    Protected by `master_mutex`

`driver_features`
:   per-device driver features

    Drivers can clear specific flags here to disallow
    certain features on a per-device basis while still
    sharing a single [`struct drm_driver`](drm-internals.md#c.drm_driver "drm_driver") instance across
    all devices.

`unplugged`
:   Flag to tell if the device has been unplugged.
    See [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter") and [`drm_dev_is_unplugged()`](drm-internals.md#c.drm_dev_is_unplugged "drm_dev_is_unplugged").

`anon_inode`
:   inode for private address-space

`unique`
:   Unique name of the device

`struct_mutex`
:   Lock for others (not [`drm_minor.master`](drm-internals.md#c.drm_minor "drm_minor") and [`drm_file.is_master`](drm-internals.md#c.drm_file "drm_file"))

    TODO: This lock used to be the BKL of the DRM subsystem. Move the
    :   lock into i915, which is the only remaining user.

`master_mutex`
:   Lock for [`drm_minor.master`](drm-internals.md#c.drm_minor "drm_minor") and [`drm_file.is_master`](drm-internals.md#c.drm_file "drm_file")

`open_count`
:   Usage counter for outstanding files open,
    protected by drm_global_mutex

`filelist_mutex`
:   Protects **filelist**.

`filelist`
:   List of userspace clients, linked through [`drm_file.lhead`](drm-internals.md#c.drm_file "drm_file").

`filelist_internal`
:   List of open DRM files for in-kernel clients.
    Protected by `filelist_mutex`.

`clientlist_mutex`
:   Protects `clientlist` access.

`clientlist`
:   List of in-kernel clients. Protected by `clientlist_mutex`.

`vblank_disable_immediate`
:   If true, vblank interrupt will be disabled immediately when the
    refcount drops to zero, as opposed to via the vblank disable
    timer.

    This can be set to true it the hardware has a working vblank counter
    with high-precision timestamping (otherwise there are races) and the
    driver uses [`drm_crtc_vblank_on()`](drm-kms.md#c.drm_crtc_vblank_on "drm_crtc_vblank_on") and [`drm_crtc_vblank_off()`](drm-kms.md#c.drm_crtc_vblank_off "drm_crtc_vblank_off")
    appropriately. See also **max_vblank_count** and
    [`drm_crtc_funcs.get_vblank_counter`](drm-kms.md#c.drm_crtc_funcs "drm_crtc_funcs").

`vblank`
:   Array of vblank tracking structures, one per [`struct drm_crtc`](drm-kms.md#c.drm_crtc "drm_crtc"). For
    historical reasons (vblank support predates kernel modesetting) this
    is free-standing and not part of [`struct drm_crtc`](drm-kms.md#c.drm_crtc "drm_crtc") itself. It must be
    initialized explicitly by calling [`drm_vblank_init()`](drm-kms.md#c.drm_vblank_init "drm_vblank_init").

`vblank_time_lock`
:   Protects vblank count and time updates during vblank enable/disable

`vbl_lock`
:   Top-level vblank references lock, wraps the low-level
    **vblank_time_lock**.

`max_vblank_count`
:   Maximum value of the vblank registers. This value +1 will result in a
    wrap-around of the vblank register. It is used by the vblank core to
    handle wrap-arounds.

    If set to zero the vblank core will try to guess the elapsed vblanks
    between times when the vblank interrupt is disabled through
    high-precision timestamps. That approach is suffering from small
    races and imprecision over longer time periods, hence exposing a
    hardware vblank counter is always recommended.

    This is the statically configured device wide maximum. The driver
    can instead choose to use a runtime configurable per-crtc value
    [`drm_vblank_crtc.max_vblank_count`](drm-kms.md#c.drm_vblank_crtc "drm_vblank_crtc"), in which case **max_vblank_count**
    must be left at zero. See [`drm_crtc_set_max_vblank_count()`](drm-kms.md#c.drm_crtc_set_max_vblank_count "drm_crtc_set_max_vblank_count") on how
    to use the per-crtc value.

    If non-zero, [`drm_crtc_funcs.get_vblank_counter`](drm-kms.md#c.drm_crtc_funcs "drm_crtc_funcs") must be set.

`vblank_event_list`
:   List of vblank events

`event_lock`
:   Protects **vblank_event_list** and event delivery in
    general. See [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") and [`drm_send_event_locked()`](drm-internals.md#c.drm_send_event_locked "drm_send_event_locked").

`num_crtcs`
:   Number of CRTCs on this device

`mode_config`
:   Current mode config

`object_name_lock`
:   GEM information

`object_name_idr`
:   GEM information

`vma_offset_manager`
:   GEM information

`vram_mm`
:   VRAM MM memory manager

`switch_power_state`
:   Power state of the client.
    Used by drivers supporting the switcheroo driver.
    The state is maintained in the
    [`vga_switcheroo_client_ops.set_gpu_state`](vga-switcheroo.md#c.vga_switcheroo_client_ops "vga_switcheroo_client_ops") callback

`fb_helper`
:   Pointer to the fbdev emulation structure.
    Set by [`drm_fb_helper_init()`](drm-kms-helpers.md#c.drm_fb_helper_init "drm_fb_helper_init") and cleared by [`drm_fb_helper_fini()`](drm-kms-helpers.md#c.drm_fb_helper_fini "drm_fb_helper_fini").

`debugfs_root`
:   Root directory for debugfs files.

**Description**

This structure represent a complete card that
may contain multiple heads.

enum drm_driver_feature
:   feature flags

**Constants**

`DRIVER_GEM`
:   Driver use the GEM memory manager. This should be set for all modern
    drivers.

`DRIVER_MODESET`
:   Driver supports mode setting interfaces (KMS).

`DRIVER_RENDER`
:   Driver supports dedicated render nodes. See also the [section on
    render nodes](drm-uapi.md#drm-render-node) for details.

`DRIVER_ATOMIC`
:   Driver supports the full atomic modesetting userspace API. Drivers
    which only use atomic internally, but do not support the full
    userspace API (e.g. not all properties converted to atomic, or
    multi-plane updates are not guaranteed to be tear-free) should not
    set this flag.

`DRIVER_SYNCOBJ`
:   Driver supports [`drm_syncobj`](drm-mm.md#c.drm_syncobj "drm_syncobj") for explicit synchronization of command
    submission.

`DRIVER_SYNCOBJ_TIMELINE`
:   Driver supports the timeline flavor of [`drm_syncobj`](drm-mm.md#c.drm_syncobj "drm_syncobj") for explicit
    synchronization of command submission.

`DRIVER_COMPUTE_ACCEL`
:   Driver supports compute acceleration devices. This flag is mutually exclusive with
    **DRIVER_RENDER** and **DRIVER_MODESET**. Devices that support both graphics and compute
    acceleration should be handled by two drivers that are connected using auxiliary bus.

`DRIVER_GEM_GPUVA`
:   Driver supports user defined GPU VA bindings for GEM objects.

`DRIVER_CURSOR_HOTSPOT`
:   Driver supports and requires cursor hotspot information in the
    cursor plane (e.g. cursor plane has to actually track the mouse
    cursor and the clients are required to set hotspot in order for
    the cursor planes to work correctly).

`DRIVER_USE_AGP`
:   Set up DRM AGP support, see drm_agp_init(), the DRM core will manage
    AGP resources. New drivers don't need this.

`DRIVER_LEGACY`
:   Denote a legacy driver using shadow attach. Do not use.

`DRIVER_PCI_DMA`
:   Driver is capable of PCI DMA, mapping of PCI DMA buffers to userspace
    will be enabled. Only for legacy drivers. Do not use.

`DRIVER_SG`
:   Driver can perform scatter/gather DMA, allocation and mapping of
    scatter/gather buffers will be enabled. Only for legacy drivers. Do
    not use.

`DRIVER_HAVE_DMA`
:   Driver supports DMA, the userspace DMA API will be supported. Only
    for legacy drivers. Do not use.

`DRIVER_HAVE_IRQ`
:   Legacy irq support. Only for legacy drivers. Do not use.

**Description**

See [`drm_driver.driver_features`](drm-internals.md#c.drm_driver "drm_driver"), drm_device.driver_features and
[`drm_core_check_feature()`](drm-internals.md#c.drm_core_check_feature "drm_core_check_feature").

struct drm_driver
:   DRM driver structure

**Definition**:

```
struct drm_driver {
    int (*load) (struct drm_device *, unsigned long flags);
    int (*open) (struct drm_device *, struct drm_file *);
    void (*postclose) (struct drm_device *, struct drm_file *);
    void (*lastclose) (struct drm_device *);
    void (*unload) (struct drm_device *);
    void (*release) (struct drm_device *);
    void (*master_set)(struct drm_device *dev, struct drm_file *file_priv, bool from_open);
    void (*master_drop)(struct drm_device *dev, struct drm_file *file_priv);
    void (*debugfs_init)(struct drm_minor *minor);
    struct drm_gem_object *(*gem_create_object)(struct drm_device *dev, size_t size);
    int (*prime_handle_to_fd)(struct drm_device *dev, struct drm_file *file_priv, uint32_t handle, uint32_t flags, int *prime_fd);
    int (*prime_fd_to_handle)(struct drm_device *dev, struct drm_file *file_priv, int prime_fd, uint32_t *handle);
    struct drm_gem_object * (*gem_prime_import)(struct drm_device *dev, struct dma_buf *dma_buf);
    struct drm_gem_object *(*gem_prime_import_sg_table)(struct drm_device *dev,struct dma_buf_attachment *attach, struct sg_table *sgt);
    int (*dumb_create)(struct drm_file *file_priv,struct drm_device *dev, struct drm_mode_create_dumb *args);
    int (*dumb_map_offset)(struct drm_file *file_priv,struct drm_device *dev, uint32_t handle, uint64_t *offset);
    void (*show_fdinfo)(struct drm_printer *p, struct drm_file *f);
    int major;
    int minor;
    int patchlevel;
    char *name;
    char *desc;
    char *date;
    u32 driver_features;
    const struct drm_ioctl_desc *ioctls;
    int num_ioctls;
    const struct file_operations *fops;
};
```

**Members**

`load`
:   Backward-compatible driver callback to complete initialization steps
    after the driver is registered. For this reason, may suffer from
    race conditions and its use is deprecated for new drivers. It is
    therefore only supported for existing drivers not yet converted to
    the new scheme. See [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc") and [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register") for
    proper and race-free way to set up a [`struct drm_device`](drm-internals.md#c.drm_device "drm_device").

    This is deprecated, do not use!

    Returns:

    Zero on success, non-zero value on failure.

`open`
:   Driver callback when a new [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") is opened. Useful for
    setting up driver-private data structures like buffer allocators,
    execution contexts or similar things. Such driver-private resources
    must be released again in **postclose**.

    Since the display/modeset side of DRM can only be owned by exactly
    one [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") (see [`drm_file.is_master`](drm-internals.md#c.drm_file "drm_file") and [`drm_device.master`](drm-internals.md#c.drm_device "drm_device"))
    there should never be a need to set up any modeset related resources
    in this callback. Doing so would be a driver design bug.

    Returns:

    0 on success, a negative error code on failure, which will be
    promoted to userspace as the result of the open() system call.

`postclose`
:   One of the driver callbacks when a new [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") is closed.
    Useful for tearing down driver-private data structures allocated in
    **open** like buffer allocators, execution contexts or similar things.

    Since the display/modeset side of DRM can only be owned by exactly
    one [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") (see [`drm_file.is_master`](drm-internals.md#c.drm_file "drm_file") and [`drm_device.master`](drm-internals.md#c.drm_device "drm_device"))
    there should never be a need to tear down any modeset related
    resources in this callback. Doing so would be a driver design bug.

`lastclose`
:   Called when the last [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") has been closed and there's
    currently no userspace client for the [`struct drm_device`](drm-internals.md#c.drm_device "drm_device").

    Modern drivers should only use this to force-restore the fbdev
    framebuffer using [`drm_fb_helper_restore_fbdev_mode_unlocked()`](drm-kms-helpers.md#c.drm_fb_helper_restore_fbdev_mode_unlocked "drm_fb_helper_restore_fbdev_mode_unlocked").
    Anything else would indicate there's something seriously wrong.
    Modern drivers can also use this to execute delayed power switching
    state changes, e.g. in conjunction with the [VGA Switcheroo](vga-switcheroo.md#vga-switcheroo)
    infrastructure.

    This is called after **postclose** hook has been called.

    NOTE:

    All legacy drivers use this callback to de-initialize the hardware.
    This is purely because of the shadow-attach model, where the DRM
    kernel driver does not really own the hardware. Instead ownershipe is
    handled with the help of userspace through an inheritedly racy dance
    to set/unset the VT into raw mode.

    Legacy drivers initialize the hardware in the **firstopen** callback,
    which isn't even called for modern drivers.

`unload`
:   Reverse the effects of the driver load callback. Ideally,
    the clean up performed by the driver should happen in the
    reverse order of the initialization. Similarly to the load
    hook, this handler is deprecated and its usage should be
    dropped in favor of an open-coded teardown function at the
    driver layer. See [`drm_dev_unregister()`](drm-internals.md#c.drm_dev_unregister "drm_dev_unregister") and [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put")
    for the proper way to remove a [`struct drm_device`](drm-internals.md#c.drm_device "drm_device").

    The unload() hook is called right after unregistering
    the device.

`release`
:   Optional callback for destroying device data after the final
    reference is released, i.e. the device is being destroyed.

    This is deprecated, clean up all memory allocations associated with a
    [`drm_device`](drm-internals.md#c.drm_device "drm_device") using [`drmm_add_action()`](drm-internals.md#c.drmm_add_action "drmm_add_action"), [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc") and related
    managed resources functions.

`master_set`
:   Called whenever the minor master is set. Only used by vmwgfx.

`master_drop`
:   Called whenever the minor master is dropped. Only used by vmwgfx.

`debugfs_init`
:   Allows drivers to create driver-specific debugfs files.

`gem_create_object`
:   constructor for gem objects

    Hook for allocating the GEM object struct, for use by the CMA
    and SHMEM GEM helpers. Returns a GEM object on success, or an
    [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR")-encoded error code otherwise.

`prime_handle_to_fd`
:   PRIME export function. Only used by vmwgfx.

`prime_fd_to_handle`
:   PRIME import function. Only used by vmwgfx.

`gem_prime_import`
:   Import hook for GEM drivers.

    This defaults to [`drm_gem_prime_import()`](drm-mm.md#c.drm_gem_prime_import "drm_gem_prime_import") if not set.

`gem_prime_import_sg_table`
:   Optional hook used by the PRIME helper functions
    [`drm_gem_prime_import()`](drm-mm.md#c.drm_gem_prime_import "drm_gem_prime_import") respectively [`drm_gem_prime_import_dev()`](drm-mm.md#c.drm_gem_prime_import_dev "drm_gem_prime_import_dev").

`dumb_create`
:   This creates a new dumb buffer in the driver's backing storage manager (GEM,
    TTM or something else entirely) and returns the resulting buffer handle. This
    handle can then be wrapped up into a framebuffer modeset object.

    Note that userspace is not allowed to use such objects for render
    acceleration - drivers must create their own private ioctls for such a use
    case.

    Width, height and depth are specified in the [`drm_mode_create_dumb`](drm-uapi.md#c.drm_mode_create_dumb "drm_mode_create_dumb")
    argument. The callback needs to fill the handle, pitch and size for
    the created buffer.

    Called by the user via ioctl.

    Returns:

    Zero on success, negative errno on failure.

`dumb_map_offset`
:   Allocate an offset in the drm device node's address space to be able to
    memory map a dumb buffer.

    The default implementation is [`drm_gem_create_mmap_offset()`](drm-mm.md#c.drm_gem_create_mmap_offset "drm_gem_create_mmap_offset"). GEM based
    drivers must not overwrite this.

    Called by the user via ioctl.

    Returns:

    Zero on success, negative errno on failure.

`show_fdinfo`
:   Print device specific fdinfo. See [DRM client usage stats](drm-usage-stats.md).

`major`
:   driver major number

`minor`
:   driver minor number

`patchlevel`
:   driver patch level

`name`
:   driver name

`desc`
:   driver description

`date`
:   driver date

`driver_features`
:   Driver features, see [`enum drm_driver_feature`](drm-internals.md#c.drm_driver_feature "drm_driver_feature"). Drivers can disable
    some features on a per-instance basis using
    [`drm_device.driver_features`](drm-internals.md#c.drm_device "drm_device").

`ioctls`
:   Array of driver-private IOCTL description entries. See the chapter on
    [IOCTL support in the userland interfaces
    chapter](drm-uapi.md#drm-driver-ioctl) for the full details.

`num_ioctls`
:   Number of entries in **ioctls**.

`fops`
:   File operations for the DRM device node. See the discussion in
    [file operations](drm-internals.md#drm-driver-fops) for in-depth coverage and
    some examples.

**Description**

This structure represent the common code for a family of cards. There will be
one [`struct drm_device`](drm-internals.md#c.drm_device "drm_device") for each card present in this family. It contains lots
of vfunc entries, and a pile of those probably should be moved to more
appropriate places like [`drm_mode_config_funcs`](drm-kms.md#c.drm_mode_config_funcs "drm_mode_config_funcs") or into a new operations
structure for GEM drivers.

devm_drm_dev_alloc

`devm_drm_dev_alloc (parent, driver, type, member)`

> Resource managed allocation of a [`drm_device`](drm-internals.md#c.drm_device "drm_device") instance

**Parameters**

`parent`
:   Parent device object

`driver`
:   DRM driver

`type`
:   the type of the struct which contains struct [`drm_device`](drm-internals.md#c.drm_device "drm_device")

`member`
:   the name of the [`drm_device`](drm-internals.md#c.drm_device "drm_device") within **type**.

**Description**

This allocates and initialize a new DRM device. No device registration is done.
Call [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register") to advertice the device to user space and register it
with other core subsystems. This should be done last in the device
initialization sequence to make sure userspace can't access an inconsistent
state.

The initial ref-count of the object is 1. Use [`drm_dev_get()`](drm-internals.md#c.drm_dev_get "drm_dev_get") and
[`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") to take and drop further ref-counts.

It is recommended that drivers embed [`struct drm_device`](drm-internals.md#c.drm_device "drm_device") into their own device
structure.

Note that this manages the lifetime of the resulting [`drm_device`](drm-internals.md#c.drm_device "drm_device")
automatically using devres. The DRM device initialized with this function is
automatically put on driver detach using [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put").

**Return**

Pointer to new DRM device, or ERR_PTR on failure.

bool drm_dev_is_unplugged(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   is a DRM device unplugged

**Parameters**

`struct drm_device *dev`
:   DRM device

**Description**

This function can be called to check whether a hotpluggable is unplugged.
Unplugging itself is singalled through [`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug"). If a device is
unplugged, these two functions guarantee that any store before calling
[`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug") is visible to callers of this function after it completes

WARNING: This function fundamentally races against [`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug"). It is
recommended that drivers instead use the underlying [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter") and
[`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit") function pairs.

bool drm_core_check_all_features(const struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, u32 features)
:   check driver feature flags mask

**Parameters**

`const struct drm_device *dev`
:   DRM device to check

`u32 features`
:   feature flag(s) mask

**Description**

This checks **dev** for driver features, see [`drm_driver.driver_features`](drm-internals.md#c.drm_driver "drm_driver"),
[`drm_device.driver_features`](drm-internals.md#c.drm_device "drm_device"), and the various [`enum drm_driver_feature`](drm-internals.md#c.drm_driver_feature "drm_driver_feature") flags.

Returns true if all features in the **features** mask are supported, false
otherwise.

bool drm_core_check_feature(const struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, enum [drm_driver_feature](drm-internals.md#c.drm_driver_feature "drm_driver_feature") feature)
:   check driver feature flags

**Parameters**

`const struct drm_device *dev`
:   DRM device to check

`enum drm_driver_feature feature`
:   feature flag

**Description**

This checks **dev** for driver features, see [`drm_driver.driver_features`](drm-internals.md#c.drm_driver "drm_driver"),
[`drm_device.driver_features`](drm-internals.md#c.drm_device "drm_device"), and the various [`enum drm_driver_feature`](drm-internals.md#c.drm_driver_feature "drm_driver_feature") flags.

Returns true if the **feature** is supported, false otherwise.

bool drm_drv_uses_atomic_modeset(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   check if the driver implements atomic_commit()

**Parameters**

`struct drm_device *dev`
:   DRM device

**Description**

This check is useful if drivers do not have DRIVER_ATOMIC set but
have atomic modesetting internally implemented.

void drm_put_dev(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   Unregister and release a DRM device

**Parameters**

`struct drm_device *dev`
:   DRM device

**Description**

Called at module unload time or when a PCI device is unplugged.

Cleans up all DRM device, calling drm_lastclose().

**Note**

Use of this function is deprecated. It will eventually go away
completely. Please use [`drm_dev_unregister()`](drm-internals.md#c.drm_dev_unregister "drm_dev_unregister") and [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") explicitly
instead to make sure that the device isn't userspace accessible any more
while teardown is in progress, ensuring that userspace can't access an
inconsistent state.

bool drm_dev_enter(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, int \*idx)
:   Enter device critical section

**Parameters**

`struct drm_device *dev`
:   DRM device

`int *idx`
:   Pointer to index that will be passed to the matching [`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit")

**Description**

This function marks and protects the beginning of a section that should not
be entered after the device has been unplugged. The section end is marked
with [`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit"). Calls to this function can be nested.

**Return**

True if it is OK to enter the section, false otherwise.

void drm_dev_exit(int idx)
:   Exit device critical section

**Parameters**

`int idx`
:   index returned from [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter")

**Description**

This function marks the end of a section that should not be entered after
the device has been unplugged.

void drm_dev_unplug(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   unplug a DRM device

**Parameters**

`struct drm_device *dev`
:   DRM device

**Description**

This unplugs a hotpluggable DRM device, which makes it inaccessible to
userspace operations. Entry-points can use [`drm_dev_enter()`](drm-internals.md#c.drm_dev_enter "drm_dev_enter") and
[`drm_dev_exit()`](drm-internals.md#c.drm_dev_exit "drm_dev_exit") to protect device resources in a race free manner. This
essentially unregisters the device like [`drm_dev_unregister()`](drm-internals.md#c.drm_dev_unregister "drm_dev_unregister"), but can be
called while there are still open users of **dev**.

struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*drm_dev_alloc(const struct [drm_driver](drm-internals.md#c.drm_driver "drm_driver") \*driver, struct [device](../driver-api/infrastructure.md#c.device "device") \*parent)
:   Allocate new DRM device

**Parameters**

`const struct drm_driver *driver`
:   DRM driver to allocate device for

`struct device *parent`
:   Parent device object

**Description**

This is the deprecated version of [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc"), which does not support
subclassing through embedding the struct [`drm_device`](drm-internals.md#c.drm_device "drm_device") in a driver private
structure, and which does not support automatic cleanup through devres.

**Return**

Pointer to new DRM device, or ERR_PTR on failure.

void drm_dev_get(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   Take reference of a DRM device

**Parameters**

`struct drm_device *dev`
:   device to take reference of or NULL

**Description**

This increases the ref-count of **dev** by one. You *must* already own a
reference when calling this. Use [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") to drop this reference
again.

This function never fails. However, this function does not provide *any*
guarantee whether the device is alive or running. It only provides a
reference to the object and the memory associated with it.

void drm_dev_put(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   Drop reference of a DRM device

**Parameters**

`struct drm_device *dev`
:   device to drop reference of or NULL

**Description**

This decreases the ref-count of **dev** by one. The device is destroyed if the
ref-count drops to zero.

int drm_dev_register(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, unsigned long flags)
:   Register DRM device

**Parameters**

`struct drm_device *dev`
:   Device to register

`unsigned long flags`
:   Flags passed to the driver's .load() function

**Description**

Register the DRM device **dev** with the system, advertise device to user-space
and start normal device operation. **dev** must be initialized via drm_dev_init()
previously.

Never call this twice on any device!

**NOTE**

To ensure backward compatibility with existing drivers method this
function calls the [`drm_driver.load`](drm-internals.md#c.drm_driver "drm_driver") method after registering the device
nodes, creating race conditions. Usage of the [`drm_driver.load`](drm-internals.md#c.drm_driver "drm_driver") methods is
therefore deprecated, drivers must perform all initialization before calling
[`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register").

**Return**

0 on success, negative error code on failure.

void drm_dev_unregister(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   Unregister DRM device

**Parameters**

`struct drm_device *dev`
:   Device to unregister

**Description**

Unregister the DRM device from the system. This does the reverse of
[`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register") but does not deallocate the device. The caller must call
[`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") to drop their final reference, unless it is managed with devres
(as devices allocated with [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc") are), in which case there is
already an unwind action registered.

A special form of unregistering for hotpluggable devices is [`drm_dev_unplug()`](drm-internals.md#c.drm_dev_unplug "drm_dev_unplug"),
which can be called while there are still open users of **dev**.

This should be called first in the device teardown code to make sure
userspace can't access the device instance any more.

### Driver Load

#### Component Helper Usage

DRM drivers that drive hardware where a logical device consists of a pile of
independent hardware blocks are recommended to use the [component helper
library](../driver-api/component.md#component). For consistency and better options for code reuse the
following guidelines apply:

> - The entire device initialization procedure should be run from the
>   [`component_master_ops.master_bind`](../driver-api/component.md#c.component_master_ops "component_master_ops") callback, starting with
>   [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc"), then binding all components with
>   [`component_bind_all()`](../driver-api/component.md#c.component_bind_all "component_bind_all") and finishing with [`drm_dev_register()`](drm-internals.md#c.drm_dev_register "drm_dev_register").
> - The opaque pointer passed to all components through [`component_bind_all()`](../driver-api/component.md#c.component_bind_all "component_bind_all")
>   should point at [`struct drm_device`](drm-internals.md#c.drm_device "drm_device") of the device instance, not some driver
>   specific private structure.
> - The component helper fills the niche where further standardization of
>   interfaces is not practical. When there already is, or will be, a
>   standardized interface like [`drm_bridge`](drm-kms-helpers.md#c.drm_bridge "drm_bridge") or [`drm_panel`](drm-kms-helpers.md#c.drm_panel "drm_panel"), providing its own
>   functions to find such components at driver load time, like
>   [`drm_of_find_panel_or_bridge()`](drm-kms-helpers.md#c.drm_of_find_panel_or_bridge "drm_of_find_panel_or_bridge"), then the component helper should not be
>   used.

#### Memory Manager Initialization

Every DRM driver requires a memory manager which must be initialized at
load time. DRM currently contains two memory managers, the Translation
Table Manager (TTM) and the Graphics Execution Manager (GEM). This
document describes the use of the GEM memory manager only. See ? for
details.

#### Miscellaneous Device Configuration

Another task that may be necessary for PCI devices during configuration
is mapping the video BIOS. On many devices, the VBIOS describes device
configuration, LCD panel timings (if any), and contains flags indicating
device state. Mapping the BIOS can be done using the [`pci_map_rom()`](../driver-api/pci/pci.md#c.pci_map_rom "pci_map_rom")
call, a convenience function that takes care of mapping the actual ROM,
whether it has been shadowed into memory (typically at address 0xc0000)
or exists on the PCI device in the ROM BAR. Note that after the ROM has
been mapped and any necessary information has been extracted, it should
be unmapped; on many devices, the ROM address decoder is shared with
other BARs, so leaving it mapped could cause undesired behaviour like
hangs or memory corruption.

### Managed Resources

Inspired by struct [`device`](../driver-api/infrastructure.md#c.device "device") managed resources, but tied to the lifetime of
struct [`drm_device`](drm-internals.md#c.drm_device "drm_device"), which can outlive the underlying physical device, usually
when userspace has some open files and other handles to resources still open.

Release actions can be added with [`drmm_add_action()`](drm-internals.md#c.drmm_add_action "drmm_add_action"), memory allocations can
be done directly with [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc") and the related functions. Everything
will be released on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") in reverse order of how the
release actions have been added and memory has been allocated since driver
loading started with [`devm_drm_dev_alloc()`](drm-internals.md#c.devm_drm_dev_alloc "devm_drm_dev_alloc").

Note that release actions and managed memory can also be added and removed
during the lifetime of the driver, all the functions are fully concurrent
safe. But it is recommended to use managed resources only for resources that
change rarely, if ever, during the lifetime of the [`drm_device`](drm-internals.md#c.drm_device "drm_device") instance.

void \*drmm_kmalloc(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, size_t size, gfp_t gfp)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kmalloc()`](../core-api/mm-api.md#c.kmalloc "kmalloc")

**Parameters**

`struct drm_device *dev`
:   DRM device

`size_t size`
:   size of the memory allocation

`gfp_t gfp`
:   GFP allocation flags

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kmalloc()`](../core-api/mm-api.md#c.kmalloc "kmalloc"). The allocated memory is
automatically freed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put"). Memory can also be freed
before the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") by calling [`drmm_kfree()`](drm-internals.md#c.drmm_kfree "drmm_kfree").

char \*drmm_kstrdup(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, const char \*s, gfp_t gfp)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kstrdup()`](../core-api/kernel-api.md#c.kstrdup "kstrdup")

**Parameters**

`struct drm_device *dev`
:   DRM device

`const char *s`
:   0-terminated string to be duplicated

`gfp_t gfp`
:   GFP allocation flags

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kstrdup()`](../core-api/kernel-api.md#c.kstrdup "kstrdup"). The allocated memory is
automatically freed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") and works exactly like a
memory allocation obtained by [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc").

void drmm_kfree(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, void \*data)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kfree()`](../core-api/mm-api.md#c.kfree "kfree")

**Parameters**

`struct drm_device *dev`
:   DRM device

`void *data`
:   memory allocation to be freed

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kfree()`](../core-api/mm-api.md#c.kfree "kfree") which can be used to
release memory allocated through [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc") or any of its related
functions before the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") of **dev**.

drmm_add_action

`drmm_add_action (dev, action, data)`

> add a managed release action to a [`drm_device`](drm-internals.md#c.drm_device "drm_device")

**Parameters**

`dev`
:   DRM device

`action`
:   function which should be called when **dev** is released

`data`
:   opaque pointer, passed to **action**

**Description**

This function adds the **release** action with optional parameter **data** to the
list of cleanup actions for **dev**. The cleanup actions will be run in reverse
order in the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") call for **dev**.

drmm_add_action_or_reset

`drmm_add_action_or_reset (dev, action, data)`

> add a managed release action to a [`drm_device`](drm-internals.md#c.drm_device "drm_device")

**Parameters**

`dev`
:   DRM device

`action`
:   function which should be called when **dev** is released

`data`
:   opaque pointer, passed to **action**

**Description**

Similar to [`drmm_add_action()`](drm-internals.md#c.drmm_add_action "drmm_add_action"), with the only difference that upon failure
**action** is directly called for any cleanup work necessary on failures.

void \*drmm_kzalloc(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, size_t size, gfp_t gfp)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kzalloc()`](../core-api/mm-api.md#c.kzalloc "kzalloc")

**Parameters**

`struct drm_device *dev`
:   DRM device

`size_t size`
:   size of the memory allocation

`gfp_t gfp`
:   GFP allocation flags

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kzalloc()`](../core-api/mm-api.md#c.kzalloc "kzalloc"). The allocated memory is
automatically freed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put"). Memory can also be freed
before the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") by calling [`drmm_kfree()`](drm-internals.md#c.drmm_kfree "drmm_kfree").

void \*drmm_kmalloc_array(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, size_t n, size_t size, gfp_t flags)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kmalloc_array()`](../core-api/mm-api.md#c.kmalloc_array "kmalloc_array")

**Parameters**

`struct drm_device *dev`
:   DRM device

`size_t n`
:   number of array elements to allocate

`size_t size`
:   size of array member

`gfp_t flags`
:   GFP allocation flags

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kmalloc_array()`](../core-api/mm-api.md#c.kmalloc_array "kmalloc_array"). The allocated
memory is automatically freed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") and works exactly
like a memory allocation obtained by [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc").

void \*drmm_kcalloc(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, size_t n, size_t size, gfp_t flags)
:   [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed [`kcalloc()`](../core-api/mm-api.md#c.kcalloc "kcalloc")

**Parameters**

`struct drm_device *dev`
:   DRM device

`size_t n`
:   number of array elements to allocate

`size_t size`
:   size of array member

`gfp_t flags`
:   GFP allocation flags

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device") managed version of [`kcalloc()`](../core-api/mm-api.md#c.kcalloc "kcalloc"). The allocated memory is
automatically freed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put") and works exactly like a
memory allocation obtained by [`drmm_kmalloc()`](drm-internals.md#c.drmm_kmalloc "drmm_kmalloc").

drmm_mutex_init

`drmm_mutex_init (dev, lock)`

> [`drm_device`](drm-internals.md#c.drm_device "drm_device")-managed [`mutex_init()`](../kernel-hacking/locking.md#c.mutex_init "mutex_init")

**Parameters**

`dev`
:   DRM device

`lock`
:   lock to be initialized

**Return**

0 on success, or a negative errno code otherwise.

**Description**

This is a [`drm_device`](drm-internals.md#c.drm_device "drm_device")-managed version of [`mutex_init()`](../kernel-hacking/locking.md#c.mutex_init "mutex_init"). The initialized
lock is automatically destroyed on the final [`drm_dev_put()`](drm-internals.md#c.drm_dev_put "drm_dev_put").

### Bus-specific Device Registration and PCI Support

A number of functions are provided to help with device registration. The
functions deal with PCI and platform devices respectively and are only
provided for historical reasons. These are all deprecated and shouldn't
be used in new drivers. Besides that there's a few helpers for pci
drivers.

## Open/Close, File Operations and IOCTLs

### File Operations

Drivers must define the file operations structure that forms the DRM
userspace API entry point, even though most of those operations are
implemented in the DRM core. The resulting `struct file_operations` must be
stored in the [`drm_driver.fops`](drm-internals.md#c.drm_driver "drm_driver") field. The mandatory functions are [`drm_open()`](drm-internals.md#c.drm_open "drm_open"),
[`drm_read()`](drm-internals.md#c.drm_read "drm_read"), [`drm_ioctl()`](drm-uapi.md#c.drm_ioctl "drm_ioctl") and [`drm_compat_ioctl()`](drm-uapi.md#c.drm_compat_ioctl "drm_compat_ioctl") if CONFIG_COMPAT is enabled
Note that drm_compat_ioctl will be NULL if CONFIG_COMPAT=n, so there's no
need to sprinkle #ifdef into the code. Drivers which implement private ioctls
that require 32/64 bit compatibility support must provide their own
`file_operations.compat_ioctl` handler that processes private ioctls and calls
[`drm_compat_ioctl()`](drm-uapi.md#c.drm_compat_ioctl "drm_compat_ioctl") for core ioctls.

In addition [`drm_read()`](drm-internals.md#c.drm_read "drm_read") and [`drm_poll()`](drm-internals.md#c.drm_poll "drm_poll") provide support for DRM events. DRM
events are a generic and extensible means to send asynchronous events to
userspace through the file descriptor. They are used to send vblank event and
page flip completions by the KMS API. But drivers can also use it for their
own needs, e.g. to signal completion of rendering.

For the driver-side event interface see [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init") and
[`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") as the main starting points.

The memory mapping implementation will vary depending on how the driver
manages memory. For GEM-based drivers this is [`drm_gem_mmap()`](drm-mm.md#c.drm_gem_mmap "drm_gem_mmap").

No other file operations are supported by the DRM userspace API. Overall the
following is an example `file_operations` structure:

```
static const example_drm_fops = {
        .owner = THIS_MODULE,
        .open = drm_open,
        .release = drm_release,
        .unlocked_ioctl = drm_ioctl,
        .compat_ioctl = drm_compat_ioctl, // NULL if CONFIG_COMPAT=n
        .poll = drm_poll,
        .read = drm_read,
        .llseek = no_llseek,
        .mmap = drm_gem_mmap,
};
```

For plain GEM based drivers there is the [`DEFINE_DRM_GEM_FOPS()`](drm-mm.md#c.DEFINE_DRM_GEM_FOPS "DEFINE_DRM_GEM_FOPS") macro, and for
DMA based drivers there is the [`DEFINE_DRM_GEM_DMA_FOPS()`](drm-mm.md#c.DEFINE_DRM_GEM_DMA_FOPS "DEFINE_DRM_GEM_DMA_FOPS") macro to make this
simpler.

The driver's `file_operations` must be stored in [`drm_driver.fops`](drm-internals.md#c.drm_driver "drm_driver").

For driver-private IOCTL handling see the more detailed discussion in
[IOCTL support in the userland interfaces chapter](drm-uapi.md#drm-driver-ioctl).

struct drm_minor
:   DRM device minor structure

**Definition**:

```
struct drm_minor {
};
```

**Members**

**Description**

This structure represents a DRM minor number for device nodes in /dev.
Entirely opaque to drivers and should never be inspected directly by drivers.
Drivers instead should only interact with [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") and of course
[`struct drm_device`](drm-internals.md#c.drm_device "drm_device"), which is also where driver-private data and resources can
be attached to.

struct drm_pending_event
:   Event queued up for userspace to read

**Definition**:

```
struct drm_pending_event {
    struct completion *completion;
    void (*completion_release)(struct completion *completion);
    struct drm_event *event;
    struct dma_fence *fence;
    struct drm_file *file_priv;
    struct list_head link;
    struct list_head pending_link;
};
```

**Members**

`completion`
:   Optional pointer to a kernel internal completion signalled when
    [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") is called, useful to internally synchronize with
    nonblocking operations.

`completion_release`
:   Optional callback currently only used by the atomic modeset helpers
    to clean up the reference count for the structure **completion** is
    stored in.

`event`
:   Pointer to the actual event that should be sent to userspace to be
    read using [`drm_read()`](drm-internals.md#c.drm_read "drm_read"). Can be optional, since nowadays events are
    also used to signal kernel internal threads with **completion** or DMA
    transactions using **fence**.

`fence`
:   Optional DMA fence to unblock other hardware transactions which
    depend upon the nonblocking DRM operation this event represents.

`file_priv`
:   [`struct drm_file`](drm-internals.md#c.drm_file "drm_file") where **event** should be delivered to. Only set when
    **event** is set.

`link`
:   Double-linked list to keep track of this event. Can be used by the
    driver up to the point when it calls [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event"), after that
    this list entry is owned by the core for its own book-keeping.

`pending_link`
:   Entry on [`drm_file.pending_event_list`](drm-internals.md#c.drm_file "drm_file"), to keep track of all pending
    events for **file_priv**, to allow correct unwinding of them when
    userspace closes the file before the event is delivered.

**Description**

This represents a DRM event. Drivers can use this as a generic completion
mechanism, which supports kernel-internal `struct completion`, [`struct dma_fence`](../driver-api/dma-buf.md#c.dma_fence "dma_fence")
and also the DRM-specific [`struct drm_event`](drm-uapi.md#c.drm_event "drm_event") delivery mechanism.

struct drm_file
:   DRM file private data

**Definition**:

```
struct drm_file {
    bool authenticated;
    bool stereo_allowed;
    bool universal_planes;
    bool atomic;
    bool aspect_ratio_allowed;
    bool writeback_connectors;
    bool was_master;
    bool is_master;
    bool supports_virtualized_cursor_plane;
    struct drm_master *master;
    spinlock_t master_lookup_lock;
    struct pid __rcu *pid;
    u64 client_id;
    drm_magic_t magic;
    struct list_head lhead;
    struct drm_minor *minor;
    struct idr object_idr;
    spinlock_t table_lock;
    struct idr syncobj_idr;
    spinlock_t syncobj_table_lock;
    struct file *filp;
    void *driver_priv;
    struct list_head fbs;
    struct mutex fbs_lock;
    struct list_head blobs;
    wait_queue_head_t event_wait;
    struct list_head pending_event_list;
    struct list_head event_list;
    int event_space;
    struct mutex event_read_lock;
    struct drm_prime_file_private prime;
};
```

**Members**

`authenticated`
:   Whether the client is allowed to submit rendering, which for legacy
    nodes means it must be authenticated.

    See also the [section on primary nodes and authentication](drm-uapi.md#drm-primary-node).

`stereo_allowed`
:   True when the client has asked us to expose stereo 3D mode flags.

`universal_planes`
:   True if client understands CRTC primary planes and cursor planes
    in the plane list. Automatically set when **atomic** is set.

`atomic`
:   True if client understands atomic properties.

`aspect_ratio_allowed`
:   True, if client can handle picture aspect ratios, and has requested
    to pass this information along with the mode.

`writeback_connectors`
:   True if client understands writeback connectors

`was_master`
:   This client has or had, master capability. Protected by struct
    [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device").

    This is used to ensure that CAP_SYS_ADMIN is not enforced, if the
    client is or was master in the past.

`is_master`
:   This client is the creator of **master**. Protected by struct
    [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device").

    See also the [section on primary nodes and authentication](drm-uapi.md#drm-primary-node).

`supports_virtualized_cursor_plane`
:   This client is capable of handling the cursor plane with the
    restrictions imposed on it by the virtualized drivers.

    This implies that the cursor plane has to behave like a cursor
    i.e. track cursor movement. It also requires setting of the
    hotspot properties by the client on the cursor plane.

`master`
:   Master this node is currently associated with. Protected by struct
    [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device"), and serialized by **master_lookup_lock**.

    Only relevant if [`drm_is_primary_client()`](drm-internals.md#c.drm_is_primary_client "drm_is_primary_client") returns true. Note that
    this only matches [`drm_device.master`](drm-internals.md#c.drm_device "drm_device") if the master is the currently
    active one.

    To update **master**, both [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device") and
    **master_lookup_lock** need to be held, therefore holding either of
    them is safe and enough for the read side.

    When dereferencing this pointer, either hold struct
    [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device") for the duration of the pointer's use, or
    use [`drm_file_get_master()`](drm-uapi.md#c.drm_file_get_master "drm_file_get_master") if struct [`drm_device.master_mutex`](drm-internals.md#c.drm_device "drm_device") is not
    currently held and there is no other need to hold it. This prevents
    **master** from being freed during use.

    See also **authentication** and **is_master** and the [section on
    primary nodes and authentication](drm-uapi.md#drm-primary-node).

`master_lookup_lock`
:   Serializes **master**.

`pid`
:   Process that is using this file.

    Must only be dereferenced under a rcu_read_lock or equivalent.

    Updates are guarded with dev->filelist_mutex and reference must be
    dropped after a RCU grace period to accommodate lockless readers.

`client_id`
:   A unique id for fdinfo

`magic`
:   Authentication magic, see **authenticated**.

`lhead`
:   List of all open files of a DRM device, linked into
    [`drm_device.filelist`](drm-internals.md#c.drm_device "drm_device"). Protected by [`drm_device.filelist_mutex`](drm-internals.md#c.drm_device "drm_device").

`minor`
:   [`struct drm_minor`](drm-internals.md#c.drm_minor "drm_minor") for this file.

`object_idr`
:   Mapping of mm object handles to object pointers. Used by the GEM
    subsystem. Protected by **table_lock**.

`table_lock`
:   Protects **object_idr**.

`syncobj_idr`
:   Mapping of sync object handles to object pointers.

`syncobj_table_lock`
:   Protects **syncobj_idr**.

`filp`
:   Pointer to the core file structure.

`driver_priv`
:   Optional pointer for driver private data. Can be allocated in
    [`drm_driver.open`](drm-internals.md#c.drm_driver "drm_driver") and should be freed in [`drm_driver.postclose`](drm-internals.md#c.drm_driver "drm_driver").

`fbs`
:   List of [`struct drm_framebuffer`](drm-kms.md#c.drm_framebuffer "drm_framebuffer") associated with this file, using the
    [`drm_framebuffer.filp_head`](drm-kms.md#c.drm_framebuffer "drm_framebuffer") entry.

    Protected by **fbs_lock**. Note that the **fbs** list holds a reference on
    the framebuffer object to prevent it from untimely disappearing.

`fbs_lock`
:   Protects **fbs**.

`blobs`
:   User-created blob properties; this retains a reference on the
    property.

    Protected by **drm_mode_config.blob_lock**;

`event_wait`
:   Waitqueue for new events added to **event_list**.

`pending_event_list`
:   List of pending [`struct drm_pending_event`](drm-internals.md#c.drm_pending_event "drm_pending_event"), used to clean up pending
    events in case this file gets closed before the event is signalled.
    Uses the [`drm_pending_event.pending_link`](drm-internals.md#c.drm_pending_event "drm_pending_event") entry.

    Protect by [`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device").

`event_list`
:   List of [`struct drm_pending_event`](drm-internals.md#c.drm_pending_event "drm_pending_event"), ready for delivery to userspace
    through [`drm_read()`](drm-internals.md#c.drm_read "drm_read"). Uses the [`drm_pending_event.link`](drm-internals.md#c.drm_pending_event "drm_pending_event") entry.

    Protect by [`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device").

`event_space`
:   Available event space to prevent userspace from
    exhausting kernel memory. Currently limited to the fairly arbitrary
    value of 4KB.

`event_read_lock`
:   Serializes [`drm_read()`](drm-internals.md#c.drm_read "drm_read").

`prime`
:   Per-file buffer caches used by the PRIME buffer sharing code.

**Description**

This structure tracks DRM state per open file descriptor.

bool drm_is_primary_client(const struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file_priv)
:   is this an open file of the primary node

**Parameters**

`const struct drm_file *file_priv`
:   DRM file

**Description**

Returns true if this is an open file of the primary node, i.e.
[`drm_file.minor`](drm-internals.md#c.drm_file "drm_file") of **file_priv** is a primary minor.

See also the [section on primary nodes and authentication](drm-uapi.md#drm-primary-node).

bool drm_is_render_client(const struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file_priv)
:   is this an open file of the render node

**Parameters**

`const struct drm_file *file_priv`
:   DRM file

**Description**

Returns true if this is an open file of the render node, i.e.
[`drm_file.minor`](drm-internals.md#c.drm_file "drm_file") of **file_priv** is a render minor.

See also the [section on render nodes](drm-uapi.md#drm-render-node).

bool drm_is_accel_client(const struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file_priv)
:   is this an open file of the compute acceleration node

**Parameters**

`const struct drm_file *file_priv`
:   DRM file

**Description**

Returns true if this is an open file of the compute acceleration node, i.e.
[`drm_file.minor`](drm-internals.md#c.drm_file "drm_file") of **file_priv** is a accel minor.

See also [Introduction to compute accelerators subsystem](../accel/introduction.md).

struct drm_memory_stats
:   GEM object stats associated

**Definition**:

```
struct drm_memory_stats {
    u64 shared;
    u64 private;
    u64 resident;
    u64 purgeable;
    u64 active;
};
```

**Members**

`shared`
:   Total size of GEM objects shared between processes

`private`
:   Total size of GEM objects

`resident`
:   Total size of GEM objects backing pages

`purgeable`
:   Total size of GEM objects that can be purged (resident and not active)

`active`
:   Total size of GEM objects active on one or more engines

**Description**

Used by [`drm_print_memory_stats()`](drm-internals.md#c.drm_print_memory_stats "drm_print_memory_stats")

int drm_open(struct [inode](drm-internals.md#c.drm_open "inode") \*inode, struct file \*filp)
:   open method for DRM file

**Parameters**

`struct inode *inode`
:   device inode

`struct file *filp`
:   file pointer.

**Description**

This function must be used by drivers as their `file_operations.open` method.
It looks up the correct DRM device and instantiates all the per-file
resources for it. It also calls the [`drm_driver.open`](drm-internals.md#c.drm_driver "drm_driver") driver callback.

0 on success or negative errno value on failure.

**Return**

int drm_release(struct [inode](drm-internals.md#c.drm_release "inode") \*inode, struct file \*filp)
:   release method for DRM file

**Parameters**

`struct inode *inode`
:   device inode

`struct file *filp`
:   file pointer.

**Description**

This function must be used by drivers as their `file_operations.release`
method. It frees any resources associated with the open file, and calls the
[`drm_driver.postclose`](drm-internals.md#c.drm_driver "drm_driver") driver callback. If this is the last open file for the
DRM device also proceeds to call the [`drm_driver.lastclose`](drm-internals.md#c.drm_driver "drm_driver") driver callback.

Always succeeds and returns 0.

**Return**

int drm_release_noglobal(struct [inode](drm-internals.md#c.drm_release_noglobal "inode") \*inode, struct file \*filp)
:   release method for DRM file

**Parameters**

`struct inode *inode`
:   device inode

`struct file *filp`
:   file pointer.

**Description**

This function may be used by drivers as their `file_operations.release`
method. It frees any resources associated with the open file prior to taking
the drm_global_mutex, which then calls the [`drm_driver.postclose`](drm-internals.md#c.drm_driver "drm_driver") driver
callback. If this is the last open file for the DRM device also proceeds to
call the [`drm_driver.lastclose`](drm-internals.md#c.drm_driver "drm_driver") driver callback.

Always succeeds and returns 0.

**Return**

ssize_t drm_read(struct file \*filp, char __user \*buffer, size_t count, loff_t \*offset)
:   read method for DRM file

**Parameters**

`struct file *filp`
:   file pointer

`char __user *buffer`
:   userspace destination pointer for the read

`size_t count`
:   count in bytes to read

`loff_t *offset`
:   offset to read

**Description**

This function must be used by drivers as their `file_operations.read`
method if they use DRM events for asynchronous signalling to userspace.
Since events are used by the KMS API for vblank and page flip completion this
means all modern display drivers must use it.

**offset** is ignored, DRM events are read like a pipe. Polling support is
provided by [`drm_poll()`](drm-internals.md#c.drm_poll "drm_poll").

This function will only ever read a full event. Therefore userspace must
supply a big enough buffer to fit any event to ensure forward progress. Since
the maximum event space is currently 4K it's recommended to just use that for
safety.

Number of bytes read (always aligned to full events, and can be 0) or a
negative error code on failure.

**Return**

__poll_t drm_poll(struct file \*filp, struct poll_table_struct \*wait)
:   poll method for DRM file

**Parameters**

`struct file *filp`
:   file pointer

`struct poll_table_struct *wait`
:   poll waiter table

**Description**

This function must be used by drivers as their `file_operations.read` method
if they use DRM events for asynchronous signalling to userspace. Since
events are used by the KMS API for vblank and page flip completion this means
all modern display drivers must use it.

See also [`drm_read()`](drm-internals.md#c.drm_read "drm_read").

Mask of POLL flags indicating the current status of the file.

**Return**

int drm_event_reserve_init_locked(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file_priv, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*p, struct [drm_event](drm-uapi.md#c.drm_event "drm_event") \*e)
:   init a DRM event and reserve space for it

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_file *file_priv`
:   DRM file private data

`struct drm_pending_event *p`
:   tracking structure for the pending event

`struct drm_event *e`
:   actual event data to deliver to userspace

**Description**

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
[`drm_event_cancel_free()`](drm-internals.md#c.drm_event_cancel_free "drm_event_cancel_free"). Successfully initialized events should be sent out
using [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") or [`drm_send_event_locked()`](drm-internals.md#c.drm_send_event_locked "drm_send_event_locked") to signal completion of the
asynchronous event to userspace.

If callers embedded **p** into a larger structure it must be allocated with
kmalloc and **p** must be the first member element.

This is the locked version of [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init") for callers which
already hold [`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device").

0 on success or a negative error code on failure.

**Return**

int drm_event_reserve_init(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file_priv, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*p, struct [drm_event](drm-uapi.md#c.drm_event "drm_event") \*e)
:   init a DRM event and reserve space for it

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_file *file_priv`
:   DRM file private data

`struct drm_pending_event *p`
:   tracking structure for the pending event

`struct drm_event *e`
:   actual event data to deliver to userspace

**Description**

This function prepares the passed in event for eventual delivery. If the event
doesn't get delivered (because the IOCTL fails later on, before queuing up
anything) then the even must be cancelled and freed using
[`drm_event_cancel_free()`](drm-internals.md#c.drm_event_cancel_free "drm_event_cancel_free"). Successfully initialized events should be sent out
using [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") or [`drm_send_event_locked()`](drm-internals.md#c.drm_send_event_locked "drm_send_event_locked") to signal completion of the
asynchronous event to userspace.

If callers embedded **p** into a larger structure it must be allocated with
kmalloc and **p** must be the first member element.

Callers which already hold [`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device") should use
[`drm_event_reserve_init_locked()`](drm-internals.md#c.drm_event_reserve_init_locked "drm_event_reserve_init_locked") instead.

0 on success or a negative error code on failure.

**Return**

void drm_event_cancel_free(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*p)
:   free a DRM event and release its space

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_pending_event *p`
:   tracking structure for the pending event

**Description**

This function frees the event **p** initialized with [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init")
and releases any allocated space. It is used to cancel an event when the
nonblocking operation could not be submitted and needed to be aborted.

void drm_send_event_timestamp_locked(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*e, ktime_t timestamp)
:   send DRM event to file descriptor

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_pending_event *e`
:   DRM event to deliver

`ktime_t timestamp`
:   timestamp to set for the fence event in kernel's CLOCK_MONOTONIC
    time domain

**Description**

This function sends the event **e**, initialized with [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init"),
to its associated userspace DRM file. Callers must already hold
[`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device").

Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.

void drm_send_event_locked(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*e)
:   send DRM event to file descriptor

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_pending_event *e`
:   DRM event to deliver

**Description**

This function sends the event **e**, initialized with [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init"),
to its associated userspace DRM file. Callers must already hold
[`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device"), see [`drm_send_event()`](drm-internals.md#c.drm_send_event "drm_send_event") for the unlocked version.

Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.

void drm_send_event(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_pending_event](drm-internals.md#c.drm_pending_event "drm_pending_event") \*e)
:   send DRM event to file descriptor

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_pending_event *e`
:   DRM event to deliver

**Description**

This function sends the event **e**, initialized with [`drm_event_reserve_init()`](drm-internals.md#c.drm_event_reserve_init "drm_event_reserve_init"),
to its associated userspace DRM file. This function acquires
[`drm_device.event_lock`](drm-internals.md#c.drm_device "drm_device"), see [`drm_send_event_locked()`](drm-internals.md#c.drm_send_event_locked "drm_send_event_locked") for callers which already
hold this lock.

Note that the core will take care of unlinking and disarming events when the
corresponding DRM file is closed. Drivers need not worry about whether the
DRM file for this event still exists and can call this function upon
completion of the asynchronous work unconditionally.

void drm_print_memory_stats(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, const struct [drm_memory_stats](drm-internals.md#c.drm_memory_stats "drm_memory_stats") \*stats, enum [drm_gem_object_status](drm-mm.md#c.drm_gem_object_status "drm_gem_object_status") supported_status, const char \*region)
:   A helper to print memory stats

**Parameters**

`struct drm_printer *p`
:   The printer to print output to

`const struct drm_memory_stats *stats`
:   The collected memory stats

`enum drm_gem_object_status supported_status`
:   Bitmask of optional stats which are available

`const char *region`
:   The memory region

void drm_show_memory_stats(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, struct [drm_file](drm-internals.md#c.drm_file "drm_file") \*file)
:   Helper to collect and show standard fdinfo memory stats

**Parameters**

`struct drm_printer *p`
:   the printer to print output to

`struct drm_file *file`
:   the DRM file

**Description**

Helper to iterate over GEM objects with a handle allocated in the specified
file.

void drm_show_fdinfo(struct seq_file \*m, struct file \*f)
:   helper for drm file fops

**Parameters**

`struct seq_file *m`
:   output stream

`struct file *f`
:   the device file instance

**Description**

Helper to implement fdinfo, for userspace to query usage stats, etc, of a
process using the GPU. See also [`drm_driver.show_fdinfo`](drm-internals.md#c.drm_driver "drm_driver").

For text output format description please see [DRM client usage stats](drm-usage-stats.md)

## Misc Utilities

### Printer

A simple wrapper for dev_printk(), seq_printf(), etc. Allows same
debug code to be used for both debugfs and printk logging.

For example:

```
void log_some_info(struct drm_printer *p)
{
        drm_printf(p, "foo=%d\n", foo);
        drm_printf(p, "bar=%d\n", bar);
}

#ifdef CONFIG_DEBUG_FS
void debugfs_show(struct seq_file *f)
{
        struct drm_printer p = drm_seq_file_printer(f);
        log_some_info(&p);
}
#endif

void some_other_function(...)
{
        struct drm_printer p = drm_info_printer(drm->dev);
        log_some_info(&p);
}
```

struct drm_printer
:   drm output "stream"

**Definition**:

```
struct drm_printer {
};
```

**Members**

**Description**

Do not use struct members directly. Use drm_printer_seq_file(),
drm_printer_info(), etc to initialize. And [`drm_printf()`](drm-internals.md#c.drm_printf "drm_printf") for output.

void drm_vprintf(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, const char \*fmt, va_list \*va)
:   print to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream

**Parameters**

`struct drm_printer *p`
:   the [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer")

`const char *fmt`
:   format string

`va_list *va`
:   the va_list

drm_printf_indent

`drm_printf_indent (printer, indent, fmt, ...)`

> Print to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream with indentation

**Parameters**

`printer`
:   DRM printer

`indent`
:   Tab indentation level (max 5)

`fmt`
:   Format string

`...`
:   variable arguments

struct drm_print_iterator
:   local struct used with drm_printer_coredump

**Definition**:

```
struct drm_print_iterator {
    void *data;
    ssize_t start;
    ssize_t remain;
};
```

**Members**

`data`
:   Pointer to the devcoredump output buffer

`start`
:   The offset within the buffer to start writing

`remain`
:   The number of bytes to write for this iteration

struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") drm_coredump_printer(struct [drm_print_iterator](drm-internals.md#c.drm_print_iterator "drm_print_iterator") \*iter)
:   construct a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") that can output to a buffer from the read function for devcoredump

**Parameters**

`struct drm_print_iterator *iter`
:   A pointer to a [`struct drm_print_iterator`](drm-internals.md#c.drm_print_iterator "drm_print_iterator") for the read instance

**Description**

This wrapper extends [`drm_printf()`](drm-internals.md#c.drm_printf "drm_printf") to work with a dev_coredumpm() callback
function. The passed in drm_print_iterator struct contains the buffer
pointer, size and offset as passed in from devcoredump.

For example:

```
void coredump_read(char *buffer, loff_t offset, size_t count,
        void *data, size_t datalen)
{
        struct drm_print_iterator iter;
        struct drm_printer p;

        iter.data = buffer;
        iter.start = offset;
        iter.remain = count;

        p = drm_coredump_printer(&iter);

        drm_printf(p, "foo=%d\n", foo);
}

void makecoredump(...)
{
        ...
        dev_coredumpm(dev, THIS_MODULE, data, 0, GFP_KERNEL,
                coredump_read, ...)
}
```

**Return**

The [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") object

struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") drm_seq_file_printer(struct seq_file \*f)
:   construct a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") that outputs to `seq_file`

**Parameters**

`struct seq_file *f`
:   the `struct seq_file` to output to

**Return**

The [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") object

struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") drm_info_printer(struct [device](../driver-api/infrastructure.md#c.device "device") \*dev)
:   construct a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") that outputs to dev_printk()

**Parameters**

`struct device *dev`
:   the [`struct device`](../driver-api/infrastructure.md#c.device "device") pointer

**Return**

The [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") object

struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") drm_debug_printer(const char \*prefix)
:   construct a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") that outputs to [`pr_debug()`](../core-api/printk-basics.md#c.pr_debug "pr_debug")

**Parameters**

`const char *prefix`
:   debug output prefix

**Return**

The [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") object

struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") drm_err_printer(const char \*prefix)
:   construct a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") that outputs to [`pr_err()`](../core-api/printk-basics.md#c.pr_err "pr_err")

**Parameters**

`const char *prefix`
:   debug output prefix

**Return**

The [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") object

enum drm_debug_category
:   The DRM debug categories

**Constants**

`DRM_UT_CORE`
:   Used in the generic drm code: drm_ioctl.c, drm_mm.c,
    drm_memory.c, ...

`DRM_UT_DRIVER`
:   Used in the vendor specific part of the driver: i915,
    radeon, ... macro.

`DRM_UT_KMS`
:   Used in the modesetting code.

`DRM_UT_PRIME`
:   Used in the prime code.

`DRM_UT_ATOMIC`
:   Used in the atomic code.

`DRM_UT_VBL`
:   Used for verbose debug message in the vblank code.

`DRM_UT_STATE`
:   Used for verbose atomic state debugging.

`DRM_UT_LEASE`
:   Used in the lease code.

`DRM_UT_DP`
:   Used in the DP code.

`DRM_UT_DRMRES`
:   Used in the drm managed resources code.

**Description**

Each of the DRM debug logging macros use a specific category, and the logging
is filtered by the drm.debug module parameter. This enum specifies the values
for the interface.

Each DRM_DEBUG_<CATEGORY> macro logs to DRM_UT_<CATEGORY> category, except
DRM_DEBUG() logs to DRM_UT_CORE.

Enabling verbose debug messages is done through the drm.debug parameter, each
category being enabled by a bit:

> - drm.debug=0x1 will enable CORE messages
> - drm.debug=0x2 will enable DRIVER messages
> - drm.debug=0x3 will enable CORE and DRIVER messages
> - ...
> - drm.debug=0x1ff will enable all messages

An interesting feature is that it's possible to enable verbose logging at
run-time by echoing the debug value in its sysfs node:

```
# echo 0xf > /sys/module/drm/parameters/debug
```

DRM_DEV_ERROR

`DRM_DEV_ERROR (dev, fmt, ...)`

> Error output.

**Parameters**

`dev`
:   device pointer

`fmt`
:   printf() like format string.

`...`
:   variable arguments

**NOTE**

this is deprecated in favor of drm_err() or dev_err().

DRM_DEV_ERROR_RATELIMITED

`DRM_DEV_ERROR_RATELIMITED (dev, fmt, ...)`

> Rate limited error output.

**Parameters**

`dev`
:   device pointer

`fmt`
:   printf() like format string.

`...`
:   variable arguments

**NOTE**

this is deprecated in favor of drm_err_ratelimited() or
dev_err_ratelimited().

**Description**

Like DRM_ERROR() but won't flood the log.

DRM_DEV_DEBUG

`DRM_DEV_DEBUG (dev, fmt, ...)`

> Debug output for generic drm code

**Parameters**

`dev`
:   device pointer

`fmt`
:   printf() like format string.

`...`
:   variable arguments

**NOTE**

this is deprecated in favor of drm_dbg_core().

DRM_DEV_DEBUG_DRIVER

`DRM_DEV_DEBUG_DRIVER (dev, fmt, ...)`

> Debug output for vendor specific part of the driver

**Parameters**

`dev`
:   device pointer

`fmt`
:   printf() like format string.

`...`
:   variable arguments

**NOTE**

this is deprecated in favor of drm_dbg() or dev_dbg().

DRM_DEV_DEBUG_KMS

`DRM_DEV_DEBUG_KMS (dev, fmt, ...)`

> Debug output for modesetting code

**Parameters**

`dev`
:   device pointer

`fmt`
:   printf() like format string.

`...`
:   variable arguments

**NOTE**

this is deprecated in favor of drm_dbg_kms().

void drm_puts(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, const char \*str)
:   print a const string to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream

**Parameters**

`struct drm_printer *p`
:   the `drm` printer

`const char *str`
:   const string

**Description**

Allow [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") types that have a constant string
option to use it.

void drm_printf(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, const char \*f, ...)
:   print to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream

**Parameters**

`struct drm_printer *p`
:   the [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer")

`const char *f`
:   format string

`...`
:   variable arguments

void drm_print_bits(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, unsigned long value, const char \*const bits[], unsigned int nbits)
:   print bits to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream

**Parameters**

`struct drm_printer *p`
:   the [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer")

`unsigned long value`
:   field value.

`const char * const bits[]`
:   Array with bit names.

`unsigned int nbits`
:   Size of bit names array.

**Description**

Print bits (in flag fields for example) in human readable form.

void drm_print_regset32(struct [drm_printer](drm-internals.md#c.drm_printer "drm_printer") \*p, struct debugfs_regset32 \*regset)
:   print the contents of registers to a [`drm_printer`](drm-internals.md#c.drm_printer "drm_printer") stream.

**Parameters**

`struct drm_printer *p`
:   the `drm` printer

`struct debugfs_regset32 *regset`
:   the list of registers to print.

**Description**

Often in driver debug, it's useful to be able to either capture the
contents of registers in the steady state using debugfs or at
specific points during operation. This lets the driver have a
single list of registers for both.

### Utilities

Macros and inline functions that does not naturally belong in other places

for_each_if

`for_each_if (condition)`

> helper for handling conditionals in various for_each macros

**Parameters**

`condition`
:   The condition to check

**Description**

Typical use:

```
#define for_each_foo_bar(x, y) \'
        list_for_each_entry(x, y->list, head) \'
                for_each_if(x->something == SOMETHING)
```

The [`for_each_if()`](drm-internals.md#c.for_each_if "for_each_if") macro makes the use of for_each_foo_bar() less error
prone.

bool drm_can_sleep(void)
:   returns true if currently okay to sleep

**Parameters**

`void`
:   no arguments

**Description**

This function shall not be used in new code.
The check for running in atomic context may not work - see linux/preempt.h.

FIXME: All users of drm_can_sleep should be removed (see [TODO list](todo.md))

**Return**

False if kgdb is active, we are in atomic context or irqs are disabled.

## Unit testing

### KUnit

KUnit (Kernel unit testing framework) provides a common framework for unit tests
within the Linux kernel.

This section covers the specifics for the DRM subsystem. For general information
about KUnit, please refer to [Getting Started](../dev-tools/kunit/start.md).

#### How to run the tests?

In order to facilitate running the test suite, a configuration file is present
in `drivers/gpu/drm/tests/.kunitconfig`. It can be used by `kunit.py` as
follows:

```bash
$ ./tools/testing/kunit/kunit.py run --kunitconfig=drivers/gpu/drm/tests \
        --kconfig_add CONFIG_VIRTIO_UML=y \
        --kconfig_add CONFIG_UML_PCI_OVER_VIRTIO=y
```

> **Note:**
>
> The configuration included in `.kunitconfig` should be as generic as
> possible.
> `CONFIG_VIRTIO_UML` and `CONFIG_UML_PCI_OVER_VIRTIO` are not
> included in it because they are only required for User Mode Linux.

## Legacy Support Code

The section very briefly covers some of the old legacy support code
which is only used by old DRM drivers which have done a so-called
shadow-attach to the underlying device instead of registering as a real
driver. This also includes some of the old generic buffer management and
command submission code. Do not use any of this in new and modern
drivers.

### Legacy Suspend/Resume

The DRM core provides some suspend/resume code, but drivers wanting full
suspend/resume support should provide save() and restore() functions.
These are called at suspend, hibernate, or resume time, and should
perform any state save or restore required by your device across suspend
or hibernate states.

int (\*suspend) ([`struct drm_device`](drm-internals.md#c.drm_device "drm_device") \*, pm_message_t state); int
(\*resume) ([`struct drm_device`](drm-internals.md#c.drm_device "drm_device") \*);
Those are legacy suspend and resume methods which *only* work with the
legacy shadow-attach driver registration functions. New driver should
use the power management interface provided by their bus type (usually
through the [`struct device_driver`](../driver-api/infrastructure.md#c.device_driver "device_driver")
dev_pm_ops) and set these methods to NULL.

### Legacy DMA Services

This should cover how DMA mapping etc. is supported by the core. These
functions are deprecated and should not be used.
