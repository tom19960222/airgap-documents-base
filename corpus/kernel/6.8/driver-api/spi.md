---
collection: kernel
version: "6.8"
title: "Serial Peripheral Interface (SPI)"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/spi.html
fetched_at: 2026-08-21T03:30:43+00:00
---
# Serial Peripheral Interface (SPI)

SPI is the "Serial Peripheral Interface", widely used with embedded
systems because it is a simple and efficient interface: basically a
multiplexed shift register. Its three signal wires hold a clock (SCK,
often in the range of 1-20 MHz), a "Master Out, Slave In" (MOSI) data
line, and a "Master In, Slave Out" (MISO) data line. SPI is a full
duplex protocol; for each bit shifted out the MOSI line (one per clock)
another is shifted in on the MISO line. Those bits are assembled into
words of various sizes on the way to and from system memory. An
additional chipselect line is usually active-low (nCS); four signals are
normally used for each peripheral, plus sometimes an interrupt.

The SPI bus facilities listed here provide a generalized interface to
declare SPI busses and devices, manage them according to the standard
Linux driver model, and perform input/output operations. At this time,
only "master" side interfaces are supported, where Linux talks to SPI
peripherals and does not implement such a peripheral itself. (Interfaces
to support implementing SPI slaves would necessarily look different.)

The programming interface is structured around two kinds of driver, and
two kinds of device. A "Controller Driver" abstracts the controller
hardware, which may be as simple as a set of GPIO pins or as complex as
a pair of FIFOs connected to dual DMA engines on the other side of the
SPI shift register (maximizing throughput). Such drivers bridge between
whatever bus they sit on (often the platform bus) and SPI, and expose
the SPI side of their device as a [`struct spi_controller`](spi.md#c.spi_controller "spi_controller"). SPI devices are children of that master,
represented as a [`struct spi_device`](spi.md#c.spi_device "spi_device") and
manufactured from [`struct spi_board_info`](spi.md#c.spi_board_info "spi_board_info") descriptors which are usually provided by
board-specific initialization code. A [`struct spi_driver`](spi.md#c.spi_driver "spi_driver") is called a "Protocol Driver", and is bound to a
spi_device using normal driver model calls.

The I/O model is a set of queued messages. Protocol drivers submit one
or more [`struct spi_message`](spi.md#c.spi_message "spi_message") objects,
which are processed and completed asynchronously. (There are synchronous
wrappers, however.) Messages are built from one or more
[`struct spi_transfer`](spi.md#c.spi_transfer "spi_transfer") objects, each of
which wraps a full duplex SPI transfer. A variety of protocol tweaking
options are needed, because different chips adopt very different
policies for how they use the bits transferred with SPI.

struct spi_statistics
:   statistics for spi transfers

**Definition**:

```
struct spi_statistics {
    struct u64_stats_sync   syncp;
    u64_stats_t messages;
    u64_stats_t transfers;
    u64_stats_t errors;
    u64_stats_t timedout;
    u64_stats_t spi_sync;
    u64_stats_t spi_sync_immediate;
    u64_stats_t spi_async;
    u64_stats_t bytes;
    u64_stats_t bytes_rx;
    u64_stats_t bytes_tx;
#define SPI_STATISTICS_HISTO_SIZE 17;
    u64_stats_t transfer_bytes_histo[SPI_STATISTICS_HISTO_SIZE];
    u64_stats_t transfers_split_maxsize;
};
```

**Members**

`syncp`
:   seqcount to protect members in this struct for per-cpu update
    on 32-bit systems

`messages`
:   number of spi-messages handled

`transfers`
:   number of spi_transfers handled

`errors`
:   number of errors during spi_transfer

`timedout`
:   number of timeouts during spi_transfer

`spi_sync`
:   number of times spi_sync is used

`spi_sync_immediate`

> number of times spi_sync is executed immediately
> in calling context without queuing and scheduling

`spi_async`
:   number of times spi_async is used

`bytes`
:   number of bytes transferred to/from device

`bytes_rx`
:   number of bytes received from device

`bytes_tx`
:   number of bytes sent to device

`transfer_bytes_histo`

> transfer bytes histogram

`transfers_split_maxsize`

> number of transfers that have been split because of
> maxsize limit

struct spi_delay
:   SPI delay information

**Definition**:

```
struct spi_delay {
#define SPI_DELAY_UNIT_USECS    0;
#define SPI_DELAY_UNIT_NSECS    1;
#define SPI_DELAY_UNIT_SCK      2;
    u16 value;
    u8 unit;
};
```

**Members**

`value`
:   Value for the delay

`unit`
:   Unit for the delay

struct spi_device
:   Controller side proxy for an SPI slave device

**Definition**:

```
struct spi_device {
    struct device           dev;
    struct spi_controller   *controller;
    struct spi_controller   *master;
    u32 max_speed_hz;
    u8 chip_select[SPI_CS_CNT_MAX];
    u8 bits_per_word;
    bool rt;
#define SPI_NO_TX               BIT(31)         ;
#define SPI_NO_RX               BIT(30)         ;
#define SPI_TPM_HW_FLOW         BIT(29)         ;
#define SPI_MODE_KERNEL_MASK    (~(BIT(29) - 1));
    u32 mode;
    int irq;
    void *controller_state;
    void *controller_data;
    char modalias[SPI_NAME_SIZE];
    const char              *driver_override;
    struct gpio_desc        *cs_gpiod[SPI_CS_CNT_MAX];
    struct spi_delay        word_delay;
    struct spi_delay        cs_setup;
    struct spi_delay        cs_hold;
    struct spi_delay        cs_inactive;
    struct spi_statistics __percpu  *pcpu_statistics;
    u32 cs_index_mask : SPI_CS_CNT_MAX;
};
```

**Members**

`dev`
:   Driver model representation of the device.

`controller`
:   SPI controller used with the device.

`master`
:   Copy of controller, for backwards compatibility.

`max_speed_hz`
:   Maximum clock rate to be used with this chip
    (on this board); may be changed by the device's driver.
    The spi_transfer.speed_hz can override this for each transfer.

`chip_select`
:   Array of physical chipselect, spi->chipselect[i] gives
    the corresponding physical CS for logical CS i.

`bits_per_word`
:   Data transfers involve one or more words; word sizes
    like eight or 12 bits are common. In-memory wordsizes are
    powers of two bytes (e.g. 20 bit samples use 32 bits).
    This may be changed by the device's driver, or left at the
    default (0) indicating protocol words are eight bit bytes.
    The spi_transfer.bits_per_word can override this for each transfer.

`rt`
:   Make the pump thread real time priority.

`mode`
:   The spi mode defines how data is clocked out and in.
    This may be changed by the device's driver.
    The "active low" default for chipselect mode can be overridden
    (by specifying SPI_CS_HIGH) as can the "MSB first" default for
    each word in a transfer (by specifying SPI_LSB_FIRST).

`irq`
:   Negative, or the number passed to [`request_irq()`](../core-api/genericirq.md#c.request_irq "request_irq") to receive
    interrupts from this device.

`controller_state`
:   Controller's runtime state

`controller_data`
:   Board-specific definitions for controller, such as
    FIFO initialization parameters; from board_info.controller_data

`modalias`
:   Name of the driver to use with this device, or an alias
    for that name. This appears in the sysfs "modalias" attribute
    for driver coldplugging, and in uevents used for hotplugging

`driver_override`
:   If the name of a driver is written to this attribute, then
    the device will bind to the named driver and only the named driver.
    Do not set directly, because core frees it; use [`driver_set_override()`](infrastructure.md#c.driver_set_override "driver_set_override") to
    set or clear it.

`cs_gpiod`
:   Array of GPIO descriptors of the corresponding chipselect lines
    (optional, NULL when not using a GPIO line)

`word_delay`
:   delay to be inserted between consecutive
    words of a transfer

`cs_setup`
:   delay to be introduced by the controller after CS is asserted

`cs_hold`
:   delay to be introduced by the controller before CS is deasserted

`cs_inactive`
:   delay to be introduced by the controller after CS is
    deasserted. If **cs_change_delay** is used from **spi_transfer**, then the
    two delays will be added up.

`pcpu_statistics`
:   statistics for the spi_device

**Description**

A **spi_device** is used to interchange data between an SPI slave
(usually a discrete chip) and CPU memory.

In **dev**, the platform_data is used to hold information about this
device that's meaningful to the device's protocol driver, but not
to its controller. One example might be an identifier for a chip
variant with slightly different functionality; another might be
information about how this particular board wires the chip's pins.

struct spi_driver
:   Host side "protocol" driver

**Definition**:

```
struct spi_driver {
    const struct spi_device_id *id_table;
    int (*probe)(struct spi_device *spi);
    void (*remove)(struct spi_device *spi);
    void (*shutdown)(struct spi_device *spi);
    struct device_driver    driver;
};
```

**Members**

`id_table`
:   List of SPI devices supported by this driver

`probe`
:   Binds this driver to the SPI device. Drivers can verify
    that the device is actually present, and may need to configure
    characteristics (such as bits_per_word) which weren't needed for
    the initial configuration done during system setup.

`remove`
:   Unbinds this driver from the SPI device

`shutdown`
:   Standard shutdown callback used during system state
    transitions such as powerdown/halt and kexec

`driver`
:   SPI device drivers should initialize the name and owner
    field of this structure.

**Description**

This represents the kind of device driver that uses SPI messages to
interact with the hardware at the other end of a SPI link. It's called
a "protocol" driver because it works through messages rather than talking
directly to SPI hardware (which is what the underlying SPI controller
driver does to pass those messages). These protocols are defined in the
specification for the device(s) supported by the driver.

As a rule, those device protocols represent the lowest level interface
supported by a driver, and it will support upper level interfaces too.
Examples of such upper levels include frameworks like MTD, networking,
MMC, RTC, filesystem character device nodes, and hardware monitoring.

void spi_unregister_driver(struct [spi_driver](spi.md#c.spi_driver "spi_driver") \*sdrv)
:   reverse effect of spi_register_driver

**Parameters**

`struct spi_driver *sdrv`
:   the driver to unregister

**Context**

can sleep

module_spi_driver

`module_spi_driver (__spi_driver)`

> Helper macro for registering a SPI driver

**Parameters**

`__spi_driver`
:   spi_driver struct

**Description**

Helper macro for SPI drivers which do not do anything special in module
init/exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces [`module_init()`](basics.md#c.module_init "module_init") and [`module_exit()`](basics.md#c.module_exit "module_exit")

struct spi_controller
:   interface to SPI master or slave controller

**Definition**:

```
struct spi_controller {
    struct device   dev;
    struct list_head list;
    s16 bus_num;
    u16 num_chipselect;
    u16 dma_alignment;
    u32 mode_bits;
    u32 buswidth_override_bits;
    u32 bits_per_word_mask;
#define SPI_BPW_MASK(bits) BIT((bits) - 1);
#define SPI_BPW_RANGE_MASK(min, max) GENMASK((max) - 1, (min) - 1);
    u32 min_speed_hz;
    u32 max_speed_hz;
    u16 flags;
#define SPI_CONTROLLER_HALF_DUPLEX      BIT(0)  ;
#define SPI_CONTROLLER_NO_RX            BIT(1)  ;
#define SPI_CONTROLLER_NO_TX            BIT(2)  ;
#define SPI_CONTROLLER_MUST_RX          BIT(3)  ;
#define SPI_CONTROLLER_MUST_TX          BIT(4)  ;
#define SPI_CONTROLLER_GPIO_SS          BIT(5)  ;
#define SPI_CONTROLLER_SUSPENDED        BIT(6)  ;
#define SPI_CONTROLLER_MULTI_CS         BIT(7);
    bool devm_allocated;
    union {
        bool slave;
        bool target;
    };
    size_t (*max_transfer_size)(struct spi_device *spi);
    size_t (*max_message_size)(struct spi_device *spi);
    struct mutex            io_mutex;
    struct mutex            add_lock;
    spinlock_t bus_lock_spinlock;
    struct mutex            bus_lock_mutex;
    bool bus_lock_flag;
    int (*setup)(struct spi_device *spi);
    int (*set_cs_timing)(struct spi_device *spi);
    int (*transfer)(struct spi_device *spi, struct spi_message *mesg);
    void (*cleanup)(struct spi_device *spi);
    bool (*can_dma)(struct spi_controller *ctlr,struct spi_device *spi, struct spi_transfer *xfer);
    struct device *dma_map_dev;
    struct device *cur_rx_dma_dev;
    struct device *cur_tx_dma_dev;
    bool queued;
    struct kthread_worker           *kworker;
    struct kthread_work             pump_messages;
    spinlock_t queue_lock;
    struct list_head                queue;
    struct spi_message              *cur_msg;
    struct completion               cur_msg_completion;
    bool cur_msg_incomplete;
    bool cur_msg_need_completion;
    bool busy;
    bool running;
    bool rt;
    bool auto_runtime_pm;
    bool cur_msg_mapped;
    char last_cs[SPI_CS_CNT_MAX];
    char last_cs_index_mask;
    bool last_cs_mode_high;
    bool fallback;
    struct completion               xfer_completion;
    size_t max_dma_len;
    int (*prepare_transfer_hardware)(struct spi_controller *ctlr);
    int (*transfer_one_message)(struct spi_controller *ctlr, struct spi_message *mesg);
    int (*unprepare_transfer_hardware)(struct spi_controller *ctlr);
    int (*prepare_message)(struct spi_controller *ctlr, struct spi_message *message);
    int (*unprepare_message)(struct spi_controller *ctlr, struct spi_message *message);
    union {
        int (*slave_abort)(struct spi_controller *ctlr);
        int (*target_abort)(struct spi_controller *ctlr);
    };
    void (*set_cs)(struct spi_device *spi, bool enable);
    int (*transfer_one)(struct spi_controller *ctlr, struct spi_device *spi, struct spi_transfer *transfer);
    void (*handle_err)(struct spi_controller *ctlr, struct spi_message *message);
    const struct spi_controller_mem_ops *mem_ops;
    const struct spi_controller_mem_caps *mem_caps;
    struct gpio_desc        **cs_gpiods;
    bool use_gpio_descriptors;
    s8 unused_native_cs;
    s8 max_native_cs;
    struct spi_statistics __percpu  *pcpu_statistics;
    struct dma_chan         *dma_tx;
    struct dma_chan         *dma_rx;
    void *dummy_rx;
    void *dummy_tx;
    int (*fw_translate_cs)(struct spi_controller *ctlr, unsigned cs);
    bool ptp_sts_supported;
    unsigned long           irq_flags;
    bool queue_empty;
    bool must_async;
};
```

**Members**

`dev`
:   device interface to this driver

`list`
:   link with the global spi_controller list

`bus_num`
:   board-specific (and often SOC-specific) identifier for a
    given SPI controller.

`num_chipselect`
:   chipselects are used to distinguish individual
    SPI slaves, and are numbered from zero to num_chipselects.
    each slave has a chipselect signal, but it's common that not
    every chipselect is connected to a slave.

`dma_alignment`
:   SPI controller constraint on DMA buffers alignment.

`mode_bits`
:   flags understood by this controller driver

`buswidth_override_bits`
:   flags to override for this controller driver

`bits_per_word_mask`
:   A mask indicating which values of bits_per_word are
    supported by the driver. Bit n indicates that a bits_per_word n+1 is
    supported. If set, the SPI core will reject any transfer with an
    unsupported bits_per_word. If not set, this value is simply ignored,
    and it's up to the individual driver to perform any validation.

`min_speed_hz`
:   Lowest supported transfer speed

`max_speed_hz`
:   Highest supported transfer speed

`flags`
:   other constraints relevant to this driver

`devm_allocated`
:   whether the allocation of this struct is devres-managed

`{unnamed_union}`
:   anonymous

`slave`
:   indicates that this is an SPI slave controller

`target`
:   indicates that this is an SPI target controller

`max_transfer_size`
:   function that returns the max transfer size for
    a [`spi_device`](spi.md#c.spi_device "spi_device"); may be `NULL`, so the default `SIZE_MAX` will be used.

`max_message_size`
:   function that returns the max message size for
    a [`spi_device`](spi.md#c.spi_device "spi_device"); may be `NULL`, so the default `SIZE_MAX` will be used.

`io_mutex`
:   mutex for physical bus access

`add_lock`
:   mutex to avoid adding devices to the same chipselect

`bus_lock_spinlock`
:   spinlock for SPI bus locking

`bus_lock_mutex`
:   mutex for exclusion of multiple callers

`bus_lock_flag`
:   indicates that the SPI bus is locked for exclusive use

`setup`
:   updates the device mode and clocking records used by a
    device's SPI controller; protocol code may call this. This
    must fail if an unrecognized or unsupported mode is requested.
    It's always safe to call this unless transfers are pending on
    the device whose settings are being modified.

`set_cs_timing`
:   optional hook for SPI devices to request SPI master
    controller for configuring specific CS setup time, hold time and inactive
    delay interms of clock counts

`transfer`
:   adds a message to the controller's transfer queue.

`cleanup`
:   frees controller-specific state

`can_dma`
:   determine whether this controller supports DMA

`dma_map_dev`
:   device which can be used for DMA mapping

`cur_rx_dma_dev`
:   device which is currently used for RX DMA mapping

`cur_tx_dma_dev`
:   device which is currently used for TX DMA mapping

`queued`
:   whether this controller is providing an internal message queue

`kworker`
:   pointer to thread struct for message pump

`pump_messages`
:   work struct for scheduling work to the message pump

`queue_lock`
:   spinlock to synchronise access to message queue

`queue`
:   message queue

`cur_msg`
:   the currently in-flight message

`cur_msg_completion`
:   a completion for the current in-flight message

`cur_msg_incomplete`
:   Flag used internally to opportunistically skip
    the **cur_msg_completion**. This flag is used to check if the driver has
    already called [`spi_finalize_current_message()`](spi.md#c.spi_finalize_current_message "spi_finalize_current_message").

`cur_msg_need_completion`
:   Flag used internally to opportunistically skip
    the **cur_msg_completion**. This flag is used to signal the context that
    is running [`spi_finalize_current_message()`](spi.md#c.spi_finalize_current_message "spi_finalize_current_message") that it needs to complete()

`busy`
:   message pump is busy

`running`
:   message pump is running

`rt`
:   whether this queue is set to run as a realtime task

`auto_runtime_pm`
:   the core should ensure a runtime PM reference is held
    while the hardware is prepared, using the parent
    device for the spidev

`cur_msg_mapped`
:   message has been mapped for DMA

`last_cs`
:   the last chip_select that is recorded by set_cs, -1 on non chip
    selected

`last_cs_mode_high`
:   was (mode & SPI_CS_HIGH) true on the last call to set_cs.

`fallback`
:   fallback to PIO if DMA transfer return failure with
    SPI_TRANS_FAIL_NO_START.

`xfer_completion`
:   used by core transfer_one_message()

`max_dma_len`
:   Maximum length of a DMA transfer for the device.

`prepare_transfer_hardware`
:   a message will soon arrive from the queue
    so the subsystem requests the driver to prepare the transfer hardware
    by issuing this call

`transfer_one_message`
:   the subsystem calls the driver to transfer a single
    message while queuing transfers that arrive in the meantime. When the
    driver is finished with this message, it must call
    [`spi_finalize_current_message()`](spi.md#c.spi_finalize_current_message "spi_finalize_current_message") so the subsystem can issue the next
    message

`unprepare_transfer_hardware`
:   there are currently no more messages on the
    queue so the subsystem notifies the driver that it may relax the
    hardware by issuing this call

`prepare_message`
:   set up the controller to transfer a single message,
    for example doing DMA mapping. Called from threaded
    context.

`unprepare_message`
:   undo any work done by prepare_message().

`{unnamed_union}`
:   anonymous

`slave_abort`
:   abort the ongoing transfer request on an SPI slave controller

`target_abort`
:   abort the ongoing transfer request on an SPI target controller

`set_cs`
:   set the logic level of the chip select line. May be called
    from interrupt context.

`transfer_one`
:   transfer a single spi_transfer.

    - return 0 if the transfer is finished,
    - return 1 if the transfer is still in progress. When
      the driver is finished with this transfer it must
      call [`spi_finalize_current_transfer()`](spi.md#c.spi_finalize_current_transfer "spi_finalize_current_transfer") so the subsystem
      can issue the next transfer. If the transfer fails, the
      driver must set the flag SPI_TRANS_FAIL_IO to
      spi_transfer->error first, before calling
      [`spi_finalize_current_transfer()`](spi.md#c.spi_finalize_current_transfer "spi_finalize_current_transfer").

`handle_err`
:   the subsystem calls the driver to handle an error that occurs
    in the generic implementation of transfer_one_message().

`mem_ops`
:   optimized/dedicated operations for interactions with SPI memory.
    This field is optional and should only be implemented if the
    controller has native support for memory like operations.

`mem_caps`
:   controller capabilities for the handling of memory operations.

`cs_gpiods`
:   Array of GPIO descriptors to use as chip select lines; one per CS
    number. Any individual value may be NULL for CS lines that
    are not GPIOs (driven by the SPI controller itself).

`use_gpio_descriptors`
:   Turns on the code in the SPI core to parse and grab
    GPIO descriptors. This will fill in **cs_gpiods** and SPI devices will have
    the cs_gpiod assigned if a GPIO line is found for the chipselect.

`unused_native_cs`
:   When cs_gpiods is used, [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller") will
    fill in this field with the first unused native CS, to be used by SPI
    controller drivers that need to drive a native CS when using GPIO CS.

`max_native_cs`
:   When cs_gpiods is used, and this field is filled in,
    [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller") will validate all native CS (including the
    unused native CS) against this value.

`pcpu_statistics`
:   statistics for the spi_controller

`dma_tx`
:   DMA transmit channel

`dma_rx`
:   DMA receive channel

`dummy_rx`
:   dummy receive buffer for full-duplex devices

`dummy_tx`
:   dummy transmit buffer for full-duplex devices

`fw_translate_cs`
:   If the boot firmware uses different numbering scheme
    what Linux expects, this optional hook can be used to translate
    between the two.

`ptp_sts_supported`
:   If the driver sets this to true, it must provide a
    time snapshot in **spi_transfer->ptp_sts** as close as possible to the
    moment in time when **spi_transfer->ptp_sts_word_pre** and
    **spi_transfer->ptp_sts_word_post** were transmitted.
    If the driver does not set this, the SPI core takes the snapshot as
    close to the driver hand-over as possible.

`irq_flags`
:   Interrupt enable state during PTP system timestamping

`queue_empty`
:   signal green light for opportunistically skipping the queue
    for spi_sync transfers.

`must_async`
:   disable all fast paths in the core

**Note**

transfer_one and transfer_one_message are mutually
:   exclusive; when both are set, the generic subsystem does
    not call your transfer_one callback.

**Description**

Each SPI controller can communicate with one or more **spi_device**
children. These make a small bus, sharing MOSI, MISO and SCK signals
but not chip select signals. Each device may be configured to use a
different clock rate, since those shared signals are ignored unless
the chip is selected.

The driver for an SPI controller manages access to those devices through
a queue of spi_message transactions, copying data between CPU memory and
an SPI slave device. For each such message it queues, it calls the
message's completion function when the transaction completes.

struct spi_res
:   SPI resource management structure

**Definition**:

```
struct spi_res {
    struct list_head        entry;
    spi_res_release_t release;
    unsigned long long      data[];
};
```

**Members**

`entry`
:   list entry

`release`
:   release code called prior to freeing this resource

`data`
:   extra data allocated for the specific use-case

**Description**

This is based on ideas from devres, but focused on life-cycle
management during spi_message processing.

struct spi_transfer
:   a read/write buffer pair

**Definition**:

```
struct spi_transfer {
    const void      *tx_buf;
    void *rx_buf;
    unsigned len;
#define SPI_TRANS_FAIL_NO_START BIT(0);
#define SPI_TRANS_FAIL_IO       BIT(1);
    u16 error;
    dma_addr_t tx_dma;
    dma_addr_t rx_dma;
    struct sg_table tx_sg;
    struct sg_table rx_sg;
    unsigned dummy_data:1;
    unsigned cs_off:1;
    unsigned cs_change:1;
    unsigned tx_nbits:3;
    unsigned rx_nbits:3;
    unsigned timestamped:1;
#define SPI_NBITS_SINGLE        0x01 ;
#define SPI_NBITS_DUAL          0x02 ;
#define SPI_NBITS_QUAD          0x04 ;
    u8 bits_per_word;
    struct spi_delay        delay;
    struct spi_delay        cs_change_delay;
    struct spi_delay        word_delay;
    u32 speed_hz;
    u32 effective_speed_hz;
    unsigned int    ptp_sts_word_pre;
    unsigned int    ptp_sts_word_post;
    struct ptp_system_timestamp *ptp_sts;
    struct list_head transfer_list;
};
```

**Members**

`tx_buf`
:   data to be written (DMA-safe memory), or NULL

`rx_buf`
:   data to be read (DMA-safe memory), or NULL

`len`
:   size of rx and tx buffers (in bytes)

`error`
:   Error status logged by SPI controller driver.

`tx_dma`
:   DMA address of tx_buf, if **spi_message.is_dma_mapped**

`rx_dma`
:   DMA address of rx_buf, if **spi_message.is_dma_mapped**

`tx_sg`
:   Scatterlist for transmit, currently not for client use

`rx_sg`
:   Scatterlist for receive, currently not for client use

`dummy_data`
:   indicates transfer is dummy bytes transfer.

`cs_off`
:   performs the transfer with chipselect off.

`cs_change`
:   affects chipselect after this transfer completes

`tx_nbits`
:   number of bits used for writing. If 0 the default
    (SPI_NBITS_SINGLE) is used.

`rx_nbits`
:   number of bits used for reading. If 0 the default
    (SPI_NBITS_SINGLE) is used.

`timestamped`
:   true if the transfer has been timestamped

`bits_per_word`
:   select a bits_per_word other than the device default
    for this transfer. If 0 the default (from **spi_device**) is used.

`delay`
:   delay to be introduced after this transfer before
    (optionally) changing the chipselect status, then starting
    the next transfer or completing this **spi_message**.

`cs_change_delay`
:   delay between cs deassert and assert when
    **cs_change** is set and **spi_transfer** is not the last in **spi_message**

`word_delay`
:   inter word delay to be introduced after each word size
    (set by bits_per_word) transmission.

`speed_hz`
:   Select a speed other than the device default for this
    transfer. If 0 the default (from **spi_device**) is used.

`effective_speed_hz`
:   the effective SCK-speed that was used to
    transfer this transfer. Set to 0 if the SPI bus driver does
    not support it.

`ptp_sts_word_pre`
:   The word (subject to bits_per_word semantics) offset
    within **tx_buf** for which the SPI device is requesting that the time
    snapshot for this transfer begins. Upon completing the SPI transfer,
    this value may have changed compared to what was requested, depending
    on the available snapshotting resolution (DMA transfer,
    **ptp_sts_supported** is false, etc).

`ptp_sts_word_post`
:   See **ptp_sts_word_post**. The two can be equal (meaning
    that a single byte should be snapshotted).
    If the core takes care of the timestamp (if **ptp_sts_supported** is false
    for this controller), it will set **ptp_sts_word_pre** to 0, and
    **ptp_sts_word_post** to the length of the transfer. This is done
    purposefully (instead of setting to spi_transfer->len - 1) to denote
    that a transfer-level snapshot taken from within the driver may still
    be of higher quality.

`ptp_sts`
:   Pointer to a memory location held by the SPI slave device where a
    PTP system timestamp structure may lie. If drivers use PIO or their
    hardware has some sort of assist for retrieving exact transfer timing,
    they can (and should) assert **ptp_sts_supported** and populate this
    structure using the ptp_read_system_\*ts helper functions.
    The timestamp must represent the time at which the SPI slave device has
    processed the word, i.e. the "pre" timestamp should be taken before
    transmitting the "pre" word, and the "post" timestamp after receiving
    transmit confirmation from the controller for the "post" word.

`transfer_list`
:   transfers are sequenced through **spi_message.transfers**

**Description**

SPI transfers always write the same number of bytes as they read.
Protocol drivers should always provide **rx_buf** and/or **tx_buf**.
In some cases, they may also want to provide DMA addresses for
the data being transferred; that may reduce overhead, when the
underlying driver uses DMA.

If the transmit buffer is NULL, zeroes will be shifted out
while filling **rx_buf**. If the receive buffer is NULL, the data
shifted in will be discarded. Only "len" bytes shift out (or in).
It's an error to try to shift out a partial word. (For example, by
shifting out three bytes with word size of sixteen or twenty bits;
the former uses two bytes per word, the latter uses four bytes.)

In-memory data values are always in native CPU byte order, translated
from the wire byte order (big-endian except with SPI_LSB_FIRST). So
for example when bits_per_word is sixteen, buffers are 2N bytes long
(**len** = 2N) and hold N sixteen bit words in CPU byte order.

When the word size of the SPI transfer is not a power-of-two multiple
of eight bits, those in-memory words include extra bits. In-memory
words are always seen by protocol drivers as right-justified, so the
undefined (rx) or unused (tx) bits are always the most significant bits.

All SPI transfers start with the relevant chipselect active. Normally
it stays selected until after the last transfer in a message. Drivers
can affect the chipselect signal using cs_change.

(i) If the transfer isn't the last one in the message, this flag is
used to make the chipselect briefly go inactive in the middle of the
message. Toggling chipselect in this way may be needed to terminate
a chip command, letting a single spi_message perform all of group of
chip transactions together.

(ii) When the transfer is the last one in the message, the chip may
stay selected until the next transfer. On multi-device SPI busses
with nothing blocking messages going to other devices, this is just
a performance hint; starting a message to another device deselects
this one. But in other cases, this can be used to ensure correctness.
Some devices need protocol transactions to be built from a series of
spi_message submissions, where the content of one message is determined
by the results of previous messages and where the whole transaction
ends when the chipselect goes inactive.

When SPI can transfer in 1x,2x or 4x. It can get this transfer information
from device through **tx_nbits** and **rx_nbits**. In Bi-direction, these
two should both be set. User can set transfer mode with SPI_NBITS_SINGLE(1x)
SPI_NBITS_DUAL(2x) and SPI_NBITS_QUAD(4x) to support these three transfer.

The code that submits an spi_message (and its spi_transfers)
to the lower layers is responsible for managing its memory.
Zero-initialize every field you don't set up explicitly, to
insulate against future API updates. After you submit a message
and its transfers, ignore them until its completion callback.

struct spi_message
:   one multi-segment SPI transaction

**Definition**:

```
struct spi_message {
    struct list_head        transfers;
    struct spi_device       *spi;
    unsigned is_dma_mapped:1;
    bool prepared;
    int status;
    void (*complete)(void *context);
    void *context;
    unsigned frame_length;
    unsigned actual_length;
    struct list_head        queue;
    void *state;
    struct list_head        resources;
};
```

**Members**

`transfers`
:   list of transfer segments in this transaction

`spi`
:   SPI device to which the transaction is queued

`is_dma_mapped`
:   if true, the caller provided both DMA and CPU virtual
    addresses for each transfer buffer

`prepared`
:   spi_prepare_message was called for the this message

`status`
:   zero for success, else negative errno

`complete`
:   called to report transaction completions

`context`
:   the argument to complete() when it's called

`frame_length`
:   the total number of bytes in the message

`actual_length`
:   the total number of bytes that were transferred in all
    successful segments

`queue`
:   for use by whichever driver currently owns the message

`state`
:   for use by whichever driver currently owns the message

`resources`
:   for resource management when the SPI message is processed

**Description**

A **spi_message** is used to execute an atomic sequence of data transfers,
each represented by a [`struct spi_transfer`](spi.md#c.spi_transfer "spi_transfer"). The sequence is "atomic"
in the sense that no other spi_message may use that SPI bus until that
sequence completes. On some systems, many such sequences can execute as
a single programmed DMA transfer. On all systems, these messages are
queued, and might complete after transactions to other devices. Messages
sent to a given spi_device are always executed in FIFO order.

The code that submits an spi_message (and its spi_transfers)
to the lower layers is responsible for managing its memory.
Zero-initialize every field you don't set up explicitly, to
insulate against future API updates. After you submit a message
and its transfers, ignore them until its completion callback.

void spi_message_init_with_transfers(struct [spi_message](spi.md#c.spi_message "spi_message") \*m, struct [spi_transfer](spi.md#c.spi_transfer "spi_transfer") \*xfers, unsigned int num_xfers)
:   Initialize spi_message and append transfers

**Parameters**

`struct spi_message *m`
:   spi_message to be initialized

`struct spi_transfer *xfers`
:   An array of SPI transfers

`unsigned int num_xfers`
:   Number of items in the xfer array

**Description**

This function initializes the given spi_message and adds each spi_transfer in
the given array to the message.

bool spi_is_bpw_supported(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, u32 bpw)
:   Check if bits per word is supported

**Parameters**

`struct spi_device *spi`
:   SPI device

`u32 bpw`
:   Bits per word

**Description**

This function checks to see if the SPI controller supports **bpw**.

**Return**

True if **bpw** is supported, false otherwise.

unsigned int spi_controller_xfer_timeout(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_transfer](spi.md#c.spi_transfer "spi_transfer") \*xfer)
:   Compute a suitable timeout value

**Parameters**

`struct spi_controller *ctlr`
:   SPI device

`struct spi_transfer *xfer`
:   Transfer descriptor

**Description**

Compute a relevant timeout value for the given transfer. We derive the time
that it would take on a single data line and take twice this amount of time
with a minimum of 500ms to avoid false positives on loaded systems.

**Return**

Transfer timeout value in milliseconds.

struct spi_replaced_transfers
:   structure describing the spi_transfer replacements that have occurred so that they can get reverted

**Definition**:

```
struct spi_replaced_transfers {
    spi_replaced_release_t release;
    void *extradata;
    struct list_head replaced_transfers;
    struct list_head *replaced_after;
    size_t inserted;
    struct spi_transfer inserted_transfers[];
};
```

**Members**

`release`
:   some extra release code to get executed prior to
    releasing this structure

`extradata`
:   pointer to some extra data if requested or NULL

`replaced_transfers`
:   transfers that have been replaced and which need
    to get restored

`replaced_after`
:   the transfer after which the **replaced_transfers**
    are to get re-inserted

`inserted`
:   number of transfers inserted

`inserted_transfers`
:   array of spi_transfers of array-size **inserted**,
    that have been replacing replaced_transfers

**Note**

that **extradata** will point to **inserted_transfers\*\*[\*\*inserted**]
if some extra allocation is requested, so alignment will be the same
as for spi_transfers.

int spi_sync_transfer(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, struct [spi_transfer](spi.md#c.spi_transfer "spi_transfer") \*xfers, unsigned int num_xfers)
:   synchronous SPI data transfer

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`struct spi_transfer *xfers`
:   An array of spi_transfers

`unsigned int num_xfers`
:   Number of items in the xfer array

**Context**

can sleep

**Description**

Does a synchronous SPI data transfer of the given spi_transfer array.

For more specific semantics see [`spi_sync()`](spi.md#c.spi_sync "spi_sync").

**Return**

zero on success, else a negative error code.

int spi_write(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, const void \*buf, size_t len)
:   SPI synchronous write

**Parameters**

`struct spi_device *spi`
:   device to which data will be written

`const void *buf`
:   data buffer

`size_t len`
:   data buffer size

**Context**

can sleep

**Description**

This function writes the buffer **buf**.
Callable only from contexts that can sleep.

**Return**

zero on success, else a negative error code.

int spi_read(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, void \*buf, size_t len)
:   SPI synchronous read

**Parameters**

`struct spi_device *spi`
:   device from which data will be read

`void *buf`
:   data buffer

`size_t len`
:   data buffer size

**Context**

can sleep

**Description**

This function reads the buffer **buf**.
Callable only from contexts that can sleep.

**Return**

zero on success, else a negative error code.

ssize_t spi_w8r8(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, u8 cmd)
:   SPI synchronous 8 bit write followed by 8 bit read

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`u8 cmd`
:   command to be written before data is read back

**Context**

can sleep

**Description**

Callable only from contexts that can sleep.

**Return**

the (unsigned) eight bit number returned by the
device, or else a negative error code.

ssize_t spi_w8r16(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, u8 cmd)
:   SPI synchronous 8 bit write followed by 16 bit read

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`u8 cmd`
:   command to be written before data is read back

**Context**

can sleep

**Description**

The number is returned in wire-order, which is at least sometimes
big-endian.

Callable only from contexts that can sleep.

**Return**

the (unsigned) sixteen bit number returned by the
device, or else a negative error code.

ssize_t spi_w8r16be(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, u8 cmd)
:   SPI synchronous 8 bit write followed by 16 bit big-endian read

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`u8 cmd`
:   command to be written before data is read back

**Context**

can sleep

**Description**

This function is similar to spi_w8r16, with the exception that it will
convert the read 16 bit data word from big-endian to native endianness.

Callable only from contexts that can sleep.

**Return**

the (unsigned) sixteen bit number returned by the device in CPU
endianness, or else a negative error code.

struct spi_board_info
:   board-specific template for a SPI device

**Definition**:

```
struct spi_board_info {
    char modalias[SPI_NAME_SIZE];
    const void      *platform_data;
    const struct software_node *swnode;
    void *controller_data;
    int irq;
    u32 max_speed_hz;
    u16 bus_num;
    u16 chip_select;
    u32 mode;
};
```

**Members**

`modalias`
:   Initializes spi_device.modalias; identifies the driver.

`platform_data`
:   Initializes spi_device.platform_data; the particular
    data stored there is driver-specific.

`swnode`
:   Software node for the device.

`controller_data`
:   Initializes spi_device.controller_data; some
    controllers need hints about hardware setup, e.g. for DMA.

`irq`
:   Initializes spi_device.irq; depends on how the board is wired.

`max_speed_hz`
:   Initializes spi_device.max_speed_hz; based on limits
    from the chip datasheet and board-specific signal quality issues.

`bus_num`
:   Identifies which spi_controller parents the spi_device; unused
    by [`spi_new_device()`](spi.md#c.spi_new_device "spi_new_device"), and otherwise depends on board wiring.

`chip_select`
:   Initializes spi_device.chip_select; depends on how
    the board is wired.

`mode`
:   Initializes spi_device.mode; based on the chip datasheet, board
    wiring (some devices support both 3WIRE and standard modes), and
    possibly presence of an inverter in the chipselect path.

**Description**

When adding new SPI devices to the device tree, these structures serve
as a partial device template. They hold information which can't always
be determined by drivers. Information that probe() can establish (such
as the default transfer wordsize) is not included here.

These structures are used in two places. Their primary role is to
be stored in tables of board-specific device descriptors, which are
declared early in board initialization and then used (much later) to
populate a controller's device tree after the that controller's driver
initializes. A secondary (and atypical) role is as a parameter to
[`spi_new_device()`](spi.md#c.spi_new_device "spi_new_device") call, which happens after those controller drivers
are active in some dynamic board configuration models.

int spi_register_board_info(struct [spi_board_info](spi.md#c.spi_board_info "spi_board_info") const \*info, unsigned n)
:   register SPI devices for a given board

**Parameters**

`struct spi_board_info const *info`
:   array of chip descriptors

`unsigned n`
:   how many descriptors are provided

**Context**

can sleep

**Description**

Board-specific early init code calls this (probably during arch_initcall)
with segments of the SPI device table. Any device nodes are created later,
after the relevant parent SPI controller (bus_num) is defined. We keep
this table of devices forever, so that reloading a controller driver will
not make Linux forget about these hard-wired devices.

Other code can also call this, e.g. a particular add-on board might provide
SPI devices through its expansion connector, so code initializing that board
would naturally declare its SPI devices.

The board info passed can safely be __initdata ... but be careful of
any embedded pointers (platform_data, etc), they're copied as-is.

**Return**

zero on success, else a negative error code.

int __spi_register_driver(struct module \*owner, struct [spi_driver](spi.md#c.spi_driver "spi_driver") \*sdrv)
:   register a SPI driver

**Parameters**

`struct module *owner`
:   owner module of the driver to register

`struct spi_driver *sdrv`
:   the driver to register

**Context**

can sleep

**Return**

zero on success, else a negative error code.

struct [spi_device](spi.md#c.spi_device "spi_device") \*spi_alloc_device(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   Allocate a new SPI device

**Parameters**

`struct spi_controller *ctlr`
:   Controller to which device is connected

**Context**

can sleep

**Description**

Allows a driver to allocate and initialize a spi_device without
registering it immediately. This allows a driver to directly
fill the spi_device with device parameters before calling
[`spi_add_device()`](spi.md#c.spi_add_device "spi_add_device") on it.

Caller is responsible to call [`spi_add_device()`](spi.md#c.spi_add_device "spi_add_device") on the returned
spi_device structure to add it to the SPI controller. If the caller
needs to discard the spi_device without adding it, then it should
call spi_dev_put() on it.

**Return**

a pointer to the new device, or NULL.

int spi_add_device(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi)
:   Add spi_device allocated with spi_alloc_device

**Parameters**

`struct spi_device *spi`
:   spi_device to register

**Description**

Companion function to spi_alloc_device. Devices allocated with
spi_alloc_device can be added onto the SPI bus with this function.

**Return**

0 on success; negative errno on failure

struct [spi_device](spi.md#c.spi_device "spi_device") \*spi_new_device(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_board_info](spi.md#c.spi_board_info "spi_board_info") \*chip)
:   instantiate one new SPI device

**Parameters**

`struct spi_controller *ctlr`
:   Controller to which device is connected

`struct spi_board_info *chip`
:   Describes the SPI device

**Context**

can sleep

**Description**

On typical mainboards, this is purely internal; and it's not needed
after board init creates the hard-wired devices. Some development
platforms may not be able to use spi_register_board_info though, and
this is exported so that for example a USB or parport based adapter
driver could add devices (which it would learn about out-of-band).

**Return**

the new device, or NULL.

void spi_unregister_device(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi)
:   unregister a single SPI device

**Parameters**

`struct spi_device *spi`
:   spi_device to unregister

**Description**

Start making the passed SPI device vanish. Normally this would be handled
by [`spi_unregister_controller()`](spi.md#c.spi_unregister_controller "spi_unregister_controller").

void spi_finalize_current_transfer(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   report completion of a transfer

**Parameters**

`struct spi_controller *ctlr`
:   the controller reporting completion

**Description**

Called by SPI drivers using the core transfer_one_message()
implementation to notify it that the current interrupt driven
transfer has finished and the next one may be scheduled.

void spi_take_timestamp_pre(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_transfer](spi.md#c.spi_transfer "spi_transfer") \*xfer, size_t progress, bool irqs_off)
:   helper to collect the beginning of the TX timestamp

**Parameters**

`struct spi_controller *ctlr`
:   Pointer to the spi_controller structure of the driver

`struct spi_transfer *xfer`
:   Pointer to the transfer being timestamped

`size_t progress`
:   How many words (not bytes) have been transferred so far

`bool irqs_off`
:   If true, will disable IRQs and preemption for the duration of the
    transfer, for less jitter in time measurement. Only compatible
    with PIO drivers. If true, must follow up with
    spi_take_timestamp_post or otherwise system will crash.
    WARNING: for fully predictable results, the CPU frequency must
    also be under control (governor).

**Description**

This is a helper for drivers to collect the beginning of the TX timestamp
for the requested byte from the SPI transfer. The frequency with which this
function must be called (once per word, once for the whole transfer, once
per batch of words etc) is arbitrary as long as the **tx** buffer offset is
greater than or equal to the requested byte at the time of the call. The
timestamp is only taken once, at the first such call. It is assumed that
the driver advances its **tx** buffer pointer monotonically.

void spi_take_timestamp_post(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_transfer](spi.md#c.spi_transfer "spi_transfer") \*xfer, size_t progress, bool irqs_off)
:   helper to collect the end of the TX timestamp

**Parameters**

`struct spi_controller *ctlr`
:   Pointer to the spi_controller structure of the driver

`struct spi_transfer *xfer`
:   Pointer to the transfer being timestamped

`size_t progress`
:   How many words (not bytes) have been transferred so far

`bool irqs_off`
:   If true, will re-enable IRQs and preemption for the local CPU.

**Description**

This is a helper for drivers to collect the end of the TX timestamp for
the requested byte from the SPI transfer. Can be called with an arbitrary
frequency: only the first call where **tx** exceeds or is equal to the
requested word will be timestamped.

struct [spi_message](spi.md#c.spi_message "spi_message") \*spi_get_next_queued_message(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   called by driver to check for queued messages

**Parameters**

`struct spi_controller *ctlr`
:   the controller to check for queued messages

**Description**

If there are more messages in the queue, the next message is returned from
this call.

**Return**

the next message in the queue, else NULL if the queue is empty.

void spi_finalize_current_message(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   the current message is complete

**Parameters**

`struct spi_controller *ctlr`
:   the controller to return the message to

**Description**

Called by the driver to notify the core that the message in the front of the
queue is complete and can be removed from the queue.

struct [spi_device](spi.md#c.spi_device "spi_device") \*spi_new_ancillary_device(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, u8 chip_select)
:   Register ancillary SPI device

**Parameters**

`struct spi_device *spi`
:   Pointer to the main SPI device registering the ancillary device

`u8 chip_select`
:   Chip Select of the ancillary device

**Description**

Register an ancillary SPI device; for example some chips have a chip-select
for normal device usage and another one for setup/firmware upload.

This may only be called from main SPI device's probe routine.

**Return**

0 on success; negative errno on failure

int acpi_spi_count_resources(struct acpi_device \*adev)
:   Count the number of SpiSerialBus resources

**Parameters**

`struct acpi_device *adev`
:   ACPI device

**Return**

the number of SpiSerialBus resources in the ACPI-device's
resource-list; or a negative error code.

struct [spi_device](spi.md#c.spi_device "spi_device") \*acpi_spi_device_alloc(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct acpi_device \*adev, int index)
:   Allocate a spi device, and fill it in with ACPI information

**Parameters**

`struct spi_controller *ctlr`
:   controller to which the spi device belongs

`struct acpi_device *adev`
:   ACPI Device for the spi device

`int index`
:   Index of the spi resource inside the ACPI Node

**Description**

This should be used to allocate a new SPI device from and ACPI Device node.
The caller is responsible for calling spi_add_device to register the SPI device.

If ctlr is set to NULL, the Controller for the SPI device will be looked up
using the resource.
If index is set to -1, index is not used.

**Note**

If index is -1, ctlr must be set.

**Return**

a pointer to the new device, or ERR_PTR on error.

int spi_slave_abort(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi)
:   abort the ongoing transfer request on an SPI slave controller

**Parameters**

`struct spi_device *spi`
:   device used for the current transfer

struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*__spi_alloc_controller(struct [device](infrastructure.md#c.device "device") \*dev, unsigned int size, bool slave)
:   allocate an SPI master or slave controller

**Parameters**

`struct device *dev`
:   the controller, possibly using the platform_bus

`unsigned int size`
:   how much zeroed driver-private data to allocate; the pointer to this
    memory is in the driver_data field of the returned device, accessible
    with spi_controller_get_devdata(); the memory is cacheline aligned;
    drivers granting DMA access to portions of their private data need to
    round up **size** using ALIGN(size, dma_get_cache_alignment()).

`bool slave`
:   flag indicating whether to allocate an SPI master (false) or SPI
    slave (true) controller

**Context**

can sleep

**Description**

This call is used only by SPI controller drivers, which are the
only ones directly touching chip registers. It's how they allocate
an spi_controller structure, prior to calling [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller").

This must be called from context that can sleep.

The caller is responsible for assigning the bus number and initializing the
controller's methods before calling [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller"); and (after
errors adding the device) calling spi_controller_put() to prevent a memory
leak.

**Return**

the SPI controller structure on success, else NULL.

struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*__devm_spi_alloc_controller(struct [device](infrastructure.md#c.device "device") \*dev, unsigned int size, bool slave)
:   resource-managed [`__spi_alloc_controller()`](spi.md#c.__spi_alloc_controller "__spi_alloc_controller")

**Parameters**

`struct device *dev`
:   physical device of SPI controller

`unsigned int size`
:   how much zeroed driver-private data to allocate

`bool slave`
:   whether to allocate an SPI master (false) or SPI slave (true)

**Context**

can sleep

**Description**

Allocate an SPI controller and automatically release a reference on it
when **dev** is unbound from its driver. Drivers are thus relieved from
having to call spi_controller_put().

The arguments to this function are identical to [`__spi_alloc_controller()`](spi.md#c.__spi_alloc_controller "__spi_alloc_controller").

**Return**

the SPI controller structure on success, else NULL.

int spi_register_controller(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   register SPI master or slave controller

**Parameters**

`struct spi_controller *ctlr`
:   initialized master, originally from spi_alloc_master() or
    spi_alloc_slave()

**Context**

can sleep

**Description**

SPI controllers connect to their drivers using some non-SPI bus,
such as the platform bus. The final stage of probe() in that code
includes calling [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller") to hook up to this SPI bus glue.

SPI controllers use board specific (often SOC specific) bus numbers,
and board-specific addressing for SPI devices combines those numbers
with chip select numbers. Since SPI does not directly support dynamic
device identification, boards need configuration tables telling which
chip is at which address.

This must be called from context that can sleep. It returns zero on
success, else a negative error code (dropping the controller's refcount).
After a successful return, the caller is responsible for calling
[`spi_unregister_controller()`](spi.md#c.spi_unregister_controller "spi_unregister_controller").

**Return**

zero on success, else a negative error code.

int devm_spi_register_controller(struct [device](infrastructure.md#c.device "device") \*dev, struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   register managed SPI master or slave controller

**Parameters**

`struct device *dev`
:   device managing SPI controller

`struct spi_controller *ctlr`
:   initialized controller, originally from spi_alloc_master() or
    spi_alloc_slave()

**Context**

can sleep

**Description**

Register a SPI device as with [`spi_register_controller()`](spi.md#c.spi_register_controller "spi_register_controller") which will
automatically be unregistered and freed.

**Return**

zero on success, else a negative error code.

void spi_unregister_controller(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   unregister SPI master or slave controller

**Parameters**

`struct spi_controller *ctlr`
:   the controller being unregistered

**Context**

can sleep

**Description**

This call is used only by SPI controller drivers, which are the
only ones directly touching chip registers.

This must be called from context that can sleep.

Note that this function also drops a reference to the controller.

int spi_split_transfers_maxsize(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_message](spi.md#c.spi_message "spi_message") \*msg, size_t maxsize, gfp_t gfp)
:   split spi transfers into multiple transfers when an individual transfer exceeds a certain size

**Parameters**

`struct spi_controller *ctlr`
:   the **spi_controller** for this transfer

`struct spi_message *msg`
:   the **spi_message** to transform

`size_t maxsize`
:   the maximum when to apply this

`gfp_t gfp`
:   GFP allocation flags

**Return**

status of transformation

int spi_split_transfers_maxwords(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr, struct [spi_message](spi.md#c.spi_message "spi_message") \*msg, size_t maxwords, gfp_t gfp)
:   split SPI transfers into multiple transfers when an individual transfer exceeds a certain number of SPI words

**Parameters**

`struct spi_controller *ctlr`
:   the **spi_controller** for this transfer

`struct spi_message *msg`
:   the **spi_message** to transform

`size_t maxwords`
:   the number of words to limit each transfer to

`gfp_t gfp`
:   GFP allocation flags

**Return**

status of transformation

int spi_setup(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi)
:   setup SPI mode and clock rate

**Parameters**

`struct spi_device *spi`
:   the device whose settings are being modified

**Context**

can sleep, and no requests are queued to the device

**Description**

SPI protocol drivers may need to update the transfer mode if the
device doesn't work with its default. They may likewise need
to update clock rates or word sizes from initial values. This function
changes those settings, and must be called from a context that can sleep.
Except for SPI_CS_HIGH, which takes effect immediately, the changes take
effect the next time the device is selected and data is transferred to
or from it. When this function returns, the SPI device is deselected.

Note that this call will fail if the protocol driver specifies an option
that the underlying controller or its driver does not support. For
example, not all hardware supports wire transfers using nine bit words,
LSB-first wire encoding, or active-high chipselects.

**Return**

zero on success, else a negative error code.

int spi_async(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, struct [spi_message](spi.md#c.spi_message "spi_message") \*message)
:   asynchronous SPI transfer

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`struct spi_message *message`
:   describes the data transfers, including completion callback

**Context**

any (IRQs may be blocked, etc)

**Description**

This call may be used in_irq and other contexts which can't sleep,
as well as from task contexts which can sleep.

The completion callback is invoked in a context which can't sleep.
Before that invocation, the value of message->status is undefined.
When the callback is issued, message->status holds either zero (to
indicate complete success) or a negative error code. After that
callback returns, the driver which issued the transfer request may
deallocate the associated memory; it's no longer in use by any SPI
core or controller driver code.

Note that although all messages to a spi_device are handled in
FIFO order, messages may go to different devices in other orders.
Some device might be higher priority, or have various "hard" access
time requirements, for example.

On detection of any fault during the transfer, processing of
the entire message is aborted, and the device is deselected.
Until returning from the associated message completion callback,
no other spi_message queued to that device will be processed.
(This rule applies equally to all the synchronous transfer calls,
which are wrappers around this core asynchronous primitive.)

**Return**

zero on success, else a negative error code.

int spi_sync(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, struct [spi_message](spi.md#c.spi_message "spi_message") \*message)
:   blocking/synchronous SPI data transfers

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`struct spi_message *message`
:   describes the data transfers

**Context**

can sleep

**Description**

This call may only be used from a context that may sleep. The sleep
is non-interruptible, and has no timeout. Low-overhead controller
drivers may DMA directly into and out of the message buffers.

Note that the SPI device's chip select is active during the message,
and then is normally disabled between messages. Drivers for some
frequently-used devices may want to minimize costs of selecting a chip,
by leaving it selected in anticipation that the next message will go
to the same chip. (That may increase power usage.)

Also, the caller is guaranteeing that the memory associated with the
message will not be freed before this call returns.

**Return**

zero on success, else a negative error code.

int spi_sync_locked(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, struct [spi_message](spi.md#c.spi_message "spi_message") \*message)
:   version of spi_sync with exclusive bus usage

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`struct spi_message *message`
:   describes the data transfers

**Context**

can sleep

**Description**

This call may only be used from a context that may sleep. The sleep
is non-interruptible, and has no timeout. Low-overhead controller
drivers may DMA directly into and out of the message buffers.

This call should be used by drivers that require exclusive access to the
SPI bus. It has to be preceded by a spi_bus_lock call. The SPI bus must
be released by a spi_bus_unlock call when the exclusive access is over.

**Return**

zero on success, else a negative error code.

int spi_bus_lock(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   obtain a lock for exclusive SPI bus usage

**Parameters**

`struct spi_controller *ctlr`
:   SPI bus master that should be locked for exclusive bus access

**Context**

can sleep

**Description**

This call may only be used from a context that may sleep. The sleep
is non-interruptible, and has no timeout.

This call should be used by drivers that require exclusive access to the
SPI bus. The SPI bus must be released by a spi_bus_unlock call when the
exclusive access is over. Data transfer must be done by spi_sync_locked
and spi_async_locked calls when the SPI bus lock is held.

**Return**

always zero.

int spi_bus_unlock(struct [spi_controller](spi.md#c.spi_controller "spi_controller") \*ctlr)
:   release the lock for exclusive SPI bus usage

**Parameters**

`struct spi_controller *ctlr`
:   SPI bus master that was locked for exclusive bus access

**Context**

can sleep

**Description**

This call may only be used from a context that may sleep. The sleep
is non-interruptible, and has no timeout.

This call releases an SPI bus lock previously obtained by an spi_bus_lock
call.

**Return**

always zero.

int spi_write_then_read(struct [spi_device](spi.md#c.spi_device "spi_device") \*spi, const void \*txbuf, unsigned n_tx, void \*rxbuf, unsigned n_rx)
:   SPI synchronous write followed by read

**Parameters**

`struct spi_device *spi`
:   device with which data will be exchanged

`const void *txbuf`
:   data to be written (need not be DMA-safe)

`unsigned n_tx`
:   size of txbuf, in bytes

`void *rxbuf`
:   buffer into which data will be read (need not be DMA-safe)

`unsigned n_rx`
:   size of rxbuf, in bytes

**Context**

can sleep

**Description**

This performs a half duplex MicroWire style transaction with the
device, sending txbuf and then reading rxbuf. The return value
is zero for success, else a negative errno status code.
This call may only be used from a context that may sleep.

Parameters to this routine are always copied using a small buffer.
Performance-sensitive or bulk transfer code should instead use
spi_{async,sync}() calls with DMA-safe buffers.

**Return**

zero on success, else a negative error code.
