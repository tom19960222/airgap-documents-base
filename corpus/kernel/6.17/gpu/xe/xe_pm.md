---
collection: kernel
version: "6.17"
title: "Runtime Power Management"
source_url: https://www.kernel.org/doc/html/v6.17/gpu/xe/xe_pm.html
fetched_at: 2026-09-16T16:30:51+00:00
---
# Runtime Power Management

Xe PM implements the main routines for both system level suspend states and
for the opportunistic runtime suspend states.

System Level Suspend (S-States) - In general this is OS initiated suspend
driven by ACPI for achieving S0ix (a.k.a. S2idle, freeze), S3 (suspend to ram),
S4 (disk). The main functions here are xe_pm_suspend and xe_pm_resume. They
are the main point for the suspend to and resume from these states.

PCI Device Suspend (D-States) - This is the opportunistic PCIe device low power
state D3, controlled by the PCI subsystem and ACPI with the help from the
runtime_pm infrastructure.
PCI D3 is special and can mean D3hot, where Vcc power is on for keeping memory
alive and quicker low latency resume or D3Cold where Vcc power is off for
better power savings.
The Vcc control of PCI hierarchy can only be controlled at the PCI root port
level, while the device driver can be behind multiple bridges/switches and
paired with other devices. For this reason, the PCI subsystem cannot perform
the transition towards D3Cold. The lowest runtime PM possible from the PCI
subsystem is D3hot. Then, if all these paired devices in the same root port
are in D3hot, ACPI will assist here and run its own methods (_PR3 and _OFF)
to perform the transition from D3hot to D3cold. Xe may disallow this
transition by calling pci_d3cold_disable(root_pdev) before going to runtime
suspend. It will be based on runtime conditions such as VRAM usage for a
quick and low latency resume for instance.

Runtime PM - This infrastructure provided by the Linux kernel allows the
device drivers to indicate when the can be runtime suspended, so the device
could be put at D3 (if supported), or allow deeper package sleep states
(PC-states), and/or other low level power states. Xe PM component provides
xe_pm_runtime_suspend and xe_pm_runtime_resume functions that PCI
subsystem will call before transition to/from runtime suspend.

Also, Xe PM provides get and put functions that Xe driver will use to
indicate activity. In order to avoid locking complications with the memory
management, whenever possible, these get and put functions needs to be called
from the higher/outer levels.
The main cases that need to be protected from the outer levels are: IOCTL,
sysfs, debugfs, dma-buf sharing, GPU execution.

This component is not responsible for GT idleness (RC6) nor GT frequency
management (RPS).

## Internal API

bool xe_rpm_reclaim_safe(const struct xe_device \*xe)
:   Whether runtime resume can be done from reclaim context

**Parameters**

`const struct xe_device *xe`
:   The xe device.

**Return**

true if it is safe to runtime resume from reclaim context.
false otherwise.

int xe_pm_suspend(struct xe_device \*xe)
:   Helper for System suspend, i.e. S0->S3 / S0->S2idle

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

0 on success

int xe_pm_resume(struct xe_device \*xe)
:   Helper for System resume S3->S0 / S2idle->S0

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

0 on success

int xe_pm_init(struct xe_device \*xe)
:   Initialize Xe Power Management

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

This component is responsible for System and Device sleep states.

Returns 0 for success, negative error code otherwise.

void xe_pm_fini(struct xe_device \*xe)
:   Finalize PM

**Parameters**

`struct xe_device *xe`
:   xe device instance

bool xe_pm_runtime_suspended(struct xe_device \*xe)
:   Check if runtime_pm state is suspended

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

This does not provide any guarantee that the device is going to remain
suspended as it might be racing with the runtime state transitions.
It can be used only as a non-reliable assertion, to ensure that we are not in
the sleep state while trying to access some memory for instance.

Returns true if PCI device is suspended, false otherwise.

int xe_pm_runtime_suspend(struct xe_device \*xe)
:   Prepare our device for D3hot/D3Cold

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

Returns 0 for success, negative error code otherwise.

int xe_pm_runtime_resume(struct xe_device \*xe)
:   Waking up from D3hot/D3Cold

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

Returns 0 for success, negative error code otherwise.

void xe_pm_runtime_get(struct xe_device \*xe)
:   Get a runtime_pm reference and resume synchronously

**Parameters**

`struct xe_device *xe`
:   xe device instance

void xe_pm_runtime_put(struct xe_device \*xe)
:   Put the runtime_pm reference back and mark as idle

**Parameters**

`struct xe_device *xe`
:   xe device instance

int xe_pm_runtime_get_ioctl(struct xe_device \*xe)
:   Get a runtime_pm reference before ioctl

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

Any number greater than or equal to 0 for success, negative error
code otherwise.

bool xe_pm_runtime_get_if_active(struct xe_device \*xe)
:   Get a runtime_pm reference if device active

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

True if device is awake (regardless the previous number of references)
and a new reference was taken, false otherwise.

bool xe_pm_runtime_get_if_in_use(struct xe_device \*xe)
:   Get a new reference if device is active with previous ref taken

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

True if device is awake, a previous reference had been already taken,
and a new reference was now taken, false otherwise.

void xe_pm_runtime_get_noresume(struct xe_device \*xe)
:   Bump runtime PM usage counter without resuming

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

This function should be used in inner places where it is surely already
protected by outer-bound callers of xe_pm_runtime_get.
It will warn if not protected.
The reference should be put back after this function regardless, since it
will always bump the usage counter, regardless.

bool xe_pm_runtime_resume_and_get(struct xe_device \*xe)
:   Resume, then get a runtime_pm ref if awake.

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Return**

True if device is awake and the reference was taken, false otherwise.

void xe_pm_assert_unbounded_bridge(struct xe_device \*xe)
:   Disable PM on unbounded pcie parent bridge

**Parameters**

`struct xe_device *xe`
:   xe device instance

int xe_pm_set_vram_threshold(struct xe_device \*xe, u32 threshold)
:   Set a VRAM threshold for allowing/blocking D3Cold

**Parameters**

`struct xe_device *xe`
:   xe device instance

`u32 threshold`
:   VRAM size in MiB for the D3cold threshold

**Return**

- 0 - success
- `-EINVAL`
  :   - invalid argument

void xe_pm_d3cold_allowed_toggle(struct xe_device \*xe)
:   Check conditions to toggle d3cold.allowed

**Parameters**

`struct xe_device *xe`
:   xe device instance

**Description**

To be called during runtime_pm idle callback.
Check for all the D3Cold conditions ahead of runtime suspend.

int xe_pm_module_init(void)
:   Perform xe_pm specific module initialization.

**Parameters**

`void`
:   no arguments

**Return**

0 on success. Currently doesn’t fail.
