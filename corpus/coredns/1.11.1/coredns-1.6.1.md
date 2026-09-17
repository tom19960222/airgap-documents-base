---
collection: coredns
version: "1.11.1"
title: "Plugins"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/notes/coredns-1.6.1.md
fetched_at: 2023-08-15T15:30:32-04:00
---
+++
title = "CoreDNS-1.6.1 Release"
description = "CoreDNS-1.6.1 Release Notes."
tags = ["Release", "1.6.1", "Notes"]
release = "1.6.1"
date = 2019-08-02T14:35:47+01:00
author = "coredns"
+++

The CoreDNS team has released
[CoreDNS-1.6.1](https://github.com/coredns/coredns/releases/tag/v1.6.1).

This is a small (bug fix) release.

# Plugins

* Fix a panic in the [*hosts*](/plugins/hosts) plugin.
* The [*reload*](/plugins/reload) now detects changes in files imported from the main Corefile.
* [*route53*](/plugins/route53) increases the paging size when talking to the AWS API, this
  decreases the chances of getting throttled.

## Brought to You By

Alan,
AllenZMC,
dzzg,
Erik Wilson,
Matt Kulka,
Miek Gieben,
Yong Tang.

## Noteworthy Changes

core: log panics (https://github.com/coredns/coredns/pull/3072)
plugin/hosts: create inline map in setup (https://github.com/coredns/coredns/pull/3071)
plugin/reload: Graceful reload of imported files (https://github.com/coredns/coredns/pull/3068)
plugin/route53: Increase ListResourceRecordSets paging size. (https://github.com/coredns/coredns/pull/3073)
