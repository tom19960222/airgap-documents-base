---
collection: kernel
version: "6.8"
title: "CPU and Device Power Management"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/pm/index.html
fetched_at: 2026-08-21T03:30:31+00:00
---
# CPU and Device Power Management

- [CPU Idle Time Management](cpuidle.md)
  - [CPU Idle Time Management Subsystem](cpuidle.md#cpu-idle-time-management-subsystem)
  - [CPU Idle Time Governors](cpuidle.md#cpu-idle-time-governors)
  - [CPU Idle Time Management Drivers](cpuidle.md#cpu-idle-time-management-drivers)
- [Device Power Management Basics](devices.md)
  - [Two Models for Device Power Management](devices.md#two-models-for-device-power-management)
  - [Interfaces for Entering System Sleep States](devices.md#interfaces-for-entering-system-sleep-states)
    - [Device Power Management Operations](devices.md#device-power-management-operations)
    - [Subsystem-Level Methods](devices.md#subsystem-level-methods)
    - [`/sys/devices/.../power/wakeup` files](devices.md#sys-devices-power-wakeup-files)
    - [`/sys/devices/.../power/control` files](devices.md#sys-devices-power-control-files)
  - [Calling Drivers to Enter and Leave System Sleep States](devices.md#calling-drivers-to-enter-and-leave-system-sleep-states)
    - [Call Sequence Guarantees](devices.md#call-sequence-guarantees)
    - [System Power Management Phases](devices.md#system-power-management-phases)
    - [Entering System Suspend](devices.md#entering-system-suspend)
    - [Leaving System Suspend](devices.md#leaving-system-suspend)
    - [Entering Hibernation](devices.md#entering-hibernation)
    - [Leaving Hibernation](devices.md#leaving-hibernation)
  - [Power Management Notifiers](devices.md#power-management-notifiers)
  - [Device Low-Power (suspend) States](devices.md#device-low-power-suspend-states)
  - [Device Power Management Domains](devices.md#device-power-management-domains)
  - [Runtime Power Management](devices.md#runtime-power-management)
    - [The `DPM_FLAG_SMART_SUSPEND` Driver Flag](devices.md#the-dpm-flag-smart-suspend-driver-flag)
    - [The `DPM_FLAG_MAY_SKIP_RESUME` Driver Flag](devices.md#the-dpm-flag-may-skip-resume-driver-flag)
- [Suspend/Hibernation Notifiers](notifiers.md)
- [Device Power Management Data Types](types.md)
