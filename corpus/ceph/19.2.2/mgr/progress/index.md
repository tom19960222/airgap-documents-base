---
collection: ceph
version: "19.2.2"
title: "Progress Module"
source_url: https://docs.ceph.com/en/squid/mgr/progress/
fetched_at: 2026-07-27T16:40:56+00:00
---
# Progress Module

The progress module is used to inform users about the recovery progress of PGs
(Placement Groups) that are affected by events such as (1) OSDs being marked
in or out and (2) `pg_autoscaler` trying to match the target PG number.

The `ceph -status` (or `ceph -s`) command returns “Global Recovery
Progress”, which reports the overall recovery progress of PGs and is based on
the number of PGs that are in the `active+clean` state.

## Enabling

The *progress* module is enabled by default, but it can be enabled manually by
running the following command:

```
ceph progress on
```

The module can be disabled at anytime by running the following command:

```
ceph progress off
```

## Commands

Show the summary of all the ongoing and completed events and their duration:

```
ceph progress
```

Show the summary of ongoing and completed events in JSON format:

```
ceph progress json
```

Clear all ongoing and completed events:

```
ceph progress clear
```

## PG Recovery Event

An event for each PG affected by recovery can be shown in `ceph progress`.
This is optional, and is disabled by default due to CPU overhead that may
adversely affect the Monitors:

```
ceph config set mgr mgr/progress/allow_pg_recovery_event true
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
