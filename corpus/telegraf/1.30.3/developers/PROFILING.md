---
collection: telegraf
version: "1.30.3"
title: "Profiling"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/docs/developers/PROFILING.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# Profiling

This article describes how to collect performance traces and memory profiles
from Telegraf. If you are submitting this for an issue, please include the
version.txt generated below.

Use the `--pprof-addr` option to enable the profiler, the easiest way to do
this may be to add this line to `/etc/default/telegraf`:

```shell
TELEGRAF_OPTS="--pprof-addr localhost:6060"
```

Restart Telegraf to activate the profile address.

## Trace Profile

Collect a trace during the time where the performance issue is occurring.  This
example collects a 10 second trace and runs for 10 seconds:

```shell
curl 'http://localhost:6060/debug/pprof/trace?seconds=10' > trace.bin
telegraf --version > version.txt
go env GOOS GOARCH >> version.txt
```

The `trace.bin` and `version.txt` files can be sent in for analysis or, if desired, you can
analyze the trace with:

```shell
go tool trace trace.bin
```

## Memory Profile

Collect a heap memory profile:

```shell
curl 'http://localhost:6060/debug/pprof/heap' > mem.prof
telegraf --version > version.txt
go env GOOS GOARCH >> version.txt
```

Analyze:

```shell
$ go tool pprof mem.prof
(pprof) top5
```

## CPU Profile

Collect a 30s CPU profile:

```shell
curl 'http://localhost:6060/debug/pprof/profile' > cpu.prof
telegraf --version > version.txt
go env GOOS GOARCH >> version.txt
```

Analyze:

```shell
go tool pprof cpu.prof
(pprof) top5
```
