---
collection: kernel
version: "6.8"
title: "Hardware vulnerabilities"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/hw-vuln/index.html
fetched_at: 2026-08-21T03:34:29+00:00
---
# Hardware vulnerabilities

This section describes CPU vulnerabilities and provides an overview of the
possible mitigations along with guidance for selecting mitigations if they
are configurable at compile, boot or run time.

- [Spectre Side Channels](spectre.md)
- [L1TF - L1 Terminal Fault](l1tf.md)
- [MDS - Microarchitectural Data Sampling](mds.md)
- [TAA - TSX Asynchronous Abort](tsx_async_abort.md)
- [iTLB multihit](multihit.md)
- [SRBDS - Special Register Buffer Data Sampling](special-register-buffer-data-sampling.md)
- [Core Scheduling](core-scheduling.md)
- [L1D Flushing](l1d_flush.md)
- [Processor MMIO Stale Data Vulnerabilities](processor_mmio_stale_data.md)
- [Cross-Thread Return Address Predictions](cross-thread-rsb.md)
- [Speculative Return Stack Overflow (SRSO)](srso.md)
- [GDS - Gather Data Sampling](gather_data_sampling.md)
