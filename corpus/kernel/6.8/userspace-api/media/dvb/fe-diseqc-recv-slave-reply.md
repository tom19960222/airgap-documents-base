---
collection: kernel
version: "6.8"
title: "2.4.8. ioctl FE_DISEQC_RECV_SLAVE_REPLY"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-diseqc-recv-slave-reply.html
fetched_at: 2026-08-21T03:39:22+00:00
---
# 2.4.8. ioctl FE_DISEQC_RECV_SLAVE_REPLY

## 2.4.8.1. Name

FE_DISEQC_RECV_SLAVE_REPLY - Receives reply from a DiSEqC 2.0 command

## 2.4.8.2. Synopsis

FE_DISEQC_RECV_SLAVE_REPLY

`int ioctl(int fd, FE_DISEQC_RECV_SLAVE_REPLY, struct dvb_diseqc_slave_reply *argp)`

## 2.4.8.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`argp`
:   pointer to struct [`dvb_diseqc_slave_reply`](frontend-header.md#c.dvb_diseqc_slave_reply "dvb_diseqc_slave_reply").

## 2.4.8.4. Description

Receives reply from a DiSEqC 2.0 command.

The received message is stored at the buffer pointed by `argp`.

## 2.4.8.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
