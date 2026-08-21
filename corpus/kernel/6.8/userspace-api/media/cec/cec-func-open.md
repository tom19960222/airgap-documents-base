---
collection: kernel
version: "6.8"
title: "2.1. cec open()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-func-open.html
fetched_at: 2026-08-21T03:38:51+00:00
---
# 2.1. cec open()

## 2.1.1. Name

cec-open - Open a cec device

## 2.1.2. Synopsis

```c
#include <fcntl.h>
```

int open(const char \*device_name, int flags)

## 2.1.3. Arguments

`device_name`
:   Device to be opened.

`flags`
:   Open flags. Access mode must be `O_RDWR`.

    When the `O_NONBLOCK` flag is given, the
    [CEC_RECEIVE](cec-ioc-receive.md#cec-receive) and [CEC_DQEVENT](cec-ioc-dqevent.md#cec-dqevent) ioctls
    will return the `EAGAIN` error code when no message or event is available, and
    ioctls [CEC_TRANSMIT](cec-ioc-receive.md#cec-transmit),
    [CEC_ADAP_S_PHYS_ADDR](cec-ioc-adap-g-phys-addr.md#cec-adap-s-phys-addr) and
    [CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md#cec-adap-s-log-addrs)
    all return 0.

    Other flags have no effect.

## 2.1.4. Description

To open a cec device applications call [`open()`](cec-func-open.md#c.CEC.open "open") with the
desired device name. The function has no side effects; the device
configuration remain unchanged.

When the device is opened in read-only mode, attempts to modify its
configuration will result in an error, and `errno` will be set to
EBADF.

## 2.1.5. Return Value

[`open()`](cec-func-open.md#c.CEC.open "open") returns the new file descriptor on success. On error,
-1 is returned, and `errno` is set appropriately. Possible error codes
include:

`EACCES`
:   The requested access to the file is not allowed.

`EMFILE`
:   The process already has the maximum number of files open.

`ENFILE`
:   The system limit on the total number of open files has been reached.

`ENOMEM`
:   Insufficient kernel memory was available.

`ENXIO`
:   No device corresponding to this device special file exists.
