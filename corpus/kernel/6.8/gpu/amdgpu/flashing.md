---
collection: kernel
version: "6.8"
title: "dGPU firmware flashing"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/amdgpu/flashing.html
fetched_at: 2026-08-21T03:48:03+00:00
---
# dGPU firmware flashing

## IFWI

Flashing the dGPU integrated firmware image (IFWI) is supported by GPUs that
use the PSP to orchestrate the update (Navi3x or newer GPUs).
For supported GPUs, amdgpu will export a series of sysfs files that can be
used for the flash process.

The IFWI flash process is:

1. Ensure the IFWI image is intended for the dGPU on the system.
2. "Write" the IFWI image to the sysfs file psp_vbflash. This will stage the IFWI in memory.
3. "Read" from the psp_vbflash sysfs file to initiate the flash process.
4. Poll the psp_vbflash_status sysfs file to determine when the flash process completes.

## USB-C PD F/W

On GPUs that support flashing an updated USB-C PD firmware image, the process
is done using the usbc_pd_fw sysfs file.

- Reading the file will provide the current firmware version.
- Writing the name of a firmware payload stored in /lib/firmware/amdgpu to the sysfs file will initiate the flash process.

The firmware payload stored in /lib/firmware/amdgpu can be named any name
as long as it doesn't conflict with other existing binaries that are used by
amdgpu.

## sysfs files

**usbc_pd_fw**

Reading from this file will retrieve the USB-C PD firmware version. Writing to
this file will trigger the update process.

**psp_vbflash**

Writing to this file will stage an IFWI for update. Reading from this file
will trigger the update process.

**psp_vbflash_status**

The status of the flash process.
0: IFWI flash not complete.
1: IFWI flash complete.
