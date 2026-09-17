---
collection: kernel
version: "6.17"
title: "rv-mon"
source_url: https://www.kernel.org/doc/html/v6.17/tools/rv/rv-mon.html
fetched_at: 2026-09-16T16:49:37+00:00
---
# rv-mon

## List available monitors

Manual section:
:   1

### SYNOPSIS

**rv mon** [*-h*] **monitor_name** [*-h*] [*MONITOR OPTIONS*]

### DESCRIPTION

The **rv mon** command runs the monitor named *monitor_name*. Each monitor
has its own set of options. The **rv list** command shows all available
monitors.

### OPTIONS

**-h**, **--help**

> Print help menu.

### AVAILABLE MONITORS

The **rv** tool provides the interface for a set of monitors. Use the
**rv list** command to list all available monitors.

Each monitor has its own set of options. See man **rv-mon**-*monitor_name*
for details about each specific monitor. Also, running **rv mon**
**monitor_name** **-h** display the help menu with the available
options.

### SEE ALSO

**rv**(1), **rv-mon**(1)

Linux kernel *RV* documentation:
<<https://www.kernel.org/doc/html/latest/trace/rv/index.html>>

### AUTHOR

Written by Daniel Bristot de Oliveira <[bristot@kernel.org](mailto:bristot%40kernel.org)>

### REPORTING BUGS

Report bugs to <[linux-kernel@vger.kernel.org](mailto:linux-kernel%40vger.kernel.org)>
and <[linux-trace-devel@vger.kernel.org](mailto:linux-trace-devel%40vger.kernel.org)>

### LICENSE

**rv** is Free Software licensed under the GNU GPLv2

### COPYING

Copyright (C) 2022 Red Hat, Inc. Free use of this software is granted under
the terms of the GNU Public License (GPL).
