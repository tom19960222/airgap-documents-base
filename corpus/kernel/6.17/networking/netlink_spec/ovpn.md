---
collection: kernel
version: "6.17"
title: "Family ovpn netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/ovpn.html
fetched_at: 2026-09-16T16:40:53+00:00
---
# [Family `ovpn` netlink specification](ovpn.md#id28)

Contents

- [Family `ovpn` netlink specification](ovpn.md#family-ovpn-netlink-specification)

  - [Summary](ovpn.md#summary)
  - [Operations](ovpn.md#operations)

    - [peer-new](ovpn.md#peer-new)
    - [peer-set](ovpn.md#peer-set)
    - [peer-get](ovpn.md#peer-get)
    - [peer-del](ovpn.md#peer-del)
    - [peer-del-ntf](ovpn.md#peer-del-ntf)
    - [key-new](ovpn.md#key-new)
    - [key-get](ovpn.md#key-get)
    - [key-swap](ovpn.md#key-swap)
    - [key-swap-ntf](ovpn.md#key-swap-ntf)
    - [key-del](ovpn.md#key-del)
  - [Multicast groups](ovpn.md#multicast-groups)
  - [Definitions](ovpn.md#definitions)

    - [nonce-tail-size](ovpn.md#nonce-tail-size)
    - [cipher-alg](ovpn.md#cipher-alg)
    - [del-peer-reason](ovpn.md#del-peer-reason)
    - [key-slot](ovpn.md#key-slot)
  - [Attribute sets](ovpn.md#attribute-sets)

    - [peer](ovpn.md#peer)
    - [peer-new-input](ovpn.md#peer-new-input)
    - [peer-set-input](ovpn.md#peer-set-input)
    - [peer-del-input](ovpn.md#peer-del-input)
    - [keyconf](ovpn.md#keyconf)
    - [keydir](ovpn.md#keydir)
    - [keyconf-get](ovpn.md#keyconf-get)
    - [keyconf-swap-input](ovpn.md#keyconf-swap-input)
    - [keyconf-del-input](ovpn.md#keyconf-del-input)
    - [ovpn](ovpn.md#ovpn)
    - [ovpn-peer-new-input](ovpn.md#ovpn-peer-new-input)
    - [ovpn-peer-set-input](ovpn.md#ovpn-peer-set-input)
    - [ovpn-peer-del-input](ovpn.md#ovpn-peer-del-input)
    - [ovpn-keyconf-get](ovpn.md#ovpn-keyconf-get)
    - [ovpn-keyconf-swap-input](ovpn.md#ovpn-keyconf-swap-input)
    - [ovpn-keyconf-del-input](ovpn.md#ovpn-keyconf-del-input)

## [Summary](ovpn.md#id29)

Netlink protocol to control OpenVPN network devices

## [Operations](ovpn.md#id30)

### [peer-new](ovpn.md#id31)

Add a remote peer

attribute-set:
:   [ovpn-peer-new-input](ovpn.md#ovpn-attribute-set-ovpn-peer-new-input)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `peer`]

### [peer-set](ovpn.md#id32)

modify a remote peer

attribute-set:
:   [ovpn-peer-set-input](ovpn.md#ovpn-attribute-set-ovpn-peer-set-input)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `peer`]

### [peer-get](ovpn.md#id33)

Retrieve data about existing remote peers (or a specific one)

attribute-set:
:   [ovpn](ovpn.md#ovpn-attribute-set-ovpn)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `peer`]

    **reply**
    :   attributes:
        :   [`peer`]

dump:
:   **request**
    :   attributes:
        :   [`ifindex`]

    **reply**
    :   attributes:
        :   [`peer`]

### [peer-del](ovpn.md#id34)

Delete existing remote peer

attribute-set:
:   [ovpn-peer-del-input](ovpn.md#ovpn-attribute-set-ovpn-peer-del-input)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `peer`]

### [peer-del-ntf](ovpn.md#id35)

Notification about a peer being deleted

notify:
:   peer-get

mcgrp:
:   peers

### [key-new](ovpn.md#id36)

Add a cipher key for a specific peer

attribute-set:
:   [ovpn](ovpn.md#ovpn-attribute-set-ovpn)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `keyconf`]

### [key-get](ovpn.md#id37)

Retrieve non-sensitive data about peer key and cipher

attribute-set:
:   [ovpn-keyconf-get](ovpn.md#ovpn-attribute-set-ovpn-keyconf-get)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `keyconf`]

    **reply**
    :   attributes:
        :   [`keyconf`]

### [key-swap](ovpn.md#id38)

Swap primary and secondary session keys for a specific peer

attribute-set:
:   [ovpn-keyconf-swap-input](ovpn.md#ovpn-attribute-set-ovpn-keyconf-swap-input)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `keyconf`]

### [key-swap-ntf](ovpn.md#id39)

Notification about key having exhausted its IV space and requiring renegotiation

notify:
:   key-get

mcgrp:
:   peers

### [key-del](ovpn.md#id40)

Delete cipher key for a specific peer

attribute-set:
:   [ovpn-keyconf-del-input](ovpn.md#ovpn-attribute-set-ovpn-keyconf-del-input)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   ovpn-nl-pre-doit

    **post**
    :   ovpn-nl-post-doit

    **request**
    :   attributes:
        :   [`ifindex`, `keyconf`]

## [Multicast groups](ovpn.md#id41)

- peers

## [Definitions](ovpn.md#id42)

### [nonce-tail-size](ovpn.md#id43)

type:
:   const

value:
:   8

### [cipher-alg](ovpn.md#id44)

type:
:   enum

entries:
:   - `none`
    - `aes-gcm`
    - `chacha20-poly1305`

### [del-peer-reason](ovpn.md#id45)

type:
:   enum

entries:
:   - `teardown`
    - `userspace`
    - `expired`
    - `transport-error`
    - `transport-disconnect`

### [key-slot](ovpn.md#id46)

type:
:   enum

entries:
:   - `primary`
    - `secondary`

## [Attribute sets](ovpn.md#id47)

### [peer](ovpn.md#id48)

#### id (`u32`)

doc:
:   The unique ID of the peer in the device context. To be used to identify peers during operations for a specific device

#### remote-ipv4 (`u32`)

doc:
:   The remote IPv4 address of the peer

byte-order:
:   big-endian

display-hint:
:   ipv4

#### remote-ipv6 (`binary`)

doc:
:   The remote IPv6 address of the peer

display-hint:
:   ipv6

#### remote-ipv6-scope-id (`u32`)

doc:
:   The scope id of the remote IPv6 address of the peer (RFC2553)

#### remote-port (`u16`)

doc:
:   The remote port of the peer

byte-order:
:   big-endian

#### socket (`u32`)

doc:
:   The socket to be used to communicate with the peer

#### socket-netnsid (`s32`)

doc:
:   The ID of the netns the socket assigned to this peer lives in

#### vpn-ipv4 (`u32`)

doc:
:   The IPv4 address assigned to the peer by the server

byte-order:
:   big-endian

display-hint:
:   ipv4

#### vpn-ipv6 (`binary`)

doc:
:   The IPv6 address assigned to the peer by the server

display-hint:
:   ipv6

#### local-ipv4 (`u32`)

doc:
:   The local IPv4 to be used to send packets to the peer (UDP only)

byte-order:
:   big-endian

display-hint:
:   ipv4

#### local-ipv6 (`binary`)

doc:
:   The local IPv6 to be used to send packets to the peer (UDP only)

display-hint:
:   ipv6

#### local-port (`u16`)

doc:
:   The local port to be used to send packets to the peer (UDP only)

byte-order:
:   big-endian

#### keepalive-interval (`u32`)

doc:
:   The number of seconds after which a keep alive message is sent to the peer

#### keepalive-timeout (`u32`)

doc:
:   The number of seconds from the last activity after which the peer is assumed dead

#### del-reason (`u32`)

doc:
:   The reason why a peer was deleted

enum:
:   [del-peer-reason](ovpn.md#ovpn-definition-del-peer-reason)

#### vpn-rx-bytes (`uint`)

doc:
:   Number of bytes received over the tunnel

#### vpn-tx-bytes (`uint`)

doc:
:   Number of bytes transmitted over the tunnel

#### vpn-rx-packets (`uint`)

doc:
:   Number of packets received over the tunnel

#### vpn-tx-packets (`uint`)

doc:
:   Number of packets transmitted over the tunnel

#### link-rx-bytes (`uint`)

doc:
:   Number of bytes received at the transport level

#### link-tx-bytes (`uint`)

doc:
:   Number of bytes transmitted at the transport level

#### link-rx-packets (`uint`)

doc:
:   Number of packets received at the transport level

#### link-tx-packets (`uint`)

doc:
:   Number of packets transmitted at the transport level

### [peer-new-input](ovpn.md#id49)

#### id

#### remote-ipv4

#### remote-ipv6

#### remote-ipv6-scope-id

#### remote-port

#### socket

#### vpn-ipv4

#### vpn-ipv6

#### local-ipv4

#### local-ipv6

#### keepalive-interval

#### keepalive-timeout

### [peer-set-input](ovpn.md#id50)

#### id

#### remote-ipv4

#### remote-ipv6

#### remote-ipv6-scope-id

#### remote-port

#### vpn-ipv4

#### vpn-ipv6

#### local-ipv4

#### local-ipv6

#### keepalive-interval

#### keepalive-timeout

### [peer-del-input](ovpn.md#id51)

#### id

### [keyconf](ovpn.md#id52)

#### peer-id (`u32`)

doc:
:   The unique ID of the peer in the device context. To be used to identify peers during key operations

#### slot (`u32`)

doc:
:   The slot where the key should be stored

enum:
:   [key-slot](ovpn.md#ovpn-definition-key-slot)

#### key-id (`u32`)

doc:
:   The unique ID of the key in the peer context. Used to fetch the correct key upon decryption

#### cipher-alg (`u32`)

doc:
:   The cipher to be used when communicating with the peer

enum:
:   [cipher-alg](ovpn.md#ovpn-definition-cipher-alg)

#### encrypt-dir (`nest`)

doc:
:   Key material for encrypt direction

nested-attributes:
:   [keydir](ovpn.md#ovpn-attribute-set-keydir)

#### decrypt-dir (`nest`)

doc:
:   Key material for decrypt direction

nested-attributes:
:   [keydir](ovpn.md#ovpn-attribute-set-keydir)

### [keydir](ovpn.md#id53)

#### cipher-key (`binary`)

doc:
:   The actual key to be used by the cipher

#### nonce-tail (`binary`)

doc:
:   Random nonce to be concatenated to the packet ID, in order to obtain the actual cipher IV

### [keyconf-get](ovpn.md#id54)

#### peer-id

#### slot

#### key-id

#### cipher-alg

### [keyconf-swap-input](ovpn.md#id55)

#### peer-id

### [keyconf-del-input](ovpn.md#id56)

#### peer-id

#### slot

### [ovpn](ovpn.md#id57)

#### ifindex (`u32`)

doc:
:   Index of the ovpn interface to operate on

#### peer (`nest`)

doc:
:   The peer object containing the attributed of interest for the specific operation

nested-attributes:
:   [peer](ovpn.md#ovpn-attribute-set-peer)

#### keyconf (`nest`)

doc:
:   Peer specific cipher configuration

nested-attributes:
:   [keyconf](ovpn.md#ovpn-attribute-set-keyconf)

### [ovpn-peer-new-input](ovpn.md#id58)

#### ifindex

#### peer

nested-attributes:
:   [peer-new-input](ovpn.md#ovpn-attribute-set-peer-new-input)

### [ovpn-peer-set-input](ovpn.md#id59)

#### ifindex

#### peer

nested-attributes:
:   [peer-set-input](ovpn.md#ovpn-attribute-set-peer-set-input)

### [ovpn-peer-del-input](ovpn.md#id60)

#### ifindex

#### peer

nested-attributes:
:   [peer-del-input](ovpn.md#ovpn-attribute-set-peer-del-input)

### [ovpn-keyconf-get](ovpn.md#id61)

#### ifindex

#### keyconf

nested-attributes:
:   [keyconf-get](ovpn.md#ovpn-attribute-set-keyconf-get)

### [ovpn-keyconf-swap-input](ovpn.md#id62)

#### ifindex

#### keyconf

nested-attributes:
:   [keyconf-swap-input](ovpn.md#ovpn-attribute-set-keyconf-swap-input)

### [ovpn-keyconf-del-input](ovpn.md#id63)

#### ifindex

#### keyconf

nested-attributes:
:   [keyconf-del-input](ovpn.md#ovpn-attribute-set-keyconf-del-input)
