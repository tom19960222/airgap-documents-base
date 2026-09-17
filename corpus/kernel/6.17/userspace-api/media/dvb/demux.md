---
collection: kernel
version: "6.17"
title: "3. Digital TV Demux Device"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/dvb/demux.html
fetched_at: 2026-09-16T16:56:00+00:00
---
# 3. Digital TV Demux Device

The Digital TV demux device controls the MPEG-TS filters for the
digital TV. If the driver and hardware supports, those filters are
implemented at the hardware. Otherwise, the Kernel provides a software
emulation.

It can be accessed through `/dev/adapter?/demux?`. Data types and
ioctl definitions can be accessed by including `linux/dvb/dmx.h` in
your application.

- [3.1. Demux Data Types](dmx_types.md)
- [3.2. Demux Function Calls](dmx_fcalls.md)
