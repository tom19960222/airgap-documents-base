---
collection: kernel
version: "6.8"
title: "清除 WARN_ONCE"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_CN/admin-guide/clearing-warn-once.html
fetched_at: 2026-08-21T03:55:10+00:00
---
Chinese (Simplified)

- [English](../../../admin-guide/clearing-warn-once.md)
- [Chinese (Traditional)](../../zh_TW/admin-guide/clearing-warn-once.md)

# 清除 WARN_ONCE

WARN_ONCE / WARN_ON_ONCE / printk_once 仅仅打印一次消息.

echo 1 > /sys/kernel/debug/clear_warn_once

可以清除这种状态并且再次允许打印一次告警信息，这对于运行测试集后重现问题
很有用。
