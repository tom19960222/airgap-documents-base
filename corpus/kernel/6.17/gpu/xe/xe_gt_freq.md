---
collection: kernel
version: "6.17"
title: "Xe GT Frequency Management"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_gt_freq.html
fetched_at: 2026-09-16T16:30:49+00:00
---
# Xe GT Frequency Management

This component is responsible for the raw GT frequency management, including
the sysfs API.

Underneath, Xe enables GuC SLPC automated frequency management. GuC is then
allowed to request PCODE any frequency between the Minimum and the Maximum
selected by this component. Furthermore, it is important to highlight that
PCODE is the ultimate decision maker of the actual running frequency, based
on thermal and other running conditions.

Xe’s Freq provides a sysfs API for frequency management:

device/tile#/gt#/freq0/<item>_freq *read-only* files:

- act_freq: The actual resolved frequency decided by PCODE.
- cur_freq: The current one requested by GuC PC to the PCODE.
- rpn_freq: The Render Performance (RP) N level, which is the minimal one.
- rpa_freq: The Render Performance (RP) A level, which is the achiveable one.
  Calculated by PCODE at runtime based on multiple running conditions
- rpe_freq: The Render Performance (RP) E level, which is the efficient one.
  Calculated by PCODE at runtime based on multiple running conditions
- rp0_freq: The Render Performance (RP) 0 level, which is the maximum one.

device/tile#/gt#/freq0/<item>_freq *read-write* files:

- min_freq: Min frequency request.
- max_freq: Max frequency request.
  :   If max <= min, then freq_min becomes a fixed frequency request.

## Internal API

int xe_gt_freq_init(struct xe_gt \*gt)
:   Initialize Xe Freq component

**Parameters**

`struct xe_gt *gt`
:   Xe GT object

**Description**

It needs to be initialized after GT Sysfs and GuC PC components are ready.

**Return**

Returns error value for failure and 0 for success.
