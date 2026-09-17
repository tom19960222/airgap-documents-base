---
collection: coredns
version: "1.11.1"
title: "coredns-1.0.2"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/notes/coredns-1.0.2.md
fetched_at: 2023-08-15T15:30:32-04:00
---
+++
title = "CoreDNS-1.0.2 Release"
description = "CoreDNS-1.0.2 Release Notes."
tags = ["Release", "1.0.2", "Notes"]
draft = false
release = "1.0.2"
date = "2017-12-31T09:06:29+00:00"
author = "coredns"
+++

We are pleased to announce the [release](https://github.com/coredns/coredns/releases/tag/v1.0.2) of CoreDNS-1.0.2!
This release can be summarized as "help external plugin developers" as most changes are geared
towards exposing CoreDNS functionality to make this as easy as possible. Is also a fairly small
release.

## Core

Expose the directives list, so that external plugins can be easily added without mucking with
CoreDNS code, see the [pull request](https://github.com/coredns/coredns/pull/1315) for details.

Fix crash when there are no handlers that can actually serve queries, i.e. a Corefile with only
*debug* and *pprof* for instance.

## Plugins

* [*metrics*](/plugins/metrics) has a New function to help external plugin developers.
* [*health*](/plugins/health) plugin now checks all plugins for a `health.Healther` implementation and will export health for those plugins that do. Again helps external plugin developers.
* [*rewrite*](/plugins/rewrite) gained regular expression and substring-matching support.

## Contributors

The following people helped with getting this release done:
Brad Beam,
Francois Tur,
Frederic Hemberger,
James Hartig,
Max Schmitt,
Miek Gieben,
Paul Greenberg,
Yong Tang.

If you want to help, please check out one of the
[issues](https://github.com/coredns/coredns/issues/) and start coding! For documentation and help,
see our [community page](https://coredns.io/community/).
