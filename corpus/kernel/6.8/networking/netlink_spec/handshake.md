---
collection: kernel
version: "6.8"
title: "Family handshake netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/handshake.html
fetched_at: 2026-08-21T03:49:16+00:00
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

      - [cert (`s32`)](handshake.md#cert-s32)
      - [privkey (`s32`)](handshake.md#privkey-s32)
    - [accept](handshake.md#id1)

      - [sockfd (`s32`)](handshake.md#sockfd-s32)
      - [handler-class (`u32`)](handshake.md#handler-class-u32)
      - [message-type (`u32`)](handshake.md#message-type-u32)
      - [timeout (`u32`)](handshake.md#timeout-u32)
      - [auth-mode (`u32`)](handshake.md#auth-mode-u32)
      - [peer-identity (`u32`)](handshake.md#peer-identity-u32)
      - [certificate (`nest`)](handshake.md#certificate-nest)
      - [peername (`string`)](handshake.md#peername-string)
    - [done](handshake.md#id2)

      - [status (`u32`)](handshake.md#status-u32)
      - [sockfd (`s32`)](handshake.md#id3)
      - [remote-auth (`u32`)](handshake.md#remote-auth-u32)

## [Summary](handshake.md#id5)

Netlink protocol to request a transport layer security handshake.

## [Operations](handshake.md#id6)

### [ready](handshake.md#id7)

Notify handlers that a new handshake request is waiting

notify
:   accept

### [accept](handshake.md#id8)

Handler retrieves next queued handshake request

attribute-set
:   accept

flags
:   ['admin-perm']

do
:   **request**
    :   attributes
        :   [`handler-class`]

    **reply**
    :   attributes
        :   [`sockfd`, `message-type`, `timeout`, `auth-mode`, `peer-identity`, `certificate`, `peername`]

### [done](handshake.md#id9)

Handler reports handshake completion

attribute-set
:   done

do
:   **request**
    :   attributes
        :   [`status`, `sockfd`, `remote-auth`]

## [Multicast groups](handshake.md#id10)

- none
- tlshd

## [Definitions](handshake.md#id11)

### [handler-class](handshake.md#id12)

type
:   enum

value-start
:   0

entries
:   - `none`
    - `tlshd`
    - `max`

### [msg-type](handshake.md#id13)

type
:   enum

value-start
:   0

entries
:   - `unspec`
    - `clienthello`
    - `serverhello`

### [auth](handshake.md#id14)

type
:   enum

value-start
:   0

entries
:   - `unspec`
    - `unauth`
    - `psk`
    - `x509`

## [Attribute sets](handshake.md#id15)

### [x509](handshake.md#id16)

#### [cert (`s32`)](handshake.md#id17)

#### [privkey (`s32`)](handshake.md#id18)

### [accept](handshake.md#id19)

#### [sockfd (`s32`)](handshake.md#id20)

#### [handler-class (`u32`)](handshake.md#id21)

enum
:   handler-class

#### [message-type (`u32`)](handshake.md#id22)

enum
:   msg-type

#### [timeout (`u32`)](handshake.md#id23)

#### [auth-mode (`u32`)](handshake.md#id24)

enum
:   auth

#### [peer-identity (`u32`)](handshake.md#id25)

multi-attr
:   True

#### [certificate (`nest`)](handshake.md#id26)

nested-attributes
:   x509

multi-attr
:   True

#### [peername (`string`)](handshake.md#id27)

### [done](handshake.md#id28)

#### [status (`u32`)](handshake.md#id29)

#### [sockfd (`s32`)](handshake.md#id30)

#### [remote-auth (`u32`)](handshake.md#id31)

multi-attr
:   True
