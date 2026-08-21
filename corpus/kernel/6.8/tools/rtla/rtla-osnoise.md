---
collection: kernel
version: "6.8"
title: "rtla-osnoise"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-osnoise.html
fetched_at: 2026-08-21T03:56:27+00:00
---
# rtla-osnoise

## Measure the operating system noise

Manual section
:   1

### SYNOPSIS

**rtla osnoise** [*MODE*] ...

### DESCRIPTION

The **rtla osnoise** tool is an interface for the *osnoise* tracer. The
*osnoise* tracer dispatches a kernel thread per-cpu. These threads read the
time in a loop while with preemption, softirq and IRQs enabled, thus
allowing all the sources of operating system noise during its execution.
The *osnoise*'s tracer threads take note of the delta between each time
read, along with an interference counter of all sources of interference.
At the end of each period, the *osnoise* tracer displays a summary of
the results.

The *osnoise* tracer outputs information in two ways. It periodically prints
a summary of the noise of the operating system, including the counters of
the occurrence of the source of interference. It also provides information
for each noise via the **osnoise:** tracepoints. The **rtla osnoise top**
mode displays information about the periodic summary from the *osnoise* tracer.
The **rtla osnoise hist** mode displays information about the noise using
the **osnoise:** tracepoints. For further details, please refer to the
respective man page.

### MODES

**top**

> Prints the summary from osnoise tracer.

**hist**

> Prints a histogram of osnoise samples.

If no MODE is given, the top mode is called, passing the arguments.

### OPTIONS

**-h**, **--help**

> Display the help text.

For other options, see the man page for the corresponding mode.

### SEE ALSO

**rtla-osnoise-top**(1), **rtla-osnoise-hist**(1)

Osnoise tracer documentation: <<https://www.kernel.org/doc/html/latest/trace/osnoise-tracer.html>>

### AUTHOR

Written by Daniel Bristot de Oliveira <[bristot@kernel.org](mailto:bristot%40kernel.org)>

### REPORTING BUGS

Report bugs to <[linux-kernel@vger.kernel.org](mailto:linux-kernel%40vger.kernel.org)>
and <[linux-trace-devel@vger.kernel.org](mailto:linux-trace-devel%40vger.kernel.org)>

### LICENSE

**rtla** is Free Software licensed under the GNU GPLv2

### COPYING

Copyright (C) 2021 Red Hat, Inc. Free use of this software is granted under
the terms of the GNU Public License (GPL).
