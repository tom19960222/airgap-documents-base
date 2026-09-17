---
collection: kernel
version: "6.17"
title: "Family lockd netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/lockd.html
fetched_at: 2026-09-16T16:40:48+00:00
---
# [Family `lockd` netlink specification](lockd.md#id1)

Contents

- [Family `lockd` netlink specification](lockd.md#family-lockd-netlink-specification)

  - [Summary](lockd.md#summary)
  - [Operations](lockd.md#operations)

    - [server-set](lockd.md#server-set)
    - [server-get](lockd.md#server-get)
  - [Attribute sets](lockd.md#attribute-sets)

    - [server](lockd.md#server)

## [Summary](lockd.md#id2)

lockd configuration over generic netlink

## [Operations](lockd.md#id3)

### [server-set](lockd.md#id4)

set the lockd server parameters

attribute-set:
:   [server](lockd.md#lockd-attribute-set-server)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`gracetime`, `tcp-port`, `udp-port`]

### [server-get](lockd.md#id5)

get the lockd server parameters

attribute-set:
:   [server](lockd.md#lockd-attribute-set-server)

do:
:   **reply**
    :   attributes:
        :   [`gracetime`, `tcp-port`, `udp-port`]

## [Attribute sets](lockd.md#id6)

### [server](lockd.md#id7)

#### gracetime (`u32`)

#### tcp-port (`u16`)

#### udp-port (`u16`)
