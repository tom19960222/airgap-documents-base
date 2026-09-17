---
collection: kernel
version: "6.17"
title: "9.10. PCI NVMe Function"
source_url: https://www.kernel.org/doc/html/v6.17/PCI/endpoint/pci-nvme-function.html
fetched_at: 2026-09-16T16:46:30+00:00
---
# 9.10. PCI NVMe Function

Author:
:   Damien Le Moal <[dlemoal@kernel.org](mailto:dlemoal%40kernel.org)>

The PCI NVMe endpoint function implements a PCI NVMe controller using the NVMe
subsystem target core code. The driver for this function resides with the NVMe
subsystem as drivers/nvme/target/pci-epf.c.

See [NVMe PCI Endpoint Function Target](../../nvme/nvme-pci-endpoint-target.md) for more details.
