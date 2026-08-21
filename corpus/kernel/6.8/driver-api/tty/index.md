---
collection: kernel
version: "6.8"
title: "TTY"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/tty/index.html
fetched_at: 2026-08-21T03:31:22+00:00
---
# TTY

Teletypewriter (TTY) layer takes care of all those serial devices. Including
the virtual ones like pseudoterminal (PTY).

## TTY structures

There are several major TTY structures. Every TTY device in a system has a
corresponding [`struct tty_port`](tty_port.md#c.tty_port "tty_port"). These devices are maintained by a TTY driver
which is [`struct tty_driver`](tty_driver.md#c.tty_driver "tty_driver"). This structure describes the driver but also
contains a reference to operations which could be performed on the TTYs. It is
[`struct tty_operations`](tty_driver.md#c.tty_operations "tty_operations"). Then, upon open, a [`struct tty_struct`](tty_struct.md#c.tty_struct "tty_struct") is allocated and
lives until the final close. During this time, several callbacks from [`struct
tty_operations`](tty_driver.md#c.tty_operations "tty_operations") are invoked by the TTY layer.

Every character received by the kernel (both from devices and users) is passed
through a preselected [TTY Line Discipline](tty_ldisc.md) (in
short ldisc; in C, [`struct tty_ldisc_ops`](tty_ldisc.md#c.tty_ldisc_ops "tty_ldisc_ops")). Its task is to transform characters
as defined by a particular ldisc or by user too. The default one is n_tty,
implementing echoes, signal handling, jobs control, special characters
processing, and more. The transformed characters are passed further to
user/device, depending on the source.

In-detail description of the named TTY structures is in separate documents:

- [TTY Driver and TTY Operations](tty_driver.md)
  - [Allocation](tty_driver.md#allocation)
  - [Registration](tty_driver.md#registration)
  - [TTY Driver Reference](tty_driver.md#tty-driver-reference)
  - [TTY Operations Reference](tty_driver.md#tty-operations-reference)
- [TTY Port](tty_port.md)
  - [TTY Port Functions](tty_port.md#tty-port-functions)
  - [TTY Port Reference](tty_port.md#tty-port-reference)
  - [TTY Port Operations Reference](tty_port.md#tty-port-operations-reference)
- [TTY Struct](tty_struct.md)
  - [Initialization](tty_struct.md#initialization)
  - [Name](tty_struct.md#name)
  - [Reference counting](tty_struct.md#reference-counting)
  - [Install](tty_struct.md#install)
  - [Read & Write](tty_struct.md#read-write)
  - [Start & Stop](tty_struct.md#start-stop)
  - [Wakeup](tty_struct.md#wakeup)
  - [Hangup](tty_struct.md#hangup)
  - [Misc](tty_struct.md#misc)
  - [TTY Struct Flags](tty_struct.md#tty-struct-flags)
  - [TTY Struct Reference](tty_struct.md#tty-struct-reference)
- [TTY Line Discipline](tty_ldisc.md)
  - [Registration](tty_ldisc.md#registration)
  - [Other Functions](tty_ldisc.md#other-functions)
  - [Line Discipline Operations Reference](tty_ldisc.md#line-discipline-operations-reference)
  - [Driver Access](tty_ldisc.md#driver-access)
  - [TTY Flags](tty_ldisc.md#tty-flags)
  - [Locking](tty_ldisc.md#locking)
  - [Internal Functions](tty_ldisc.md#internal-functions)
- [TTY Buffer](tty_buffer.md)
  - [Flip Buffer Management](tty_buffer.md#flip-buffer-management)
  - [Other Functions](tty_buffer.md#other-functions)
  - [Buffer Locking](tty_buffer.md#buffer-locking)
  - [Internal Functions](tty_buffer.md#internal-functions)
- [TTY IOCTL Helpers](tty_ioctl.md)
- [TTY Internals](tty_internals.md)
  - [Kopen](tty_internals.md#kopen)
  - [Exported Internal Functions](tty_internals.md#exported-internal-functions)
  - [Internal Functions](tty_internals.md#internal-functions)

## Writing TTY Driver

Before one starts writing a TTY driver, they must consider
[Serial](../serial/driver.md) and [USB Serial](../../usb/usb-serial.md)
layers first. Drivers for serial devices can often use one of these specific
layers to implement a serial driver. Only special devices should be handled
directly by the TTY Layer. If you are about to write such a driver, read on.

A *typical* sequence a TTY driver performs is as follows:

1. Allocate and register a TTY driver (module init)
2. Create and register TTY devices as they are probed (probe function)
3. Handle TTY operations and events like interrupts (TTY core invokes the
   former, the device the latter)
4. Remove devices as they are going away (remove function)
5. Unregister and free the TTY driver (module exit)

Steps regarding driver, i.e. 1., 3., and 5. are described in detail in
[TTY Driver and TTY Operations](tty_driver.md). For the other two (devices handling), look into
[TTY Port](tty_port.md).

## Other Documentation

Miscellaneous documentation can be further found in these documents:

- [MOXA Smartio/Industio Family Device Driver Installation Guide](moxa-smartio.md)
  - [1. Introduction](moxa-smartio.md#introduction)
  - [2. System Requirement](moxa-smartio.md#system-requirement)
  - [3. Installation](moxa-smartio.md#installation)
  - [4. Utilities](moxa-smartio.md#utilities)
  - [5. Setserial](moxa-smartio.md#setserial)
  - [6. Troubleshooting](moxa-smartio.md#troubleshooting)
- [GSM 0710 tty multiplexor HOWTO](n_gsm.md)
  - [How to use it](n_gsm.md#how-to-use-it)
- [N_TTY](n_tty.md)
  - [External Functions](n_tty.md#external-functions)
  - [Internal Functions](n_tty.md#internal-functions)
