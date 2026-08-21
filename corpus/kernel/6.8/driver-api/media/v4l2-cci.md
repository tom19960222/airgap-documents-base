---
collection: kernel
version: "6.8"
title: "2.24. V4L2 CCI kAPI"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/v4l2-cci.html
fetched_at: 2026-08-21T03:38:45+00:00
---
# 2.24. V4L2 CCI kAPI

struct cci_reg_sequence
:   An individual write from a sequence of CCI writes

**Definition**:

```
struct cci_reg_sequence {
    u32 reg;
    u64 val;
};
```

**Members**

`reg`
:   Register address, use CCI_REG#() macros to encode reg width

`val`
:   Register value

**Description**

Register/value pairs for sequences of writes.

int cci_read(struct regmap \*map, u32 reg, u64 \*val, int \*err)
:   Read a value from a single CCI register

**Parameters**

`struct regmap *map`
:   Register map to read from

`u32 reg`
:   Register address to read, use CCI_REG#() macros to encode reg width

`u64 *val`
:   Pointer to store read value

`int *err`
:   Optional pointer to store errors, if a previous error is set
    then the read will be skipped

**Return**

`0` on success or a negative error code on failure.

int cci_write(struct regmap \*map, u32 reg, u64 val, int \*err)
:   Write a value to a single CCI register

**Parameters**

`struct regmap *map`
:   Register map to write to

`u32 reg`
:   Register address to write, use CCI_REG#() macros to encode reg width

`u64 val`
:   Value to be written

`int *err`
:   Optional pointer to store errors, if a previous error is set
    then the write will be skipped

**Return**

`0` on success or a negative error code on failure.

int cci_update_bits(struct regmap \*map, u32 reg, u64 mask, u64 val, int \*err)
:   Perform a read/modify/write cycle on a single CCI register

**Parameters**

`struct regmap *map`
:   Register map to update

`u32 reg`
:   Register address to update, use CCI_REG#() macros to encode reg width

`u64 mask`
:   Bitmask to change

`u64 val`
:   New value for bitmask

`int *err`
:   Optional pointer to store errors, if a previous error is set
    then the update will be skipped

**Description**

Note this uses read-modify-write to update the bits, atomicity with regards
to other cci_\*() register access functions is NOT guaranteed.

**Return**

`0` on success or a negative error code on failure.

int cci_multi_reg_write(struct regmap \*map, const struct [cci_reg_sequence](v4l2-cci.md#c.cci_reg_sequence "cci_reg_sequence") \*regs, unsigned int num_regs, int \*err)
:   Write multiple registers to the device

**Parameters**

`struct regmap *map`
:   Register map to write to

`const struct cci_reg_sequence *regs`
:   Array of structures containing register-address, -value pairs to be
    written, register-addresses use CCI_REG#() macros to encode reg width

`unsigned int num_regs`
:   Number of registers to write

`int *err`
:   Optional pointer to store errors, if a previous error is set
    then the write will be skipped

**Description**

Write multiple registers to the device where the set of register, value
pairs are supplied in any order, possibly not all in a single range.

Use of the CCI_REG#() macros to encode reg width is mandatory.

For raw lists of register-address, -value pairs with only 8 bit
wide writes regmap_multi_reg_write() can be used instead.

**Return**

`0` on success or a negative error code on failure.

struct regmap \*devm_cci_regmap_init_i2c(struct [i2c_client](../i2c.md#c.i2c_client "i2c_client") \*client, int reg_addr_bits)
:   Create regmap to use with cci_\*() register access functions

**Parameters**

`struct i2c_client *client`
:   i2c_client to create the regmap for

`int reg_addr_bits`
:   register address width to use (8 or 16)

**Description**

Note the memory for the created regmap is devm() managed, tied to the client.

**Return**

`0` on success or a negative error code on failure.
