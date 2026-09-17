---
collection: kernel
version: "6.17"
title: "Netfilter Sysfs variables"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netfilter-sysctl.html
fetched_at: 2026-09-16T16:41:16+00:00
---
# Netfilter Sysfs variables

## /proc/sys/net/netfilter/\* Variables:

nf_log_all_netns - BOOLEAN
:   - 0 - disabled (default)
    - not 0 - enabled

    By default, only init_net namespace can log packets into kernel log
    with LOG target; this aims to prevent containers from flooding host
    kernel log. If enabled, this target also works in other network
    namespaces. This variable is only accessible from init_net.
