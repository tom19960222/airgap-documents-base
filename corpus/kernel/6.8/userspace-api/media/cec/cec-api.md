---
collection: kernel
version: "6.8"
title: "Part V - Consumer Electronics Control API"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/media/cec/cec-api.html
fetched_at: 2026-08-21T03:35:39+00:00
---
# Part V - Consumer Electronics Control API

This part describes the CEC: Consumer Electronics Control

Table of Contents

- [1. Introduction](cec-intro.md)
- [2. Function Reference](cec-funcs.md)
  - [2.1. cec open()](cec-func-open.md)
    - [2.1.1. Name](cec-func-open.md#name)
    - [2.1.2. Synopsis](cec-func-open.md#synopsis)
    - [2.1.3. Arguments](cec-func-open.md#arguments)
    - [2.1.4. Description](cec-func-open.md#description)
    - [2.1.5. Return Value](cec-func-open.md#return-value)
  - [2.2. cec close()](cec-func-close.md)
    - [2.2.1. Name](cec-func-close.md#name)
    - [2.2.2. Synopsis](cec-func-close.md#synopsis)
    - [2.2.3. Arguments](cec-func-close.md#arguments)
    - [2.2.4. Description](cec-func-close.md#description)
    - [2.2.5. Return Value](cec-func-close.md#return-value)
  - [2.3. cec ioctl()](cec-func-ioctl.md)
    - [2.3.1. Name](cec-func-ioctl.md#name)
    - [2.3.2. Synopsis](cec-func-ioctl.md#synopsis)
    - [2.3.3. Arguments](cec-func-ioctl.md#arguments)
    - [2.3.4. Description](cec-func-ioctl.md#description)
    - [2.3.5. Return Value](cec-func-ioctl.md#return-value)
  - [2.4. cec poll()](cec-func-poll.md)
    - [2.4.1. Name](cec-func-poll.md#name)
    - [2.4.2. Synopsis](cec-func-poll.md#synopsis)
    - [2.4.3. Arguments](cec-func-poll.md#arguments)
    - [2.4.4. Description](cec-func-poll.md#description)
    - [2.4.5. Return Value](cec-func-poll.md#return-value)
  - [2.5. ioctl CEC_ADAP_G_CAPS](cec-ioc-adap-g-caps.md)
    - [2.5.1. Name](cec-ioc-adap-g-caps.md#name)
    - [2.5.2. Synopsis](cec-ioc-adap-g-caps.md#synopsis)
    - [2.5.3. Arguments](cec-ioc-adap-g-caps.md#arguments)
    - [2.5.4. Description](cec-ioc-adap-g-caps.md#description)
    - [2.5.5. Return Value](cec-ioc-adap-g-caps.md#return-value)
  - [2.6. ioctls CEC_ADAP_G_LOG_ADDRS and CEC_ADAP_S_LOG_ADDRS](cec-ioc-adap-g-log-addrs.md)
    - [2.6.1. Name](cec-ioc-adap-g-log-addrs.md#name)
    - [2.6.2. Synopsis](cec-ioc-adap-g-log-addrs.md#synopsis)
    - [2.6.3. Arguments](cec-ioc-adap-g-log-addrs.md#arguments)
    - [2.6.4. Description](cec-ioc-adap-g-log-addrs.md#description)
    - [2.6.5. Return Value](cec-ioc-adap-g-log-addrs.md#return-value)
  - [2.7. ioctls CEC_ADAP_G_PHYS_ADDR and CEC_ADAP_S_PHYS_ADDR](cec-ioc-adap-g-phys-addr.md)
    - [2.7.1. Name](cec-ioc-adap-g-phys-addr.md#name)
    - [2.7.2. Synopsis](cec-ioc-adap-g-phys-addr.md#synopsis)
    - [2.7.3. Arguments](cec-ioc-adap-g-phys-addr.md#arguments)
    - [2.7.4. Description](cec-ioc-adap-g-phys-addr.md#description)
    - [2.7.5. Return Value](cec-ioc-adap-g-phys-addr.md#return-value)
  - [2.8. ioctl CEC_ADAP_G_CONNECTOR_INFO](cec-ioc-adap-g-conn-info.md)
    - [2.8.1. Name](cec-ioc-adap-g-conn-info.md#name)
    - [2.8.2. Synopsis](cec-ioc-adap-g-conn-info.md#synopsis)
    - [2.8.3. Arguments](cec-ioc-adap-g-conn-info.md#arguments)
    - [2.8.4. Description](cec-ioc-adap-g-conn-info.md#description)
  - [2.9. ioctl CEC_DQEVENT](cec-ioc-dqevent.md)
    - [2.9.1. Name](cec-ioc-dqevent.md#name)
    - [2.9.2. Synopsis](cec-ioc-dqevent.md#synopsis)
    - [2.9.3. Arguments](cec-ioc-dqevent.md#arguments)
    - [2.9.4. Description](cec-ioc-dqevent.md#description)
    - [2.9.5. Return Value](cec-ioc-dqevent.md#return-value)
  - [2.10. ioctls CEC_G_MODE and CEC_S_MODE](cec-ioc-g-mode.md)
    - [2.10.1. Synopsis](cec-ioc-g-mode.md#synopsis)
    - [2.10.2. Arguments](cec-ioc-g-mode.md#arguments)
    - [2.10.3. Description](cec-ioc-g-mode.md#description)
    - [2.10.4. Return Value](cec-ioc-g-mode.md#return-value)
  - [2.11. ioctls CEC_RECEIVE and CEC_TRANSMIT](cec-ioc-receive.md)
    - [2.11.1. Name](cec-ioc-receive.md#name)
    - [2.11.2. Synopsis](cec-ioc-receive.md#synopsis)
    - [2.11.3. Arguments](cec-ioc-receive.md#arguments)
    - [2.11.4. Description](cec-ioc-receive.md#description)
    - [2.11.5. Return Value](cec-ioc-receive.md#return-value)
- [3. CEC Pin Framework Error Injection](cec-pin-error-inj.md)
  - [3.1. Basic Syntax](cec-pin-error-inj.md#basic-syntax)
  - [3.2. Clear Error Injections](cec-pin-error-inj.md#clear-error-injections)
  - [3.3. Receive Messages](cec-pin-error-inj.md#receive-messages)
  - [3.4. Transmit Messages](cec-pin-error-inj.md#transmit-messages)
  - [3.5. Custom Pulses](cec-pin-error-inj.md#custom-pulses)
- [4. CEC Header File](cec-header.md)
  - [4.1. cec.h](cec-header.md#cec-h)

## Revision and Copyright

Authors:

- Verkuil, Hans <[hverkuil-cisco@xs4all.nl](mailto:hverkuil-cisco%40xs4all.nl)>

> - Initial version.

**Copyright** © 2016 : Hans Verkuil

## Revision History

revision
:   1.0.0 / 2016-03-17 (*hv*)

Initial revision
