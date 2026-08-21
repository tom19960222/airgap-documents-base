---
collection: kernel
version: "6.8"
title: "8.1.2. Selection flags"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/v4l/v4l2-selection-flags.html
fetched_at: 2026-08-21T03:57:41+00:00
---
# 8.1.2. Selection flags

Selection flag definitions

| Flag name | id | Definition | Valid for V4L2 | Valid for V4L2 subdev |
| --- | --- | --- | --- | --- |
| `V4L2_SEL_FLAG_GE` | (1 << 0) | Suggest the driver it should choose greater or equal rectangle (in size) than was requested. Albeit the driver may choose a lesser size, it will only do so due to hardware limitations. Without this flag (and `V4L2_SEL_FLAG_LE`) the behaviour is to choose the closest possible rectangle. | Yes | Yes |
| `V4L2_SEL_FLAG_LE` | (1 << 1) | Suggest the driver it should choose lesser or equal rectangle (in size) than was requested. Albeit the driver may choose a greater size, it will only do so due to hardware limitations. | Yes | Yes |
| `V4L2_SEL_FLAG_KEEP_CONFIG` | (1 << 2) | The configuration must not be propagated to any further processing steps. If this flag is not given, the configuration is propagated inside the subdevice to all further processing steps. | No | Yes |
