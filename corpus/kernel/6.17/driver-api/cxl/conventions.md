---
collection: kernel
version: "6.17"
title: "Compute Express Link: Linux Conventions"
source_url: https://www.kernel.org/doc/html/v6.17/driver-api/cxl/conventions.html
fetched_at: 2026-09-16T16:36:30+00:00
---
# Compute Express Link: Linux Conventions

There exists shipping platforms that bend or break CXL specification
expectations. Record the details and the rationale for those deviations.
Borrow the ACPI Code First template format to capture the assumptions
and tradeoffs such that multiple platform implementations can follow the
same convention.

## <(template) Title>

### Document

CXL Revision <rev>, Version <ver>

### License

SPDX-License Identifier: CC-BY-4.0

### Creator/Contributors

### Summary of the Change

<Detail the conflict with the specification and where available the
assumptions and tradeoffs taken by the hardware platform.>

### Benefits of the Change

<Detail what happens if platforms and Linux do not adopt this
convention.>

### References

### Detailed Description of the Change

<Propose spec language that corrects the conflict.>
