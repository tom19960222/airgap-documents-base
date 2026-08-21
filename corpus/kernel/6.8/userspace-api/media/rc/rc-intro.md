---
collection: kernel
version: "6.8"
title: "1. Introduction"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/rc/rc-intro.html
fetched_at: 2026-08-21T03:46:39+00:00
---
# 1. Introduction

Currently, most analog and digital devices have a Infrared input for
remote controllers. Each manufacturer has their own type of control. It
is not rare for the same manufacturer to ship different types of
controls, depending on the device.

A Remote Controller interface is mapped as a normal evdev/input
interface, just like a keyboard or a mouse. So, it uses all ioctls
already defined for any other input devices.

However, remove controllers are more flexible than a normal input
device, as the IR receiver (and/or transmitter) can be used in
conjunction with a wide variety of different IR remotes.

In order to allow flexibility, the Remote Controller subsystem allows
controlling the RC-specific attributes via
[the sysfs class nodes](rc-sysfs-nodes.md#remote-controllers-sysfs-nodes).
