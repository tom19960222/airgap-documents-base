---
collection: kernel
version: "6.17"
title: "3. SoC Platforms with DTS Compliance Requirements"
source_url: https://www.kernel.org/doc/html/v6.17/process/maintainer-soc-clean-dts.html
fetched_at: 2026-09-16T16:31:26+00:00
---
# 3. SoC Platforms with DTS Compliance Requirements

## 3.1. Overview

SoC platforms or subarchitectures should follow all the rules from
[SoC Subsystem](maintainer-soc.md). This document referenced in
MAINTAINERS impose additional requirements listed below.

## 3.2. Strict DTS DT Schema and dtc Compliance

No changes to the SoC platform Devicetree sources (DTS files) should introduce
new `make dtbs_check W=1` warnings. Warnings in a new board DTS, which are
results of issues in an included DTSI file, are considered existing, not new
warnings. For series split between different trees (DT bindings go via driver
subsystem tree), warnings on linux-next are decisive. The platform maintainers
have automation in place which should point out any new warnings.

If a commit introducing new warnings gets accepted somehow, the resulting
issues shall be fixed in reasonable time (e.g. within one release) or the
commit reverted.
