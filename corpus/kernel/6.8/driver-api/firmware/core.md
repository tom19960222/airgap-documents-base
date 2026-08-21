---
collection: kernel
version: "6.8"
title: "Firmware API core features"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/firmware/core.html
fetched_at: 2026-08-21T03:32:12+00:00
---
# Firmware API core features

The firmware API has a rich set of core features available. This section
documents these features.

- [Firmware search paths](fw_search_path.md)
- [Built-in firmware](built-in-fw.md)
- [Firmware cache](firmware_cache.md)
- [Direct filesystem lookup](direct-fs-lookup.md)
  - [Firmware and initramfs](direct-fs-lookup.md#firmware-and-initramfs)
- [Fallback mechanisms](fallback-mechanisms.md)
  - [Justifying the firmware fallback mechanism](fallback-mechanisms.md#justifying-the-firmware-fallback-mechanism)
  - [Types of fallback mechanisms](fallback-mechanisms.md#types-of-fallback-mechanisms)
  - [Firmware sysfs loading facility](fallback-mechanisms.md#firmware-sysfs-loading-facility)
    - [firmware_fallback_sysfs](fallback-mechanisms.md#firmware-fallback-sysfs)
  - [Firmware kobject uevent fallback mechanism](fallback-mechanisms.md#firmware-kobject-uevent-fallback-mechanism)
  - [Firmware custom fallback mechanism](fallback-mechanisms.md#firmware-custom-fallback-mechanism)
  - [Firmware fallback timeout](fallback-mechanisms.md#firmware-fallback-timeout)
  - [EFI embedded firmware fallback mechanism](fallback-mechanisms.md#efi-embedded-firmware-fallback-mechanism)
    - [Example how to check for and extract embedded firmware](fallback-mechanisms.md#example-how-to-check-for-and-extract-embedded-firmware)
- [Firmware lookup order](lookup-order.md)
- [Firmware Guidelines](firmware-usage-guidelines.md)
