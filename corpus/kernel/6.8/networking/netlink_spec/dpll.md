---
collection: kernel
version: "6.8"
title: "Family dpll netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/dpll.html
fetched_at: 2026-08-21T03:49:14+00:00
---
# [Family `dpll` netlink specification](dpll.md#id8)

Contents

- [Family `dpll` netlink specification](dpll.md#family-dpll-netlink-specification)

  - [Summary](dpll.md#summary)
  - [Operations](dpll.md#operations)

    - [device-id-get](dpll.md#device-id-get)
    - [device-get](dpll.md#device-get)
    - [device-set](dpll.md#device-set)
    - [device-create-ntf](dpll.md#device-create-ntf)
    - [device-delete-ntf](dpll.md#device-delete-ntf)
    - [device-change-ntf](dpll.md#device-change-ntf)
    - [pin-id-get](dpll.md#pin-id-get)
    - [pin-get](dpll.md#pin-get)
    - [pin-set](dpll.md#pin-set)
    - [pin-create-ntf](dpll.md#pin-create-ntf)
    - [pin-delete-ntf](dpll.md#pin-delete-ntf)
    - [pin-change-ntf](dpll.md#pin-change-ntf)
  - [Multicast groups](dpll.md#multicast-groups)
  - [Definitions](dpll.md#definitions)

    - [mode](dpll.md#mode)
    - [lock-status](dpll.md#lock-status)
    - [temp-divider](dpll.md#temp-divider)
    - [type](dpll.md#type)
    - [pin-type](dpll.md#pin-type)
    - [pin-direction](dpll.md#pin-direction)
    - [pin-frequency-1-hz](dpll.md#pin-frequency-1-hz)
    - [pin-frequency-10-khz](dpll.md#pin-frequency-10-khz)
    - [pin-frequency-77_5-khz](dpll.md#pin-frequency-77-5-khz)
    - [pin-frequency-10-mhz](dpll.md#pin-frequency-10-mhz)
    - [pin-state](dpll.md#pin-state)
    - [pin-capabilities](dpll.md#pin-capabilities)
    - [phase-offset-divider](dpll.md#phase-offset-divider)
  - [Attribute sets](dpll.md#attribute-sets)

    - [dpll](dpll.md#dpll)

      - [id (`u32`)](dpll.md#id-u32)
      - [module-name (`string`)](dpll.md#module-name-string)
      - [pad (`pad`)](dpll.md#pad-pad)
      - [clock-id (`u64`)](dpll.md#clock-id-u64)
      - [mode (`u32`)](dpll.md#mode-u32)
      - [mode-supported (`u32`)](dpll.md#mode-supported-u32)
      - [lock-status (`u32`)](dpll.md#lock-status-u32)
      - [temp (`s32`)](dpll.md#temp-s32)
      - [type (`u32`)](dpll.md#type-u32)
    - [pin](dpll.md#pin)

      - [id (`u32`)](dpll.md#id1)
      - [parent-id (`u32`)](dpll.md#parent-id-u32)
      - [module-name (`string`)](dpll.md#id2)
      - [pad (`pad`)](dpll.md#id3)
      - [clock-id (`u64`)](dpll.md#id4)
      - [board-label (`string`)](dpll.md#board-label-string)
      - [panel-label (`string`)](dpll.md#panel-label-string)
      - [package-label (`string`)](dpll.md#package-label-string)
      - [type (`u32`)](dpll.md#id5)
      - [direction (`u32`)](dpll.md#direction-u32)
      - [frequency (`u64`)](dpll.md#frequency-u64)
      - [frequency-supported (`nest`)](dpll.md#frequency-supported-nest)
      - [frequency-min (`u64`)](dpll.md#frequency-min-u64)
      - [frequency-max (`u64`)](dpll.md#frequency-max-u64)
      - [prio (`u32`)](dpll.md#prio-u32)
      - [state (`u32`)](dpll.md#state-u32)
      - [capabilities (`u32`)](dpll.md#capabilities-u32)
      - [parent-device (`nest`)](dpll.md#parent-device-nest)
      - [parent-pin (`nest`)](dpll.md#parent-pin-nest)
      - [phase-adjust-min (`s32`)](dpll.md#phase-adjust-min-s32)
      - [phase-adjust-max (`s32`)](dpll.md#phase-adjust-max-s32)
      - [phase-adjust (`s32`)](dpll.md#phase-adjust-s32)
      - [phase-offset (`s64`)](dpll.md#phase-offset-s64)
      - [fractional-frequency-offset (`sint`)](dpll.md#fractional-frequency-offset-sint)
    - [pin-parent-device](dpll.md#pin-parent-device)

      - [parent-id](dpll.md#parent-id)
      - [direction](dpll.md#direction)
      - [prio](dpll.md#prio)
      - [state](dpll.md#state)
      - [phase-offset](dpll.md#phase-offset)
    - [pin-parent-pin](dpll.md#pin-parent-pin)

      - [parent-id](dpll.md#id6)
      - [state](dpll.md#id7)
    - [frequency-range](dpll.md#frequency-range)

      - [frequency-min](dpll.md#frequency-min)
      - [frequency-max](dpll.md#frequency-max)

## [Summary](dpll.md#id9)

DPLL subsystem.

## [Operations](dpll.md#id10)

### [device-id-get](dpll.md#id11)

Get id of dpll device that matches given attributes

attribute-set
:   dpll

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`module-name`, `clock-id`, `type`]

    **reply**
    :   attributes
        :   [`id`]

### [device-get](dpll.md#id12)

Get list of DPLL devices (dump) or attributes of a single dpll device

attribute-set
:   dpll

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`id`]

    **reply**
    :   attributes
        :   [`id`, `module-name`, `mode`, `mode-supported`, `lock-status`, `temp`, `clock-id`, `type`]

dump
:   **reply**
    :   attributes
        :   [`id`, `module-name`, `mode`, `mode-supported`, `lock-status`, `temp`, `clock-id`, `type`]

### [device-set](dpll.md#id13)

Set attributes for a DPLL device

attribute-set
:   dpll

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`id`]

### [device-create-ntf](dpll.md#id14)

Notification about device appearing

notify
:   device-get

mcgrp
:   monitor

### [device-delete-ntf](dpll.md#id15)

Notification about device disappearing

notify
:   device-get

mcgrp
:   monitor

### [device-change-ntf](dpll.md#id16)

Notification about device configuration being changed

notify
:   device-get

mcgrp
:   monitor

### [pin-id-get](dpll.md#id17)

Get id of a pin that matches given attributes

attribute-set
:   pin

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`module-name`, `clock-id`, `board-label`, `panel-label`, `package-label`, `type`]

    **reply**
    :   attributes
        :   [`id`]

### [pin-get](dpll.md#id18)

Get list of pins and its attributes.- dump request without any attributes given - list all the pins in the system- dump request with target dpll - list all the pins registered with a given dpll device- do request with target dpll and target pin - single pin attributes

attribute-set
:   pin

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`id`]

    **reply**
    :   attributes
        :   [`id`, `board-label`, `panel-label`, `package-label`, `type`, `frequency`, `frequency-supported`, `capabilities`, `parent-device`, `parent-pin`, `phase-adjust-min`, `phase-adjust-max`, `phase-adjust`, `fractional-frequency-offset`]

dump
:   **request**
    :   attributes
        :   [`id`]

    **reply**
    :   attributes
        :   [`id`, `board-label`, `panel-label`, `package-label`, `type`, `frequency`, `frequency-supported`, `capabilities`, `parent-device`, `parent-pin`, `phase-adjust-min`, `phase-adjust-max`, `phase-adjust`, `fractional-frequency-offset`]

### [pin-set](dpll.md#id19)

Set attributes of a target pin

attribute-set
:   pin

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`id`, `frequency`, `direction`, `prio`, `state`, `parent-device`, `parent-pin`, `phase-adjust`]

### [pin-create-ntf](dpll.md#id20)

Notification about pin appearing

notify
:   pin-get

mcgrp
:   monitor

### [pin-delete-ntf](dpll.md#id21)

Notification about pin disappearing

notify
:   pin-get

mcgrp
:   monitor

### [pin-change-ntf](dpll.md#id22)

Notification about pin configuration being changed

notify
:   pin-get

mcgrp
:   monitor

## [Multicast groups](dpll.md#id23)

- monitor

## [Definitions](dpll.md#id24)

### [mode](dpll.md#id25)

type
:   enum

doc
:   working modes a dpll can support, differentiates if and how dpll selectsone of its inputs to syntonize with it, valid values for DPLL_A_MODEattribute

entries
:   manual
    :   input can be only selected by sending a request to dpll

    automatic
    :   highest prio input pin auto selected by dpll

### [lock-status](dpll.md#id26)

type
:   enum

doc
:   provides information of dpll device lock status, valid values forDPLL_A_LOCK_STATUS attribute

entries
:   unlocked
    :   dpll was not yet locked to any valid input (or forced by settingDPLL_A_MODE to DPLL_MODE_DETACHED)

    locked
    :   dpll is locked to a valid signal, but no holdover available

    locked-ho-acq
    :   dpll is locked and holdover acquired

    holdover
    :   dpll is in holdover state - lost a valid lock or was forcedby disconnecting all the pins (latter possible onlywhen dpll lock-state was already DPLL_LOCK_STATUS_LOCKED_HO_ACQ,if dpll lock-state was not DPLL_LOCK_STATUS_LOCKED_HO_ACQ, thedpll's lock-state shall remain DPLL_LOCK_STATUS_UNLOCKED)

### [temp-divider](dpll.md#id27)

type
:   const

value
:   1000

doc
:   temperature divider allowing userspace to calculate thetemperature as float with three digit decimal precision.Value of (DPLL_A_TEMP / DPLL_TEMP_DIVIDER) is integer part oftemperature value.Value of (DPLL_A_TEMP % DPLL_TEMP_DIVIDER) is fractional part oftemperature value.

### [type](dpll.md#id28)

type
:   enum

doc
:   type of dpll, valid values for DPLL_A_TYPE attribute

entries
:   pps
    :   dpll produces Pulse-Per-Second signal

    eec
    :   dpll drives the Ethernet Equipment Clock

### [pin-type](dpll.md#id29)

type
:   enum

doc
:   defines possible types of a pin, valid values for DPLL_A_PIN_TYPEattribute

entries
:   mux
    :   aggregates another layer of selectable pins

    ext
    :   external input

    synce-eth-port
    :   ethernet port PHY's recovered clock

    int-oscillator
    :   device internal oscillator

    gnss
    :   GNSS recovered clock

### [pin-direction](dpll.md#id30)

type
:   enum

doc
:   defines possible direction of a pin, valid values forDPLL_A_PIN_DIRECTION attribute

entries
:   input
    :   pin used as a input of a signal

    output
    :   pin used to output the signal

### [pin-frequency-1-hz](dpll.md#id31)

type
:   const

value
:   1

### [pin-frequency-10-khz](dpll.md#id32)

type
:   const

value
:   10000

### [pin-frequency-77_5-khz](dpll.md#id33)

type
:   const

value
:   77500

### [pin-frequency-10-mhz](dpll.md#id34)

type
:   const

value
:   10000000

### [pin-state](dpll.md#id35)

type
:   enum

doc
:   defines possible states of a pin, valid values forDPLL_A_PIN_STATE attribute

entries
:   connected
    :   pin connected, active input of phase locked loop

    disconnected
    :   pin disconnected, not considered as a valid input

    selectable
    :   pin enabled for automatic input selection

### [pin-capabilities](dpll.md#id36)

type
:   flags

doc
:   defines possible capabilities of a pin, valid flags onDPLL_A_PIN_CAPABILITIES attribute

entries
:   direction-can-change
    :   pin direction can be changed

    priority-can-change
    :   pin priority can be changed

    state-can-change
    :   pin state can be changed

### [phase-offset-divider](dpll.md#id37)

type
:   const

value
:   1000

doc
:   phase offset divider allows userspace to calculate a value ofmeasured signal phase difference between a pin and dpll deviceas a fractional value with three digit decimal precision.Value of (DPLL_A_PHASE_OFFSET / DPLL_PHASE_OFFSET_DIVIDER) is aninteger part of a measured phase offset value.Value of (DPLL_A_PHASE_OFFSET % DPLL_PHASE_OFFSET_DIVIDER) is afractional part of a measured phase offset value.

## [Attribute sets](dpll.md#id38)

### [dpll](dpll.md#id39)

#### [id (`u32`)](dpll.md#id40)

#### [module-name (`string`)](dpll.md#id41)

#### [pad (`pad`)](dpll.md#id42)

#### [clock-id (`u64`)](dpll.md#id43)

#### [mode (`u32`)](dpll.md#id44)

enum
:   mode

#### [mode-supported (`u32`)](dpll.md#id45)

enum
:   mode

multi-attr
:   True

#### [lock-status (`u32`)](dpll.md#id46)

enum
:   lock-status

#### [temp (`s32`)](dpll.md#id47)

#### [type (`u32`)](dpll.md#id48)

enum
:   type

### [pin](dpll.md#id49)

#### [id (`u32`)](dpll.md#id50)

#### [parent-id (`u32`)](dpll.md#id51)

#### [module-name (`string`)](dpll.md#id52)

#### [pad (`pad`)](dpll.md#id53)

#### [clock-id (`u64`)](dpll.md#id54)

#### [board-label (`string`)](dpll.md#id55)

#### [panel-label (`string`)](dpll.md#id56)

#### [package-label (`string`)](dpll.md#id57)

#### [type (`u32`)](dpll.md#id58)

enum
:   pin-type

#### [direction (`u32`)](dpll.md#id59)

enum
:   pin-direction

#### [frequency (`u64`)](dpll.md#id60)

#### [frequency-supported (`nest`)](dpll.md#id61)

multi-attr
:   True

nested-attributes
:   frequency-range

#### [frequency-min (`u64`)](dpll.md#id62)

#### [frequency-max (`u64`)](dpll.md#id63)

#### [prio (`u32`)](dpll.md#id64)

#### [state (`u32`)](dpll.md#id65)

enum
:   pin-state

#### [capabilities (`u32`)](dpll.md#id66)

#### [parent-device (`nest`)](dpll.md#id67)

multi-attr
:   True

nested-attributes
:   pin-parent-device

#### [parent-pin (`nest`)](dpll.md#id68)

multi-attr
:   True

nested-attributes
:   pin-parent-pin

#### [phase-adjust-min (`s32`)](dpll.md#id69)

#### [phase-adjust-max (`s32`)](dpll.md#id70)

#### [phase-adjust (`s32`)](dpll.md#id71)

#### [phase-offset (`s64`)](dpll.md#id72)

#### [fractional-frequency-offset (`sint`)](dpll.md#id73)

doc
:   The FFO (Fractional Frequency Offset) between the RX and TXsymbol rate on the media associated with the pin:(rx_frequency-tx_frequency)/rx_frequencyValue is in PPM (parts per million).This may be implemented for example for pin of typePIN_TYPE_SYNCE_ETH_PORT.

### [pin-parent-device](dpll.md#id74)

#### [parent-id](dpll.md#id75)

#### [direction](dpll.md#id76)

#### [prio](dpll.md#id77)

#### [state](dpll.md#id78)

#### [phase-offset](dpll.md#id79)

### [pin-parent-pin](dpll.md#id80)

#### [parent-id](dpll.md#id81)

#### [state](dpll.md#id82)

### [frequency-range](dpll.md#id83)

#### [frequency-min](dpll.md#id84)

#### [frequency-max](dpll.md#id85)
