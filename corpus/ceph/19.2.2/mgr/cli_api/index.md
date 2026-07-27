---
collection: ceph
version: "19.2.2"
title: "CLI API Commands Module"
source_url: https://docs.ceph.com/en/squid/mgr/cli_api/
fetched_at: 2026-07-27T16:40:56+00:00
---
# CLI API Commands Module

The CLI API module exposes most of the ceph-mgr Python API via CLI commands.
This API can be benchmarked.

## Enabling

Enable the `cli api` module by running the following command:

```
ceph mgr module enable cli_api
```

Ensure that the `cli api` module is enabled by running the following command:

```
ceph mgr module ls | grep cli_api
```

## Usage

This the the general form of Manager CLI commands:

```
ceph mgr cli <command> <param>
```

Print the list of servers by running the following command:

```
ceph mgr cli list_servers
```

List all available Manager module commands by running the following command:

```
ceph mgr cli --help
```

Benchmark a command, by running a command of the following form:

```
ceph mgr cli_benchmark <number of calls> <number of threads> <command> <param>
```

For example, run the following command to benchmark the command to get
`osd_map`:

```
ceph mgr cli_benchmark 100 10 get osd_map
```

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
