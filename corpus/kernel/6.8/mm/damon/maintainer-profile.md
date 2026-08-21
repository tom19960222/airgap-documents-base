---
collection: kernel
version: "6.8"
title: "DAMON Maintainer Entry Profile"
source_url: https://www.kernel.org/doc/html/v6.8/mm/damon/maintainer-profile.html
fetched_at: 2026-08-21T03:42:51+00:00
---
# DAMON Maintainer Entry Profile

The DAMON subsystem covers the files that are listed in 'DATA ACCESS MONITOR'
section of 'MAINTAINERS' file.

The mailing lists for the subsystem are [damon@lists.linux.dev](mailto:damon%40lists.linux.dev) and
[linux-mm@kvack.org](mailto:linux-mm%40kvack.org). Patches should be made against the mm-unstable tree [1](maintainer-profile.md#id9)
whenever possible and posted to the mailing lists.

## SCM Trees

There are multiple Linux trees for DAMON development. Patches under
development or testing are queued in damon/next [2](maintainer-profile.md#id10) by the DAMON maintainer.
Sufficiently reviewed patches will be queued in mm-unstable [1](maintainer-profile.md#id9) by the memory
management subsystem maintainer. After more sufficient tests, the patches will
be queued in mm-stable [3](maintainer-profile.md#id11) , and finally pull-requested to the mainline by the
memory management subsystem maintainer.

Note again the patches for review should be made against the mm-unstable
tree[1] whenever possible. damon/next is only for preview of others' works in
progress.

## Submit checklist addendum

When making DAMON changes, you should do below.

- Build changes related outputs including kernel and documents.
- Ensure the builds introduce no new errors or warnings.
- Run and ensure no new failures for DAMON selftests [4](maintainer-profile.md#id12) and kunittests [5](maintainer-profile.md#id13) .

Further doing below and putting the results will be helpful.

- Run damon-tests/corr [6](maintainer-profile.md#id14) for normal changes.
- Run damon-tests/perf [7](maintainer-profile.md#id15) for performance changes.

## Key cycle dates

Patches can be sent anytime. Key cycle dates of the mm-unstable[1] and
mm-stable[3] trees depend on the memory management subsystem maintainer.

## Review cadence

The DAMON maintainer does the work on the usual work hour (09:00 to 17:00,
Mon-Fri) in PST. The response to patches will occasionally be slow. Do not
hesitate to send a ping if you have not heard back within a week of sending a
patch.

1([1](maintainer-profile.md#id1),[2](maintainer-profile.md#id3))
:   <https://git.kernel.org/akpm/mm/h/mm-unstable>

[2](maintainer-profile.md#id2)
:   <https://git.kernel.org/sj/h/damon/next>

[3](maintainer-profile.md#id4)
:   <https://git.kernel.org/akpm/mm/h/mm-stable>

[4](maintainer-profile.md#id5)
:   <https://github.com/awslabs/damon-tests/blob/master/corr/run.sh#L49>

[5](maintainer-profile.md#id6)
:   <https://github.com/awslabs/damon-tests/blob/master/corr/tests/kunit.sh>

[6](maintainer-profile.md#id7)
:   <https://github.com/awslabs/damon-tests/tree/master/corr>

[7](maintainer-profile.md#id8)
:   <https://github.com/awslabs/damon-tests/tree/master/perf>
