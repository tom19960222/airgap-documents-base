---
collection: kernel
version: "6.8"
title: "Family ovs_datapath netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/ovs_datapath.html
fetched_at: 2026-08-21T03:49:19+00:00
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
    - [datapath-stats](ovs_datapath.md#datapath-stats)
    - [megaflow-stats](ovs_datapath.md#megaflow-stats)
  - [Attribute sets](ovs_datapath.md#attribute-sets)

    - [datapath](ovs_datapath.md#datapath)

      - [name (`string`)](ovs_datapath.md#name-string)
      - [upcall-pid (`u32`)](ovs_datapath.md#upcall-pid-u32)
      - [stats (`binary`)](ovs_datapath.md#stats-binary)
      - [megaflow-stats (`binary`)](ovs_datapath.md#megaflow-stats-binary)
      - [user-features (`u32`)](ovs_datapath.md#user-features-u32)
      - [pad (`unused`)](ovs_datapath.md#pad-unused)
      - [masks-cache-size (`u32`)](ovs_datapath.md#masks-cache-size-u32)
      - [per-cpu-pids (`binary`)](ovs_datapath.md#per-cpu-pids-binary)
      - [ifindex (`u32`)](ovs_datapath.md#ifindex-u32)

## [Summary](ovs_datapath.md#id2)

OVS datapath configuration over generic netlink.

## [Operations](ovs_datapath.md#id3)

### [get](ovs_datapath.md#id4)

Get / dump OVS data path configuration and state

value
:   3

attribute-set
:   datapath

do
:   **request**
    :   attributes
        :   [`name`]

    **reply**
    :   attributes
        :   [`name`, `upcall-pid`, `stats`, `megaflow-stats`, `user-features`, `masks-cache-size`, `per-cpu-pids`]

dump
:   **request**
    :   attributes
        :   [`name`]

    **reply**
    :   attributes
        :   [`name`, `upcall-pid`, `stats`, `megaflow-stats`, `user-features`, `masks-cache-size`, `per-cpu-pids`]

### [new](ovs_datapath.md#id5)

Create new OVS data path

value
:   1

attribute-set
:   datapath

do
:   **request**
    :   attributes
        :   [`name`, `upcall-pid`, `user-features`]

### [del](ovs_datapath.md#id6)

Delete existing OVS data path

value
:   2

attribute-set
:   datapath

do
:   **request**
    :   attributes
        :   [`name`]

## [Multicast groups](ovs_datapath.md#id7)

- ovs_datapath

## [Definitions](ovs_datapath.md#id8)

### [ovs-header](ovs_datapath.md#id9)

type
:   struct

members
:   dp-ifindex

### [user-features](ovs_datapath.md#id10)

type
:   flags

name-prefix
:   ovs-dp-f-

enum-name
:   None

entries
:   unaligned
    :   Allow last Netlink attribute to be unaligned

    vport-pids
    :   Allow datapath to associate multiple Netlink PIDs to each vport

    tc-recirc-sharing
    :   Allow tc offload recirc sharing

    dispatch-upcall-per-cpu
    :   Allow per-cpu dispatch of upcalls

### [datapath-stats](ovs_datapath.md#id11)

enum-name
:   ovs-dp-stats

type
:   struct

members
:   n-hit

    n-missed

    n-lost

    n-flows

### [megaflow-stats](ovs_datapath.md#id12)

enum-name
:   ovs-dp-megaflow-stats

type
:   struct

members
:   n-mask-hit

    n-masks

    padding

    n-cache-hit

    pad1

## [Attribute sets](ovs_datapath.md#id13)

### [datapath](ovs_datapath.md#id14)

#### [name (`string`)](ovs_datapath.md#id15)

#### [upcall-pid (`u32`)](ovs_datapath.md#id16)

doc
:   upcall pid

#### [stats (`binary`)](ovs_datapath.md#id17)

struct
:   datapath-stats

#### [megaflow-stats (`binary`)](ovs_datapath.md#id18)

struct
:   megaflow-stats

#### [user-features (`u32`)](ovs_datapath.md#id19)

enum
:   user-features

enum-as-flags
:   True

#### [pad (`unused`)](ovs_datapath.md#id20)

#### [masks-cache-size (`u32`)](ovs_datapath.md#id21)

#### [per-cpu-pids (`binary`)](ovs_datapath.md#id22)

sub-type
:   u32

#### [ifindex (`u32`)](ovs_datapath.md#id23)
