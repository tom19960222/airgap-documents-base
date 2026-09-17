---
collection: kernel
version: "6.17"
title: "Debugging advice for Linux Kernel developers"
source_url: https://www.kernel.org/doc/html/v6.17/process/debugging/index.html
fetched_at: 2026-09-16T16:18:39+00:00
---
# Debugging advice for Linux Kernel developers

## general guides

- [Debugging advice for driver development](driver_development_debugging_guide.md)
- [Debugging kernel and modules via gdb](gdb-kernel-debugging.md)
- [Using kgdb, kdb and the kernel debugger internals](kgdb.md)
- [Userspace debugging advice](userspace_debugging_guide.md)

## subsystem specific guides

- [Debugging and tracing in the media subsystem](media_specific_debugging_guide.md)

### General debugging advice

Depending on the issue, a different set of tools is available to track down the
problem or even to realize whether there is one in the first place.

As a first step you have to figure out what kind of issue you want to debug.
Depending on the answer, your methodology and choice of tools may vary.

## Do I need to debug with limited access?

Do you have limited access to the machine or are you unable to stop the running
execution?

In this case your debugging capability depends on built-in debugging support of
provided distribution kernel.
The [Userspace debugging advice](userspace_debugging_guide.md) provides a brief
overview over a range of possible debugging tools in that situation. You can
check the capability of your kernel, in most cases, by looking into config file
within the /boot directory.

## Do I have root access to the system?

Are you easily able to replace the module in question or to install a new
kernel?

In that case your range of available tools is a lot bigger, you can find the
tools in the [Debugging advice for driver development](driver_development_debugging_guide.md).

## Is timing a factor?

It is important to understand if the problem you want to debug manifests itself
consistently (i.e. given a set of inputs you always get the same, incorrect
output), or inconsistently. If it manifests itself inconsistently, some timing
factor might be at play. If inserting delays into the code does change the
behavior, then quite likely timing is a factor.

When timing does alter the outcome of the code execution using a simple
[`printk()`](../../core-api/printk-basics.md#c.printk "printk") for debugging purposes may not work, a similar alternative is to use
[`trace_printk()`](../../driver-api/basics.md#c.trace_printk "trace_printk") , which logs the debug messages to the trace file instead of the
kernel log.

**Copyright** ©2024 : Collabora
