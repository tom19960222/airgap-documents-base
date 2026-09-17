---
collection: kernel
version: "6.17"
title: "Misc AMDGPU driver information"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/amdgpu/driver-misc.html
fetched_at: 2026-09-16T16:39:27+00:00
---
# Misc AMDGPU driver information

## GPU Product Information

Information about the GPU can be obtained on certain cards
via sysfs

### product_name

The amdgpu driver provides a sysfs API for reporting the product name
for the device
The file product_name is used for this and returns the product name
as returned from the FRU.
NOTE: This is only available for certain server cards

### product_number

The amdgpu driver provides a sysfs API for reporting the part number
for the device
The file product_number is used for this and returns the part number
as returned from the FRU.
NOTE: This is only available for certain server cards

### serial_number

The amdgpu driver provides a sysfs API for reporting the serial number
for the device
The file serial_number is used for this and returns the serial number
as returned from the FRU.
NOTE: This is only available for certain server cards

### fru_id

The amdgpu driver provides a sysfs API for reporting FRU File Id
for the device.
The file fru_id is used for this and returns the File Id value
as returned from the FRU.
NOTE: This is only available for certain server cards

### manufacturer

The amdgpu driver provides a sysfs API for reporting manufacturer name from
FRU information.
The file manufacturer returns the value as returned from the FRU.
NOTE: This is only available for certain server cards

### unique_id

The amdgpu driver provides a sysfs API for providing a unique ID for the GPU
The file unique_id is used for this.
This will provide a Unique ID that will persist from machine to machine

NOTE: This will only work for GFX9 and newer. This file will be absent
on unsupported ASICs (GFX8 and older)

### board_info

The amdgpu driver provides a sysfs API for giving board related information.
It provides the form factor information in the format

> type : form factor

Possible form factor values

- “cem” - PCIE CEM card
- “oam” - Open Compute Accelerator Module
- “unknown” - Not known

## GPU Memory Usage Information

Various memory accounting can be accessed via sysfs

### mem_info_vram_total

The amdgpu driver provides a sysfs API for reporting current total VRAM
available on the device
The file mem_info_vram_total is used for this and returns the total
amount of VRAM in bytes

### mem_info_vram_used

The amdgpu driver provides a sysfs API for reporting current total VRAM
available on the device
The file mem_info_vram_used is used for this and returns the total
amount of currently used VRAM in bytes

### mem_info_vis_vram_total

The amdgpu driver provides a sysfs API for reporting current total
visible VRAM available on the device
The file mem_info_vis_vram_total is used for this and returns the total
amount of visible VRAM in bytes

### mem_info_vis_vram_used

The amdgpu driver provides a sysfs API for reporting current total of
used visible VRAM
The file mem_info_vis_vram_used is used for this and returns the total
amount of currently used visible VRAM in bytes

### mem_info_gtt_total

The amdgpu driver provides a sysfs API for reporting current total size of
the GTT.
The file mem_info_gtt_total is used for this, and returns the total size of
the GTT block, in bytes

### mem_info_gtt_used

The amdgpu driver provides a sysfs API for reporting current total amount of
used GTT.
The file mem_info_gtt_used is used for this, and returns the current used
size of the GTT block, in bytes

## PCIe Accounting Information

### pcie_bw

The amdgpu driver provides a sysfs API for estimating how much data
has been received and sent by the GPU in the last second through PCIe.
The file pcie_bw is used for this.
The Perf counters count the number of received and sent messages and return
those values, as well as the maximum payload size of a PCIe packet (mps).
Note that it is not possible to easily and quickly obtain the size of each
packet transmitted, so we output the max payload size (mps) to allow for
quick estimation of the PCIe bandwidth usage

### pcie_replay_count

The amdgpu driver provides a sysfs API for reporting the total number
of PCIe replays (NAKs).
The file pcie_replay_count is used for this and returns the total
number of replays as a sum of the NAKs generated and NAKs received.

## GPU SmartShift Information

GPU SmartShift information via sysfs

### smartshift_apu_power

The amdgpu driver provides a sysfs API for reporting APU power
shift in percentage if platform supports smartshift. Value 0 means that
there is no powershift and values between [1-100] means that the power
is shifted to APU, the percentage of boost is with respect to APU power
limit on the platform.

### smartshift_dgpu_power

The amdgpu driver provides a sysfs API for reporting dGPU power
shift in percentage if platform supports smartshift. Value 0 means that
there is no powershift and values between [1-100] means that the power is
shifted to dGPU, the percentage of boost is with respect to dGPU power
limit on the platform.

### smartshift_bias

The amdgpu driver provides a sysfs API for reporting the
smartshift(SS2.0) bias level. The value ranges from -100 to 100
and the default is 0. -100 sets maximum preference to APU
and 100 sets max perference to dGPU.
