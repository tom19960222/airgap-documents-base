---
collection: kernel
version: "6.17"
title: "TEE (Trusted Execution Environment)"
source_url: https://www.kernel.org/doc/html/v6.17/tee/tee.html
fetched_at: 2026-09-16T16:46:43+00:00
---
# TEE (Trusted Execution Environment)

This document describes the TEE subsystem in Linux.

## Overview

A TEE is a trusted OS running in some secure environment, for example,
TrustZone on ARM CPUs, or a separate secure co-processor etc. A TEE driver
handles the details needed to communicate with the TEE.

This subsystem deals with:

- Registration of TEE drivers
- Managing shared memory between Linux and the TEE
- Providing a generic API to the TEE
