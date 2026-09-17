---
collection: kernel
version: "6.17"
title: "Driver implementer’s API guide"
source_url: https://www.kernel.org/doc/html/v6.17/driver-api/index.html
fetched_at: 2026-09-16T16:17:39+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/driver-api/index.md)

# Driver implementer’s API guide

The kernel offers a wide variety of interfaces to support the development
of device drivers. This document is an only somewhat organized collection
of some of those interfaces — it will hopefully get better over time! The
available subsections can be seen below.

## General information for driver authors

This section contains documentation that should, at some point or other, be
of interest to most developers working on device drivers.

- [Driver Basics](basics.md)
- [Driver Model](driver-model/index.md)
- [Device links](device_link.md)
- [Device drivers infrastructure](infrastructure.md)
- [ioctl based interfaces](ioctl.md)
- [CPU and Device Power Management](pm/index.md)

## Useful support libraries

This section contains documentation that should, at some point or other, be
of interest to most developers working on device drivers.

- [Early Userspace](early-userspace/index.md)
- [Kernel Connector](connector.md)
- [Bus-Independent Device Accesses](device-io.md)
- [Device Frequency Scaling](devfreq.md)
- [Buffer Sharing and Synchronization (dma-buf)](dma-buf.md)
- [Component Helper for Aggregate Drivers](component.md)
- [The io_mapping functions](io-mapping.md)
- [Ordering I/O writes to memory-mapped addresses](io_ordering.md)
- [The Userspace I/O HOWTO](uio-howto.md)
- [VFIO Mediated devices](vfio-mediated-device.md)
- [VFIO - “Virtual Function I/O”](vfio.md)
- [Acceptance criteria for vfio-pci device specific driver variants](vfio-pci-device-specific-driver-acceptance.md)

## Bus-level documentation

- [Auxiliary Bus](auxiliary_bus.md)
- [Compute Express Link](cxl/index.md)
- [EISA bus support](eisa.md)
- [Firewire (IEEE 1394) driver Interface Guide](firewire.md)
- [I3C subsystem](i3c/index.md)
- [ISA Drivers](isa.md)
- [MEN Chameleon Bus](men-chameleon-bus.md)
- [The Linux PCI driver implementer’s API guide](pci/index.md)
- [The Linux RapidIO Subsystem](rapidio/index.md)
- [Linux kernel SLIMbus support](slimbus.md)
- [Linux USB API](usb/index.md)
- [Virtio](virtio/index.md)
- [VME Device Drivers](vme.md)
- [W1: Dallas’ 1-wire bus](w1.md)
- [Xillybus driver for generic FPGA interface](xillybus.md)

## Subsystem-specific APIs

- [Linux 802.11 Driver Developer’s Guide](80211/index.md)
- [ACPI Support](acpi/index.md)
- [Kernel driver lp855x](backlight/lp855x-driver.md)
- [The Common Clk Framework](clk.md)
- [Confidential Computing](coco/index.md)
- [Console Drivers](console.md)
- [Crypto Drivers](crypto/index.md)
- [DMAEngine documentation](dmaengine/index.md)
- [The Linux kernel dpll subsystem](dpll.md)
- [Error Detection And Correction (EDAC) Devices](edac.md)
- [Extcon Device Subsystem](extcon.md)
- [Linux Firmware API](firmware/index.md)
- [FPGA Subsystem](fpga/index.md)
- [Frame Buffer Library](frame-buffer.md)
- [Managing Ownership of the Framebuffer Aperture](aperture.md)
- [Generic Counter Interface](generic-counter.md)
- [General Purpose Input/Output (GPIO)](gpio/index.md)
- [High Speed Synchronous Serial Interface (HSI)](hsi.md)
- [The Linux Hardware Timestamping Engine (HTE)](hte/index.md)
- [I2C and SMBus Subsystem](i2c.md)
- [Industrial I/O](iio/index.md)
- [InfiniBand and Remote DMA (RDMA) Interfaces](infiniband.md)
- [Input Subsystem](input.md)
- [Generic System Interconnect Subsystem](interconnect.md)
- [IPMB Driver for a Satellite MC](ipmb.md)
- [The Linux IPMI Driver](ipmi.md)
- [libATA Developer’s Guide](libata.md)
- [The Common Mailbox Framework](mailbox.md)
- [RAID](md/index.md)
- [Media subsystem kernel internal API](media/index.md)
- [Intel(R) Management Engine Interface (Intel(R) MEI)](mei/index.md)
- [Memory Controller drivers](memory-devices/index.md)
- [Message-based devices](message-based.md)
- [Miscellaneous Devices](misc_devices.md)
- [Parallel Port Devices](miscellaneous.md)
- [16x50 UART Driver](miscellaneous.md#x50-uart-driver)
- [Pulse-Width Modulation (PWM)](miscellaneous.md#pulse-width-modulation-pwm)
- [MMC/SD/SDIO card support](mmc/index.md)
- [Memory Technology Device (MTD)](mtd/index.md)
- [MTD NAND Driver Programming Interface](mtdnand.md)
- [Near Field Communication](nfc/index.md)
- [NTB Drivers](ntb.md)
- [Non-Volatile Memory Device (NVDIMM)](nvdimm/index.md)
- [NVMEM Subsystem](nvmem.md)
- [PARPORT interface documentation](parport-lowlevel.md)
- [Generic PHY Framework](phy/index.md)
- [PINCTRL (PIN CONTROL) subsystem](pin-control.md)
- [PLDM Firmware Flash Update Library](pldmfw/index.md)
- [Overview of the `pldmfw` library](pldmfw/index.md#overview-of-the-pldmfw-library)
- [PPS - Pulse Per Second](pps.md)
- [PTP hardware clock infrastructure for Linux](ptp.md)
- [Pulse Width Modulation (PWM) interface](pwm.md)
- [Power Sequencing API](pwrseq.md)
- [Voltage and current regulator API](regulator.md)
- [Reset controller API](reset.md)
- [rfkill - RF kill switch support](rfkill.md)
- [Writing s390 channel device drivers](s390-drivers.md)
- [SCSI Interfaces Guide](scsi.md)
- [Support for Serial devices](serial/index.md)
- [SM501 Driver](sm501.md)
- [SoundWire Documentation](soundwire/index.md)
- [Serial Peripheral Interface (SPI)](spi.md)
- [Surface System Aggregator Module (SSAM)](surface_aggregator/index.md)
- [Linux Switchtec Support](switchtec.md)
- [Sync File API Guide](sync_file.md)
- [target and iSCSI Interfaces Guide](target.md)
- [TEE (Trusted Execution Environment) driver API](tee.md)
- [Thermal](thermal/index.md)
- [TTY](tty/index.md)
- [WBRF - Wifi Band RFI Mitigations](wbrf.md)
- [WMI Driver API](wmi.md)
- [Xilinx FPGA](xilinx/index.md)
- [Writing Device Drivers for Zorro Devices](zorro.md)
