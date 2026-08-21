---
collection: kernel
version: "6.8"
title: "6.5.1. LIRC read()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/lirc-read.html
fetched_at: 2026-08-21T03:40:14+00:00
---
# 6.5.1. LIRC read()

## 6.5.1.1. Name

lirc-read - Read from a LIRC device

## 6.5.1.2. Synopsis

```c
#include <unistd.h>
```

ssize_t read(int fd, void \*buf, size_t count)

## 6.5.1.3. Arguments

`fd`
:   File descriptor returned by `open()`.

`buf`
:   Buffer to be filled

`count`
:   Max number of bytes to read

## 6.5.1.4. Description

[`read()`](lirc-read.md#c.RC.read "read") attempts to read up to `count` bytes from file
descriptor `fd` into the buffer starting at `buf`. If `count` is zero,
[`read()`](lirc-read.md#c.RC.read "read") returns zero and has no other results. If `count`
is greater than `SSIZE_MAX`, the result is unspecified.

The exact format of the data depends on what [LIRC modes](lirc-dev-intro.md#lirc-modes) a driver
uses. Use [ioctl LIRC_GET_FEATURES](lirc-get-features.md#lirc-get-features) to get the supported mode, and use
[ioctls LIRC_GET_REC_MODE and LIRC_SET_REC_MODE](lirc-get-rec-mode.md#lirc-set-rec-mode) set the current active mode.

The mode [LIRC_MODE_MODE2](lirc-dev-intro.md#lirc-mode-mode2) is for raw IR,
in which packets containing an unsigned int value describing an IR signal are
read from the chardev.

Alternatively, [LIRC_MODE_SCANCODE](lirc-dev-intro.md#lirc-mode-scancode) can be available,
in this mode scancodes which are either decoded by software decoders, or
by hardware decoders. The [`rc_proto`](lirc-dev-intro.md#c.rc_proto "rc_proto") member is set to the
[IR protocol](rc-protos.md#remote-controllers-protocols)
used for transmission, and `scancode` to the decoded scancode,
and the `keycode` set to the keycode or `KEY_RESERVED`.

## 6.5.1.5. Return Value

On success, the number of bytes read is returned. It is not an error if
this number is smaller than the number of bytes requested, or the amount
of data required for one frame. On error, -1 is returned, and the `errno`
variable is set appropriately.
