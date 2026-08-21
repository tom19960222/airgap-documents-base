---
collection: kernel
version: "6.8"
title: "Linux Input Subsystem kernel API"
source_url: https://www.kernel.org/doc/html/v6.8/input/input_kapi.html
fetched_at: 2026-08-21T03:47:13+00:00
---
# Linux Input Subsystem kernel API

Table of Contents

- [1. Creating an input device driver](input-programming.md)
  - [1.1. The simplest example](input-programming.md#the-simplest-example)
  - [1.2. What the example does](input-programming.md#what-the-example-does)
  - [1.3. dev->open() and dev->close()](input-programming.md#dev-open-and-dev-close)
  - [1.4. Inhibiting input devices](input-programming.md#inhibiting-input-devices)
  - [1.5. Basic event types](input-programming.md#basic-event-types)
  - [1.6. BITS_TO_LONGS(), BIT_WORD(), BIT_MASK()](input-programming.md#bits-to-longs-bit-word-bit-mask)
  - [1.7. The id\* and name fields](input-programming.md#the-id-and-name-fields)
  - [1.8. The keycode, keycodemax, keycodesize fields](input-programming.md#the-keycode-keycodemax-keycodesize-fields)
  - [1.9. dev->getkeycode() and dev->setkeycode()](input-programming.md#dev-getkeycode-and-dev-setkeycode)
  - [1.10. Key autorepeat](input-programming.md#key-autorepeat)
  - [1.11. Other event types, handling output events](input-programming.md#other-event-types-handling-output-events)
- [2. Programming gameport drivers](gameport-programming.md)
  - [2.1. A basic classic gameport](gameport-programming.md#a-basic-classic-gameport)
  - [2.2. Memory mapped gameport](gameport-programming.md#memory-mapped-gameport)
  - [2.3. Cooked mode gameport](gameport-programming.md#cooked-mode-gameport)
  - [2.4. More complex gameports](gameport-programming.md#more-complex-gameports)
  - [2.5. Unregistering a gameport](gameport-programming.md#unregistering-a-gameport)
  - [2.6. The gameport structure](gameport-programming.md#the-gameport-structure)
- [3. Keyboard notifier](notifier.md)
