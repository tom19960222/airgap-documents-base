---
collection: kernel
version: "6.8"
title: "4. Digital TV CA Device"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/dvb/ca.html
fetched_at: 2026-08-21T03:57:52+00:00
---
# 4. Digital TV CA Device

The Digital TV CA device controls the conditional access hardware. It
can be accessed through `/dev/dvb/adapter?/ca?`. Data types and ioctl
definitions can be accessed by including `linux/dvb/ca.h` in your
application.

> **Note:**
>
> There are three ioctls at this API that aren't documented:
> [CA_GET_MSG](ca-get-msg.md#ca-get-msg), [CA_SEND_MSG](ca-send-msg.md#ca-send-msg) and [CA_SET_DESCR](ca-set-descr.md#ca-set-descr).
> Documentation for them are welcome.

- [4.1. CA Data Types](ca_data_types.md)
- [4.2. CA Function Calls](ca_function_calls.md)
- [4.3. The High level CI API](ca_high_level.md)
