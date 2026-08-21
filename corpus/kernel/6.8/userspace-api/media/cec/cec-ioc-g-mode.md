---
collection: kernel
version: "6.8"
title: "2.10. ioctls CEC_G_MODE and CEC_S_MODE"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-ioc-g-mode.html
fetched_at: 2026-08-21T03:38:49+00:00
---
# 2.10. ioctls CEC_G_MODE and CEC_S_MODE

CEC_G_MODE, CEC_S_MODE - Get or set exclusive use of the CEC adapter

## 2.10.1. Synopsis

CEC_G_MODE

`int ioctl(int fd, CEC_G_MODE, __u32 *argp)`

CEC_S_MODE

`int ioctl(int fd, CEC_S_MODE, __u32 *argp)`

## 2.10.2. Arguments

`fd`
:   File descriptor returned by [`open()`](cec-func-open.md#c.CEC.open "open").

`argp`
:   Pointer to CEC mode.

## 2.10.3. Description

By default any filehandle can use [ioctls CEC_RECEIVE and CEC_TRANSMIT](cec-ioc-receive.md#cec-transmit), but in order to prevent
applications from stepping on each others toes it must be possible to
obtain exclusive access to the CEC adapter. This ioctl sets the
filehandle to initiator and/or follower mode which can be exclusive
depending on the chosen mode. The initiator is the filehandle that is
used to initiate messages, i.e. it commands other CEC devices. The
follower is the filehandle that receives messages sent to the CEC
adapter and processes them. The same filehandle can be both initiator
and follower, or this role can be taken by two different filehandles.

When a CEC message is received, then the CEC framework will decide how
it will be processed. If the message is a reply to an earlier
transmitted message, then the reply is sent back to the filehandle that
is waiting for it. In addition the CEC framework will process it.

If the message is not a reply, then the CEC framework will process it
first. If there is no follower, then the message is just discarded and a
feature abort is sent back to the initiator if the framework couldn't
process it. If there is a follower, then the message is passed on to the
follower who will use [ioctl CEC_RECEIVE](cec-ioc-receive.md#cec-receive) to dequeue
the new message. The framework expects the follower to make the right
decisions.

The CEC framework will process core messages unless requested otherwise
by the follower. The follower can enable the passthrough mode. In that
case, the CEC framework will pass on most core messages without
processing them and the follower will have to implement those messages.
There are some messages that the core will always process, regardless of
the passthrough mode. See [Core Message Processing](cec-ioc-g-mode.md#cec-core-processing) for details.

If there is no initiator, then any CEC filehandle can use
[ioctl CEC_TRANSMIT](cec-ioc-receive.md#cec-transmit). If there is an exclusive
initiator then only that initiator can call
[ioctls CEC_RECEIVE and CEC_TRANSMIT](cec-ioc-receive.md#cec-transmit). The follower can of course
always call [ioctl CEC_TRANSMIT](cec-ioc-receive.md#cec-transmit).

Available initiator modes are:

Initiator Modes

|  |  |  |
| --- | --- | --- |
| `CEC_MODE_NO_INITIATOR` | 0x0 | This is not an initiator, i.e. it cannot transmit CEC messages or make any other changes to the CEC adapter. |
| `CEC_MODE_INITIATOR` | 0x1 | This is an initiator (the default when the device is opened) and it can transmit CEC messages and make changes to the CEC adapter, unless there is an exclusive initiator. |
| `CEC_MODE_EXCL_INITIATOR` | 0x2 | This is an exclusive initiator and this file descriptor is the only one that can transmit CEC messages and make changes to the CEC adapter. If someone else is already the exclusive initiator then an attempt to become one will return the `EBUSY` error code error. |

Available follower modes are:

Follower Modes

|  |  |  |
| --- | --- | --- |
| `CEC_MODE_NO_FOLLOWER` | 0x00 | This is not a follower (the default when the device is opened). |
| `CEC_MODE_FOLLOWER` | 0x10 | This is a follower and it will receive CEC messages unless there is an exclusive follower. You cannot become a follower if [CEC_CAP_TRANSMIT](cec-ioc-adap-g-caps.md#cec-cap-transmit) is not set or if [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator) was specified, the `EINVAL` error code is returned in that case. |
| `CEC_MODE_EXCL_FOLLOWER` | 0x20 | This is an exclusive follower and only this file descriptor will receive CEC messages for processing. If someone else is already the exclusive follower then an attempt to become one will return the `EBUSY` error code. You cannot become a follower if [CEC_CAP_TRANSMIT](cec-ioc-adap-g-caps.md#cec-cap-transmit) is not set or if [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator) was specified, the `EINVAL` error code is returned in that case. |
| `CEC_MODE_EXCL_FOLLOWER_PASSTHRU` | 0x30 | This is an exclusive follower and only this file descriptor will receive CEC messages for processing. In addition it will put the CEC device into passthrough mode, allowing the exclusive follower to handle most core messages instead of relying on the CEC framework for that. If someone else is already the exclusive follower then an attempt to become one will return the `EBUSY` error code. You cannot become a follower if [CEC_CAP_TRANSMIT](cec-ioc-adap-g-caps.md#cec-cap-transmit) is not set or if [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator) was specified, the `EINVAL` error code is returned in that case. |
| `CEC_MODE_MONITOR_PIN` | 0xd0 | Put the file descriptor into pin monitoring mode. Can only be used in combination with [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator), otherwise the `EINVAL` error code will be returned. This mode requires that the [CEC_CAP_MONITOR_PIN](cec-ioc-adap-g-caps.md#cec-cap-monitor-pin) capability is set, otherwise the `EINVAL` error code is returned. While in pin monitoring mode this file descriptor can receive the `CEC_EVENT_PIN_CEC_LOW` and `CEC_EVENT_PIN_CEC_HIGH` events to see the low-level CEC pin transitions. This is very useful for debugging. This mode is only allowed if the process has the `CAP_NET_ADMIN` capability. If that is not set, then the `EPERM` error code is returned. |
| `CEC_MODE_MONITOR` | 0xe0 | Put the file descriptor into monitor mode. Can only be used in combination with [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator), otherwise the `EINVAL` error code will be returned. In monitor mode all messages this CEC device transmits and all messages it receives (both broadcast messages and directed messages for one its logical addresses) will be reported. This is very useful for debugging. This is only allowed if the process has the `CAP_NET_ADMIN` capability. If that is not set, then the `EPERM` error code is returned. |
| `CEC_MODE_MONITOR_ALL` | 0xf0 | Put the file descriptor into 'monitor all' mode. Can only be used in combination with [CEC_MODE_NO_INITIATOR](cec-ioc-g-mode.md#cec-mode-no-initiator), otherwise the `EINVAL` error code will be returned. In 'monitor all' mode all messages this CEC device transmits and all messages it receives, including directed messages for other CEC devices, will be reported. This is very useful for debugging, but not all devices support this. This mode requires that the [CEC_CAP_MONITOR_ALL](cec-ioc-adap-g-caps.md#cec-cap-monitor-all) capability is set, otherwise the `EINVAL` error code is returned. This is only allowed if the process has the `CAP_NET_ADMIN` capability. If that is not set, then the `EPERM` error code is returned. |

Core message processing details:

Core Message Processing

|  |  |
| --- | --- |
| `CEC_MSG_GET_CEC_VERSION` | The core will return the CEC version that was set with [ioctl CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md#cec-adap-s-log-addrs), except when in passthrough mode. In passthrough mode the core does nothing and this message has to be handled by a follower instead. |
| `CEC_MSG_GIVE_DEVICE_VENDOR_ID` | The core will return the vendor ID that was set with [ioctl CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md#cec-adap-s-log-addrs), except when in passthrough mode. In passthrough mode the core does nothing and this message has to be handled by a follower instead. |
| `CEC_MSG_ABORT` | The core will return a Feature Abort message with reason 'Feature Refused' as per the specification, except when in passthrough mode. In passthrough mode the core does nothing and this message has to be handled by a follower instead. |
| `CEC_MSG_GIVE_PHYSICAL_ADDR` | The core will report the current physical address, except when in passthrough mode. In passthrough mode the core does nothing and this message has to be handled by a follower instead. |
| `CEC_MSG_GIVE_OSD_NAME` | The core will report the current OSD name that was set with [ioctl CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md#cec-adap-s-log-addrs), except when in passthrough mode. In passthrough mode the core does nothing and this message has to be handled by a follower instead. |
| `CEC_MSG_GIVE_FEATURES` | The core will do nothing if the CEC version is older than 2.0, otherwise it will report the current features that were set with [ioctl CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md#cec-adap-s-log-addrs), except when in passthrough mode. In passthrough mode the core does nothing (for any CEC version) and this message has to be handled by a follower instead. |
| `CEC_MSG_USER_CONTROL_PRESSED` | If [CEC_CAP_RC](cec-ioc-adap-g-caps.md#cec-cap-rc) is set and if [CEC_LOG_ADDRS_FL_ALLOW_RC_PASSTHRU](cec-ioc-adap-g-log-addrs.md#cec-log-addrs-fl-allow-rc-passthru) is set, then generate a remote control key press. This message is always passed on to the follower(s). |
| `CEC_MSG_USER_CONTROL_RELEASED` | If [CEC_CAP_RC](cec-ioc-adap-g-caps.md#cec-cap-rc) is set and if [CEC_LOG_ADDRS_FL_ALLOW_RC_PASSTHRU](cec-ioc-adap-g-log-addrs.md#cec-log-addrs-fl-allow-rc-passthru) is set, then generate a remote control key release. This message is always passed on to the follower(s). |
| `CEC_MSG_REPORT_PHYSICAL_ADDR` | The CEC framework will make note of the reported physical address and then just pass the message on to the follower(s). |

## 2.10.4. Return Value

On success 0 is returned, on error -1 and the `errno` variable is set
appropriately. The generic error codes are described at the
[Generic Error Codes](../gen-errors.md#id1) chapter.

The [ioctl CEC_S_MODE](cec-ioc-g-mode.md#cec-s-mode) can return the following
error codes:

EINVAL
:   The requested mode is invalid.

EPERM
:   Monitor mode is requested, but the process does have the `CAP_NET_ADMIN`
    capability.

EBUSY
:   Someone else is already an exclusive follower or initiator.
