---
collection: ceph
version: "19.2.2"
title: "Issue Tracker"
source_url: https://docs.ceph.com/en/squid/dev/developer_guide/issue-tracker/
fetched_at: 2026-07-27T16:41:08+00:00
---
# Issue Tracker

See [Redmine Issue Tracker](https://tracker.ceph.com) for a brief introduction to the Ceph Issue
Tracker.

Ceph developers use the issue tracker to

1. keep track of issues - bugs, fix requests, feature requests, backport
requests, etc.

2. communicate with other developers and keep them informed as work
on the issues progresses.

## Issue tracker conventions

When you start working on an existing issue, it’s nice to let the other
developers know this - to avoid duplication of labor. Typically, this is
done by changing the `Assignee` field (to yourself) and changing the
`Status` to *In progress*. Newcomers to the Ceph community typically do
not have sufficient privileges to update these fields, however: they can
simply update the issue with a brief note.

Meanings of some commonly used statuses

| Status | Meaning |
| --- | --- |
| New | Initial status |
| In Progress | Somebody is working on it |
| Need Review | Pull request is open with a fix |
| Pending Backport | Fix has been merged, backport(s) pending |
| Resolved | Fix and backports (if any) have been merged |

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
