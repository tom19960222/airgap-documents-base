---
collection: kernel
version: "6.8"
title: "What is an IRQ?"
source_url: https://www.kernel.org/doc/html/v6.8/core-api/irq/concepts.html
fetched_at: 2026-08-21T03:45:41+00:00
---
English

- [Chinese (Simplified)](../../translations/zh_CN/core-api/irq/concepts.md)

# What is an IRQ?

An IRQ is an interrupt request from a device.
Currently they can come in over a pin, or over a packet.
Several devices may be connected to the same pin thus
sharing an IRQ.

An IRQ number is a kernel identifier used to talk about a hardware
interrupt source. Typically this is an index into the global irq_desc
array, but except for what linux/interrupt.h implements the details
are architecture specific.

An IRQ number is an enumeration of the possible interrupt sources on a
machine. Typically what is enumerated is the number of input pins on
all of the interrupt controller in the system. In the case of ISA
what is enumerated are the 16 input pins on the two i8259 interrupt
controllers.

Architectures can assign additional meaning to the IRQ numbers, and
are encouraged to in the case where there is any manual configuration
of the hardware involved. The ISA IRQs are a classic example of
assigning this kind of additional meaning.
