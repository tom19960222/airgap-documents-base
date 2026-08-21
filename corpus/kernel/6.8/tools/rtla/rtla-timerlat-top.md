---
collection: kernel
version: "6.8"
title: "rtla-timerlat-top"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-timerlat-top.html
fetched_at: 2026-08-21T03:56:30+00:00
---
# rtla-timerlat-top

## Measures the operating system timer latency

Manual section
:   1

### SYNOPSIS

**rtla timerlat top** [*OPTIONS*] ...

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

The **rtla timerlat top** displays a summary of the periodic output
from the *timerlat* tracer. It also provides information for each
operating system noise via the **osnoise:** tracepoints that can be
seem with the option **-T**.

### OPTIONS

**-a**, **--auto** *us*

> Set the automatic trace mode. This mode sets some commonly used options
> while debugging the system. It is equivalent to use **-T** *us* **-s** *us*
> **-t**. By default, *timerlat* tracer uses FIFO:95 for *timerlat* threads,
> thus equilavent to **-P** *f:95*.

**-p**, **--period** *us*

> Set the *timerlat* tracer period in microseconds.

**-i**, **--irq** *us*

> Stop trace if the *IRQ* latency is higher than the argument in us.

**-T**, **--thread** *us*

> Stop trace if the *Thread* latency is higher than the argument in us.

**-s**, **--stack** *us*

> Save the stack trace at the *IRQ* if a *Thread* latency is higher than the
> argument in us.

**--dma-latency** *us*
:   Set the /dev/cpu_dma_latency to *us*, aiming to bound exit from idle latencies.
    *cyclictest* sets this value to *0* by default, use **--dma-latency** *0* to have
    similar results.

**-u**, **--user-threads**

> Set timerlat to run without a workload, and then dispatches user-space workloads
> to wait on the timerlat_fd. Once the workload is awakes, it goes to sleep again
> adding so the measurement for the kernel-to-user and user-to-kernel to the tracer
> output.

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

**--dump-tasks**

> prints the task running on all CPUs if stop conditions are met (depends on !--no-aa)

**--no-aa**

> disable auto-analysis, reducing rtla timerlat cpu usage

**--aa-only** *us*

> Set stop tracing conditions and run without collecting and displaying statistics.
> Print the auto-analysis if the system hits the stop tracing condition. This option
> is useful to reduce rtla timerlat CPU, enabling the debug without the overhead of
> collecting the statistics.

### EXAMPLE

In the example below, the timerlat tracer is dispatched in cpus *1-23* in the
automatic trace mode, instructing the tracer to stop if a *40 us* latency or
higher is found:

```
# timerlat -a 40 -c 1-23 -q
                                   Timer Latency
  0 00:00:12   |          IRQ Timer Latency (us)        |         Thread Timer Latency (us)
CPU COUNT      |      cur       min       avg       max |      cur       min       avg       max
  1 #12322     |        0         0         1        15 |       10         3         9        31
  2 #12322     |        3         0         1        12 |       10         3         9        23
  3 #12322     |        1         0         1        21 |        8         2         8        34
  4 #12322     |        1         0         1        17 |       10         2        11        33
  5 #12322     |        0         0         1        12 |        8         3         8        25
  6 #12322     |        1         0         1        14 |       16         3        11        35
  7 #12322     |        0         0         1        14 |        9         2         8        29
  8 #12322     |        1         0         1        22 |        9         3         9        34
  9 #12322     |        0         0         1        14 |        8         2         8        24
 10 #12322     |        1         0         0        12 |        9         3         8        24
 11 #12322     |        0         0         0        15 |        6         2         7        29
 12 #12321     |        1         0         0        13 |        5         3         8        23
 13 #12319     |        0         0         1        14 |        9         3         9        26
 14 #12321     |        1         0         0        13 |        6         2         8        24
 15 #12321     |        1         0         1        15 |       12         3        11        27
 16 #12318     |        0         0         1        13 |        7         3        10        24
 17 #12319     |        0         0         1        13 |       11         3         9        25
 18 #12318     |        0         0         0        12 |        8         2         8        20
 19 #12319     |        0         0         1        18 |       10         2         9        28
 20 #12317     |        0         0         0        20 |        9         3         8        34
 21 #12318     |        0         0         0        13 |        8         3         8        28
 22 #12319     |        0         0         1        11 |        8         3        10        22
 23 #12320     |       28         0         1        28 |       41         3        11        41
rtla timerlat hit stop tracing
## CPU 23 hit stop tracing, analyzing it ##
IRQ handler delay:                                        27.49 us (65.52 %)
IRQ latency:                                              28.13 us
Timerlat IRQ duration:                                     9.59 us (22.85 %)
Blocking thread:                                           3.79 us (9.03 %)
                       objtool:49256                       3.79 us
  Blocking thread stacktrace
              -> timerlat_irq
              -> __hrtimer_run_queues
              -> hrtimer_interrupt
              -> __sysvec_apic_timer_interrupt
              -> sysvec_apic_timer_interrupt
              -> asm_sysvec_apic_timer_interrupt
              -> _raw_spin_unlock_irqrestore
              -> cgroup_rstat_flush_locked
              -> cgroup_rstat_flush_irqsafe
              -> mem_cgroup_flush_stats
              -> mem_cgroup_wb_stats
              -> balance_dirty_pages
              -> balance_dirty_pages_ratelimited_flags
              -> btrfs_buffered_write
              -> btrfs_do_write_iter
              -> vfs_write
              -> __x64_sys_pwrite64
              -> do_syscall_64
              -> entry_SYSCALL_64_after_hwframe
------------------------------------------------------------------------
  Thread latency:                                          41.96 us (100%)

The system has exit from idle latency!
  Max timerlat IRQ latency from idle: 17.48 us in cpu 4
Saving trace to timerlat_trace.txt
```

In this case, the major factor was the delay suffered by the *IRQ handler*
that handles **timerlat** wakeup: *65.52%*. This can be caused by the
current thread masking interrupts, which can be seen in the blocking
thread stacktrace: the current thread (*objtool:49256*) disabled interrupts
via *raw spin lock* operations inside mem cgroup, while doing write
syscall in a btrfs file system.

The raw trace is saved in the **timerlat_trace.txt** file for further analysis.

Note that **rtla timerlat** was dispatched without changing *timerlat* tracer
threads' priority. That is generally not needed because these threads have
priority *FIFO:95* by default, which is a common priority used by real-time
kernel developers to analyze scheduling delays.

#### SEE ALSO

**rtla-timerlat**(1), **rtla-timerlat-hist**(1)

*timerlat* tracer documentation: <<https://www.kernel.org/doc/html/latest/trace/timerlat-tracer.html>>

#### AUTHOR

Written by Daniel Bristot de Oliveira <[bristot@kernel.org](mailto:bristot%40kernel.org)>

### REPORTING BUGS

Report bugs to <[linux-kernel@vger.kernel.org](mailto:linux-kernel%40vger.kernel.org)>
and <[linux-trace-devel@vger.kernel.org](mailto:linux-trace-devel%40vger.kernel.org)>

### LICENSE

**rtla** is Free Software licensed under the GNU GPLv2

### COPYING

Copyright (C) 2021 Red Hat, Inc. Free use of this software is granted under
the terms of the GNU Public License (GPL).
