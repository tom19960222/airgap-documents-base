---
collection: kernel
version: "6.8"
title: "5.12. request poll()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/mediactl/request-func-poll.html
fetched_at: 2026-08-21T03:40:00+00:00
---
# 5.12. request poll()

## 5.12.1. Name

request-poll - Wait for some event on a file descriptor

## 5.12.2. Synopsis

```c
#include <sys/poll.h>
```

int poll(struct pollfd \*ufds, unsigned int nfds, int timeout)

## 5.12.3. Arguments

`ufds`
:   List of file descriptor events to be watched

`nfds`
:   Number of file descriptor events at the \*ufds array

`timeout`
:   Timeout to wait for events

## 5.12.4. Description

With the [`poll()`](request-func-poll.md#c.MC.poll "poll") function applications can wait
for a request to complete.

On success [`poll()`](request-func-poll.md#c.MC.poll "poll") returns the number of file
descriptors that have been selected (that is, file descriptors for which the
`revents` field of the respective struct `pollfd`
is non-zero). Request file descriptor set the `POLLPRI` flag in `revents`
when the request was completed. When the function times out it returns
a value of zero, on failure it returns -1 and the `errno` variable is
set appropriately.

Attempting to poll for a request that is not yet queued will
set the `POLLERR` flag in `revents`.

## 5.12.5. Return Value

On success, [`poll()`](request-func-poll.md#c.MC.poll "poll") returns the number of
structures which have non-zero `revents` fields, or zero if the call
timed out. On error -1 is returned, and the `errno` variable is set
appropriately:

`EBADF`
:   One or more of the `ufds` members specify an invalid file
    descriptor.

`EFAULT`
:   `ufds` references an inaccessible memory area.

`EINTR`
:   The call was interrupted by a signal.

`EINVAL`
:   The `nfds` value exceeds the `RLIMIT_NOFILE` value. Use
    `getrlimit()` to obtain this value.
