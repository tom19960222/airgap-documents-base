---
collection: qemu
version: "11.1.0"
title: "Vhost-user-gpu Protocol"
source_url: https://www.qemu.org/docs/master/interop/vhost-user-gpu.html
fetched_at: 2026-08-21T03:22:28+00:00
---
# [Vhost-user-gpu Protocol](vhost-user-gpu.md#id1)

Table of Contents

- [Vhost-user-gpu Protocol](vhost-user-gpu.md#vhost-user-gpu-protocol)

  - [Introduction](vhost-user-gpu.md#introduction)
  - [Wire format](vhost-user-gpu.md#wire-format)

    - [Header](vhost-user-gpu.md#header)
    - [Payload types](vhost-user-gpu.md#payload-types)

      - [VhostUserGpuCursorPos](vhost-user-gpu.md#vhostusergpucursorpos)
      - [VhostUserGpuCursorUpdate](vhost-user-gpu.md#vhostusergpucursorupdate)
      - [VhostUserGpuScanout](vhost-user-gpu.md#vhostusergpuscanout)
      - [VhostUserGpuUpdate](vhost-user-gpu.md#vhostusergpuupdate)
      - [VhostUserGpuDMABUFScanout](vhost-user-gpu.md#vhostusergpudmabufscanout)
      - [VhostUserGpuEdidRequest](vhost-user-gpu.md#vhostusergpuedidrequest)
      - [VhostUserGpuDMABUFScanout2](vhost-user-gpu.md#vhostusergpudmabufscanout2)
    - [C structure](vhost-user-gpu.md#c-structure)
    - [Protocol features](vhost-user-gpu.md#protocol-features)
  - [Communication](vhost-user-gpu.md#communication)

    - [Message types](vhost-user-gpu.md#message-types)

## [Introduction](vhost-user-gpu.md#id2)

The vhost-user-gpu protocol is aiming at sharing the rendering result
of a virtio-gpu, done from a vhost-user back-end process to a vhost-user
front-end process (such as QEMU). It bears a resemblance to a display
server protocol, if you consider QEMU as the display server and the
back-end as the client, but in a very limited way. Typically, it will
work by setting a scanout/display configuration, before sending flush
events for the display updates. It will also update the cursor shape
and position.

The protocol is sent over a UNIX domain stream socket, since it uses
socket ancillary data to share opened file descriptors (DMABUF fds or
shared memory). The socket is usually obtained via
`VHOST_USER_GPU_SET_SOCKET`.

Requests are sent by the *back-end*, and the optional replies by the
*front-end*.

## [Wire format](vhost-user-gpu.md#id3)

Unless specified differently, numbers are in the machine native byte
order.

A vhost-user-gpu message (request and reply) consists of 3 header
fields and a payload.

|  |  |  |  |
| --- | --- | --- | --- |
| request | flags | size | payload |

### [Header](vhost-user-gpu.md#id4)

request:
:   `u32`, type of the request

flags:
:   `u32`, 32-bit bit field:

    - Bit 2 is the reply flag - needs to be set on each reply

size:
:   `u32`, size of the payload

### [Payload types](vhost-user-gpu.md#id5)

Depending on the request type, **payload** can be:

#### [VhostUserGpuCursorPos](vhost-user-gpu.md#id6)

|  |  |  |
| --- | --- | --- |
| scanout-id | x | y |

scanout-id:
:   `u32`, the scanout where the cursor is located

x/y:
:   `u32`, the cursor position

#### [VhostUserGpuCursorUpdate](vhost-user-gpu.md#id7)

|  |  |  |  |
| --- | --- | --- | --- |
| pos | hot_x | hot_y | cursor |

pos:
:   a `VhostUserGpuCursorPos`, the cursor location

hot_x/hot_y:
:   `u32`, the cursor hot location

cursor:
:   `[u32; 64 * 64]`, 64x64 RGBA cursor data (PIXMAN_a8r8g8b8 format)

#### [VhostUserGpuScanout](vhost-user-gpu.md#id8)

|  |  |  |
| --- | --- | --- |
| scanout-id | w | h |

scanout-id:
:   `u32`, the scanout configuration to set

w/h:
:   `u32`, the scanout width/height size

#### [VhostUserGpuUpdate](vhost-user-gpu.md#id9)

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| scanout-id | x | y | w | h | data |

scanout-id:
:   `u32`, the scanout content to update

x/y/w/h:
:   `u32`, region of the update

data:
:   RGB data (PIXMAN_x8r8g8b8 format)

#### [VhostUserGpuDMABUFScanout](vhost-user-gpu.md#id10)

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| scanout-id | x | y | w | h | fdw | fwh | stride | flags | fourcc |

scanout-id:
:   `u32`, the scanout configuration to set

x/y:
:   `u32`, the location of the scanout within the DMABUF

w/h:
:   `u32`, the scanout width/height size

fdw/fdh/stride/flags:
:   `u32`, the DMABUF width/height/stride/flags

fourcc:
:   `i32`, the DMABUF fourcc

#### [VhostUserGpuEdidRequest](vhost-user-gpu.md#id11)

|  |
| --- |
| scanout-id |

scanout-id:
:   `u32`, the scanout to get edid from

#### [VhostUserGpuDMABUFScanout2](vhost-user-gpu.md#id12)

|  |  |
| --- | --- |
| dmabuf_scanout | modifier |

dmabuf_scanout:
:   `VhostUserGpuDMABUFScanout`, filled as described in the
    VhostUserGpuDMABUFScanout structure.

modifier:
:   `u64`, the DMABUF modifiers

### [C structure](vhost-user-gpu.md#id13)

In QEMU the vhost-user-gpu message is implemented with the following struct:

```c
typedef struct VhostUserGpuMsg {
    uint32_t request; /* VhostUserGpuRequest */
    uint32_t flags;
    uint32_t size; /* the following payload size */
    union {
        VhostUserGpuCursorPos cursor_pos;
        VhostUserGpuCursorUpdate cursor_update;
        VhostUserGpuScanout scanout;
        VhostUserGpuUpdate update;
        VhostUserGpuDMABUFScanout dmabuf_scanout;
        VhostUserGpuEdidRequest edid_req;
        struct virtio_gpu_resp_edid resp_edid;
        struct virtio_gpu_resp_display_info display_info;
        uint64_t u64;
    } payload;
} QEMU_PACKED VhostUserGpuMsg;
```

### [Protocol features](vhost-user-gpu.md#id14)

```c
#define VHOST_USER_GPU_PROTOCOL_F_EDID    0
#define VHOST_USER_GPU_PROTOCOL_F_DMABUF2 1
```

New messages and communication changes are negotiated thanks to the
`VHOST_USER_GPU_GET_PROTOCOL_FEATURES` and
`VHOST_USER_GPU_SET_PROTOCOL_FEATURES` requests.

## [Communication](vhost-user-gpu.md#id15)

### [Message types](vhost-user-gpu.md#id16)

`VHOST_USER_GPU_GET_PROTOCOL_FEATURES`
:   id:
    :   1

    request payload:
    :   N/A

    reply payload:
    :   `u64`

    Get the supported protocol features bitmask.

`VHOST_USER_GPU_SET_PROTOCOL_FEATURES`
:   id:
    :   2

    request payload:
    :   `u64`

    reply payload:
    :   N/A

    Enable protocol features using a bitmask.

`VHOST_USER_GPU_GET_DISPLAY_INFO`
:   id:
    :   3

    request payload:
    :   N/A

    reply payload:
    :   `struct virtio_gpu_resp_display_info` (from virtio specification)

    Get the preferred display configuration.

`VHOST_USER_GPU_CURSOR_POS`
:   id:
    :   4

    request payload:
    :   `VhostUserGpuCursorPos`

    reply payload:
    :   N/A

    Set/show the cursor position.

`VHOST_USER_GPU_CURSOR_POS_HIDE`
:   id:
    :   5

    request payload:
    :   `VhostUserGpuCursorPos`

    reply payload:
    :   N/A

    Set/hide the cursor.

`VHOST_USER_GPU_CURSOR_UPDATE`
:   id:
    :   6

    request payload:
    :   `VhostUserGpuCursorUpdate`

    reply payload:
    :   N/A

    Update the cursor shape and location.

`VHOST_USER_GPU_SCANOUT`
:   id:
    :   7

    request payload:
    :   `VhostUserGpuScanout`

    reply payload:
    :   N/A

    Set the scanout resolution. To disable a scanout, the dimensions
    width/height are set to 0.

`VHOST_USER_GPU_UPDATE`
:   id:
    :   8

    request payload:
    :   `VhostUserGpuUpdate`

    reply payload:
    :   N/A

    Update the scanout content. The data payload contains the graphical bits.
    The display should be flushed and presented.

`VHOST_USER_GPU_DMABUF_SCANOUT`
:   id:
    :   9

    request payload:
    :   `VhostUserGpuDMABUFScanout`

    reply payload:
    :   N/A

    Set the scanout resolution/configuration, and share a DMABUF file
    descriptor for the scanout content, which is passed as ancillary
    data. To disable a scanout, the dimensions width/height are set
    to 0, there is no file descriptor passed.

`VHOST_USER_GPU_DMABUF_UPDATE`
:   id:
    :   10

    request payload:
    :   `VhostUserGpuUpdate`

    reply payload:
    :   empty payload

    The display should be flushed and presented according to updated
    region from `VhostUserGpuUpdate`.

    Note: there is no data payload, since the scanout is shared thanks
    to DMABUF, that must have been set previously with
    `VHOST_USER_GPU_DMABUF_SCANOUT`.

`VHOST_USER_GPU_GET_EDID`
:   id:
    :   11

    request payload:
    :   `struct VhostUserGpuEdidRequest`

    reply payload:
    :   `struct virtio_gpu_resp_edid` (from virtio specification)

    Retrieve the EDID data for a given scanout.
    This message requires the `VHOST_USER_GPU_PROTOCOL_F_EDID` protocol
    feature to be supported.

`VHOST_USER_GPU_DMABUF_SCANOUT2`
:   id:
    :   12

    request payload:
    :   `VhostUserGpuDMABUFScanout2`

    reply payload:
    :   N/A

    Same as VHOST_USER_GPU_DMABUF_SCANOUT, but also sends the dmabuf modifiers
    appended to the message, which were not provided in the other message.
    This message requires the `VHOST_USER_GPU_PROTOCOL_F_DMABUF2` protocol
    feature to be supported.
