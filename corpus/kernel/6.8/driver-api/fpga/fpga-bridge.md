---
collection: kernel
version: "6.8"
title: "FPGA Bridge"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/fpga/fpga-bridge.html
fetched_at: 2026-08-21T03:32:37+00:00
---
# FPGA Bridge

## API to implement a new FPGA bridge

- [`struct fpga_bridge`](fpga-bridge.md#c.fpga_bridge "fpga_bridge") - The FPGA Bridge structure
- [`struct fpga_bridge_ops`](fpga-bridge.md#c.fpga_bridge_ops "fpga_bridge_ops") - Low level Bridge driver ops
- [`fpga_bridge_register()`](fpga-bridge.md#c.fpga_bridge_register "fpga_bridge_register") - Create and register a bridge
- [`fpga_bridge_unregister()`](fpga-bridge.md#c.fpga_bridge_unregister "fpga_bridge_unregister") - Unregister a bridge

struct fpga_bridge
:   FPGA bridge structure

**Definition**:

```
struct fpga_bridge {
    const char *name;
    struct device dev;
    struct mutex mutex;
    const struct fpga_bridge_ops *br_ops;
    struct fpga_image_info *info;
    struct list_head node;
    void *priv;
};
```

**Members**

`name`
:   name of low level FPGA bridge

`dev`
:   FPGA bridge device

`mutex`
:   enforces exclusive reference to bridge

`br_ops`
:   pointer to struct of FPGA bridge ops

`info`
:   fpga image specific information

`node`
:   FPGA bridge list node

`priv`
:   low level driver private date

struct fpga_bridge_ops
:   ops for low level FPGA bridge drivers

**Definition**:

```
struct fpga_bridge_ops {
    int (*enable_show)(struct fpga_bridge *bridge);
    int (*enable_set)(struct fpga_bridge *bridge, bool enable);
    void (*fpga_bridge_remove)(struct fpga_bridge *bridge);
    const struct attribute_group **groups;
};
```

**Members**

`enable_show`
:   returns the FPGA bridge's status

`enable_set`
:   set an FPGA bridge as enabled or disabled

`fpga_bridge_remove`
:   set FPGA into a specific state during driver remove

`groups`
:   optional attribute groups.

struct [fpga_bridge](fpga-bridge.md#c.fpga_bridge "fpga_bridge") \*fpga_bridge_register(struct [device](../infrastructure.md#c.device "device") \*parent, const char \*name, const struct [fpga_bridge_ops](fpga-bridge.md#c.fpga_bridge_ops "fpga_bridge_ops") \*br_ops, void \*priv)
:   create and register an FPGA Bridge device

**Parameters**

`struct device *parent`
:   FPGA bridge device from pdev

`const char *name`
:   FPGA bridge name

`const struct fpga_bridge_ops *br_ops`
:   pointer to structure of fpga bridge ops

`void *priv`
:   FPGA bridge private data

**Return**

[`struct fpga_bridge`](fpga-bridge.md#c.fpga_bridge "fpga_bridge") pointer or [`ERR_PTR()`](../../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR")

void fpga_bridge_unregister(struct [fpga_bridge](fpga-bridge.md#c.fpga_bridge "fpga_bridge") \*bridge)
:   unregister an FPGA bridge

**Parameters**

`struct fpga_bridge *bridge`
:   FPGA bridge struct

**Description**

This function is intended for use in an FPGA bridge driver's remove function.
