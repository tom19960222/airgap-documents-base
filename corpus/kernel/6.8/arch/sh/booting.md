---
collection: kernel
version: "6.8"
title: "DeviceTree Booting"
source_url: https://www.kernel.org/doc/html/v6.8/arch/sh/booting.html
fetched_at: 2026-08-21T03:36:59+00:00
---
# DeviceTree Booting

> Device-tree compatible SH bootloaders are expected to provide the physical
> address of the device tree blob in r4. Since legacy bootloaders did not
> guarantee any particular initial register state, kernels built to
> inter-operate with old bootloaders must either use a builtin DTB or
> select a legacy board option (something other than CONFIG_SH_DEVICE_TREE)
> that does not use device tree. Support for the latter is being phased out
> in favor of device tree.
