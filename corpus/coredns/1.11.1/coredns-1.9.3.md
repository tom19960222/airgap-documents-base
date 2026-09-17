---
collection: coredns
version: "1.11.1"
title: "coredns-1.9.3"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/notes/coredns-1.9.3.md
fetched_at: 2023-08-15T15:30:32-04:00
---
+++
title = "CoreDNS-1.9.3 Release"
description = "CoreDNS-1.9.3 Release Notes."
tags = ["Release", "1.9.3", "Notes"]
release = "1.9.3"
date = "2022-05-27T00:00:00+00:00"
author = "coredns"
+++

This is a release with a focus on security (CVE-2022-27191 and CVE-2022-28948) fixes. Additionally,
several feature enhancements and bug fixes have been added.

## Brought to You By

Chris O'Haver,
lobshunter,
Naveen,
Radim Hatlapatka,
RetoHaslerMGB,
Tintin,
Yong Tang

## Noteworthy Changes

* core: update gopkg.in/yaml.v3 to fix CVE-2022-28948 (https://github.com/coredns/coredns/pull/5408)
* core: update golang.org/x/crypto to fix CVE-2022-27191 (https://github.com/coredns/coredns/pull/5407)
* plugin/acl: adding a check to parse out zone info (https://github.com/coredns/coredns/pull/5387)
* plugin/dnstap: support FQDN TCP endpoint (https://github.com/coredns/coredns/pull/5377)
* plugin/errors: add `stacktrace` option to log a stacktrace during panic recovery (https://github.com/coredns/coredns/pull/5392)
* plugin/template: return SERVFAIL for zone-match regex-no-match case (https://github.com/coredns/coredns/pull/5180)
