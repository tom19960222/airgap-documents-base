---
collection: kernel
version: "6.8"
title: "8.6. TechnoTrend/Hauppauge DEC USB Driver"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/media/ttusb-dec.html
fetched_at: 2026-08-21T03:56:07+00:00
---
# 8.6. TechnoTrend/Hauppauge DEC USB Driver

## 8.6.1. Driver Status

Supported:

> - DEC2000-t
> - DEC2450-t
> - DEC3000-s
> - Video Streaming
> - Audio Streaming
> - Section Filters
> - Channel Zapping
> - Hotplug firmware loader

To Do:

> - Tuner status information
> - DVB network interface
> - Streaming video PC->DEC
> - Conax support for 2450-t

## 8.6.2. Getting the Firmware

To download the firmware, use the following commands:

```
scripts/get_dvb_firmware dec2000t
scripts/get_dvb_firmware dec2540t
scripts/get_dvb_firmware dec3000s
```

## 8.6.3. Hotplug Firmware Loading

Since 2.6 kernels, the firmware is loaded at the point that the driver module
is loaded.

Copy the three files downloaded above into the /usr/lib/hotplug/firmware or
/lib/firmware directory (depending on configuration of firmware hotplug).
