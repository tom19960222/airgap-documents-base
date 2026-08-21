---
collection: kernel
version: "6.8"
title: "TEE (Trusted Execution Environment)"
source_url: https://www.kernel.org/doc/html/v6.8/tee/tee.html
fetched_at: 2026-08-21T03:54:23+00:00
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
