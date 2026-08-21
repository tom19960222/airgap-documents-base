---
collection: kernel
version: "6.8"
title: "Surface ACPI Notify"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/surface_aggregator/clients/san.html
fetched_at: 2026-08-21T03:40:17+00:00
---
# Surface ACPI Notify

The Surface ACPI Notify (SAN) device provides the bridge between ACPI and
SAM controller. Specifically, ACPI code can execute requests and handle
battery and thermal events via this interface. In addition to this, events
relating to the discrete GPU (dGPU) of the Surface Book 2 can be sent from
ACPI code (note: the Surface Book 3 uses a different method for this). The
only currently known event sent via this interface is a dGPU power-on
notification. While this driver handles the former part internally, it only
relays the dGPU events to any other driver interested via its public API and
does not handle them.

The public interface of this driver is split into two parts: Client
registration and notifier-block registration.

A client to the SAN interface can be linked as consumer to the SAN device
via [`san_client_link()`](san.md#c.san_client_link "san_client_link"). This can be used to ensure that the a client
receiving dGPU events does not miss any events due to the SAN interface not
being set up as this forces the client driver to unbind once the SAN driver
is unbound.

Notifier-blocks can be registered by any device for as long as the module is
loaded, regardless of being linked as client or not. Registration is done
with [`san_dgpu_notifier_register()`](san.md#c.san_dgpu_notifier_register "san_dgpu_notifier_register"). If the notifier is not needed any more, it
should be unregistered via [`san_dgpu_notifier_unregister()`](san.md#c.san_dgpu_notifier_unregister "san_dgpu_notifier_unregister").

Consult the API documentation below for more details.

## API Documentation

struct san_dgpu_event
:   Discrete GPU ACPI event.

**Definition**:

```
struct san_dgpu_event {
    u8 category;
    u8 target;
    u8 command;
    u8 instance;
    u16 length;
    u8 *payload;
};
```

**Members**

`category`
:   Category of the event.

`target`
:   Target ID of the event source.

`command`
:   Command ID of the event.

`instance`
:   Instance ID of the event source.

`length`
:   Length of the event's payload data (in bytes).

`payload`
:   Pointer to the event's payload data.

int san_client_link(struct [device](../../infrastructure.md#c.device "device") \*client)
:   Link client as consumer to SAN device.

**Parameters**

`struct device *client`
:   The client to link.

**Description**

Sets up a device link between the provided client device as consumer and
the SAN device as provider. This function can be used to ensure that the
SAN interface has been set up and will be set up for as long as the driver
of the client device is bound. This guarantees that, during that time, all
dGPU events will be received by any registered notifier.

The link will be automatically removed once the client device's driver is
unbound.

**Return**

Returns zero on success, `-ENXIO` if the SAN interface has not been
set up yet, and `-ENOMEM` if device link creation failed.

int san_dgpu_notifier_register(struct notifier_block \*nb)
:   Register a SAN dGPU notifier.

**Parameters**

`struct notifier_block *nb`
:   The notifier-block to register.

**Description**

Registers a SAN dGPU notifier, receiving any new SAN dGPU events sent from
ACPI. The registered notifier will be called with [`struct san_dgpu_event`](san.md#c.san_dgpu_event "san_dgpu_event")
as notifier data and the command ID of that event as notifier action.

int san_dgpu_notifier_unregister(struct notifier_block \*nb)
:   Unregister a SAN dGPU notifier.

**Parameters**

`struct notifier_block *nb`
:   The notifier-block to unregister.
