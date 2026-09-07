---
collection: ceph
version: "20.2.4"
title: "CLI API Commands Module"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/cli_api.rst
fetched_at: 2026-08-18T01:32:45Z
---
# CLI API Commands Module

The CLI API module exposes most of the ceph-mgr Python API via CLI commands.
This API can be benchmarked.

## Enabling

Enable the `cli api` module by running the following command:

```bash
ceph mgr module enable cli_api
```

Ensure that the `cli api` module is enabled by running the following command:

```bash
ceph mgr module ls | grep cli_api
```

## Usage

This the the general form of Manager CLI commands:

```bash
ceph mgr cli <command> <param>
```

Print the list of servers by running the following command:

```bash
ceph mgr cli list_servers
```

List all available Manager module commands by running the following command:

```bash
ceph mgr cli --help
```

Benchmark a command, by running a command of the following form:

```bash
ceph mgr cli_benchmark <number of calls> <number of threads> <command> <param>
```

For example, run the following command to benchmark the command to get
`osd_map`:

```bash
ceph mgr cli_benchmark 100 10 get osd_map
```
