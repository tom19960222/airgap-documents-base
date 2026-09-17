---
collection: kernel
version: "6.17"
title: "Guidelines"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/nova/core/guidelines.html
fetched_at: 2026-09-16T16:39:40+00:00
---
# Guidelines

This documents contains the guidelines for nova-core. Additionally, all common
guidelines of the Nova project do apply.

## Driver API

One main purpose of nova-core is to implement the abstraction around the
firmware interface of GSP and provide a firmware (version) independent API for
2nd level drivers, such as nova-drm or the vGPU manager VFIO driver.

Therefore, it is not permitted to leak firmware (version) specifics, through the
driver API, to 2nd level drivers.

## Acceptance Criteria

- To the extend possible, patches submitted to nova-core must be tested for
  regressions with all 2nd level drivers.
