---
collection: kernel
version: "6.8"
title: "3.5. Digital TV Network kABI"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/media/dtv-net.html
fetched_at: 2026-08-21T03:39:38+00:00
---
# 3.5. Digital TV Network kABI

struct dvb_net
:   describes a DVB network interface

**Definition**:

```
struct dvb_net {
    struct dvb_device *dvbdev;
    struct net_device *device[DVB_NET_DEVICES_MAX];
    int state[DVB_NET_DEVICES_MAX];
    unsigned int exit:1;
    struct dmx_demux *demux;
    struct mutex ioctl_mutex;
    struct mutex remove_mutex;
};
```

**Members**

`dvbdev`
:   pointer to [`struct dvb_device`](dtv-common.md#c.dvb_device "dvb_device").

`device`
:   array of pointers to [`struct net_device`](../../networking/kapi.md#c.net_device "net_device").

`state`
:   array of integers to each net device. A value
    different than zero means that the interface is
    in usage.

`exit`
:   flag to indicate when the device is being removed.

`demux`
:   pointer to [`struct dmx_demux`](dtv-demux.md#c.dmx_demux "dmx_demux").

`ioctl_mutex`
:   protect access to this struct.

`remove_mutex`
:   mutex that avoids a race condition between a callback
    called when the hardware is disconnected and the
    file_operations of dvb_net.

**Description**

Currently, the core supports up to `DVB_NET_DEVICES_MAX` (10) network
devices.

int dvb_net_init(struct [dvb_adapter](dtv-common.md#c.dvb_adapter "dvb_adapter") \*adap, struct [dvb_net](dtv-net.md#c.dvb_net "dvb_net") \*dvbnet, struct [dmx_demux](dtv-demux.md#c.dmx_demux "dmx_demux") \*dmxdemux)
:   nitializes a digital TV network device and registers it.

**Parameters**

`struct dvb_adapter *adap`
:   pointer to [`struct dvb_adapter`](dtv-common.md#c.dvb_adapter "dvb_adapter").

`struct dvb_net *dvbnet`
:   pointer to [`struct dvb_net`](dtv-net.md#c.dvb_net "dvb_net").

`struct dmx_demux *dmxdemux`
:   pointer to [`struct dmx_demux`](dtv-demux.md#c.dmx_demux "dmx_demux").

void dvb_net_release(struct [dvb_net](dtv-net.md#c.dvb_net "dvb_net") \*dvbnet)
:   releases a digital TV network device and unregisters it.

**Parameters**

`struct dvb_net *dvbnet`
:   pointer to [`struct dvb_net`](dtv-net.md#c.dvb_net "dvb_net").
