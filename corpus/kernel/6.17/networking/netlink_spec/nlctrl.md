---
collection: kernel
version: "6.17"
title: "Family nlctrl netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/nlctrl.html
fetched_at: 2026-09-16T16:40:53+00:00
---
# [Family `nlctrl` netlink specification](nlctrl.md#id2)

Contents

- [Family `nlctrl` netlink specification](nlctrl.md#family-nlctrl-netlink-specification)

  - [Summary](nlctrl.md#summary)
  - [Operations](nlctrl.md#operations)

    - [getfamily](nlctrl.md#getfamily)
    - [getpolicy](nlctrl.md#getpolicy)
  - [Definitions](nlctrl.md#definitions)

    - [op-flags](nlctrl.md#op-flags)
    - [attr-type](nlctrl.md#attr-type)
  - [Attribute sets](nlctrl.md#attribute-sets)

    - [ctrl-attrs](nlctrl.md#ctrl-attrs)
    - [mcast-group-attrs](nlctrl.md#mcast-group-attrs)
    - [op-attrs](nlctrl.md#op-attrs)
    - [policy-attrs](nlctrl.md#policy-attrs)
    - [op-policy-attrs](nlctrl.md#op-policy-attrs)

## [Summary](nlctrl.md#id3)

genetlink meta-family that exposes information about all genetlink
families registered in the kernel (including itself).

## [Operations](nlctrl.md#id4)

### [getfamily](nlctrl.md#id5)

Get / dump genetlink families

attribute-set:
:   [ctrl-attrs](nlctrl.md#nlctrl-attribute-set-ctrl-attrs)

do:
:   **request**
    :   attributes:
        :   [`family-name`]

    **reply**
    :   attributes:
        :   [`family-id`, `family-name`, `hdrsize`, `maxattr`, `mcast-groups`, `ops`, `version`]

dump:
:   **reply**
    :   attributes:
        :   [`family-id`, `family-name`, `hdrsize`, `maxattr`, `mcast-groups`, `ops`, `version`]

### [getpolicy](nlctrl.md#id6)

Get / dump genetlink policies

attribute-set:
:   [ctrl-attrs](nlctrl.md#nlctrl-attribute-set-ctrl-attrs)

dump:
:   **request**
    :   attributes:
        :   [`family-name`, `family-id`, `op`]

    **reply**
    :   attributes:
        :   [`family-id`, `op-policy`, `policy`]

## [Definitions](nlctrl.md#id7)

### [op-flags](nlctrl.md#id8)

type:
:   flags

enum-name:
:   None

entries:
:   - `admin-perm`
    - `cmd-cap-do`
    - `cmd-cap-dump`
    - `cmd-cap-haspol`
    - `uns-admin-perm`

### [attr-type](nlctrl.md#id9)

enum-name:
:   netlink-attribute-type

type:
:   enum

entries:
:   - `invalid`
    - `flag`
    - `u8`
    - `u16`
    - `u32`
    - `u64`
    - `s8`
    - `s16`
    - `s32`
    - `s64`
    - `binary`
    - `string`
    - `nul-string`
    - `nested`
    - `nested-array`
    - `bitfield32`
    - `sint`
    - `uint`

## [Attribute sets](nlctrl.md#id10)

### [ctrl-attrs](nlctrl.md#id11)

#### family-id (`u16`)

#### family-name (`string`)

#### version (`u32`)

#### hdrsize (`u32`)

#### maxattr (`u32`)

#### ops (`indexed-array`)

sub-type:
:   nest

nested-attributes:
:   [op-attrs](nlctrl.md#nlctrl-attribute-set-op-attrs)

#### mcast-groups (`indexed-array`)

sub-type:
:   nest

nested-attributes:
:   [mcast-group-attrs](nlctrl.md#nlctrl-attribute-set-mcast-group-attrs)

#### policy (`nest-type-value`)

type-value:
:   [‘policy-id’, ‘attr-id’]

nested-attributes:
:   [policy-attrs](nlctrl.md#nlctrl-attribute-set-policy-attrs)

#### op-policy (`nest-type-value`)

type-value:
:   [‘op-id’]

nested-attributes:
:   [op-policy-attrs](nlctrl.md#nlctrl-attribute-set-op-policy-attrs)

#### op (`u32`)

### [mcast-group-attrs](nlctrl.md#id12)

#### name (`string`)

#### id (`u32`)

### [op-attrs](nlctrl.md#id13)

#### id (`u32`)

#### flags (`u32`)

enum:
:   [op-flags](nlctrl.md#nlctrl-definition-op-flags)

enum-as-flags:
:   True

### [policy-attrs](nlctrl.md#id14)

#### type (`u32`)

enum:
:   [attr-type](nlctrl.md#nlctrl-definition-attr-type)

#### min-value-s (`s64`)

#### max-value-s (`s64`)

#### min-value-u (`u64`)

#### max-value-u (`u64`)

#### min-length (`u32`)

#### max-length (`u32`)

#### policy-idx (`u32`)

#### policy-maxtype (`u32`)

#### bitfield32-mask (`u32`)

#### mask (`u64`)

#### pad (`pad`)

### [op-policy-attrs](nlctrl.md#id15)

#### do (`u32`)

#### dump (`u32`)
