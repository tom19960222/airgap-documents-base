---
collection: kernel
version: "6.8"
title: "Misc AMDGPU driver information"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/driver-misc.html
fetched_at: 2026-08-21T03:48:05+00:00
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

- "cem" - PCIE CEM card
- "oam" - Open Compute Accelerator Module
- "unknown" - Not known

### Accelerated Processing Units (APU) Info

| Product Name | Code Reference | DCN/DCE version | GC version | VCE/UVD/VCN version | SDMA version | MP0 version |
| --- | --- | --- | --- | --- | --- | --- |
| Radeon R\* Graphics | CARRIZO/STONEY | DCE 11 | 8 | VCE 3 / UVD 6 | 3 | n/a |
| Ryzen 3000 series / AMD Ryzen Embedded V1\*/R1\* with Radeon Vega Gfx | RAVEN/PICASSO | DCN 1.0 | 9.1.0 | VCN 1.0 | 4.1.0 | 10.0.0 |
| Ryzen 4000 series | RENOIR | DCN 2.1 | 9.3 | VCN 2.2 | 4.1.2 | 11.0.3 |
| Ryzen 3000 series / AMD Ryzen Embedded V1\*/R1\* with Radeon Vega Gfx | RAVEN2 | DCN 1.0 | 9.2.2 | VCN 1.0.1 | 4.1.1 | 10.0.1 |
| SteamDeck | VANGOGH | DCN 3.0.1 | 10.3.1 | VCN 3.1.0 | 5.2.1 | 11.5.0 |
| Ryzen 5000 series / Ryzen 7x30 series | GREEN SARDINE / Cezanne / Barcelo / Barcelo-R | DCN 2.1 | 9.3 | VCN 2.2 | 4.1.1 | 12.0.1 |
| Ryzen 6000 series / Ryzen 7x35 series / Ryzen 7x36 series | YELLOW CARP / Rembrandt / Rembrandt-R | 3.1.2 | 10.3.3 | VCN 3.1.1 | 5.2.3 | 13.0.3 |
| Ryzen 7000 series (AM5) | Raphael | 3.1.5 | 10.3.6 | 3.1.2 | 5.2.6 | 13.0.5 |
| Ryzen 7x45 series (FL1) | Dragon Range | 3.1.5 | 10.3.6 | 3.1.2 | 5.2.6 | 13.0.5 |
| Ryzen 7x20 series | Mendocino | 3.1.6 | 10.3.7 | 3.1.1 | 5.2.7 | 13.0.8 |
| Ryzen 7x40 series | Phoenix | 3.1.4 | 11.0.1 / 11.0.4 | 4.0.2 | 6.0.1 | 13.0.4 / 13.0.11 |
| Ryzen 8x40 series | Hawk Point | 3.1.4 | 11.0.1 / 11.0.4 | 4.0.2 | 6.0.1 | 13.0.4 / 13.0.11 |

### Discrete GPU Info

| Product Name | Code Reference | DCN/DCE version | GC version | VCN version | SDMA version |
| --- | --- | --- | --- | --- | --- |
| AMD Radeon (TM) HD 8500M/ 8600M /M200 /M320 /M330 /M335 Series | HAINAN | -- | 6 | -- | -- |
| AMD Radeon HD 7800 /7900 /FireGL Series | TAHITI | DCE 6 | 6 | VCE 1 / UVD 3 | -- |
| AMD Radeon R7 (TM|HD) M265 /M370 /8500M /8600 /8700 /8700M | OLAND | DCE 6 | 6 | VCE 1 / UVD 3 | -- |
| AMD Radeon (TM) (HD|R7) 7800 /7970 /8800 /8970 /370/ Series | PITCAIRN | DCE 6 | 6 | VCE 1 / UVD 3 | -- |
| AMD Radeon (TM|R7|R9|HD) E8860 /M360 /7700 /7800 /8800 /9000(M) /W4100 Series | VERDE | DCE 6 | 6 | VCE 1 / UVD 3 | -- |
| AMD Radeon HD M280X /M380 /7700 /8950 /W5100 | BONAIRE | DCE 8 | 7 | VCE 2 / UVD 4.2 | 1 |
| AMD Radeon (R9|TM) 200 /390 /W8100 /W9100 Series | HAWAII | DCE 8 | 7 | VCE 2 / UVD 4.2 | 1 |
| AMD Radeon (TM) R(5|7) M315 /M340 /M360 | TOPAZ |  | 8 | -- | 2 |
| AMD Radeon (TM) R9 200 /380 /W7100 /S7150 /M390 /M395 Series | TONGA | DCE 10 | 8 | VCE 3 / UVD 5 | 3 |
| AMD Radeon (FirePro) (TM) R9 Fury Series | FIJI | DCE 10 | 8 | VCE 3 / UVD 6 | 3 |
| Radeon RX 470 /480 /570 /580 /590 Series - AMD Radeon (TM) (Pro WX) 5100 /E9390 /E9560 /E9565 /V7350 /7100 /P30PH | POLARIS10 | DCE 11.2 | 8 | VCE 3.4 / UVD 6.3 | 3 |
| Radeon (TM) (RX|Pro WX) E9260 /460 /V5300X /550 /560(X) Series | POLARIS11 | DCE 11.2 | 8 | VCE 3.4 / UVD 6.3 | 3 |
| Radeon (RX/Pro) 500 /540(X) /550 /640 /WX2100 /WX3100 /WX200 Series | POLARIS12 | DCE 11.2 | 8 | VCE 3.4 / UVD 6.3 | 3 |
| Radeon (RX|TM) (PRO|WX) Vega /MI25 /V320 /V340L /8200 /9100 /SSG MxGPU | VEGA10 | DCE 12 | 9.0.1 | VCE 4.0.0 / UVD 7.0.0 | 4.0.0 |
| AMD Radeon (Pro) VII /MI50 /MI60 | VEGA20 | DCE 12 | 9.4.0 | VCE 4.1.0 / UVD 7.2.0 | 4.2.0 |
| MI100 | ARCTURUS |  | 9.4.1 | VCN 2.5.0 | 4.2.2 |
| MI200 | ALDEBARAN |  | 9.4.2 | VCN 2.6.0 | 4.4.0 |
| AMD Radeon (RX|Pro) 5600(M|XT) /5700 (M|XT|XTB) /W5700 | NAVI10 | DCN 2.0.0 | 10.1.10 | VCN 2.0.0 | 5.0.0 |
| AMD Radeon (Pro) 5300 /5500XTB/5500(XT|M) /W5500M /W5500 | NAVI14 | DCN 2.0.0 | 10.1.1 | VCN 2.0.2 | 5.0.2 |
| AMD Radeon RX 6800(XT) /6900(XT) /W6800 | SIENNA_CICHLID | DCN 3.0.0 | 10.3.0 | VCN 3.0.0 | 5.2.0 |
| AMD Radeon RX 6700 XT / 6800M / 6700M | NAVY_FLOUNDER | DCN 3.0.0 | 10.3.2 | VCN 3.0.0 | 5.2.2 |
| AMD Radeon RX 6600(XT) /6600M /W6600 /W6600M | DIMGREY_CAVEFISH | DCN 3.0.2 | 10.3.4 | VCN 3.0.16 | 5.2.4 |
| AMD Radeon RX 6500M /6300M /W6500M /W6300M | BEIGE_GOBY | DCN 3.0.3 | 10.3.5 | VCN 3.0.33 | 5.2.5 |
| AMD Radeon RX 7900 XT /XTX |  | DCN 3.2.0 | 11.0.0 | VCN 4.0.0 | 6.0.0 |
| AMD Radeon RX 7600M (XT) /7700S /7600S |  | DCN 3.2.1 | 11.0.2 | VCN 4.0.4 | 6.0.2 |

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
of PCIe replays (NAKs)
The file pcie_replay_count is used for this and returns the total
number of replays as a sum of the NAKs generated and NAKs received

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
