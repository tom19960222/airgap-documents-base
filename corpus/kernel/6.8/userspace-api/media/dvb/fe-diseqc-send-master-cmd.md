---
collection: kernel
version: "6.8"
title: "2.4.7. ioctl FE_DISEQC_SEND_MASTER_CMD"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/fe-diseqc-send-master-cmd.html
fetched_at: 2026-08-21T03:39:24+00:00
---
# 2.4.7. ioctl FE_DISEQC_SEND_MASTER_CMD

## 2.4.7.1. Name

FE_DISEQC_SEND_MASTER_CMD - Sends a DiSEqC command

## 2.4.7.2. Synopsis

FE_DISEQC_SEND_MASTER_CMD

`int ioctl(int fd, FE_DISEQC_SEND_MASTER_CMD, struct dvb_diseqc_master_cmd *argp)`

## 2.4.7.3. Arguments

`fd`
:   File descriptor returned by [`open()`](frontend_f_open.md#c.DTV.fe.open "open").

`argp`
:   pointer to struct
    [`dvb_diseqc_master_cmd`](frontend-header.md#c.dvb_diseqc_master_cmd "dvb_diseqc_master_cmd")

## 2.4.7.4. Description

Sends the DiSEqC command pointed by [`dvb_diseqc_master_cmd`](frontend-header.md#c.dvb_diseqc_master_cmd "dvb_diseqc_master_cmd")
to the antenna subsystem.

## 2.4.7.5. Return Value

On success 0 is returned.

On error -1 is returned, and the `errno` variable is set
appropriately.

Generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.
