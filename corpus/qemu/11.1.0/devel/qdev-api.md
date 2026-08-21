---
collection: qemu
version: "11.1.0"
title: "QEMU Device (qdev) API Reference"
source_url: https://www.qemu.org/docs/master/devel/qdev-api.html
fetched_at: 2026-08-21T03:25:58+00:00
---
# QEMU Device (qdev) API Reference

**The QEMU Device API**

All modern devices should represented as a derived QOM class of
TYPE_DEVICE. The device API introduces the additional methods of
**realize** and **unrealize** to represent additional stages in a device
objects life cycle.

## Realization

Devices are constructed in two stages:

1. object instantiation via object_initialize() and
2. device realization via the [`DeviceState.realized`](qdev-api.md#c.DeviceState "DeviceState") property

The former may not fail (and must not abort or exit, since it is called
during device introspection already), and the latter may return error
information to the caller and must be re-entrant.
Trivial field initializations should go into [`TypeInfo.instance_init`](qom-api.md#c.TypeInfo "TypeInfo").
Operations depending on **props** static properties should go into **realize**.
After successful realization, setting static properties will fail.

As an interim step, the [`DeviceState.realized`](qdev-api.md#c.DeviceState "DeviceState") property can also be
set with qdev_realize(). In the future, devices will propagate this
state change to their children and along busses they expose. The
point in time will be deferred to machine creation, so that values
set in **realize** will not be introspectable beforehand. Therefore
devices must not create children during **realize**; they should
initialize them via object_initialize() in their own
[`TypeInfo.instance_init`](qom-api.md#c.TypeInfo "TypeInfo") and forward the realization events
appropriately.

Any type may override the **realize** and/or **unrealize** callbacks but needs
to call the parent type’s implementation if keeping their functionality
is desired. Refer to QOM documentation for further discussion and examples.

> **Note:**
>
> Since TYPE_DEVICE doesn’t implement **realize** and **unrealize**, types
> derived directly from it need not call their parent’s **realize** and
> **unrealize**. For other types consult the documentation and
> implementation of the respective parent types.

## Hiding a device

To hide a device, a DeviceListener function hide_device() needs to
be registered. It can be used to defer adding a device and
therefore hide it from the guest. The handler registering to this
DeviceListener can save the QOpts passed to it for re-using it
later. It must return if it wants the device to be hidden or
visible. When the handler function decides the device shall be
visible it will be added with qdev_device_add() and realized as any
other device. Otherwise qdev_device_add() will return early without
adding the device. The guest will not see a “hidden” device until
it was marked visible and qdev_device_add called again.

struct DeviceClass
:   The base class for all devices.

**Definition**:

```
struct DeviceClass {
    unsigned long categories[BITS_TO_LONGS(DEVICE_CATEGORY_MAX)];
    const char *fw_name;
    const char *desc;
    const Property *props_;
    uint16_t props_count_;
    bool user_creatable;
    bool hotpluggable;
    DeviceReset legacy_reset;
    DeviceRealize realize;
    DeviceUnrealize unrealize;
    DeviceSyncConfig sync_config;
    const VMStateDescription *vmsd;
    const char *bus_type;
};
```

**Members**

`categories`
:   device categories device belongs to

`fw_name`
:   name used to identify device to firmware interfaces

`desc`
:   human readable description of device

`props_`
:   properties associated with device, should only be
    assigned by using device_class_set_props(). The underscore
    ensures a compile-time error if someone attempts to assign
    dc->props directly.

`props_count_`
:   number of elements in **props_**; should only be
    assigned by using device_class_set_props().

`user_creatable`
:   Can user instantiate with -device / device_add?

    All devices should support instantiation with device_add, and
    this flag should not exist. But we’re not there, yet. Some
    devices fail to instantiate with cryptic error messages.
    Others instantiate, but don’t work. Exposing users to such
    behavior would be cruel; clearing this flag will protect them.
    It should never be cleared without a comment explaining why it
    is cleared.

    TODO remove once we’re there

`hotpluggable`
:   indicates if [`DeviceClass`](qdev-api.md#c.DeviceClass "DeviceClass") is hotpluggable, available
    as readonly “hotpluggable” property of [`DeviceState`](qdev-api.md#c.DeviceState "DeviceState") instance

`legacy_reset`
:   deprecated device reset method pointer

    Modern code should use the ResettableClass interface to
    implement a multi-phase reset.

    TODO: remove once every reset callback is unused

`realize`
:   Callback function invoked when the [`DeviceState`](qdev-api.md#c.DeviceState "DeviceState"):realized
    property is changed to `true`.

`unrealize`
:   Callback function invoked when the [`DeviceState`](qdev-api.md#c.DeviceState "DeviceState"):realized
    property is changed to `false`.

`sync_config`
:   Callback function invoked when QMP command device-sync-config
    is called. Should synchronize device configuration from host to guest part
    and notify the guest about the change.

`vmsd`
:   device state serialisation description for
    migration/save/restore

`bus_type`
:   bus type
    private: to qdev / bus.

struct DeviceState
:   common device state, accessed with qdev helpers

**Definition**:

```
struct DeviceState {
    char *id;
    char *canonical_path;
    bool realized;
    bool pending_deleted_event;
    int64_t pending_deleted_expires_ms;
    int hotplugged;
    bool allow_unplug_during_migration;
    BusState *parent_bus;
    NamedGPIOListHead gpios;
    NamedClockListHead clocks;
    BusStateHead child_bus;
    int num_child_bus;
    int instance_id_alias;
    int alias_required_for_version;
    ResettableState reset;
    GSList *unplug_blockers;
    MemReentrancyGuard mem_reentrancy_guard;
};
```

**Members**

`id`
:   global device id

`canonical_path`
:   canonical path of realized device in the QOM tree

`realized`
:   has device been realized?

`pending_deleted_event`
:   track pending deletion events during unplug

`pending_deleted_expires_ms`
:   optional timeout for deletion events

`hotplugged`
:   was device added after PHASE_MACHINE_READY?

`allow_unplug_during_migration`
:   can device be unplugged during migration

`parent_bus`
:   bus this device belongs to

`gpios`
:   QLIST of named GPIOs the device provides.

`clocks`
:   QLIST of named clocks the device provides.

`child_bus`
:   QLIST of child buses

`num_child_bus`
:   number of **child_bus** entries

`instance_id_alias`
:   device alias for handling legacy migration setups

`alias_required_for_version`
:   indicates **instance_id_alias** is
    needed for migration

`reset`
:   ResettableState for the device; handled by Resettable interface.

`unplug_blockers`
:   list of reasons to block unplugging of device

`mem_reentrancy_guard`
:   Is the device currently in mmio/pio/dma?

    Used to prevent re-entrancy confusing things.

**Description**

This structure should not be accessed directly. We declare it here
so that it can be embedded in individual device state structures.

struct BusState

**Definition**:

```
struct BusState {
    DeviceState *parent;
    char *name;
    HotplugHandler *hotplug_handler;
    int max_index;
    bool realized;
    bool full;
    int num_children;
    BusChildHead children;
    BusStateEntry sibling;
    ResettableState reset;
};
```

**Members**

`parent`
:   parent Device

`name`
:   name of bus

`hotplug_handler`
:   link to a hotplug handler associated with bus.

`max_index`
:   max number of child buses

`realized`
:   is the bus itself realized?

`full`
:   is the bus full?

`num_children`
:   current number of child buses

`children`
:   an RCU protected QTAILQ, thus readers must use RCU
    to access it, and writers must hold the big qemu lock

`sibling`
:   next bus

`reset`
:   ResettableState for the bus; handled by Resettable interface.

[DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*qdev_new(const char \*name)
:   Create a device on the heap

**Parameters**

`const char *name`
:   device type to create (we assert() that this type exists)

**Description**

This only allocates the memory and initializes the device state
structure, ready for the caller to set properties if they wish.
The device still needs to be realized.

**Return**

a derived DeviceState object with a reference count of 1.

[DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*qdev_try_new(const char \*name)
:   Try to create a device on the heap

**Parameters**

`const char *name`
:   device type to create

**Description**

This is like qdev_new(), except it returns `NULL` when type **name**
does not exist, rather than asserting.

**Return**

a derived DeviceState object with a reference count of 1 or
NULL if type **name** does not exist.

bool qdev_is_realized(const [DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   check if device is realized

**Parameters**

`const DeviceState *dev`
:   The device to check.

**Context**

May be called outside big qemu lock.

**Return**

true if the device has been fully constructed, false otherwise.

bool qdev_realize([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, [BusState](qdev-api.md#c.BusState "BusState") \*bus, Error \*\*errp)
:   Realize **dev**.

**Parameters**

`DeviceState *dev`
:   device to realize

`BusState *bus`
:   bus to plug it into (may be NULL)

`Error **errp`
:   pointer to error object

**Description**

“Realize” the device, i.e. perform the second phase of device
initialization.
**dev** must not be plugged into a bus already.
If **bus**, plug **dev** into **bus**. This takes a reference to **dev**.
If **dev** has no QOM parent, make one up, taking another reference.

If you created **dev** using qdev_new(), you probably want to use
qdev_realize_and_unref() instead.

**Return**

true on success, else false setting **errp** with error

bool qdev_realize_and_unref([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, [BusState](qdev-api.md#c.BusState "BusState") \*bus, Error \*\*errp)
:   Realize **dev** and drop a reference

**Parameters**

`DeviceState *dev`
:   device to realize

`BusState *bus`
:   bus to plug it into (may be NULL)

`Error **errp`
:   pointer to error object

**Description**

Realize **dev** and drop a reference.
This is like qdev_realize(), except the caller must hold a
(private) reference, which is dropped on return regardless of
success or failure. Intended use:

```
dev = qdev_new();
[...]
qdev_realize_and_unref(dev, bus, errp);
```

Now **dev** can go away without further ado.

If you are embedding the device into some other QOM device and
initialized it via some variant on object_initialize_child() then
do not use this function, because that family of functions arrange
for the only reference to the child device to be held by the parent
via the child<> property, and so the reference-count-drop done here
would be incorrect. For that use case you want qdev_realize().

**Return**

true on success, else false setting **errp** with error

void qdev_unrealize([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   Unrealize a device

**Parameters**

`DeviceState *dev`
:   device to unrealize

**Description**

This function will “unrealize” a device, which is the first phase
of correctly destroying a device that has been realized. It will:

> - unrealize any child buses by calling qbus_unrealize()
>   (this will recursively unrealize any devices on those buses)
> - call the unrealize method of **dev**

The device can then be freed by causing its reference count to go
to zero.

Warning: most devices in QEMU do not expect to be unrealized. Only
devices which are hot-unpluggable should be unrealized (as part of
the unplugging process); all other devices are expected to last for
the life of the simulation and should not be unrealized and freed.

HotplugHandler \*qdev_get_hotplug_handler([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   Get handler responsible for device wiring

**Parameters**

`DeviceState *dev`
:   the device we want the HOTPLUG_HANDLER for.

**Note**

in case **dev** has a parent bus, it will be returned as handler unless
machine handler overrides it.

**Return**

pointer to object that implements TYPE_HOTPLUG_HANDLER interface
or NULL if there aren’t any.

void qdev_add_unplug_blocker([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, Error \*reason)
:   Add an unplug blocker to a device

**Parameters**

`DeviceState *dev`
:   Device to be blocked from unplug

`Error *reason`
:   Reason for blocking

void qdev_del_unplug_blocker([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, Error \*reason)
:   Remove an unplug blocker from a device

**Parameters**

`DeviceState *dev`
:   Device to be unblocked

`Error *reason`
:   Pointer to the Error used with qdev_add_unplug_blocker.
    Used as a handle to lookup the blocker for deletion.

bool qdev_unplug_blocked([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, Error \*\*errp)
:   Confirm if a device is blocked from unplug

**Parameters**

`DeviceState *dev`
:   Device to be tested

`Error **errp`
:   The reasons why the device is blocked, if any

**Return**

true (also setting **errp**) if device is blocked from unplug,
false otherwise

type GpioPolarity
:   Polarity of a GPIO line

**Description**

GPIO lines use either positive (active-high) logic,
or negative (active-low) logic.

In active-high logic (`GPIO_POLARITY_ACTIVE_HIGH`), a pin is
active when the voltage on the pin is high (relative to ground);
whereas in active-low logic (`GPIO_POLARITY_ACTIVE_LOW`), a pin
is active when the voltage on the pin is low (or grounded).

qemu_irq qdev_get_gpio_in([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, int n)
:   Get one of a device’s anonymous input GPIO lines

**Parameters**

`DeviceState *dev`
:   Device whose GPIO we want

`int n`
:   Number of the anonymous GPIO line (which must be in range)

**Description**

Returns the qemu_irq corresponding to an anonymous input GPIO line
(which the device has set up with qdev_init_gpio_in()). The index
**n** of the GPIO line must be valid (i.e. be at least 0 and less than
the total number of anonymous input GPIOs the device has); this
function will assert() if passed an invalid index.

This function is intended to be used by board code or SoC “container”
device models to wire up the GPIO lines; usually the return value
will be passed to qdev_connect_gpio_out() or a similar function to
connect another device’s output GPIO line to this input.

For named input GPIO lines, use qdev_get_gpio_in_named().

**Return**

qemu_irq corresponding to anonymous input GPIO line

qemu_irq qdev_get_gpio_in_named([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, const char \*name, int n)
:   Get one of a device’s named input GPIO lines

**Parameters**

`DeviceState *dev`
:   Device whose GPIO we want

`const char *name`
:   Name of the input GPIO array

`int n`
:   Number of the GPIO line in that array (which must be in range)

**Description**

Returns the qemu_irq corresponding to a single input GPIO line
in a named array of input GPIO lines on a device (which the device
has set up with qdev_init_gpio_in_named()).
The **name** string must correspond to an input GPIO array which exists on
the device, and the index **n** of the GPIO line must be valid (i.e.
be at least 0 and less than the total number of input GPIOs in that
array); this function will assert() if passed an invalid name or index.

For anonymous input GPIO lines, use qdev_get_gpio_in().

**Return**

qemu_irq corresponding to named input GPIO line

void qdev_connect_gpio_out([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, int n, qemu_irq pin)
:   Connect one of a device’s anonymous output GPIO lines

**Parameters**

`DeviceState *dev`
:   Device whose GPIO to connect

`int n`
:   Number of the anonymous output GPIO line (which must be in range)

`qemu_irq pin`
:   qemu_irq to connect the output line to

**Description**

This function connects an anonymous output GPIO line on a device
up to an arbitrary qemu_irq, so that when the device asserts that
output GPIO line, the qemu_irq’s callback is invoked.
The index **n** of the GPIO line must be valid (i.e. be at least 0 and
less than the total number of anonymous output GPIOs the device has
created with qdev_init_gpio_out()); otherwise this function will assert().

Outbound GPIO lines can be connected to any qemu_irq, but the common
case is connecting them to another device’s inbound GPIO line, using
the qemu_irq returned by qdev_get_gpio_in() or qdev_get_gpio_in_named().

It is not valid to try to connect one outbound GPIO to multiple
qemu_irqs at once, or to connect multiple outbound GPIOs to the
same qemu_irq. (Warning: there is no assertion or other guard to
catch this error: the model will just not do the right thing.)
Instead, for fan-out you can use the TYPE_SPLIT_IRQ device: connect
a device’s outbound GPIO to the splitter’s input, and connect each
of the splitter’s outputs to a different device. For fan-in you
can use the TYPE_OR_IRQ device, which is a model of a logical OR
gate with multiple inputs and one output.

For named output GPIO lines, use qdev_connect_gpio_out_named().

void qdev_connect_gpio_out_named([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, const char \*name, int n, qemu_irq input_pin)
:   Connect one of a device’s named output GPIO lines

**Parameters**

`DeviceState *dev`
:   Device whose GPIO to connect

`const char *name`
:   Name of the output GPIO array

`int n`
:   Number of the output GPIO line within that array (which must be in range)

`qemu_irq input_pin`
:   qemu_irq to connect the output line to

**Description**

This function connects a single GPIO output in a named array of output
GPIO lines on a device up to an arbitrary qemu_irq, so that when the
device asserts that output GPIO line, the qemu_irq’s callback is invoked.
The **name** string must correspond to an output GPIO array which exists on
the device, and the index **n** of the GPIO line must be valid (i.e.
be at least 0 and less than the total number of output GPIOs in that
array); this function will assert() if passed an invalid name or index.

Outbound GPIO lines can be connected to any qemu_irq, but the common
case is connecting them to another device’s inbound GPIO line, using
the qemu_irq returned by qdev_get_gpio_in() or qdev_get_gpio_in_named().

It is not valid to try to connect one outbound GPIO to multiple
qemu_irqs at once, or to connect multiple outbound GPIOs to the
same qemu_irq; see qdev_connect_gpio_out() for details.

For anonymous output GPIO lines, use qdev_connect_gpio_out().

qemu_irq qdev_get_gpio_out_connector(const [DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, const char \*name, int n)
:   Get the qemu_irq connected to an output GPIO

**Parameters**

`const DeviceState *dev`
:   Device whose output GPIO we are interested in

`const char *name`
:   Name of the output GPIO array

`int n`
:   Number of the output GPIO line within that array

**Description**

Returns whatever qemu_irq is currently connected to the specified
output GPIO line of **dev**. This will be NULL if the output GPIO line
has never been wired up to the anything. Note that the qemu_irq
returned does not belong to **dev** – it will be the input GPIO or
IRQ of whichever device the board code has connected up to **dev**’s
output GPIO.

You probably don’t need to use this function – it is used only
by the platform-bus subsystem.

**Return**

qemu_irq associated with GPIO or NULL if un-wired.

qemu_irq qdev_intercept_gpio_out([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq icpt, const char \*name, int n)
:   Intercept an existing GPIO connection

**Parameters**

`DeviceState *dev`
:   Device to intercept the outbound GPIO line from

`qemu_irq icpt`
:   New qemu_irq to connect instead

`const char *name`
:   Name of the output GPIO array

`int n`
:   Number of the GPIO line in the array

**Description**

> **Note:**
>
> This function is provided only for use by the qtest testing framework
> and is not suitable for use in non-testing parts of QEMU.

This function breaks an existing connection of an outbound GPIO
line from **dev**, and replaces it with the new qemu_irq **icpt**, as if
`qdev_connect_gpio_out_named(dev, icpt, name, n)` had been called.
The previously connected qemu_irq is returned, so it can be restored
by a second call to qdev_intercept_gpio_out() if desired.

**Return**

old disconnected qemu_irq if one existed

void qdev_init_gpio_in([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq_handler handler, int n)
:   create an array of anonymous input GPIO lines

**Parameters**

`DeviceState *dev`
:   Device to create input GPIOs for

`qemu_irq_handler handler`
:   Function to call when GPIO line value is set

`int n`
:   Number of GPIO lines to create

**Description**

Devices should use functions in the qdev_init_gpio_in\* family in
their instance_init or realize methods to create any input GPIO
lines they need. There is no functional difference between
anonymous and named GPIO lines. Stylistically, named GPIOs are
preferable (easier to understand at callsites) unless a device
has exactly one uniform kind of GPIO input whose purpose is obvious.
Note that input GPIO lines can serve as ‘sinks’ for IRQ lines.

See qdev_get_gpio_in() for how code that uses such a device can get
hold of an input GPIO line to manipulate it.

void qdev_init_gpio_out([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq \*pins, int n)
:   create an array of anonymous output GPIO lines

**Parameters**

`DeviceState *dev`
:   Device to create output GPIOs for

`qemu_irq *pins`
:   Pointer to qemu_irq or qemu_irq array for the GPIO lines

`int n`
:   Number of GPIO lines to create

**Description**

Devices should use functions in the qdev_init_gpio_out\* family
in their instance_init or realize methods to create any output
GPIO lines they need. There is no functional difference between
anonymous and named GPIO lines. Stylistically, named GPIOs are
preferable (easier to understand at callsites) unless a device
has exactly one uniform kind of GPIO output whose purpose is obvious.

The **pins** argument should be a pointer to either a “qemu_irq”
(if **n** == 1) or a “qemu_irq []” array (if **n** > 1) in the device’s
state structure. The device implementation can then raise and
lower the GPIO line by calling qemu_set_irq(). (If anything is
connected to the other end of the GPIO this will cause the handler
function for that input GPIO to be called.)

See qdev_connect_gpio_out() for how code that uses such a device
can connect to one of its output GPIO lines.

There is no need to release the **pins** allocated array because it
will be automatically released when **dev** calls its instance_finalize()
handler.

void qdev_init_gpio_out_named([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq \*pins, const char \*name, int n)
:   create an array of named output GPIO lines

**Parameters**

`DeviceState *dev`
:   Device to create output GPIOs for

`qemu_irq *pins`
:   Pointer to qemu_irq or qemu_irq array for the GPIO lines

`const char *name`
:   Name to give this array of GPIO lines

`int n`
:   Number of GPIO lines to create in this array

**Description**

Like qdev_init_gpio_out(), but creates an array of GPIO output lines
with a name. Code using the device can then connect these GPIO lines
using qdev_connect_gpio_out_named().

void qdev_init_gpio_in_named_with_opaque([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq_handler handler, void \*opaque, const char \*name, int n)
:   create an array of input GPIO lines

**Parameters**

`DeviceState *dev`
:   Device to create input GPIOs for

`qemu_irq_handler handler`
:   Function to call when GPIO line value is set

`void *opaque`
:   Opaque data pointer to pass to **handler**

`const char *name`
:   Name of the GPIO input (must be unique for this device)

`int n`
:   Number of GPIO lines in this input set

void qdev_init_gpio_in_named([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, qemu_irq_handler handler, const char \*name, int n)
:   create an array of input GPIO lines

**Parameters**

`DeviceState *dev`
:   device to add array to

`qemu_irq_handler handler`
:   a &typedef qemu_irq_handler function to call when GPIO is set

`const char *name`
:   Name of the GPIO input (must be unique for this device)

`int n`
:   Number of GPIO lines in this input set

**Description**

Like qdev_init_gpio_in_named_with_opaque(), but the opaque pointer
passed to the handler is **dev** (which is the most commonly desired behaviour).

void qdev_pass_gpios([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev, [DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*container, const char \*name)
:   create GPIO lines on container which pass through to device

**Parameters**

`DeviceState *dev`
:   Device which has GPIO lines

`DeviceState *container`
:   Container device which needs to expose them

`const char *name`
:   Name of GPIO array to pass through (NULL for the anonymous GPIO array)

**Description**

In QEMU, complicated devices like SoCs are often modelled with a
“container” QOM device which itself contains other QOM devices and
which wires them up appropriately. This function allows the container
to create GPIO arrays on itself which simply pass through to a GPIO
array of one of its internal devices.

If **dev** has both input and output GPIOs named **name** then both will
be passed through. It is not possible to pass a subset of the array
with this function.

To users of the container device, the GPIO array created on **container**
behaves exactly like any other.

void device_cold_reset([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   perform a recursive cold reset on a device

**Parameters**

`DeviceState *dev`
:   device to reset.

**Description**

Reset device **dev** and perform a recursive processing using the resettable
interface. It triggers a RESET_TYPE_COLD.

void bus_cold_reset([BusState](qdev-api.md#c.BusState "BusState") \*bus)
:   perform a recursive cold reset on a bus

**Parameters**

`BusState *bus`
:   bus to reset

**Description**

Reset bus **bus** and perform a recursive processing using the resettable
interface. It triggers a RESET_TYPE_COLD.

bool device_is_in_reset([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   check device reset state

**Parameters**

`DeviceState *dev`
:   device to check

**Return**

true if the device **dev** is currently being reset.

bool bus_is_in_reset([BusState](qdev-api.md#c.BusState "BusState") \*bus)
:   check bus reset state

**Parameters**

`BusState *bus`
:   bus to check

**Return**

true if the bus **bus** is currently being reset.

device_class_set_props

`device_class_set_props (dc, props)`

> add a set of properties to an device

**Parameters**

`dc`
:   the parent DeviceClass all devices inherit

`props`
:   an array of properties

**Description**

This will add a set of properties to the object. It will fault if
you attempt to add an existing property defined by a parent class.
To modify an inherited property you need to use????

Validate that **props** has at least one Property.
Validate that **props** is an array, not a pointer, via ARRAY_SIZE.
Validate that the array does not have a legacy terminator at compile-time;
requires -O2 and the array to be const.

void device_class_set_props_n([DeviceClass](qdev-api.md#c.DeviceClass "DeviceClass") \*dc, const Property \*props, size_t n)
:   add a set of properties to an device

**Parameters**

`DeviceClass *dc`
:   the parent DeviceClass all devices inherit

`const Property *props`
:   an array of properties

`size_t n`
:   ARRAY_SIZE(**props**)

**Description**

This will add a set of properties to the object. It will fault if
you attempt to add an existing property defined by a parent class.
To modify an inherited property you need to use????

void device_class_set_parent_realize([DeviceClass](qdev-api.md#c.DeviceClass "DeviceClass") \*dc, DeviceRealize dev_realize, DeviceRealize \*parent_realize)
:   set up for chaining realize fns

**Parameters**

`DeviceClass *dc`
:   The device class

`DeviceRealize dev_realize`
:   the device realize function

`DeviceRealize *parent_realize`
:   somewhere to save the parents realize function

**Description**

This is intended to be used when the new realize function will
eventually call its parent realization function during creation.
This requires storing the function call somewhere (usually in the
instance structure) so you can eventually call
dc->parent_realize(dev, errp)

void device_class_set_legacy_reset([DeviceClass](qdev-api.md#c.DeviceClass "DeviceClass") \*dc, DeviceReset dev_reset)
:   set the DeviceClass::reset method

**Parameters**

`DeviceClass *dc`
:   The device class

`DeviceReset dev_reset`
:   the reset function

**Description**

This function sets the DeviceClass::reset method. This is widely
used in existing code, but new code should prefer to use the
Resettable API as documented in docs/devel/reset.rst.
In addition, devices which need to chain to their parent class’s
reset methods or which need to be subclassed must use Resettable.

void device_class_set_parent_unrealize([DeviceClass](qdev-api.md#c.DeviceClass "DeviceClass") \*dc, DeviceUnrealize dev_unrealize, DeviceUnrealize \*parent_unrealize)
:   set up for chaining unrealize fns

**Parameters**

`DeviceClass *dc`
:   The device class

`DeviceUnrealize dev_unrealize`
:   the device realize function

`DeviceUnrealize *parent_unrealize`
:   somewhere to save the parents unrealize function

**Description**

This is intended to be used when the new unrealize function will
eventually call its parent unrealization function during the
unrealize phase. This requires storing the function call somewhere
(usually in the instance structure) so you can eventually call
dc->parent_unrealize(dev);

void qdev_create_fake_machine(void)
:   Create a fake machine container.

**Parameters**

`void`
:   no arguments

**Description**

> **Note:**
>
> This function is a kludge for user emulation (USER_ONLY)
> because when thread (TYPE_CPU) are realized, qdev_realize()
> access a machine container.

[Object](qom-api.md#c.Object "Object") \*machine_get_container(const char \*name)

**Parameters**

`const char *name`
:   The name of container to lookup

**Description**

Get a container of the machine (QOM path “/machine/NAME”).

**Return**

the machine container object.

char \*qdev_get_human_name([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   Return a human-readable name for a device

**Parameters**

`DeviceState *dev`
:   The device. Must be a valid and non-NULL pointer.

**Return**

A newly allocated string suitable for user-facing error
messages.

**Description**

Return the device’s ID if it has one. Else, return the path of a
device on its bus if it has one. Else return its canonical QOM
path.

char \*qdev_get_dev_path([DeviceState](qdev-api.md#c.DeviceState "DeviceState") \*dev)
:   Return the path of a device on its bus

**Parameters**

`DeviceState *dev`
:   device to get the path of

**Return**

A newly allocated string containing the dev path of
**dev**. The caller must free this with g_free().
The format of the string depends on the bus; for instance a
PCI device’s path will be in the format:

```
**Description**
```

> Domain:00:Slot.Function:Slot.Function….:Slot.Function

and a SCSI device’s path will be:

```
channel:ID:LUN
```

(possibly prefixed by the path of the SCSI controller).

If **dev** is NULL or not on a bus, returns NULL.

void qbus_mark_full([BusState](qdev-api.md#c.BusState "BusState") \*bus)
:   Mark this bus as full, so no more devices can be attached

**Parameters**

`BusState *bus`
:   Bus to mark as full

**Description**

By default, QEMU will allow devices to be plugged into a bus up
to the bus class’s device count limit. Calling this function
marks a particular bus as full, so that no more devices can be
plugged into it. In particular this means that the bus will not
be considered as a candidate for plugging in devices created by
the user on the commandline or via the monitor.
If a machine has multiple buses of a given type, such as I2C,
where some of those buses in the real hardware are used only for
internal devices and some are exposed via expansion ports, you
can use this function to mark the internal-only buses as full
after you have created all their internal devices. Then user
created devices will appear on the expansion-port bus where
guest software expects them.

bool qdev_should_hide_device(const QDict \*opts, bool from_json, Error \*\*errp)
:   check if device should be hidden

**Parameters**

`const QDict *opts`
:   options QDict

`bool from_json`
:   true if **opts** entries are typed, false for all strings

`Error **errp`
:   pointer to error object

**Description**

When a device is added via qdev_device_add() this will be called.

**Return**

if the device should be added now or not.
