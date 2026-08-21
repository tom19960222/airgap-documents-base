---
collection: qemu
version: "11.1.0"
title: "Arm System emulator"
source_url: https://www.qemu.org/docs/master/system/target-arm.html
fetched_at: 2026-08-21T03:23:25+00:00
---
# Arm System emulator

QEMU can emulate both 32-bit and 64-bit Arm CPUs. Use the
`qemu-system-aarch64` executable to simulate a 64-bit Arm machine.
You can use either `qemu-system-arm` or `qemu-system-aarch64`
to simulate a 32-bit Arm machine: in general, command lines that
work for `qemu-system-arm` will behave the same when used with
`qemu-system-aarch64`.

QEMU has generally good support for Arm guests. It has support for
nearly fifty different machines. The reason we support so many is that
Arm hardware is much more widely varying than x86 hardware. Arm CPUs
are generally built into “system-on-chip” (SoC) designs created by
many different companies with different devices, and these SoCs are
then built into machines which can vary still further even if they use
the same SoC. Even with fifty boards QEMU does not cover more than a
small fraction of the Arm hardware ecosystem.

The situation for 64-bit Arm is fairly similar, except that we don’t
implement so many different machines.

As well as the more common “A-profile” CPUs (which have MMUs and will
run Linux) QEMU also supports “M-profile” CPUs such as the Cortex-M0,
Cortex-M4 and Cortex-M33 (which are microcontrollers used in very
embedded boards). For most boards the CPU type is fixed (matching what
the hardware has), so typically you don’t need to specify the CPU type
by hand, except for special cases like the `virt` board.

## Choosing a board model

For QEMU’s Arm system emulation, you must specify which board
model you want to use with the `-M` or `--machine` option;
there is no default.

Because Arm systems differ so much and in fundamental ways, typically
operating system or firmware images intended to run on one machine
will not run at all on any other. This is often surprising for new
users who are used to the x86 world where every system looks like a
standard PC. (Once the kernel has booted, most userspace software
cares much less about the detail of the hardware.)

If you already have a system image or a kernel that works on hardware
and you want to boot with QEMU, check whether QEMU lists that machine
in its `-machine help` output. If it is listed, then you can probably
use that board model. If it is not listed, then unfortunately your image
will almost certainly not boot on QEMU. (You might be able to
extract the filesystem and use that with a different kernel which
boots on a system that QEMU does emulate.)

If you don’t care about reproducing the idiosyncrasies of a particular
bit of hardware, such as small amount of RAM, no PCI or other hard
disk, etc., and just want to run Linux, the best option is to use the
`virt` board. This is a platform which doesn’t correspond to any
real hardware and is designed for use in virtual machines. You’ll
need to compile Linux with a suitable configuration for running on
the `virt` board. `virt` supports PCI, virtio, recent CPUs and
large amounts of RAM. It also supports 64-bit CPUs.

## Board-specific documentation

- [Analog Devices max78000 board (`max78000fthr`)](arm/max78000.md)
- [Arm Integrator/CP (`integratorcp`)](arm/integratorcp.md)
- [Arm MPS2 and MPS3 boards (`mps2-an385`, `mps2-an386`, `mps2-an500`, `mps2-an505`, `mps2-an511`, `mps2-an521`, `mps3-an524`, `mps3-an536`, `mps3-an547`)](arm/mps2.md)
- [Arm Musca boards (`musca-a`, `musca-b1`)](arm/musca.md)
- [Arm Realview boards (`realview-eb`, `realview-eb-mpcore`, `realview-pb-a8`, `realview-pbx-a9`)](arm/realview.md)
- [Arm Server Base System Architecture Reference board (`sbsa-ref`)](arm/sbsa.md)
- [Arm Versatile boards (`versatileab`, `versatilepb`)](arm/versatile.md)
- [Arm Versatile Express boards (`vexpress-a9`, `vexpress-a15`)](arm/vexpress.md)
- [Aspeed family boards (`anacapa-bmc`, `ast2500-evb`, `ast2600-evb`, `bletchley-bmc`, `fuji-bmc`, `gb200nvl-bmc`, `fby35-bmc`, `g220a-bmc`, `palmetto-bmc`, `quanta-q71l-bmc`, `rainier-bmc`, `romulus-bmc`, `supermicrox11-bmc`, `supermicrox11spi-bmc`, `tiogapass-bmc`, `witherspoon-bmc`, `yosemitev2-bmc`)](arm/aspeed.md)
- [Aspeed 2700 family boards (`ast2700-evb`, `ast2700fc`)](arm/aspeed.md#aspeed-2700-family-boards-ast2700-evb-ast2700fc)
- [Aspeed Bridge IC and Platform Root of Trust processor family boards (`ast1030-evb`, `ast1040-evb`, `ast1060-evb`)](arm/aspeed.md#aspeed-bridge-ic-and-platform-root-of-trust-processor-family-boards-ast1030-evb-ast1040-evb-ast1060-evb)
- [Banana Pi BPI-M2U (`bpim2u`)](arm/bananapi_m2u.md)
- [B-L475E-IOT01A IoT Node (`b-l475e-iot01a`)](arm/b-l475e-iot01a.md)
- [Boundary Devices SABRE Lite (`sabrelite`)](arm/sabrelite.md)
- [Canon A1100 (`canon-a1100`)](arm/digic.md)
- [Cubietech Cubieboard (`cubieboard`)](arm/cubieboard.md)
- [Emcraft SmartFusion2 SOM kit (`emcraft-sf2`)](arm/emcraft-sf2.md)
- [Exynos4 boards (`nuri`, `smdkc210`)](arm/exynos.md)
- [Freecom MusicPal (`musicpal`)](arm/musicpal.md)
- [Kyoto Microcomputer KZM-ARM11-01 (`kzm`)](arm/kzm.md)
- [Nordic nRF boards (`microbit`)](arm/nrf.md)
- [Nuvoton iBMC boards (`kudo-bmc`, `mori-bmc`, `npcm750-evb`, `quanta-gbs-bmc`, `quanta-gsj`, `npcm845-evb`)](arm/nuvoton.md)
- [NXP i.MX25 PDK board (`imx25-pdk`)](arm/imx25-pdk.md)
- [NXP MCIMX6UL-EVK (`mcimx6ul-evk`)](arm/mcimx6ul-evk.md)
- [NXP MCIMX7D Sabre (`mcimx7d-sabre`)](arm/mcimx7d-sabre.md)
- [NXP i.MX 8M Plus and i.MX 8M Mini Evaluation Kits (`imx8mp-evk`, `imx8mm-evk`)](arm/imx8m.md)
- [Orange Pi PC (`orangepi-pc`)](arm/orangepi.md)
- [Raspberry Pi boards (`raspi0`, `raspi1ap`, `raspi2b`, `raspi3ap`, `raspi3b`, `raspi4b`)](arm/raspi.md)
- [Sharp Zaurus SL-5500 (`collie`)](arm/collie.md)
- [Siemens SX1 (`sx1`, `sx1-v1`)](arm/sx1.md)
- [Stellaris boards (`lm3s6965evb`, `lm3s811evb`)](arm/stellaris.md)
- [STMicroelectronics STM32 boards (`netduino2`, `netduinoplus2`, `olimex-stm32-h405`, `stm32vldiscovery`)](arm/stm32.md)
- [‘virt’ generic virtual platform (`virt`)](arm/virt.md)
- [VMApple machine emulation](arm/vmapple.md)
- [Xen Device Emulation Backend (`xenpvh`)](arm/xenpvh.md)
- [AMD Versal Virt (`amd-versal-virt`, `amd-versal2-virt`)](arm/xlnx-versal-virt.md)
- [Xilinx Zynq board (`xilinx-zynq-a9`)](arm/xlnx-zynq.md)
- [Xilinx ZynqMP ZCU102 (`xlnx-zcu102`)](arm/xlnx-zcu102.md)

## Emulated CPU architecture support

- [A-profile CPU architecture support](arm/emulation.md)
- [R-profile CPU architecture support](arm/emulation.md#r-profile-cpu-architecture-support)
- [M-profile CPU architecture support](arm/emulation.md#m-profile-cpu-architecture-support)

## Arm CPU features

- [Arm CPU Features](arm/cpu-features.md)
- [CPU Feature Probing](arm/cpu-features.md#cpu-feature-probing)
  - [A note about CPU feature dependencies](arm/cpu-features.md#a-note-about-cpu-feature-dependencies)
  - [A note about CPU models and KVM](arm/cpu-features.md#a-note-about-cpu-models-and-kvm)
- [Using CPU Features](arm/cpu-features.md#using-cpu-features)
- [KVM VCPU Features](arm/cpu-features.md#kvm-vcpu-features)
- [TCG VCPU Features](arm/cpu-features.md#tcg-vcpu-features)
- [SVE CPU Properties](arm/cpu-features.md#sve-cpu-properties)
  - [SVE CPU Property Dependencies and Constraints](arm/cpu-features.md#sve-cpu-property-dependencies-and-constraints)
  - [SVE CPU Property Parsing Semantics](arm/cpu-features.md#sve-cpu-property-parsing-semantics)
  - [SVE CPU Property Examples](arm/cpu-features.md#sve-cpu-property-examples)
  - [SVE CPU Property Recommendations](arm/cpu-features.md#sve-cpu-property-recommendations)
  - [SME CPU Property Examples](arm/cpu-features.md#sme-cpu-property-examples)
  - [SVE User-mode Default Vector Length Property](arm/cpu-features.md#sve-user-mode-default-vector-length-property)
- [SME CPU Properties](arm/cpu-features.md#sme-cpu-properties)
  - [SME User-mode Default Vector Length Property](arm/cpu-features.md#sme-user-mode-default-vector-length-property)
- [RME CPU Properties](arm/cpu-features.md#rme-cpu-properties)
  - [RME Level 0 GPT Size Property](arm/cpu-features.md#rme-level-0-gpt-size-property)
