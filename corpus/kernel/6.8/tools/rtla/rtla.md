---
collection: kernel
version: "6.8"
title: "rtla"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla.html
fetched_at: 2026-08-21T03:56:27+00:00
---
# rtla

## Real-time Linux Analysis tool

Manual section
:   1

### SYNOPSIS

**rtla** *COMMAND* [*OPTIONS*]

### DESCRIPTION

The **rtla** is a meta-tool that includes a set of commands that aims to
analyze the real-time properties of Linux. But instead of testing Linux
as a black box, **rtla** leverages kernel tracing capabilities to provide
precise information about the properties and root causes of unexpected
results.

### COMMANDS

**osnoise**

> Gives information about the operating system noise (osnoise).

**timerlat**

> Measures the IRQ and thread timer latency.

### OPTIONS

**-h**, **--help**

> Display the help text.

For other options, see the man page for the corresponding command.

### SEE ALSO

**rtla-osnoise**(1), **rtla-timerlat**(1)

### AUTHOR

Daniel Bristot de Oliveira <[bristot@kernel.org](mailto:bristot%40kernel.org)>

### REPORTING BUGS

Report bugs to <[linux-kernel@vger.kernel.org](mailto:linux-kernel%40vger.kernel.org)>
and <[linux-trace-devel@vger.kernel.org](mailto:linux-trace-devel%40vger.kernel.org)>

### LICENSE

**rtla** is Free Software licensed under the GNU GPLv2

### COPYING

Copyright (C) 2021 Red Hat, Inc. Free use of this software is granted under
the terms of the GNU Public License (GPL).
