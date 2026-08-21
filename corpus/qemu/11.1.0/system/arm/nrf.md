---
collection: qemu
version: "11.1.0"
title: "Nordic nRF boards ( microbit )"
source_url: https://www.qemu.org/docs/master/system/arm/nrf.html
fetched_at: 2026-08-21T03:24:10+00:00
---
# Nordic nRF boards (`microbit`)

The [Nordic nRF](https://www.nordicsemi.com/Products) chips are a family of Arm-based System-on-Chip that
are designed to be used for low-power and short-range wireless solutions.

The nRF51 series is the first series for short range wireless applications.
It is superseded by the nRF52 series.
The following machines are based on this chip :

- `microbit` BBC micro:bit board with nRF51822 SoC

There are other series such as nRF52, nRF53 and nRF91 which are currently not
supported by QEMU.

## Supported devices

> - Arm Cortex-M0 (ARMv6-M)
> - Serial ports (UART)
> - Clock controller
> - Timers
> - Random Number Generator (RNG)
> - GPIO controller
> - NVMC
> - SWI

## Missing devices

> - Watchdog
> - Real-Time Clock (RTC) controller
> - TWI (i2c)
> - SPI controller
> - Analog to Digital Converter (ADC)
> - Quadrature decoder
> - Radio

## Boot options

The Micro:bit machine can be started using the `-device` option to load a
firmware in [ihex format](https://en.wikipedia.org/wiki/Intel_HEX). Example:

```bash
$ qemu-system-arm -M microbit -device loader,file=test.hex
```
