---
collection: qemu
version: "11.1.0"
title: "Bitwise operations"
source_url: https://www.qemu.org/docs/master/devel/bitops.html
fetched_at: 2026-08-21T03:25:49+00:00
---
# Bitwise operations

The header `qemu/bitops.h` provides utility functions for
performing bitwise operations.

**Functions operating on arrays of bits**

We provide a set of functions which work on arbitrary-length arrays of
bits. These come in several flavours which vary in what the type of the
underlying storage for the bits is:

- Bits stored in an array of ‘unsigned long’: set_bit(), clear_bit(), etc
- Bits stored in an array of ‘uint32_t’: set_bit32(), clear_bit32(), etc

Because the ‘unsigned long’ type has a size which varies between
host systems, the versions using ‘uint32_t’ are often preferable.
This is particularly the case in a device model where there may
be some guest-visible register view of the bit array.

We do not currently implement uint32_t versions of find_last_bit(),
find_next_bit(), find_next_zero_bit() or find_first_zero_bit(),
because we haven’t yet needed them. If you need them you should
implement them similarly to the ‘unsigned long’ versions.

You can declare a bitmap to be used with these functions via the
DECLARE_BITMAP and DECLARE_BITMAP32 macros in bitmap.h.

**‘unsigned long’ bit array APIs**

void set_bit(long nr, unsigned long \*addr)
:   Set a bit in memory

**Parameters**

`long nr`
:   the bit to set

`unsigned long *addr`
:   the address to start counting from

void set_bit_atomic(long nr, unsigned long \*addr)
:   Set a bit in memory atomically

**Parameters**

`long nr`
:   the bit to set

`unsigned long *addr`
:   the address to start counting from

void clear_bit(long nr, unsigned long \*addr)
:   Clears a bit in memory

**Parameters**

`long nr`
:   Bit to clear

`unsigned long *addr`
:   Address to start counting from

void clear_bit_atomic(long nr, unsigned long \*addr)
:   Clears a bit in memory atomically

**Parameters**

`long nr`
:   Bit to clear

`unsigned long *addr`
:   Address to start counting from

void change_bit(long nr, unsigned long \*addr)
:   Toggle a bit in memory

**Parameters**

`long nr`
:   Bit to change

`unsigned long *addr`
:   Address to start counting from

int test_and_set_bit(long nr, unsigned long \*addr)
:   Set a bit and return its old value

**Parameters**

`long nr`
:   Bit to set

`unsigned long *addr`
:   Address to count from

int test_and_clear_bit(long nr, unsigned long \*addr)
:   Clear a bit and return its old value

**Parameters**

`long nr`
:   Bit to clear

`unsigned long *addr`
:   Address to count from

int test_and_change_bit(long nr, unsigned long \*addr)
:   Change a bit and return its old value

**Parameters**

`long nr`
:   Bit to change

`unsigned long *addr`
:   Address to count from

int test_bit(long nr, const unsigned long \*addr)
:   Determine whether a bit is set

**Parameters**

`long nr`
:   bit number to test

`const unsigned long *addr`
:   Address to start counting from

unsigned long find_last_bit(const unsigned long \*addr, unsigned long size)
:   find the last set bit in a memory region

**Parameters**

`const unsigned long *addr`
:   The address to start the search at

`unsigned long size`
:   The maximum size to search

**Description**

Returns the bit number of the last set bit,
or **size** if there is no set bit in the bitmap.

unsigned long find_next_bit(const unsigned long \*addr, unsigned long size, unsigned long offset)
:   find the next set bit in a memory region

**Parameters**

`const unsigned long *addr`
:   The address to base the search on

`unsigned long size`
:   The bitmap size in bits

`unsigned long offset`
:   The bitnumber to start searching at

**Description**

Returns the bit number of the next set bit,
or **size** if there are no further set bits in the bitmap.

unsigned long find_next_zero_bit(const unsigned long \*addr, unsigned long size, unsigned long offset)
:   find the next cleared bit in a memory region

**Parameters**

`const unsigned long *addr`
:   The address to base the search on

`unsigned long size`
:   The bitmap size in bits

`unsigned long offset`
:   The bitnumber to start searching at

**Description**

Returns the bit number of the next cleared bit,
or **size** if there are no further clear bits in the bitmap.

unsigned long find_first_bit(const unsigned long \*addr, unsigned long size)
:   find the first set bit in a memory region

**Parameters**

`const unsigned long *addr`
:   The address to start the search at

`unsigned long size`
:   The maximum size to search

**Description**

Returns the bit number of the first set bit,
or **size** if there is no set bit in the bitmap.

unsigned long find_first_zero_bit(const unsigned long \*addr, unsigned long size)
:   find the first cleared bit in a memory region

**Parameters**

`const unsigned long *addr`
:   The address to start the search at

`unsigned long size`
:   The maximum size to search

**Description**

Returns the bit number of the first cleared bit,
or **size** if there is no clear bit in the bitmap.

**‘uint32_t’ bit array APIs**

void set_bit32(long nr, uint32_t \*addr)
:   Set a bit in memory

**Parameters**

`long nr`
:   the bit to set

`uint32_t *addr`
:   the address to start counting from

void set_bit32_atomic(long nr, uint32_t \*addr)
:   Set a bit in memory atomically

**Parameters**

`long nr`
:   the bit to set

`uint32_t *addr`
:   the address to start counting from

void clear_bit32(long nr, uint32_t \*addr)
:   Clears a bit in memory

**Parameters**

`long nr`
:   Bit to clear

`uint32_t *addr`
:   Address to start counting from

void clear_bit32_atomic(long nr, uint32_t \*addr)
:   Clears a bit in memory atomically

**Parameters**

`long nr`
:   Bit to clear

`uint32_t *addr`
:   Address to start counting from

void change_bit32(long nr, uint32_t \*addr)
:   Toggle a bit in memory

**Parameters**

`long nr`
:   Bit to change

`uint32_t *addr`
:   Address to start counting from

int test_and_set_bit32(long nr, uint32_t \*addr)
:   Set a bit and return its old value

**Parameters**

`long nr`
:   Bit to set

`uint32_t *addr`
:   Address to count from

int test_and_clear_bit32(long nr, uint32_t \*addr)
:   Clear a bit and return its old value

**Parameters**

`long nr`
:   Bit to clear

`uint32_t *addr`
:   Address to count from

int test_and_change_bit32(long nr, uint32_t \*addr)
:   Change a bit and return its old value

**Parameters**

`long nr`
:   Bit to change

`uint32_t *addr`
:   Address to count from

int test_bit32(long nr, const uint32_t \*addr)
:   Determine whether a bit is set

**Parameters**

`long nr`
:   bit number to test

`const uint32_t *addr`
:   Address to start counting from

uint32_t find_first_bit32(const uint32_t \*addr, uint32_t size)
:   find the first set bit in a memory region

**Parameters**

`const uint32_t *addr`
:   The address to start the search at

`uint32_t size`
:   The maximum size to search

**Description**

Returns the bit number of the first set bit,
or **size** if there is no set bit in the bitmap.

**Miscellaneous bit operations on single values**

These functions are a collection of useful operations
(rotations, bit extract, bit deposit, etc) on single
integer values.

uint8_t rol8(uint8_t word, unsigned int shift)
:   rotate an 8-bit value left

**Parameters**

`uint8_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint8_t ror8(uint8_t word, unsigned int shift)
:   rotate an 8-bit value right

**Parameters**

`uint8_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint16_t rol16(uint16_t word, unsigned int shift)
:   rotate a 16-bit value left

**Parameters**

`uint16_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint16_t ror16(uint16_t word, unsigned int shift)
:   rotate a 16-bit value right

**Parameters**

`uint16_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint32_t rol32(uint32_t word, unsigned int shift)
:   rotate a 32-bit value left

**Parameters**

`uint32_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint32_t ror32(uint32_t word, unsigned int shift)
:   rotate a 32-bit value right

**Parameters**

`uint32_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint64_t rol64(uint64_t word, unsigned int shift)
:   rotate a 64-bit value left

**Parameters**

`uint64_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint64_t ror64(uint64_t word, unsigned int shift)
:   rotate a 64-bit value right

**Parameters**

`uint64_t word`
:   value to rotate

`unsigned int shift`
:   bits to roll

uint32_t hswap32(uint32_t h)
:   swap 16-bit halfwords within a 32-bit value

**Parameters**

`uint32_t h`
:   value to swap

uint64_t hswap64(uint64_t h)
:   swap 16-bit halfwords within a 64-bit value

**Parameters**

`uint64_t h`
:   value to swap

uint64_t wswap64(uint64_t h)
:   swap 32-bit words within a 64-bit value

**Parameters**

`uint64_t h`
:   value to swap

uint32_t extract32(uint32_t value, int start, int length)

**Parameters**

`uint32_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 32 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it. The bit field must
lie entirely within the 32 bit word. It is valid to request that
all 32 bits are returned (ie **length** 32 and **start** 0).

**Return**

the value of the bit field extracted from the input value.

uint8_t extract8(uint8_t value, int start, int length)

**Parameters**

`uint8_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 8 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it. The bit field must
lie entirely within the 8 bit word. It is valid to request that
all 8 bits are returned (ie **length** 8 and **start** 0).

**Return**

the value of the bit field extracted from the input value.

uint16_t extract16(uint16_t value, int start, int length)

**Parameters**

`uint16_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 16 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it. The bit field must
lie entirely within the 16 bit word. It is valid to request that
all 16 bits are returned (ie **length** 16 and **start** 0).

**Return**

the value of the bit field extracted from the input value.

uint64_t extract64(uint64_t value, int start, int length)

**Parameters**

`uint64_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 64 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it. The bit field must
lie entirely within the 64 bit word. It is valid to request that
all 64 bits are returned (ie **length** 64 and **start** 0).

**Return**

the value of the bit field extracted from the input value.

int32_t sextract32(uint32_t value, int start, int length)

**Parameters**

`uint32_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 32 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it, sign extended to
an int32_t (ie with the most significant bit of the field propagated
to all the upper bits of the return value). The bit field must lie
entirely within the 32 bit word. It is valid to request that
all 32 bits are returned (ie **length** 32 and **start** 0).

**Return**

the sign extended value of the bit field extracted from the
input value.

int64_t sextract64(uint64_t value, int start, int length)

**Parameters**

`uint64_t value`
:   the value to extract the bit field from

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

**Description**

Extract from the 64 bit input **value** the bit field specified by the
**start** and **length** parameters, and return it, sign extended to
an int64_t (ie with the most significant bit of the field propagated
to all the upper bits of the return value). The bit field must lie
entirely within the 64 bit word. It is valid to request that
all 64 bits are returned (ie **length** 64 and **start** 0).

**Return**

the sign extended value of the bit field extracted from the
input value.

uint32_t deposit32(uint32_t value, int start, int length, uint32_t fieldval)

**Parameters**

`uint32_t value`
:   initial value to insert bit field into

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

`uint32_t fieldval`
:   the value to insert into the bit field

**Description**

Deposit **fieldval** into the 32 bit **value** at the bit field specified
by the **start** and **length** parameters, and return the modified
**value**. Bits of **value** outside the bit field are not modified.
Bits of **fieldval** above the least significant **length** bits are
ignored. The bit field must lie entirely within the 32 bit word.
It is valid to request that all 32 bits are modified (ie **length**
32 and **start** 0).

**Return**

the modified **value**.

uint64_t deposit64(uint64_t value, int start, int length, uint64_t fieldval)

**Parameters**

`uint64_t value`
:   initial value to insert bit field into

`int start`
:   the lowest bit in the bit field (numbered from 0)

`int length`
:   the length of the bit field

`uint64_t fieldval`
:   the value to insert into the bit field

**Description**

Deposit **fieldval** into the 64 bit **value** at the bit field specified
by the **start** and **length** parameters, and return the modified
**value**. Bits of **value** outside the bit field are not modified.
Bits of **fieldval** above the least significant **length** bits are
ignored. The bit field must lie entirely within the 64 bit word.
It is valid to request that all 64 bits are modified (ie **length**
64 and **start** 0).

**Return**

the modified **value**.

uint32_t half_shuffle32(uint32_t x)

**Parameters**

`uint32_t x`
:   32-bit value (of which only the bottom 16 bits are of interest)

**Description**

Given an input value:

```
xxxx xxxx xxxx xxxx ABCD EFGH IJKL MNOP
```

return the value where the bottom 16 bits are spread out into
the odd bits in the word, and the even bits are zeroed:

```
0A0B 0C0D 0E0F 0G0H 0I0J 0K0L 0M0N 0O0P
```

Any bits set in the top half of the input are ignored.

**Return**

the shuffled bits.

uint64_t half_shuffle64(uint64_t x)

**Parameters**

`uint64_t x`
:   64-bit value (of which only the bottom 32 bits are of interest)

**Description**

Given an input value:

```
xxxx xxxx xxxx .... xxxx xxxx ABCD EFGH IJKL MNOP QRST UVWX YZab cdef
```

return the value where the bottom 32 bits are spread out into
the odd bits in the word, and the even bits are zeroed:

```
0A0B 0C0D 0E0F 0G0H 0I0J 0K0L 0M0N .... 0U0V 0W0X 0Y0Z 0a0b 0c0d 0e0f
```

Any bits set in the top half of the input are ignored.

**Return**

the shuffled bits.

uint32_t half_unshuffle32(uint32_t x)

**Parameters**

`uint32_t x`
:   32-bit value (of which only the odd bits are of interest)

**Description**

Given an input value:

```
xAxB xCxD xExF xGxH xIxJ xKxL xMxN xOxP
```

return the value where all the odd bits are compressed down
into the low half of the word, and the high half is zeroed:

```
0000 0000 0000 0000 ABCD EFGH IJKL MNOP
```

Any even bits set in the input are ignored.

**Return**

the unshuffled bits.

uint64_t half_unshuffle64(uint64_t x)

**Parameters**

`uint64_t x`
:   64-bit value (of which only the odd bits are of interest)

**Description**

Given an input value:

```
xAxB xCxD xExF xGxH xIxJ xKxL xMxN .... xUxV xWxX xYxZ xaxb xcxd xexf
```

return the value where all the odd bits are compressed down
into the low half of the word, and the high half is zeroed:

```
0000 0000 0000 .... 0000 0000 ABCD EFGH IJKL MNOP QRST UVWX YZab cdef
```

Any even bits set in the input are ignored.

**Return**

the unshuffled bits.
