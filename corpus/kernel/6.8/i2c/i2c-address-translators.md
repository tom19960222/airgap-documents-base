---
collection: kernel
version: "6.8"
title: "I2C Address Translators"
source_url: https://www.kernel.org/doc/html/v6.8/i2c/i2c-address-translators.html
fetched_at: 2026-08-21T03:39:47+00:00
---
# I2C Address Translators

Author: Luca Ceresoli <[luca@lucaceresoli.net](mailto:luca%40lucaceresoli.net)>
Author: Tomi Valkeinen <[tomi.valkeinen@ideasonboard.com](mailto:tomi.valkeinen%40ideasonboard.com)>

## Description

An I2C Address Translator (ATR) is a device with an I2C slave parent
("upstream") port and N I2C master child ("downstream") ports, and
forwards transactions from upstream to the appropriate downstream port
with a modified slave address. The address used on the parent bus is
called the "alias" and is (potentially) different from the physical
slave address of the child bus. Address translation is done by the
hardware.

An ATR looks similar to an i2c-mux except:
:   - the address on the parent and child busses can be different
    - there is normally no need to select the child port; the alias used on the
      parent bus implies it

The ATR functionality can be provided by a chip with many other features.
The kernel i2c-atr provides a helper to implement an ATR within a driver.

The ATR creates a new I2C "child" adapter on each child bus. Adding
devices on the child bus ends up in invoking the driver code to select
an available alias. Maintaining an appropriate pool of available aliases
and picking one for each new device is up to the driver implementer. The
ATR maintains a table of currently assigned alias and uses it to modify
all I2C transactions directed to devices on the child buses.

A typical example follows.

Topology:

```
                    Slave X @ 0x10
            .-----.   |
.-----.     |     |---+---- B
| CPU |--A--| ATR |
`-----'     |     |---+---- C
            `-----'   |
                    Slave Y @ 0x10
```

Alias table:

A, B and C are three physical I2C busses, electrically independent from
each other. The ATR receives the transactions initiated on bus A and
propagates them on bus B or bus C or none depending on the device address
in the transaction and based on the alias table.

Alias table:

| Client | Alias |
| --- | --- |
| X (bus B, 0x10) | 0x20 |
| Y (bus C, 0x10) | 0x30 |

Transaction:

> - Slave X driver requests a transaction (on adapter B), slave address 0x10
> - ATR driver finds slave X is on bus B and has alias 0x20, rewrites
>   messages with address 0x20, forwards to adapter A
> - Physical I2C transaction on bus A, slave address 0x20
> - ATR chip detects transaction on address 0x20, finds it in table,
>   propagates transaction on bus B with address translated to 0x10,
>   keeps clock stretched on bus A waiting for reply
> - Slave X chip (on bus B) detects transaction at its own physical
>   address 0x10 and replies normally
> - ATR chip stops clock stretching and forwards reply on bus A,
>   with address translated back to 0x20
> - ATR driver receives the reply, rewrites messages with address 0x10
>   as they were initially
> - Slave X driver gets back the msgs[], with reply and address 0x10

Usage:

> 1. In the driver (typically in the probe function) add an ATR by
>    calling [`i2c_atr_new()`](i2c-address-translators.md#c.i2c_atr_new "i2c_atr_new") passing attach/detach callbacks
> 2. When the attach callback is called pick an appropriate alias,
>    configure it in the chip and return the chosen alias in the
>    alias_id parameter
> 3. When the detach callback is called, deconfigure the alias from
>    the chip and put the alias back in the pool for later usage

## I2C ATR functions and data structures

struct i2c_atr_ops
:   Callbacks from ATR to the device driver.

**Definition**:

```
struct i2c_atr_ops {
    int (*attach_client)(struct i2c_atr *atr, u32 chan_id, const struct i2c_client *client, u16 alias);
    void (*detach_client)(struct i2c_atr *atr, u32 chan_id, const struct i2c_client *client);
};
```

**Members**

`attach_client`
:   Notify the driver of a new device connected on a child
    bus, with the alias assigned to it. The driver must
    configure the hardware to use the alias.

`detach_client`
:   Notify the driver of a device getting disconnected. The
    driver must configure the hardware to stop using the
    alias.

**Description**

All these functions return 0 on success, a negative error code otherwise.

struct i2c_atr \*i2c_atr_new(struct i2c_adapter \*parent, struct [device](../driver-api/infrastructure.md#c.device "device") \*dev, const struct [i2c_atr_ops](i2c-address-translators.md#c.i2c_atr_ops "i2c_atr_ops") \*ops, int max_adapters)
:   Allocate and initialize an I2C ATR helper.

**Parameters**

`struct i2c_adapter *parent`
:   The parent (upstream) adapter

`struct device *dev`
:   The device acting as an ATR

`const struct i2c_atr_ops *ops`
:   Driver-specific callbacks

`int max_adapters`
:   Maximum number of child adapters

**Description**

The new ATR helper is connected to the parent adapter but has no child
adapters. Call [`i2c_atr_add_adapter()`](i2c-address-translators.md#c.i2c_atr_add_adapter "i2c_atr_add_adapter") to add some.

Call [`i2c_atr_delete()`](i2c-address-translators.md#c.i2c_atr_delete "i2c_atr_delete") to remove.

**Return**

pointer to the new ATR helper object, or ERR_PTR

void i2c_atr_delete(struct i2c_atr \*atr)
:   Delete an I2C ATR helper.

**Parameters**

`struct i2c_atr *atr`
:   I2C ATR helper to be deleted.

**Description**

Precondition: all the adapters added with [`i2c_atr_add_adapter()`](i2c-address-translators.md#c.i2c_atr_add_adapter "i2c_atr_add_adapter") must be
removed by calling [`i2c_atr_del_adapter()`](i2c-address-translators.md#c.i2c_atr_del_adapter "i2c_atr_del_adapter").

int i2c_atr_add_adapter(struct i2c_atr \*atr, u32 chan_id, struct [device](../driver-api/infrastructure.md#c.device "device") \*adapter_parent, struct fwnode_handle \*bus_handle)
:   Create a child ("downstream") I2C bus.

**Parameters**

`struct i2c_atr *atr`
:   The I2C ATR

`u32 chan_id`
:   Index of the new adapter (0 .. max_adapters-1). This value is
    passed to the callbacks in [`struct i2c_atr_ops`](i2c-address-translators.md#c.i2c_atr_ops "i2c_atr_ops").

`struct device *adapter_parent`
:   The device used as the parent of the new i2c adapter, or NULL
    to use the i2c-atr device as the parent.

`struct fwnode_handle *bus_handle`
:   The fwnode handle that points to the adapter's i2c
    peripherals, or NULL.

**Description**

After calling this function a new i2c bus will appear. Adding and removing
devices on the downstream bus will result in calls to the
[`i2c_atr_ops->attach_client`](i2c-address-translators.md#c.i2c_atr_ops "i2c_atr_ops") and [`i2c_atr_ops->detach_client`](i2c-address-translators.md#c.i2c_atr_ops "i2c_atr_ops") callbacks for the
driver to assign an alias to the device.

The adapter's fwnode is set to **bus_handle**, or if **bus_handle** is NULL the
function looks for a child node whose 'reg' property matches the chan_id
under the i2c-atr device's 'i2c-atr' node.

Call [`i2c_atr_del_adapter()`](i2c-address-translators.md#c.i2c_atr_del_adapter "i2c_atr_del_adapter") to remove the adapter.

**Return**

0 on success, a negative error code otherwise.

void i2c_atr_del_adapter(struct i2c_atr \*atr, u32 chan_id)
:   Remove a child ("downstream") I2C bus added by [`i2c_atr_add_adapter()`](i2c-address-translators.md#c.i2c_atr_add_adapter "i2c_atr_add_adapter"). If no I2C bus has been added this function is a no-op.

**Parameters**

`struct i2c_atr *atr`
:   The I2C ATR

`u32 chan_id`
:   Index of the adapter to be removed (0 .. max_adapters-1)

void i2c_atr_set_driver_data(struct i2c_atr \*atr, void \*data)
:   Set private driver data to the i2c-atr instance.

**Parameters**

`struct i2c_atr *atr`
:   The I2C ATR

`void *data`
:   Pointer to the data to store

void \*i2c_atr_get_driver_data(struct i2c_atr \*atr)
:   Get the stored drive data.

**Parameters**

`struct i2c_atr *atr`
:   The I2C ATR

**Return**

Pointer to the stored data
