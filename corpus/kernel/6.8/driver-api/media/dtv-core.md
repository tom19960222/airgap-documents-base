---
collection: kernel
version: "6.8"
title: "3. Digital TV (DVB) devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/dtv-core.html
fetched_at: 2026-08-21T03:32:23+00:00
---
# 3. Digital TV (DVB) devices

Digital TV devices are implemented by several different drivers:

- A bridge driver that is responsible to talk with the bus where the other
  devices are connected (PCI, USB, SPI), bind to the other drivers and
  implement the digital demux logic (either in software or in hardware);
- Frontend drivers that are usually implemented as two separate drivers:

  - A tuner driver that implements the logic which commands the part of
    the hardware responsible for tuning into a digital TV transponder or
    physical channel. The output of a tuner is usually a baseband or
    Intermediate Frequency (IF) signal;
  - A demodulator driver (a.k.a "demod") that implements the logic which
    commands the digital TV decoding hardware. The output of a demod is
    a digital stream, with multiple audio, video and data channels typically
    multiplexed using MPEG Transport Stream [1](dtv-core.md#f1).

On most hardware, the frontend drivers talk with the bridge driver using an
I2C bus.

[1](dtv-core.md#id1)
:   Some standards use TCP/IP for multiplexing data, like DVB-H (an
    abandoned standard, not used anymore) and ATSC version 3.0 current
    proposals. Currently, the DVB subsystem doesn't implement those standards.

- [3.1. Digital TV Common functions](dtv-common.md)
- [3.2. Digital TV Frontend kABI](dtv-frontend.md)
- [3.3. Digital TV Demux kABI](dtv-demux.md)
- [3.4. Digital TV Conditional Access kABI](dtv-ca.md)
- [3.5. Digital TV Network kABI](dtv-net.md)
