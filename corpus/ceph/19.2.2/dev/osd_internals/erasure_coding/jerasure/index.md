---
collection: ceph
version: "19.2.2"
title: "jerasure plugin"
source_url: https://docs.ceph.com/en/squid/dev/osd_internals/erasure_coding/jerasure/
fetched_at: 2026-07-27T16:43:11+00:00
---
# jerasure plugin

## Introduction

The parameters interpreted by the `jerasure` plugin are:

```
ceph osd erasure-code-profile set myprofile \
   directory=<dir>         \ # plugin directory absolute path
   plugin=jerasure         \ # plugin name (only jerasure)
   k=<k>                   \ # data chunks (default 2)
   m=<m>                   \ # coding chunks (default 2)
   technique=<technique>   \ # coding technique
```

The coding techniques can be chosen among *reed_sol_van*,
*reed_sol_r6_op*, *cauchy_orig*, *cauchy_good*, *liberation*,
*blaum_roth* and *liber8tion*.

The *src/erasure-code/jerasure* directory contains the
implementation. It is a wrapper around the code found at
<https://github.com/ceph/jerasure>
and <https://github.com/ceph/gf-complete> , pinned to the latest stable
version in *.gitmodules*. These repositories are copies of the
upstream repositories <http://jerasure.org/jerasure/jerasure> and
<http://jerasure.org/jerasure/gf-complete> . The difference
between the two, if any, should match pull requests against upstream.
Note that as of 2023, the `jerasure.org` web site may no longer be
legitimate and/or associated with the original project.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
