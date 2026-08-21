---
collection: kernel
version: "6.8"
title: "7.68. V4L2 open()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/func-open.html
fetched_at: 2026-08-21T03:40:26+00:00
---
# 7.68. V4L2 open()

## 7.68.1. Name

v4l2-open - Open a V4L2 device

## 7.68.2. Synopsis

```c
#include <fcntl.h>
```

int open(const char \*device_name, int flags)

## 7.68.3. Arguments

`device_name`
:   Device to be opened.

`flags`
:   Open flags. Access mode must be `O_RDWR`. This is just a
    technicality, input devices still support only reading and output
    devices only writing.

    When the `O_NONBLOCK` flag is given, the [`read()`](func-read.md#c.V4L.read "read")
    function and the [VIDIOC_DQBUF](vidioc-qbuf.md#vidioc-qbuf) ioctl will
    return the `EAGAIN` error code when no data is available or no
    buffer is in the driver outgoing queue, otherwise these functions
    block until data becomes available. All V4L2 drivers exchanging data
    with applications must support the `O_NONBLOCK` flag.

    Other flags have no effect.

## 7.68.4. Description

To open a V4L2 device applications call [`open()`](func-open.md#c.V4L.open "open") with the
desired device name. This function has no side effects; all data format
parameters, current input or output, control values or other properties
remain unchanged. At the first [`open()`](func-open.md#c.V4L.open "open") call after loading the
driver they will be reset to default values, drivers are never in an
undefined state.

## 7.68.5. Return Value

On success [`open()`](func-open.md#c.V4L.open "open") returns the new file descriptor. On error
-1 is returned, and the `errno` variable is set appropriately.
Possible error codes are:

EACCES
:   The caller has no permission to access the device.

EBUSY
:   The driver does not support multiple opens and the device is already
    in use.

ENXIO
:   No device corresponding to this device special file exists.

ENOMEM
:   Not enough kernel memory was available to complete the request.

EMFILE
:   The process already has the maximum number of files open.

ENFILE
:   The limit on the total number of files open on the system has been
    reached.
