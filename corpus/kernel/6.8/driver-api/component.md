---
collection: kernel
version: "6.8"
title: "Component Helper for Aggregate Drivers"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/component.html
fetched_at: 2026-08-21T03:30:34+00:00
---
# Component Helper for Aggregate Drivers

The component helper allows drivers to collect a pile of sub-devices,
including their bound drivers, into an aggregate driver. Various subsystems
already provide functions to get hold of such components, e.g.
of_clk_get_by_name(). The component helper can be used when such a
subsystem-specific way to find a device is not available: The component
helper fills the niche of aggregate drivers for specific hardware, where
further standardization into a subsystem would not be practical. The common
example is when a logical device (e.g. a DRM display driver) is spread around
the SoC on various components (scanout engines, blending blocks, transcoders
for various outputs and so on).

The component helper also doesn't solve runtime dependencies, e.g. for system
suspend and resume operations. See also [device links](device_link.md#device-link).

Components are registered using [`component_add()`](component.md#c.component_add "component_add") and unregistered with
[`component_del()`](component.md#c.component_del "component_del"), usually from the driver's probe and disconnect functions.

Aggregate drivers first assemble a component match list of what they need
using [`component_match_add()`](component.md#c.component_match_add "component_match_add"). This is then registered as an aggregate driver
using [`component_master_add_with_match()`](component.md#c.component_master_add_with_match "component_master_add_with_match"), and unregistered using
[`component_master_del()`](component.md#c.component_master_del "component_master_del").

## API

struct component_ops
:   callbacks for component drivers

**Definition**:

```
struct component_ops {
    int (*bind)(struct device *comp, struct device *master, void *master_data);
    void (*unbind)(struct device *comp, struct device *master, void *master_data);
};
```

**Members**

`bind`
:   Called through [`component_bind_all()`](component.md#c.component_bind_all "component_bind_all") when the aggregate driver is
    ready to bind the overall driver.

`unbind`
:   Called through [`component_unbind_all()`](component.md#c.component_unbind_all "component_unbind_all") when the aggregate driver is
    ready to bind the overall driver, or when [`component_bind_all()`](component.md#c.component_bind_all "component_bind_all") fails
    part-ways through and needs to unbind some already bound components.

**Description**

Components are registered with [`component_add()`](component.md#c.component_add "component_add") and unregistered with
[`component_del()`](component.md#c.component_del "component_del").

struct component_master_ops
:   callback for the aggregate driver

**Definition**:

```
struct component_master_ops {
    int (*bind)(struct device *master);
    void (*unbind)(struct device *master);
};
```

**Members**

`bind`
:   Called when all components or the aggregate driver, as specified in
    the match list passed to [`component_master_add_with_match()`](component.md#c.component_master_add_with_match "component_master_add_with_match"), are
    ready. Usually there are 3 steps to bind an aggregate driver:

    1. Allocate a structure for the aggregate driver.
    2. Bind all components to the aggregate driver by calling
       [`component_bind_all()`](component.md#c.component_bind_all "component_bind_all") with the aggregate driver structure as opaque
       pointer data.
    3. Register the aggregate driver with the subsystem to publish its
       interfaces.

    Note that the lifetime of the aggregate driver does not align with
    any of the underlying [`struct device`](infrastructure.md#c.device "device") instances. Therefore devm cannot
    be used and all resources acquired or allocated in this callback must
    be explicitly released in the **unbind** callback.

`unbind`
:   Called when either the aggregate driver, using
    [`component_master_del()`](component.md#c.component_master_del "component_master_del"), or one of its components, using
    [`component_del()`](component.md#c.component_del "component_del"), is unregistered.

**Description**

Aggregate drivers are registered with [`component_master_add_with_match()`](component.md#c.component_master_add_with_match "component_master_add_with_match") and
unregistered with [`component_master_del()`](component.md#c.component_master_del "component_master_del").

void component_match_add(struct [device](infrastructure.md#c.device "device") \*parent, struct component_match \*\*matchptr, int (\*compare)(struct [device](infrastructure.md#c.device "device")\*, void\*), void \*compare_data)
:   add a component match entry

**Parameters**

`struct device *parent`
:   device with the aggregate driver

`struct component_match **matchptr`
:   pointer to the list of component matches

`int (*compare)(struct device *, void *)`
:   compare function to match against all components

`void *compare_data`
:   opaque pointer passed to the **compare** function

**Description**

Adds a new component match to the list stored in **matchptr**, which the **parent**
aggregate driver needs to function. The list of component matches pointed to
by **matchptr** must be initialized to NULL before adding the first match. This
only matches against components added with [`component_add()`](component.md#c.component_add "component_add").

The allocated match list in **matchptr** is automatically released using devm
actions.

See also [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release") and [`component_match_add_typed()`](component.md#c.component_match_add_typed "component_match_add_typed").

int component_compare_of(struct [device](infrastructure.md#c.device "device") \*dev, void \*data)
:   A common component compare function for of_node

**Parameters**

`struct device *dev`
:   component device

`void *data`
:   **compare_data** from [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release")

**Description**

A common compare function when compare_data is device of_node. e.g.
component_match_add_release(masterdev, `match`, component_release_of,
component_compare_of, component_dev_of_node)

void component_release_of(struct [device](infrastructure.md#c.device "device") \*dev, void \*data)
:   A common component release function for of_node

**Parameters**

`struct device *dev`
:   component device

`void *data`
:   **compare_data** from [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release")

**Description**

About the example, Please see [`component_compare_of()`](component.md#c.component_compare_of "component_compare_of").

int component_compare_dev(struct [device](infrastructure.md#c.device "device") \*dev, void \*data)
:   A common component compare function for dev

**Parameters**

`struct device *dev`
:   component device

`void *data`
:   **compare_data** from [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release")

**Description**

A common compare function when compare_data is struce device. e.g.
component_match_add(masterdev, `match`, component_compare_dev, component_dev)

int component_compare_dev_name(struct [device](infrastructure.md#c.device "device") \*dev, void \*data)
:   A common component compare function for device name

**Parameters**

`struct device *dev`
:   component device

`void *data`
:   **compare_data** from [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release")

**Description**

A common compare function when compare_data is device name string. e.g.
component_match_add(masterdev, `match`, component_compare_dev_name,
"component_dev_name")

void component_match_add_release(struct [device](infrastructure.md#c.device "device") \*parent, struct component_match \*\*matchptr, void (\*release)(struct [device](infrastructure.md#c.device "device")\*, void\*), int (\*compare)(struct [device](infrastructure.md#c.device "device")\*, void\*), void \*compare_data)
:   add a component match entry with release callback

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`struct component_match **matchptr`
:   pointer to the list of component matches

`void (*release)(struct device *, void *)`
:   release function for **compare_data**

`int (*compare)(struct device *, void *)`
:   compare function to match against all components

`void *compare_data`
:   opaque pointer passed to the **compare** function

**Description**

Adds a new component match to the list stored in **matchptr**, which the
aggregate driver needs to function. The list of component matches pointed to
by **matchptr** must be initialized to NULL before adding the first match. This
only matches against components added with [`component_add()`](component.md#c.component_add "component_add").

The allocated match list in **matchptr** is automatically released using devm
actions, where upon **release** will be called to free any references held by
**compare_data**, e.g. when **compare_data** is a `device_node` that must be
released with [`of_node_put()`](../devicetree/kernel-api.md#c.of_node_put "of_node_put").

See also [`component_match_add()`](component.md#c.component_match_add "component_match_add") and [`component_match_add_typed()`](component.md#c.component_match_add_typed "component_match_add_typed").

void component_match_add_typed(struct [device](infrastructure.md#c.device "device") \*parent, struct component_match \*\*matchptr, int (\*compare_typed)(struct [device](infrastructure.md#c.device "device")\*, int, void\*), void \*compare_data)
:   add a component match entry for a typed component

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`struct component_match **matchptr`
:   pointer to the list of component matches

`int (*compare_typed)(struct device *, int, void *)`
:   compare function to match against all typed components

`void *compare_data`
:   opaque pointer passed to the **compare** function

**Description**

Adds a new component match to the list stored in **matchptr**, which the
aggregate driver needs to function. The list of component matches pointed to
by **matchptr** must be initialized to NULL before adding the first match. This
only matches against components added with [`component_add_typed()`](component.md#c.component_add_typed "component_add_typed").

The allocated match list in **matchptr** is automatically released using devm
actions.

See also [`component_match_add_release()`](component.md#c.component_match_add_release "component_match_add_release") and [`component_match_add_typed()`](component.md#c.component_match_add_typed "component_match_add_typed").

int component_master_add_with_match(struct [device](infrastructure.md#c.device "device") \*parent, const struct [component_master_ops](component.md#c.component_master_ops "component_master_ops") \*ops, struct component_match \*match)
:   register an aggregate driver

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`const struct component_master_ops *ops`
:   callbacks for the aggregate driver

`struct component_match *match`
:   component match list for the aggregate driver

**Description**

Registers a new aggregate driver consisting of the components added to **match**
by calling one of the [`component_match_add()`](component.md#c.component_match_add "component_match_add") functions. Once all components in
**match** are available, it will be assembled by calling
[`component_master_ops.bind`](component.md#c.component_master_ops "component_master_ops") from **ops**. Must be unregistered by calling
[`component_master_del()`](component.md#c.component_master_del "component_master_del").

void component_master_del(struct [device](infrastructure.md#c.device "device") \*parent, const struct [component_master_ops](component.md#c.component_master_ops "component_master_ops") \*ops)
:   unregister an aggregate driver

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`const struct component_master_ops *ops`
:   callbacks for the aggregate driver

**Description**

Unregisters an aggregate driver registered with
[`component_master_add_with_match()`](component.md#c.component_master_add_with_match "component_master_add_with_match"). If necessary the aggregate driver is first
disassembled by calling [`component_master_ops.unbind`](component.md#c.component_master_ops "component_master_ops") from **ops**.

void component_unbind_all(struct [device](infrastructure.md#c.device "device") \*parent, void \*data)
:   unbind all components of an aggregate driver

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`void *data`
:   opaque pointer, passed to all components

**Description**

Unbinds all components of the aggregate device by passing **data** to their
[`component_ops.unbind`](component.md#c.component_ops "component_ops") functions. Should be called from
[`component_master_ops.unbind`](component.md#c.component_master_ops "component_master_ops").

int component_bind_all(struct [device](infrastructure.md#c.device "device") \*parent, void \*data)
:   bind all components of an aggregate driver

**Parameters**

`struct device *parent`
:   parent device of the aggregate driver

`void *data`
:   opaque pointer, passed to all components

**Description**

Binds all components of the aggregate **dev** by passing **data** to their
[`component_ops.bind`](component.md#c.component_ops "component_ops") functions. Should be called from
[`component_master_ops.bind`](component.md#c.component_master_ops "component_master_ops").

int component_add_typed(struct [device](infrastructure.md#c.device "device") \*dev, const struct [component_ops](component.md#c.component_ops "component_ops") \*ops, int subcomponent)
:   register a component

**Parameters**

`struct device *dev`
:   component device

`const struct component_ops *ops`
:   component callbacks

`int subcomponent`
:   nonzero identifier for subcomponents

**Description**

Register a new component for **dev**. Functions in **ops** will be call when the
aggregate driver is ready to bind the overall driver by calling
[`component_bind_all()`](component.md#c.component_bind_all "component_bind_all"). See also [`struct component_ops`](component.md#c.component_ops "component_ops").

**subcomponent** must be nonzero and is used to differentiate between multiple
components registerd on the same device **dev**. These components are match
using [`component_match_add_typed()`](component.md#c.component_match_add_typed "component_match_add_typed").

The component needs to be unregistered at driver unload/disconnect by
calling [`component_del()`](component.md#c.component_del "component_del").

See also [`component_add()`](component.md#c.component_add "component_add").

int component_add(struct [device](infrastructure.md#c.device "device") \*dev, const struct [component_ops](component.md#c.component_ops "component_ops") \*ops)
:   register a component

**Parameters**

`struct device *dev`
:   component device

`const struct component_ops *ops`
:   component callbacks

**Description**

Register a new component for **dev**. Functions in **ops** will be called when the
aggregate driver is ready to bind the overall driver by calling
[`component_bind_all()`](component.md#c.component_bind_all "component_bind_all"). See also [`struct component_ops`](component.md#c.component_ops "component_ops").

The component needs to be unregistered at driver unload/disconnect by
calling [`component_del()`](component.md#c.component_del "component_del").

See also [`component_add_typed()`](component.md#c.component_add_typed "component_add_typed") for a variant that allows multipled different
components on the same device.

void component_del(struct [device](infrastructure.md#c.device "device") \*dev, const struct [component_ops](component.md#c.component_ops "component_ops") \*ops)
:   unregister a component

**Parameters**

`struct device *dev`
:   component device

`const struct component_ops *ops`
:   component callbacks

**Description**

Unregister a component added with [`component_add()`](component.md#c.component_add "component_add"). If the component is bound
into an aggregate driver, this will force the entire aggregate driver, including
all its components, to be unbound.
