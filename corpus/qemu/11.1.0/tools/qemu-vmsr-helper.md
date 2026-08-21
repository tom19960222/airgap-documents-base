---
collection: qemu
version: "11.1.0"
title: "QEMU virtual RAPL MSR helper"
source_url: https://www.qemu.org/docs/master/tools/qemu-vmsr-helper.html
fetched_at: 2026-08-21T03:21:59+00:00
---
# QEMU virtual RAPL MSR helper

## Synopsis

**qemu-vmsr-helper** [*OPTION*]

## Description

Implements the virtual RAPL MSR helper for QEMU.

Accessing the RAPL (Running Average Power Limit) MSR enables the RAPL powercap
driver to advertise and monitor the power consumption or accumulated energy
consumption of different power domains, such as CPU packages, DRAM, and other
components when available.

However those registers are accessible under privileged access (CAP_SYS_RAWIO).
QEMU can use an external helper to access those privileged registers.

**qemu-vmsr-helper** is that external helper; it creates a listener
socket which will accept incoming connections for communication with QEMU.

If you want to run VMs in a setup like this, this helper should be started as a
system service, and you should read the QEMU manual section on “RAPL MSR
support” to find out how to configure QEMU to connect to the socket created by
**qemu-vmsr-helper**.

After connecting to the socket, **qemu-vmsr-helper** can
optionally drop root privileges, except for those capabilities that
are needed for its operation.

**qemu-vmsr-helper** can also use the systemd socket activation
protocol. In this case, the systemd socket unit should specify a
Unix stream socket, like this:

```
[Socket]
ListenStream=/var/run/qemu-vmsr-helper.sock
```

## Options

-d, --daemon
:   run in the background (and create a PID file)

-q, --quiet
:   decrease verbosity

-v, --verbose
:   increase verbosity

-f, --pidfile=PATH
:   PID file when running as a daemon. By default the PID file
    is created in the system runtime state directory, for example
    `/var/run/qemu-vmsr-helper.pid`.

-k, --socket=PATH
:   path to the socket. By default the socket is created in
    the system runtime state directory, for example
    `/var/run/qemu-vmsr-helper.sock`.

-T, --trace [[enable=]PATTERN][,events=FILE][,file=FILE]
:   Specify tracing options.

    `[enable=]PATTERN`

    > Immediately enable events matching *PATTERN*
    > (either event name or a globbing pattern). This option is only
    > available if QEMU has been compiled with the `simple`, `log`
    > or `ftrace` tracing backend. To specify multiple events or patterns,
    > specify the `-trace` option multiple times.
    >
    > Use `-trace help` to print a list of names of trace points.

    `events=FILE`

    > Immediately enable events listed in *FILE*.
    > The file must contain one event name (as listed in the `trace-events-all`
    > file) per line; globbing patterns are accepted too. This option is only
    > available if QEMU has been compiled with the `simple`, `log` or
    > `ftrace` tracing backend.

    `file=FILE`

    > Log output traces to *FILE*.
    > This option is only available if QEMU has been compiled with
    > the `simple` tracing backend.

-u, --user=USER
:   user to drop privileges to

-g, --group=GROUP
:   group to drop privileges to

-h, --help
:   Display a help message and exit.

-V, --version
:   Display version information and exit.
