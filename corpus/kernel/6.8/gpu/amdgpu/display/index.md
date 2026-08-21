---
collection: kernel
version: "6.8"
title: "drm/amd/display - Display Core (DC)"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/display/index.html
fetched_at: 2026-08-21T03:48:01+00:00
---
# drm/amd/display - Display Core (DC)

AMD display engine is partially shared with other operating systems; for this
reason, our Display Core Driver is divided into two pieces:

1. **Display Core (DC)** contains the OS-agnostic components. Things like
   hardware programming and resource management are handled here.
2. **Display Manager (DM)** contains the OS-dependent components. Hooks to the
   amdgpu base driver and DRM are implemented here.

The display pipe is responsible for "scanning out" a rendered frame from the
GPU memory (also called VRAM, FrameBuffer, etc.) to a display. In other words,
it would:

1. Read frame information from memory;
2. Perform required transformation;
3. Send pixel data to sink devices.

If you want to learn more about our driver details, take a look at the below
table of content:

- [AMDgpu Display Manager](display-manager.md)
  - [Lifecycle](display-manager.md#lifecycle)
  - [Interrupts](display-manager.md#interrupts)
  - [Atomic Implementation](display-manager.md#atomic-implementation)
  - [Color Management Properties](display-manager.md#color-management-properties)
    - [DC Color Capabilities between DCN generations](display-manager.md#dc-color-capabilities-between-dcn-generations)
  - [Blend Mode Properties](display-manager.md#blend-mode-properties)
    - [Blend configuration flow](display-manager.md#blend-configuration-flow)
- [Display Core Debug tools](dc-debug.md)
  - [DC Visual Confirmation](dc-debug.md#dc-visual-confirmation)
    - [Multiple Planes Debug](dc-debug.md#multiple-planes-debug)
    - [Pipe Split Debug](dc-debug.md#pipe-split-debug)
  - [DTN Debug](dc-debug.md#dtn-debug)
  - [DMUB Firmware Debug](dc-debug.md#dmub-firmware-debug)
    - [Trace Groups](dc-debug.md#trace-groups)
- [Display Core Next (DCN)](dcn-overview.md)
  - [Front End and Back End](dcn-overview.md#front-end-and-back-end)
  - [Data Flow](dcn-overview.md#data-flow)
  - [AMD Hardware Pipeline](dcn-overview.md#amd-hardware-pipeline)
  - [Global Sync](dcn-overview.md#global-sync)
- [Multiplane Overlay (MPO)](mpo-overview.md)
  - [Plane Restrictions](mpo-overview.md#plane-restrictions)
  - [Cursor Restrictions](mpo-overview.md#cursor-restrictions)
  - [Use Cases](mpo-overview.md#use-cases)
    - [Picture-in-Picture (PIP) playback - Underlay strategy](mpo-overview.md#picture-in-picture-pip-playback-underlay-strategy)
    - [Multiple Display MPO](mpo-overview.md#multiple-display-mpo)
      - [Limitations](mpo-overview.md#limitations)
- [DC Glossary](dc-glossary.md)
