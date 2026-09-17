---
collection: kernel
version: "6.17"
title: "Family team netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/team.html
fetched_at: 2026-09-16T16:41:01+00:00
---
# [Family `team` netlink specification](team.md#id5)

Contents

- [Family `team` netlink specification](team.md#family-team-netlink-specification)

  - [Summary](team.md#summary)
  - [Operations](team.md#operations)

    - [noop](team.md#noop)
    - [options-set](team.md#options-set)
    - [options-get](team.md#options-get)
    - [port-list-get](team.md#port-list-get)
  - [Definitions](team.md#definitions)

    - [string-max-len](team.md#string-max-len)
    - [genl-change-event-mc-grp-name](team.md#genl-change-event-mc-grp-name)
  - [Attribute sets](team.md#attribute-sets)

    - [team](team.md#team)
    - [item-option](team.md#item-option)
    - [attr-option](team.md#attr-option)
    - [item-port](team.md#item-port)
    - [attr-port](team.md#attr-port)

## [Summary](team.md#id6)

Network team device driver.

## [Operations](team.md#id7)

### [noop](team.md#id8)

No operation

value:
:   0

attribute-set:
:   [team](team.md#team-attribute-set-team)

dont-validate:
:   [‘strict’]

do:
:   **reply**
    :   attributes:
        :   [`team-ifindex`]

### [options-set](team.md#id9)

Set team options

attribute-set:
:   [team](team.md#team-attribute-set-team)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`team-ifindex`, `list-option`]

    **reply**
    :   attributes:
        :   [`team-ifindex`, `list-option`]

### [options-get](team.md#id10)

Get team options info

attribute-set:
:   [team](team.md#team-attribute-set-team)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`team-ifindex`]

    **reply**
    :   attributes:
        :   [`team-ifindex`, `list-option`]

### [port-list-get](team.md#id11)

Get team ports info

attribute-set:
:   [team](team.md#team-attribute-set-team)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`team-ifindex`]

    **reply**
    :   attributes:
        :   [`team-ifindex`, `list-port`]

## [Definitions](team.md#id12)

### [string-max-len](team.md#id13)

type:
:   const

value:
:   32

### [genl-change-event-mc-grp-name](team.md#id14)

type:
:   const

value:
:   change_event

## [Attribute sets](team.md#id15)

### [team](team.md#id16)

#### unspec (`unused`)

value:
:   0

#### team-ifindex (`u32`)

#### list-option (`nest`)

nested-attributes:
:   [item-option](team.md#team-attribute-set-item-option)

#### list-port (`nest`)

nested-attributes:
:   [item-port](team.md#team-attribute-set-item-port)

### [item-option](team.md#id17)

#### option-unspec (`unused`)

value:
:   0

#### option (`nest`)

nested-attributes:
:   [attr-option](team.md#team-attribute-set-attr-option)

### [attr-option](team.md#id18)

#### unspec (`unused`)

value:
:   0

#### name (`string`)

#### changed (`flag`)

#### type (`u8`)

#### data (`binary`)

#### removed (`flag`)

#### port-ifindex (`u32`)

doc:
:   for per-port options

#### array-index (`u32`)

doc:
:   for array options

### [item-port](team.md#id19)

#### port-unspec (`unused`)

value:
:   0

#### port (`nest`)

nested-attributes:
:   [attr-port](team.md#team-attribute-set-attr-port)

### [attr-port](team.md#id20)

#### unspec (`unused`)

value:
:   0

#### ifindex (`u32`)

#### changed (`flag`)

#### linkup (`flag`)

#### speed (`u32`)

#### duplex (`u8`)

#### removed (`flag`)
