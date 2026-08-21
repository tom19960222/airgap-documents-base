---
collection: kernel
version: "6.8"
title: "rtla-timerlat"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-timerlat.html
fetched_at: 2026-08-21T03:56:29+00:00
---
# rtla-timerlat

## Measures the operating system timer latency

Manual section
:   1

### SYNOPSIS

**rtla timerlat** [*MODE*] ...

### DESCRIPTION

The **rtla timerlat** tool is an interface for the *timerlat* tracer. The
*timerlat* tracer dispatches a kernel thread per-cpu. These threads
set a periodic timer to wake themselves up and go back to sleep. After
the wakeup, they collect and generate useful information for the
debugging of operating system timer latency.

The *timerlat* tracer outputs information in two ways. It periodically
prints the timer latency at the timer *IRQ* handler and the *Thread*
handler. It also enable the trace of the most relevant information via
**osnoise:** tracepoints.

The *timerlat* tracer outputs information in two ways. It periodically
prints the timer latency at the timer *IRQ* handler and the *Thread* handler.
It also provides information for each noise via the **osnoise:** tracepoints.
The **rtla timerlat top** mode displays a summary of the periodic output
from the *timerlat* tracer. The **rtla hist hist** mode displays a histogram
of each tracer event occurrence. For further details, please refer to the
respective man page.

### MODES

**top**

> Prints the summary from *timerlat* tracer.

**hist**

> Prints a histogram of timerlat samples.

If no *MODE* is given, the top mode is called, passing the arguments.

### OPTIONS

**-h**, **--help**

> Display the help text.

For other options, see the man page for the corresponding mode.

### SEE ALSO

**rtla-timerlat-top**(1), **rtla-timerlat-hist**(1)

*timerlat* tracer documentation: <<https://www.kernel.org/doc/html/latest/trace/timerlat-tracer.html>>

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
