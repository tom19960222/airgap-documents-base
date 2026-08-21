---
collection: kernel
version: "6.8"
title: "OMAP history"
source_url: https://www.kernel.org/doc/html/v6.8/arch/arm/omap/omap.html
fetched_at: 2026-08-21T03:58:48+00:00
---
# OMAP history

This file contains documentation for running mainline
kernel on omaps.

| KERNEL | NEW DEPENDENCIES |
| --- | --- |
| v4.3+ | Update is needed for custom .config files to make sure CONFIG_REGULATOR_PBIAS is enabled for MMC1 to work properly. |
| v4.18+ | Update is needed for custom .config files to make sure CONFIG_MMC_SDHCI_OMAP is enabled for all MMC instances to work in DRA7 and K2G based boards. |
