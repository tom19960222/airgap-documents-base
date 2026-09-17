---
collection: kernel
version: "6.17"
title: "The Linux WatchDog Timer Power Management Guide"
source_url: https://www.kernel.org/doc/html/v6.17/watchdog/watchdog-pm.html
fetched_at: 2026-09-16T16:43:32+00:00
---
# The Linux WatchDog Timer Power Management Guide

Last reviewed: 17-Dec-2018

Wolfram Sang <[wsa+renesas@sang-engineering.com](mailto:wsa+renesas%40sang-engineering.com)>

## Introduction

This document states rules about watchdog devices and their power management
handling to ensure a uniform behaviour for Linux systems.

## Ping on resume

On resume, a watchdog timer shall be reset to its selected value to give
userspace enough time to resume. [1] [2]

[1] <https://patchwork.kernel.org/patch/10252209/>

[2] <https://patchwork.kernel.org/patch/10711625/>
