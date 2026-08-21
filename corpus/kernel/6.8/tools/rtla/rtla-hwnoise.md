---
collection: kernel
version: "6.8"
title: "rtla-hwnoise"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-hwnoise.html
fetched_at: 2026-08-21T03:56:30+00:00
---
# rtla-hwnoise

## Detect and quantify hardware-related noise

Manual section
:   1

### SYNOPSIS

**rtla hwnoise** [*OPTIONS*]

### DESCRIPTION

**rtla hwnoise** collects the periodic summary from the *osnoise* tracer
running with *interrupts disabled*. By disabling interrupts, and the scheduling
of threads as a consequence, only non-maskable interrupts and hardware-related
noise is allowed.

The tool also allows the configurations of the *osnoise* tracer and the
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

In the example below, the **rtla hwnoise** tool is set to run on CPUs *1-7*
on a system with 8 cores/16 threads with hyper-threading enabled.

The tool is set to detect any noise higher than *one microsecond*,
to run for *ten minutes*, displaying a summary of the report at the
end of the session:

```
# rtla hwnoise -c 1-7 -T 1 -d 10m -q
                                        Hardware-related Noise
duration:   0 00:10:00 | time is in us
CPU Period       Runtime        Noise  % CPU Aval   Max Noise   Max Single          HW          NMI
  1 #599       599000000          138    99.99997           3            3           4           74
  2 #599       599000000           85    99.99998           3            3           4           75
  3 #599       599000000           86    99.99998           4            3           6           75
  4 #599       599000000           81    99.99998           4            4           2           75
  5 #599       599000000           85    99.99998           2            2           2           75
  6 #599       599000000           76    99.99998           2            2           0           75
  7 #599       599000000           77    99.99998           3            3           0           75
```

The first column shows the *CPU*, and the second column shows how many
*Periods* the tool ran during the session. The *Runtime* is the time
the tool effectively runs on the CPU. The *Noise* column is the sum of
all noise that the tool observed, and the *% CPU Aval* is the relation
between the *Runtime* and *Noise*.

The *Max Noise* column is the maximum hardware noise the tool detected in a
single period, and the *Max Single* is the maximum single noise seen.

The *HW* and *NMI* columns show the total number of *hardware* and *NMI* noise
occurrence observed by the tool.

For example, *CPU 3* ran *599* periods of *1 second Runtime*. The CPU received
*86 us* of noise during the entire execution, leaving *99.99997 %* of CPU time
for the application. In the worst single period, the CPU caused *4 us* of
noise to the application, but it was certainly caused by more than one single
noise, as the *Max Single* noise was of *3 us*. The CPU has *HW noise,* at a
rate of *six occurrences*/*ten minutes*. The CPU also has *NMIs*, at a higher
frequency: around *seven per second*.

The tool should report *0* hardware-related noise in the ideal situation.
For example, by disabling hyper-threading to remove the hardware noise,
and disabling the TSC watchdog to remove the NMI (it is possible to identify
this using tracing options of **rtla hwnoise**), it was possible to reach
the ideal situation in the same hardware:

```
# rtla hwnoise -c 1-7 -T 1 -d 10m -q
                                        Hardware-related Noise
duration:   0 00:10:00 | time is in us
CPU Period       Runtime        Noise  % CPU Aval   Max Noise   Max Single          HW          NMI
  1 #599       599000000            0   100.00000           0            0           0            0
  2 #599       599000000            0   100.00000           0            0           0            0
  3 #599       599000000            0   100.00000           0            0           0            0
  4 #599       599000000            0   100.00000           0            0           0            0
  5 #599       599000000            0   100.00000           0            0           0            0
  6 #599       599000000            0   100.00000           0            0           0            0
  7 #599       599000000            0   100.00000           0            0           0            0
```

### SEE ALSO

**rtla-osnoise**(1)

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
