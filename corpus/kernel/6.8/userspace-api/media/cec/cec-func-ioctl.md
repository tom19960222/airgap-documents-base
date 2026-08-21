---
collection: kernel
version: "6.8"
title: "2.3. cec ioctl()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-func-ioctl.html
fetched_at: 2026-08-21T03:58:07+00:00
---
# 2.3. cec ioctl()

## 2.3.1. Name

cec-ioctl - Control a cec device

## 2.3.2. Synopsis

```c
#include <sys/ioctl.h>
```

`int ioctl(int fd, int request, void *argp)`

## 2.3.3. Arguments

`fd`
:   File descriptor returned by [`open()`](cec-func-open.md#c.CEC.open "open").

`request`
:   CEC ioctl request code as defined in the cec.h header file, for
    example [CEC_ADAP_G_CAPS](cec-ioc-adap-g-caps.md#cec-adap-g-caps).

`argp`
:   Pointer to a request-specific structure.

## 2.3.4. Description

The `ioctl()` function manipulates cec device parameters. The
argument `fd` must be an open file descriptor.

The ioctl `request` code specifies the cec function to be called. It
has encoded in it whether the argument is an input, output or read/write
parameter, and the size of the argument `argp` in bytes.

Macros and structures definitions specifying cec ioctl requests and
their parameters are located in the cec.h header file. All cec ioctl
requests, their respective function and parameters are specified in
[Function Reference](cec-funcs.md#cec-user-func).

## 2.3.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

Request-specific error codes are listed in the individual requests
descriptions.

When an ioctl that takes an output or read/write parameter fails, the
parameter remains unmodified.
