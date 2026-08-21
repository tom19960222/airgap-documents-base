---
collection: kernel
version: "6.8"
title: "5. Media Controller devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/mc-core.html
fetched_at: 2026-08-21T03:32:24+00:00
---
# 5. Media Controller devices

## 5.1. Media Controller

The media controller userspace API is documented in
[the Media Controller uAPI book](../../userspace-api/media/mediactl/media-controller.md#media-controller). This document focus
on the kernel-side implementation of the media framework.

### 5.1.1. Abstract media device model

Discovering a device internal topology, and configuring it at runtime, is one
of the goals of the media framework. To achieve this, hardware devices are
modelled as an oriented graph of building blocks called entities connected
through pads.

An entity is a basic media hardware building block. It can correspond to
a large variety of logical blocks such as physical hardware devices
(CMOS sensor for instance), logical hardware devices (a building block
in a System-on-Chip image processing pipeline), DMA channels or physical
connectors.

A pad is a connection endpoint through which an entity can interact with
other entities. Data (not restricted to video) produced by an entity
flows from the entity's output to one or more entity inputs. Pads should
not be confused with physical pins at chip boundaries.

A link is a point-to-point oriented connection between two pads, either
on the same entity or on different entities. Data flows from a source
pad to a sink pad.

### 5.1.2. Media device

A media device is represented by a [`struct media_device`](mc-core.md#c.media_device "media_device")
instance, defined in `include/media/media-device.h`.
Allocation of the structure is handled by the media device driver, usually by
embedding the [`media_device`](mc-core.md#c.media_device "media_device") instance in a larger driver-specific
structure.

Drivers initialise media device instances by calling
[`media_device_init()`](mc-core.md#c.media_device_init "media_device_init"). After initialising a media device instance, it is
registered by calling [`__media_device_register()`](mc-core.md#c.__media_device_register "__media_device_register") via the macro
`media_device_register()` and unregistered by calling
[`media_device_unregister()`](mc-core.md#c.media_device_unregister "media_device_unregister"). An initialised media device must be
eventually cleaned up by calling [`media_device_cleanup()`](mc-core.md#c.media_device_cleanup "media_device_cleanup").

Note that it is not allowed to unregister a media device instance that was not
previously registered, or clean up a media device instance that was not
previously initialised.

### 5.1.3. Entities

Entities are represented by a [`struct media_entity`](mc-core.md#c.media_entity "media_entity")
instance, defined in `include/media/media-entity.h`. The structure is usually
embedded into a higher-level structure, such as
[`v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") or [`video_device`](v4l2-dev.md#c.video_device "video_device")
instances, although drivers can allocate entities directly.

Drivers initialize entity pads by calling
[`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init").

Drivers register entities with a media device by calling
[`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity")
and unregistered by calling
[`media_device_unregister_entity()`](mc-core.md#c.media_device_unregister_entity "media_device_unregister_entity").

### 5.1.4. Interfaces

Interfaces are represented by a
[`struct media_interface`](mc-core.md#c.media_interface "media_interface") instance, defined in
`include/media/media-entity.h`. Currently, only one type of interface is
defined: a device node. Such interfaces are represented by a
[`struct media_intf_devnode`](mc-core.md#c.media_intf_devnode "media_intf_devnode").

Drivers initialize and create device node interfaces by calling
[`media_devnode_create()`](mc-core.md#c.media_devnode_create "media_devnode_create")
and remove them by calling:
[`media_devnode_remove()`](mc-core.md#c.media_devnode_remove "media_devnode_remove").

### 5.1.5. Pads

Pads are represented by a [`struct media_pad`](mc-core.md#c.media_pad "media_pad") instance,
defined in `include/media/media-entity.h`. Each entity stores its pads in
a pads array managed by the entity driver. Drivers usually embed the array in
a driver-specific structure.

Pads are identified by their entity and their 0-based index in the pads
array.

Both information are stored in the [`struct media_pad`](mc-core.md#c.media_pad "media_pad"),
making the [`struct media_pad`](mc-core.md#c.media_pad "media_pad") pointer the canonical way
to store and pass link references.

Pads have flags that describe the pad capabilities and state.

`MEDIA_PAD_FL_SINK` indicates that the pad supports sinking data.
`MEDIA_PAD_FL_SOURCE` indicates that the pad supports sourcing data.

> **Note:**
>
> One and only one of `MEDIA_PAD_FL_SINK` or `MEDIA_PAD_FL_SOURCE` must
> be set for each pad.

### 5.1.6. Links

Links are represented by a [`struct media_link`](mc-core.md#c.media_link "media_link") instance,
defined in `include/media/media-entity.h`. There are two types of links:

**1. pad to pad links**:

Associate two entities via their PADs. Each entity has a list that points
to all links originating at or targeting any of its pads.
A given link is thus stored twice, once in the source entity and once in
the target entity.

Drivers create pad to pad links by calling:
[`media_create_pad_link()`](mc-core.md#c.media_create_pad_link "media_create_pad_link") and remove with
[`media_entity_remove_links()`](mc-core.md#c.media_entity_remove_links "media_entity_remove_links").

**2. interface to entity links**:

Associate one interface to a Link.

Drivers create interface to entity links by calling:
[`media_create_intf_link()`](mc-core.md#c.media_create_intf_link "media_create_intf_link") and remove with
[`media_remove_intf_links()`](mc-core.md#c.media_remove_intf_links "media_remove_intf_links").

> **Note:**
>
> Links can only be created after having both ends already created.

Links have flags that describe the link capabilities and state. The
valid values are described at [`media_create_pad_link()`](mc-core.md#c.media_create_pad_link "media_create_pad_link") and
[`media_create_intf_link()`](mc-core.md#c.media_create_intf_link "media_create_intf_link").

### 5.1.7. Graph traversal

The media framework provides APIs to iterate over entities in a graph.

To iterate over all entities belonging to a media device, drivers can use
the media_device_for_each_entity macro, defined in
`include/media/media-device.h`.

```c
struct media_entity *entity;

media_device_for_each_entity(entity, mdev) {
// entity will point to each entity in turn
...
}
```

Drivers might also need to iterate over all entities in a graph that can be
reached only through enabled links starting at a given entity. The media
framework provides a depth-first graph traversal API for that purpose.

> **Note:**
>
> Graphs with cycles (whether directed or undirected) are **NOT**
> supported by the graph traversal API. To prevent infinite loops, the graph
> traversal code limits the maximum depth to `MEDIA_ENTITY_ENUM_MAX_DEPTH`,
> currently defined as 16.

Drivers initiate a graph traversal by calling
[`media_graph_walk_start()`](mc-core.md#c.media_graph_walk_start "media_graph_walk_start")

The graph structure, provided by the caller, is initialized to start graph
traversal at the given entity.

Drivers can then retrieve the next entity by calling
[`media_graph_walk_next()`](mc-core.md#c.media_graph_walk_next "media_graph_walk_next")

When the graph traversal is complete the function will return `NULL`.

Graph traversal can be interrupted at any moment. No cleanup function call
is required and the graph structure can be freed normally.

Helper functions can be used to find a link between two given pads, or a pad
connected to another pad through an enabled link
([`media_entity_find_link()`](mc-core.md#c.media_entity_find_link "media_entity_find_link"), [`media_pad_remote_pad_first()`](mc-core.md#c.media_pad_remote_pad_first "media_pad_remote_pad_first"),
[`media_entity_remote_source_pad_unique()`](mc-core.md#c.media_entity_remote_source_pad_unique "media_entity_remote_source_pad_unique") and
[`media_pad_remote_pad_unique()`](mc-core.md#c.media_pad_remote_pad_unique "media_pad_remote_pad_unique")).

### 5.1.8. Use count and power handling

Due to the wide differences between drivers regarding power management
needs, the media controller does not implement power management. However,
the [`struct media_entity`](mc-core.md#c.media_entity "media_entity") includes a `use_count`
field that media drivers
can use to track the number of users of every entity for power management
needs.

The [`media_entity`](mc-core.md#c.media_entity "media_entity").`use_count` field is owned by
media drivers and must not be
touched by entity drivers. Access to the field must be protected by the
[`media_device`](mc-core.md#c.media_device "media_device").`graph_mutex` lock.

### 5.1.9. Links setup

Link properties can be modified at runtime by calling
[`media_entity_setup_link()`](mc-core.md#c.media_entity_setup_link "media_entity_setup_link").

### 5.1.10. Pipelines and media streams

A media stream is a stream of pixels or metadata originating from one or more
source devices (such as a sensors) and flowing through media entity pads
towards the final sinks. The stream can be modified on the route by the
devices (e.g. scaling or pixel format conversions), or it can be split into
multiple branches, or multiple branches can be merged.

A media pipeline is a set of media streams which are interdependent. This
interdependency can be caused by the hardware (e.g. configuration of a second
stream cannot be changed if the first stream has been enabled) or by the driver
due to the software design. Most commonly a media pipeline consists of a single
stream which does not branch.

When starting streaming, drivers must notify all entities in the pipeline to
prevent link states from being modified during streaming by calling
[`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start").

The function will mark all the pads which are part of the pipeline as streaming.

The [`struct media_pipeline`](mc-core.md#c.media_pipeline "media_pipeline") instance pointed to by the pipe argument will be
stored in every pad in the pipeline. Drivers should embed the [`struct
media_pipeline`](mc-core.md#c.media_pipeline "media_pipeline") in higher-level pipeline structures and can then access the
pipeline through the [`struct media_pad`](mc-core.md#c.media_pad "media_pad") pipe field.

Calls to [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") can be nested.
The pipeline pointer must be identical for all nested calls to the function.

[`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") may return an error. In that case,
it will clean up any of the changes it did by itself.

When stopping the stream, drivers must notify the entities with
[`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop").

If multiple calls to [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") have been
made the same number of [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop") calls
are required to stop streaming.
The [`media_entity`](mc-core.md#c.media_entity "media_entity").`pipe` field is reset to `NULL` on the last
nested stop call.

Link configuration will fail with `-EBUSY` by default if either end of the
link is a streaming entity. Links that can be modified while streaming must
be marked with the `MEDIA_LNK_FL_DYNAMIC` flag.

If other operations need to be disallowed on streaming entities (such as
changing entities configuration parameters) drivers can explicitly check the
media_entity stream_count field to find out if an entity is streaming. This
operation must be done with the media_device graph_mutex held.

### 5.1.11. Link validation

Link validation is performed by [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start")
for any entity which has sink pads in the pipeline. The
[`media_entity`](mc-core.md#c.media_entity "media_entity").`link_validate()` callback is used for that
purpose. In `link_validate()` callback, entity driver should check
that the properties of the source pad of the connected entity and its own
sink pad match. It is up to the type of the entity (and in the end, the
properties of the hardware) what matching actually means.

Subsystems should facilitate link validation by providing subsystem specific
helper functions to provide easy access for commonly needed information, and
in the end provide a way to use driver-specific callbacks.

### 5.1.12. Media Controller Device Allocator API

When the media device belongs to more than one driver, the shared media
device is allocated with the shared [`struct device`](../infrastructure.md#c.device "device") as the key for look ups.

The shared media device should stay in registered state until the last
driver unregisters it. In addition, the media device should be released when
all the references are released. Each driver gets a reference to the media
device during probe, when it allocates the media device. If media device is
already allocated, the allocate API bumps up the refcount and returns the
existing media device. The driver puts the reference back in its disconnect
routine when it calls [`media_device_delete()`](mc-core.md#c.media_device_delete "media_device_delete").

The media device is unregistered and cleaned up from the kref put handler to
ensure that the media device stays in registered state until the last driver
unregisters the media device.

**Driver Usage**

Drivers should use the appropriate media-core routines to manage the shared
media device life-time handling the two states:
1. allocate -> register -> delete
2. get reference to already registered device -> delete

call [`media_device_delete()`](mc-core.md#c.media_device_delete "media_device_delete") routine to make sure the shared media
device delete is handled correctly.

**driver probe:**
Call [`media_device_usb_allocate()`](mc-core.md#c.media_device_usb_allocate "media_device_usb_allocate") to allocate or get a reference
Call [`media_device_register()`](mc-core.md#c.media_device_register "media_device_register"), if media devnode isn't registered

**driver disconnect:**
Call [`media_device_delete()`](mc-core.md#c.media_device_delete "media_device_delete") to free the media_device. Freeing is
handled by the kref put handler.

### 5.1.13. API Definitions

struct media_entity_notify
:   Media Entity Notify

**Definition**:

```
struct media_entity_notify {
    struct list_head list;
    void *notify_data;
    void (*notify)(struct media_entity *entity, void *notify_data);
};
```

**Members**

`list`
:   List head

`notify_data`
:   Input data to invoke the callback

`notify`
:   Callback function pointer

**Description**

Drivers may register a callback to take action when new entities get
registered with the media device. This handler is intended for creating
links between existing entities and should not create entities and register
them.

struct media_device_ops
:   Media device operations

**Definition**:

```
struct media_device_ops {
    int (*link_notify)(struct media_link *link, u32 flags, unsigned int notification);
    struct media_request *(*req_alloc)(struct media_device *mdev);
    void (*req_free)(struct media_request *req);
    int (*req_validate)(struct media_request *req);
    void (*req_queue)(struct media_request *req);
};
```

**Members**

`link_notify`
:   Link state change notification callback. This callback is
    called with the graph_mutex held.

`req_alloc`
:   Allocate a request. Set this if you need to allocate a struct
    larger then [`struct media_request`](mc-core.md#c.media_request "media_request"). **req_alloc** and **req_free** must
    either both be set or both be NULL.

`req_free`
:   Free a request. Set this if **req_alloc** was set as well, leave
    to NULL otherwise.

`req_validate`
:   Validate a request, but do not queue yet. The req_queue_mutex
    lock is held when this op is called.

`req_queue`
:   Queue a validated request, cannot fail. If something goes
    wrong when queueing this request then it should be marked
    as such internally in the driver and any related buffers
    must eventually return to vb2 with state VB2_BUF_STATE_ERROR.
    The req_queue_mutex lock is held when this op is called.
    It is important that vb2 buffer objects are queued last after
    all other object types are queued: queueing a buffer kickstarts
    the request processing, so all other objects related to the
    request (and thus the buffer) must be available to the driver.
    And once a buffer is queued, then the driver can complete
    or delete objects from the request before req_queue exits.

struct media_device
:   Media device

**Definition**:

```
struct media_device {
    struct device *dev;
    struct media_devnode *devnode;
    char model[32];
    char driver_name[32];
    char serial[40];
    char bus_info[32];
    u32 hw_revision;
    u64 topology_version;
    u32 id;
    struct ida entity_internal_idx;
    int entity_internal_idx_max;
    struct list_head entities;
    struct list_head interfaces;
    struct list_head pads;
    struct list_head links;
    struct list_head entity_notify;
    struct mutex graph_mutex;
    struct media_graph pm_count_walk;
    void *source_priv;
    int (*enable_source)(struct media_entity *entity, struct media_pipeline *pipe);
    void (*disable_source)(struct media_entity *entity);
    const struct media_device_ops *ops;
    struct mutex req_queue_mutex;
    atomic_t request_id;
};
```

**Members**

`dev`
:   Parent device

`devnode`
:   Media device node

`model`
:   Device model name

`driver_name`
:   Optional device driver name. If not set, calls to
    `MEDIA_IOC_DEVICE_INFO` will return `dev->driver->name`.
    This is needed for USB drivers for example, as otherwise
    they'll all appear as if the driver name was "usb".

`serial`
:   Device serial number (optional)

`bus_info`
:   Unique and stable device location identifier

`hw_revision`
:   Hardware device revision

`topology_version`
:   Monotonic counter for storing the version of the graph
    topology. Should be incremented each time the topology changes.

`id`
:   Unique ID used on the last registered graph object

`entity_internal_idx`
:   Unique internal entity ID used by the graph traversal
    algorithms

`entity_internal_idx_max`
:   Allocated internal entity indices

`entities`
:   List of registered entities

`interfaces`
:   List of registered interfaces

`pads`
:   List of registered pads

`links`
:   List of registered links

`entity_notify`
:   List of registered entity_notify callbacks

`graph_mutex`
:   Protects access to [`struct media_device`](mc-core.md#c.media_device "media_device") data

`pm_count_walk`
:   Graph walk for power state walk. Access serialised using
    graph_mutex.

`source_priv`
:   Driver Private data for enable/disable source handlers

`enable_source`
:   Enable Source Handler function pointer

`disable_source`
:   Disable Source Handler function pointer

`ops`
:   Operation handler callbacks

`req_queue_mutex`
:   Serialise the MEDIA_REQUEST_IOC_QUEUE ioctl w.r.t.
    other operations that stop or start streaming.

`request_id`
:   Used to generate unique request IDs

**Description**

This structure represents an abstract high-level media device. It allows easy
access to entities and provides basic media device-level support. The
structure can be allocated directly or embedded in a larger structure.

The parent **dev** is a physical device. It must be set before registering the
media device.

**model** is a descriptive model name exported through sysfs. It doesn't have to
be unique.

**enable_source** is a handler to find source entity for the
sink entity and activate the link between them if source
entity is free. Drivers should call this handler before
accessing the source.

**disable_source** is a handler to find source entity for the
sink entity and deactivate the link between them. Drivers
should call this handler to release the source.

Use-case: find tuner entity connected to the decoder
entity and check if it is available, and activate the
link between them from **enable_source** and deactivate
from **disable_source**.

> **Note:**
>
> Bridge driver is expected to implement and set the
> handler when [`media_device`](mc-core.md#c.media_device "media_device") is registered or when
> bridge driver finds the media_device during probe.
> Bridge driver sets source_priv with information
> necessary to run **enable_source** and **disable_source** handlers.
> Callers should hold graph_mutex to access and call **enable_source**
> and **disable_source** handlers.

void media_device_init(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   Initializes a media device element

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

**Description**

This function initializes the media device prior to its registration.
The media device initialization and registration is split in two functions
to avoid race conditions and make the media device available to user-space
before the media graph has been completed.

So drivers need to first initialize the media device, register any entity
within the media device, create pad to pad links and then finally register
the media device by calling [`media_device_register()`](mc-core.md#c.media_device_register "media_device_register") as a final step.

The caller is responsible for initializing the media device before
registration. The following fields must be set:

- dev must point to the parent device
- model must be filled with the device model name

The bus_info field is set by [`media_device_init()`](mc-core.md#c.media_device_init "media_device_init") for PCI and platform devices
if the field begins with '0'.

void media_device_cleanup(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   Cleanups a media device element

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

**Description**

This function that will destroy the graph_mutex that is
initialized in [`media_device_init()`](mc-core.md#c.media_device_init "media_device_init").

int __media_device_register(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct module \*owner)
:   Registers a media device element

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`struct module *owner`
:   should be filled with `THIS_MODULE`

**Description**

Users, should, instead, call the [`media_device_register()`](mc-core.md#c.media_device_register "media_device_register") macro.

The caller is responsible for initializing the [`media_device`](mc-core.md#c.media_device "media_device") structure
before registration. The following fields of [`media_device`](mc-core.md#c.media_device "media_device") must be set:

> - [`media_device.model`](mc-core.md#c.media_device "media_device") must be filled with the device model name as a
>   NUL-terminated UTF-8 string. The device/model revision must not be
>   stored in this field.

The following fields are optional:

> - [`media_device.serial`](mc-core.md#c.media_device "media_device") is a unique serial number stored as a
>   NUL-terminated ASCII string. The field is big enough to store a GUID
>   in text form. If the hardware doesn't provide a unique serial number
>   this field must be left empty.
> - [`media_device.bus_info`](mc-core.md#c.media_device "media_device") represents the location of the device in the
>   system as a NUL-terminated ASCII string. For PCI/PCIe devices
>   [`media_device.bus_info`](mc-core.md#c.media_device "media_device") must be set to "PCI:" (or "PCIe:") followed by
>   the value of pci_name(). For USB devices,the [`usb_make_path()`](../usb/usb.md#c.usb_make_path "usb_make_path") function
>   must be used. This field is used by applications to distinguish between
>   otherwise identical devices that don't provide a serial number.
> - [`media_device.hw_revision`](mc-core.md#c.media_device "media_device") is the hardware device revision in a
>   driver-specific format. When possible the revision should be formatted
>   with the KERNEL_VERSION() macro.

> **Note:**
>
> 1. Upon successful registration a character device named media[0-9]+ is created. The device major and minor numbers are dynamic. The model name is exported as a sysfs attribute.
> 2. Unregistering a media device that hasn't been registered is **NOT** safe.

**Return**

returns zero on success or a negative error code.

media_device_register

`media_device_register (mdev)`

> Registers a media device element

**Parameters**

`mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

**Description**

This macro calls [`__media_device_register()`](mc-core.md#c.__media_device_register "__media_device_register") passing `THIS_MODULE` as
the [`__media_device_register()`](mc-core.md#c.__media_device_register "__media_device_register") second argument (**owner**).

void media_device_unregister(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   Unregisters a media device element

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

**Description**

It is safe to call this function on an unregistered (but initialised)
media device.

int media_device_register_entity(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   registers a media entity inside a previously registered media device.

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`struct media_entity *entity`
:   pointer to struct [`media_entity`](mc-core.md#c.media_entity "media_entity") to be registered

**Description**

Entities are identified by a unique positive integer ID. The media
controller framework will such ID automatically. IDs are not guaranteed
to be contiguous, and the ID number can change on newer Kernel versions.
So, neither the driver nor userspace should hardcode ID numbers to refer
to the entities, but, instead, use the framework to find the ID, when
needed.

The media_entity name, type and flags fields should be initialized before
calling [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity"). Entities embedded in higher-level
standard structures can have some of those fields set by the higher-level
framework.

If the device has pads, [`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init") should be called before
this function. Otherwise, the [`media_entity.pad`](mc-core.md#c.media_entity "media_entity") and [`media_entity.num_pads`](mc-core.md#c.media_entity "media_entity")
should be zeroed before calling this function.

Entities have flags that describe the entity capabilities and state:

`MEDIA_ENT_FL_DEFAULT`
:   indicates the default entity for a given type.
    This can be used to report the default audio and video devices or the
    default camera sensor.

> **Note:**
>
> Drivers should set the entity function before calling this function.
> Please notice that the values `MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN` and
> `MEDIA_ENT_F_UNKNOWN` should not be used by the drivers.

void media_device_unregister_entity(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   unregisters a media entity.

**Parameters**

`struct media_entity *entity`
:   pointer to struct [`media_entity`](mc-core.md#c.media_entity "media_entity") to be unregistered

**Description**

All links associated with the entity and all PADs are automatically
unregistered from the media_device when this function is called.

Unregistering an entity will not change the IDs of the other entities and
the previoully used ID will never be reused for a newly registered entities.

When a media device is unregistered, all its entities are unregistered
automatically. No manual entities unregistration is then required.

> **Note:**
>
> The media_entity instance itself must be freed explicitly by
> the driver if required.

void media_device_register_entity_notify(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [media_entity_notify](mc-core.md#c.media_entity_notify "media_entity_notify") \*nptr)
:   Registers a media entity_notify callback

**Parameters**

`struct media_device *mdev`
:   The media device

`struct media_entity_notify *nptr`
:   The media_entity_notify

**Description**

> **Note:**
>
> When a new entity is registered, all the registered
> media_entity_notify callbacks are invoked.

void media_device_unregister_entity_notify(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [media_entity_notify](mc-core.md#c.media_entity_notify "media_entity_notify") \*nptr)
:   Unregister a media entity notify callback

**Parameters**

`struct media_device *mdev`
:   The media device

`struct media_entity_notify *nptr`
:   The media_entity_notify

void media_device_pci_init(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [pci_dev](mc-core.md#c.media_device_pci_init "pci_dev") \*pci_dev, const char \*name)
:   create and initialize a struct [`media_device`](mc-core.md#c.media_device "media_device") from a PCI device.

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`struct pci_dev *pci_dev`
:   pointer to struct pci_dev

`const char *name`
:   media device name. If `NULL`, the routine will use the default
    name for the pci device, given by pci_name() macro.

void __media_device_usb_init(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [usb_device](../usb/usb.md#c.usb_device "usb_device") \*udev, const char \*board_name, const char \*driver_name)
:   create and initialize a struct [`media_device`](mc-core.md#c.media_device "media_device") from a PCI device.

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`struct usb_device *udev`
:   pointer to [`struct usb_device`](../usb/usb.md#c.usb_device "usb_device")

`const char *board_name`
:   media device name. If `NULL`, the routine will use the usb
    product name, if available.

`const char *driver_name`
:   name of the driver. if `NULL`, the routine will use the name
    given by `udev->dev->driver->name`, with is usually the wrong
    thing to do.

**Description**

> **Note:**
>
> It is better to call [`media_device_usb_init()`](mc-core.md#c.media_device_usb_init "media_device_usb_init") instead, as
> such macro fills driver_name with `KBUILD_MODNAME`.

media_device_usb_init

`media_device_usb_init (mdev, udev, name)`

> create and initialize a struct [`media_device`](mc-core.md#c.media_device "media_device") from a PCI device.

**Parameters**

`mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`udev`
:   pointer to [`struct usb_device`](../usb/usb.md#c.usb_device "usb_device")

`name`
:   media device name. If `NULL`, the routine will use the usb
    product name, if available.

**Description**

This macro calls [`media_device_usb_init()`](mc-core.md#c.media_device_usb_init "media_device_usb_init") passing the
[`media_device_usb_init()`](mc-core.md#c.media_device_usb_init "media_device_usb_init") **driver_name** parameter filled with
`KBUILD_MODNAME`.

void media_set_bus_info(char \*bus_info, size_t bus_info_size, struct [device](../infrastructure.md#c.device "device") \*dev)
:   Set bus_info field

**Parameters**

`char *bus_info`
:   Variable where to write the bus info (char array)

`size_t bus_info_size`
:   Length of the bus_info

`struct device *dev`
:   Related [`struct device`](../infrastructure.md#c.device "device")

**Description**

Sets bus information based on `dev`. This is currently done for PCI and
platform devices. dev is required to be non-NULL for this to happen.

This function is not meant to be called from drivers.

struct media_file_operations
:   Media device file operations

**Definition**:

```
struct media_file_operations {
    struct module *owner;
    ssize_t (*read) (struct file *, char __user *, size_t, loff_t *);
    ssize_t (*write) (struct file *, const char __user *, size_t, loff_t *);
    __poll_t (*poll) (struct file *, struct poll_table_struct *);
    long (*ioctl) (struct file *, unsigned int, unsigned long);
    long (*compat_ioctl) (struct file *, unsigned int, unsigned long);
    int (*open) (struct file *);
    int (*release) (struct file *);
};
```

**Members**

`owner`
:   should be filled with `THIS_MODULE`

`read`
:   pointer to the function that implements read() syscall

`write`
:   pointer to the function that implements write() syscall

`poll`
:   pointer to the function that implements poll() syscall

`ioctl`
:   pointer to the function that implements ioctl() syscall

`compat_ioctl`
:   pointer to the function that will handle 32 bits userspace
    calls to the ioctl() syscall on a Kernel compiled with 64 bits.

`open`
:   pointer to the function that implements open() syscall

`release`
:   pointer to the function that will release the resources allocated
    by the **open** function.

struct media_devnode
:   Media device node

**Definition**:

```
struct media_devnode {
    struct media_device *media_dev;
    const struct media_file_operations *fops;
    struct device dev;
    struct cdev cdev;
    struct device *parent;
    int minor;
    unsigned long flags;
    void (*release)(struct media_devnode *devnode);
};
```

**Members**

`media_dev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`fops`
:   pointer to struct [`media_file_operations`](mc-core.md#c.media_file_operations "media_file_operations") with media device ops

`dev`
:   pointer to struct [`device`](../infrastructure.md#c.device "device") containing the media controller device

`cdev`
:   struct cdev pointer character device

`parent`
:   parent device

`minor`
:   device node minor number

`flags`
:   flags, combination of the `MEDIA_FLAG_*` constants

`release`
:   release callback called at the end of `media_devnode_release()`
    routine at media-device.c.

**Description**

This structure represents a media-related device node.

The **parent** is a physical device. It must be set by core or device drivers
before registering the node.

int media_devnode_register(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, struct [media_devnode](mc-core.md#c.media_devnode "media_devnode") \*devnode, struct module \*owner)
:   register a media device node

**Parameters**

`struct media_device *mdev`
:   [`struct media_device`](mc-core.md#c.media_device "media_device") we want to register a device node

`struct media_devnode *devnode`
:   media device node structure we want to register

`struct module *owner`
:   should be filled with `THIS_MODULE`

**Description**

The registration code assigns minor numbers and registers the new device node
with the kernel. An error is returned if no free minor number can be found,
or if the registration of the device node fails.

Zero is returned on success.

Note that if the media_devnode_register call fails, the release() callback of
the media_devnode structure is *not* called, so the caller is responsible for
freeing any data.

void media_devnode_unregister_prepare(struct [media_devnode](mc-core.md#c.media_devnode "media_devnode") \*devnode)
:   clear the media device node register bit

**Parameters**

`struct media_devnode *devnode`
:   the device node to prepare for unregister

**Description**

This clears the passed device register bit. Future open calls will be met
with errors. Should be called before [`media_devnode_unregister()`](mc-core.md#c.media_devnode_unregister "media_devnode_unregister") to avoid
races with unregister and device file open calls.

This function can safely be called if the device node has never been
registered or has already been unregistered.

void media_devnode_unregister(struct [media_devnode](mc-core.md#c.media_devnode "media_devnode") \*devnode)
:   unregister a media device node

**Parameters**

`struct media_devnode *devnode`
:   the device node to unregister

**Description**

This unregisters the passed device. Future open calls will be met with
errors.

Should be called after [`media_devnode_unregister_prepare()`](mc-core.md#c.media_devnode_unregister_prepare "media_devnode_unregister_prepare")

struct [media_devnode](mc-core.md#c.media_devnode "media_devnode") \*media_devnode_data(struct file \*filp)
:   returns a pointer to the [`media_devnode`](mc-core.md#c.media_devnode "media_devnode")

**Parameters**

`struct file *filp`
:   pointer to struct `file`

int media_devnode_is_registered(struct [media_devnode](mc-core.md#c.media_devnode "media_devnode") \*devnode)
:   returns true if [`media_devnode`](mc-core.md#c.media_devnode "media_devnode") is registered; false otherwise.

**Parameters**

`struct media_devnode *devnode`
:   pointer to struct [`media_devnode`](mc-core.md#c.media_devnode "media_devnode").

**Note**

If mdev is NULL, it also returns false.

enum media_gobj_type
:   type of a graph object

**Constants**

`MEDIA_GRAPH_ENTITY`
:   Identify a media entity

`MEDIA_GRAPH_PAD`
:   Identify a media pad

`MEDIA_GRAPH_LINK`
:   Identify a media link

`MEDIA_GRAPH_INTF_DEVNODE`
:   Identify a media Kernel API interface via
    a device node

struct media_gobj
:   Define a graph object.

**Definition**:

```
struct media_gobj {
    struct media_device     *mdev;
    u32 id;
    struct list_head        list;
};
```

**Members**

`mdev`
:   Pointer to the struct [`media_device`](mc-core.md#c.media_device "media_device") that owns the object

`id`
:   Non-zero object ID identifier. The ID should be unique
    inside a media_device, as it is composed by
    `MEDIA_BITS_PER_TYPE` to store the type plus
    `MEDIA_BITS_PER_ID` to store the ID

`list`
:   List entry stored in one of the per-type mdev object lists

**Description**

All objects on the media graph should have this struct embedded

struct media_entity_enum
:   An enumeration of media entities.

**Definition**:

```
struct media_entity_enum {
    unsigned long *bmap;
    int idx_max;
};
```

**Members**

`bmap`
:   Bit map in which each bit represents one entity at [`struct
    media_entity`](mc-core.md#c.media_entity "media_entity")->internal_idx.

`idx_max`
:   Number of bits in bmap

struct media_graph
:   Media graph traversal state

**Definition**:

```
struct media_graph {
    struct {
        struct media_entity *entity;
        struct list_head *link;
    } stack[MEDIA_ENTITY_ENUM_MAX_DEPTH];
    struct media_entity_enum ent_enum;
    int top;
};
```

**Members**

`stack`
:   Graph traversal stack; the stack contains information
    on the path the media entities to be walked and the
    links through which they were reached.

`stack.entity`
:   pointer to [`struct media_entity`](mc-core.md#c.media_entity "media_entity") at the graph.

`stack.link`
:   pointer to `struct list_head`.

`ent_enum`
:   Visited entities

`top`
:   The top of the stack

struct media_pipeline
:   Media pipeline related information

**Definition**:

```
struct media_pipeline {
    bool allocated;
    struct media_device *mdev;
    struct list_head pads;
    int start_count;
};
```

**Members**

`allocated`
:   Media pipeline allocated and freed by the framework

`mdev`
:   The media device the pipeline is part of

`pads`
:   List of media_pipeline_pad

`start_count`
:   Media pipeline start - stop count

struct media_pipeline_pad
:   A pad part of a media pipeline

**Definition**:

```
struct media_pipeline_pad {
    struct list_head list;
    struct media_pipeline *pipe;
    struct media_pad *pad;
};
```

**Members**

`list`
:   Entry in the media_pad pads list

`pipe`
:   The media_pipeline that the pad is part of

`pad`
:   The media pad

**Description**

This structure associate a pad with a media pipeline. Instances of
media_pipeline_pad are created by [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") when it builds the
pipeline, and stored in the [`media_pad.pads`](mc-core.md#c.media_pad "media_pad") list. [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop")
removes the entries from the list and deletes them.

struct media_pipeline_pad_iter
:   Iterator for media_pipeline_for_each_pad

**Definition**:

```
struct media_pipeline_pad_iter {
    struct list_head *cursor;
};
```

**Members**

`cursor`
:   The current element

struct media_pipeline_entity_iter
:   Iterator for media_pipeline_for_each_entity

**Definition**:

```
struct media_pipeline_entity_iter {
    struct media_entity_enum ent_enum;
    struct list_head *cursor;
};
```

**Members**

`ent_enum`
:   The entity enumeration tracker

`cursor`
:   The current element

struct media_link
:   A link object part of a media graph.

**Definition**:

```
struct media_link {
    struct media_gobj graph_obj;
    struct list_head list;
    union {
        struct media_gobj *gobj0;
        struct media_pad *source;
        struct media_interface *intf;
    };
    union {
        struct media_gobj *gobj1;
        struct media_pad *sink;
        struct media_entity *entity;
    };
    struct media_link *reverse;
    unsigned long flags;
    bool is_backlink;
};
```

**Members**

`graph_obj`
:   Embedded structure containing the media object common data

`list`
:   Linked list associated with an entity or an interface that
    owns the link.

`{unnamed_union}`
:   anonymous

`gobj0`
:   Part of a union. Used to get the pointer for the first
    graph_object of the link.

`source`
:   Part of a union. Used only if the first object (gobj0) is
    a pad. In that case, it represents the source pad.

`intf`
:   Part of a union. Used only if the first object (gobj0) is
    an interface.

`{unnamed_union}`
:   anonymous

`gobj1`
:   Part of a union. Used to get the pointer for the second
    graph_object of the link.

`sink`
:   Part of a union. Used only if the second object (gobj1) is
    a pad. In that case, it represents the sink pad.

`entity`
:   Part of a union. Used only if the second object (gobj1) is
    an entity.

`reverse`
:   Pointer to the link for the reverse direction of a pad to pad
    link.

`flags`
:   Link flags, as defined in uapi/media.h (MEDIA_LNK_FL_\*)

`is_backlink`
:   Indicate if the link is a backlink.

enum media_pad_signal_type
:   type of the signal inside a media pad

**Constants**

`PAD_SIGNAL_DEFAULT`

> Default signal. Use this when all inputs or all outputs are
> uniquely identified by the pad number.

`PAD_SIGNAL_ANALOG`

> The pad contains an analog signal. It can be Radio Frequency,
> Intermediate Frequency, a baseband signal or sub-carriers.
> Tuner inputs, IF-PLL demodulators, composite and s-video signals
> should use it.

`PAD_SIGNAL_DV`

> Contains a digital video signal, with can be a bitstream of samples
> taken from an analog TV video source. On such case, it usually
> contains the VBI data on it.

`PAD_SIGNAL_AUDIO`

> Contains an Intermediate Frequency analog signal from an audio
> sub-carrier or an audio bitstream. IF signals are provided by tuners
> and consumed by audio AM/FM decoders. Bitstream audio is provided by
> an audio decoder.

struct media_pad
:   A media pad graph object.

**Definition**:

```
struct media_pad {
    struct media_gobj graph_obj;
    struct media_entity *entity;
    u16 index;
    enum media_pad_signal_type sig_type;
    unsigned long flags;
    struct media_pipeline *pipe;
};
```

**Members**

`graph_obj`
:   Embedded structure containing the media object common data

`entity`
:   Entity this pad belongs to

`index`
:   Pad index in the entity pads array, numbered from 0 to n

`sig_type`
:   Type of the signal inside a media pad

`flags`
:   Pad flags, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_PAD_FL_*`)

`pipe`
:   Pipeline this pad belongs to. Use [`media_entity_pipeline()`](mc-core.md#c.media_entity_pipeline "media_entity_pipeline") to
    access this field.

struct media_entity_operations
:   Media entity operations

**Definition**:

```
struct media_entity_operations {
    int (*get_fwnode_pad)(struct media_entity *entity, struct fwnode_endpoint *endpoint);
    int (*link_setup)(struct media_entity *entity,const struct media_pad *local, const struct media_pad *remote, u32 flags);
    int (*link_validate)(struct media_link *link);
    bool (*has_pad_interdep)(struct media_entity *entity, unsigned int pad0, unsigned int pad1);
};
```

**Members**

`get_fwnode_pad`
:   Return the pad number based on a fwnode endpoint or
    a negative value on error. This operation can be used
    to map a fwnode to a media pad number. Optional.

`link_setup`
:   Notify the entity of link changes. The operation can
    return an error, in which case link setup will be
    cancelled. Optional.

`link_validate`
:   Return whether a link is valid from the entity point of
    view. The [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") function
    validates all links by calling this operation. Optional.

`has_pad_interdep`
:   Return whether two pads of the entity are
    interdependent. If two pads are interdependent they are
    part of the same pipeline and enabling one of the pads
    means that the other pad will become "locked" and
    doesn't allow configuration changes. pad0 and pad1 are
    guaranteed to not both be sinks or sources. Never call
    the .has_pad_interdep() operation directly, always use
    media_entity_has_pad_interdep().
    Optional: If the operation isn't implemented all pads
    will be considered as interdependent.

**Description**

> **Note:**
>
> Those these callbacks are called with struct [`media_device.graph_mutex`](mc-core.md#c.media_device "media_device")
> mutex held.

enum media_entity_type
:   Media entity type

**Constants**

`MEDIA_ENTITY_TYPE_BASE`

> The entity isn't embedded in another subsystem structure.

`MEDIA_ENTITY_TYPE_VIDEO_DEVICE`

> The entity is embedded in a [`struct video_device`](v4l2-dev.md#c.video_device "video_device") instance.

`MEDIA_ENTITY_TYPE_V4L2_SUBDEV`

> The entity is embedded in a [`struct v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") instance.

**Description**

Media entity objects are often not instantiated directly, but the media
entity structure is inherited by (through embedding) other subsystem-specific
structures. The media entity type identifies the type of the subclass
structure that implements a media entity instance.

This allows runtime type identification of media entities and safe casting to
the correct object type. For instance, a media entity structure instance
embedded in a v4l2_subdev structure instance will have the type
`MEDIA_ENTITY_TYPE_V4L2_SUBDEV` and can safely be cast to a [`v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev")
structure using the container_of() macro.

struct media_entity
:   A media entity graph object.

**Definition**:

```
struct media_entity {
    struct media_gobj graph_obj;
    const char *name;
    enum media_entity_type obj_type;
    u32 function;
    unsigned long flags;
    u16 num_pads;
    u16 num_links;
    u16 num_backlinks;
    int internal_idx;
    struct media_pad *pads;
    struct list_head links;
    const struct media_entity_operations *ops;
    int use_count;
    union {
        struct {
            u32 major;
            u32 minor;
        } dev;
    } info;
};
```

**Members**

`graph_obj`
:   Embedded structure containing the media object common data.

`name`
:   Entity name.

`obj_type`
:   Type of the object that implements the media_entity.

`function`
:   Entity main function, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_ENT_F_*`)

`flags`
:   Entity flags, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_ENT_FL_*`)

`num_pads`
:   Number of sink and source pads.

`num_links`
:   Total number of links, forward and back, enabled and disabled.

`num_backlinks`
:   Number of backlinks

`internal_idx`
:   An unique internal entity specific number. The numbers are
    re-used if entities are unregistered or registered again.

`pads`
:   Pads array with the size defined by **num_pads**.

`links`
:   List of data links.

`ops`
:   Entity operations.

`use_count`
:   Use count for the entity.

`info`
:   Union with devnode information. Kept just for backward
    compatibility.

`info.dev`
:   Contains device major and minor info.

`info.dev.major`
:   device node major, if the device is a devnode.

`info.dev.minor`
:   device node minor, if the device is a devnode.

**Description**

> **Note:**
>
> The **use_count** reference count must never be negative, but is a signed
> integer on purpose: a simple `WARN_ON(<0)` check can be used to detect
> reference count bugs that would make it negative.

media_entity_for_each_pad

`media_entity_for_each_pad (entity, iter)`

> Iterate on all pads in an entity

**Parameters**

`entity`
:   The entity the pads belong to

`iter`
:   The iterator pad

**Description**

Iterate on all pads in a media entity.

struct media_interface
:   A media interface graph object.

**Definition**:

```
struct media_interface {
    struct media_gobj               graph_obj;
    struct list_head                links;
    u32 type;
    u32 flags;
};
```

**Members**

`graph_obj`
:   embedded graph object

`links`
:   List of links pointing to graph entities

`type`
:   Type of the interface as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_INTF_T_*`)

`flags`
:   Interface flags as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_INTF_FL_*`)

**Description**

> **Note:**
>
> Currently, no flags for [`media_interface`](mc-core.md#c.media_interface "media_interface") is defined.

struct media_intf_devnode
:   A media interface via a device node.

**Definition**:

```
struct media_intf_devnode {
    struct media_interface          intf;
    u32 major;
    u32 minor;
};
```

**Members**

`intf`
:   embedded interface object

`major`
:   Major number of a device node

`minor`
:   Minor number of a device node

u32 media_entity_id(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   return the media entity graph object id

**Parameters**

`struct media_entity *entity`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity")

enum [media_gobj_type](mc-core.md#c.media_gobj_type "media_gobj_type") media_type(struct [media_gobj](mc-core.md#c.media_gobj "media_gobj") \*gobj)
:   return the media object type

**Parameters**

`struct media_gobj *gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

u32 media_id(struct [media_gobj](mc-core.md#c.media_gobj "media_gobj") \*gobj)
:   return the media object ID

**Parameters**

`struct media_gobj *gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

u32 media_gobj_gen_id(enum [media_gobj_type](mc-core.md#c.media_gobj_type "media_gobj_type") type, u64 local_id)
:   encapsulates type and ID on at the object ID

**Parameters**

`enum media_gobj_type type`
:   object type as define at enum [`media_gobj_type`](mc-core.md#c.media_gobj_type "media_gobj_type").

`u64 local_id`
:   next ID, from struct [`media_device.id`](mc-core.md#c.media_device "media_device").

bool is_media_entity_v4l2_video_device(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Check if the entity is a video_device

**Parameters**

`struct media_entity *entity`
:   pointer to entity

**Return**

`true` if the entity is an instance of a video_device object and can
safely be cast to a [`struct video_device`](v4l2-dev.md#c.video_device "video_device") using the container_of() macro, or
`false` otherwise.

bool is_media_entity_v4l2_subdev(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Check if the entity is a v4l2_subdev

**Parameters**

`struct media_entity *entity`
:   pointer to entity

**Return**

`true` if the entity is an instance of a [`v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") object and can
safely be cast to a struct [`v4l2_subdev`](v4l2-subdev.md#c.v4l2_subdev "v4l2_subdev") using the container_of() macro, or
`false` otherwise.

int media_entity_enum_init(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum, struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   Initialise an entity enumeration

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration to be initialised

`struct media_device *mdev`
:   The related media device

**Return**

zero on success or a negative error code.

void media_entity_enum_cleanup(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum)
:   Release resources of an entity enumeration

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration to be released

void media_entity_enum_zero(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum)
:   Clear the entire enum

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration to be cleared

void media_entity_enum_set(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Mark a single entity in the enum

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration

`struct media_entity *entity`
:   Entity to be marked

void media_entity_enum_clear(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Unmark a single entity in the enum

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration

`struct media_entity *entity`
:   Entity to be unmarked

bool media_entity_enum_test(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Test whether the entity is marked

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration

`struct media_entity *entity`
:   Entity to be tested

**Description**

Returns `true` if the entity was marked.

bool media_entity_enum_test_and_set(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Test whether the entity is marked, and mark it

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration

`struct media_entity *entity`
:   Entity to be tested

**Description**

Returns `true` if the entity was marked, and mark it before doing so.

bool media_entity_enum_empty(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum)
:   Test whether the entire enum is empty

**Parameters**

`struct media_entity_enum *ent_enum`
:   Entity enumeration

**Return**

`true` if the entity was empty.

bool media_entity_enum_intersects(struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum1, struct [media_entity_enum](mc-core.md#c.media_entity_enum "media_entity_enum") \*ent_enum2)
:   Test whether two enums intersect

**Parameters**

`struct media_entity_enum *ent_enum1`
:   First entity enumeration

`struct media_entity_enum *ent_enum2`
:   Second entity enumeration

**Return**

`true` if entity enumerations **ent_enum1** and **ent_enum2** intersect,
otherwise `false`.

gobj_to_entity

`gobj_to_entity (gobj)`

> returns the struct [`media_entity`](mc-core.md#c.media_entity "media_entity") pointer from the **gobj** contained on it.

**Parameters**

`gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

gobj_to_pad

`gobj_to_pad (gobj)`

> returns the struct [`media_pad`](mc-core.md#c.media_pad "media_pad") pointer from the **gobj** contained on it.

**Parameters**

`gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

gobj_to_link

`gobj_to_link (gobj)`

> returns the struct [`media_link`](mc-core.md#c.media_link "media_link") pointer from the **gobj** contained on it.

**Parameters**

`gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

gobj_to_intf

`gobj_to_intf (gobj)`

> returns the struct [`media_interface`](mc-core.md#c.media_interface "media_interface") pointer from the **gobj** contained on it.

**Parameters**

`gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

intf_to_devnode

`intf_to_devnode (intf)`

> returns the [`struct media_intf_devnode`](mc-core.md#c.media_intf_devnode "media_intf_devnode") pointer from the **intf** contained on it.

**Parameters**

`intf`
:   Pointer to struct [`media_intf_devnode`](mc-core.md#c.media_intf_devnode "media_intf_devnode")

void media_gobj_create(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, enum [media_gobj_type](mc-core.md#c.media_gobj_type "media_gobj_type") type, struct [media_gobj](mc-core.md#c.media_gobj "media_gobj") \*gobj)
:   Initialize a graph object

**Parameters**

`struct media_device *mdev`
:   Pointer to the [`media_device`](mc-core.md#c.media_device "media_device") that contains the object

`enum media_gobj_type type`
:   Type of the object

`struct media_gobj *gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

**Description**

This routine initializes the embedded struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") inside a
media graph object. It is called automatically if `media_*_create`
function calls are used. However, if the object (entity, link, pad,
interface) is embedded on some other object, this function should be
called before registering the object at the media controller.

void media_gobj_destroy(struct [media_gobj](mc-core.md#c.media_gobj "media_gobj") \*gobj)
:   Stop using a graph object on a media device

**Parameters**

`struct media_gobj *gobj`
:   Pointer to the struct [`media_gobj`](mc-core.md#c.media_gobj "media_gobj") graph object

**Description**

This should be called by all routines like [`media_device_unregister()`](mc-core.md#c.media_device_unregister "media_device_unregister")
that remove/destroy media graph objects.

int media_entity_pads_init(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, u16 num_pads, struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pads)
:   Initialize the entity pads

**Parameters**

`struct media_entity *entity`
:   entity where the pads belong

`u16 num_pads`
:   total number of sink and source pads

`struct media_pad *pads`
:   Array of **num_pads** pads.

**Description**

The pads array is managed by the entity driver and passed to
[`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init") where its pointer will be stored in the
[`media_entity`](mc-core.md#c.media_entity "media_entity") structure.

If no pads are needed, drivers could either directly fill
[`media_entity->num_pads`](mc-core.md#c.media_entity "media_entity") with 0 and [`media_entity->pads`](mc-core.md#c.media_entity "media_entity") with `NULL` or call
this function that will do the same.

As the number of pads is known in advance, the pads array is not allocated
dynamically but is managed by the entity driver. Most drivers will embed the
pads array in a driver-specific structure, avoiding dynamic allocation.

Drivers must set the direction of every pad in the pads array before calling
[`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init"). The function will initialize the other pads fields.

void media_entity_cleanup(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   free resources associated with an entity

**Parameters**

`struct media_entity *entity`
:   entity where the pads belong

**Description**

This function must be called during the cleanup phase after unregistering
the entity (currently, it does nothing).

Calling [`media_entity_cleanup()`](mc-core.md#c.media_entity_cleanup "media_entity_cleanup") on a media_entity whose memory has been
zeroed but that has not been initialized with media_entity_pad_init() is
valid and is a no-op.

int media_get_pad_index(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, u32 pad_type, enum [media_pad_signal_type](mc-core.md#c.media_pad_signal_type "media_pad_signal_type") sig_type)
:   retrieves a pad index from an entity

**Parameters**

`struct media_entity *entity`
:   entity where the pads belong

`u32 pad_type`
:   the type of the pad, one of MEDIA_PAD_FL_\* pad types

`enum media_pad_signal_type sig_type`
:   type of signal of the pad to be search

**Description**

This helper function finds the first pad index inside an entity that
satisfies both **is_sink** and **sig_type** conditions.

On success, return the pad number. If the pad was not found or the media
entity is a NULL pointer, return -EINVAL.

**Return**

int media_create_pad_link(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*source, u16 source_pad, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*sink, u16 sink_pad, u32 flags)
:   creates a link between two entities.

**Parameters**

`struct media_entity *source`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity") of the source pad.

`u16 source_pad`
:   number of the source pad in the pads array

`struct media_entity *sink`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity") of the sink pad.

`u16 sink_pad`
:   number of the sink pad in the pads array.

`u32 flags`
:   Link flags, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    ( seek for `MEDIA_LNK_FL_*`)

**Description**

Valid values for flags:

`MEDIA_LNK_FL_ENABLED`
:   Indicates that the link is enabled and can be used to transfer media data.
    When two or more links target a sink pad, only one of them can be
    enabled at a time.

`MEDIA_LNK_FL_IMMUTABLE`
:   Indicates that the link enabled state can't be modified at runtime. If
    `MEDIA_LNK_FL_IMMUTABLE` is set, then `MEDIA_LNK_FL_ENABLED` must also be
    set, since an immutable link is always enabled.

> **Note:**
>
> Before calling this function, [`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init") and
> [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity") should be called previously for both ends.

int media_create_pad_links(const struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, const u32 source_function, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*source, const u16 source_pad, const u32 sink_function, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*sink, const u16 sink_pad, u32 flags, const bool allow_both_undefined)
:   creates a link between two entities.

**Parameters**

`const struct media_device *mdev`
:   Pointer to the media_device that contains the object

`const u32 source_function`
:   Function of the source entities. Used only if **source** is
    NULL.

`struct media_entity *source`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity") of the source pad. If NULL, it will use
    all entities that matches the **sink_function**.

`const u16 source_pad`
:   number of the source pad in the pads array

`const u32 sink_function`
:   Function of the sink entities. Used only if **sink** is NULL.

`struct media_entity *sink`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity") of the sink pad. If NULL, it will use
    all entities that matches the **sink_function**.

`const u16 sink_pad`
:   number of the sink pad in the pads array.

`u32 flags`
:   Link flags, as defined in include/uapi/linux/media.h.

`const bool allow_both_undefined`
:   if `true`, then both **source** and **sink** can be NULL.
    In such case, it will create a crossbar between all entities that
    matches **source_function** to all entities that matches **sink_function**.
    If `false`, it will return 0 and won't create any link if both **source**
    and **sink** are NULL.

**Description**

Valid values for flags:

A `MEDIA_LNK_FL_ENABLED` flag indicates that the link is enabled and can be
:   used to transfer media data. If multiple links are created and this
    flag is passed as an argument, only the first created link will have
    this flag.

A `MEDIA_LNK_FL_IMMUTABLE` flag indicates that the link enabled state can't
:   be modified at runtime. If `MEDIA_LNK_FL_IMMUTABLE` is set, then
    `MEDIA_LNK_FL_ENABLED` must also be set since an immutable link is
    always enabled.

It is common for some devices to have multiple source and/or sink entities
of the same type that should be linked. While [`media_create_pad_link()`](mc-core.md#c.media_create_pad_link "media_create_pad_link")
creates link by link, this function is meant to allow 1:n, n:1 and even
cross-bar (n:n) links.

> **Note:**
>
> Before calling this function, [`media_entity_pads_init()`](mc-core.md#c.media_entity_pads_init "media_entity_pads_init") and
> [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity") should be called previously for the
> entities to be linked.

void media_entity_remove_links(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   remove all links associated with an entity

**Parameters**

`struct media_entity *entity`
:   pointer to [`media_entity`](mc-core.md#c.media_entity "media_entity")

**Description**

> **Note:**
>
> This is called automatically when an entity is unregistered via
> [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity").

int __media_entity_setup_link(struct [media_link](mc-core.md#c.media_link "media_link") \*link, u32 flags)
:   Configure a media link without locking

**Parameters**

`struct media_link *link`
:   The link being configured

`u32 flags`
:   Link configuration flags

**Description**

The bulk of link setup is handled by the two entities connected through the
link. This function notifies both entities of the link configuration change.

If the link is immutable or if the current and new configuration are
identical, return immediately.

The user is expected to hold link->source->parent->mutex. If not,
[`media_entity_setup_link()`](mc-core.md#c.media_entity_setup_link "media_entity_setup_link") should be used instead.

int media_entity_setup_link(struct [media_link](mc-core.md#c.media_link "media_link") \*link, u32 flags)
:   changes the link flags properties in runtime

**Parameters**

`struct media_link *link`
:   pointer to [`media_link`](mc-core.md#c.media_link "media_link")

`u32 flags`
:   the requested new link flags

**Description**

The only configurable property is the `MEDIA_LNK_FL_ENABLED` link flag
to enable/disable a link. Links marked with the
`MEDIA_LNK_FL_IMMUTABLE` link flag can not be enabled or disabled.

When a link is enabled or disabled, the media framework calls the
link_setup operation for the two entities at the source and sink of the
link, in that order. If the second link_setup call fails, another
link_setup call is made on the first entity to restore the original link
flags.

Media device drivers can be notified of link setup operations by setting the
[`media_device.link_notify`](mc-core.md#c.media_device "media_device") pointer to a callback function. If provided, the
notification callback will be called before enabling and after disabling
links.

Entity drivers must implement the link_setup operation if any of their links
is non-immutable. The operation must either configure the hardware or store
the configuration information to be applied later.

Link configuration must not have any side effect on other links. If an
enabled link at a sink pad prevents another link at the same pad from
being enabled, the link_setup operation must return `-EBUSY` and can't
implicitly disable the first enabled link.

> **Note:**
>
> The valid values of the flags for the link is the same as described
> on [`media_create_pad_link()`](mc-core.md#c.media_create_pad_link "media_create_pad_link"), for pad to pad links or the same as described
> on [`media_create_intf_link()`](mc-core.md#c.media_create_intf_link "media_create_intf_link"), for interface to entity links.

struct [media_link](mc-core.md#c.media_link "media_link") \*media_entity_find_link(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*source, struct [media_pad](mc-core.md#c.media_pad "media_pad") \*sink)
:   Find a link between two pads

**Parameters**

`struct media_pad *source`
:   Source pad

`struct media_pad *sink`
:   Sink pad

**Return**

returns a pointer to the link between the two entities. If no
such link exists, return `NULL`.

struct [media_pad](mc-core.md#c.media_pad "media_pad") \*media_pad_remote_pad_first(const struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Find the first pad at the remote end of a link

**Parameters**

`const struct media_pad *pad`
:   Pad at the local end of the link

**Description**

Search for a remote pad connected to the given pad by iterating over all
links originating or terminating at that pad until an enabled link is found.

**Return**

returns a pointer to the pad at the remote end of the first found
enabled link, or `NULL` if no enabled link has been found.

struct [media_pad](mc-core.md#c.media_pad "media_pad") \*media_pad_remote_pad_unique(const struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Find a remote pad connected to a pad

**Parameters**

`const struct media_pad *pad`
:   The pad

**Description**

Search for and return a remote pad connected to **pad** through an enabled
link. If multiple (or no) remote pads are found, an error is returned.

The uniqueness constraint makes this helper function suitable for entities
that support a single active source at a time on a given pad.

- -ENOTUNIQ - Multiple links are enabled
- -ENOLINK - No connected pad found

**Return**

A pointer to the remote pad, or one of the following error pointers
if an error occurs:

struct [media_pad](mc-core.md#c.media_pad "media_pad") \*media_entity_remote_pad_unique(const struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, unsigned int type)
:   Find a remote pad connected to an entity

**Parameters**

`const struct media_entity *entity`
:   The entity

`unsigned int type`
:   The type of pad to find (MEDIA_PAD_FL_SINK or MEDIA_PAD_FL_SOURCE)

**Description**

Search for and return a remote pad of **type** connected to **entity** through an
enabled link. If multiple (or no) remote pads match these criteria, an error
is returned.

The uniqueness constraint makes this helper function suitable for entities
that support a single active source or sink at a time.

- -ENOTUNIQ - Multiple links are enabled
- -ENOLINK - No connected pad found

**Return**

A pointer to the remote pad, or one of the following error pointers
if an error occurs:

struct [media_pad](mc-core.md#c.media_pad "media_pad") \*media_entity_remote_source_pad_unique(const struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Find a remote source pad connected to an entity

**Parameters**

`const struct media_entity *entity`
:   The entity

**Description**

Search for and return a remote source pad connected to **entity** through an
enabled link. If multiple (or no) remote pads match these criteria, an error
is returned.

The uniqueness constraint makes this helper function suitable for entities
that support a single active source at a time.

- -ENOTUNIQ - Multiple links are enabled
- -ENOLINK - No connected pad found

**Return**

A pointer to the remote pad, or one of the following error pointers
if an error occurs:

bool media_pad_is_streaming(const struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Test if a pad is part of a streaming pipeline

**Parameters**

`const struct media_pad *pad`
:   The pad

**Return**

True if the pad is part of a pipeline started with the
[`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") function, false otherwise.

bool media_entity_is_streaming(const struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Test if an entity is part of a streaming pipeline

**Parameters**

`const struct media_entity *entity`
:   The entity

**Return**

True if the entity is part of a pipeline started with the
[`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") function, false otherwise.

struct [media_pipeline](mc-core.md#c.media_pipeline "media_pipeline") \*media_entity_pipeline(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Get the media pipeline an entity is part of

**Parameters**

`struct media_entity *entity`
:   The entity

**Description**

DEPRECATED: use [`media_pad_pipeline()`](mc-core.md#c.media_pad_pipeline "media_pad_pipeline") instead.

This function returns the media pipeline that an entity has been associated
with when constructing the pipeline with [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start"). The pointer
remains valid until [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop") is called.

In general, entities can be part of multiple pipelines, when carrying
multiple streams (either on different pads, or on the same pad using
multiplexed streams). This function is to be used only for entities that
do not support multiple pipelines.

**Return**

The media_pipeline the entity is part of, or NULL if the entity is
not part of any pipeline.

struct [media_pipeline](mc-core.md#c.media_pipeline "media_pipeline") \*media_pad_pipeline(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Get the media pipeline a pad is part of

**Parameters**

`struct media_pad *pad`
:   The pad

**Description**

This function returns the media pipeline that a pad has been associated
with when constructing the pipeline with [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start"). The pointer
remains valid until [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop") is called.

**Return**

The media_pipeline the pad is part of, or NULL if the pad is
not part of any pipeline.

int media_entity_get_fwnode_pad(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, const struct fwnode_handle \*fwnode, unsigned long direction_flags)
:   Get pad number from fwnode

**Parameters**

`struct media_entity *entity`
:   The entity

`const struct fwnode_handle *fwnode`
:   Pointer to the fwnode_handle which should be used to find the pad

`unsigned long direction_flags`
:   Expected direction of the pad, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    (seek for `MEDIA_PAD_FL_*`)

**Description**

This function can be used to resolve the media pad number from
a fwnode. This is useful for devices which use more complex
mappings of media pads.

If the entity does not implement the get_fwnode_pad() operation
then this function searches the entity for the first pad that
matches the **direction_flags**.

**Return**

returns the pad number on success or a negative error code.

int media_graph_walk_init(struct [media_graph](mc-core.md#c.media_graph "media_graph") \*graph, struct [media_device](mc-core.md#c.media_device "media_device") \*mdev)
:   Allocate resources used by graph walk.

**Parameters**

`struct media_graph *graph`
:   Media graph structure that will be used to walk the graph

`struct media_device *mdev`
:   Pointer to the [`media_device`](mc-core.md#c.media_device "media_device") that contains the object

**Description**

This function is deprecated, use [`media_pipeline_for_each_pad()`](mc-core.md#c.media_pipeline_for_each_pad "media_pipeline_for_each_pad") instead.

The caller is required to hold the media_device graph_mutex during the graph
walk until the graph state is released.

Returns zero on success or a negative error code otherwise.

void media_graph_walk_cleanup(struct [media_graph](mc-core.md#c.media_graph "media_graph") \*graph)
:   Release resources used by graph walk.

**Parameters**

`struct media_graph *graph`
:   Media graph structure that will be used to walk the graph

**Description**

This function is deprecated, use [`media_pipeline_for_each_pad()`](mc-core.md#c.media_pipeline_for_each_pad "media_pipeline_for_each_pad") instead.

void media_graph_walk_start(struct [media_graph](mc-core.md#c.media_graph "media_graph") \*graph, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity)
:   Start walking the media graph at a given entity

**Parameters**

`struct media_graph *graph`
:   Media graph structure that will be used to walk the graph

`struct media_entity *entity`
:   Starting entity

**Description**

This function is deprecated, use [`media_pipeline_for_each_pad()`](mc-core.md#c.media_pipeline_for_each_pad "media_pipeline_for_each_pad") instead.

Before using this function, [`media_graph_walk_init()`](mc-core.md#c.media_graph_walk_init "media_graph_walk_init") must be
used to allocate resources used for walking the graph. This
function initializes the graph traversal structure to walk the
entities graph starting at the given entity. The traversal
structure must not be modified by the caller during graph
traversal. After the graph walk, the resources must be released
using [`media_graph_walk_cleanup()`](mc-core.md#c.media_graph_walk_cleanup "media_graph_walk_cleanup").

struct [media_entity](mc-core.md#c.media_entity "media_entity") \*media_graph_walk_next(struct [media_graph](mc-core.md#c.media_graph "media_graph") \*graph)
:   Get the next entity in the graph

**Parameters**

`struct media_graph *graph`
:   Media graph structure

**Description**

This function is deprecated, use [`media_pipeline_for_each_pad()`](mc-core.md#c.media_pipeline_for_each_pad "media_pipeline_for_each_pad") instead.

Perform a depth-first traversal of the given media entities graph.

The graph structure must have been previously initialized with a call to
[`media_graph_walk_start()`](mc-core.md#c.media_graph_walk_start "media_graph_walk_start").

**Return**

returns the next entity in the graph or `NULL` if the whole graph
have been traversed.

int media_pipeline_start(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad, struct [media_pipeline](mc-core.md#c.media_pipeline "media_pipeline") \*pipe)
:   Mark a pipeline as streaming

**Parameters**

`struct media_pad *pad`
:   Starting pad

`struct media_pipeline *pipe`
:   Media pipeline to be assigned to all pads in the pipeline.

**Description**

Mark all pads connected to a given pad through enabled links, either
directly or indirectly, as streaming. The given pipeline object is assigned
to every pad in the pipeline and stored in the media_pad pipe field.

Calls to this function can be nested, in which case the same number of
[`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop") calls will be required to stop streaming. The
pipeline pointer must be identical for all nested calls to
[`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start").

int __media_pipeline_start(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad, struct [media_pipeline](mc-core.md#c.media_pipeline "media_pipeline") \*pipe)
:   Mark a pipeline as streaming

**Parameters**

`struct media_pad *pad`
:   Starting pad

`struct media_pipeline *pipe`
:   Media pipeline to be assigned to all pads in the pipeline.

**Description**

..note:: This is the non-locking version of [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start")

void media_pipeline_stop(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Mark a pipeline as not streaming

**Parameters**

`struct media_pad *pad`
:   Starting pad

**Description**

Mark all pads connected to a given pad through enabled links, either
directly or indirectly, as not streaming. The media_pad pipe field is
reset to `NULL`.

If multiple calls to [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") have been made, the same
number of calls to this function are required to mark the pipeline as not
streaming.

void __media_pipeline_stop(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Mark a pipeline as not streaming

**Parameters**

`struct media_pad *pad`
:   Starting pad

**Description**

> **Note:**
>
> This is the non-locking version of [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop")

media_pipeline_for_each_pad

`media_pipeline_for_each_pad (pipe, iter, pad)`

> Iterate on all pads in a media pipeline

**Parameters**

`pipe`
:   The pipeline

`iter`
:   The iterator ([`struct media_pipeline_pad_iter`](mc-core.md#c.media_pipeline_pad_iter "media_pipeline_pad_iter"))

`pad`
:   The iterator pad

**Description**

Iterate on all pads in a media pipeline. This is only valid after the
pipeline has been built with [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") and before it gets
destroyed with [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop").

int media_pipeline_entity_iter_init(struct [media_pipeline](mc-core.md#c.media_pipeline "media_pipeline") \*pipe, struct [media_pipeline_entity_iter](mc-core.md#c.media_pipeline_entity_iter "media_pipeline_entity_iter") \*iter)
:   Initialize a pipeline entity iterator

**Parameters**

`struct media_pipeline *pipe`
:   The pipeline

`struct media_pipeline_entity_iter *iter`
:   The iterator

**Description**

This function must be called to initialize the iterator before using it in a
[`media_pipeline_for_each_entity()`](mc-core.md#c.media_pipeline_for_each_entity "media_pipeline_for_each_entity") loop. The iterator must be destroyed by a
call to media_pipeline_entity_iter_cleanup after the loop (including in code
paths that break from the loop).

The same iterator can be used in multiple consecutive loops without being
destroyed and reinitialized.

**Return**

0 on success or a negative error code otherwise.

void media_pipeline_entity_iter_cleanup(struct [media_pipeline_entity_iter](mc-core.md#c.media_pipeline_entity_iter "media_pipeline_entity_iter") \*iter)
:   Destroy a pipeline entity iterator

**Parameters**

`struct media_pipeline_entity_iter *iter`
:   The iterator

**Description**

This function must be called to destroy iterators initialized with
[`media_pipeline_entity_iter_init()`](mc-core.md#c.media_pipeline_entity_iter_init "media_pipeline_entity_iter_init").

media_pipeline_for_each_entity

`media_pipeline_for_each_entity (pipe, iter, entity)`

> Iterate on all entities in a media pipeline

**Parameters**

`pipe`
:   The pipeline

`iter`
:   The iterator ([`struct media_pipeline_entity_iter`](mc-core.md#c.media_pipeline_entity_iter "media_pipeline_entity_iter"))

`entity`
:   The iterator entity

**Description**

Iterate on all entities in a media pipeline. This is only valid after the
pipeline has been built with [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") and before it gets
destroyed with [`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop"). The iterator must be initialized with
[`media_pipeline_entity_iter_init()`](mc-core.md#c.media_pipeline_entity_iter_init "media_pipeline_entity_iter_init") before iteration, and destroyed with
[`media_pipeline_entity_iter_cleanup()`](mc-core.md#c.media_pipeline_entity_iter_cleanup "media_pipeline_entity_iter_cleanup") after (including in code paths that
break from the loop).

int media_pipeline_alloc_start(struct [media_pad](mc-core.md#c.media_pad "media_pad") \*pad)
:   Mark a pipeline as streaming

**Parameters**

`struct media_pad *pad`
:   Starting pad

**Description**

[`media_pipeline_alloc_start()`](mc-core.md#c.media_pipeline_alloc_start "media_pipeline_alloc_start") is similar to [`media_pipeline_start()`](mc-core.md#c.media_pipeline_start "media_pipeline_start") but instead
of working on a given pipeline the function will use an existing pipeline if
the pad is already part of a pipeline, or allocate a new pipeline.

Calls to [`media_pipeline_alloc_start()`](mc-core.md#c.media_pipeline_alloc_start "media_pipeline_alloc_start") must be matched with
[`media_pipeline_stop()`](mc-core.md#c.media_pipeline_stop "media_pipeline_stop").

struct [media_intf_devnode](mc-core.md#c.media_intf_devnode "media_intf_devnode") \*media_devnode_create(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, u32 type, u32 flags, u32 major, u32 minor)
:   creates and initializes a device node interface

**Parameters**

`struct media_device *mdev`
:   pointer to struct [`media_device`](mc-core.md#c.media_device "media_device")

`u32 type`
:   type of the interface, as given by
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    ( seek for `MEDIA_INTF_T_*`) macros.

`u32 flags`
:   Interface flags, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    ( seek for `MEDIA_INTF_FL_*`)

`u32 major`
:   Device node major number.

`u32 minor`
:   Device node minor number.

**Return**

if succeeded, returns a pointer to the newly allocated
:   [`media_intf_devnode`](mc-core.md#c.media_intf_devnode "media_intf_devnode") pointer.

**Description**

> **Note:**
>
> Currently, no flags for [`media_interface`](mc-core.md#c.media_interface "media_interface") is defined.

void media_devnode_remove(struct [media_intf_devnode](mc-core.md#c.media_intf_devnode "media_intf_devnode") \*devnode)
:   removes a device node interface

**Parameters**

`struct media_intf_devnode *devnode`
:   pointer to [`media_intf_devnode`](mc-core.md#c.media_intf_devnode "media_intf_devnode") to be freed.

**Description**

When a device node interface is removed, all links to it are automatically
removed.

struct [media_link](mc-core.md#c.media_link "media_link") \*media_create_intf_link(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, struct [media_interface](mc-core.md#c.media_interface "media_interface") \*intf, u32 flags)
:   creates a link between an entity and an interface

**Parameters**

`struct media_entity *entity`
:   pointer to `media_entity`

`struct media_interface *intf`
:   pointer to `media_interface`

`u32 flags`
:   Link flags, as defined in
    [include/uapi/linux/media.h](../../userspace-api/media/mediactl/media-header.md#media-header)
    ( seek for `MEDIA_LNK_FL_*`)

**Description**

Valid values for flags:

`MEDIA_LNK_FL_ENABLED`
:   Indicates that the interface is connected to the entity hardware.
    That's the default value for interfaces. An interface may be disabled if
    the hardware is busy due to the usage of some other interface that it is
    currently controlling the hardware.

    A typical example is an hybrid TV device that handle only one type of
    stream on a given time. So, when the digital TV is streaming,
    the V4L2 interfaces won't be enabled, as such device is not able to
    also stream analog TV or radio.

> **Note:**
>
> Before calling this function, [`media_devnode_create()`](mc-core.md#c.media_devnode_create "media_devnode_create") should be called for
> the interface and [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity") should be called for the
> interface that will be part of the link.

void __media_remove_intf_link(struct [media_link](mc-core.md#c.media_link "media_link") \*link)
:   remove a single interface link

**Parameters**

`struct media_link *link`
:   pointer to [`media_link`](mc-core.md#c.media_link "media_link").

**Description**

> **Note:**
>
> This is an unlocked version of [`media_remove_intf_link()`](mc-core.md#c.media_remove_intf_link "media_remove_intf_link")

void media_remove_intf_link(struct [media_link](mc-core.md#c.media_link "media_link") \*link)
:   remove a single interface link

**Parameters**

`struct media_link *link`
:   pointer to [`media_link`](mc-core.md#c.media_link "media_link").

**Description**

> **Note:**
>
> Prefer to use this one, instead of [`__media_remove_intf_link()`](mc-core.md#c.__media_remove_intf_link "__media_remove_intf_link")

void __media_remove_intf_links(struct [media_interface](mc-core.md#c.media_interface "media_interface") \*intf)
:   remove all links associated with an interface

**Parameters**

`struct media_interface *intf`
:   pointer to [`media_interface`](mc-core.md#c.media_interface "media_interface")

**Description**

> **Note:**
>
> This is an unlocked version of [`media_remove_intf_links()`](mc-core.md#c.media_remove_intf_links "media_remove_intf_links").

void media_remove_intf_links(struct [media_interface](mc-core.md#c.media_interface "media_interface") \*intf)
:   remove all links associated with an interface

**Parameters**

`struct media_interface *intf`
:   pointer to [`media_interface`](mc-core.md#c.media_interface "media_interface")

**Description**

> **Note:**
>
> 1. This is called automatically when an entity is unregistered via
>    [`media_device_register_entity()`](mc-core.md#c.media_device_register_entity "media_device_register_entity") and by [`media_devnode_remove()`](mc-core.md#c.media_devnode_remove "media_devnode_remove").
> 2. Prefer to use this one, instead of [`__media_remove_intf_links()`](mc-core.md#c.__media_remove_intf_links "__media_remove_intf_links").

media_entity_call

`media_entity_call (entity, operation, args...)`

> Calls a [`struct media_entity_operations`](mc-core.md#c.media_entity_operations "media_entity_operations") operation on an entity

**Parameters**

`entity`
:   entity where the **operation** will be called

`operation`
:   type of the operation. Should be the name of a member of
    struct [`media_entity_operations`](mc-core.md#c.media_entity_operations "media_entity_operations").

`args...`
:   variable arguments

**Description**

This helper function will check if **operation** is not `NULL`. On such case,
it will issue a call to **operation**(**entity**, **args**).

struct [media_link](mc-core.md#c.media_link "media_link") \*media_create_ancillary_link(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*primary, struct [media_entity](mc-core.md#c.media_entity "media_entity") \*ancillary)
:   create an ancillary link between two instances of [`media_entity`](mc-core.md#c.media_entity "media_entity")

**Parameters**

`struct media_entity *primary`
:   pointer to the primary [`media_entity`](mc-core.md#c.media_entity "media_entity")

`struct media_entity *ancillary`
:   pointer to the ancillary [`media_entity`](mc-core.md#c.media_entity "media_entity")

**Description**

Create an ancillary link between two entities, indicating that they
represent two connected pieces of hardware that form a single logical unit.
A typical example is a camera lens controller being linked to the sensor that
it is supporting.

The function sets both MEDIA_LNK_FL_ENABLED and MEDIA_LNK_FL_IMMUTABLE for
the new link.

struct [media_link](mc-core.md#c.media_link "media_link") \*__media_entity_next_link(struct [media_entity](mc-core.md#c.media_entity "media_entity") \*entity, struct [media_link](mc-core.md#c.media_link "media_link") \*link, unsigned long link_type)
:   Iterate through a [`media_entity`](mc-core.md#c.media_entity "media_entity")'s links

**Parameters**

`struct media_entity *entity`
:   pointer to the [`media_entity`](mc-core.md#c.media_entity "media_entity")

`struct media_link *link`
:   pointer to a [`media_link`](mc-core.md#c.media_link "media_link") to hold the iterated values

`unsigned long link_type`
:   one of the MEDIA_LNK_FL_LINK_TYPE flags

**Description**

Return the next link against an entity matching a specific link type. This
allows iteration through an entity's links whilst guaranteeing all of the
returned links are of the given type.

for_each_media_entity_data_link

`for_each_media_entity_data_link (entity, link)`

> Iterate through an entity's data links

**Parameters**

`entity`
:   pointer to the [`media_entity`](mc-core.md#c.media_entity "media_entity")

`link`
:   pointer to a [`media_link`](mc-core.md#c.media_link "media_link") to hold the iterated values

**Description**

Iterate over a [`media_entity`](mc-core.md#c.media_entity "media_entity")'s data links

enum media_request_state
:   media request state

**Constants**

`MEDIA_REQUEST_STATE_IDLE`
:   Idle

`MEDIA_REQUEST_STATE_VALIDATING`
:   Validating the request, no state changes
    allowed

`MEDIA_REQUEST_STATE_QUEUED`
:   Queued

`MEDIA_REQUEST_STATE_COMPLETE`
:   Completed, the request is done

`MEDIA_REQUEST_STATE_CLEANING`
:   Cleaning, the request is being re-inited

`MEDIA_REQUEST_STATE_UPDATING`
:   The request is being updated, i.e.
    request objects are being added,
    modified or removed

`NR_OF_MEDIA_REQUEST_STATE`
:   The number of media request states, used
    internally for sanity check purposes

struct media_request
:   Media device request

**Definition**:

```
struct media_request {
    struct media_device *mdev;
    struct kref kref;
    char debug_str[TASK_COMM_LEN + 11];
    enum media_request_state state;
    unsigned int updating_count;
    unsigned int access_count;
    struct list_head objects;
    unsigned int num_incomplete_objects;
    wait_queue_head_t poll_wait;
    spinlock_t lock;
};
```

**Members**

`mdev`
:   Media device this request belongs to

`kref`
:   Reference count

`debug_str`
:   Prefix for debug messages (process name:fd)

`state`
:   The state of the request

`updating_count`
:   count the number of request updates that are in progress

`access_count`
:   count the number of request accesses that are in progress

`objects`
:   List of **struct** media_request_object request objects

`num_incomplete_objects`
:   The number of incomplete objects in the request

`poll_wait`
:   Wait queue for poll

`lock`
:   Serializes access to this struct

int media_request_lock_for_access(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Lock the request to access its objects

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Use before accessing a completed request. A reference to the request must
be held during the access. This usually takes place automatically through
a file handle. Use **media_request_unlock_for_access** when done.

void media_request_unlock_for_access(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Unlock a request previously locked for access

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Unlock a request that has previously been locked using
**media_request_lock_for_access**.

int media_request_lock_for_update(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Lock the request for updating its objects

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Use before updating a request, i.e. adding, modifying or removing a request
object in it. A reference to the request must be held during the update. This
usually takes place automatically through a file handle. Use
**media_request_unlock_for_update** when done.

void media_request_unlock_for_update(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Unlock a request previously locked for update

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Unlock a request that has previously been locked using
**media_request_lock_for_update**.

void media_request_get(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Get the media request

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Get the media request.

void media_request_put(struct [media_request](mc-core.md#c.media_request "media_request") \*req)
:   Put the media request

**Parameters**

`struct media_request *req`
:   The media request

**Description**

Put the media request. The media request will be released
when the refcount reaches 0.

struct [media_request](mc-core.md#c.media_request "media_request") \*media_request_get_by_fd(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, int request_fd)
:   Get a media request by fd

**Parameters**

`struct media_device *mdev`
:   Media device this request belongs to

`int request_fd`
:   The file descriptor of the request

**Description**

Get the request represented by **request_fd** that is owned
by the media device.

Return a -EBADR error pointer if requests are not supported
by this driver. Return -EINVAL if the request was not found.
Return the pointer to the request if found: the caller will
have to call **media_request_put** when it finished using the
request.

int media_request_alloc(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, int \*alloc_fd)
:   Allocate the media request

**Parameters**

`struct media_device *mdev`
:   Media device this request belongs to

`int *alloc_fd`
:   Store the request's file descriptor in this int

**Description**

Allocated the media request and put the fd in **alloc_fd**.

struct media_request_object_ops
:   Media request object operations

**Definition**:

```
struct media_request_object_ops {
    int (*prepare)(struct media_request_object *object);
    void (*unprepare)(struct media_request_object *object);
    void (*queue)(struct media_request_object *object);
    void (*unbind)(struct media_request_object *object);
    void (*release)(struct media_request_object *object);
};
```

**Members**

`prepare`
:   Validate and prepare the request object, optional.

`unprepare`
:   Unprepare the request object, optional.

`queue`
:   Queue the request object, optional.

`unbind`
:   Unbind the request object, optional.

`release`
:   Release the request object, required.

struct media_request_object
:   An opaque object that belongs to a media request

**Definition**:

```
struct media_request_object {
    const struct media_request_object_ops *ops;
    void *priv;
    struct media_request *req;
    struct list_head list;
    struct kref kref;
    bool completed;
};
```

**Members**

`ops`
:   object's operations

`priv`
:   object's priv pointer

`req`
:   the request this object belongs to (can be NULL)

`list`
:   List entry of the object for **struct** media_request

`kref`
:   Reference count of the object, acquire before releasing req->lock

`completed`
:   If true, then this object was completed.

**Description**

An object related to the request. This struct is always embedded in
another struct that contains the actual data for this request object.

void media_request_object_get(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Get a media request object

**Parameters**

`struct media_request_object *obj`
:   The object

**Description**

Get a media request object.

void media_request_object_put(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Put a media request object

**Parameters**

`struct media_request_object *obj`
:   The object

**Description**

Put a media request object. Once all references are gone, the
object's memory is released.

struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*media_request_object_find(struct [media_request](mc-core.md#c.media_request "media_request") \*req, const struct [media_request_object_ops](mc-core.md#c.media_request_object_ops "media_request_object_ops") \*ops, void \*priv)
:   Find an object in a request

**Parameters**

`struct media_request *req`
:   The media request

`const struct media_request_object_ops *ops`
:   Find an object with this ops value

`void *priv`
:   Find an object with this priv value

**Description**

Both **ops** and **priv** must be non-NULL.

Returns the object pointer or NULL if not found. The caller must
call [`media_request_object_put()`](mc-core.md#c.media_request_object_put "media_request_object_put") once it finished using the object.

Since this function needs to walk the list of objects it takes
the **req->lock** spin lock to make this safe.

void media_request_object_init(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Initialise a media request object

**Parameters**

`struct media_request_object *obj`
:   The object

**Description**

Initialise a media request object. The object will be released using the
release callback of the ops once it has no references (this function
initialises references to one).

int media_request_object_bind(struct [media_request](mc-core.md#c.media_request "media_request") \*req, const struct [media_request_object_ops](mc-core.md#c.media_request_object_ops "media_request_object_ops") \*ops, void \*priv, bool is_buffer, struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Bind a media request object to a request

**Parameters**

`struct media_request *req`
:   The media request

`const struct media_request_object_ops *ops`
:   The object ops for this object

`void *priv`
:   A driver-specific priv pointer associated with this object

`bool is_buffer`
:   Set to true if the object a buffer object.

`struct media_request_object *obj`
:   The object

**Description**

Bind this object to the request and set the ops and priv values of
the object so it can be found later with [`media_request_object_find()`](mc-core.md#c.media_request_object_find "media_request_object_find").

Every bound object must be unbound or completed by the kernel at some
point in time, otherwise the request will never complete. When the
request is released all completed objects will be unbound by the
request core code.

Buffer objects will be added to the end of the request's object
list, non-buffer objects will be added to the front of the list.
This ensures that all buffer objects are at the end of the list
and that all non-buffer objects that they depend on are processed
first.

void media_request_object_unbind(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Unbind a media request object

**Parameters**

`struct media_request_object *obj`
:   The object

**Description**

Unbind the media request object from the request.

void media_request_object_complete(struct [media_request_object](mc-core.md#c.media_request_object "media_request_object") \*obj)
:   Mark the media request object as complete

**Parameters**

`struct media_request_object *obj`
:   The object

**Description**

Mark the media request object as complete. Only bound objects can
be completed.

struct [media_device](mc-core.md#c.media_device "media_device") \*media_device_usb_allocate(struct [usb_device](../usb/usb.md#c.usb_device "usb_device") \*udev, const char \*module_name, struct module \*owner)
:   Allocate and return struct `media` device

**Parameters**

`struct usb_device *udev`
:   struct [`usb_device`](../usb/usb.md#c.usb_device "usb_device") pointer

`const char *module_name`
:   should be filled with `KBUILD_MODNAME`

`struct module *owner`
:   struct module pointer `THIS_MODULE` for the driver.
    `THIS_MODULE` is null for a built-in driver.
    It is safe even when `THIS_MODULE` is null.

**Description**

This interface should be called to allocate a Media Device when multiple
drivers share usb_device and the media device. This interface allocates
[`media_device`](mc-core.md#c.media_device "media_device") structure and calls [`media_device_usb_init()`](mc-core.md#c.media_device_usb_init "media_device_usb_init") to initialize
it.

void media_device_delete(struct [media_device](mc-core.md#c.media_device "media_device") \*mdev, const char \*module_name, struct module \*owner)
:   Release media device. Calls kref_put().

**Parameters**

`struct media_device *mdev`
:   struct [`media_device`](mc-core.md#c.media_device "media_device") pointer

`const char *module_name`
:   should be filled with `KBUILD_MODNAME`

`struct module *owner`
:   struct module pointer `THIS_MODULE` for the driver.
    `THIS_MODULE` is null for a built-in driver.
    It is safe even when `THIS_MODULE` is null.

**Description**

This interface should be called to put Media Device Instance kref.
