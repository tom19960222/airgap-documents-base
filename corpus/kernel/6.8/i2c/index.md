---
collection: kernel
version: "6.8"
title: "I2C/SMBus Subsystem"
source_url: https://www.kernel.org/doc/html/v6.8/i2c/index.html
fetched_at: 2026-08-21T03:33:03+00:00
---
# I2C/SMBus Subsystem

## Introduction

- [Introduction to I2C and SMBus](summary.md)
- [The I2C Protocol](i2c-protocol.md)
- [The SMBus Protocol](smbus-protocol.md)
- [How to instantiate I2C devices](instantiating-devices.md)
- [I2C Bus Drivers](busses/index.md)
- [I2C muxes and complex topologies](i2c-topology.md)
- [Kernel driver i2c-mux-gpio](muxes/i2c-mux-gpio.md)
- [Linux I2C Sysfs](i2c-sysfs.md)
- [I2C Address Translators](i2c-address-translators.md)

## Writing device drivers

- [Implementing I2C device drivers](writing-clients.md)
- [Implementing I2C device drivers in userspace](dev-interface.md)
- [Linux I2C and DMA](dma-considerations.md)
- [I2C/SMBUS Fault Codes](fault-codes.md)
- [I2C/SMBus Functionality](functionality.md)

## Debugging

- [Linux I2C fault injection](gpio-fault-injection.md)
- [i2c-stub](i2c-stub.md)

## Slave I2C

- [Linux I2C slave interface description](slave-interface.md)
- [Linux I2C slave EEPROM backend](slave-eeprom-backend.md)
- [Linux I2C slave testunit backend](slave-testunit-backend.md)

## Advanced topics

- [I2C Ten-bit Addresses](ten-bit-addresses.md)

## Legacy documentation

- [I2C device driver binding control from user-space in old kernels](old-module-parameters.md)
