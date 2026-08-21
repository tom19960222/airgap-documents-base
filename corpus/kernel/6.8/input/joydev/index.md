---
collection: kernel
version: "6.8"
title: "6. Linux Joystick support"
source_url: https://www.kernel.org/doc/html/v6.8/input/joydev/index.html
fetched_at: 2026-08-21T03:47:11+00:00
---
# 6. Linux Joystick support

Copyright
:   © 1996-2000 Vojtech Pavlik <[vojtech@ucw.cz](mailto:vojtech%40ucw.cz)> - Sponsored by SuSE

Table of Contents

- [6.1. Introduction](joystick.md)
- [6.2. Usage](joystick.md#usage)
  - [6.2.1. Utilities](joystick.md#utilities)
  - [6.2.2. Device nodes](joystick.md#device-nodes)
  - [6.2.3. Modules needed](joystick.md#modules-needed)
  - [6.2.4. Verifying that it works](joystick.md#verifying-that-it-works)
  - [6.2.5. Calibration](joystick.md#calibration)
- [6.3. Hardware-specific driver information](joystick.md#hardware-specific-driver-information)
  - [6.3.1. Analog joysticks](joystick.md#analog-joysticks)
  - [6.3.2. Microsoft SideWinder joysticks](joystick.md#microsoft-sidewinder-joysticks)
  - [6.3.3. Logitech ADI devices](joystick.md#logitech-adi-devices)
  - [6.3.4. Gravis GrIP](joystick.md#gravis-grip)
  - [6.3.5. FPGaming A3D and MadCatz A3D](joystick.md#fpgaming-a3d-and-madcatz-a3d)
  - [6.3.6. ThrustMaster DirectConnect (BSP)](joystick.md#thrustmaster-directconnect-bsp)
  - [6.3.7. Creative Labs Blaster](joystick.md#creative-labs-blaster)
  - [6.3.8. Genius Digital joysticks](joystick.md#genius-digital-joysticks)
  - [6.3.9. InterAct Digital joysticks](joystick.md#interact-digital-joysticks)
  - [6.3.10. PDPI Lightning 4 gamecards](joystick.md#pdpi-lightning-4-gamecards)
  - [6.3.11. Trident 4DWave / Aureal Vortex](joystick.md#trident-4dwave-aureal-vortex)
  - [6.3.12. Crystal SoundFusion](joystick.md#crystal-soundfusion)
  - [6.3.13. SoundBlaster Live!](joystick.md#soundblaster-live)
  - [6.3.14. SoundBlaster 64 and 128 - ES1370 and ES1371, ESS Solo1 and S3 SonicVibes](joystick.md#soundblaster-64-and-128-es1370-and-es1371-ess-solo1-and-s3-sonicvibes)
  - [6.3.15. Amiga](joystick.md#amiga)
  - [6.3.16. Game console and 8-bit pads and joysticks](joystick.md#game-console-and-8-bit-pads-and-joysticks)
  - [6.3.17. SpaceTec/LabTec devices](joystick.md#spacetec-labtec-devices)
  - [6.3.18. Logitech SWIFT devices](joystick.md#logitech-swift-devices)
  - [6.3.19. Magellan / Space Mouse](joystick.md#magellan-space-mouse)
  - [6.3.20. I-Force devices](joystick.md#i-force-devices)
  - [6.3.21. Gravis Stinger gamepad](joystick.md#gravis-stinger-gamepad)
- [6.4. Troubleshooting](joystick.md#troubleshooting)
- [6.5. FAQ](joystick.md#faq)
- [6.6. Programming Interface](joystick-api.md)
  - [6.6.1. Introduction](joystick-api.md#introduction)
  - [6.6.2. Initialization](joystick-api.md#initialization)
  - [6.6.3. Event Reading](joystick-api.md#event-reading)
    - [6.6.3.1. js_event.type](joystick-api.md#js-event-type)
    - [6.6.3.2. js_event.number](joystick-api.md#js-event-number)
    - [6.6.3.3. js_event.value](joystick-api.md#js-event-value)
    - [6.6.3.4. js_event.time](joystick-api.md#js-event-time)
  - [6.6.4. Reading](joystick-api.md#reading)
    - [6.6.4.1. O_NONBLOCK](joystick-api.md#o-nonblock)
  - [6.6.5. IOCTLs](joystick-api.md#ioctls)
    - [6.6.5.1. JSIOGCVERSION](joystick-api.md#jsiogcversion)
    - [6.6.5.2. JSIOCGNAME](joystick-api.md#jsiocgname)
    - [6.6.5.3. JSIOC[SG]CORR](joystick-api.md#jsioc-sg-corr)
  - [6.6.6. Backward compatibility](joystick-api.md#backward-compatibility)
  - [6.6.7. Final Notes](joystick-api.md#final-notes)
