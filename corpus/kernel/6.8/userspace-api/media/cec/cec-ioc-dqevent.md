---
collection: kernel
version: "6.8"
title: "2.9. ioctl CEC_DQEVENT"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-ioc-dqevent.html
fetched_at: 2026-08-21T03:38:48+00:00
---
# 2.9. ioctl CEC_DQEVENT

## 2.9.1. Name

CEC_DQEVENT - Dequeue a CEC event

## 2.9.2. Synopsis

CEC_DQEVENT

`int ioctl(int fd, CEC_DQEVENT, struct cec_event *argp)`

## 2.9.3. Arguments

`fd`
:   File descriptor returned by [`open()`](cec-func-open.md#c.CEC.open "open").

`argp`

## 2.9.4. Description

CEC devices can send asynchronous events. These can be retrieved by
calling [`CEC_DQEVENT()`](cec-ioc-dqevent.md#c.CEC.CEC_DQEVENT "CEC_DQEVENT"). If the file descriptor is in
non-blocking mode and no event is pending, then it will return -1 and
set errno to the `EAGAIN` error code.

The internal event queues are per-filehandle and per-event type. If
there is no more room in a queue then the last event is overwritten with
the new one. This means that intermediate results can be thrown away but
that the latest event is always available. This also means that is it
possible to read two successive events that have the same value (e.g.
two [CEC_EVENT_STATE_CHANGE](cec-ioc-dqevent.md#cec-event-state-change) events with
the same state). In that case the intermediate state changes were lost but
it is guaranteed that the state did change in between the two events.

type cec_event_state_change

struct cec_event_state_change

|  |  |  |
| --- | --- | --- |
| __u16 | `phys_addr` | The current physical address. This is `CEC_PHYS_ADDR_INVALID` if no valid physical address is set. |
| __u16 | `log_addr_mask` | The current set of claimed logical addresses. This is 0 if no logical addresses are claimed or if `phys_addr` is `CEC_PHYS_ADDR_INVALID`. If bit 15 is set (`1 << CEC_LOG_ADDR_UNREGISTERED`) then this device has the unregistered logical address. In that case all other bits are 0. |
| __u16 | `have_conn_info` | If non-zero, then HDMI connector information is available. This field is only valid if `CEC_CAP_CONNECTOR_INFO` is set. If that capability is set and `have_conn_info` is zero, then that indicates that the HDMI connector device is not instantiated, either because the HDMI driver is still configuring the device or because the HDMI device was unbound. |

type cec_event_lost_msgs

struct cec_event_lost_msgs

|  |  |  |
| --- | --- | --- |
| __u32 | `lost_msgs` | Set to the number of lost messages since the filehandle was opened or since the last time this event was dequeued for this filehandle. The messages lost are the oldest messages. So when a new message arrives and there is no more room, then the oldest message is discarded to make room for the new one. The internal size of the message queue guarantees that all messages received in the last two seconds will be stored. Since messages should be replied to within a second according to the CEC specification, this is more than enough. |

type cec_event

struct cec_event

|  |  |  |
| --- | --- | --- |
| __u64 | `ts` | Timestamp of the event in ns.  The timestamp has been taken from the `CLOCK_MONOTONIC` clock.  To access the same clock from userspace use `clock_gettime()`. |
| __u32 | `event` | The CEC event type, see [CEC Events Types](cec-ioc-dqevent.md#cec-events). |
| __u32 | `flags` | Event flags, see [CEC Event Flags](cec-ioc-dqevent.md#cec-event-flags). |
| union { | (anonymous) | |
| [`struct cec_event_state_change`](cec-ioc-dqevent.md#c.CEC.cec_event_state_change "CEC.cec_event_state_change") | `state_change` | The new adapter state as sent by the [CEC_EVENT_STATE_CHANGE](cec-ioc-dqevent.md#cec-event-state-change) event. |
| [`struct cec_event_lost_msgs`](cec-ioc-dqevent.md#c.CEC.cec_event_lost_msgs "CEC.cec_event_lost_msgs") | `lost_msgs` | The number of lost messages as sent by the [CEC_EVENT_LOST_MSGS](cec-ioc-dqevent.md#cec-event-lost-msgs) event. |
| } |  | |

CEC Events Types

|  |  |  |
| --- | --- | --- |
| `CEC_EVENT_STATE_CHANGE` | 1 | Generated when the CEC Adapter's state changes. When [`open()`](cec-func-open.md#c.CEC.open "CEC.open") is called an initial event will be generated for that filehandle with the CEC Adapter's state at that time. |
| `CEC_EVENT_LOST_MSGS` | 2 | Generated if one or more CEC messages were lost because the application didn't dequeue CEC messages fast enough. |
| `CEC_EVENT_PIN_CEC_LOW` | 3 | Generated if the CEC pin goes from a high voltage to a low voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. |
| `CEC_EVENT_PIN_CEC_HIGH` | 4 | Generated if the CEC pin goes from a low voltage to a high voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. |
| `CEC_EVENT_PIN_HPD_LOW` | 5 | Generated if the HPD pin goes from a high voltage to a low voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. When [`open()`](cec-func-open.md#c.CEC.open "CEC.open") is called, the HPD pin can be read and if the HPD is low, then an initial event will be generated for that filehandle. |
| `CEC_EVENT_PIN_HPD_HIGH` | 6 | Generated if the HPD pin goes from a low voltage to a high voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. When [`open()`](cec-func-open.md#c.CEC.open "CEC.open") is called, the HPD pin can be read and if the HPD is high, then an initial event will be generated for that filehandle. |
| `CEC_EVENT_PIN_5V_LOW` | 6 | Generated if the 5V pin goes from a high voltage to a low voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. When [`open()`](cec-func-open.md#c.CEC.open "CEC.open") is called, the 5V pin can be read and if the 5V is low, then an initial event will be generated for that filehandle. |
| `CEC_EVENT_PIN_5V_HIGH` | 7 | Generated if the 5V pin goes from a low voltage to a high voltage. Only applies to adapters that have the `CEC_CAP_MONITOR_PIN` capability set. When [`open()`](cec-func-open.md#c.CEC.open "CEC.open") is called, the 5V pin can be read and if the 5V is high, then an initial event will be generated for that filehandle. |

CEC Event Flags

|  |  |  |
| --- | --- | --- |
| `CEC_EVENT_FL_INITIAL_STATE` | 1 | Set for the initial events that are generated when the device is opened. See the table above for which events do this. This allows applications to learn the initial state of the CEC adapter at [`open()`](cec-func-open.md#c.CEC.open "CEC.open") time. |
| `CEC_EVENT_FL_DROPPED_EVENTS` | 2 | Set if one or more events of the given event type have been dropped. This is an indication that the application cannot keep up. |

## 2.9.5. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

The [ioctl CEC_DQEVENT](cec-ioc-dqevent.md#cec-dqevent) can return the following
error codes:

EAGAIN
:   This is returned when the filehandle is in non-blocking mode and there
    are no pending events.

ERESTARTSYS
:   An interrupt (e.g. Ctrl-C) arrived while in blocking mode waiting for
    events to arrive.
