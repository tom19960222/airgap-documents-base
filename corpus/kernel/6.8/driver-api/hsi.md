---
collection: kernel
version: "6.8"
title: "High Speed Synchronous Serial Interface (HSI)"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/hsi.html
fetched_at: 2026-08-21T03:30:47+00:00
---
# High Speed Synchronous Serial Interface (HSI)

## Introduction

High Speed Synchronous Interface (HSI) is a full duplex, low latency protocol,
that is optimized for die-level interconnect between an Application Processor
and a Baseband chipset. It has been specified by the MIPI alliance in 2003 and
implemented by multiple vendors since then.

The HSI interface supports full duplex communication over multiple channels
(typically 8) and is capable of reaching speeds up to 200 Mbit/s.

The serial protocol uses two signals, DATA and FLAG as combined data and clock
signals and an additional READY signal for flow control. An additional WAKE
signal can be used to wakeup the chips from standby modes. The signals are
commonly prefixed by AC for signals going from the application die to the
cellular die and CA for signals going the other way around.

```
+------------+                                 +---------------+
|  Cellular  |                                 |  Application  |
|    Die     |                                 |      Die      |
|            | - - - - - - CAWAKE - - - - - - >|               |
|           T|------------ CADATA ------------>|R              |
|           X|------------ CAFLAG ------------>|X              |
|            |<----------- ACREADY ------------|               |
|            |                                 |               |
|            |                                 |               |
|            |< - - - - -  ACWAKE - - - - - - -|               |
|           R|<----------- ACDATA -------------|T              |
|           X|<----------- ACFLAG -------------|X              |
|            |------------ CAREADY ----------->|               |
|            |                                 |               |
|            |                                 |               |
+------------+                                 +---------------+
```

## HSI Subsystem in Linux

In the Linux kernel the hsi subsystem is supposed to be used for HSI devices.
The hsi subsystem contains drivers for hsi controllers including support for
multi-port controllers and provides a generic API for using the HSI ports.

It also contains HSI client drivers, which make use of the generic API to
implement a protocol used on the HSI interface. These client drivers can
use an arbitrary number of channels.

## hsi-char Device

Each port automatically registers a generic client driver called hsi_char,
which provides a character device for userspace representing the HSI port.
It can be used to communicate via HSI from userspace. Userspace may
configure the hsi_char device using the following ioctl commands:

HSC_RESET
:   flush the HSI port

HSC_SET_PM
:   enable or disable the client.

HSC_SEND_BREAK
:   send break

HSC_SET_RX
:   set RX configuration

HSC_GET_RX
:   get RX configuration

HSC_SET_TX
:   set TX configuration

HSC_GET_TX
:   get TX configuration

## The kernel HSI API

struct hsi_channel
:   channel resource used by the hsi clients

**Definition**:

```
struct hsi_channel {
    unsigned int    id;
    const char      *name;
};
```

**Members**

`id`
:   Channel number

`name`
:   Channel name

struct hsi_config
:   Configuration for RX/TX HSI modules

**Definition**:

```
struct hsi_config {
    unsigned int            mode;
    struct hsi_channel      *channels;
    unsigned int            num_channels;
    unsigned int            num_hw_channels;
    unsigned int            speed;
    union {
        unsigned int    flow;
        unsigned int    arb_mode;
    };
};
```

**Members**

`mode`
:   Bit transmission mode (STREAM or FRAME)

`channels`
:   Channel resources used by the client

`num_channels`
:   Number of channel resources

`num_hw_channels`
:   Number of channels the transceiver is configured for [1..16]

`speed`
:   Max bit transmission speed (Kbit/s)

`{unnamed_union}`
:   anonymous

`flow`
:   RX flow type (SYNCHRONIZED or PIPELINE)

`arb_mode`
:   Arbitration mode for TX frame (Round robin, priority)

struct hsi_board_info
:   HSI client board info

**Definition**:

```
struct hsi_board_info {
    const char              *name;
    unsigned int            hsi_id;
    unsigned int            port;
    struct hsi_config       tx_cfg;
    struct hsi_config       rx_cfg;
    void *platform_data;
    struct dev_archdata     *archdata;
};
```

**Members**

`name`
:   Name for the HSI device

`hsi_id`
:   HSI controller id where the client sits

`port`
:   Port number in the controller where the client sits

`tx_cfg`
:   HSI TX configuration

`rx_cfg`
:   HSI RX configuration

`platform_data`
:   Platform related data

`archdata`
:   Architecture-dependent device data

struct hsi_client
:   HSI client attached to an HSI port

**Definition**:

```
struct hsi_client {
    struct device           device;
    struct hsi_config       tx_cfg;
    struct hsi_config       rx_cfg;
};
```

**Members**

`device`
:   Driver model representation of the device

`tx_cfg`
:   HSI TX configuration

`rx_cfg`
:   HSI RX configuration

struct hsi_client_driver
:   Driver associated to an HSI client

**Definition**:

```
struct hsi_client_driver {
    struct device_driver    driver;
};
```

**Members**

`driver`
:   Driver model representation of the driver

struct hsi_msg
:   HSI message descriptor

**Definition**:

```
struct hsi_msg {
    struct list_head        link;
    struct hsi_client       *cl;
    struct sg_table         sgt;
    void *context;
    void (*complete)(struct hsi_msg *msg);
    void (*destructor)(struct hsi_msg *msg);
    int status;
    unsigned int            actual_len;
    unsigned int            channel;
    unsigned int            ttype:1;
    unsigned int            break_frame:1;
};
```

**Members**

`link`
:   Free to use by the current descriptor owner

`cl`
:   HSI device client that issues the transfer

`sgt`
:   Head of the scatterlist array

`context`
:   Client context data associated to the transfer

`complete`
:   Transfer completion callback

`destructor`
:   Destructor to free resources when flushing

`status`
:   Status of the transfer when completed

`actual_len`
:   Actual length of data transferred on completion

`channel`
:   Channel were to TX/RX the message

`ttype`
:   Transfer type (TX if set, RX otherwise)

`break_frame`
:   if true HSI will send/receive a break frame. Data buffers are
    ignored in the request.

struct hsi_port
:   HSI port device

**Definition**:

```
struct hsi_port {
    struct device                   device;
    struct hsi_config               tx_cfg;
    struct hsi_config               rx_cfg;
    unsigned int                    num;
    unsigned int                    shared:1;
    int claimed;
    struct mutex                    lock;
    int (*async)(struct hsi_msg *msg);
    int (*setup)(struct hsi_client *cl);
    int (*flush)(struct hsi_client *cl);
    int (*start_tx)(struct hsi_client *cl);
    int (*stop_tx)(struct hsi_client *cl);
    int (*release)(struct hsi_client *cl);
    struct blocking_notifier_head   n_head;
};
```

**Members**

`device`
:   Driver model representation of the device

`tx_cfg`
:   Current TX path configuration

`rx_cfg`
:   Current RX path configuration

`num`
:   Port number

`shared`
:   Set when port can be shared by different clients

`claimed`
:   Reference count of clients which claimed the port

`lock`
:   Serialize port claim

`async`
:   Asynchronous transfer callback

`setup`
:   Callback to set the HSI client configuration

`flush`
:   Callback to clean the HW state and destroy all pending transfers

`start_tx`
:   Callback to inform that a client wants to TX data

`stop_tx`
:   Callback to inform that a client no longer wishes to TX data

`release`
:   Callback to inform that a client no longer uses the port

`n_head`
:   Notifier chain for signaling port events to the clients.

struct hsi_controller
:   HSI controller device

**Definition**:

```
struct hsi_controller {
    struct device           device;
    struct module           *owner;
    unsigned int            id;
    unsigned int            num_ports;
    struct hsi_port         **port;
};
```

**Members**

`device`
:   Driver model representation of the device

`owner`
:   Pointer to the module owning the controller

`id`
:   HSI controller ID

`num_ports`
:   Number of ports in the HSI controller

`port`
:   Array of HSI ports

unsigned int hsi_id(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Get HSI controller ID associated to a client

**Parameters**

`struct hsi_client *cl`
:   Pointer to a HSI client

**Description**

Return the controller id where the client is attached to

unsigned int hsi_port_id(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Gets the port number a client is attached to

**Parameters**

`struct hsi_client *cl`
:   Pointer to HSI client

**Description**

Return the port number associated to the client

int hsi_setup(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Configure the client's port

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

**Description**

When sharing ports, clients should either relay on a single
client setup or have the same setup for all of them.

Return -errno on failure, 0 on success

int hsi_flush(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Flush all pending transactions on the client's port

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

**Description**

This function will destroy all pending hsi_msg in the port and reset
the HW port so it is ready to receive and transmit from a clean state.

Return -errno on failure, 0 on success

int hsi_async_read(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, struct [hsi_msg](hsi.md#c.hsi_msg "hsi_msg") \*msg)
:   Submit a read transfer

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

`struct hsi_msg *msg`
:   HSI message descriptor of the transfer

**Description**

Return -errno on failure, 0 on success

int hsi_async_write(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, struct [hsi_msg](hsi.md#c.hsi_msg "hsi_msg") \*msg)
:   Submit a write transfer

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

`struct hsi_msg *msg`
:   HSI message descriptor of the transfer

**Description**

Return -errno on failure, 0 on success

int hsi_start_tx(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Signal the port that the client wants to start a TX

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

**Description**

Return -errno on failure, 0 on success

int hsi_stop_tx(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Signal the port that the client no longer wants to transmit

**Parameters**

`struct hsi_client *cl`
:   Pointer to the HSI client

**Description**

Return -errno on failure, 0 on success

void hsi_port_unregister_clients(struct [hsi_port](hsi.md#c.hsi_port "hsi_port") \*port)
:   Unregister an HSI port

**Parameters**

`struct hsi_port *port`
:   The HSI port to unregister

void hsi_unregister_controller(struct [hsi_controller](hsi.md#c.hsi_controller "hsi_controller") \*hsi)
:   Unregister an HSI controller

**Parameters**

`struct hsi_controller *hsi`
:   The HSI controller to register

int hsi_register_controller(struct [hsi_controller](hsi.md#c.hsi_controller "hsi_controller") \*hsi)
:   Register an HSI controller and its ports

**Parameters**

`struct hsi_controller *hsi`
:   The HSI controller to register

**Description**

Returns -errno on failure, 0 on success.

int hsi_register_client_driver(struct [hsi_client_driver](hsi.md#c.hsi_client_driver "hsi_client_driver") \*drv)
:   Register an HSI client to the HSI bus

**Parameters**

`struct hsi_client_driver *drv`
:   HSI client driver to register

**Description**

Returns -errno on failure, 0 on success.

void hsi_put_controller(struct [hsi_controller](hsi.md#c.hsi_controller "hsi_controller") \*hsi)
:   Free an HSI controller

**Parameters**

`struct hsi_controller *hsi`
:   Pointer to the HSI controller to freed

**Description**

HSI controller drivers should only use this function if they need
to free their allocated hsi_controller structures before a successful
call to hsi_register_controller. Other use is not allowed.

struct [hsi_controller](hsi.md#c.hsi_controller "hsi_controller") \*hsi_alloc_controller(unsigned int n_ports, gfp_t flags)
:   Allocate an HSI controller and its ports

**Parameters**

`unsigned int n_ports`
:   Number of ports on the HSI controller

`gfp_t flags`
:   Kernel allocation flags

**Description**

Return NULL on failure or a pointer to an hsi_controller on success.

void hsi_free_msg(struct [hsi_msg](hsi.md#c.hsi_msg "hsi_msg") \*msg)
:   Free an HSI message

**Parameters**

`struct hsi_msg *msg`
:   Pointer to the HSI message

**Description**

Client is responsible to free the buffers pointed by the scatterlists.

struct [hsi_msg](hsi.md#c.hsi_msg "hsi_msg") \*hsi_alloc_msg(unsigned int nents, gfp_t flags)
:   Allocate an HSI message

**Parameters**

`unsigned int nents`
:   Number of memory entries

`gfp_t flags`
:   Kernel allocation flags

**Description**

nents can be 0. This mainly makes sense for read transfer.
In that case, HSI drivers will call the complete callback when
there is data to be read without consuming it.

Return NULL on failure or a pointer to an hsi_msg on success.

int hsi_async(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, struct [hsi_msg](hsi.md#c.hsi_msg "hsi_msg") \*msg)
:   Submit an HSI transfer to the controller

**Parameters**

`struct hsi_client *cl`
:   HSI client sending the transfer

`struct hsi_msg *msg`
:   The HSI transfer passed to controller

**Description**

The HSI message must have the channel, ttype, complete and destructor
fields set beforehand. If nents > 0 then the client has to initialize
also the scatterlists to point to the buffers to write to or read from.

HSI controllers relay on pre-allocated buffers from their clients and they
do not allocate buffers on their own.

Once the HSI message transfer finishes, the HSI controller calls the
complete callback with the status and actual_len fields of the HSI message
updated. The complete callback can be called before returning from
hsi_async.

Returns -errno on failure or 0 on success

int hsi_claim_port(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, unsigned int share)
:   Claim the HSI client's port

**Parameters**

`struct hsi_client *cl`
:   HSI client that wants to claim its port

`unsigned int share`
:   Flag to indicate if the client wants to share the port or not.

**Description**

Returns -errno on failure, 0 on success.

void hsi_release_port(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Release the HSI client's port

**Parameters**

`struct hsi_client *cl`
:   HSI client which previously claimed its port

int hsi_register_port_event(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, void (\*handler)(struct [hsi_client](hsi.md#c.hsi_client "hsi_client")\*, unsigned long))
:   Register a client to receive port events

**Parameters**

`struct hsi_client *cl`
:   HSI client that wants to receive port events

`void (*handler)(struct hsi_client *, unsigned long)`
:   Event handler callback

**Description**

Clients should register a callback to be able to receive
events from the ports. Registration should happen after
claiming the port.
The handler can be called in interrupt context.

Returns -errno on error, or 0 on success.

int hsi_unregister_port_event(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl)
:   Stop receiving port events for a client

**Parameters**

`struct hsi_client *cl`
:   HSI client that wants to stop receiving port events

**Description**

Clients should call this function before releasing their associated
port.

Returns -errno on error, or 0 on success.

int hsi_event(struct [hsi_port](hsi.md#c.hsi_port "hsi_port") \*port, unsigned long event)
:   Notifies clients about port events

**Parameters**

`struct hsi_port *port`
:   Port where the event occurred

`unsigned long event`
:   The event type

**Description**

Clients should not be concerned about wake line behavior. However, due
to a race condition in HSI HW protocol, clients need to be notified
about wake line changes, so they can implement a workaround for it.

Events:
HSI_EVENT_START_RX - Incoming wake line high
HSI_EVENT_STOP_RX - Incoming wake line down

Returns -errno on error, or 0 on success.

int hsi_get_channel_id_by_name(struct [hsi_client](hsi.md#c.hsi_client "hsi_client") \*cl, char \*name)
:   acquire channel id by channel name

**Parameters**

`struct hsi_client *cl`
:   HSI client, which uses the channel

`char *name`
:   name the channel is known under

**Description**

Clients can call this function to get the hsi channel ids similar to
requesting IRQs or GPIOs by name. This function assumes the same
channel configuration is used for RX and TX.

Returns -errno on error or channel id on success.
