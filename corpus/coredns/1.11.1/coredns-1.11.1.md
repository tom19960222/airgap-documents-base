---
collection: coredns
version: "1.11.1"
title: "coredns-1.11.1"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/notes/coredns-1.11.1.md
fetched_at: 2023-08-15T15:30:32-04:00
---
+++
title = "CoreDNS-1.11.1 Release"
description = "CoreDNS-1.11.1 Release Notes."
tags = ["Release", "1.11.1", "Notes"]
release = "1.11.1"
date = "2023-08-15T00:00:00+00:00"
author = "coredns"
+++

This release fixes a major performance regression introduced in 1.11.0 that affected DoT (TLS) forwarded connections.
It also adds a new option to _dnstap_ to add metadata to the dnstap extra field, and fixes a config parsing bug in _cache_.

## Brought to You By

Chris O'Haver,
P. Radha Krishna,
Yong Tang,
Yuheng,
Zhizhen He

## Noteworthy Changes

* Revert "plugin/forward: Continue waiting after receiving malformed responses (https://github.com/coredns/coredns/pull/6014)" (#6270)
* plugin/dnstap: add support for "extra" field in payload (https://github.com/coredns/coredns/pull/6226)
* plugin/cache: fix keepttl parsing (https://github.com/coredns/coredns/pull/6250)
