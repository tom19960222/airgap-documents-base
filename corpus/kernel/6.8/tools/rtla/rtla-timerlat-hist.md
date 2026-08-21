---
collection: kernel
version: "6.8"
title: "rtla-timerlat-hist"
source_url: https://www.kernel.org/doc/html/v6.8/tools/rtla/rtla-timerlat-hist.html
fetched_at: 2026-08-21T03:56:30+00:00
---
# rtla-timerlat-hist

## Histograms of the operating system timer latency

Manual section
:   1

### SYNOPSIS

**rtla timerlat hist** [*OPTIONS*] ...

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

The **rtla timerlat hist** displays a histogram of each tracer event
occurrence. This tool uses the periodic information, and the
**osnoise:** tracepoints are enabled when using the **-T** option.

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

**--dump-tasks**

> prints the task running on all CPUs if stop conditions are met (depends on !--no-aa)

**--no-aa**

> disable auto-analysis, reducing rtla timerlat cpu usage

### EXAMPLE

In the example below, **rtla timerlat hist** is set to run for *10* minutes,
in the cpus *0-4*, *skipping zero* only lines. Moreover, **rtla timerlat
hist** will change the priority of the *timerlat* threads to run under
*SCHED_DEADLINE* priority, with a *100us* runtime every *1ms* period. The
*1ms* period is also passed to the *timerlat* tracer. Auto-analysis is disabled
to reduce overhead

```
[root@alien ~]# timerlat hist -d 10m -c 0-4 -P d:100us:1ms -p 1000 --no-aa
# RTLA timerlat histogram
# Time unit is microseconds (us)
# Duration:   0 00:10:00
Index   IRQ-000   Thr-000   IRQ-001   Thr-001   IRQ-002   Thr-002   IRQ-003   Thr-003   IRQ-004   Thr-004
0        276489         0    206089         0    466018         0    481102         0    205546         0
1        318327     35487    388149     30024     94531     48382     83082     71078    388026     55730
2          3282    122584      4019    126527     28231    109012     23311     89309      4568     98739
3           940     11815       837      9863      6209     16227      6895     17196       910      9780
4           444     17287       424     11574      2097     38443      2169     36736       462     13476
5           206     43291       255     25581      1223    101908      1304    101137       236     28913
6           132    101501        96     64584       635    213774       757    215471        99     73453
7            74    169347        65    124758       350     57466       441     53639        69    148573
8            53     85183        31    156751       229      9052       306      9026        39    139907
9            22     10387        12     42762       161      2554       225      2689        19     26192
10           13      1898         8      5770       114      1247       128      1405        13      3772
11            9       560         9       924        71       686        76       765         8       713
12            4       256         2       360        50       411        64       474         3       278
13            2       167         2       172        43       256        53       350         4       180
14            1        88         1       116        15       198        42       223         0       115
15            2        63         3        94        11       139        20       150         0        58
16            2        37         0        56         5        78        10       102         0        39
17            0        18         0        28         4        57         8        80         0        15
18            0         8         0        17         2        50         6        56         0        12
19            0         9         0         5         0        19         0        48         0        18
20            0         4         0         8         0        11         2        27         0         4
21            0         2         0         3         1         9         1        18         0         6
22            0         1         0         3         1         7         0         3         0         5
23            0         2         0         4         0         2         0         7         0         2
24            0         2         0         2         1         3         0         3         0         5
25            0         0         0         1         0         1         0         1         0         3
26            0         1         0         0         0         2         0         2         0         0
27            0         0         0         3         0         1         0         0         0         1
28            0         0         0         3         0         0         0         1         0         0
29            0         0         0         2         0         2         0         1         0         3
30            0         1         0         0         0         0         0         0         0         0
31            0         1         0         0         0         0         0         2         0         2
32            0         0         0         1         0         2         0         0         0         0
33            0         0         0         2         0         0         0         0         0         1
34            0         0         0         0         0         0         0         0         0         2
35            0         1         0         1         0         0         0         0         0         1
36            0         1         0         0         0         1         0         1         0         0
37            0         0         0         1         0         0         0         0         0         0
40            0         0         0         0         0         1         0         1         0         0
41            0         0         0         0         0         0         0         0         0         1
42            0         0         0         0         0         0         0         0         0         1
44            0         0         0         0         0         1         0         0         0         0
46            0         0         0         0         0         0         0         1         0         0
47            0         0         0         0         0         0         0         0         0         1
50            0         0         0         0         0         0         0         0         0         1
54            0         0         0         1         0         0         0         0         0         0
58            0         0         0         1         0         0         0         0         0         0
over:         0         0         0         0         0         0         0         0         0         0
count:   600002    600002    600002    600002    600002    600002    600002    600002    600002    600002
min:          0         1         0         1         0         1         0         1         0         1
avg:          0         5         0         5         0         4         0         4         0         5
max:         16        36        15        58        24        44        21        46        13        50
```

### SEE ALSO

**rtla-timerlat**(1), **rtla-timerlat-top**(1)

*timerlat* tracer documentation: <<https://www.kernel.org/doc/html/latest/trace/timerlat-tracer.html>>

### AUTHOR

Written by Daniel Bristot de Oliveira <[bristot@kernel.org](mailto:bristot%40kernel.org)>
