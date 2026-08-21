---
collection: kernel
version: "6.8"
title: "Video4Linux (V4L)  driver-specific documentation"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/drivers/index.html
fetched_at: 2026-08-21T03:35:41+00:00
---
# Video4Linux (V4L) driver-specific documentation

**Copyright** © 1999-2016 : LinuxTV Developers

This documentation is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the Free
Software Foundation version 2 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
more details.

For more details see the file COPYING in the source distribution of Linux.

Table of Contents

- [1. ASPEED video driver](aspeed-video.md)
  - [1.1. `V4L2_CID_ASPEED_HQ_MODE`](aspeed-video.md#v4l2-cid-aspeed-hq-mode)
  - [1.2. `V4L2_CID_ASPEED_HQ_JPEG_QUALITY`](aspeed-video.md#v4l2-cid-aspeed-hq-jpeg-quality)
- [2. Using camera sensor drivers](camera-sensor.md)
  - [2.1. Frame size](camera-sensor.md#frame-size)
    - [2.1.1. Freely configurable camera sensor drivers](camera-sensor.md#freely-configurable-camera-sensor-drivers)
    - [2.1.2. Register list based drivers](camera-sensor.md#register-list-based-drivers)
  - [2.2. Frame interval configuration](camera-sensor.md#frame-interval-configuration)
    - [2.2.1. Raw camera sensors](camera-sensor.md#raw-camera-sensors)
    - [2.2.2. USB cameras etc. devices](camera-sensor.md#usb-cameras-etc-devices)
  - [2.3. Rotation, orientation and flipping](camera-sensor.md#rotation-orientation-and-flipping)
- [3. MIPI CCS camera sensor driver](ccs.md)
  - [3.1. Pixel Array sub-device](ccs.md#pixel-array-sub-device)
  - [3.2. Binner](ccs.md#binner)
  - [3.3. Scaler](ccs.md#scaler)
  - [3.4. Digital and analogue crop](ccs.md#digital-and-analogue-crop)
  - [3.5. Private controls](ccs.md#private-controls)
    - [3.5.1. Analogue gain model](ccs.md#analogue-gain-model)
    - [3.5.2. Alternate analogue gain model](ccs.md#alternate-analogue-gain-model)
    - [3.5.3. Shading correction](ccs.md#shading-correction)
- [4. The cx2341x driver](cx2341x-uapi.md)
  - [4.1. Non-compressed file format](cx2341x-uapi.md#non-compressed-file-format)
    - [4.1.1. Raw format c example](cx2341x-uapi.md#raw-format-c-example)
  - [4.2. Format of embedded V4L2_MPEG_STREAM_VBI_FMT_IVTV VBI data](cx2341x-uapi.md#format-of-embedded-v4l2-mpeg-stream-vbi-fmt-ivtv-vbi-data)
- [5. DW100 dewarp driver](dw100.md)
- [6. i.MX Video Capture Driver](imx-uapi.md)
  - [6.1. Events](imx-uapi.md#events)
    - [6.1.1. ipuX_csiY](imx-uapi.md#ipux-csiy)
  - [6.2. Controls](imx-uapi.md#controls)
    - [6.2.1. Frame Interval Monitor in ipuX_csiY](imx-uapi.md#frame-interval-monitor-in-ipux-csiy)
    - [6.2.2. File list](imx-uapi.md#file-list)
    - [6.2.3. Authors](imx-uapi.md#authors)
- [7. Maxim Integrated MAX2175 RF to bits tuner driver](max2175.md)
  - [7.1. `V4L2_CID_MAX2175_I2S_ENABLE`](max2175.md#v4l2-cid-max2175-i2s-enable)
  - [7.2. `V4L2_CID_MAX2175_HSLS`](max2175.md#v4l2-cid-max2175-hsls)
  - [7.3. `V4L2_CID_MAX2175_RX_MODE (menu)`](max2175.md#v4l2-cid-max2175-rx-mode-menu)
- [8. NPCM video driver](npcm-video.md)
  - [8.1. Driver-specific Controls](npcm-video.md#driver-specific-controls)
    - [8.1.1. V4L2_CID_NPCM_CAPTURE_MODE](npcm-video.md#v4l2-cid-npcm-capture-mode)
    - [8.1.2. V4L2_CID_NPCM_RECT_COUNT](npcm-video.md#v4l2-cid-npcm-rect-count)
  - [8.2. References](npcm-video.md#references)
- [9. OMAP 3 Image Signal Processor (ISP) driver](omap3isp-uapi.md)
  - [9.1. Events](omap3isp-uapi.md#events)
  - [9.2. Private IOCTLs](omap3isp-uapi.md#private-ioctls)
  - [9.3. CCDC and preview block IOCTLs](omap3isp-uapi.md#ccdc-and-preview-block-ioctls)
  - [9.4. Statistic blocks IOCTLs](omap3isp-uapi.md#statistic-blocks-ioctls)
  - [9.5. VIDIOC_OMAP3ISP_STAT_EN](omap3isp-uapi.md#vidioc-omap3isp-stat-en)
  - [9.6. VIDIOC_OMAP3ISP_AEWB_CFG, VIDIOC_OMAP3ISP_HIST_CFG and VIDIOC_OMAP3ISP_AF_CFG](omap3isp-uapi.md#vidioc-omap3isp-aewb-cfg-vidioc-omap3isp-hist-cfg-and-vidioc-omap3isp-af-cfg)
  - [9.7. VIDIOC_OMAP3ISP_STAT_REQ](omap3isp-uapi.md#vidioc-omap3isp-stat-req)
  - [9.8. References](omap3isp-uapi.md#references)
- [10. ST VGXY61 camera sensor driver](st-vgxy61.md)
  - [10.1. `V4L2_CID_HDR_SENSOR_MODE`](st-vgxy61.md#v4l2-cid-hdr-sensor-mode)
- [11. THine THP7312 ISP driver](thp7312.md)
- [12. The Linux USB Video Class (UVC) driver](uvcvideo.md)
  - [12.1. Extension Unit (XU) support](uvcvideo.md#extension-unit-xu-support)
    - [12.1.1. Introduction](uvcvideo.md#introduction)
    - [12.1.2. Control mappings](uvcvideo.md#control-mappings)
    - [12.1.3. Security](uvcvideo.md#security)
    - [12.1.4. Debugging](uvcvideo.md#debugging)
    - [12.1.5. IOCTL reference](uvcvideo.md#ioctl-reference)
      - [12.1.5.1. UVCIOC_CTRL_MAP - Map a UVC control to a V4L2 control](uvcvideo.md#uvcioc-ctrl-map-map-a-uvc-control-to-a-v4l2-control)
      - [12.1.5.2. UVCIOC_CTRL_QUERY - Query a UVC XU control](uvcvideo.md#uvcioc-ctrl-query-query-a-uvc-xu-control)
