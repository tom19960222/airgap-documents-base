---
collection: kernel
version: "6.17"
title: "Linux Tracing Technologies Guide"
source_url: https://www.kernel.org/doc/html/v6.17/trace/index.html
fetched_at: 2026-09-16T16:17:44+00:00
---
# Linux Tracing Technologies Guide

Tracing in the Linux kernel is a powerful mechanism that allows
developers and system administrators to analyze and debug system
behavior. This guide provides documentation on various tracing
frameworks and tools available in the Linux kernel.

## Introduction to Tracing

This section provides an overview of Linux tracing mechanisms
and debugging approaches.

- [Using the tracer for debugging](debugging.md)
- [Using the Linux Kernel Tracepoints](tracepoints.md)
- [Notes on Analysing Behaviour Using Events and Tracepoints](tracepoint-analysis.md)
- [Tracefs ring-buffer memory mapping](ring-buffer-map.md)

## Core Tracing Frameworks

The following are the primary tracing frameworks integrated into
the Linux kernel.

- [ftrace - Function Tracer](ftrace.md)
- [Function Tracer Design](ftrace-design.md)
- [Using ftrace to hook to functions](ftrace-uses.md)
- [Kernel Probes (Kprobes)](kprobes.md)
- [Kprobe-based Event Tracing](kprobetrace.md)
- [Fprobe-based Event Tracing](fprobetrace.md)
- [Eprobe - Event-based Probe Tracing](eprobetrace.md)
- [Fprobe - Function entry/exit probe](fprobe.md)
- [Lockless Ring Buffer Design](ring-buffer-design.md)

## Event Tracing and Analysis

A detailed explanation of event tracing mechanisms and their
applications.

- [Event Tracing](events.md)
- [Subsystem Trace Points: kmem](events-kmem.md)
- [Subsystem Trace Points: power](events-power.md)
- [NMI Trace Events](events-nmi.md)
- [MSR Trace Events](events-msr.md)
- [Boot-time tracing](boottime-trace.md)
- [Event Histograms](histogram.md)
- [Histogram Design Notes](histogram-design.md)

## Hardware and Performance Tracing

This section covers tracing features that monitor hardware
interactions and system performance.

- [Intel(R) Trace Hub (TH)](intel_th.md)
- [System Trace Module](stm.md)
- [MIPI SyS-T over STP](sys-t.md)
- [CoreSight - ARM Hardware Trace](coresight/index.md)
- [Runtime Verification](rv/index.md)
- [HiSilicon PCIe Tune and Trace device](hisi-ptt.md)
- [In-kernel memory-mapped I/O tracing](mmiotrace.md)
- [Hardware Latency Detector](hwlat_detector.md)
- [OSNOISE Tracer](osnoise-tracer.md)
- [Timerlat tracer](timerlat-tracer.md)

## User-Space Tracing

These tools allow tracing user-space applications and
interactions.

- [user_events: User-based Event Tracing](user_events.md)
- [Uprobe-tracer: Uprobe-based Event Tracing](uprobetracer.md)

## Additional Resources

For more details, refer to the respective documentation of each
tracing tool and framework.
