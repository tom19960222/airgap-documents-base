---
collection: python
version: "3.10.21"
title: "Debugging and Profiling"
source_url: https://docs.python.org/3.10/library/debug.html
fetched_at: 2026-09-17T15:14:50+00:00
---
# Debugging and Profiling

These libraries help you with Python development: the debugger enables you to
step through code, analyze stack frames and set breakpoints etc., and the
profilers run code and give you a detailed breakdown of execution times,
allowing you to identify bottlenecks in your programs. Auditing events
provide visibility into runtime behaviors that would otherwise require
intrusive debugging or patching.

- [Audit events table](audit_events.md)
- [`bdb` — Debugger framework](bdb.md)
- [`faulthandler` — Dump the Python traceback](faulthandler.md)
  - [Dumping the traceback](faulthandler.md#dumping-the-traceback)
  - [Fault handler state](faulthandler.md#fault-handler-state)
  - [Dumping the tracebacks after a timeout](faulthandler.md#dumping-the-tracebacks-after-a-timeout)
  - [Dumping the traceback on a user signal](faulthandler.md#dumping-the-traceback-on-a-user-signal)
  - [Issue with file descriptors](faulthandler.md#issue-with-file-descriptors)
  - [Example](faulthandler.md#example)
- [`pdb` — The Python Debugger](pdb.md)
  - [Debugger Commands](pdb.md#debugger-commands)
- [The Python Profilers](profile.md)
  - [Introduction to the profilers](profile.md#introduction-to-the-profilers)
  - [Instant User’s Manual](profile.md#instant-user-s-manual)
  - [`profile` and `cProfile` Module Reference](profile.md#module-cProfile)
  - [The `Stats` Class](profile.md#the-stats-class)
  - [What Is Deterministic Profiling?](profile.md#what-is-deterministic-profiling)
  - [Limitations](profile.md#limitations)
  - [Calibration](profile.md#calibration)
  - [Using a custom timer](profile.md#using-a-custom-timer)
- [`timeit` — Measure execution time of small code snippets](timeit.md)
  - [Basic Examples](timeit.md#basic-examples)
  - [Python Interface](timeit.md#python-interface)
  - [Command-Line Interface](timeit.md#command-line-interface)
  - [Examples](timeit.md#examples)
- [`trace` — Trace or track Python statement execution](trace.md)
  - [Command-Line Usage](trace.md#command-line-usage)
    - [Main options](trace.md#main-options)
    - [Modifiers](trace.md#modifiers)
    - [Filters](trace.md#filters)
  - [Programmatic Interface](trace.md#programmatic-interface)
- [`tracemalloc` — Trace memory allocations](tracemalloc.md)
  - [Examples](tracemalloc.md#examples)
    - [Display the top 10](tracemalloc.md#display-the-top-10)
    - [Compute differences](tracemalloc.md#compute-differences)
    - [Get the traceback of a memory block](tracemalloc.md#get-the-traceback-of-a-memory-block)
    - [Pretty top](tracemalloc.md#pretty-top)
      - [Record the current and peak size of all traced memory blocks](tracemalloc.md#record-the-current-and-peak-size-of-all-traced-memory-blocks)
  - [API](tracemalloc.md#api)
    - [Functions](tracemalloc.md#functions)
    - [DomainFilter](tracemalloc.md#domainfilter)
    - [Filter](tracemalloc.md#filter)
    - [Frame](tracemalloc.md#frame)
    - [Snapshot](tracemalloc.md#snapshot)
    - [Statistic](tracemalloc.md#statistic)
    - [StatisticDiff](tracemalloc.md#statisticdiff)
    - [Trace](tracemalloc.md#trace)
    - [Traceback](tracemalloc.md#traceback)
