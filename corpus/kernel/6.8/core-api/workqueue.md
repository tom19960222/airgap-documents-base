---
collection: kernel
version: "6.8"
title: "Workqueue"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/workqueue.html
fetched_at: 2026-08-21T03:29:52+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/core-api/workqueue.md)

# Workqueue

Date
:   September, 2010

Author
:   Tejun Heo <[tj@kernel.org](mailto:tj%40kernel.org)>

Author
:   Florian Mickler <[florian@mickler.org](mailto:florian%40mickler.org)>

## Introduction

There are many cases where an asynchronous process execution context
is needed and the workqueue (wq) API is the most commonly used
mechanism for such cases.

When such an asynchronous execution context is needed, a work item
describing which function to execute is put on a queue. An
independent thread serves as the asynchronous execution context. The
queue is called workqueue and the thread is called worker.

While there are work items on the workqueue the worker executes the
functions associated with the work items one after the other. When
there is no work item left on the workqueue the worker becomes idle.
When a new work item gets queued, the worker begins executing again.

## Why Concurrency Managed Workqueue?

In the original wq implementation, a multi threaded (MT) wq had one
worker thread per CPU and a single threaded (ST) wq had one worker
thread system-wide. A single MT wq needed to keep around the same
number of workers as the number of CPUs. The kernel grew a lot of MT
wq users over the years and with the number of CPU cores continuously
rising, some systems saturated the default 32k PID space just booting
up.

Although MT wq wasted a lot of resource, the level of concurrency
provided was unsatisfactory. The limitation was common to both ST and
MT wq albeit less severe on MT. Each wq maintained its own separate
worker pool. An MT wq could provide only one execution context per CPU
while an ST wq one for the whole system. Work items had to compete for
those very limited execution contexts leading to various problems
including proneness to deadlocks around the single execution context.

The tension between the provided level of concurrency and resource
usage also forced its users to make unnecessary tradeoffs like libata
choosing to use ST wq for polling PIOs and accepting an unnecessary
limitation that no two polling PIOs can progress at the same time. As
MT wq don't provide much better concurrency, users which require
higher level of concurrency, like async or fscache, had to implement
their own thread pool.

Concurrency Managed Workqueue (cmwq) is a reimplementation of wq with
focus on the following goals.

- Maintain compatibility with the original workqueue API.
- Use per-CPU unified worker pools shared by all wq to provide
  flexible level of concurrency on demand without wasting a lot of
  resource.
- Automatically regulate worker pool and level of concurrency so that
  the API users don't need to worry about such details.

## The Design

In order to ease the asynchronous execution of functions a new
abstraction, the work item, is introduced.

A work item is a simple struct that holds a pointer to the function
that is to be executed asynchronously. Whenever a driver or subsystem
wants a function to be executed asynchronously it has to set up a work
item pointing to that function and queue that work item on a
workqueue.

Special purpose threads, called worker threads, execute the functions
off of the queue, one after the other. If no work is queued, the
worker threads become idle. These worker threads are managed in so
called worker-pools.

The cmwq design differentiates between the user-facing workqueues that
subsystems and drivers queue work items on and the backend mechanism
which manages worker-pools and processes the queued work items.

There are two worker-pools, one for normal work items and the other
for high priority ones, for each possible CPU and some extra
worker-pools to serve work items queued on unbound workqueues - the
number of these backing pools is dynamic.

Subsystems and drivers can create and queue work items through special
workqueue API functions as they see fit. They can influence some
aspects of the way the work items are executed by setting flags on the
workqueue they are putting the work item on. These flags include
things like CPU locality, concurrency limits, priority and more. To
get a detailed overview refer to the API description of
`alloc_workqueue()` below.

When a work item is queued to a workqueue, the target worker-pool is
determined according to the queue parameters and workqueue attributes
and appended on the shared worklist of the worker-pool. For example,
unless specifically overridden, a work item of a bound workqueue will
be queued on the worklist of either normal or highpri worker-pool that
is associated to the CPU the issuer is running on.

For any worker pool implementation, managing the concurrency level
(how many execution contexts are active) is an important issue. cmwq
tries to keep the concurrency at a minimal but sufficient level.
Minimal to save resources and sufficient in that the system is used at
its full capacity.

Each worker-pool bound to an actual CPU implements concurrency
management by hooking into the scheduler. The worker-pool is notified
whenever an active worker wakes up or sleeps and keeps track of the
number of the currently runnable workers. Generally, work items are
not expected to hog a CPU and consume many cycles. That means
maintaining just enough concurrency to prevent work processing from
stalling should be optimal. As long as there are one or more runnable
workers on the CPU, the worker-pool doesn't start execution of a new
work, but, when the last running worker goes to sleep, it immediately
schedules a new worker so that the CPU doesn't sit idle while there
are pending work items. This allows using a minimal number of workers
without losing execution bandwidth.

Keeping idle workers around doesn't cost other than the memory space
for kthreads, so cmwq holds onto idle ones for a while before killing
them.

For unbound workqueues, the number of backing pools is dynamic.
Unbound workqueue can be assigned custom attributes using
`apply_workqueue_attrs()` and workqueue will automatically create
backing worker pools matching the attributes. The responsibility of
regulating concurrency level is on the users. There is also a flag to
mark a bound wq to ignore the concurrency management. Please refer to
the API section for details.

Forward progress guarantee relies on that workers can be created when
more execution contexts are necessary, which in turn is guaranteed
through the use of rescue workers. All work items which might be used
on code paths that handle memory reclaim are required to be queued on
wq's that have a rescue-worker reserved for execution under memory
pressure. Else it is possible that the worker-pool deadlocks waiting
for execution contexts to free up.

## Application Programming Interface (API)

`alloc_workqueue()` allocates a wq. The original
`create_*workqueue()` functions are deprecated and scheduled for
removal. `alloc_workqueue()` takes three arguments - `@name`,
`@flags` and `@max_active`. `@name` is the name of the wq and
also used as the name of the rescuer thread if there is one.

A wq no longer manages execution resources but serves as a domain for
forward progress guarantee, flush and work item attributes. `@flags`
and `@max_active` control how work items are assigned execution
resources, scheduled and executed.

### `flags`

`WQ_UNBOUND`
:   Work items queued to an unbound wq are served by the special
    worker-pools which host workers which are not bound to any
    specific CPU. This makes the wq behave as a simple execution
    context provider without concurrency management. The unbound
    worker-pools try to start execution of work items as soon as
    possible. Unbound wq sacrifices locality but is useful for
    the following cases.

    - Wide fluctuation in the concurrency level requirement is
      expected and using bound wq may end up creating large number
      of mostly unused workers across different CPUs as the issuer
      hops through different CPUs.
    - Long running CPU intensive workloads which can be better
      managed by the system scheduler.

`WQ_FREEZABLE`
:   A freezable wq participates in the freeze phase of the system
    suspend operations. Work items on the wq are drained and no
    new work item starts execution until thawed.

`WQ_MEM_RECLAIM`
:   All wq which might be used in the memory reclaim paths **MUST**
    have this flag set. The wq is guaranteed to have at least one
    execution context regardless of memory pressure.

`WQ_HIGHPRI`
:   Work items of a highpri wq are queued to the highpri
    worker-pool of the target cpu. Highpri worker-pools are
    served by worker threads with elevated nice level.

    Note that normal and highpri worker-pools don't interact with
    each other. Each maintains its separate pool of workers and
    implements concurrency management among its workers.

`WQ_CPU_INTENSIVE`
:   Work items of a CPU intensive wq do not contribute to the
    concurrency level. In other words, runnable CPU intensive
    work items will not prevent other work items in the same
    worker-pool from starting execution. This is useful for bound
    work items which are expected to hog CPU cycles so that their
    execution is regulated by the system scheduler.

    Although CPU intensive work items don't contribute to the
    concurrency level, start of their executions is still
    regulated by the concurrency management and runnable
    non-CPU-intensive work items can delay execution of CPU
    intensive work items.

    This flag is meaningless for unbound wq.

### `max_active`

`@max_active` determines the maximum number of execution contexts per
CPU which can be assigned to the work items of a wq. For example, with
`@max_active` of 16, at most 16 work items of the wq can be executing
at the same time per CPU. This is always a per-CPU attribute, even for
unbound workqueues.

The maximum limit for `@max_active` is 512 and the default value used
when 0 is specified is 256. These values are chosen sufficiently high
such that they are not the limiting factor while providing protection in
runaway cases.

The number of active work items of a wq is usually regulated by the
users of the wq, more specifically, by how many work items the users
may queue at the same time. Unless there is a specific need for
throttling the number of active work items, specifying '0' is
recommended.

Some users depend on the strict execution ordering of ST wq. The
combination of `@max_active` of 1 and `WQ_UNBOUND` used to
achieve this behavior. Work items on such wq were always queued to the
unbound worker-pools and only one work item could be active at any given
time thus achieving the same ordering property as ST wq.

In the current implementation the above configuration only guarantees
ST behavior within a given NUMA node. Instead `alloc_ordered_workqueue()` should
be used to achieve system-wide ST behavior.

## Example Execution Scenarios

The following example execution scenarios try to illustrate how cmwq
behave under different configurations.

> Work items w0, w1, w2 are queued to a bound wq q0 on the same CPU.
> w0 burns CPU for 5ms then sleeps for 10ms then burns CPU for 5ms
> again before finishing. w1 and w2 burn CPU for 5ms then sleep for
> 10ms.

Ignoring all other tasks, works and processing overhead, and assuming
simple FIFO scheduling, the following is one highly simplified version
of possible sequences of events with the original wq.

```
TIME IN MSECS  EVENT
0              w0 starts and burns CPU
5              w0 sleeps
15             w0 wakes up and burns CPU
20             w0 finishes
20             w1 starts and burns CPU
25             w1 sleeps
35             w1 wakes up and finishes
35             w2 starts and burns CPU
40             w2 sleeps
50             w2 wakes up and finishes
```

And with cmwq with `@max_active` >= 3,

```
TIME IN MSECS  EVENT
0              w0 starts and burns CPU
5              w0 sleeps
5              w1 starts and burns CPU
10             w1 sleeps
10             w2 starts and burns CPU
15             w2 sleeps
15             w0 wakes up and burns CPU
20             w0 finishes
20             w1 wakes up and finishes
25             w2 wakes up and finishes
```

If `@max_active` == 2,

```
TIME IN MSECS  EVENT
0              w0 starts and burns CPU
5              w0 sleeps
5              w1 starts and burns CPU
10             w1 sleeps
15             w0 wakes up and burns CPU
20             w0 finishes
20             w1 wakes up and finishes
20             w2 starts and burns CPU
25             w2 sleeps
35             w2 wakes up and finishes
```

Now, let's assume w1 and w2 are queued to a different wq q1 which has
`WQ_CPU_INTENSIVE` set,

```
TIME IN MSECS  EVENT
0              w0 starts and burns CPU
5              w0 sleeps
5              w1 and w2 start and burn CPU
10             w1 sleeps
15             w2 sleeps
15             w0 wakes up and burns CPU
20             w0 finishes
20             w1 wakes up and finishes
25             w2 wakes up and finishes
```

## Guidelines

- Do not forget to use `WQ_MEM_RECLAIM` if a wq may process work
  items which are used during memory reclaim. Each wq with
  `WQ_MEM_RECLAIM` set has an execution context reserved for it. If
  there is dependency among multiple work items used during memory
  reclaim, they should be queued to separate wq each with
  `WQ_MEM_RECLAIM`.
- Unless strict ordering is required, there is no need to use ST wq.
- Unless there is a specific need, using 0 for @max_active is
  recommended. In most use cases, concurrency level usually stays
  well under the default limit.
- A wq serves as a domain for forward progress guarantee
  (`WQ_MEM_RECLAIM`, flush and work item attributes. Work items
  which are not involved in memory reclaim and don't need to be
  flushed as a part of a group of work items, and don't require any
  special attribute, can use one of the system wq. There is no
  difference in execution characteristics between using a dedicated wq
  and a system wq.
- Unless work items are expected to consume a huge amount of CPU
  cycles, using a bound wq is usually beneficial due to the increased
  level of locality in wq operations and work item execution.

## Affinity Scopes

An unbound workqueue groups CPUs according to its affinity scope to improve
cache locality. For example, if a workqueue is using the default affinity
scope of "cache", it will group CPUs according to last level cache
boundaries. A work item queued on the workqueue will be assigned to a worker
on one of the CPUs which share the last level cache with the issuing CPU.
Once started, the worker may or may not be allowed to move outside the scope
depending on the `affinity_strict` setting of the scope.

Workqueue currently supports the following affinity scopes.

`default`
:   Use the scope in module parameter `workqueue.default_affinity_scope`
    which is always set to one of the scopes below.

`cpu`
:   CPUs are not grouped. A work item issued on one CPU is processed by a
    worker on the same CPU. This makes unbound workqueues behave as per-cpu
    workqueues without concurrency management.

`smt`
:   CPUs are grouped according to SMT boundaries. This usually means that the
    logical threads of each physical CPU core are grouped together.

`cache`
:   CPUs are grouped according to cache boundaries. Which specific cache
    boundary is used is determined by the arch code. L3 is used in a lot of
    cases. This is the default affinity scope.

`numa`
:   CPUs are grouped according to NUMA boundaries.

`system`
:   All CPUs are put in the same group. Workqueue makes no effort to process a
    work item on a CPU close to the issuing CPU.

The default affinity scope can be changed with the module parameter
`workqueue.default_affinity_scope` and a specific workqueue's affinity
scope can be changed using `apply_workqueue_attrs()`.

If `WQ_SYSFS` is set, the workqueue will have the following affinity scope
related interface files under its `/sys/devices/virtual/workqueue/WQ_NAME/`
directory.

`affinity_scope`
:   Read to see the current affinity scope. Write to change.

    When default is the current scope, reading this file will also show the
    current effective scope in parentheses, for example, `default (cache)`.

`affinity_strict`
:   0 by default indicating that affinity scopes are not strict. When a work
    item starts execution, workqueue makes a best-effort attempt to ensure
    that the worker is inside its affinity scope, which is called
    repatriation. Once started, the scheduler is free to move the worker
    anywhere in the system as it sees fit. This enables benefiting from scope
    locality while still being able to utilize other CPUs if necessary and
    available.

    If set to 1, all workers of the scope are guaranteed always to be in the
    scope. This may be useful when crossing affinity scopes has other
    implications, for example, in terms of power consumption or workload
    isolation. Strict NUMA scope can also be used to match the workqueue
    behavior of older kernels.

## Affinity Scopes and Performance

It'd be ideal if an unbound workqueue's behavior is optimal for vast
majority of use cases without further tuning. Unfortunately, in the current
kernel, there exists a pronounced trade-off between locality and utilization
necessitating explicit configurations when workqueues are heavily used.

Higher locality leads to higher efficiency where more work is performed for
the same number of consumed CPU cycles. However, higher locality may also
cause lower overall system utilization if the work items are not spread
enough across the affinity scopes by the issuers. The following performance
testing with dm-crypt clearly illustrates this trade-off.

The tests are run on a CPU with 12-cores/24-threads split across four L3
caches (AMD Ryzen 9 3900x). CPU clock boost is turned off for consistency.
`/dev/dm-0` is a dm-crypt device created on NVME SSD (Samsung 990 PRO) and
opened with `cryptsetup` with default settings.

### Scenario 1: Enough issuers and work spread across the machine

The command used:

```
$ fio --filename=/dev/dm-0 --direct=1 --rw=randrw --bs=32k --ioengine=libaio \
  --iodepth=64 --runtime=60 --numjobs=24 --time_based --group_reporting \
  --name=iops-test-job --verify=sha512
```

There are 24 issuers, each issuing 64 IOs concurrently. `--verify=sha512`
makes `fio` generate and read back the content each time which makes
execution locality matter between the issuer and `kcryptd`. The following
are the read bandwidths and CPU utilizations depending on different affinity
scope settings on `kcryptd` measured over five runs. Bandwidths are in
MiBps, and CPU util in percents.

| Affinity | Bandwidth (MiBps) | CPU util (%) |
| --- | --- | --- |
| system | 1159.40 ±1.34 | 99.31 ±0.02 |
| cache | 1166.40 ±0.89 | 99.34 ±0.01 |
| cache (strict) | 1166.00 ±0.71 | 99.35 ±0.01 |

With enough issuers spread across the system, there is no downside to
"cache", strict or otherwise. All three configurations saturate the whole
machine but the cache-affine ones outperform by 0.6% thanks to improved
locality.

### Scenario 2: Fewer issuers, enough work for saturation

The command used:

```
$ fio --filename=/dev/dm-0 --direct=1 --rw=randrw --bs=32k \
  --ioengine=libaio --iodepth=64 --runtime=60 --numjobs=8 \
  --time_based --group_reporting --name=iops-test-job --verify=sha512
```

The only difference from the previous scenario is `--numjobs=8`. There are
a third of the issuers but is still enough total work to saturate the
system.

| Affinity | Bandwidth (MiBps) | CPU util (%) |
| --- | --- | --- |
| system | 1155.40 ±0.89 | 97.41 ±0.05 |
| cache | 1154.40 ±1.14 | 96.15 ±0.09 |
| cache (strict) | 1112.00 ±4.64 | 93.26 ±0.35 |

This is more than enough work to saturate the system. Both "system" and
"cache" are nearly saturating the machine but not fully. "cache" is using
less CPU but the better efficiency puts it at the same bandwidth as
"system".

Eight issuers moving around over four L3 cache scope still allow "cache
(strict)" to mostly saturate the machine but the loss of work conservation
is now starting to hurt with 3.7% bandwidth loss.

### Scenario 3: Even fewer issuers, not enough work to saturate

The command used:

```
$ fio --filename=/dev/dm-0 --direct=1 --rw=randrw --bs=32k \
  --ioengine=libaio --iodepth=64 --runtime=60 --numjobs=4 \
  --time_based --group_reporting --name=iops-test-job --verify=sha512
```

Again, the only difference is `--numjobs=4`. With the number of issuers
reduced to four, there now isn't enough work to saturate the whole system
and the bandwidth becomes dependent on completion latencies.

| Affinity | Bandwidth (MiBps) | CPU util (%) |
| --- | --- | --- |
| system | 993.60 ±1.82 | 75.49 ±0.06 |
| cache | 973.40 ±1.52 | 74.90 ±0.07 |
| cache (strict) | 828.20 ±4.49 | 66.84 ±0.29 |

Now, the tradeoff between locality and utilization is clearer. "cache" shows
2% bandwidth loss compared to "system" and "cache (struct)" whopping 20%.

### Conclusion and Recommendations

In the above experiments, the efficiency advantage of the "cache" affinity
scope over "system" is, while consistent and noticeable, small. However, the
impact is dependent on the distances between the scopes and may be more
pronounced in processors with more complex topologies.

While the loss of work-conservation in certain scenarios hurts, it is a lot
better than "cache (strict)" and maximizing workqueue utilization is
unlikely to be the common case anyway. As such, "cache" is the default
affinity scope for unbound pools.

- As there is no one option which is great for most cases, workqueue usages
  that may consume a significant amount of CPU are recommended to configure
  the workqueues using `apply_workqueue_attrs()` and/or enable
  `WQ_SYSFS`.
- An unbound workqueue with strict "cpu" affinity scope behaves the same as
  `WQ_CPU_INTENSIVE` per-cpu workqueue. There is no real advanage to the
  latter and an unbound workqueue provides a lot more flexibility.
- Affinity scopes are introduced in Linux v6.5. To emulate the previous
  behavior, use strict "numa" affinity scope.
- The loss of work-conservation in non-strict affinity scopes is likely
  originating from the scheduler. There is no theoretical reason why the
  kernel wouldn't be able to do the right thing and maintain
  work-conservation in most cases. As such, it is possible that future
  scheduler improvements may make most of these tunables unnecessary.

## Examining Configuration

Use tools/workqueue/wq_dump.py to examine unbound CPU affinity
configuration, worker pools and how workqueues map to the pools:

```
$ tools/workqueue/wq_dump.py
Affinity Scopes
===============
wq_unbound_cpumask=0000000f

CPU
  nr_pods  4
  pod_cpus [0]=00000001 [1]=00000002 [2]=00000004 [3]=00000008
  pod_node [0]=0 [1]=0 [2]=1 [3]=1
  cpu_pod  [0]=0 [1]=1 [2]=2 [3]=3

SMT
  nr_pods  4
  pod_cpus [0]=00000001 [1]=00000002 [2]=00000004 [3]=00000008
  pod_node [0]=0 [1]=0 [2]=1 [3]=1
  cpu_pod  [0]=0 [1]=1 [2]=2 [3]=3

CACHE (default)
  nr_pods  2
  pod_cpus [0]=00000003 [1]=0000000c
  pod_node [0]=0 [1]=1
  cpu_pod  [0]=0 [1]=0 [2]=1 [3]=1

NUMA
  nr_pods  2
  pod_cpus [0]=00000003 [1]=0000000c
  pod_node [0]=0 [1]=1
  cpu_pod  [0]=0 [1]=0 [2]=1 [3]=1

SYSTEM
  nr_pods  1
  pod_cpus [0]=0000000f
  pod_node [0]=-1
  cpu_pod  [0]=0 [1]=0 [2]=0 [3]=0

Worker Pools
============
pool[00] ref= 1 nice=  0 idle/workers=  4/  4 cpu=  0
pool[01] ref= 1 nice=-20 idle/workers=  2/  2 cpu=  0
pool[02] ref= 1 nice=  0 idle/workers=  4/  4 cpu=  1
pool[03] ref= 1 nice=-20 idle/workers=  2/  2 cpu=  1
pool[04] ref= 1 nice=  0 idle/workers=  4/  4 cpu=  2
pool[05] ref= 1 nice=-20 idle/workers=  2/  2 cpu=  2
pool[06] ref= 1 nice=  0 idle/workers=  3/  3 cpu=  3
pool[07] ref= 1 nice=-20 idle/workers=  2/  2 cpu=  3
pool[08] ref=42 nice=  0 idle/workers=  6/  6 cpus=0000000f
pool[09] ref=28 nice=  0 idle/workers=  3/  3 cpus=00000003
pool[10] ref=28 nice=  0 idle/workers= 17/ 17 cpus=0000000c
pool[11] ref= 1 nice=-20 idle/workers=  1/  1 cpus=0000000f
pool[12] ref= 2 nice=-20 idle/workers=  1/  1 cpus=00000003
pool[13] ref= 2 nice=-20 idle/workers=  1/  1 cpus=0000000c

Workqueue CPU -> pool
=====================
[    workqueue \ CPU              0  1  2  3 dfl]
events                   percpu   0  2  4  6
events_highpri           percpu   1  3  5  7
events_long              percpu   0  2  4  6
events_unbound           unbound  9  9 10 10  8
events_freezable         percpu   0  2  4  6
events_power_efficient   percpu   0  2  4  6
events_freezable_power_  percpu   0  2  4  6
rcu_gp                   percpu   0  2  4  6
rcu_par_gp               percpu   0  2  4  6
slub_flushwq             percpu   0  2  4  6
netns                    ordered  8  8  8  8  8
...
```

See the command's help message for more info.

## Monitoring

Use tools/workqueue/wq_monitor.py to monitor workqueue operations:

```
$ tools/workqueue/wq_monitor.py events
                            total  infl  CPUtime  CPUhog CMW/RPR  mayday rescued
events                      18545     0      6.1       0       5       -       -
events_highpri                  8     0      0.0       0       0       -       -
events_long                     3     0      0.0       0       0       -       -
events_unbound              38306     0      0.1       -       7       -       -
events_freezable                0     0      0.0       0       0       -       -
events_power_efficient      29598     0      0.2       0       0       -       -
events_freezable_power_        10     0      0.0       0       0       -       -
sock_diag_events                0     0      0.0       0       0       -       -

                            total  infl  CPUtime  CPUhog CMW/RPR  mayday rescued
events                      18548     0      6.1       0       5       -       -
events_highpri                  8     0      0.0       0       0       -       -
events_long                     3     0      0.0       0       0       -       -
events_unbound              38322     0      0.1       -       7       -       -
events_freezable                0     0      0.0       0       0       -       -
events_power_efficient      29603     0      0.2       0       0       -       -
events_freezable_power_        10     0      0.0       0       0       -       -
sock_diag_events                0     0      0.0       0       0       -       -

...
```

See the command's help message for more info.

## Debugging

Because the work functions are executed by generic worker threads
there are a few tricks needed to shed some light on misbehaving
workqueue users.

Worker threads show up in the process list as:

```
root      5671  0.0  0.0      0     0 ?        S    12:07   0:00 [kworker/0:1]
root      5672  0.0  0.0      0     0 ?        S    12:07   0:00 [kworker/1:2]
root      5673  0.0  0.0      0     0 ?        S    12:12   0:00 [kworker/0:0]
root      5674  0.0  0.0      0     0 ?        S    12:13   0:00 [kworker/1:0]
```

If kworkers are going crazy (using too much cpu), there are two types
of possible problems:

> 1. Something being scheduled in rapid succession
> 2. A single work item that consumes lots of cpu cycles

The first one can be tracked using tracing:

```
$ echo workqueue:workqueue_queue_work > /sys/kernel/tracing/set_event
$ cat /sys/kernel/tracing/trace_pipe > out.txt
(wait a few secs)
^C
```

If something is busy looping on work queueing, it would be dominating
the output and the offender can be determined with the work item
function.

For the second type of problems it should be possible to just check
the stack trace of the offending worker thread.

```
$ cat /proc/THE_OFFENDING_KWORKER/stack
```

The work item's function should be trivially visible in the stack
trace.

## Non-reentrance Conditions

Workqueue guarantees that a work item cannot be re-entrant if the following
conditions hold after a work item gets queued:

> 1. The work function hasn't been changed.
> 2. No one queues the work item to another workqueue.
> 3. The work item hasn't been reinitiated.

In other words, if the above conditions hold, the work item is guaranteed to be
executed by at most one worker system-wide at any given time.

Note that requeuing the work item (to the same queue) in the self function
doesn't break these conditions, so it's safe to do. Otherwise, caution is
required when breaking the conditions inside a work function.

## Kernel Inline Documentations Reference

struct workqueue_attrs
:   A struct for workqueue attributes.

**Definition**:

```
struct workqueue_attrs {
    int nice;
    cpumask_var_t cpumask;
    cpumask_var_t __pod_cpumask;
    bool affn_strict;
    enum wq_affn_scope affn_scope;
    bool ordered;
};
```

**Members**

`nice`
:   nice level

`cpumask`
:   allowed CPUs

    Work items in this workqueue are affine to these CPUs and not allowed
    to execute on other CPUs. A pool serving a workqueue must have the
    same **cpumask**.

`__pod_cpumask`
:   internal attribute used to create per-pod pools

    Internal use only.

    Per-pod unbound worker pools are used to improve locality. Always a
    subset of ->cpumask. A workqueue can be associated with multiple
    worker pools with disjoint **__pod_cpumask**'s. Whether the enforcement
    of a pool's **__pod_cpumask** is strict depends on **affn_strict**.

`affn_strict`
:   affinity scope is strict

    If clear, workqueue will make a best-effort attempt at starting the
    worker inside **__pod_cpumask** but the scheduler is free to migrate it
    outside.

    If set, workers are only allowed to run inside **__pod_cpumask**.

`affn_scope`
:   unbound CPU affinity scope

    CPU pods are used to improve execution locality of unbound work
    items. There are multiple pod types, one for each wq_affn_scope, and
    every CPU in the system belongs to one pod in every pod type. CPUs
    that belong to the same pod share the worker pool. For example,
    selecting `WQ_AFFN_NUMA` makes the workqueue use a separate worker
    pool for each NUMA node.

`ordered`
:   work items must be executed one by one in queueing order

**Description**

This can be used to change attributes of an unbound workqueue.

work_pending

`work_pending (work)`

> Find out whether a work item is currently pending

**Parameters**

`work`
:   The work item in question

delayed_work_pending

`delayed_work_pending (w)`

> Find out whether a delayable work item is currently pending

**Parameters**

`w`
:   The work item in question

struct workqueue_struct \*alloc_workqueue(const char \*fmt, unsigned int flags, int max_active, ...)
:   allocate a workqueue

**Parameters**

`const char *fmt`
:   printf format for the name of the workqueue

`unsigned int flags`
:   WQ_\* flags

`int max_active`
:   max in-flight work items per CPU, 0 for default
    remaining args: args for **fmt**

`...`
:   variable arguments

**Description**

Allocate a workqueue with the specified parameters. For detailed
information on WQ_\* flags, please refer to
[Workqueue](workqueue.md).

**Return**

Pointer to the allocated workqueue on success, `NULL` on failure.

alloc_ordered_workqueue

`alloc_ordered_workqueue (fmt, flags, args...)`

> allocate an ordered workqueue

**Parameters**

`fmt`
:   printf format for the name of the workqueue

`flags`
:   WQ_\* flags (only WQ_FREEZABLE and WQ_MEM_RECLAIM are meaningful)

`args...`
:   args for **fmt**

**Description**

Allocate an ordered workqueue. An ordered workqueue executes at
most one work item at any given time in the queued order. They are
implemented as unbound workqueues with **max_active** of one.

**Return**

Pointer to the allocated workqueue on success, `NULL` on failure.

bool queue_work(struct workqueue_struct \*wq, struct work_struct \*work)
:   queue work on a workqueue

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to use

`struct work_struct *work`
:   work to queue

**Description**

Returns `false` if **work** was already on a queue, `true` otherwise.

We queue the work to the CPU on which it was submitted, but if the CPU dies
it can be processed by another CPU.

Memory-ordering properties: If it returns `true`, guarantees that all stores
preceding the call to [`queue_work()`](workqueue.md#c.queue_work "queue_work") in the program order will be visible from
the CPU which will execute **work** by the time such work executes, e.g.,

{ x is initially 0 }

> CPU0 CPU1
>
> WRITE_ONCE(x, 1); [ **work** is being executed ]
> r0 = queue_work(wq, work); r1 = READ_ONCE(x);

Forbids: r0 == true && r1 == 0

bool queue_delayed_work(struct workqueue_struct \*wq, struct delayed_work \*dwork, unsigned long delay)
:   queue work on a workqueue after delay

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to use

`struct delayed_work *dwork`
:   delayable work to queue

`unsigned long delay`
:   number of jiffies to wait before queueing

**Description**

Equivalent to [`queue_delayed_work_on()`](workqueue.md#c.queue_delayed_work_on "queue_delayed_work_on") but tries to use the local CPU.

bool mod_delayed_work(struct workqueue_struct \*wq, struct delayed_work \*dwork, unsigned long delay)
:   modify delay of or queue a delayed work

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to use

`struct delayed_work *dwork`
:   work to queue

`unsigned long delay`
:   number of jiffies to wait before queueing

**Description**

[`mod_delayed_work_on()`](workqueue.md#c.mod_delayed_work_on "mod_delayed_work_on") on local CPU.

bool schedule_work_on(int cpu, struct work_struct \*work)
:   put work task on a specific cpu

**Parameters**

`int cpu`
:   cpu to put the work task on

`struct work_struct *work`
:   job to be done

**Description**

This puts a job on a specific cpu

bool schedule_work(struct work_struct \*work)
:   put work task in global workqueue

**Parameters**

`struct work_struct *work`
:   job to be done

**Description**

Returns `false` if **work** was already on the kernel-global workqueue and
`true` otherwise.

This puts a job in the kernel-global workqueue if it was not already
queued and leaves it in the same position on the kernel-global
workqueue otherwise.

Shares the same memory-ordering properties of [`queue_work()`](workqueue.md#c.queue_work "queue_work"), cf. the
DocBook header of [`queue_work()`](workqueue.md#c.queue_work "queue_work").

bool schedule_delayed_work_on(int cpu, struct delayed_work \*dwork, unsigned long delay)
:   queue work in global workqueue on CPU after delay

**Parameters**

`int cpu`
:   cpu to use

`struct delayed_work *dwork`
:   job to be done

`unsigned long delay`
:   number of jiffies to wait

**Description**

After waiting for a given time this puts a job in the kernel-global
workqueue on the specified CPU.

bool schedule_delayed_work(struct delayed_work \*dwork, unsigned long delay)
:   put work task in global workqueue after delay

**Parameters**

`struct delayed_work *dwork`
:   job to be done

`unsigned long delay`
:   number of jiffies to wait or 0 for immediate execution

**Description**

After waiting for a given time this puts a job in the kernel-global
workqueue.

for_each_pool

`for_each_pool (pool, pi)`

> iterate through all worker_pools in the system

**Parameters**

`pool`
:   iteration cursor

`pi`
:   integer used for iteration

**Description**

This must be called either with wq_pool_mutex held or RCU read
locked. If the pool needs to be used beyond the locking in effect, the
caller is responsible for guaranteeing that the pool stays online.

The if/else clause exists only for the lockdep assertion and can be
ignored.

for_each_pool_worker

`for_each_pool_worker (worker, pool)`

> iterate through all workers of a worker_pool

**Parameters**

`worker`
:   iteration cursor

`pool`
:   worker_pool to iterate workers of

**Description**

This must be called with wq_pool_attach_mutex.

The if/else clause exists only for the lockdep assertion and can be
ignored.

for_each_pwq

`for_each_pwq (pwq, wq)`

> iterate through all pool_workqueues of the specified workqueue

**Parameters**

`pwq`
:   iteration cursor

`wq`
:   the target workqueue

**Description**

This must be called either with wq->mutex held or RCU read locked.
If the pwq needs to be used beyond the locking in effect, the caller is
responsible for guaranteeing that the pwq stays online.

The if/else clause exists only for the lockdep assertion and can be
ignored.

int worker_pool_assign_id(struct worker_pool \*pool)
:   allocate ID and assign it to **pool**

**Parameters**

`struct worker_pool *pool`
:   the pool pointer of interest

**Description**

Returns 0 if ID in [0, WORK_OFFQ_POOL_NONE) is allocated and assigned
successfully, -errno on failure.

struct worker_pool \*get_work_pool(struct work_struct \*work)
:   return the worker_pool a given work was associated with

**Parameters**

`struct work_struct *work`
:   the work item of interest

**Description**

Pools are created and destroyed under wq_pool_mutex, and allows read
access under RCU read lock. As such, this function should be
called under wq_pool_mutex or inside of a [`rcu_read_lock()`](kernel-api.md#c.rcu_read_lock "rcu_read_lock") region.

All fields of the returned pool are accessible as long as the above
mentioned locking is in effect. If the returned pool needs to be used
beyond the critical section, the caller is responsible for ensuring the
returned pool is and stays online.

**Return**

The worker_pool **work** was last associated with. `NULL` if none.

int get_work_pool_id(struct work_struct \*work)
:   return the worker pool ID a given work is associated with

**Parameters**

`struct work_struct *work`
:   the work item of interest

**Return**

The worker_pool ID **work** was last associated with.
`WORK_OFFQ_POOL_NONE` if none.

void worker_set_flags(struct [worker](workqueue.md#c.worker_set_flags "worker") \*worker, unsigned int flags)
:   set worker flags and adjust nr_running accordingly

**Parameters**

`struct worker *worker`
:   self

`unsigned int flags`
:   flags to set

**Description**

Set **flags** in **worker->flags** and adjust nr_running accordingly.

void worker_clr_flags(struct [worker](workqueue.md#c.worker_clr_flags "worker") \*worker, unsigned int flags)
:   clear worker flags and adjust nr_running accordingly

**Parameters**

`struct worker *worker`
:   self

`unsigned int flags`
:   flags to clear

**Description**

Clear **flags** in **worker->flags** and adjust nr_running accordingly.

void worker_enter_idle(struct [worker](workqueue.md#c.worker_enter_idle "worker") \*worker)
:   enter idle state

**Parameters**

`struct worker *worker`
:   worker which is entering idle state

**Description**

**worker** is entering idle state. Update stats and idle timer if
necessary.

LOCKING:
raw_spin_lock_irq(pool->lock).

void worker_leave_idle(struct [worker](workqueue.md#c.worker_leave_idle "worker") \*worker)
:   leave idle state

**Parameters**

`struct worker *worker`
:   worker which is leaving idle state

**Description**

**worker** is leaving idle state. Update stats.

LOCKING:
raw_spin_lock_irq(pool->lock).

struct worker \*find_worker_executing_work(struct worker_pool \*pool, struct work_struct \*work)
:   find worker which is executing a work

**Parameters**

`struct worker_pool *pool`
:   pool of interest

`struct work_struct *work`
:   work to find worker for

**Description**

Find a worker which is executing **work** on **pool** by searching
**pool->busy_hash** which is keyed by the address of **work**. For a worker
to match, its current execution should match the address of **work** and
its work function. This is to avoid unwanted dependency between
unrelated work executions through a work item being recycled while still
being executed.

This is a bit tricky. A work item may be freed once its execution
starts and nothing prevents the freed area from being recycled for
another work item. If the same work item address ends up being reused
before the original execution finishes, workqueue will identify the
recycled work item as currently executing and make it wait until the
current execution finishes, introducing an unwanted dependency.

This function checks the work item address and work function to avoid
false positives. Note that this isn't complete as one may construct a
work function which can introduce dependency onto itself through a
recycled work item. Well, if somebody wants to shoot oneself in the
foot that badly, there's only so much we can do, and if such deadlock
actually occurs, it should be easy to locate the culprit work function.

**Context**

raw_spin_lock_irq(pool->lock).

**Return**

Pointer to worker which is executing **work** if found, `NULL`
otherwise.

void move_linked_works(struct work_struct \*work, struct list_head \*head, struct work_struct \*\*nextp)
:   move linked works to a list

**Parameters**

`struct work_struct *work`
:   start of series of works to be scheduled

`struct list_head *head`
:   target list to append **work** to

`struct work_struct **nextp`
:   out parameter for nested worklist walking

**Description**

Schedule linked works starting from **work** to **head**. Work series to be
scheduled starts at **work** and includes any consecutive work with
WORK_STRUCT_LINKED set in its predecessor. See [`assign_work()`](workqueue.md#c.assign_work "assign_work") for details on
**nextp**.

**Context**

raw_spin_lock_irq(pool->lock).

bool assign_work(struct work_struct \*work, struct [worker](workqueue.md#c.assign_work "worker") \*worker, struct work_struct \*\*nextp)
:   assign a work item and its linked work items to a worker

**Parameters**

`struct work_struct *work`
:   work to assign

`struct worker *worker`
:   worker to assign to

`struct work_struct **nextp`
:   out parameter for nested worklist walking

**Description**

Assign **work** and its linked work items to **worker**. If **work** is already being
executed by another worker in the same pool, it'll be punted there.

If **nextp** is not NULL, it's updated to point to the next work of the last
scheduled work. This allows [`assign_work()`](workqueue.md#c.assign_work "assign_work") to be nested inside
[`list_for_each_entry_safe()`](kernel-api.md#c.list_for_each_entry_safe "list_for_each_entry_safe").

Returns `true` if **work** was successfully assigned to **worker**. `false` if **work**
was punted to another worker already executing it.

bool kick_pool(struct worker_pool \*pool)
:   wake up an idle worker if necessary

**Parameters**

`struct worker_pool *pool`
:   pool to kick

**Description**

**pool** may have pending work items. Wake up worker if necessary. Returns
whether a worker was woken up.

void wq_worker_running(struct task_struct \*task)
:   a worker is running again

**Parameters**

`struct task_struct *task`
:   task waking up

**Description**

This function is called when a worker returns from schedule()

void wq_worker_sleeping(struct task_struct \*task)
:   a worker is going to sleep

**Parameters**

`struct task_struct *task`
:   task going to sleep

**Description**

This function is called from schedule() when a busy worker is
going to sleep.

void wq_worker_tick(struct task_struct \*task)
:   a scheduler tick occurred while a kworker is running

**Parameters**

`struct task_struct *task`
:   task currently running

**Description**

Called from scheduler_tick(). We're in the IRQ context and the current
worker's fields which follow the 'K' locking rule can be accessed safely.

work_func_t wq_worker_last_func(struct task_struct \*task)
:   retrieve worker's last work function

**Parameters**

`struct task_struct *task`
:   Task to retrieve last work function of.

**Description**

Determine the last function a worker executed. This is called from
the scheduler to get a worker's last known identity.

This function is called during schedule() when a kworker is going
to sleep. It's used by psi to identify aggregation workers during
dequeuing, to allow periodic aggregation to shut-off when that
worker is the last task in the system or cgroup to go to sleep.

As this function doesn't involve any workqueue-related locking, it
only returns stable values when called from inside the scheduler's
queuing and dequeuing paths, when **task**, which must be a kworker,
is guaranteed to not be processing any works.

**Context**

raw_spin_lock_irq(rq->lock)

**Return**

The last work function `current` executed as a worker, NULL if it
hasn't executed any work yet.

void get_pwq(struct pool_workqueue \*pwq)
:   get an extra reference on the specified pool_workqueue

**Parameters**

`struct pool_workqueue *pwq`
:   pool_workqueue to get

**Description**

Obtain an extra reference on **pwq**. The caller should guarantee that
**pwq** has positive refcnt and be holding the matching pool->lock.

void put_pwq(struct pool_workqueue \*pwq)
:   put a pool_workqueue reference

**Parameters**

`struct pool_workqueue *pwq`
:   pool_workqueue to put

**Description**

Drop a reference of **pwq**. If its refcnt reaches zero, schedule its
destruction. The caller should be holding the matching pool->lock.

void put_pwq_unlocked(struct pool_workqueue \*pwq)
:   [`put_pwq()`](workqueue.md#c.put_pwq "put_pwq") with surrounding pool lock/unlock

**Parameters**

`struct pool_workqueue *pwq`
:   pool_workqueue to put (can be `NULL`)

**Description**

[`put_pwq()`](workqueue.md#c.put_pwq "put_pwq") with locking. This function also allows `NULL` **pwq**.

void pwq_dec_nr_in_flight(struct pool_workqueue \*pwq, unsigned long work_data)
:   decrement pwq's nr_in_flight

**Parameters**

`struct pool_workqueue *pwq`
:   pwq of interest

`unsigned long work_data`
:   work_data of work which left the queue

**Description**

A work either has completed or is removed from pending queue,
decrement nr_in_flight of its pwq and handle workqueue flushing.

**Context**

raw_spin_lock_irq(pool->lock).

int try_to_grab_pending(struct work_struct \*work, bool is_dwork, unsigned long \*flags)
:   steal work item from worklist and disable irq

**Parameters**

`struct work_struct *work`
:   work item to steal

`bool is_dwork`
:   **work** is a delayed_work

`unsigned long *flags`
:   place to store irq state

**Description**

Try to grab PENDING bit of **work**. This function can handle **work** in any
stable state - idle, on timer or on worklist.

On successful return, >= 0, irq is disabled and the caller is
responsible for releasing it using local_irq_restore(**\*flags**).

This function is safe to call from any context including IRQ handler.

**Return**

> |  |  |
> | --- | --- |
> | 1 | if **work** was pending and we successfully stole PENDING |
> | 0 | if **work** was idle and we claimed PENDING |
> | -EAGAIN | if PENDING couldn't be grabbed at the moment, safe to busy-retry |
> | -ENOENT | if someone else is canceling **work**, this state may persist for arbitrarily long |

**Note**

On >= 0 return, the caller owns **work**'s PENDING bit. To avoid getting
interrupted while holding PENDING and **work** off queue, irq must be
disabled on entry. This, combined with delayed_work->timer being
irqsafe, ensures that we return -EAGAIN for finite short period of time.

void insert_work(struct pool_workqueue \*pwq, struct work_struct \*work, struct list_head \*head, unsigned int extra_flags)
:   insert a work into a pool

**Parameters**

`struct pool_workqueue *pwq`
:   pwq **work** belongs to

`struct work_struct *work`
:   work to insert

`struct list_head *head`
:   insertion point

`unsigned int extra_flags`
:   extra WORK_STRUCT_\* flags to set

**Description**

Insert **work** which belongs to **pwq** after **head**. **extra_flags** is or'd to
work_struct flags.

**Context**

raw_spin_lock_irq(pool->lock).

bool queue_work_on(int cpu, struct workqueue_struct \*wq, struct work_struct \*work)
:   queue work on specific cpu

**Parameters**

`int cpu`
:   CPU number to execute work on

`struct workqueue_struct *wq`
:   workqueue to use

`struct work_struct *work`
:   work to queue

**Description**

We queue the work to a specific CPU, the caller must ensure it
can't go away. Callers that fail to ensure that the specified
CPU cannot go away will execute on a randomly chosen CPU.
But note well that callers specifying a CPU that never has been
online will get a splat.

**Return**

`false` if **work** was already on a queue, `true` otherwise.

int select_numa_node_cpu(int node)
:   Select a CPU based on NUMA node

**Parameters**

`int node`
:   NUMA node ID that we want to select a CPU from

**Description**

This function will attempt to find a "random" cpu available on a given
node. If there are no CPUs available on the given node it will return
WORK_CPU_UNBOUND indicating that we should just schedule to any
available CPU if we need to schedule this work.

bool queue_work_node(int node, struct workqueue_struct \*wq, struct work_struct \*work)
:   queue work on a "random" cpu for a given NUMA node

**Parameters**

`int node`
:   NUMA node that we are targeting the work for

`struct workqueue_struct *wq`
:   workqueue to use

`struct work_struct *work`
:   work to queue

**Description**

We queue the work to a "random" CPU within a given NUMA node. The basic
idea here is to provide a way to somehow associate work with a given
NUMA node.

This function will only make a best effort attempt at getting this onto
the right NUMA node. If no node is requested or the requested node is
offline then we just fall back to standard queue_work behavior.

Currently the "random" CPU ends up being the first available CPU in the
intersection of cpu_online_mask and the cpumask of the node, unless we
are running on the node. In that case we just use the current CPU.

**Return**

`false` if **work** was already on a queue, `true` otherwise.

bool queue_delayed_work_on(int cpu, struct workqueue_struct \*wq, struct delayed_work \*dwork, unsigned long delay)
:   queue work on specific CPU after delay

**Parameters**

`int cpu`
:   CPU number to execute work on

`struct workqueue_struct *wq`
:   workqueue to use

`struct delayed_work *dwork`
:   work to queue

`unsigned long delay`
:   number of jiffies to wait before queueing

**Return**

`false` if **work** was already on a queue, `true` otherwise. If
**delay** is zero and **dwork** is idle, it will be scheduled for immediate
execution.

bool mod_delayed_work_on(int cpu, struct workqueue_struct \*wq, struct delayed_work \*dwork, unsigned long delay)
:   modify delay of or queue a delayed work on specific CPU

**Parameters**

`int cpu`
:   CPU number to execute work on

`struct workqueue_struct *wq`
:   workqueue to use

`struct delayed_work *dwork`
:   work to queue

`unsigned long delay`
:   number of jiffies to wait before queueing

**Description**

If **dwork** is idle, equivalent to [`queue_delayed_work_on()`](workqueue.md#c.queue_delayed_work_on "queue_delayed_work_on"); otherwise,
modify **dwork**'s timer so that it expires after **delay**. If **delay** is
zero, **work** is guaranteed to be scheduled immediately regardless of its
current state.

This function is safe to call from any context including IRQ handler.
See [`try_to_grab_pending()`](workqueue.md#c.try_to_grab_pending "try_to_grab_pending") for details.

**Return**

`false` if **dwork** was idle and queued, `true` if **dwork** was
pending and its timer was modified.

bool queue_rcu_work(struct workqueue_struct \*wq, struct rcu_work \*rwork)
:   queue work after a RCU grace period

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to use

`struct rcu_work *rwork`
:   work to queue

**Return**

`false` if **rwork** was already pending, `true` otherwise. Note
that a full RCU grace period is guaranteed only after a `true` return.
While **rwork** is guaranteed to be executed after a `false` return, the
execution may happen before a full RCU grace period has passed.

void worker_attach_to_pool(struct [worker](workqueue.md#c.worker_attach_to_pool "worker") \*worker, struct worker_pool \*pool)
:   attach a worker to a pool

**Parameters**

`struct worker *worker`
:   worker to be attached

`struct worker_pool *pool`
:   the target pool

**Description**

Attach **worker** to **pool**. Once attached, the `WORKER_UNBOUND` flag and
cpu-binding of **worker** are kept coordinated with the pool across
cpu-[un]hotplugs.

void worker_detach_from_pool(struct [worker](workqueue.md#c.worker_detach_from_pool "worker") \*worker)
:   detach a worker from its pool

**Parameters**

`struct worker *worker`
:   worker which is attached to its pool

**Description**

Undo the attaching which had been done in [`worker_attach_to_pool()`](workqueue.md#c.worker_attach_to_pool "worker_attach_to_pool"). The
caller worker shouldn't access to the pool after detached except it has
other reference to the pool.

struct worker \*create_worker(struct worker_pool \*pool)
:   create a new workqueue worker

**Parameters**

`struct worker_pool *pool`
:   pool the new worker will belong to

**Description**

Create and start a new worker which is attached to **pool**.

**Context**

Might sleep. Does GFP_KERNEL allocations.

**Return**

Pointer to the newly created worker.

void set_worker_dying(struct [worker](workqueue.md#c.set_worker_dying "worker") \*worker, struct list_head \*list)
:   Tag a worker for destruction

**Parameters**

`struct worker *worker`
:   worker to be destroyed

`struct list_head *list`
:   transfer worker away from its pool->idle_list and into list

**Description**

Tag **worker** for destruction and adjust **pool** stats accordingly. The worker
should be idle.

**Context**

raw_spin_lock_irq(pool->lock).

void idle_worker_timeout(struct timer_list \*t)
:   check if some idle workers can now be deleted.

**Parameters**

`struct timer_list *t`
:   The pool's idle_timer that just expired

**Description**

The timer is armed in [`worker_enter_idle()`](workqueue.md#c.worker_enter_idle "worker_enter_idle"). Note that it isn't disarmed in
[`worker_leave_idle()`](workqueue.md#c.worker_leave_idle "worker_leave_idle"), as a worker flicking between idle and active while its
pool is at the too_many_workers() tipping point would cause too much timer
housekeeping overhead. Since IDLE_WORKER_TIMEOUT is long enough, we just let
it expire and re-evaluate things from there.

void idle_cull_fn(struct work_struct \*work)
:   cull workers that have been idle for too long.

**Parameters**

`struct work_struct *work`
:   the pool's work for handling these idle workers

**Description**

This goes through a pool's idle workers and gets rid of those that have been
idle for at least IDLE_WORKER_TIMEOUT seconds.

We don't want to disturb isolated CPUs because of a pcpu kworker being
culled, so this also resets worker affinity. This requires a sleepable
context, hence the split between timer callback and work item.

void maybe_create_worker(struct worker_pool \*pool)
:   create a new worker if necessary

**Parameters**

`struct worker_pool *pool`
:   pool to create a new worker for

**Description**

Create a new worker for **pool** if necessary. **pool** is guaranteed to
have at least one idle worker on return from this function. If
creating a new worker takes longer than MAYDAY_INTERVAL, mayday is
sent to all rescuers with works scheduled on **pool** to resolve
possible allocation deadlock.

On return, need_to_create_worker() is guaranteed to be `false` and
may_start_working() `true`.

LOCKING:
raw_spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times. Does GFP_KERNEL allocations. Called only from
manager.

bool manage_workers(struct [worker](workqueue.md#c.manage_workers "worker") \*worker)
:   manage worker pool

**Parameters**

`struct worker *worker`
:   self

**Description**

Assume the manager role and manage the worker pool **worker** belongs
to. At any given time, there can be only zero or one manager per
pool. The exclusion is handled automatically by this function.

The caller can safely start processing works on false return. On
true return, it's guaranteed that need_to_create_worker() is false
and may_start_working() is true.

**Context**

raw_spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times. Does GFP_KERNEL allocations.

**Return**

`false` if the pool doesn't need management and the caller can safely
start processing works, `true` if management function was performed and
the conditions that the caller verified before calling the function may
no longer be true.

void process_one_work(struct [worker](workqueue.md#c.process_one_work "worker") \*worker, struct work_struct \*work)
:   process single work

**Parameters**

`struct worker *worker`
:   self

`struct work_struct *work`
:   work to process

**Description**

Process **work**. This function contains all the logics necessary to
process a single work including synchronization against and
interaction with other workers on the same cpu, queueing and
flushing. As long as context requirement is met, any worker can
call this function to process a work.

**Context**

raw_spin_lock_irq(pool->lock) which is released and regrabbed.

void process_scheduled_works(struct [worker](workqueue.md#c.process_scheduled_works "worker") \*worker)
:   process scheduled works

**Parameters**

`struct worker *worker`
:   self

**Description**

Process all scheduled works. Please note that the scheduled list
may change while processing a work, so this function repeatedly
fetches a work from the top and executes it.

**Context**

raw_spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times.

int worker_thread(void \*__worker)
:   the worker thread function

**Parameters**

`void *__worker`
:   self

**Description**

The worker thread function. All workers belong to a worker_pool -
either a per-cpu one or dynamic unbound one. These workers process all
work items regardless of their specific target workqueue. The only
exception is work items which belong to workqueues with a rescuer which
will be explained in [`rescuer_thread()`](workqueue.md#c.rescuer_thread "rescuer_thread").

**Return**

0

int rescuer_thread(void \*__rescuer)
:   the rescuer thread function

**Parameters**

`void *__rescuer`
:   self

**Description**

Workqueue rescuer thread function. There's one rescuer for each
workqueue which has WQ_MEM_RECLAIM set.

Regular work processing on a pool may block trying to create a new
worker which uses GFP_KERNEL allocation which has slight chance of
developing into deadlock if some works currently on the same queue
need to be processed to satisfy the GFP_KERNEL allocation. This is
the problem rescuer solves.

When such condition is possible, the pool summons rescuers of all
workqueues which have works queued on the pool and let them process
those works so that forward progress can be guaranteed.

This should happen rarely.

**Return**

0

void check_flush_dependency(struct workqueue_struct \*target_wq, struct work_struct \*target_work)
:   check for flush dependency sanity

**Parameters**

`struct workqueue_struct *target_wq`
:   workqueue being flushed

`struct work_struct *target_work`
:   work item being flushed (NULL for workqueue flushes)

**Description**

`current` is trying to flush the whole **target_wq** or **target_work** on it.
If **target_wq** doesn't have `WQ_MEM_RECLAIM`, verify that `current` is not
reclaiming memory or running on a workqueue which doesn't have
`WQ_MEM_RECLAIM` as that can break forward-progress guarantee leading to
a deadlock.

void insert_wq_barrier(struct pool_workqueue \*pwq, struct wq_barrier \*barr, struct work_struct \*target, struct [worker](workqueue.md#c.insert_wq_barrier "worker") \*worker)
:   insert a barrier work

**Parameters**

`struct pool_workqueue *pwq`
:   pwq to insert barrier into

`struct wq_barrier *barr`
:   wq_barrier to insert

`struct work_struct *target`
:   target work to attach **barr** to

`struct worker *worker`
:   worker currently executing **target**, NULL if **target** is not executing

**Description**

**barr** is linked to **target** such that **barr** is completed only after
**target** finishes execution. Please note that the ordering
guarantee is observed only with respect to **target** and on the local
cpu.

Currently, a queued barrier can't be canceled. This is because
[`try_to_grab_pending()`](workqueue.md#c.try_to_grab_pending "try_to_grab_pending") can't determine whether the work to be
grabbed is at the head of the queue and thus can't clear LINKED
flag of the previous work while there must be a valid next work
after a work with LINKED flag set.

Note that when **worker** is non-NULL, **target** may be modified
underneath us, so we can't reliably determine pwq from **target**.

**Context**

raw_spin_lock_irq(pool->lock).

bool flush_workqueue_prep_pwqs(struct workqueue_struct \*wq, int flush_color, int work_color)
:   prepare pwqs for workqueue flushing

**Parameters**

`struct workqueue_struct *wq`
:   workqueue being flushed

`int flush_color`
:   new flush color, < 0 for no-op

`int work_color`
:   new work color, < 0 for no-op

**Description**

Prepare pwqs for workqueue flushing.

If **flush_color** is non-negative, flush_color on all pwqs should be
-1. If no pwq has in-flight commands at the specified color, all
pwq->flush_color's stay at -1 and `false` is returned. If any pwq
has in flight commands, its pwq->flush_color is set to
**flush_color**, **wq->nr_pwqs_to_flush** is updated accordingly, pwq
wakeup logic is armed and `true` is returned.

The caller should have initialized **wq->first_flusher** prior to
calling this function with non-negative **flush_color**. If
**flush_color** is negative, no flush color update is done and `false`
is returned.

If **work_color** is non-negative, all pwqs should have the same
work_color which is previous to **work_color** and all will be
advanced to **work_color**.

**Context**

mutex_lock(wq->mutex).

**Return**

`true` if **flush_color** >= 0 and there's something to flush. `false`
otherwise.

void __flush_workqueue(struct workqueue_struct \*wq)
:   ensure that any scheduled work has run to completion.

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to flush

**Description**

This function sleeps until all work items which were queued on entry
have finished execution, but it is not livelocked by new incoming ones.

void drain_workqueue(struct workqueue_struct \*wq)
:   drain a workqueue

**Parameters**

`struct workqueue_struct *wq`
:   workqueue to drain

**Description**

Wait until the workqueue becomes empty. While draining is in progress,
only chain queueing is allowed. IOW, only currently pending or running
work items on **wq** can queue further work items on it. **wq** is flushed
repeatedly until it becomes empty. The number of flushing is determined
by the depth of chaining and should be relatively short. Whine if it
takes too long.

bool flush_work(struct work_struct \*work)
:   wait for a work to finish executing the last queueing instance

**Parameters**

`struct work_struct *work`
:   the work to flush

**Description**

Wait until **work** has finished execution. **work** is guaranteed to be idle
on return if it hasn't been requeued since flush started.

**Return**

`true` if [`flush_work()`](workqueue.md#c.flush_work "flush_work") waited for the work to finish execution,
`false` if it was already idle.

bool cancel_work_sync(struct work_struct \*work)
:   cancel a work and wait for it to finish

**Parameters**

`struct work_struct *work`
:   the work to cancel

**Description**

Cancel **work** and wait for its execution to finish. This function
can be used even if the work re-queues itself or migrates to
another workqueue. On return from this function, **work** is
guaranteed to be not pending or executing on any CPU.

cancel_work_sync(`delayed_work->work`) must not be used for
delayed_work's. Use [`cancel_delayed_work_sync()`](workqueue.md#c.cancel_delayed_work_sync "cancel_delayed_work_sync") instead.

The caller must ensure that the workqueue on which **work** was last
queued can't be destroyed before this function returns.

**Return**

`true` if **work** was pending, `false` otherwise.

bool flush_delayed_work(struct delayed_work \*dwork)
:   wait for a dwork to finish executing the last queueing

**Parameters**

`struct delayed_work *dwork`
:   the delayed work to flush

**Description**

Delayed timer is cancelled and the pending work is queued for
immediate execution. Like [`flush_work()`](workqueue.md#c.flush_work "flush_work"), this function only
considers the last queueing instance of **dwork**.

**Return**

`true` if [`flush_work()`](workqueue.md#c.flush_work "flush_work") waited for the work to finish execution,
`false` if it was already idle.

bool flush_rcu_work(struct rcu_work \*rwork)
:   wait for a rwork to finish executing the last queueing

**Parameters**

`struct rcu_work *rwork`
:   the rcu work to flush

**Return**

`true` if [`flush_rcu_work()`](workqueue.md#c.flush_rcu_work "flush_rcu_work") waited for the work to finish execution,
`false` if it was already idle.

bool cancel_delayed_work(struct delayed_work \*dwork)
:   cancel a delayed work

**Parameters**

`struct delayed_work *dwork`
:   delayed_work to cancel

**Description**

Kill off a pending delayed_work.

This function is safe to call from any context including IRQ handler.

**Return**

`true` if **dwork** was pending and canceled; `false` if it wasn't
pending.

**Note**

The work callback function may still be running on return, unless
it returns `true` and the work doesn't re-arm itself. Explicitly flush or
use [`cancel_delayed_work_sync()`](workqueue.md#c.cancel_delayed_work_sync "cancel_delayed_work_sync") to wait on it.

bool cancel_delayed_work_sync(struct delayed_work \*dwork)
:   cancel a delayed work and wait for it to finish

**Parameters**

`struct delayed_work *dwork`
:   the delayed work cancel

**Description**

This is [`cancel_work_sync()`](workqueue.md#c.cancel_work_sync "cancel_work_sync") for delayed works.

**Return**

`true` if **dwork** was pending, `false` otherwise.

int schedule_on_each_cpu(work_func_t func)
:   execute a function synchronously on each online CPU

**Parameters**

`work_func_t func`
:   the function to call

**Description**

[`schedule_on_each_cpu()`](workqueue.md#c.schedule_on_each_cpu "schedule_on_each_cpu") executes **func** on each online CPU using the
system workqueue and blocks until all CPUs have completed.
[`schedule_on_each_cpu()`](workqueue.md#c.schedule_on_each_cpu "schedule_on_each_cpu") is very slow.

**Return**

0 on success, -errno on failure.

int execute_in_process_context(work_func_t fn, struct execute_work \*ew)
:   reliably execute the routine with user context

**Parameters**

`work_func_t fn`
:   the function to execute

`struct execute_work *ew`
:   guaranteed storage for the execute work structure (must
    be available when the work executes)

**Description**

Executes the function immediately if process context is available,
otherwise schedules the function for delayed execution.

**Return**

0 - function was executed
:   1 - function was scheduled for execution

void free_workqueue_attrs(struct [workqueue_attrs](workqueue.md#c.workqueue_attrs "workqueue_attrs") \*attrs)
:   free a workqueue_attrs

**Parameters**

`struct workqueue_attrs *attrs`
:   workqueue_attrs to free

**Description**

Undo [`alloc_workqueue_attrs()`](workqueue.md#c.alloc_workqueue_attrs "alloc_workqueue_attrs").

struct [workqueue_attrs](workqueue.md#c.workqueue_attrs "workqueue_attrs") \*alloc_workqueue_attrs(void)
:   allocate a workqueue_attrs

**Parameters**

`void`
:   no arguments

**Description**

Allocate a new workqueue_attrs, initialize with default settings and
return it.

**Return**

The allocated new workqueue_attr on success. `NULL` on failure.

int init_worker_pool(struct worker_pool \*pool)
:   initialize a newly zalloc'd worker_pool

**Parameters**

`struct worker_pool *pool`
:   worker_pool to initialize

**Description**

Initialize a newly zalloc'd **pool**. It also allocates **pool->attrs**.

**Return**

0 on success, -errno on failure. Even on failure, all fields
inside **pool** proper are initialized and [`put_unbound_pool()`](workqueue.md#c.put_unbound_pool "put_unbound_pool") can be called
on **pool** safely to release it.

void put_unbound_pool(struct worker_pool \*pool)
:   put a worker_pool

**Parameters**

`struct worker_pool *pool`
:   worker_pool to put

**Description**

Put **pool**. If its refcnt reaches zero, it gets destroyed in RCU
safe manner. [`get_unbound_pool()`](workqueue.md#c.get_unbound_pool "get_unbound_pool") calls this function on its failure path
and this function should be able to release pools which went through,
successfully or not, [`init_worker_pool()`](workqueue.md#c.init_worker_pool "init_worker_pool").

Should be called with wq_pool_mutex held.

struct worker_pool \*get_unbound_pool(const struct [workqueue_attrs](workqueue.md#c.workqueue_attrs "workqueue_attrs") \*attrs)
:   get a worker_pool with the specified attributes

**Parameters**

`const struct workqueue_attrs *attrs`
:   the attributes of the worker_pool to get

**Description**

Obtain a worker_pool which has the same attributes as **attrs**, bump the
reference count and return it. If there already is a matching
worker_pool, it will be used; otherwise, this function attempts to
create a new one.

Should be called with wq_pool_mutex held.

**Return**

On success, a worker_pool with the same attributes as **attrs**.
On failure, `NULL`.

void pwq_adjust_max_active(struct pool_workqueue \*pwq)
:   update a pwq's max_active to the current setting

**Parameters**

`struct pool_workqueue *pwq`
:   target pool_workqueue

**Description**

If **pwq** isn't freezing, set **pwq->max_active** to the associated
workqueue's saved_max_active and activate inactive work items
accordingly. If **pwq** is freezing, clear **pwq->max_active** to zero.

void wq_calc_pod_cpumask(struct [workqueue_attrs](workqueue.md#c.workqueue_attrs "workqueue_attrs") \*attrs, int cpu, int cpu_going_down)
:   calculate a wq_attrs' cpumask for a pod

**Parameters**

`struct workqueue_attrs *attrs`
:   the wq_attrs of the default pwq of the target workqueue

`int cpu`
:   the target CPU

`int cpu_going_down`
:   if >= 0, the CPU to consider as offline

**Description**

Calculate the cpumask a workqueue with **attrs** should use on **pod**. If
**cpu_going_down** is >= 0, that cpu is considered offline during calculation.
The result is stored in **attrs->__pod_cpumask**.

If pod affinity is not enabled, **attrs->cpumask** is always used. If enabled
and **pod** has online CPUs requested by **attrs**, the returned cpumask is the
intersection of the possible CPUs of **pod** and **attrs->cpumask**.

The caller is responsible for ensuring that the cpumask of **pod** stays stable.

int apply_workqueue_attrs(struct workqueue_struct \*wq, const struct [workqueue_attrs](workqueue.md#c.workqueue_attrs "workqueue_attrs") \*attrs)
:   apply new workqueue_attrs to an unbound workqueue

**Parameters**

`struct workqueue_struct *wq`
:   the target workqueue

`const struct workqueue_attrs *attrs`
:   the workqueue_attrs to apply, allocated with [`alloc_workqueue_attrs()`](workqueue.md#c.alloc_workqueue_attrs "alloc_workqueue_attrs")

**Description**

Apply **attrs** to an unbound workqueue **wq**. Unless disabled, this function maps
a separate pwq to each CPU pod with possibles CPUs in **attrs->cpumask** so that
work items are affine to the pod it was issued on. Older pwqs are released as
in-flight work items finish. Note that a work item which repeatedly requeues
itself back-to-back will stay on its current pwq.

Performs GFP_KERNEL allocations.

Assumes caller has CPU hotplug read exclusion, i.e. cpus_read_lock().

**Return**

0 on success and -errno on failure.

void wq_update_pod(struct workqueue_struct \*wq, int cpu, int hotplug_cpu, bool online)
:   update pod affinity of a wq for CPU hot[un]plug

**Parameters**

`struct workqueue_struct *wq`
:   the target workqueue

`int cpu`
:   the CPU to update pool association for

`int hotplug_cpu`
:   the CPU coming up or going down

`bool online`
:   whether **cpu** is coming up or going down

**Description**

This function is to be called from `CPU_DOWN_PREPARE`, `CPU_ONLINE` and
`CPU_DOWN_FAILED`. **cpu** is being hot[un]plugged, update pod affinity of
**wq** accordingly.

If pod affinity can't be adjusted due to memory allocation failure, it falls
back to **wq->dfl_pwq** which may not be optimal but is always correct.

Note that when the last allowed CPU of a pod goes offline for a workqueue
with a cpumask spanning multiple pods, the workers which were already
executing the work items for the workqueue will lose their CPU affinity and
may execute on any CPU. This is similar to how per-cpu workqueues behave on
CPU_DOWN. If a workqueue user wants strict affinity, it's the user's
responsibility to flush the work item from CPU_DOWN_PREPARE.

void destroy_workqueue(struct workqueue_struct \*wq)
:   safely terminate a workqueue

**Parameters**

`struct workqueue_struct *wq`
:   target workqueue

**Description**

Safely destroy a workqueue. All work currently pending will be done first.

void workqueue_set_max_active(struct workqueue_struct \*wq, int max_active)
:   adjust max_active of a workqueue

**Parameters**

`struct workqueue_struct *wq`
:   target workqueue

`int max_active`
:   new max_active value.

**Description**

Set max_active of **wq** to **max_active**.

**Context**

Don't call from IRQ context.

struct work_struct \*current_work(void)
:   retrieve `current` task's work struct

**Parameters**

`void`
:   no arguments

**Description**

Determine if `current` task is a workqueue worker and what it's working on.
Useful to find out the context that the `current` task is running in.

**Return**

work struct if `current` task is a workqueue worker, `NULL` otherwise.

bool current_is_workqueue_rescuer(void)
:   is `current` workqueue rescuer?

**Parameters**

`void`
:   no arguments

**Description**

Determine whether `current` is a workqueue rescuer. Can be used from
work functions to determine whether it's being run off the rescuer task.

**Return**

`true` if `current` is a workqueue rescuer. `false` otherwise.

bool workqueue_congested(int cpu, struct workqueue_struct \*wq)
:   test whether a workqueue is congested

**Parameters**

`int cpu`
:   CPU in question

`struct workqueue_struct *wq`
:   target workqueue

**Description**

Test whether **wq**'s cpu workqueue for **cpu** is congested. There is
no synchronization around this function and the test result is
unreliable and only useful as advisory hints or for debugging.

If **cpu** is WORK_CPU_UNBOUND, the test is performed on the local CPU.

With the exception of ordered workqueues, all workqueues have per-cpu
pool_workqueues, each with its own congested state. A workqueue being
congested on one CPU doesn't mean that the workqueue is contested on any
other CPUs.

**Return**

`true` if congested, `false` otherwise.

unsigned int work_busy(struct work_struct \*work)
:   test whether a work is currently pending or running

**Parameters**

`struct work_struct *work`
:   the work to be tested

**Description**

Test whether **work** is currently pending or running. There is no
synchronization around this function and the test result is
unreliable and only useful as advisory hints or for debugging.

**Return**

OR'd bitmask of WORK_BUSY_\* bits.

void set_worker_desc(const char \*fmt, ...)
:   set description for the current work item

**Parameters**

`const char *fmt`
:   printf-style format string

`...`
:   arguments for the format string

**Description**

This function can be called by a running work function to describe what
the work item is about. If the worker task gets dumped, this
information will be printed out together to help debugging. The
description can be at most WORKER_DESC_LEN including the trailing '0'.

void print_worker_info(const char \*log_lvl, struct task_struct \*task)
:   print out worker information and description

**Parameters**

`const char *log_lvl`
:   the log level to use when printing

`struct task_struct *task`
:   target task

**Description**

If **task** is a worker and currently executing a work item, print out the
name of the workqueue being serviced and worker description set with
[`set_worker_desc()`](workqueue.md#c.set_worker_desc "set_worker_desc") by the currently executing work item.

This function can be safely called on any task as long as the
task_struct itself is accessible. While safe, this function isn't
synchronized and may print out mixups or garbages of limited length.

void show_one_workqueue(struct workqueue_struct \*wq)
:   dump state of specified workqueue

**Parameters**

`struct workqueue_struct *wq`
:   workqueue whose state will be printed

void show_one_worker_pool(struct worker_pool \*pool)
:   dump state of specified worker pool

**Parameters**

`struct worker_pool *pool`
:   worker pool whose state will be printed

void show_all_workqueues(void)
:   dump workqueue state

**Parameters**

`void`
:   no arguments

**Description**

Called from a sysrq handler and prints out all busy workqueues and pools.

void show_freezable_workqueues(void)
:   dump freezable workqueue state

**Parameters**

`void`
:   no arguments

**Description**

Called from try_to_freeze_tasks() and prints out all freezable workqueues
still busy.

void rebind_workers(struct worker_pool \*pool)
:   rebind all workers of a pool to the associated CPU

**Parameters**

`struct worker_pool *pool`
:   pool of interest

**Description**

**pool->cpu** is coming online. Rebind all workers to the CPU.

void restore_unbound_workers_cpumask(struct worker_pool \*pool, int cpu)
:   restore cpumask of unbound workers

**Parameters**

`struct worker_pool *pool`
:   unbound pool of interest

`int cpu`
:   the CPU which is coming up

**Description**

An unbound pool may end up with a cpumask which doesn't have any online
CPUs. When a worker of such pool get scheduled, the scheduler resets
its cpus_allowed. If **cpu** is in **pool**'s cpumask which didn't have any
online CPU before, cpus_allowed of all its workers should be restored.

long work_on_cpu_key(int cpu, long (\*fn)(void\*), void \*arg, struct lock_class_key \*key)
:   run a function in thread context on a particular cpu

**Parameters**

`int cpu`
:   the cpu to run on

`long (*fn)(void *)`
:   the function to run

`void *arg`
:   the function arg

`struct lock_class_key *key`
:   The lock class key for lock debugging purposes

**Description**

It is up to the caller to ensure that the cpu doesn't go offline.
The caller must not hold any locks which would prevent **fn** from completing.

**Return**

The value **fn** returns.

long work_on_cpu_safe_key(int cpu, long (\*fn)(void\*), void \*arg, struct lock_class_key \*key)
:   run a function in thread context on a particular cpu

**Parameters**

`int cpu`
:   the cpu to run on

`long (*fn)(void *)`
:   the function to run

`void *arg`
:   the function argument

`struct lock_class_key *key`
:   The lock class key for lock debugging purposes

**Description**

Disables CPU hotplug and calls work_on_cpu(). The caller must not hold
any locks which would prevent **fn** from completing.

**Return**

The value **fn** returns.

void freeze_workqueues_begin(void)
:   begin freezing workqueues

**Parameters**

`void`
:   no arguments

**Description**

Start freezing workqueues. After this function returns, all freezable
workqueues will queue new works to their inactive_works list instead of
pool->worklist.

**Context**

Grabs and releases wq_pool_mutex, wq->mutex and pool->lock's.

bool freeze_workqueues_busy(void)
:   are freezable workqueues still busy?

**Parameters**

`void`
:   no arguments

**Description**

Check whether freezing is complete. This function must be called
between [`freeze_workqueues_begin()`](workqueue.md#c.freeze_workqueues_begin "freeze_workqueues_begin") and [`thaw_workqueues()`](workqueue.md#c.thaw_workqueues "thaw_workqueues").

**Context**

Grabs and releases wq_pool_mutex.

**Return**

`true` if some freezable workqueues are still busy. `false` if freezing
is complete.

void thaw_workqueues(void)
:   thaw workqueues

**Parameters**

`void`
:   no arguments

**Description**

Thaw workqueues. Normal queueing is restored and all collected
frozen works are transferred to their respective pool worklists.

**Context**

Grabs and releases wq_pool_mutex, wq->mutex and pool->lock's.

int workqueue_unbound_exclude_cpumask(cpumask_var_t exclude_cpumask)
:   Exclude given CPUs from unbound cpumask

**Parameters**

`cpumask_var_t exclude_cpumask`
:   the cpumask to be excluded from wq_unbound_cpumask

**Description**

This function can be called from cpuset code to provide a set of isolated
CPUs that should be excluded from wq_unbound_cpumask. The caller must hold
either cpus_read_lock or cpus_write_lock.

int workqueue_set_unbound_cpumask(cpumask_var_t cpumask)
:   Set the low-level unbound cpumask

**Parameters**

`cpumask_var_t cpumask`
:   the cpumask to set

    The low-level workqueues cpumask is a global cpumask that limits
    the affinity of all unbound workqueues. This function check the **cpumask**
    and apply it to all unbound workqueues and updates all pwqs of them.

**Return**

0 - Success
:   -EINVAL - Invalid **cpumask**
    -ENOMEM - Failed to allocate memory for attrs or pwqs.

int workqueue_sysfs_register(struct workqueue_struct \*wq)
:   make a workqueue visible in sysfs

**Parameters**

`struct workqueue_struct *wq`
:   the workqueue to register

**Description**

Expose **wq** in sysfs under /sys/bus/workqueue/devices.
alloc_workqueue\*() automatically calls this function if WQ_SYSFS is set
which is the preferred method.

Workqueue user should use this function directly iff it wants to apply
workqueue_attrs before making the workqueue visible in sysfs; otherwise,
[`apply_workqueue_attrs()`](workqueue.md#c.apply_workqueue_attrs "apply_workqueue_attrs") may race against userland updating the
attributes.

**Return**

0 on success, -errno on failure.

void workqueue_sysfs_unregister(struct workqueue_struct \*wq)
:   undo [`workqueue_sysfs_register()`](workqueue.md#c.workqueue_sysfs_register "workqueue_sysfs_register")

**Parameters**

`struct workqueue_struct *wq`
:   the workqueue to unregister

**Description**

If **wq** is registered to sysfs by [`workqueue_sysfs_register()`](workqueue.md#c.workqueue_sysfs_register "workqueue_sysfs_register"), unregister.

void workqueue_init_early(void)
:   early init for workqueue subsystem

**Parameters**

`void`
:   no arguments

**Description**

This is the first step of three-staged workqueue subsystem initialization and
invoked as soon as the bare basics - memory allocation, cpumasks and idr are
up. It sets up all the data structures and system workqueues and allows early
boot code to create workqueues and queue/cancel work items. Actual work item
execution starts only after kthreads can be created and scheduled right
before early initcalls.

void workqueue_init(void)
:   bring workqueue subsystem fully online

**Parameters**

`void`
:   no arguments

**Description**

This is the second step of three-staged workqueue subsystem initialization
and invoked as soon as kthreads can be created and scheduled. Workqueues have
been created and work items queued on them, but there are no kworkers
executing the work items yet. Populate the worker pools with the initial
workers and enable future kworker creations.

void workqueue_init_topology(void)
:   initialize CPU pods for unbound workqueues

**Parameters**

`void`
:   no arguments

**Description**

This is the third step of there-staged workqueue subsystem initialization and
invoked after SMP and topology information are fully initialized. It
initializes the unbound CPU pods accordingly.
