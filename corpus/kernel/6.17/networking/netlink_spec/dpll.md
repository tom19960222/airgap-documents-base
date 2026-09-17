---
collection: kernel
version: "6.17"
title: "Family dpll netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/dpll.html
fetched_at: 2026-09-16T16:40:45+00:00
---
# [Family `dpll` netlink specification](dpll.md#id9)

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
    - [lock-status-error](dpll.md#lock-status-error)
    - [clock-quality-level](dpll.md#clock-quality-level)
    - [temp-divider](dpll.md#temp-divider)
    - [type](dpll.md#type)
    - [pin-type](dpll.md#pin-type)
    - [pin-direction](dpll.md#pin-direction)
    - [pin-frequency-1-hz](dpll.md#pin-frequency-1-hz)
    - [pin-frequency-10-khz](dpll.md#pin-frequency-10-khz)
    - [pin-frequency-77-5-khz](dpll.md#pin-frequency-77-5-khz)
    - [pin-frequency-10-mhz](dpll.md#pin-frequency-10-mhz)
    - [pin-state](dpll.md#pin-state)
    - [pin-capabilities](dpll.md#pin-capabilities)
    - [phase-offset-divider](dpll.md#phase-offset-divider)
    - [feature-state](dpll.md#feature-state)
  - [Attribute sets](dpll.md#attribute-sets)

    - [dpll](dpll.md#dpll)
    - [pin](dpll.md#pin)
    - [pin-parent-device](dpll.md#pin-parent-device)
    - [pin-parent-pin](dpll.md#pin-parent-pin)
    - [frequency-range](dpll.md#frequency-range)
    - [reference-sync](dpll.md#reference-sync)

## [Summary](dpll.md#id10)

DPLL subsystem.

## [Operations](dpll.md#id11)

### [device-id-get](dpll.md#id12)

Get id of dpll device that matches given attributes

attribute-set:
:   [dpll](dpll.md#dpll-attribute-set-dpll)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-lock-doit

    **post**
    :   dpll-unlock-doit

    **request**
    :   attributes:
        :   [`module-name`, `clock-id`, `type`]

    **reply**
    :   attributes:
        :   [`id`]

### [device-get](dpll.md#id13)

Get list of DPLL devices (dump) or attributes of a single dpll device

attribute-set:
:   [dpll](dpll.md#dpll-attribute-set-dpll)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-pre-doit

    **post**
    :   dpll-post-doit

    **request**
    :   attributes:
        :   [`id`]

    **reply**
    :   attributes:
        :   [`id`, `module-name`, `mode`, `mode-supported`, `lock-status`, `lock-status-error`, `temp`, `clock-id`, `type`, `phase-offset-monitor`]

dump:
:   **reply**
    :   attributes:
        :   [`id`, `module-name`, `mode`, `mode-supported`, `lock-status`, `lock-status-error`, `temp`, `clock-id`, `type`, `phase-offset-monitor`]

### [device-set](dpll.md#id14)

Set attributes for a DPLL device

attribute-set:
:   [dpll](dpll.md#dpll-attribute-set-dpll)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-pre-doit

    **post**
    :   dpll-post-doit

    **request**
    :   attributes:
        :   [`id`, `phase-offset-monitor`]

### [device-create-ntf](dpll.md#id15)

Notification about device appearing

notify:
:   device-get

mcgrp:
:   monitor

### [device-delete-ntf](dpll.md#id16)

Notification about device disappearing

notify:
:   device-get

mcgrp:
:   monitor

### [device-change-ntf](dpll.md#id17)

Notification about device configuration being changed

notify:
:   device-get

mcgrp:
:   monitor

### [pin-id-get](dpll.md#id18)

Get id of a pin that matches given attributes

attribute-set:
:   [pin](dpll.md#dpll-attribute-set-pin)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-lock-doit

    **post**
    :   dpll-unlock-doit

    **request**
    :   attributes:
        :   [`module-name`, `clock-id`, `board-label`, `panel-label`, `package-label`, `type`]

    **reply**
    :   attributes:
        :   [`id`]

### [pin-get](dpll.md#id19)

Get list of pins and its attributes.

- dump request without any attributes given - list all the pins in the
  system
- dump request with target dpll - list all the pins registered with
  a given dpll device
- do request with target dpll and target pin - single pin attributes

attribute-set:
:   [pin](dpll.md#dpll-attribute-set-pin)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-pin-pre-doit

    **post**
    :   dpll-pin-post-doit

    **request**
    :   attributes:
        :   [`id`]

    **reply**
    :   attributes:
        :   [`id`, `board-label`, `panel-label`, `package-label`, `type`, `frequency`, `frequency-supported`, `capabilities`, `parent-device`, `parent-pin`, `phase-adjust-min`, `phase-adjust-max`, `phase-adjust`, `fractional-frequency-offset`, `esync-frequency`, `esync-frequency-supported`, `esync-pulse`, `reference-sync`]

dump:
:   **request**
    :   attributes:
        :   [`id`]

    **reply**
    :   attributes:
        :   [`id`, `board-label`, `panel-label`, `package-label`, `type`, `frequency`, `frequency-supported`, `capabilities`, `parent-device`, `parent-pin`, `phase-adjust-min`, `phase-adjust-max`, `phase-adjust`, `fractional-frequency-offset`, `esync-frequency`, `esync-frequency-supported`, `esync-pulse`, `reference-sync`]

### [pin-set](dpll.md#id20)

Set attributes of a target pin

attribute-set:
:   [pin](dpll.md#dpll-attribute-set-pin)

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   dpll-pin-pre-doit

    **post**
    :   dpll-pin-post-doit

    **request**
    :   attributes:
        :   [`id`, `frequency`, `direction`, `prio`, `state`, `parent-device`, `parent-pin`, `phase-adjust`, `esync-frequency`, `reference-sync`]

### [pin-create-ntf](dpll.md#id21)

Notification about pin appearing

notify:
:   pin-get

mcgrp:
:   monitor

### [pin-delete-ntf](dpll.md#id22)

Notification about pin disappearing

notify:
:   pin-get

mcgrp:
:   monitor

### [pin-change-ntf](dpll.md#id23)

Notification about pin configuration being changed

notify:
:   pin-get

mcgrp:
:   monitor

## [Multicast groups](dpll.md#id24)

- monitor

## [Definitions](dpll.md#id25)

### [mode](dpll.md#id26)

type:
:   enum

doc:
:   working modes a dpll can support, differentiates if and how dpll selects one of its inputs to syntonize with it, valid values for DPLL_A_MODE attribute

entries:
:   manual:
    :   input can be only selected by sending a request to dpll

    automatic:
    :   highest prio input pin auto selected by dpll

### [lock-status](dpll.md#id27)

type:
:   enum

doc:
:   provides information of dpll device lock status, valid values for DPLL_A_LOCK_STATUS attribute

entries:
:   unlocked:
    :   dpll was not yet locked to any valid input (or forced by setting DPLL_A_MODE to DPLL_MODE_DETACHED)

    locked:
    :   dpll is locked to a valid signal, but no holdover available

    locked-ho-acq:
    :   dpll is locked and holdover acquired

    holdover:
    :   dpll is in holdover state - lost a valid lock or was forced by disconnecting all the pins (latter possible only when dpll lock-state was already DPLL_LOCK_STATUS_LOCKED_HO_ACQ, if dpll lock-state was not DPLL_LOCK_STATUS_LOCKED_HO_ACQ, the dpll’s lock-state shall remain DPLL_LOCK_STATUS_UNLOCKED)

### [lock-status-error](dpll.md#id28)

type:
:   enum

doc:
:   if previous status change was done due to a failure, this provides information of dpll device lock status error. Valid values for DPLL_A_LOCK_STATUS_ERROR attribute

entries:
:   none:
    :   dpll device lock status was changed without any error

    undefined:
    :   dpll device lock status was changed due to undefined error. Driver fills this value up in case it is not able to obtain suitable exact error type.

    media-down:
    :   dpll device lock status was changed because of associated media got down. This may happen for example if dpll device was previously locked on an input pin of type PIN_TYPE_SYNCE_ETH_PORT.

    fractional-frequency-offset-too-high:
    :   the FFO (Fractional Frequency Offset) between the RX and TX symbol rate on the media got too high. This may happen for example if dpll device was previously locked on an input pin of type PIN_TYPE_SYNCE_ETH_PORT.

### [clock-quality-level](dpll.md#id29)

type:
:   enum

doc:
:   level of quality of a clock device. This mainly applies when the dpll lock-status is DPLL_LOCK_STATUS_HOLDOVER. The current list is defined according to the table 11-7 contained in ITU-T G.8264/Y.1364 document. One may extend this list freely by other ITU-T defined clock qualities, or different ones defined by another standardization body (for those, please use different prefix).

entries:
:   itu-opt1-prc:

    itu-opt1-ssu-a:

    itu-opt1-ssu-b:

    itu-opt1-eec1:

    itu-opt1-prtc:

    itu-opt1-eprtc:

    itu-opt1-eeec:

    itu-opt1-eprc:

### [temp-divider](dpll.md#id30)

type:
:   const

value:
:   1000

doc:
:   temperature divider allowing userspace to calculate the temperature as float with three digit decimal precision. Value of (DPLL_A_TEMP / DPLL_TEMP_DIVIDER) is integer part of temperature value. Value of (DPLL_A_TEMP % DPLL_TEMP_DIVIDER) is fractional part of temperature value.

### [type](dpll.md#id31)

type:
:   enum

doc:
:   type of dpll, valid values for DPLL_A_TYPE attribute

entries:
:   pps:
    :   dpll produces Pulse-Per-Second signal

    eec:
    :   dpll drives the Ethernet Equipment Clock

### [pin-type](dpll.md#id32)

type:
:   enum

doc:
:   defines possible types of a pin, valid values for DPLL_A_PIN_TYPE attribute

entries:
:   mux:
    :   aggregates another layer of selectable pins

    ext:
    :   external input

    synce-eth-port:
    :   ethernet port PHY’s recovered clock

    int-oscillator:
    :   device internal oscillator

    gnss:
    :   GNSS recovered clock

### [pin-direction](dpll.md#id33)

type:
:   enum

doc:
:   defines possible direction of a pin, valid values for DPLL_A_PIN_DIRECTION attribute

entries:
:   input:
    :   pin used as a input of a signal

    output:
    :   pin used to output the signal

### [pin-frequency-1-hz](dpll.md#id34)

type:
:   const

value:
:   1

### [pin-frequency-10-khz](dpll.md#id35)

type:
:   const

value:
:   10000

### [pin-frequency-77-5-khz](dpll.md#id36)

type:
:   const

value:
:   77500

### [pin-frequency-10-mhz](dpll.md#id37)

type:
:   const

value:
:   10000000

### [pin-state](dpll.md#id38)

type:
:   enum

doc:
:   defines possible states of a pin, valid values for DPLL_A_PIN_STATE attribute

entries:
:   connected:
    :   pin connected, active input of phase locked loop

    disconnected:
    :   pin disconnected, not considered as a valid input

    selectable:
    :   pin enabled for automatic input selection

### [pin-capabilities](dpll.md#id39)

type:
:   flags

doc:
:   defines possible capabilities of a pin, valid flags on DPLL_A_PIN_CAPABILITIES attribute

entries:
:   direction-can-change:
    :   pin direction can be changed

    priority-can-change:
    :   pin priority can be changed

    state-can-change:
    :   pin state can be changed

### [phase-offset-divider](dpll.md#id40)

type:
:   const

value:
:   1000

doc:
:   phase offset divider allows userspace to calculate a value of measured signal phase difference between a pin and dpll device as a fractional value with three digit decimal precision. Value of (DPLL_A_PHASE_OFFSET / DPLL_PHASE_OFFSET_DIVIDER) is an integer part of a measured phase offset value. Value of (DPLL_A_PHASE_OFFSET % DPLL_PHASE_OFFSET_DIVIDER) is a fractional part of a measured phase offset value.

### [feature-state](dpll.md#id41)

type:
:   enum

doc:
:   Allow control (enable/disable) and status checking over features.

entries:
:   disable:
    :   feature shall be disabled

    enable:
    :   feature shall be enabled

## [Attribute sets](dpll.md#id42)

### [dpll](dpll.md#id43)

#### id (`u32`)

#### module-name (`string`)

#### pad (`pad`)

#### clock-id (`u64`)

#### mode (`u32`)

enum:
:   [mode](dpll.md#dpll-definition-mode)

#### mode-supported (`u32`)

enum:
:   [mode](dpll.md#dpll-definition-mode)

multi-attr:
:   True

#### lock-status (`u32`)

enum:
:   [lock-status](dpll.md#dpll-definition-lock-status)

#### temp (`s32`)

#### type (`u32`)

enum:
:   [type](dpll.md#dpll-definition-type)

#### lock-status-error (`u32`)

enum:
:   [lock-status-error](dpll.md#dpll-definition-lock-status-error)

#### clock-quality-level (`u32`)

enum:
:   [clock-quality-level](dpll.md#dpll-definition-clock-quality-level)

multi-attr:
:   True

doc:
:   Level of quality of a clock device. This mainly applies when the dpll lock-status is DPLL_LOCK_STATUS_HOLDOVER. This could be put to message multiple times to indicate possible parallel quality levels (e.g. one specified by ITU option 1 and another one specified by option 2).

#### phase-offset-monitor (`u32`)

enum:
:   [feature-state](dpll.md#dpll-definition-feature-state)

doc:
:   Receive or request state of phase offset monitor feature. If enabled, dpll device shall monitor and notify all currently available inputs for changes of their phase offset against the dpll device.

### [pin](dpll.md#id44)

#### id (`u32`)

#### parent-id (`u32`)

#### module-name (`string`)

#### pad (`pad`)

#### clock-id (`u64`)

#### board-label (`string`)

#### panel-label (`string`)

#### package-label (`string`)

#### type (`u32`)

enum:
:   [pin-type](dpll.md#dpll-definition-pin-type)

#### direction (`u32`)

enum:
:   [pin-direction](dpll.md#dpll-definition-pin-direction)

#### frequency (`u64`)

#### frequency-supported (`nest`)

multi-attr:
:   True

nested-attributes:
:   [frequency-range](dpll.md#dpll-attribute-set-frequency-range)

#### frequency-min (`u64`)

#### frequency-max (`u64`)

#### prio (`u32`)

#### state (`u32`)

enum:
:   [pin-state](dpll.md#dpll-definition-pin-state)

#### capabilities (`u32`)

enum:
:   [pin-capabilities](dpll.md#dpll-definition-pin-capabilities)

#### parent-device (`nest`)

multi-attr:
:   True

nested-attributes:
:   [pin-parent-device](dpll.md#dpll-attribute-set-pin-parent-device)

#### parent-pin (`nest`)

multi-attr:
:   True

nested-attributes:
:   [pin-parent-pin](dpll.md#dpll-attribute-set-pin-parent-pin)

#### phase-adjust-min (`s32`)

#### phase-adjust-max (`s32`)

#### phase-adjust (`s32`)

#### phase-offset (`s64`)

#### fractional-frequency-offset (`sint`)

doc:
:   The FFO (Fractional Frequency Offset) between the RX and TX symbol rate on the media associated with the pin: (rx_frequency-tx_frequency)/rx_frequency Value is in PPM (parts per million). This may be implemented for example for pin of type PIN_TYPE_SYNCE_ETH_PORT.

#### esync-frequency (`u64`)

doc:
:   Frequency of Embedded SYNC signal. If provided, the pin is configured with a SYNC signal embedded into its base clock frequency.

#### esync-frequency-supported (`nest`)

multi-attr:
:   True

nested-attributes:
:   [frequency-range](dpll.md#dpll-attribute-set-frequency-range)

doc:
:   If provided a pin is capable of embedding a SYNC signal (within given range) into its base frequency signal.

#### esync-pulse (`u32`)

doc:
:   A ratio of high to low state of a SYNC signal pulse embedded into base clock frequency. Value is in percents.

#### reference-sync (`nest`)

multi-attr:
:   True

nested-attributes:
:   [reference-sync](dpll.md#dpll-attribute-set-reference-sync)

doc:
:   Capable pin provides list of pins that can be bound to create a reference-sync pin pair.

### [pin-parent-device](dpll.md#id45)

#### parent-id

#### direction

#### prio

#### state

#### phase-offset

### [pin-parent-pin](dpll.md#id46)

#### parent-id

#### state

### [frequency-range](dpll.md#id47)

#### frequency-min

#### frequency-max

### [reference-sync](dpll.md#id48)

#### id

#### state
