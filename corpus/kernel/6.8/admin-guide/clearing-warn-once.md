---
collection: kernel
version: "6.8"
title: "Clearing WARN_ONCE"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/clearing-warn-once.html
fetched_at: 2026-08-21T03:34:42+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/admin-guide/clearing-warn-once.md)
- [Chinese (Traditional)](../translations/zh_TW/admin-guide/clearing-warn-once.md)

# Clearing WARN_ONCE

WARN_ONCE / WARN_ON_ONCE / printk_once only emit a message once.

echo 1 > /sys/kernel/debug/clear_warn_once

clears the state and allows the warnings to print once again.
This can be useful after test suite runs to reproduce problems.
