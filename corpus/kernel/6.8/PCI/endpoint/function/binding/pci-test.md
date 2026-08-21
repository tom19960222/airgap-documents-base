---
collection: kernel
version: "6.8"
title: "9.10. PCI Test Endpoint Function"
source_url: https://www.kernel.org/doc/html/v6.8/PCI/endpoint/function/binding/pci-test.html
fetched_at: 2026-08-21T03:54:17+00:00
---
# 9.10. PCI Test Endpoint Function

name: Should be "pci_epf_test" to bind to the pci_epf_test driver.

Configurable Fields:

|  |  |
| --- | --- |
| vendorid | should be 0x104c |
| deviceid | should be 0xb500 for DRA74x and 0xb501 for DRA72x |
| revid | don't care |
| progif_code | don't care |
| subclass_code | don't care |
| baseclass_code | should be 0xff |
| cache_line_size | don't care |
| subsys_vendor_id | don't care |
| subsys_id | don't care |
| interrupt_pin | Should be 1 - INTA, 2 - INTB, 3 - INTC, 4 -INTD |
| msi_interrupts | Should be 1 to 32 depending on the number of MSI interrupts to test |
| msix_interrupts | Should be 1 to 2048 depending on the number of MSI-X interrupts to test |
