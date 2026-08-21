---
collection: kernel
version: "6.8"
title: "13. pxrc - PhoenixRC Flight Controller Adapter"
source_url: https://www.kernel.org/doc/html/v6.8/input/devices/pxrc.html
fetched_at: 2026-08-21T03:44:25+00:00
---
# 13. pxrc - PhoenixRC Flight Controller Adapter

Author
:   Marcus Folkesson <[marcus.folkesson@gmail.com](mailto:marcus.folkesson%40gmail.com)>

This driver let you use your own RC controller plugged into the
adapter that comes with PhoenixRC or other compatible adapters.

The adapter supports 7 analog channels and 1 digital input switch.

## 13.1. Notes

Many RC controllers is able to configure which stick goes to which channel.
This is also configurable in most simulators, so a matching is not necessary.

The driver is generating the following input event for analog channels:

| Channel | Event |
| --- | --- |
| 1 | ABS_X |
| 2 | ABS_Y |
| 3 | ABS_RX |
| 4 | ABS_RY |
| 5 | ABS_RUDDER |
| 6 | ABS_THROTTLE |
| 7 | ABS_MISC |

The digital input switch is generated as an BTN_A event.

## 13.2. Manual Testing

To test this driver's functionality you may use input-event which is part of
the input layer utilities suite [1](pxrc.md#id2).

For example:

```
> modprobe pxrc
> input-events <devnr>
```

To print all input events from input devnr.

## 13.3. References

[1](pxrc.md#id1)
:   <https://www.kraxel.org/cgit/input/>
