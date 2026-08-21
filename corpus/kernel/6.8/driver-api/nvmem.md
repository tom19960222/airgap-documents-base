---
collection: kernel
version: "6.8"
title: "NVMEM Subsystem"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/nvmem.html
fetched_at: 2026-08-21T03:31:14+00:00
---
# NVMEM Subsystem

> Srinivas Kandagatla <[srinivas.kandagatla@linaro.org](mailto:srinivas.kandagatla%40linaro.org)>

This document explains the NVMEM Framework along with the APIs provided,
and how to use it.

## 1. Introduction

*NVMEM* is the abbreviation for Non Volatile Memory layer. It is used to
retrieve configuration of SOC or Device specific data from non volatile
memories like eeprom, efuses and so on.

Before this framework existed, NVMEM drivers like eeprom were stored in
drivers/misc, where they all had to duplicate pretty much the same code to
register a sysfs file, allow in-kernel users to access the content of the
devices they were driving, etc.

This was also a problem as far as other in-kernel users were involved, since
the solutions used were pretty much different from one driver to another, there
was a rather big abstraction leak.

This framework aims at solve these problems. It also introduces DT
representation for consumer devices to go get the data they require (MAC
Addresses, SoC/Revision ID, part numbers, and so on) from the NVMEMs.

### NVMEM Providers

NVMEM provider refers to an entity that implements methods to initialize, read
and write the non-volatile memory.

## 2. Registering/Unregistering the NVMEM provider

A NVMEM provider can register with NVMEM core by supplying relevant
nvmem configuration to [`nvmem_register()`](nvmem.md#c.nvmem_register "nvmem_register"), on success core would return a valid
nvmem_device pointer.

[`nvmem_unregister()`](nvmem.md#c.nvmem_unregister "nvmem_unregister") is used to unregister a previously registered provider.

For example, a simple nvram case:

```
static int brcm_nvram_probe(struct platform_device *pdev)
{
      struct nvmem_config config = {
              .name = "brcm-nvram",
              .reg_read = brcm_nvram_read,
      };
      ...
      config.dev = &pdev->dev;
      config.priv = priv;
      config.size = resource_size(res);

      devm_nvmem_register(&config);
}
```

Users of board files can define and register nvmem cells using the
nvmem_cell_table struct:

```
static struct nvmem_cell_info foo_nvmem_cells[] = {
      {
              .name           = "macaddr",
              .offset         = 0x7f00,
              .bytes          = ETH_ALEN,
      }
};

static struct nvmem_cell_table foo_nvmem_cell_table = {
      .nvmem_name             = "i2c-eeprom",
      .cells                  = foo_nvmem_cells,
      .ncells                 = ARRAY_SIZE(foo_nvmem_cells),
};

nvmem_add_cell_table(&foo_nvmem_cell_table);
```

Additionally it is possible to create nvmem cell lookup entries and register
them with the nvmem framework from machine code as shown in the example below:

```
static struct nvmem_cell_lookup foo_nvmem_lookup = {
      .nvmem_name             = "i2c-eeprom",
      .cell_name              = "macaddr",
      .dev_id                 = "foo_mac.0",
      .con_id                 = "mac-address",
};

nvmem_add_cell_lookups(&foo_nvmem_lookup, 1);
```

### NVMEM Consumers

NVMEM consumers are the entities which make use of the NVMEM provider to
read from and to NVMEM.

## 3. NVMEM cell based consumer APIs

NVMEM cells are the data entries/fields in the NVMEM.
The NVMEM framework provides 3 APIs to read/write NVMEM cells:

```
struct nvmem_cell *nvmem_cell_get(struct device *dev, const char *name);
struct nvmem_cell *devm_nvmem_cell_get(struct device *dev, const char *name);

void nvmem_cell_put(struct nvmem_cell *cell);
void devm_nvmem_cell_put(struct device *dev, struct nvmem_cell *cell);

void *nvmem_cell_read(struct nvmem_cell *cell, ssize_t *len);
int nvmem_cell_write(struct nvmem_cell *cell, void *buf, ssize_t len);
```

\*[`nvmem_cell_get()`](nvmem.md#c.nvmem_cell_get "nvmem_cell_get") apis will get a reference to nvmem cell for a given id,
and nvmem_cell_read/write() can then read or write to the cell.
Once the usage of the cell is finished the consumer should call
\*[`nvmem_cell_put()`](nvmem.md#c.nvmem_cell_put "nvmem_cell_put") to free all the allocation memory for the cell.

## 4. Direct NVMEM device based consumer APIs

In some instances it is necessary to directly read/write the NVMEM.
To facilitate such consumers NVMEM framework provides below apis:

```
struct nvmem_device *nvmem_device_get(struct device *dev, const char *name);
struct nvmem_device *devm_nvmem_device_get(struct device *dev,
                                         const char *name);
struct nvmem_device *nvmem_device_find(void *data,
                      int (*match)(struct device *dev, const void *data));
void nvmem_device_put(struct nvmem_device *nvmem);
int nvmem_device_read(struct nvmem_device *nvmem, unsigned int offset,
                    size_t bytes, void *buf);
int nvmem_device_write(struct nvmem_device *nvmem, unsigned int offset,
                     size_t bytes, void *buf);
int nvmem_device_cell_read(struct nvmem_device *nvmem,
                         struct nvmem_cell_info *info, void *buf);
int nvmem_device_cell_write(struct nvmem_device *nvmem,
                          struct nvmem_cell_info *info, void *buf);
```

Before the consumers can read/write NVMEM directly, it should get hold
of nvmem_controller from one of the \*[`nvmem_device_get()`](nvmem.md#c.nvmem_device_get "nvmem_device_get") api.

The difference between these apis and cell based apis is that these apis always
take nvmem_device as parameter.

## 5. Releasing a reference to the NVMEM

When a consumer no longer needs the NVMEM, it has to release the reference
to the NVMEM it has obtained using the APIs mentioned in the above section.
The NVMEM framework provides 2 APIs to release a reference to the NVMEM:

```
void nvmem_cell_put(struct nvmem_cell *cell);
void devm_nvmem_cell_put(struct device *dev, struct nvmem_cell *cell);
void nvmem_device_put(struct nvmem_device *nvmem);
void devm_nvmem_device_put(struct device *dev, struct nvmem_device *nvmem);
```

Both these APIs are used to release a reference to the NVMEM and
devm_nvmem_cell_put and devm_nvmem_device_put destroys the devres associated
with this NVMEM.

### Userspace

## 6. Userspace binary interface

Userspace can read/write the raw NVMEM file located at:

```
/sys/bus/nvmem/devices/*/nvmem
```

ex:

```
hexdump /sys/bus/nvmem/devices/qfprom0/nvmem

0000000 0000 0000 0000 0000 0000 0000 0000 0000
*
00000a0 db10 2240 0000 e000 0c00 0c00 0000 0c00
0000000 0000 0000 0000 0000 0000 0000 0000 0000
...
*
0001000
```

## 7. DeviceTree Binding

See Documentation/devicetree/bindings/nvmem/nvmem.txt

## 8. NVMEM layouts

NVMEM layouts are yet another mechanism to create cells. With the device
tree binding it is possible to specify simple cells by using an offset
and a length. Sometimes, the cells doesn't have a static offset, but
the content is still well defined, e.g. tag-length-values. In this case,
the NVMEM device content has to be first parsed and the cells need to
be added accordingly. Layouts let you read the content of the NVMEM device
and let you add cells dynamically.

Another use case for layouts is the post processing of cells. With layouts,
it is possible to associate a custom post processing hook to a cell. It
even possible to add this hook to cells not created by the layout itself.

## 9. Internal kernel API

int nvmem_add_one_cell(struct nvmem_device \*nvmem, const struct nvmem_cell_info \*info)
:   Add one cell information to an nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device to add cells to.

`const struct nvmem_cell_info *info`
:   nvmem cell info to add to the device

**Return**

0 or negative error code on failure.

int nvmem_register_notifier(struct notifier_block \*nb)
:   Register a notifier block for nvmem events.

**Parameters**

`struct notifier_block *nb`
:   notifier block to be called on nvmem events.

**Return**

0 on success, negative error number on failure.

int nvmem_unregister_notifier(struct notifier_block \*nb)
:   Unregister a notifier block for nvmem events.

**Parameters**

`struct notifier_block *nb`
:   notifier block to be unregistered.

**Return**

0 on success, negative error number on failure.

struct nvmem_device \*nvmem_register(const struct nvmem_config \*config)
:   Register a nvmem device for given nvmem_config. Also creates a binary entry in /sys/bus/nvmem/devices/dev-name/nvmem

**Parameters**

`const struct nvmem_config *config`
:   nvmem device configuration with which nvmem device is created.

**Return**

Will be an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to nvmem_device
on success.

void nvmem_unregister(struct nvmem_device \*nvmem)
:   Unregister previously registered nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   Pointer to previously registered nvmem device.

struct nvmem_device \*devm_nvmem_register(struct [device](infrastructure.md#c.device "device") \*dev, const struct nvmem_config \*config)
:   Register a managed nvmem device for given nvmem_config. Also creates a binary entry in /sys/bus/nvmem/devices/dev-name/nvmem

**Parameters**

`struct device *dev`
:   Device that uses the nvmem device.

`const struct nvmem_config *config`
:   nvmem device configuration with which nvmem device is created.

**Return**

Will be an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to nvmem_device
on success.

struct nvmem_device \*of_nvmem_device_get(struct device_node \*np, const char \*id)
:   Get nvmem device from a given id

**Parameters**

`struct device_node *np`
:   Device tree node that uses the nvmem device.

`const char *id`
:   nvmem name from nvmem-names property.

**Return**

[`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to a struct nvmem_device
on success.

struct nvmem_device \*nvmem_device_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*dev_name)
:   Get nvmem device from a given id

**Parameters**

`struct device *dev`
:   Device that uses the nvmem device.

`const char *dev_name`
:   name of the requested nvmem device.

**Return**

[`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to a struct nvmem_device
on success.

struct nvmem_device \*nvmem_device_find(void \*data, int (\*match)(struct [device](infrastructure.md#c.device "device") \*dev, const void \*data))
:   Find nvmem device with matching function

**Parameters**

`void *data`
:   Data to pass to match function

`int (*match)(struct device *dev, const void *data)`
:   Callback function to check device

**Return**

[`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to a struct nvmem_device
on success.

void devm_nvmem_device_put(struct [device](infrastructure.md#c.device "device") \*dev, struct nvmem_device \*nvmem)
:   put alredy got nvmem device

**Parameters**

`struct device *dev`
:   Device that uses the nvmem device.

`struct nvmem_device *nvmem`
:   pointer to nvmem device allocated by [`devm_nvmem_cell_get()`](nvmem.md#c.devm_nvmem_cell_get "devm_nvmem_cell_get"),
    that needs to be released.

void nvmem_device_put(struct nvmem_device \*nvmem)
:   put alredy got nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   pointer to nvmem device that needs to be released.

struct nvmem_device \*devm_nvmem_device_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   Get nvmem cell of device form a given id

**Parameters**

`struct device *dev`
:   Device that requests the nvmem device.

`const char *id`
:   name id for the requested nvmem device.

**Return**

[`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to a struct nvmem_cell
on success. The nvmem_cell will be freed by the automatically once the
device is freed.

struct nvmem_cell \*of_nvmem_cell_get(struct device_node \*np, const char \*id)
:   Get a nvmem cell from given device node and cell id

**Parameters**

`struct device_node *np`
:   Device tree node that uses the nvmem cell.

`const char *id`
:   nvmem cell name from nvmem-cell-names property, or NULL
    for the cell at index 0 (the lone cell with no accompanying
    nvmem-cell-names property).

**Return**

Will be an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer
to a struct nvmem_cell. The nvmem_cell will be freed by the
[`nvmem_cell_put()`](nvmem.md#c.nvmem_cell_put "nvmem_cell_put").

struct nvmem_cell \*nvmem_cell_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   Get nvmem cell of device form a given cell name

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *id`
:   nvmem cell name to get (this corresponds with the name from the
    nvmem-cell-names property for DT systems and with the con_id from
    the lookup entry for non-DT systems).

**Return**

Will be an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer
to a struct nvmem_cell. The nvmem_cell will be freed by the
[`nvmem_cell_put()`](nvmem.md#c.nvmem_cell_put "nvmem_cell_put").

struct nvmem_cell \*devm_nvmem_cell_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*id)
:   Get nvmem cell of device form a given id

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *id`
:   nvmem cell name id to get.

**Return**

Will be an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer
to a struct nvmem_cell. The nvmem_cell will be freed by the
automatically once the device is freed.

void devm_nvmem_cell_put(struct [device](infrastructure.md#c.device "device") \*dev, struct nvmem_cell \*cell)
:   Release previously allocated nvmem cell from devm_nvmem_cell_get.

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`struct nvmem_cell *cell`
:   Previously allocated nvmem cell by [`devm_nvmem_cell_get()`](nvmem.md#c.devm_nvmem_cell_get "devm_nvmem_cell_get").

void nvmem_cell_put(struct nvmem_cell \*cell)
:   Release previously allocated nvmem cell.

**Parameters**

`struct nvmem_cell *cell`
:   Previously allocated nvmem cell by [`nvmem_cell_get()`](nvmem.md#c.nvmem_cell_get "nvmem_cell_get").

void \*nvmem_cell_read(struct nvmem_cell \*cell, size_t \*len)
:   Read a given nvmem cell

**Parameters**

`struct nvmem_cell *cell`
:   nvmem cell to be read.

`size_t *len`
:   pointer to length of cell which will be populated on successful read;
    can be NULL.

**Return**

[`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR") on error or a valid pointer to a buffer on success. The
buffer should be freed by the consumer with a [`kfree()`](../core-api/mm-api.md#c.kfree "kfree").

int nvmem_cell_write(struct nvmem_cell \*cell, void \*buf, size_t len)
:   Write to a given nvmem cell

**Parameters**

`struct nvmem_cell *cell`
:   nvmem cell to be written.

`void *buf`
:   Buffer to be written.

`size_t len`
:   length of buffer to be written to nvmem cell.

**Return**

length of bytes written or negative on failure.

int nvmem_cell_read_u8(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u8 \*val)
:   Read a cell value as a u8

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u8 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

int nvmem_cell_read_u16(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u16 \*val)
:   Read a cell value as a u16

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u16 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

int nvmem_cell_read_u32(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u32 \*val)
:   Read a cell value as a u32

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u32 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

int nvmem_cell_read_u64(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u64 \*val)
:   Read a cell value as a u64

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u64 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

int nvmem_cell_read_variable_le_u32(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u32 \*val)
:   Read up to 32-bits of data as a little endian number.

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u32 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

int nvmem_cell_read_variable_le_u64(struct [device](infrastructure.md#c.device "device") \*dev, const char \*cell_id, u64 \*val)
:   Read up to 64-bits of data as a little endian number.

**Parameters**

`struct device *dev`
:   Device that requests the nvmem cell.

`const char *cell_id`
:   Name of nvmem cell to read.

`u64 *val`
:   pointer to output value.

**Return**

0 on success or negative errno.

ssize_t nvmem_device_cell_read(struct nvmem_device \*nvmem, struct nvmem_cell_info \*info, void \*buf)
:   Read a given nvmem device and cell

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device to read from.

`struct nvmem_cell_info *info`
:   nvmem cell info to be read.

`void *buf`
:   buffer pointer which will be populated on successful read.

**Return**

length of successful bytes read on success and negative
error code on error.

int nvmem_device_cell_write(struct nvmem_device \*nvmem, struct nvmem_cell_info \*info, void \*buf)
:   Write cell to a given nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device to be written to.

`struct nvmem_cell_info *info`
:   nvmem cell info to be written.

`void *buf`
:   buffer to be written to cell.

**Return**

length of bytes written or negative error code on failure.

int nvmem_device_read(struct nvmem_device \*nvmem, unsigned int offset, size_t bytes, void \*buf)
:   Read from a given nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device to read from.

`unsigned int offset`
:   offset in nvmem device.

`size_t bytes`
:   number of bytes to read.

`void *buf`
:   buffer pointer which will be populated on successful read.

**Return**

length of successful bytes read on success and negative
error code on error.

int nvmem_device_write(struct nvmem_device \*nvmem, unsigned int offset, size_t bytes, void \*buf)
:   Write cell to a given nvmem device

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device to be written to.

`unsigned int offset`
:   offset in nvmem device.

`size_t bytes`
:   number of bytes to write.

`void *buf`
:   buffer to be written.

**Return**

length of bytes written or negative error code on failure.

void nvmem_add_cell_table(struct nvmem_cell_table \*table)
:   register a table of cell info entries

**Parameters**

`struct nvmem_cell_table *table`
:   table of cell info entries

void nvmem_del_cell_table(struct nvmem_cell_table \*table)
:   remove a previously registered cell info table

**Parameters**

`struct nvmem_cell_table *table`
:   table of cell info entries

void nvmem_add_cell_lookups(struct nvmem_cell_lookup \*entries, size_t nentries)
:   register a list of cell lookup entries

**Parameters**

`struct nvmem_cell_lookup *entries`
:   array of cell lookup entries

`size_t nentries`
:   number of cell lookup entries in the array

void nvmem_del_cell_lookups(struct nvmem_cell_lookup \*entries, size_t nentries)
:   remove a list of previously added cell lookup entries

**Parameters**

`struct nvmem_cell_lookup *entries`
:   array of cell lookup entries

`size_t nentries`
:   number of cell lookup entries in the array

const char \*nvmem_dev_name(struct nvmem_device \*nvmem)
:   Get the name of a given nvmem device.

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device.

**Return**

name of the nvmem device.

size_t nvmem_dev_size(struct nvmem_device \*nvmem)
:   Get the size of a given nvmem device.

**Parameters**

`struct nvmem_device *nvmem`
:   nvmem device.

**Return**

size of the nvmem device.
