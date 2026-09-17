---
collection: kernel
version: "6.17"
title: "HTM (Hardware Trace Macro)"
source_url: https://www.kernel.org/doc/html/v6.17/arch/powerpc/htm.html
fetched_at: 2026-09-16T16:24:39+00:00
---
# [HTM (Hardware Trace Macro)](htm.md#id1)

Athira Rajeev, 2 Mar 2025

Contents

- [HTM (Hardware Trace Macro)](htm.md#htm-hardware-trace-macro)

  - [Basic overview](htm.md#basic-overview)
  - [HTM debugfs example usage](htm.md#htm-debugfs-example-usage)
  - [Read the HTM trace data](htm.md#read-the-htm-trace-data)
  - [Benefits of using HTM debugfs interface](htm.md#benefits-of-using-htm-debugfs-interface)

## [Basic overview](htm.md#id2)

H_HTM is used as an interface for executing Hardware Trace Macro (HTM)
functions, including setup, configuration, control and dumping of the HTM data.
For using HTM, it is required to setup HTM buffers and HTM operations can
be controlled using the H_HTM hcall. The hcall can be invoked for any core/chip
of the system from within a partition itself. To use this feature, a debugfs
folder called “htmdump” is present under /sys/kernel/debug/powerpc.

## [HTM debugfs example usage](htm.md#id3)

```sh
#  ls /sys/kernel/debug/powerpc/htmdump/
coreindexonchip  htmcaps  htmconfigure  htmflags  htminfo  htmsetup
htmstart  htmstatus  htmtype  nodalchipindex  nodeindex  trace
```

Details on each file:

- nodeindex, nodalchipindex, coreindexonchip specifies which partition to configure the HTM for.
- htmtype: specifies the type of HTM. Supported target is hardwareTarget.
- trace: is to read the HTM data.
- htmconfigure: Configure/Deconfigure the HTM. Writing 1 to the file will configure the trace, writing 0 to the file will do deconfigure.
- htmstart: start/Stop the HTM. Writing 1 to the file will start the tracing, writing 0 to the file will stop the tracing.
- htmstatus: get the status of HTM. This is needed to understand the HTM state after each operation.
- htmsetup: set the HTM buffer size. Size of HTM buffer is in power of 2
- htminfo: provides the system processor configuration details. This is needed to understand the appropriate values for nodeindex, nodalchipindex, coreindexonchip.
- htmcaps : provides the HTM capabilities like minimum/maximum buffer size, what kind of tracing the HTM supports etc.
- htmflags : allows to pass flags to hcall. Currently supports controlling the wrapping of HTM buffer.

To see the system processor configuration details:

```sh
# cat /sys/kernel/debug/powerpc/htmdump/htminfo > htminfo_file
```

The result can be interpreted using hexdump.

To collect HTM traces for a partition represented by nodeindex as
zero, nodalchipindex as 1 and coreindexonchip as 12

```sh
# cd /sys/kernel/debug/powerpc/htmdump/
# echo 2 > htmtype
# echo 33 > htmsetup ( sets 8GB memory for HTM buffer, number is size in power of 2 )
```

This requires a CEC reboot to get the HTM buffers allocated.

```sh
# cd /sys/kernel/debug/powerpc/htmdump/
# echo 2 > htmtype
# echo 0 > nodeindex
# echo 1 > nodalchipindex
# echo 12 > coreindexonchip
# echo 1 > htmflags     # to set noWrap for HTM buffers
# echo 1 > htmconfigure # Configure the HTM
# echo 1 > htmstart     # Start the HTM
# echo 0 > htmstart     # Stop the HTM
# echo 0 > htmconfigure # Deconfigure the HTM
# cat htmstatus         # Dump the status of HTM entries as data
```

Above will set the htmtype and core details, followed by executing respective HTM operation.

## [Read the HTM trace data](htm.md#id4)

After starting the trace collection, run the workload
of interest. Stop the trace collection after required period
of time, and read the trace file.

```sh
# cat /sys/kernel/debug/powerpc/htmdump/trace > trace_file
```

This trace file will contain the relevant instruction traces
collected during the workload execution. And can be used as
input file for trace decoders to understand data.

## [Benefits of using HTM debugfs interface](htm.md#id5)

It is now possible to collect traces for a particular core/chip
from within any partition of the system and decode it. Through
this enablement, a small partition can be dedicated to collect the
trace data and analyze to provide important information for Performance
analysis, Software tuning, or Hardware debug.
