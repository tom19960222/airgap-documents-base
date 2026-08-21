---
collection: qemu
version: "11.1.0"
title: "QEMU SystemTap trace tool"
source_url: https://www.qemu.org/docs/master/tools/qemu-trace-stap.html
fetched_at: 2026-08-21T03:21:58+00:00
---
# QEMU SystemTap trace tool

## Synopsis

**qemu-trace-stap** [*GLOBAL-OPTIONS*] *COMMAND* [*COMMAND-OPTIONS*] *ARGS*…

## Description

The `qemu-trace-stap` program facilitates tracing of the execution
of QEMU emulators using SystemTap.

It is required to have the SystemTap runtime environment installed to use
this program, since it is a wrapper around execution of the `stap`
program.

## Options

The following global options may be used regardless of which command
is executed:

--verbose, -v
:   Display verbose information about command execution.

The following commands are valid:

list BINARY PATTERN...
:   List all the probe names provided by *BINARY* that match
    *PATTERN*.

    If *BINARY* is not an absolute path, it will be located by searching
    the directories listed in the `$PATH` environment variable.

    *PATTERN* is a plain string that is used to filter the results of
    this command. It may optionally contain a `*` wildcard to facilitate
    matching multiple probes without listing each one explicitly. Multiple
    *PATTERN* arguments may be given, causing listing of probes that match
    any of the listed names. If no *PATTERN* is given, the all possible
    probes will be listed.

    For example, to list all probes available in the qemu-system-x86_64
    binary:

    ```
    $ qemu-trace-stap list qemu-system-x86_64
    ```

    To filter the list to only cover probes related to QEMU’s cryptographic
    subsystem, in a binary outside `$PATH`

    ```
    $ qemu-trace-stap list /opt/qemu/11.1.50/bin/qemu-system-x86_64 'qcrypto*'
    ```

run OPTIONS BINARY PATTERN...
:   Run a trace session, printing formatted output any time a process that is
    executing *BINARY* triggers a probe matching *PATTERN*.

    If *BINARY* is not an absolute path, it will be located by searching
    the directories listed in the `$PATH` environment variable.

    *PATTERN* is a plain string that matches a probe name shown by the
    *LIST* command. It may optionally contain a `*` wildcard to
    facilitate matching multiple probes without listing each one explicitly.
    Multiple *PATTERN* arguments may be given, causing all matching probes
    to be monitored. At least one *PATTERN* is required, since stap is not
    capable of tracing all known QEMU probes concurrently without overflowing
    its trace buffer.

    Invocation of this command does not need to be synchronized with
    invocation of the QEMU process(es). It will match probes on all
    existing running processes and all future launched processes,
    unless told to only monitor a specific process.

    Valid command specific options are:

    --pid=PID, -p PID
    :   Restrict the tracing session so that it only triggers for the process
        identified by *PID*.

    For example, to monitor all processes executing qemu-system-x86_64
    as found on `$PATH`, displaying all I/O related probes:

    ```
    $ qemu-trace-stap run qemu-system-x86_64 'qio*'
    ```

    To monitor only the QEMU process with PID 1732

    ```
    $ qemu-trace-stap run --pid=1732 qemu-system-x86_64 'qio*'
    ```

    To monitor QEMU processes running an alternative binary outside of
    `$PATH`, displaying verbose information about setup of the
    tracing environment:

    ```
    $ qemu-trace-stap -v run /opt/qemu/11.1.50/bin/qemu-system-x86_64 'qio*'
    ```

## See also

*qemu(1)*, *stap(1)*
