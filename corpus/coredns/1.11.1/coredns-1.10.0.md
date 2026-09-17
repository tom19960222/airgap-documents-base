---
collection: coredns
version: "1.11.1"
title: "coredns-1.10.0"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/notes/coredns-1.10.0.md
fetched_at: 2023-08-15T15:30:32-04:00
---
+++
title = "CoreDNS-1.10.0 Release"
description = "CoreDNS-1.10.0 Release Notes."
tags = ["Release", "1.10.0", "Notes"]
release = "1.10.0"
date = "2022-09-16T00:00:00+00:00"
author = "coredns"
+++

This release adds the new *view* plugin, enabling advanced server-block routing configurations such as split-DNS.

## Brought to You By

Ben Kochie
Chris O'Haver
Erik Johansson
John Belamaric
Marius Kimmina
Ondřej Benkovský

## Noteworthy Changes

* plugin/view: Advanced routing interface and new 'view' plugin (https://github.com/coredns/coredns/pull/5538)
* plugin/template: Add parseInt template function (https://github.com/coredns/coredns/pull/5609)
