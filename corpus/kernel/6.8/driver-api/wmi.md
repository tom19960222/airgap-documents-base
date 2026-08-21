---
collection: kernel
version: "6.8"
title: "WMI Driver API"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/wmi.html
fetched_at: 2026-08-21T03:31:27+00:00
---
# WMI Driver API

The WMI driver core supports a more modern bus-based interface for interacting
with WMI devices, and an older GUID-based interface. The latter interface is
considered to be deprecated, so new WMI drivers should generally avoid it since
it has some issues with multiple WMI devices and events sharing the same GUIDs
and/or notification IDs. The modern bus-based interface instead maps each
WMI device to a [`struct wmi_device`](wmi.md#c.wmi_device "wmi_device"), so it supports
WMI devices sharing GUIDs and/or notification IDs. Drivers can then register
a [`struct wmi_driver`](wmi.md#c.wmi_driver "wmi_driver"), which will be bound to compatible
WMI devices by the driver core.

struct wmi_device
:   WMI device structure

**Definition**:

```
struct wmi_device {
    struct device dev;
    bool setable;
};
```

**Members**

`dev`
:   Device associated with this WMI device

`setable`
:   True for devices implementing the Set Control Method

**Description**

This represents WMI devices discovered by the WMI driver core.

to_wmi_device

`to_wmi_device (device)`

> Helper macro to cast a device to a wmi_device

**Parameters**

`device`
:   device struct

**Description**

Cast a [`struct device`](infrastructure.md#c.device "device") to a [`struct wmi_device`](wmi.md#c.wmi_device "wmi_device").

struct wmi_driver
:   WMI driver structure

**Definition**:

```
struct wmi_driver {
    struct device_driver driver;
    const struct wmi_device_id *id_table;
    bool no_notify_data;
    int (*probe)(struct wmi_device *wdev, const void *context);
    void (*remove)(struct wmi_device *wdev);
    void (*notify)(struct wmi_device *device, union acpi_object *data);
};
```

**Members**

`driver`
:   Driver model structure

`id_table`
:   List of WMI GUIDs supported by this driver

`no_notify_data`
:   WMI events provide no event data

`probe`
:   Callback for device binding

`remove`
:   Callback for device unbinding

`notify`
:   Callback for receiving WMI events

**Description**

This represents WMI drivers which handle WMI devices.

wmi_driver_register

`wmi_driver_register (driver)`

> Helper macro to register a WMI driver

**Parameters**

`driver`
:   wmi_driver struct

**Description**

Helper macro for registering a WMI driver. It automatically passes
THIS_MODULE to the underlying function.

module_wmi_driver

`module_wmi_driver (__wmi_driver)`

> Helper macro to register/unregister a WMI driver

**Parameters**

`__wmi_driver`
:   wmi_driver struct

**Description**

Helper macro for WMI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces [`module_init()`](basics.md#c.module_init "module_init") and [`module_exit()`](basics.md#c.module_exit "module_exit").

int wmi_instance_count(const char \*guid_string)
:   Get number of WMI object instances

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

**Description**

Get the number of WMI object instances.

**Return**

Number of WMI object instances or negative error code.

u8 wmidev_instance_count(struct [wmi_device](wmi.md#c.wmi_device "wmi_device") \*wdev)
:   Get number of WMI object instances

**Parameters**

`struct wmi_device *wdev`
:   A wmi bus device from a driver

**Description**

Get the number of WMI object instances.

**Return**

Number of WMI object instances.

acpi_status wmi_evaluate_method(const char \*guid_string, u8 instance, u32 method_id, const struct acpi_buffer \*in, struct acpi_buffer \*out)
:   Evaluate a WMI method (deprecated)

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

`u8 instance`
:   Instance index

`u32 method_id`
:   Method ID to call

`const struct acpi_buffer *in`
:   Buffer containing input for the method call

`struct acpi_buffer *out`
:   Empty buffer to return the method results

**Description**

Call an ACPI-WMI method, the caller must free **out**.

**Return**

acpi_status signaling success or error.

acpi_status wmidev_evaluate_method(struct [wmi_device](wmi.md#c.wmi_device "wmi_device") \*wdev, u8 instance, u32 method_id, const struct acpi_buffer \*in, struct acpi_buffer \*out)
:   Evaluate a WMI method

**Parameters**

`struct wmi_device *wdev`
:   A wmi bus device from a driver

`u8 instance`
:   Instance index

`u32 method_id`
:   Method ID to call

`const struct acpi_buffer *in`
:   Buffer containing input for the method call

`struct acpi_buffer *out`
:   Empty buffer to return the method results

**Description**

Call an ACPI-WMI method, the caller must free **out**.

**Return**

acpi_status signaling success or error.

acpi_status wmi_query_block(const char \*guid_string, u8 instance, struct acpi_buffer \*out)
:   Return contents of a WMI block (deprecated)

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

`u8 instance`
:   Instance index

`struct acpi_buffer *out`
:   Empty buffer to return the contents of the data block to

**Description**

Query a ACPI-WMI block, the caller must free **out**.

**Return**

ACPI object containing the content of the WMI block.

union acpi_object \*wmidev_block_query(struct [wmi_device](wmi.md#c.wmi_device "wmi_device") \*wdev, u8 instance)
:   Return contents of a WMI block

**Parameters**

`struct wmi_device *wdev`
:   A wmi bus device from a driver

`u8 instance`
:   Instance index

**Description**

Query an ACPI-WMI block, the caller must free the result.

**Return**

ACPI object containing the content of the WMI block.

acpi_status wmi_set_block(const char \*guid_string, u8 instance, const struct acpi_buffer \*in)
:   Write to a WMI block (deprecated)

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

`u8 instance`
:   Instance index

`const struct acpi_buffer *in`
:   Buffer containing new values for the data block

**Description**

Write the contents of the input buffer to an ACPI-WMI data block.

**Return**

acpi_status signaling success or error.

acpi_status wmidev_block_set(struct [wmi_device](wmi.md#c.wmi_device "wmi_device") \*wdev, u8 instance, const struct acpi_buffer \*in)
:   Write to a WMI block

**Parameters**

`struct wmi_device *wdev`
:   A wmi bus device from a driver

`u8 instance`
:   Instance index

`const struct acpi_buffer *in`
:   Buffer containing new values for the data block

**Description**

Write contents of the input buffer to an ACPI-WMI data block.

**Return**

acpi_status signaling success or error.

acpi_status wmi_install_notify_handler(const char \*guid, wmi_notify_handler handler, void \*data)
:   Register handler for WMI events (deprecated)

**Parameters**

`const char *guid`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

`wmi_notify_handler handler`
:   Function to handle notifications

`void *data`
:   Data to be returned to handler when event is fired

**Description**

Register a handler for events sent to the ACPI-WMI mapper device.

**Return**

acpi_status signaling success or error.

acpi_status wmi_remove_notify_handler(const char \*guid)
:   Unregister handler for WMI events (deprecated)

**Parameters**

`const char *guid`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

**Description**

Unregister handler for events sent to the ACPI-WMI mapper device.

**Return**

acpi_status signaling success or error.

acpi_status wmi_get_event_data(u32 event, struct acpi_buffer \*out)
:   Get WMI data associated with an event (deprecated)

**Parameters**

`u32 event`
:   Event to find

`struct acpi_buffer *out`
:   Buffer to hold event data

**Description**

Get extra data associated with an WMI event, the caller needs to free **out**.

**Return**

acpi_status signaling success or error.

bool wmi_has_guid(const char \*guid_string)
:   Check if a GUID is available

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

**Description**

Check if a given GUID is defined by _WDG.

**Return**

True if GUID is available, false otherwise.

char \*wmi_get_acpi_device_uid(const char \*guid_string)
:   Get _UID name of ACPI device that defines GUID (deprecated)

**Parameters**

`const char *guid_string`
:   36 char string of the form fa50ff2b-f2e8-45de-83fa-65417f2f49ba

**Description**

Find the _UID of ACPI device associated with this WMI GUID.

**Return**

The ACPI _UID field value or NULL if the WMI GUID was not found.

void wmi_driver_unregister(struct [wmi_driver](wmi.md#c.wmi_driver "wmi_driver") \*driver)
:   Unregister a WMI driver

**Parameters**

`struct wmi_driver *driver`
:   WMI driver to unregister

**Description**

Unregisters a WMI driver from the WMI bus.
