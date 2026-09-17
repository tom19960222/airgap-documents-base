---
collection: kernel
version: "6.17"
title: "9.1.4. The Samsung S5P/EXYNOS4 FIMC driver"
source_url: https://www.kernel.org/doc/html/v6.17/driver-api/media/drivers/fimc-devel.html
fetched_at: 2026-09-16T16:37:20+00:00
---
# 9.1.4. The Samsung S5P/EXYNOS4 FIMC driver

Copyright © 2012 - 2013 Samsung Electronics Co., Ltd.

## 9.1.4.1. Files partitioning

- media device driver

  drivers/media/platform/samsung/exynos4-is/media-dev.[ch]
- camera capture video device driver

  drivers/media/platform/samsung/exynos4-is/fimc-capture.c
- MIPI-CSI2 receiver subdev

  drivers/media/platform/samsung/exynos4-is/mipi-csis.[ch]
- video post-processor (mem-to-mem)

  drivers/media/platform/samsung/exynos4-is/fimc-core.c
- common files

  drivers/media/platform/samsung/exynos4-is/fimc-core.h
  drivers/media/platform/samsung/exynos4-is/fimc-reg.h
  drivers/media/platform/samsung/exynos4-is/regs-fimc.h
