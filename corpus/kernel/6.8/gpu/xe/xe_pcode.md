---
collection: kernel
version: "6.8"
title: "Pcode"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_pcode.html
fetched_at: 2026-08-21T03:41:25+00:00
---
# Pcode

Xe PCODE is the component responsible for interfacing with the PCODE
firmware.
It shall provide a very simple ABI to other Xe components, but be the
single and consolidated place that will communicate with PCODE. All read
and write operations to PCODE will be internal and private to this component.

What's next:
- PCODE hw metrics
- PCODE for display operations

## Internal API

int xe_pcode_request(struct xe_gt \*gt, u32 mbox, u32 request, u32 reply_mask, u32 reply, int timeout_base_ms)
:   send PCODE request until acknowledgment

**Parameters**

`struct xe_gt *gt`
:   gt

`u32 mbox`
:   PCODE mailbox ID the request is targeted for

`u32 request`
:   request ID

`u32 reply_mask`
:   mask used to check for request acknowledgment

`u32 reply`
:   value used to check for request acknowledgment

`int timeout_base_ms`
:   timeout for polling with preemption enabled

**Description**

Keep resending the **request** to **mbox** until PCODE acknowledges it, PCODE
reports an error or an overall timeout of **timeout_base_ms\*\*+50 ms expires.
The request is acknowledged once the PCODE reply dword equals \*\*reply** after
applying **reply_mask**. Polling is first attempted with preemption enabled
for **timeout_base_ms** and if this times out for another 50 ms with
preemption disabled.

Returns 0 on success, `-ETIMEDOUT` in case of a timeout, <0 in case of some
other error as reported by PCODE.

int xe_pcode_init_min_freq_table(struct xe_gt \*gt, u32 min_gt_freq, u32 max_gt_freq)
:   Initialize PCODE's QOS frequency table

**Parameters**

`struct xe_gt *gt`
:   gt instance

`u32 min_gt_freq`
:   Minimal (RPn) GT frequency in units of 50MHz.

`u32 max_gt_freq`
:   Maximal (RP0) GT frequency in units of 50MHz.

**Description**

This function initialize PCODE's QOS frequency table for a proper minimal
frequency/power steering decision, depending on the current requested GT
frequency. For older platforms this was a more complete table including
the IA freq. However for the latest platforms this table become a simple
1-1 Ring vs GT frequency. Even though, without setting it, PCODE might
not take the right decisions for some memory frequencies and affect latency.

It returns 0 on success, and -ERROR number on failure, -EINVAL if max
frequency is higher then the minimal, and other errors directly translated
from the PCODE Error returs:
- -ENXIO: "Illegal Command"
- -ETIMEDOUT: "Timed out"
- -EINVAL: "Illegal Data"
- -ENXIO, "Illegal Subcommand"
- -EBUSY: "PCODE Locked"
- -EOVERFLOW, "GT ratio out of range"
- -EACCES, "PCODE Rejected"
- -EPROTO, "Unknown"

int xe_pcode_init(struct xe_gt \*gt)
:   Ensure PCODE is initialized

**Parameters**

`struct xe_gt *gt`
:   gt instance

**Description**

This function ensures that PCODE is properly initialized. To be called during
probe and resume paths.

It returns 0 on success, and -error number on failure.

int xe_pcode_probe(struct xe_gt \*gt)
:   Prepare xe_pcode and also ensure PCODE is initialized.

**Parameters**

`struct xe_gt *gt`
:   gt instance

**Description**

This function initializes the xe_pcode component, and when needed, it ensures
that PCODE has properly performed its initialization and it is really ready
to go. To be called once only during probe.

It returns 0 on success, and -error number on failure.
