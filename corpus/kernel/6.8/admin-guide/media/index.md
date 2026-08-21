---
collection: kernel
version: "6.8"
title: "Media subsystem admin and user guide"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/media/index.html
fetched_at: 2026-08-21T03:34:55+00:00
---
# Media subsystem admin and user guide

This section contains usage information about media subsystem and
its supported drivers.

Please see:

[Linux Media Infrastructure userspace API](../../userspace-api/media/index.md)

> - for the userspace APIs used on media devices.

[Media subsystem kernel internal API](../../driver-api/media/index.md)

> - for driver development information and Kernel APIs used by
>   media devices;

Table of Contents

- [1. Introduction](intro.md)
- [2. Building support for a media device](building.md)
  - [2.1. Configuring the Linux Kernel](building.md#configuring-the-linux-kernel)
  - [2.2. Building and installing a new Kernel](building.md#building-and-installing-a-new-kernel)
  - [2.3. Building just the new media drivers and core](building.md#building-just-the-new-media-drivers-and-core)
- [3. Infrared remote control support in video4linux drivers](remote-controller.md)
  - [3.1. Basics](remote-controller.md#basics)
  - [3.2. How it works](remote-controller.md#how-it-works)
- [4. HDMI CEC](cec.md)
  - [4.1. Supported hardware in mainline](cec.md#supported-hardware-in-mainline)
  - [4.2. Utilities](cec.md#utilities)
  - [4.3. DisplayPort to HDMI Adapters with working CEC](cec.md#displayport-to-hdmi-adapters-with-working-cec)
  - [4.4. USB CEC Dongles](cec.md#usb-cec-dongles)
  - [4.5. CEC Without HPD](cec.md#cec-without-hpd)
  - [4.6. Microcontrollers & CEC](cec.md#microcontrollers-cec)
  - [4.7. Making a CEC debugger](cec.md#making-a-cec-debugger)
- [5. Digital TV](dvb.md)
  - [5.1. Using the Digital TV Framework](dvb_intro.md)
  - [5.2. Digital TV Conditional Access Interface](ci.md)
  - [5.3. FAQ](faq.md)
  - [5.4. References](dvb_references.md)
- [6. Cards List](cardlist.md)
  - [6.1. USB drivers](usb-cardlist.md)
  - [6.2. PCI drivers](pci-cardlist.md)
  - [6.3. Platform drivers](platform-cardlist.md)
  - [6.4. Radio drivers](radio-cardlist.md)
  - [6.5. I²C drivers](i2c-cardlist.md)
  - [6.6. Firewire driver](misc-cardlist.md)
  - [6.7. Test drivers](misc-cardlist.md#test-drivers)
- [7. Video4Linux (V4L) driver-specific documentation](v4l-drivers.md)
  - [7.1. The bttv driver](bttv.md)
  - [7.2. The cafe_ccic driver](cafe_ccic.md)
  - [7.3. The cx88 driver](cx88.md)
  - [7.4. The Samsung S5P/Exynos4 FIMC driver](fimc.md)
  - [7.5. i.MX Video Capture Driver](imx.md)
  - [7.6. i.MX7 Video Capture Driver](imx7.md)
  - [7.7. Intel Image Processing Unit 3 (IPU3) Imaging Unit (ImgU) driver](ipu3.md)
  - [7.8. The ivtv driver](ivtv.md)
  - [7.9. mgb4 sysfs interface](mgb4.md)
  - [7.10. mgb4 mtd partitions](mgb4.md#mgb4-mtd-partitions)
  - [7.11. mgb4 iio (triggers)](mgb4.md#mgb4-iio-triggers)
  - [7.12. OMAP 3 Image Signal Processor (ISP) driver](omap3isp.md)
  - [7.13. OMAP4 ISS Driver](omap4_camera.md)
  - [7.14. Philips webcams (pwc driver)](philips.md)
  - [7.15. Qualcomm Camera Subsystem driver](qcom_camss.md)
  - [7.16. Renesas R-Car Fine Display Processor (FDP1) Driver](rcar-fdp1.md)
  - [7.17. Rockchip Image Signal Processor (rkisp1)](rkisp1.md)
  - [7.18. The saa7134 driver](saa7134.md)
  - [7.19. The Silicon Labs Si470x FM Radio Receivers driver](si470x.md)
  - [7.20. The Silicon Labs Si4713 FM Radio Transmitter Driver](si4713.md)
  - [7.21. The SI476x Driver](si476x.md)
  - [7.22. Starfive Camera Subsystem driver](starfive_camss.md)
  - [7.23. The Virtual Media Controller Driver (vimc)](vimc.md)
  - [7.24. The Virtual Stateless Decoder Driver (visl)](visl.md)
  - [7.25. The Virtual Video Test Driver (vivid)](vivid.md)
- [8. Digital TV driver-specific documentation](dvb-drivers.md)
  - [8.1. Avermedia DVB-T on BT878 Release Notes](avermedia.md)
  - [8.2. How to get the bt8xx cards working](bt8xx.md)
  - [8.3. Firmware files for lmedm04 cards](lmedm04.md)
  - [8.4. Opera firmware](opera-firmware.md)
  - [8.5. How to set up the Technisat/B2C2 Flexcop devices](technisat.md)
  - [8.6. TechnoTrend/Hauppauge DEC USB Driver](ttusb-dec.md)

**Copyright** © 1999-2020 : LinuxTV Developers

```
This documentation is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation; either version 2 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

For more details see the file COPYING in the source distribution of Linux.
```
