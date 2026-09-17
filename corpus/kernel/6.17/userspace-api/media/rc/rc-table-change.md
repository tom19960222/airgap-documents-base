---
collection: kernel
version: "6.17"
title: "5. Changing default Remote Controller mappings"
source_url: https://www.kernel.org/doc/html/v6.17/userspace-api/media/rc/rc-table-change.html
fetched_at: 2026-09-16T16:56:07+00:00
---
# 5. Changing default Remote Controller mappings

The event interface provides two ioctls to be used against the
/dev/input/event device, to allow changing the default keymapping.

This program demonstrates how to replace the keymap tables.

- [5.1. file: uapi/v4l/keytable.c](keytable.c.md)
