---
collection: kernel
version: "6.17"
title: "Family ovs_datapath netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/ovs_datapath.html
fetched_at: 2026-09-16T16:40:54+00:00
---
# [Family `ovs_datapath` netlink specification](ovs_datapath.md#id1)

Contents

- [Family `ovs_datapath` netlink specification](ovs_datapath.md#family-ovs-datapath-netlink-specification)

  - [Summary](ovs_datapath.md#summary)
  - [Operations](ovs_datapath.md#operations)

    - [get](ovs_datapath.md#get)
    - [new](ovs_datapath.md#new)
    - [del](ovs_datapath.md#del)
  - [Multicast groups](ovs_datapath.md#multicast-groups)
  - [Definitions](ovs_datapath.md#definitions)

    - [ovs-header](ovs_datapath.md#ovs-header)
    - [user-features](ovs_datapath.md#user-features)
    - [ovs-dp-stats](ovs_datapath.md#ovs-dp-stats)
    - [ovs-dp-megaflow-stats](ovs_datapath.md#ovs-dp-megaflow-stats)
  - [Attribute sets](ovs_datapath.md#attribute-sets)

    - [datapath](ovs_datapath.md#datapath)

## [Summary](ovs_datapath.md#id2)

OVS datapath configuration over generic netlink.

## [Operations](ovs_datapath.md#id3)

### [get](ovs_datapath.md#id4)

Get / dump OVS data path configuration and state

value:
:   3

attribute-set:
:   [datapath](ovs_datapath.md#ovs-datapath-attribute-set-datapath)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`, `upcall-pid`, `stats`, `megaflow-stats`, `user-features`, `masks-cache-size`, `per-cpu-pids`]

dump:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`, `upcall-pid`, `stats`, `megaflow-stats`, `user-features`, `masks-cache-size`, `per-cpu-pids`]

### [new](ovs_datapath.md#id5)

Create new OVS data path

value:
:   1

attribute-set:
:   [datapath](ovs_datapath.md#ovs-datapath-attribute-set-datapath)

do:
:   **request**
    :   attributes:
        :   [`name`, `upcall-pid`, `user-features`]

### [del](ovs_datapath.md#id6)

Delete existing OVS data path

value:
:   2

attribute-set:
:   [datapath](ovs_datapath.md#ovs-datapath-attribute-set-datapath)

do:
:   **request**
    :   attributes:
        :   [`name`]

## [Multicast groups](ovs_datapath.md#id7)

- ovs_datapath

## [Definitions](ovs_datapath.md#id8)

### [ovs-header](ovs_datapath.md#id9)

type:
:   struct

members:
:   dp-ifindex (`u32`):

### [user-features](ovs_datapath.md#id10)

type:
:   flags

name-prefix:
:   ovs-dp-f-

enum-name:
:   None

entries:
:   unaligned:
    :   Allow last Netlink attribute to be unaligned

    vport-pids:
    :   Allow datapath to associate multiple Netlink PIDs to each vport

    tc-recirc-sharing:
    :   Allow tc offload recirc sharing

    dispatch-upcall-per-cpu:
    :   Allow per-cpu dispatch of upcalls

### [ovs-dp-stats](ovs_datapath.md#id11)

type:
:   struct

members:
:   n-hit (`u64`):

    n-missed (`u64`):

    n-lost (`u64`):

    n-flows (`u64`):

### [ovs-dp-megaflow-stats](ovs_datapath.md#id12)

type:
:   struct

members:
:   n-mask-hit (`u64`):

    n-masks (`u32`):

    padding (`u32`):

    n-cache-hit (`u64`):

    pad1 (`u64`):

## [Attribute sets](ovs_datapath.md#id13)

### [datapath](ovs_datapath.md#id14)

#### name (`string`)

#### upcall-pid (`u32`)

doc:
:   upcall pid

#### stats (`binary`)

struct:
:   [ovs-dp-stats](ovs_datapath.md#ovs-datapath-definition-ovs-dp-stats)

#### megaflow-stats (`binary`)

struct:
:   [ovs-dp-megaflow-stats](ovs_datapath.md#ovs-datapath-definition-ovs-dp-megaflow-stats)

#### user-features (`u32`)

enum:
:   [user-features](ovs_datapath.md#ovs-datapath-definition-user-features)

enum-as-flags:
:   True

#### pad (`unused`)

#### masks-cache-size (`u32`)

#### per-cpu-pids (`binary`)

sub-type:
:   u32

#### ifindex (`u32`)
