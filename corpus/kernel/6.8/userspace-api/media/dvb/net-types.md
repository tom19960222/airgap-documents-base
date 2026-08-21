---
collection: kernel
version: "6.8"
title: "5.1.1. Net Data Types"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/net-types.html
fetched_at: 2026-08-21T03:39:38+00:00
---
# 5.1.1. Net Data Types

struct dvb_net_if
:   describes a DVB network interface

**Definition**:

```
struct dvb_net_if {
    __u16 pid;
    __u16 if_num;
    __u8 feedtype;
#define DVB_NET_FEEDTYPE_MPE 0  ;
#define DVB_NET_FEEDTYPE_ULE 1  ;
};
```

**Members**

`pid`
:   Packet ID (PID) of the MPEG-TS that contains data

`if_num`
:   number of the Digital TV interface.

`feedtype`
:   Encapsulation type of the feed.

**Description**

A MPEG-TS stream may contain packet IDs with IP packages on it.
This struct describes it, and the type of encoding.

**feedtype** can be:

> - `DVB_NET_FEEDTYPE_MPE` for MPE encoding
> - `DVB_NET_FEEDTYPE_ULE` for ULE encoding.
