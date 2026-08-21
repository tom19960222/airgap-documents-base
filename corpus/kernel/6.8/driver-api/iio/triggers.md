---
collection: kernel
version: "6.8"
title: "Triggers"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/iio/triggers.html
fetched_at: 2026-08-21T03:31:41+00:00
---
# Triggers

- [`struct iio_trigger`](triggers.md#c.iio_trigger "iio_trigger") — industrial I/O trigger device
- `devm_iio_trigger_alloc()` — Resource-managed iio_trigger_alloc
- [`devm_iio_trigger_register()`](triggers.md#c.devm_iio_trigger_register "devm_iio_trigger_register") — Resource-managed iio_trigger_register
  iio_trigger_unregister
- [`iio_trigger_validate_own_device()`](triggers.md#c.iio_trigger_validate_own_device "iio_trigger_validate_own_device") — Check if a trigger and IIO
  device belong to the same device

In many situations it is useful for a driver to be able to capture data based
on some external event (trigger) as opposed to periodically polling for data.
An IIO trigger can be provided by a device driver that also has an IIO device
based on hardware generated events (e.g. data ready or threshold exceeded) or
provided by a separate driver from an independent interrupt source (e.g. GPIO
line connected to some external system, timer interrupt or user space writing
a specific file in sysfs). A trigger may initiate data capture for a number of
sensors and also it may be completely unrelated to the sensor itself.

## IIO trigger sysfs interface

There are two locations in sysfs related to triggers:

- `/sys/bus/iio/devices/triggerY/*`, this file is created once an
  IIO trigger is registered with the IIO core and corresponds to trigger
  with index Y.
  Because triggers can be very different depending on type there are few
  standard attributes that we can describe here:

  - `name`, trigger name that can be later used for association with a
    device.
  - `sampling_frequency`, some timer based triggers use this attribute to
    specify the frequency for trigger calls.
- `/sys/bus/iio/devices/iio:deviceX/trigger/*`, this directory is
  created once the device supports a triggered buffer. We can associate a
  trigger with our device by writing the trigger's name in the
  `current_trigger` file.

## IIO trigger setup

Let's see a simple example of how to setup a trigger to be used by a driver:

```
struct iio_trigger_ops trigger_ops = {
    .set_trigger_state = sample_trigger_state,
    .validate_device = sample_validate_device,
}

struct iio_trigger *trig;

/* first, allocate memory for our trigger */
trig = iio_trigger_alloc(dev, "trig-%s-%d", name, idx);

/* setup trigger operations field */
trig->ops = &trigger_ops;

/* now register the trigger with the IIO core */
iio_trigger_register(trig);
```

## IIO trigger ops

- [`struct iio_trigger_ops`](triggers.md#c.iio_trigger_ops "iio_trigger_ops") — operations structure for an iio_trigger.

Notice that a trigger has a set of operations attached:

- `set_trigger_state`, switch the trigger on/off on demand.
- `validate_device`, function to validate the device when the current
  trigger gets changed.

## More details

struct iio_trigger_ops
:   operations structure for an iio_trigger.

**Definition**:

```
struct iio_trigger_ops {
    int (*set_trigger_state)(struct iio_trigger *trig, bool state);
    void (*reenable)(struct iio_trigger *trig);
    int (*validate_device)(struct iio_trigger *trig, struct iio_dev *indio_dev);
};
```

**Members**

`set_trigger_state`
:   switch on/off the trigger on demand

`reenable`
:   function to reenable the trigger when the
    use count is zero (may be NULL)

`validate_device`
:   function to validate the device when the
    current trigger gets changed.

**Description**

This is typically static const within a driver and shared by
instances of a given device.

struct iio_trigger
:   industrial I/O trigger device

**Definition**:

```
struct iio_trigger {
    const struct iio_trigger_ops    *ops;
    struct module                   *owner;
    int id;
    const char                      *name;
    struct device                   dev;
    struct list_head                list;
    struct list_head                alloc_list;
    atomic_t use_count;
    struct irq_chip                 subirq_chip;
    int subirq_base;
    struct iio_subirq subirqs[CONFIG_IIO_CONSUMERS_PER_TRIGGER];
    unsigned long pool[BITS_TO_LONGS(CONFIG_IIO_CONSUMERS_PER_TRIGGER)];
    struct mutex                    pool_lock;
    bool attached_own_device;
    struct work_struct              reenable_work;
};
```

**Members**

`ops`
:   [DRIVER] operations structure

`owner`
:   [INTERN] owner of this driver module

`id`
:   [INTERN] unique id number

`name`
:   [DRIVER] unique name

`dev`
:   [DRIVER] associated device (if relevant)

`list`
:   [INTERN] used in maintenance of global trigger list

`alloc_list`
:   [DRIVER] used for driver specific trigger list

`use_count`
:   [INTERN] use count for the trigger.

`subirq_chip`
:   [INTERN] associate 'virtual' irq chip.

`subirq_base`
:   [INTERN] base number for irqs provided by trigger.

`subirqs`
:   [INTERN] information about the 'child' irqs.

`pool`
:   [INTERN] bitmap of irqs currently in use.

`pool_lock`
:   [INTERN] protection of the irq pool.

`attached_own_device`
:   [INTERN] if we are using our own device as trigger,
    i.e. if we registered a poll function to the same
    device as the one providing the trigger.

`reenable_work`
:   [INTERN] work item used to ensure reenable can sleep.

void iio_trigger_set_drvdata(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig, void \*data)
:   Set trigger driver data

**Parameters**

`struct iio_trigger *trig`
:   IIO trigger structure

`void *data`
:   Driver specific data

**Description**

Allows to attach an arbitrary pointer to an IIO trigger, which can later be
retrieved by [`iio_trigger_get_drvdata()`](triggers.md#c.iio_trigger_get_drvdata "iio_trigger_get_drvdata").

void \*iio_trigger_get_drvdata(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig)
:   Get trigger driver data

**Parameters**

`struct iio_trigger *trig`
:   IIO trigger structure

**Description**

Returns the data previously set with [`iio_trigger_set_drvdata()`](triggers.md#c.iio_trigger_set_drvdata "iio_trigger_set_drvdata")

int iio_trigger_register(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig_info)
:   register a trigger with the IIO core

**Parameters**

`struct iio_trigger *trig_info`
:   trigger to be registered

void iio_trigger_unregister(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig_info)
:   unregister a trigger from the core

**Parameters**

`struct iio_trigger *trig_info`
:   trigger to be unregistered

int iio_trigger_set_immutable(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev, struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig)
:   set an immutable trigger on destination

**Parameters**

`struct iio_dev *indio_dev`
:   IIO device structure containing the device

`struct iio_trigger *trig`
:   trigger to assign to device

bool iio_trigger_using_own(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   tells us if we use our own HW trigger ourselves

**Parameters**

`struct iio_dev *indio_dev`
:   device to check

void iio_trigger_poll(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig)
:   Call the IRQ trigger handler of the consumers

**Parameters**

`struct iio_trigger *trig`
:   trigger which occurred

**Description**

This function should only be called from a hard IRQ context.

void iio_trigger_poll_nested(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig)
:   Call the threaded trigger handler of the consumers

**Parameters**

`struct iio_trigger *trig`
:   trigger which occurred

**Description**

This function should only be called from a kernel thread context.

struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*__iio_trigger_alloc(struct [device](../infrastructure.md#c.device "device") \*parent, struct module \*this_mod, const char \*fmt, ...)
:   Allocate a trigger

**Parameters**

`struct device *parent`
:   Device to allocate iio_trigger for

`struct module *this_mod`
:   module allocating the trigger

`const char *fmt`
:   trigger name format. If it includes format
    specifiers, the additional arguments following
    format are formatted and inserted in the resulting
    string replacing their respective specifiers.

`...`
:   variable arguments

**Return**

Pointer to allocated iio_trigger on success, NULL on failure.

struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*__devm_iio_trigger_alloc(struct [device](../infrastructure.md#c.device "device") \*parent, struct module \*this_mod, const char \*fmt, ...)
:   Resource-managed iio_trigger_alloc() Managed iio_trigger_alloc. iio_trigger allocated with this function is automatically freed on driver detach.

**Parameters**

`struct device *parent`
:   Device to allocate iio_trigger for

`struct module *this_mod`
:   module allocating the trigger

`const char *fmt`
:   trigger name format. If it includes format
    specifiers, the additional arguments following
    format are formatted and inserted in the resulting
    string replacing their respective specifiers.

`...`
:   variable arguments

**Return**

Pointer to allocated iio_trigger on success, NULL on failure.

int devm_iio_trigger_register(struct [device](../infrastructure.md#c.device "device") \*dev, struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig_info)
:   Resource-managed [`iio_trigger_register()`](triggers.md#c.iio_trigger_register "iio_trigger_register")

**Parameters**

`struct device *dev`
:   device this trigger was allocated for

`struct iio_trigger *trig_info`
:   trigger to register

**Description**

Managed [`iio_trigger_register()`](triggers.md#c.iio_trigger_register "iio_trigger_register"). The IIO trigger registered with this
function is automatically unregistered on driver detach. This function
calls [`iio_trigger_register()`](triggers.md#c.iio_trigger_register "iio_trigger_register") internally. Refer to that function for more
information.

**Return**

0 on success, negative error number on failure.

int iio_validate_own_trigger(struct [iio_dev](core.md#c.iio_dev "iio_dev") \*idev, struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig)
:   Check if a trigger and IIO device belong to the same device

**Parameters**

`struct iio_dev *idev`
:   the IIO device to check

`struct iio_trigger *trig`
:   the IIO trigger to check

**Description**

This function can be used as the validate_trigger callback for triggers that
can only be attached to their own device.

**Return**

0 if both the trigger and the IIO device belong to the same
device, -EINVAL otherwise.

int iio_trigger_validate_own_device(struct [iio_trigger](triggers.md#c.iio_trigger "iio_trigger") \*trig, struct [iio_dev](core.md#c.iio_dev "iio_dev") \*indio_dev)
:   Check if a trigger and IIO device belong to the same device

**Parameters**

`struct iio_trigger *trig`
:   The IIO trigger to check

`struct iio_dev *indio_dev`
:   the IIO device to check

**Description**

This function can be used as the validate_device callback for triggers that
can only be attached to their own device.

**Return**

0 if both the trigger and the IIO device belong to the same
device, -EINVAL otherwise.
