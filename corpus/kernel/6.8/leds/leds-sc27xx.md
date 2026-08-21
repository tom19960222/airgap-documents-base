---
collection: kernel
version: "6.8"
title: "Kernel driver for Spreadtrum SC27XX"
source_url: https://www.kernel.org/doc/html/v6.8/leds/leds-sc27xx.html
fetched_at: 2026-08-21T03:48:44+00:00
---
# Kernel driver for Spreadtrum SC27XX

## /sys/class/leds/<led>/hw_pattern

Specify a hardware pattern for the SC27XX LED. For the SC27XX
LED controller, it only supports 4 stages to make a single
hardware pattern, which is used to configure the rise time,
high time, fall time and low time for the breathing mode.

For the breathing mode, the SC27XX LED only expects one brightness
for the high stage. To be compatible with the hardware pattern
format, we should set brightness as 0 for rise stage, fall
stage and low stage.

- Min stage duration: 125 ms
- Max stage duration: 31875 ms

Since the stage duration step is 125 ms, the duration should be
a multiplier of 125, like 125ms, 250ms, 375ms, 500ms ... 31875ms.

Thus the format of the hardware pattern values should be:
"0 rise_duration brightness high_duration 0 fall_duration 0 low_duration".
