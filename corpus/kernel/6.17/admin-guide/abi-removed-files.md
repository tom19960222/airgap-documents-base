---
collection: kernel
version: "6.17"
title: "Removed ABI Files"
source_url: https://www.kernel.org/doc/html/v6.17/admin-guide/abi-removed-files.html
fetched_at: 2026-09-16T16:47:30+00:00
---
# Removed ABI Files

## ABI file removed/devfs

Has the following ABI:

- [devfs](abi-removed.md#abi-devfs)

## ABI file removed/dv1394

Has the following ABI:

- [dv1394 (a.k.a. “OHCI-DV I/O support” for FireWire)](abi-removed.md#abi-dv1394-a-k-a-ohci-dv-i-o-support-for-firewire)

## ABI file removed/ip_queue

Has the following ABI:

- [ip_queue](abi-removed.md#abi-ip-queue)

## ABI file removed/net_dma

Has the following ABI:

- [tcp_dma_copybreak sysctl](abi-removed.md#abi-tcp-dma-copybreak-sysctl)

## ABI file removed/o2cb

Has the following ABI:

- [/sys/o2cb symlink](abi-removed.md#abi-sys-o2cb-symlink)

## ABI file removed/raw1394

Has the following ABI:

- [raw1394 (a.k.a. “Raw IEEE1394 I/O support” for FireWire)](abi-removed.md#abi-raw1394-a-k-a-raw-ieee1394-i-o-support-for-firewire)

## ABI file removed/sysfs-bus-nfit

Has the following ABI:

- [/sys/bus/nd/devices/regionX/nfit/ecc_unit_size](abi-removed.md#abi-sys-bus-nd-devices-regionx-nfit-ecc-unit-size)

## ABI file removed/sysfs-class-cxl

The cxl driver was removed in 6.15.

Please note that attributes that are shared between devices are stored in
the directory pointed to by the symlink device/.
For example, the real path of the attribute /sys/class/cxl/afu0.0s/irqs_max is
/sys/class/cxl/afu0.0s/device/irqs_max, i.e. /sys/class/cxl/afu0.0/irqs_max.

Slave contexts (eg. /sys/class/cxl/afu0.0s):

Has the following ABI:

- [/sys/class/cxl/<afu>/afu_err_buf](abi-removed.md#abi-sys-class-cxl-afu-afu-err-buf)
- [/sys/class/cxl/<afu>/irqs_max](abi-removed.md#abi-sys-class-cxl-afu-irqs-max)
- [/sys/class/cxl/<afu>/irqs_min](abi-removed.md#abi-sys-class-cxl-afu-irqs-min)
- [/sys/class/cxl/<afu>/mmio_size](abi-removed.md#abi-sys-class-cxl-afu-mmio-size)
- [/sys/class/cxl/<afu>/modes_supported](abi-removed.md#abi-sys-class-cxl-afu-modes-supported)
- [/sys/class/cxl/<afu>/mode](abi-removed.md#abi-sys-class-cxl-afu-mode)
- [/sys/class/cxl/<afu>/prefault_mode](abi-removed.md#abi-sys-class-cxl-afu-prefault-mode)
- [/sys/class/cxl/<afu>/reset](abi-removed.md#abi-sys-class-cxl-afu-reset)
- [/sys/class/cxl/<afu>/api_version](abi-removed.md#abi-sys-class-cxl-afu-api-version)
- [/sys/class/cxl/<afu>/api_version_compatible](abi-removed.md#abi-sys-class-cxl-afu-api-version-compatible)
- [/sys/class/cxl/<afu>/cr<config num>/vendor](abi-removed.md#abi-sys-class-cxl-afu-cr-config-num-vendor)
- [/sys/class/cxl/<afu>/cr<config num>/device](abi-removed.md#abi-sys-class-cxl-afu-cr-config-num-device)
- [/sys/class/cxl/<afu>/cr<config num>/class](abi-removed.md#abi-sys-class-cxl-afu-cr-config-num-class)
- [/sys/class/cxl/<afu>/cr<config num>/config](abi-removed.md#abi-sys-class-cxl-afu-cr-config-num-config)
- [/sys/class/cxl/<afu>m/mmio_size](abi-removed.md#abi-sys-class-cxl-afu-m-mmio-size)
- [/sys/class/cxl/<afu>m/pp_mmio_len](abi-removed.md#abi-sys-class-cxl-afu-m-pp-mmio-len)
- [/sys/class/cxl/<afu>m/pp_mmio_off](abi-removed.md#abi-sys-class-cxl-afu-m-pp-mmio-off)
- [/sys/class/cxl/<card>/caia_version](abi-removed.md#abi-sys-class-cxl-card-caia-version)
- [/sys/class/cxl/<card>/psl_revision](abi-removed.md#abi-sys-class-cxl-card-psl-revision)
- [/sys/class/cxl/<card>/base_image](abi-removed.md#abi-sys-class-cxl-card-base-image)
- [/sys/class/cxl/<card>/image_loaded](abi-removed.md#abi-sys-class-cxl-card-image-loaded)
- [/sys/class/cxl/<card>/load_image_on_perst](abi-removed.md#abi-sys-class-cxl-card-load-image-on-perst)
- [/sys/class/cxl/<card>/reset](abi-removed.md#abi-sys-class-cxl-card-reset)
- [/sys/class/cxl/<card>/perst_reloads_same_image](abi-removed.md#abi-sys-class-cxl-card-perst-reloads-same-image)
- [/sys/class/cxl/<card>/psl_timebase_synced](abi-removed.md#abi-sys-class-cxl-card-psl-timebase-synced)
- [/sys/class/cxl/<card>/tunneled_ops_supported](abi-removed.md#abi-sys-class-cxl-card-tunneled-ops-supported)

## ABI file removed/sysfs-class-rfkill

rfkill - radio frequency (RF) connector kill switch support

For details to this subsystem look at [rfkill - RF kill switch support](../driver-api/rfkill.md).

Has the following ABI:

- [/sys/class/rfkill/rfkill[0-9]+/claim](abi-removed.md#abi-sys-class-rfkill-rfkill-0-9-claim)

## ABI file removed/sysfs-firmware-efi-vars

Has the following ABI:

- [/sys/firmware/efi/vars](abi-removed.md#abi-sys-firmware-efi-vars)

## ABI file removed/sysfs-kernel-fadump_release_opalcore

This ABI is moved to /sys/firmware/opal/mpipl/release_core.

Has the following ABI:

- [/sys/kernel/fadump_release_opalcore](abi-removed.md#abi-sys-kernel-fadump-release-opalcore)

## ABI file removed/sysfs-kernel-uids

Has the following ABI:

- [/sys/kernel/uids/<uid>/cpu_shares](abi-removed.md#abi-sys-kernel-uids-uid-cpu-shares)

## ABI file removed/sysfs-mce

Has the following ABI:

- [/sys/devices/system/machinecheck/machinecheckX/tolerant](abi-removed.md#abi-sys-devices-system-machinecheck-machinecheckx-tolerant)

## ABI file removed/sysfs-selinux-checkreqprot

Has the following ABI:

- [/sys/fs/selinux/checkreqprot](abi-removed.md#abi-sys-fs-selinux-checkreqprot)

## ABI file removed/sysfs-selinux-disable

Has the following ABI:

- [/sys/fs/selinux/disable](abi-removed.md#abi-sys-fs-selinux-disable)

## ABI file removed/video1394

Has the following ABI:

- [video1394 (a.k.a. “OHCI-1394 Video support” for FireWire)](abi-removed.md#abi-video1394-a-k-a-ohci-1394-video-support-for-firewire)
