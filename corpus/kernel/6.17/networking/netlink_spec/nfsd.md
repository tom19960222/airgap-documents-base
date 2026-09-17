---
collection: kernel
version: "6.17"
title: "Family nfsd netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/nfsd.html
fetched_at: 2026-09-16T16:40:51+00:00
---
# [Family `nfsd` netlink specification](nfsd.md#id1)

Contents

- [Family `nfsd` netlink specification](nfsd.md#family-nfsd-netlink-specification)

  - [Summary](nfsd.md#summary)
  - [Operations](nfsd.md#operations)

    - [rpc-status-get](nfsd.md#rpc-status-get)
    - [threads-set](nfsd.md#threads-set)
    - [threads-get](nfsd.md#threads-get)
    - [version-set](nfsd.md#version-set)
    - [version-get](nfsd.md#version-get)
    - [listener-set](nfsd.md#listener-set)
    - [listener-get](nfsd.md#listener-get)
    - [pool-mode-set](nfsd.md#pool-mode-set)
    - [pool-mode-get](nfsd.md#pool-mode-get)
  - [Attribute sets](nfsd.md#attribute-sets)

    - [rpc-status](nfsd.md#rpc-status)
    - [server](nfsd.md#server)
    - [version](nfsd.md#version)
    - [server-proto](nfsd.md#server-proto)
    - [sock](nfsd.md#sock)
    - [server-sock](nfsd.md#server-sock)
    - [pool-mode](nfsd.md#pool-mode)

## [Summary](nfsd.md#id2)

NFSD configuration over generic netlink.

## [Operations](nfsd.md#id3)

### [rpc-status-get](nfsd.md#id4)

dump pending nfsd rpc

attribute-set:
:   [rpc-status](nfsd.md#nfsd-attribute-set-rpc-status)

dump:
:   **reply**
    :   attributes:
        :   [`xid`, `flags`, `prog`, `version`, `proc`, `service-time`, `saddr4`, `daddr4`, `saddr6`, `daddr6`, `sport`, `dport`, `compound-ops`]

### [threads-set](nfsd.md#id5)

set the number of running threads

attribute-set:
:   [server](nfsd.md#nfsd-attribute-set-server)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`threads`, `gracetime`, `leasetime`, `scope`]

### [threads-get](nfsd.md#id6)

get the number of running threads

attribute-set:
:   [server](nfsd.md#nfsd-attribute-set-server)

do:
:   **reply**
    :   attributes:
        :   [`threads`, `gracetime`, `leasetime`, `scope`]

### [version-set](nfsd.md#id7)

set nfs enabled versions

attribute-set:
:   [server-proto](nfsd.md#nfsd-attribute-set-server-proto)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`version`]

### [version-get](nfsd.md#id8)

get nfs enabled versions

attribute-set:
:   [server-proto](nfsd.md#nfsd-attribute-set-server-proto)

do:
:   **reply**
    :   attributes:
        :   [`version`]

### [listener-set](nfsd.md#id9)

set nfs running sockets

attribute-set:
:   [server-sock](nfsd.md#nfsd-attribute-set-server-sock)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`addr`]

### [listener-get](nfsd.md#id10)

get nfs running listeners

attribute-set:
:   [server-sock](nfsd.md#nfsd-attribute-set-server-sock)

do:
:   **reply**
    :   attributes:
        :   [`addr`]

### [pool-mode-set](nfsd.md#id11)

set the current server pool-mode

attribute-set:
:   [pool-mode](nfsd.md#nfsd-attribute-set-pool-mode)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`mode`]

### [pool-mode-get](nfsd.md#id12)

get info about server pool-mode

attribute-set:
:   [pool-mode](nfsd.md#nfsd-attribute-set-pool-mode)

do:
:   **reply**
    :   attributes:
        :   [`mode`, `npools`]

## [Attribute sets](nfsd.md#id13)

### [rpc-status](nfsd.md#id14)

#### xid (`u32`)

byte-order:
:   big-endian

#### flags (`u32`)

#### prog (`u32`)

#### version (`u8`)

#### proc (`u32`)

#### service-time (`s64`)

#### pad (`pad`)

#### saddr4 (`u32`)

byte-order:
:   big-endian

display-hint:
:   ipv4

#### daddr4 (`u32`)

byte-order:
:   big-endian

display-hint:
:   ipv4

#### saddr6 (`binary`)

display-hint:
:   ipv6

#### daddr6 (`binary`)

display-hint:
:   ipv6

#### sport (`u16`)

byte-order:
:   big-endian

#### dport (`u16`)

byte-order:
:   big-endian

#### compound-ops (`u32`)

multi-attr:
:   True

### [server](nfsd.md#id15)

#### threads (`u32`)

multi-attr:
:   True

#### gracetime (`u32`)

#### leasetime (`u32`)

#### scope (`string`)

### [version](nfsd.md#id16)

#### major (`u32`)

#### minor (`u32`)

#### enabled (`flag`)

### [server-proto](nfsd.md#id17)

#### version (`nest`)

nested-attributes:
:   [version](nfsd.md#nfsd-attribute-set-version)

multi-attr:
:   True

### [sock](nfsd.md#id18)

#### addr (`binary`)

#### transport-name (`string`)

### [server-sock](nfsd.md#id19)

#### addr (`nest`)

nested-attributes:
:   [sock](nfsd.md#nfsd-attribute-set-sock)

multi-attr:
:   True

### [pool-mode](nfsd.md#id20)

#### mode (`string`)

#### npools (`u32`)
