---
collection: kernel
version: "6.8"
title: "Link Power Managent Policy"
source_url: https://www.kernel.org/doc/html/v6.8/scsi/link_power_management_policy.html
fetched_at: 2026-08-21T03:50:47+00:00
---
# Link Power Managent Policy

This parameter allows the user to set the link (interface) power management.
There are 3 possible options:

| Value | Effect |
| --- | --- |
| min_power | Tell the controller to try to make the link use the least possible power when possible. This may sacrifice some performance due to increased latency when coming out of lower power states. |
| max_performance | Generally, this means no power management. Tell the controller to have performance be a priority over power management. |
| medium_power | Tell the controller to enter a lower power state when possible, but do not enter the lowest power state, thus improving latency over min_power setting. |
