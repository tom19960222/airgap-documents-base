---
collection: kernel
version: "6.8"
title: "AMDGPU XGMI Support"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/xgmi.html
fetched_at: 2026-08-21T03:48:04+00:00
---
# AMDGPU XGMI Support

**AMDGPU XGMI Support**

XGMI is a high speed interconnect that joins multiple GPU cards
into a homogeneous memory space that is organized by a collective
hive ID and individual node IDs, both of which are 64-bit numbers.

The file xgmi_device_id contains the unique per GPU device ID and
is stored in the /sys/class/drm/card${cardno}/device/ directory.

Inside the device directory a sub-directory 'xgmi_hive_info' is
created which contains the hive ID and the list of nodes.

The hive ID is stored in:
:   /sys/class/drm/card${cardno}/device/xgmi_hive_info/xgmi_hive_id

The node information is stored in numbered directories:
:   /sys/class/drm/card${cardno}/device/xgmi_hive_info/node${nodeno}/xgmi_device_id

Each device has their own xgmi_hive_info direction with a mirror
set of node sub-directories.

The XGMI memory space is built by contiguously adding the power of
two padded VRAM space from each node to each other.
