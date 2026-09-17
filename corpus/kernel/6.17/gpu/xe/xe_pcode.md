---
collection: kernel
version: "6.17"
title: "Pcode"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_pcode.html
fetched_at: 2026-09-16T16:30:50+00:00
---
# Pcode

Xe PCODE is the component responsible for interfacing with the PCODE
firmware.
It shall provide a very simple ABI to other Xe components, but be the
single and consolidated place that will communicate with PCODE. All read
and write operations to PCODE will be internal and private to this component.

What’s next:
- PCODE hw metrics
- PCODE for display operations

## Internal API

int xe_pcode_request(struct xe_tile \*tile, u32 mbox, u32 request, u32 reply_mask, u32 reply, int timeout_base_ms)
:   send PCODE request until acknowledgment

**Parameters**

`struct xe_tile *tile`
:   tile

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

int xe_pcode_init_min_freq_table(struct xe_tile \*tile, u32 min_gt_freq, u32 max_gt_freq)
:   Initialize PCODE’s QOS frequency table

**Parameters**

`struct xe_tile *tile`
:   tile instance

`u32 min_gt_freq`
:   Minimal (RPn) GT frequency in units of 50MHz.

`u32 max_gt_freq`
:   Maximal (RP0) GT frequency in units of 50MHz.

**Description**

This function initialize PCODE’s QOS frequency table for a proper minimal
frequency/power steering decision, depending on the current requested GT
frequency. For older platforms this was a more complete table including
the IA freq. However for the latest platforms this table become a simple
1-1 Ring vs GT frequency. Even though, without setting it, PCODE might
not take the right decisions for some memory frequencies and affect latency.

It returns 0 on success, and -ERROR number on failure, -EINVAL if max
frequency is higher then the minimal, and other errors directly translated
from the PCODE Error returns:
- -ENXIO: “Illegal Command”
- -ETIMEDOUT: “Timed out”
- -EINVAL: “Illegal Data”
- -ENXIO, “Illegal Subcommand”
- -EBUSY: “PCODE Locked”
- -EOVERFLOW, “GT ratio out of range”
- -EACCES, “PCODE Rejected”
- -EPROTO, “Unknown”

int xe_pcode_ready(struct xe_device \*xe, bool locked)
:   Ensure PCODE is initialized

**Parameters**

`struct xe_device *xe`
:   xe instance

`bool locked`
:   true if lock held, false otherwise

**Description**

PCODE init mailbox is polled only on root gt of root tile
as the root tile provides the initialization is complete only
after all the tiles have completed the initialization.
Called only on early probe without locks and with locks in
resume path.

Returns 0 on success, and -error number on failure.

void xe_pcode_init(struct xe_tile \*tile)
:   initialize components of PCODE

**Parameters**

`struct xe_tile *tile`
:   tile instance

**Description**

This function initializes the xe_pcode component.
To be called once only during probe.

int xe_pcode_probe_early(struct xe_device \*xe)
:   initializes PCODE

**Parameters**

`struct xe_device *xe`
:   xe instance

**Description**

This function checks the initialization status of PCODE
To be called once only during early probe without locks.

Returns 0 on success, error code otherwise

# Boot Survivability

Boot Survivability is a software based workflow for recovering a system in a failed boot state
Here system recoverability is concerned with recovering the firmware responsible for boot.

This is implemented by loading the driver with bare minimum (no drm card) to allow the firmware
to be flashed through mei and collect telemetry. The driver’s probe flow is modified
such that it enters survivability mode when pcode initialization is incomplete and boot status
denotes a failure.

Survivability mode can also be entered manually using the survivability mode attribute available
through configfs which is beneficial in several usecases. It can be used to address scenarios
where pcode does not detect failure or for validation purposes. It can also be used in
In-Field-Repair (IFR) to repair a single card without impacting the other cards in a node.

Use below command enable survivability mode manually:

```
# echo 1 > /sys/kernel/config/xe/0000:03:00.0/survivability_mode
```

It is the responsibility of the user to clear the mode once firmware flash is complete.

Refer [Xe Configfs](xe_configfs.md#xe-configfs) for more details on how to use configfs

Survivability mode is indicated by the below admin-only readable sysfs which provides additional
debug information:

```
/sys/bus/pci/devices/<device>/surivability_mode
```

Capability Information:
:   Provides boot status

Postcode Information:
:   Provides information about the failure

Overflow Information
:   Provides history of previous failures

Auxiliary Information
:   Certain failures may have information in addition to postcode information
