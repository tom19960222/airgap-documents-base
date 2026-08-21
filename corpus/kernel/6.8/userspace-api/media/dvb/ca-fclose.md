---
collection: kernel
version: "6.8"
title: "4.2.2. Digital TV CA close()"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca-fclose.html
fetched_at: 2026-08-21T03:39:09+00:00
---
# 4.2.2. Digital TV CA close()

## 4.2.2.1. Name

Digital TV CA [`close()`](ca-fclose.md#c.DTV.ca.close "DTV.ca.close")

## 4.2.2.2. Synopsis

int close(int fd)

## 4.2.2.3. Arguments

`fd`
:   File descriptor returned by a previous call to [`open()`](ca-fopen.md#c.DTV.ca.open "open").

## 4.2.2.4. Description

This system call closes a previously opened CA device.

## 4.2.2.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
