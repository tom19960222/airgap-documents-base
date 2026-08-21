---
collection: kernel
version: "6.8"
title: "Driver for PCI Endpoint Test Function"
source_url: https://www.kernel.org/doc/html/v6.8/misc-devices/pci-endpoint-test.html
fetched_at: 2026-08-21T03:44:22+00:00
---
# Driver for PCI Endpoint Test Function

This driver should be used as a host side driver if the root complex is
connected to a configurable PCI endpoint running `pci_epf_test` function
driver configured according to [1](pci-endpoint-test.md#id2).

The "pci_endpoint_test" driver can be used to perform the following tests.

The PCI driver for the test device performs the following tests:

> 1. verifying addresses programmed in BAR
> 2. raise legacy IRQ
> 3. raise MSI IRQ
> 4. raise MSI-X IRQ
> 5. read data
> 6. write data
> 7. copy data

This misc driver creates /dev/pci-endpoint-test.<num> for every
`pci_epf_test` function connected to the root complex and "ioctls"
should be used to perform the above tests.

## ioctl

> PCITEST_BAR:
> :   Tests the BAR. The number of the BAR to be tested
>     should be passed as argument.
>
> PCITEST_LEGACY_IRQ:
> :   Tests legacy IRQ
>
> PCITEST_MSI:
> :   Tests message signalled interrupts. The MSI number
>     to be tested should be passed as argument.
>
> PCITEST_MSIX:
> :   Tests message signalled interrupts. The MSI-X number
>     to be tested should be passed as argument.
>
> PCITEST_SET_IRQTYPE:
> :   Changes driver IRQ type configuration. The IRQ type
>     should be passed as argument (0: Legacy, 1:MSI, 2:MSI-X).
>
> PCITEST_GET_IRQTYPE:
> :   Gets driver IRQ type configuration.
>
> PCITEST_WRITE:
> :   Perform write tests. The size of the buffer should be passed
>     as argument.
>
> PCITEST_READ:
> :   Perform read tests. The size of the buffer should be passed
>     as argument.
>
> PCITEST_COPY:
> :   Perform read tests. The size of the buffer should be passed
>     as argument.

[1](pci-endpoint-test.md#id1)
:   [PCI Test Endpoint Function](../PCI/endpoint/function/binding/pci-test.md)
