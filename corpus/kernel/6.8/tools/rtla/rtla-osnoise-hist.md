---
collection: kernel
version: "6.8"
title: "rtla-osnoise-hist"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-osnoise-hist.html
fetched_at: 2026-08-21T03:56:28+00:00
---
# rtla-osnoise-hist

## Display a histogram of the osnoise tracer samples

Manual section
:   1

### SYNOPSIS

**rtla osnoise hist** [*OPTIONS*]

### DESCRIPTION

The **rtla osnoise** tool is an interface for the *osnoise* tracer. The
*osnoise* tracer dispatches a kernel thread per-cpu. These threads read the
time in a loop while with preemption, softirq and IRQs enabled, thus
allowing all the sources of operating system noise during its execution.
The *osnoise*'s tracer threads take note of the delta between each time
read, along with an interference counter of all sources of interference.
At the end of each period, the *osnoise* tracer displays a summary of
the results.

The **rtla osnoise hist** tool collects all **osnoise:sample_threshold**
occurrence in a histogram, displaying the results in a user-friendly way.
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

**-b**, **--bucket-size** *N*

> Set the histogram bucket size (default *1*).

**-E**, **--entries** *N*

> Set the number of entries of the histogram (default 256).

**--no-header**

> Do not print header.

**--no-summary**

> Do not print summary.

**--no-index**

> Do not print index.

**--with-zeros**

> Print zero only entries.

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

In the example below, *osnoise* tracer threads are set to run with real-time
priority *FIFO:1*, on CPUs *0-11*, for *900ms* at each period (*1s* by
default). The reason for reducing the runtime is to avoid starving the
**rtla** tool. The tool is also set to run for *one minute*. The output
histogram is set to group outputs in buckets of *10us* and *25* entries:

```
[root@f34 ~/]# rtla osnoise hist -P F:1 -c 0-11 -r 900000 -d 1M -b 10 -E 25
# RTLA osnoise histogram
# Time unit is microseconds (us)
# Duration:   0 00:01:00
Index   CPU-000   CPU-001   CPU-002   CPU-003   CPU-004   CPU-005   CPU-006   CPU-007   CPU-008   CPU-009   CPU-010   CPU-011
0         42982     46287     51779     53740     52024     44817     49898     36500     50408     50128     49523     52377
10        12224      8356      2912       878      2667     10155      4573     18894      4214      4836      5708      2413
20            8         5        12         2        13        24        20        41        29        53        39        39
30            1         1         0         0        10         3         6        19        15        31        30        38
40            0         0         0         0         0         4         2         7         2         3         8        11
50            0         0         0         0         0         0         0         0         0         1         1         2
over:         0         0         0         0         0         0         0         0         0         0         0         0
count:    55215     54649     54703     54620     54714     55003     54499     55461     54668     55052     55309     54880
min:          0         0         0         0         0         0         0         0         0         0         0         0
avg:          0         0         0         0         0         0         0         0         0         0         0         0
max:         30        30        20        20        30        40        40        40        40        50        50        50
```

### SEE ALSO

**rtla-osnoise**(1), **rtla-osnoise-top**(1)

*osnoise* tracer documentation: <<https://www.kernel.org/doc/html/latest/trace/osnoise-tracer.html>>

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
