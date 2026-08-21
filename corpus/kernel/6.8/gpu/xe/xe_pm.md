---
collection: kernel
version: "6.8"
title: "Runtime Power Management"
source_url: https://www.kernel.org/doc/html/v6.8/gpu/xe/xe_pm.html
fetched_at: 2026-08-21T03:41:25+00:00
---
# Runtime Power Management

Xe PM shall be guided by the simplicity.
Use the simplest hook options whenever possible.
Let's not reinvent the runtime_pm references and hooks.
Shall have a clear separation of display and gt underneath this component.

What's next:

For now s2idle and s3 are only working in integrated devices. The next step
is to iterate through all VRAM's BO backing them up into the system memory
before allowing the system suspend.

Also runtime_pm needs to be here from the beginning.

RC6/RPS are also critical PM features. Let's start with GuCRC and GuC SLPC
and no wait boost. Frequency optimizations should come on a next stage.

## Internal API

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
