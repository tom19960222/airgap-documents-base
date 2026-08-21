---
collection: kernel
version: "6.8"
title: "Set udev rules for PMF Smart PC Builder"
source_url: https://www.kernel.org/doc/html/v6.8/admin-guide/pmf.html
fetched_at: 2026-08-21T03:35:00+00:00
---
# Set udev rules for PMF Smart PC Builder

AMD PMF(Platform Management Framework) Smart PC Solution builder has to set the system states
like S0i3, Screen lock, hibernate etc, based on the output actions provided by the PMF
TA (Trusted Application).

In order for this to work the PMF driver generates a uevent for userspace to react to. Below are
sample udev rules that can facilitate this experience when a machine has PMF Smart PC solution builder
enabled.

Please add the following line(s) to
`/etc/udev/rules.d/99-local.rules`:

```
DRIVERS=="amd-pmf", ACTION=="change", ENV{EVENT_ID}=="0", RUN+="/usr/bin/systemctl suspend"
DRIVERS=="amd-pmf", ACTION=="change", ENV{EVENT_ID}=="1", RUN+="/usr/bin/systemctl hibernate"
DRIVERS=="amd-pmf", ACTION=="change", ENV{EVENT_ID}=="2", RUN+="/bin/loginctl lock-sessions"
```

EVENT_ID values:
0= Put the system to S0i3/S2Idle
1= Put the system to hibernate
2= Lock the screen
