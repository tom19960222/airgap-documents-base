---
collection: kernel
version: "6.8"
title: "Kernel clients"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/drm-client.html
fetched_at: 2026-08-21T03:39:02+00:00
---
# Kernel clients

This library provides support for clients running in the kernel like fbdev and bootsplash.

GEM drivers which provide a GEM based dumb buffer with a virtual address are supported.

struct drm_client_funcs
:   DRM client callbacks

**Definition**:

```
struct drm_client_funcs {
    struct module *owner;
    void (*unregister)(struct drm_client_dev *client);
    int (*restore)(struct drm_client_dev *client);
    int (*hotplug)(struct drm_client_dev *client);
};
```

**Members**

`owner`
:   The module owner

`unregister`
:   Called when [`drm_device`](drm-internals.md#c.drm_device "drm_device") is unregistered. The client should respond by
    releasing its resources using [`drm_client_release()`](drm-client.md#c.drm_client_release "drm_client_release").

    This callback is optional.

`restore`
:   Called on drm_lastclose(). The first client instance in the list that
    returns zero gets the privilege to restore and no more clients are
    called. This callback is not called after **unregister** has been called.

    Note that the core does not guarantee exclusion against concurrent
    [`drm_open()`](drm-internals.md#c.drm_open "drm_open"). Clients need to ensure this themselves, for example by
    using drm_master_internal_acquire() and
    drm_master_internal_release().

    This callback is optional.

`hotplug`
:   Called on [`drm_kms_helper_hotplug_event()`](drm-kms-helpers.md#c.drm_kms_helper_hotplug_event "drm_kms_helper_hotplug_event").
    This callback is not called after **unregister** has been called.

    This callback is optional.

struct drm_client_dev
:   DRM client instance

**Definition**:

```
struct drm_client_dev {
    struct drm_device *dev;
    const char *name;
    struct list_head list;
    const struct drm_client_funcs *funcs;
    struct drm_file *file;
    struct mutex modeset_mutex;
    struct drm_mode_set *modesets;
    bool hotplug_failed;
};
```

**Members**

`dev`
:   DRM device

`name`
:   Name of the client.

`list`
:   List of all clients of a DRM device, linked into
    [`drm_device.clientlist`](drm-internals.md#c.drm_device "drm_device"). Protected by [`drm_device.clientlist_mutex`](drm-internals.md#c.drm_device "drm_device").

`funcs`
:   DRM client functions (optional)

`file`
:   DRM file

`modeset_mutex`
:   Protects **modesets**.

`modesets`
:   CRTC configurations

`hotplug_failed`
:   Set by client hotplug helpers if the hotplugging failed
    before. It is usually not tried again.

struct drm_client_buffer
:   DRM client buffer

**Definition**:

```
struct drm_client_buffer {
    struct drm_client_dev *client;
    u32 pitch;
    struct drm_gem_object *gem;
    struct iosys_map map;
    struct drm_framebuffer *fb;
};
```

**Members**

`client`
:   DRM client

`pitch`
:   Buffer pitch

`gem`
:   GEM object backing this buffer

`map`
:   Virtual address for the buffer

`fb`
:   DRM framebuffer

drm_client_for_each_modeset

`drm_client_for_each_modeset (modeset, client)`

> Iterate over client modesets

**Parameters**

`modeset`
:   [`drm_mode_set`](drm-kms.md#c.drm_mode_set "drm_mode_set") loop cursor

`client`
:   DRM client

drm_client_for_each_connector_iter

`drm_client_for_each_connector_iter (connector, iter)`

> connector_list iterator macro

**Parameters**

`connector`
:   [`struct drm_connector`](drm-kms.md#c.drm_connector "drm_connector") pointer used as cursor

`iter`
:   [`struct drm_connector_list_iter`](drm-kms.md#c.drm_connector_list_iter "drm_connector_list_iter")

**Description**

This iterates the connectors that are useable for internal clients (excludes
writeback connectors).

For more info see [`drm_for_each_connector_iter()`](drm-kms.md#c.drm_for_each_connector_iter "drm_for_each_connector_iter").

int drm_client_init(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev, struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client, const char \*name, const struct [drm_client_funcs](drm-client.md#c.drm_client_funcs "drm_client_funcs") \*funcs)
:   Initialise a DRM client

**Parameters**

`struct drm_device *dev`
:   DRM device

`struct drm_client_dev *client`
:   DRM client

`const char *name`
:   Client name

`const struct drm_client_funcs *funcs`
:   DRM client functions (optional)

**Description**

This initialises the client and opens a [`drm_file`](drm-internals.md#c.drm_file "drm_file").
Use [`drm_client_register()`](drm-client.md#c.drm_client_register "drm_client_register") to complete the process.
The caller needs to hold a reference on **dev** before calling this function.
The client is freed when the [`drm_device`](drm-internals.md#c.drm_device "drm_device") is unregistered. See [`drm_client_release()`](drm-client.md#c.drm_client_release "drm_client_release").

**Return**

Zero on success or negative error code on failure.

void drm_client_register(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client)
:   Register client

**Parameters**

`struct drm_client_dev *client`
:   DRM client

**Description**

Add the client to the [`drm_device`](drm-internals.md#c.drm_device "drm_device") client list to activate its callbacks.
**client** must be initialized by a call to [`drm_client_init()`](drm-client.md#c.drm_client_init "drm_client_init"). After
[`drm_client_register()`](drm-client.md#c.drm_client_register "drm_client_register") it is no longer permissible to call [`drm_client_release()`](drm-client.md#c.drm_client_release "drm_client_release")
directly (outside the unregister callback), instead cleanup will happen
automatically on driver unload.

Registering a client generates a hotplug event that allows the client
to set up its display from pre-existing outputs. The client must have
initialized its state to able to handle the hotplug event successfully.

void drm_client_release(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client)
:   Release DRM client resources

**Parameters**

`struct drm_client_dev *client`
:   DRM client

**Description**

Releases resources by closing the [`drm_file`](drm-internals.md#c.drm_file "drm_file") that was opened by [`drm_client_init()`](drm-client.md#c.drm_client_init "drm_client_init").
It is called automatically if the [`drm_client_funcs.unregister`](drm-client.md#c.drm_client_funcs "drm_client_funcs") callback is _not_ set.

This function should only be called from the unregister callback. An exception
is fbdev which cannot free the buffer if userspace has open file descriptors.

**Note**

Clients cannot initiate a release by themselves. This is done to keep the code simple.
The driver has to be unloaded before the client can be unloaded.

void drm_client_dev_hotplug(struct [drm_device](drm-internals.md#c.drm_device "drm_device") \*dev)
:   Send hotplug event to clients

**Parameters**

`struct drm_device *dev`
:   DRM device

**Description**

This function calls the [`drm_client_funcs.hotplug`](drm-client.md#c.drm_client_funcs "drm_client_funcs") callback on the attached clients.

[`drm_kms_helper_hotplug_event()`](drm-kms-helpers.md#c.drm_kms_helper_hotplug_event "drm_kms_helper_hotplug_event") calls this function, so drivers that use it
don't need to call this function themselves.

int drm_client_buffer_vmap(struct [drm_client_buffer](drm-client.md#c.drm_client_buffer "drm_client_buffer") \*buffer, struct [iosys_map](../driver-api/device-io.md#c.iosys_map "iosys_map") \*map_copy)
:   Map DRM client buffer into address space

**Parameters**

`struct drm_client_buffer *buffer`
:   DRM client buffer

`struct iosys_map *map_copy`
:   Returns the mapped memory's address

**Description**

This function maps a client buffer into kernel address space. If the
buffer is already mapped, it returns the existing mapping's address.

Client buffer mappings are not ref'counted. Each call to
[`drm_client_buffer_vmap()`](drm-client.md#c.drm_client_buffer_vmap "drm_client_buffer_vmap") should be followed by a call to
[`drm_client_buffer_vunmap()`](drm-client.md#c.drm_client_buffer_vunmap "drm_client_buffer_vunmap"); or the client buffer should be mapped
throughout its lifetime.

The returned address is a copy of the internal value. In contrast to
other vmap interfaces, you don't need it for the client's vunmap
function. So you can modify it at will during blit and draw operations.

**Return**

> 0 on success, or a negative errno code otherwise.

void drm_client_buffer_vunmap(struct [drm_client_buffer](drm-client.md#c.drm_client_buffer "drm_client_buffer") \*buffer)
:   Unmap DRM client buffer

**Parameters**

`struct drm_client_buffer *buffer`
:   DRM client buffer

**Description**

This function removes a client buffer's memory mapping. Calling this
function is only required by clients that manage their buffer mappings
by themselves.

struct [drm_client_buffer](drm-client.md#c.drm_client_buffer "drm_client_buffer") \*drm_client_framebuffer_create(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client, u32 width, u32 height, u32 format)
:   Create a client framebuffer

**Parameters**

`struct drm_client_dev *client`
:   DRM client

`u32 width`
:   Framebuffer width

`u32 height`
:   Framebuffer height

`u32 format`
:   Buffer format

**Description**

This function creates a [`drm_client_buffer`](drm-client.md#c.drm_client_buffer "drm_client_buffer") which consists of a
[`drm_framebuffer`](drm-kms.md#c.drm_framebuffer "drm_framebuffer") backed by a dumb buffer.
Call [`drm_client_framebuffer_delete()`](drm-client.md#c.drm_client_framebuffer_delete "drm_client_framebuffer_delete") to free the buffer.

**Return**

Pointer to a client buffer or an error pointer on failure.

void drm_client_framebuffer_delete(struct [drm_client_buffer](drm-client.md#c.drm_client_buffer "drm_client_buffer") \*buffer)
:   Delete a client framebuffer

**Parameters**

`struct drm_client_buffer *buffer`
:   DRM client buffer (can be NULL)

int drm_client_framebuffer_flush(struct [drm_client_buffer](drm-client.md#c.drm_client_buffer "drm_client_buffer") \*buffer, struct [drm_rect](drm-kms-helpers.md#c.drm_rect "drm_rect") \*rect)
:   Manually flush client framebuffer

**Parameters**

`struct drm_client_buffer *buffer`
:   DRM client buffer (can be NULL)

`struct drm_rect *rect`
:   Damage rectangle (if NULL flushes all)

**Description**

This calls [`drm_framebuffer_funcs->dirty`](drm-kms.md#c.drm_framebuffer_funcs "drm_framebuffer_funcs") (if present) to flush buffer changes
for drivers that need it.

**Return**

Zero on success or negative error code on failure.

int drm_client_modeset_probe(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client, unsigned int width, unsigned int height)
:   Probe for displays

**Parameters**

`struct drm_client_dev *client`
:   DRM client

`unsigned int width`
:   Maximum display mode width (optional)

`unsigned int height`
:   Maximum display mode height (optional)

**Description**

This function sets up display pipelines for enabled connectors and stores the
config in the client's modeset array.

**Return**

Zero on success or negative error code on failure.

bool drm_client_rotation(struct [drm_mode_set](drm-kms.md#c.drm_mode_set "drm_mode_set") \*modeset, unsigned int \*rotation)
:   Check the initial rotation value

**Parameters**

`struct drm_mode_set *modeset`
:   DRM modeset

`unsigned int *rotation`
:   Returned rotation value

**Description**

This function checks if the primary plane in **modeset** can hw rotate
to match the rotation needed on its connector.

**Note**

Currently only 0 and 180 degrees are supported.

**Return**

True if the plane can do the rotation, false otherwise.

int drm_client_modeset_check(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client)
:   Check modeset configuration

**Parameters**

`struct drm_client_dev *client`
:   DRM client

**Description**

Check modeset configuration.

**Return**

Zero on success or negative error code on failure.

int drm_client_modeset_commit_locked(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client)
:   Force commit CRTC configuration

**Parameters**

`struct drm_client_dev *client`
:   DRM client

**Description**

Commit modeset configuration to crtcs without checking if there is a DRM
master. The assumption is that the caller already holds an internal DRM
master reference acquired with drm_master_internal_acquire().

**Return**

Zero on success or negative error code on failure.

int drm_client_modeset_commit(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client)
:   Commit CRTC configuration

**Parameters**

`struct drm_client_dev *client`
:   DRM client

**Description**

Commit modeset configuration to crtcs.

**Return**

Zero on success or negative error code on failure.

int drm_client_modeset_dpms(struct [drm_client_dev](drm-client.md#c.drm_client_dev "drm_client_dev") \*client, int mode)
:   Set DPMS mode

**Parameters**

`struct drm_client_dev *client`
:   DRM client

`int mode`
:   DPMS mode

**Note**

For atomic drivers **mode** is reduced to on/off.

**Return**

Zero on success or negative error code on failure.
