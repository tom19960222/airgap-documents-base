---
collection: kernel
version: "6.8"
title: "rtla-osnoise-top"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-osnoise-top.html
fetched_at: 2026-08-21T03:56:28+00:00
---
# rtla-osnoise-top

## Display a summary of the operating system noise

Manual section
:   1

### SYNOPSIS

**rtla osnoise top** [*OPTIONS*]

### DESCRIPTION

The **rtla osnoise** tool is an interface for the *osnoise* tracer. The
*osnoise* tracer dispatches a kernel thread per-cpu. These threads read the
time in a loop while with preemption, softirq and IRQs enabled, thus
allowing all the sources of operating system noise during its execution.
The *osnoise*'s tracer threads take note of the delta between each time
read, along with an interference counter of all sources of interference.
At the end of each period, the *osnoise* tracer displays a summary of
the results.

**rtla osnoise top** collects the periodic summary from the *osnoise* tracer,
including the counters of the occurrence of the interference source,
displaying the results in a user-friendly format.

The tool also allows many configurations of the *osnoise* tracer and the
collection of the tracer output.

### OPTIONS

**-a**, **--auto** *us*

> Set the automatic trace mode. This mode sets some commonly used options
> while debugging the system. It is equivalent to use **-s** *us* **-T 1 -t**.

**-p**, **--period** *us*

> Set the *osnoise* tracer period in microseconds.

**-r**, **--runtime** *us*

> Set the *osnoise* tracer runtime in microseconds.

**-s**, **--stop** *us*

> Stop the trace if a single sample is higher than the argument in microseconds.
> If **-T** is set, it will also save the trace to the output.

**-S**, **--stop-total** *us*

> Stop the trace if the total sample is higher than the argument in microseconds.
> If **-T** is set, it will also save the trace to the output.

**-T**, **--threshold** *us*

> Specify the minimum delta between two time reads to be considered noise.
> The default threshold is *5 us*.

**-q**, **--quiet**

> Print only a summary at the end of the session.

**-c**, **--cpus** *cpu-list*

> Set the osnoise tracer to run the sample threads in the cpu-list.

**-H**, **--house-keeping** *cpu-list*

> Run rtla control threads only on the given cpu-list.

**-d**, **--duration** *time[s|m|h|d]*

> Set the duration of the session.

**-D**, **--debug**

> Print debug info.

**-t**, **--trace**[*=file*]

> Save the stopped trace to [*file|osnoise_trace.txt*].

**-e**, **--event** *sys:event*

> Enable an event in the trace (**-t**) session. The argument can be a specific event, e.g., **-e** *sched:sched_switch*, or all events of a system group, e.g., **-e** *sched*. Multiple **-e** are allowed. It is only active when **-t** or **-a** are set.

**--filter** *<filter>*

> Filter the previous **-e** *sys:event* event with *<filter>*. For further information about event filtering see <https://www.kernel.org/doc/html/latest/trace/events.html#event-filtering>.

**--trigger** *<trigger>*
:   Enable a trace event trigger to the previous **-e** *sys:event*.
    If the *hist:* trigger is activated, the output histogram will be automatically saved to a file named *system_event_hist.txt*.
    For example, the command:

    rtla <command> <mode> -t -e osnoise:irq_noise --trigger="hist:key=desc,duration/1000:sort=desc,duration/1000:vals=hitcount"

    Will automatically save the content of the histogram associated to *osnoise:irq_noise* event in *osnoise_irq_noise_hist.txt*.

    For further information about event trigger see <https://www.kernel.org/doc/html/latest/trace/events.html#event-triggers>.

**-P**, **--priority** *o:prio|r:prio|f:prio|d:runtime:period*

> Set scheduling parameters to the osnoise tracer threads, the format to set the priority are:
>
> - *o:prio* - use SCHED_OTHER with *prio*;
> - *r:prio* - use SCHED_RR with *prio*;
> - *f:prio* - use SCHED_FIFO with *prio*;
> - *d:runtime[us|ms|s]:period[us|ms|s]* - use SCHED_DEADLINE with *runtime* and *period* in nanoseconds.

**-C**, **--cgroup**[*=cgroup*]

> Set a *cgroup* to the tracer's threads. If the **-C** option is passed without arguments, the tracer's thread will inherit **rtla**'s *cgroup*. Otherwise, the threads will be placed on the *cgroup* passed to the option.

**-h**, **--help**

> Print help menu.

### EXAMPLE

In the example below, the **rtla osnoise top** tool is set to run with a
real-time priority *FIFO:1*, on CPUs *0-3*, for *900ms* at each period
(*1s* by default). The reason for reducing the runtime is to avoid starving
the rtla tool. The tool is also set to run for *one minute* and to display
a summary of the report at the end of the session:

```
[root@f34 ~]# rtla osnoise top -P F:1 -c 0-3 -r 900000 -d 1M -q
                                        Operating System Noise
duration:   0 00:01:00 | time is in us
CPU Period       Runtime        Noise  % CPU Aval   Max Noise   Max Single          HW          NMI          IRQ      Softirq       Thread
  0 #59         53100000       304896    99.42580        6978           56         549            0        53111         1590           13
  1 #59         53100000       338339    99.36282        8092           24         399            0        53130         1448           31
  2 #59         53100000       290842    99.45227        6582           39         855            0        53110         1406           12
  3 #59         53100000       204935    99.61405        6251           33         290            0        53156         1460           12
```

### SEE ALSO

**rtla-osnoise**(1), **rtla-osnoise-hist**(1)

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
