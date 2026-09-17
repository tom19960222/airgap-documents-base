---
collection: kernel
version: "6.17"
title: "Family handshake netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/handshake.html
fetched_at: 2026-09-16T16:40:47+00:00
---
# [Family `handshake` netlink specification](handshake.md#id4)

Contents

- [Family `handshake` netlink specification](handshake.md#family-handshake-netlink-specification)

  - [Summary](handshake.md#summary)
  - [Operations](handshake.md#operations)

    - [ready](handshake.md#ready)
    - [accept](handshake.md#accept)
    - [done](handshake.md#done)
  - [Multicast groups](handshake.md#multicast-groups)
  - [Definitions](handshake.md#definitions)

    - [handler-class](handshake.md#handler-class)
    - [msg-type](handshake.md#msg-type)
    - [auth](handshake.md#auth)
  - [Attribute sets](handshake.md#attribute-sets)

    - [x509](handshake.md#x509)
    - [accept](handshake.md#handshake-attribute-set-accept)
    - [done](handshake.md#handshake-attribute-set-done)

## [Summary](handshake.md#id5)

Netlink protocol to request a transport layer security handshake.

## [Operations](handshake.md#id6)

### [ready](handshake.md#id7)

Notify handlers that a new handshake request is waiting

notify:
:   accept

### [accept](handshake.md#id8)

Handler retrieves next queued handshake request

attribute-set:
:   [accept](handshake.md#handshake-attribute-set-accept)

flags:
:   [`admin-perm`]

do:
:   **request**
    :   attributes:
        :   [`handler-class`]

    **reply**
    :   attributes:
        :   [`sockfd`, `message-type`, `timeout`, `auth-mode`, `peer-identity`, `certificate`, `peername`, `keyring`]

### [done](handshake.md#id9)

Handler reports handshake completion

attribute-set:
:   [done](handshake.md#handshake-attribute-set-done)

do:
:   **request**
    :   attributes:
        :   [`status`, `sockfd`, `remote-auth`]

## [Multicast groups](handshake.md#id10)

- none
- tlshd

## [Definitions](handshake.md#id11)

### [handler-class](handshake.md#id12)

type:
:   enum

value-start:
:   0

entries:
:   - `none`
    - `tlshd`
    - `max`

### [msg-type](handshake.md#id13)

type:
:   enum

value-start:
:   0

entries:
:   - `unspec`
    - `clienthello`
    - `serverhello`

### [auth](handshake.md#id14)

type:
:   enum

value-start:
:   0

entries:
:   - `unspec`
    - `unauth`
    - `psk`
    - `x509`

## [Attribute sets](handshake.md#id15)

### [x509](handshake.md#id16)

#### cert (`s32`)

#### privkey (`s32`)

### [accept](handshake.md#id17)

#### sockfd (`s32`)

#### handler-class (`u32`)

enum:
:   [handler-class](handshake.md#handshake-definition-handler-class)

#### message-type (`u32`)

enum:
:   [msg-type](handshake.md#handshake-definition-msg-type)

#### timeout (`u32`)

#### auth-mode (`u32`)

enum:
:   [auth](handshake.md#handshake-definition-auth)

#### peer-identity (`u32`)

multi-attr:
:   True

#### certificate (`nest`)

nested-attributes:
:   [x509](handshake.md#handshake-attribute-set-x509)

multi-attr:
:   True

#### peername (`string`)

#### keyring (`u32`)

### [done](handshake.md#id18)

#### status (`u32`)

#### sockfd (`s32`)

#### remote-auth (`u32`)

multi-attr:
:   True
