---
collection: kernel
version: "6.8"
title: "1. Common API Elements"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/common.html
fetched_at: 2026-08-21T03:56:38+00:00
---
# 1. Common API Elements

Programming a V4L2 device consists of these steps:

- Opening the device
- Changing device properties, selecting a video and audio input, video
  standard, picture brightness a. o.
- Negotiating a data format
- Negotiating an input/output method
- The actual input/output loop
- Closing the device

In practice most steps are optional and can be executed out of order. It
depends on the V4L2 device type, you can read about the details in
[Interfaces](devices.md#devices). In this chapter we will discuss the basic concepts
applicable to all devices.

- [1.1. Opening and Closing Devices](open.md)
- [1.2. Querying Capabilities](querycap.md)
- [1.3. Application Priority](app-pri.md)
- [1.4. Video Inputs and Outputs](video.md)
- [1.5. Audio Inputs and Outputs](audio.md)
- [1.6. Tuners and Modulators](tuner.md)
- [1.7. Video Standards](standard.md)
- [1.8. Digital Video (DV) Timings](dv-timings.md)
- [1.9. User Controls](control.md)
- [1.10. Extended Controls API](extended-controls.md)
- [1.11. Camera Control Reference](ext-ctrls-camera.md)
- [1.12. Flash Control Reference](ext-ctrls-flash.md)
- [1.13. Image Source Control Reference](ext-ctrls-image-source.md)
- [1.14. Image Process Control Reference](ext-ctrls-image-process.md)
- [1.15. Codec Control Reference](ext-ctrls-codec.md)
- [1.16. Stateless Codec Control Reference](ext-ctrls-codec-stateless.md)
- [1.17. JPEG Control Reference](ext-ctrls-jpeg.md)
- [1.18. Digital Video Control Reference](ext-ctrls-dv.md)
- [1.19. RF Tuner Control Reference](ext-ctrls-rf-tuner.md)
- [1.20. FM Transmitter Control Reference](ext-ctrls-fm-tx.md)
- [1.21. FM Receiver Control Reference](ext-ctrls-fm-rx.md)
- [1.22. Detect Control Reference](ext-ctrls-detect.md)
- [1.23. Colorimetry Control Reference](ext-ctrls-colorimetry.md)
- [1.24. Guidelines for Video4Linux pixel format 4CCs](fourcc.md)
- [1.25. Data Formats](format.md)
- [1.26. Single- and multi-planar APIs](planar-apis.md)
- [1.27. Cropping, composing and scaling -- the SELECTION API](selection-api.md)
- [1.28. Image Cropping, Insertion and Scaling -- the CROP API](crop.md)
- [1.29. Streaming Parameters](streaming-par.md)
