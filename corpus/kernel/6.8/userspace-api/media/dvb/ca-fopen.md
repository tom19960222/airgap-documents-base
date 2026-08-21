---
collection: kernel
version: "6.8"
title: "4.2.1. Digital TV CA open()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-fopen.html
fetched_at: 2026-08-21T03:39:09+00:00
---
# 4.2.1. Digital TV CA open()

## 4.2.1.1. Name

Digital TV CA [`open()`](ca-fopen.md#c.DTV.ca.open "DTV.ca.open")

## 4.2.1.2. Synopsis

int open(const char \*name, int flags)

## 4.2.1.3. Arguments

`name`
:   Name of specific Digital TV CA device.

`flags`
:   A bit-wise OR of the following flags:

|  |  |
| --- | --- |
| `O_RDONLY` | read-only access |
| `O_RDWR` | read/write access |
| `O_NONBLOCK` | open in non-blocking mode (blocking mode is the default) |

## 4.2.1.4. Description

This system call opens a named ca device (e.g. `/dev/dvb/adapter?/ca?`)
for subsequent use.

When an `open()` call has succeeded, the device will be ready for use. The
significance of blocking or non-blocking mode is described in the
documentation for functions where there is a difference. It does not
affect the semantics of the `open()` call itself. A device opened in
blocking mode can later be put into non-blocking mode (and vice versa)
using the `F_SETFL` command of the `fcntl` system call. This is a
standard system call, documented in the Linux manual page for fcntl.
Only one user can open the CA Device in `O_RDWR` mode. All other
attempts to open the device in this mode will fail, and an error code
will be returned.

## 4.2.1.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
