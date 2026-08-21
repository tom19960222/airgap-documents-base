---
collection: kernel
version: "6.8"
title: "4.2.3. CA_RESET"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-reset.html
fetched_at: 2026-08-21T03:39:07+00:00
---
# 4.2.3. CA_RESET

## 4.2.3.1. Name

CA_RESET

## 4.2.3.2. Synopsis

CA_RESET

`int ioctl(fd, CA_RESET)`

## 4.2.3.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

## 4.2.3.4. Description

Puts the Conditional Access hardware on its initial state. It should
be called before start using the CA hardware.

## 4.2.3.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
