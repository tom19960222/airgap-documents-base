---
collection: kernel
version: "6.8"
title: "6.5.2. LIRC write()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-write.html
fetched_at: 2026-08-21T03:40:15+00:00
---
# 6.5.2. LIRC write()

## 6.5.2.1. Name

lirc-write - Write to a LIRC device

## 6.5.2.2. Synopsis

```c
#include <unistd.h>
```

ssize_t write(int fd, void \*buf, size_t count)

## 6.5.2.3. Arguments

`fd`
:   File descriptor returned by `open()`.

`buf`
:   Buffer with data to be written

`count`
:   Number of bytes at the buffer

## 6.5.2.4. Description

[`write()`](lirc-write.md#c.RC.write "write") writes up to `count` bytes to the device
referenced by the file descriptor `fd` from the buffer starting at
`buf`.

The exact format of the data depends on what mode a driver is in, use
[ioctl LIRC_GET_FEATURES](lirc-get-features.md#lirc-get-features) to get the supported modes and use
[ioctls LIRC_GET_SEND_MODE and LIRC_SET_SEND_MODE](lirc-get-send-mode.md#lirc-set-send-mode) set the mode.

When in [LIRC_MODE_PULSE](lirc-dev-intro.md#lirc-mode-pulse) mode, the data written to
the chardev is a pulse/space sequence of integer values. Pulses and spaces
are only marked implicitly by their position. The data must start and end
with a pulse, therefore, the data must always include an uneven number of
samples. The write function blocks until the data has been transmitted
by the hardware. If more data is provided than the hardware can send, the
driver returns `EINVAL`.

When in [LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) mode, one
`struct lirc_scancode` must be written to the chardev at a time, else
`EINVAL` is returned. Set the desired scancode in the `scancode` member,
and the [IR protocol](rc-protos.md#remote-controllers-protocols) in the
[`rc_proto`](lirc-dev-intro.md#c.rc_proto "rc_proto"): member. All other members must be
set to 0, else `EINVAL` is returned. If there is no protocol encoder
for the protocol or the scancode is not valid for the specified protocol,
`EINVAL` is returned. The write function blocks until the scancode
is transmitted by the hardware.

## 6.5.2.5. Return Value

On success, the number of bytes written is returned. It is not an error if
this number is smaller than the number of bytes requested, or the amount
of data required for one frame. On error, -1 is returned, and the `errno`
variable is set appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
