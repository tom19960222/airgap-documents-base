---
collection: kernel
version: "6.8"
title: "Parallel Port Devices"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/miscellaneous.html
fetched_at: 2026-08-21T03:30:52+00:00
---
# Parallel Port Devices

parport_register_driver

`parport_register_driver (driver)`

> register a parallel port device driver

**Parameters**

`driver`
:   structure describing the driver

    This can be called by a parallel port device driver in order
    to receive notifications about ports being found in the
    system, as well as ports no longer available.

    If devmodel is true then the new device model is used
    for registration.

    The **driver** structure is allocated by the caller and must not be
    deallocated until after calling [`parport_unregister_driver()`](miscellaneous.md#c.parport_unregister_driver "parport_unregister_driver").

    If using the non device model:
    The driver's attach() function may block. The port that
    attach() is given will be valid for the duration of the
    callback, but if the driver wants to take a copy of the
    pointer it must call [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") to do so. Calling
    parport_register_device() on that port will do this for you.

    The driver's detach() function may block. The port that
    detach() is given will be valid for the duration of the
    callback, but if the driver wants to take a copy of the
    pointer it must call [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") to do so.

    Returns 0 on success. The non device model will always succeeds.
    but the new device model can fail and will return the error code.

module_parport_driver

`module_parport_driver (__parport_driver)`

> Helper macro for registering a modular parport driver

**Parameters**

`__parport_driver`
:   struct parport_driver to be used

**Description**

Helper macro for parport drivers which do not do anything special in module
init and exit. This eliminates a lot of boilerplate. Each module may only
use this macro once, and calling it replaces [`module_init()`](basics.md#c.module_init "module_init") and [`module_exit()`](basics.md#c.module_exit "module_exit").

int parport_yield(struct pardevice \*dev)
:   relinquish a parallel port temporarily

**Parameters**

`struct pardevice *dev`
:   a device on the parallel port

**Description**

This function relinquishes the port if it would be helpful to other
drivers to do so. Afterwards it tries to reclaim the port using
[`parport_claim()`](miscellaneous.md#c.parport_claim "parport_claim"), and the return value is the same as for
[`parport_claim()`](miscellaneous.md#c.parport_claim "parport_claim"). If it fails, the port is left unclaimed and it is
the driver's responsibility to reclaim the port.

The [`parport_yield()`](miscellaneous.md#c.parport_yield "parport_yield") and [`parport_yield_blocking()`](miscellaneous.md#c.parport_yield_blocking "parport_yield_blocking") functions are for
marking points in the driver at which other drivers may claim the
port and use their devices. Yielding the port is similar to
releasing it and reclaiming it, but is more efficient because no
action is taken if there are no other devices needing the port. In
fact, nothing is done even if there are other devices waiting but
the current device is still within its "timeslice". The default
timeslice is half a second, but it can be adjusted via the /proc
interface.

int parport_yield_blocking(struct pardevice \*dev)
:   relinquish a parallel port temporarily

**Parameters**

`struct pardevice *dev`
:   a device on the parallel port

**Description**

This function relinquishes the port if it would be helpful to other
drivers to do so. Afterwards it tries to reclaim the port using
[`parport_claim_or_block()`](miscellaneous.md#c.parport_claim_or_block "parport_claim_or_block"), and the return value is the same as for
[`parport_claim_or_block()`](miscellaneous.md#c.parport_claim_or_block "parport_claim_or_block").

int parport_wait_event(struct parport \*port, signed long timeout)
:   wait for an event on a parallel port

**Parameters**

`struct parport *port`
:   port to wait on

`signed long timeout`
:   time to wait (in jiffies)

    This function waits for up to **timeout** jiffies for an
    interrupt to occur on a parallel port. If the port timeout is
    set to zero, it returns immediately.

    If an interrupt occurs before the timeout period elapses, this
    function returns zero immediately. If it times out, it returns
    one. An error code less than zero indicates an error (most
    likely a pending signal), and the calling code should finish
    what it's doing as soon as it can.

int parport_wait_peripheral(struct parport \*port, unsigned char mask, unsigned char result)
:   wait for status lines to change in 35ms

**Parameters**

`struct parport *port`
:   port to watch

`unsigned char mask`
:   status lines to watch

`unsigned char result`
:   desired values of chosen status lines

    This function waits until the masked status lines have the
    desired values, or until 35ms have elapsed (see IEEE 1284-1994
    page 24 to 25 for why this value in particular is hardcoded).
    The **mask** and **result** parameters are bitmasks, with the bits
    defined by the constants in parport.h: `PARPORT_STATUS_BUSY`,
    and so on.

    The port is polled quickly to start off with, in anticipation
    of a fast response from the peripheral. This fast polling
    time is configurable (using /proc), and defaults to 500usec.
    If the timeout for this port (see [`parport_set_timeout()`](miscellaneous.md#c.parport_set_timeout "parport_set_timeout")) is
    zero, the fast polling time is 35ms, and this function does
    not call schedule().

    If the timeout for this port is non-zero, after the fast
    polling fails it uses [`parport_wait_event()`](miscellaneous.md#c.parport_wait_event "parport_wait_event") to wait for up to
    10ms, waking up if an interrupt occurs.

int parport_negotiate(struct parport \*port, int mode)
:   negotiate an IEEE 1284 mode

**Parameters**

`struct parport *port`
:   port to use

`int mode`
:   mode to negotiate to

    Use this to negotiate to a particular IEEE 1284 transfer mode.
    The **mode** parameter should be one of the constants in
    parport.h starting `IEEE1284_MODE_xxx`.

    The return value is 0 if the peripheral has accepted the
    negotiation to the mode specified, -1 if the peripheral is not
    IEEE 1284 compliant (or not present), or 1 if the peripheral
    has rejected the negotiation.

ssize_t parport_write(struct parport \*port, const void \*buffer, size_t len)
:   write a block of data to a parallel port

**Parameters**

`struct parport *port`
:   port to write to

`const void *buffer`
:   data buffer (in kernel space)

`size_t len`
:   number of bytes of data to transfer

    This will write up to **len** bytes of **buffer** to the port
    specified, using the IEEE 1284 transfer mode most recently
    negotiated to (using [`parport_negotiate()`](miscellaneous.md#c.parport_negotiate "parport_negotiate")), as long as that
    mode supports forward transfers (host to peripheral).

    It is the caller's responsibility to ensure that the first
    **len** bytes of **buffer** are valid.

    This function returns the number of bytes transferred (if zero
    or positive), or else an error code.

ssize_t parport_read(struct parport \*port, void \*buffer, size_t len)
:   read a block of data from a parallel port

**Parameters**

`struct parport *port`
:   port to read from

`void *buffer`
:   data buffer (in kernel space)

`size_t len`
:   number of bytes of data to transfer

    This will read up to **len** bytes of **buffer** to the port
    specified, using the IEEE 1284 transfer mode most recently
    negotiated to (using [`parport_negotiate()`](miscellaneous.md#c.parport_negotiate "parport_negotiate")), as long as that
    mode supports reverse transfers (peripheral to host).

    It is the caller's responsibility to ensure that the first
    **len** bytes of **buffer** are available to write to.

    This function returns the number of bytes transferred (if zero
    or positive), or else an error code.

long parport_set_timeout(struct pardevice \*dev, long inactivity)
:   set the inactivity timeout for a device

**Parameters**

`struct pardevice *dev`
:   device on a port

`long inactivity`
:   inactivity timeout (in jiffies)

    This sets the inactivity timeout for a particular device on a
    port. This affects functions like [`parport_wait_peripheral()`](miscellaneous.md#c.parport_wait_peripheral "parport_wait_peripheral").
    The special value 0 means not to call schedule() while dealing
    with this device.

    The return value is the previous inactivity timeout.

    Any callers of [`parport_wait_event()`](miscellaneous.md#c.parport_wait_event "parport_wait_event") for this device are woken
    up.

int __parport_register_driver(struct parport_driver \*drv, struct module \*owner, const char \*mod_name)
:   register a parallel port device driver

**Parameters**

`struct parport_driver *drv`
:   structure describing the driver

`struct module *owner`
:   owner module of drv

`const char *mod_name`
:   module name string

    This can be called by a parallel port device driver in order
    to receive notifications about ports being found in the
    system, as well as ports no longer available.

    If devmodel is true then the new device model is used
    for registration.

    The **drv** structure is allocated by the caller and must not be
    deallocated until after calling [`parport_unregister_driver()`](miscellaneous.md#c.parport_unregister_driver "parport_unregister_driver").

    If using the non device model:
    The driver's attach() function may block. The port that
    attach() is given will be valid for the duration of the
    callback, but if the driver wants to take a copy of the
    pointer it must call [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") to do so. Calling
    parport_register_device() on that port will do this for you.

    The driver's detach() function may block. The port that
    detach() is given will be valid for the duration of the
    callback, but if the driver wants to take a copy of the
    pointer it must call [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") to do so.

    Returns 0 on success. The non device model will always succeeds.
    but the new device model can fail and will return the error code.

void parport_unregister_driver(struct parport_driver \*drv)
:   deregister a parallel port device driver

**Parameters**

`struct parport_driver *drv`
:   structure describing the driver that was given to
    [`parport_register_driver()`](miscellaneous.md#c.parport_register_driver "parport_register_driver")

    > This should be called by a parallel port device driver that
    > has registered itself using [`parport_register_driver()`](miscellaneous.md#c.parport_register_driver "parport_register_driver") when it
    > is about to be unloaded.
    >
    > When it returns, the driver's attach() routine will no longer
    > be called, and for each port that attach() was called for, the
    > detach() routine will have been called.
    >
    > All the driver's attach() and detach() calls are guaranteed to have
    > finished by the time this function returns.

struct parport \*parport_get_port(struct parport \*port)
:   increment a port's reference count

**Parameters**

`struct parport *port`
:   the port

    This ensures that a struct parport pointer remains valid
    until the matching [`parport_put_port()`](miscellaneous.md#c.parport_put_port "parport_put_port") call.

void parport_put_port(struct parport \*port)
:   decrement a port's reference count

**Parameters**

`struct parport *port`
:   the port

    This should be called once for each call to [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port"),
    once the port is no longer needed. When the reference count reaches
    zero (port is no longer used), free_port is called.

struct parport \*parport_register_port(unsigned long base, int irq, int dma, struct parport_operations \*ops)
:   register a parallel port

**Parameters**

`unsigned long base`
:   base I/O address

`int irq`
:   IRQ line

`int dma`
:   DMA channel

`struct parport_operations *ops`
:   pointer to the port driver's port operations structure

    When a parallel port (lowlevel) driver finds a port that
    should be made available to parallel port device drivers, it
    should call [`parport_register_port()`](miscellaneous.md#c.parport_register_port "parport_register_port"). The **base**, **irq**, and
    **dma** parameters are for the convenience of port drivers, and
    for ports where they aren't meaningful needn't be set to
    anything special. They can be altered afterwards by adjusting
    the relevant members of the parport structure that is returned
    and represents the port. They should not be tampered with
    after calling parport_announce_port, however.

    If there are parallel port device drivers in the system that
    have registered themselves using [`parport_register_driver()`](miscellaneous.md#c.parport_register_driver "parport_register_driver"),
    they are not told about the port at this time; that is done by
    [`parport_announce_port()`](miscellaneous.md#c.parport_announce_port "parport_announce_port").

    The **ops** structure is allocated by the caller, and must not be
    deallocated before calling [`parport_remove_port()`](miscellaneous.md#c.parport_remove_port "parport_remove_port").

    If there is no memory to allocate a new parport structure,
    this function will return `NULL`.

void parport_announce_port(struct parport \*port)
:   tell device drivers about a parallel port

**Parameters**

`struct parport *port`
:   parallel port to announce

    After a port driver has registered a parallel port with
    parport_register_port, and performed any necessary
    initialisation or adjustments, it should call
    [`parport_announce_port()`](miscellaneous.md#c.parport_announce_port "parport_announce_port") in order to notify all device drivers
    that have called [`parport_register_driver()`](miscellaneous.md#c.parport_register_driver "parport_register_driver"). Their attach()
    functions will be called, with **port** as the parameter.

void parport_remove_port(struct parport \*port)
:   deregister a parallel port

**Parameters**

`struct parport *port`
:   parallel port to deregister

    When a parallel port driver is forcibly unloaded, or a
    parallel port becomes inaccessible, the port driver must call
    this function in order to deal with device drivers that still
    want to use it.

    The parport structure associated with the port has its
    operations structure replaced with one containing 'null'
    operations that return errors or just don't do anything.

    Any drivers that have registered themselves using
    [`parport_register_driver()`](miscellaneous.md#c.parport_register_driver "parport_register_driver") are notified that the port is no
    longer accessible by having their detach() routines called
    with **port** as the parameter.

struct pardevice \*parport_register_dev_model(struct parport \*port, const char \*name, const struct pardev_cb \*par_dev_cb, int id)
:   register a device on a parallel port

**Parameters**

`struct parport *port`
:   port to which the device is attached

`const char *name`
:   a name to refer to the device

`const struct pardev_cb *par_dev_cb`
:   struct containing callbacks

`int id`
:   device number to be given to the device

    This function, called by parallel port device drivers,
    declares that a device is connected to a port, and tells the
    system all it needs to know.

    The struct pardev_cb contains pointer to callbacks. preemption
    callback function, **preempt**, is called when this device driver
    has claimed access to the port but another device driver wants
    to use it. It is given, **private**, as its parameter, and should
    return zero if it is willing for the system to release the port
    to another driver on its behalf. If it wants to keep control of
    the port it should return non-zero, and no action will be taken.
    It is good manners for the driver to try to release the port at
    the earliest opportunity after its preemption callback rejects a
    preemption attempt. Note that if a preemption callback is happy
    for preemption to go ahead, there is no need to release the
    port; it is done automatically. This function may not block, as
    it may be called from interrupt context. If the device driver
    does not support preemption, **preempt** can be `NULL`.

    The wake-up ("kick") callback function, **wakeup**, is called when
    the port is available to be claimed for exclusive access; that
    is, [`parport_claim()`](miscellaneous.md#c.parport_claim "parport_claim") is guaranteed to succeed when called from
    inside the wake-up callback function. If the driver wants to
    claim the port it should do so; otherwise, it need not take
    any action. This function may not block, as it may be called
    from interrupt context. If the device driver does not want to
    be explicitly invited to claim the port in this way, **wakeup** can
    be `NULL`.

    The interrupt handler, **irq_func**, is called when an interrupt
    arrives from the parallel port. Note that if a device driver
    wants to use interrupts it should use parport_enable_irq(),
    and can also check the irq member of the parport structure
    representing the port.

    The parallel port (lowlevel) driver is the one that has called
    [`request_irq()`](../core-api/genericirq.md#c.request_irq "request_irq") and whose interrupt handler is called first.
    This handler does whatever needs to be done to the hardware to
    acknowledge the interrupt (for PC-style ports there is nothing
    special to be done). It then tells the IEEE 1284 code about
    the interrupt, which may involve reacting to an IEEE 1284
    event depending on the current IEEE 1284 phase. After this,
    it calls **irq_func**. Needless to say, **irq_func** will be called
    from interrupt context, and may not block.

    The `PARPORT_DEV_EXCL` flag is for preventing port sharing, and
    so should only be used when sharing the port with other device
    drivers is impossible and would lead to incorrect behaviour.
    Use it sparingly! Normally, **flags** will be zero.

    This function returns a pointer to a structure that represents
    the device on the port, or `NULL` if there is not enough memory
    to allocate space for that structure.

void parport_unregister_device(struct pardevice \*dev)
:   deregister a device on a parallel port

**Parameters**

`struct pardevice *dev`
:   pointer to structure representing device

    This undoes the effect of parport_register_device().

struct parport \*parport_find_number(int number)
:   find a parallel port by number

**Parameters**

`int number`
:   parallel port number

    This returns the parallel port with the specified number, or
    `NULL` if there is none.

    There is an implicit [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") done already; to throw
    away the reference to the port that [`parport_find_number()`](miscellaneous.md#c.parport_find_number "parport_find_number")
    gives you, use [`parport_put_port()`](miscellaneous.md#c.parport_put_port "parport_put_port").

struct parport \*parport_find_base(unsigned long base)
:   find a parallel port by base address

**Parameters**

`unsigned long base`
:   base I/O address

    This returns the parallel port with the specified base
    address, or `NULL` if there is none.

    There is an implicit [`parport_get_port()`](miscellaneous.md#c.parport_get_port "parport_get_port") done already; to throw
    away the reference to the port that [`parport_find_base()`](miscellaneous.md#c.parport_find_base "parport_find_base")
    gives you, use [`parport_put_port()`](miscellaneous.md#c.parport_put_port "parport_put_port").

int parport_claim(struct pardevice \*dev)
:   claim access to a parallel port device

**Parameters**

`struct pardevice *dev`
:   pointer to structure representing a device on the port

    This function will not block and so can be used from interrupt
    context. If [`parport_claim()`](miscellaneous.md#c.parport_claim "parport_claim") succeeds in claiming access to
    the port it returns zero and the port is available to use. It
    may fail (returning non-zero) if the port is in use by another
    driver and that driver is not willing to relinquish control of
    the port.

int parport_claim_or_block(struct pardevice \*dev)
:   claim access to a parallel port device

**Parameters**

`struct pardevice *dev`
:   pointer to structure representing a device on the port

    This behaves like [`parport_claim()`](miscellaneous.md#c.parport_claim "parport_claim"), but will block if necessary
    to wait for the port to be free. A return value of 1
    indicates that it slept; 0 means that it succeeded without
    needing to sleep. A negative error code indicates failure.

void parport_release(struct pardevice \*dev)
:   give up access to a parallel port device

**Parameters**

`struct pardevice *dev`
:   pointer to structure representing parallel port device

    This function cannot fail, but it should not be called without
    the port claimed. Similarly, if the port is already claimed
    you should not try claiming it again.

struct pardevice \*parport_open(int devnum, const char \*name)
:   find a device by canonical device number

**Parameters**

`int devnum`
:   canonical device number

`const char *name`
:   name to associate with the device

    This function is similar to parport_register_device(), except
    that it locates a device by its number rather than by the port
    it is attached to.

    All parameters except for **devnum** are the same as for
    parport_register_device(). The return value is the same as
    for parport_register_device().

void parport_close(struct pardevice \*dev)
:   close a device opened with [`parport_open()`](miscellaneous.md#c.parport_open "parport_open")

**Parameters**

`struct pardevice *dev`
:   device to close

    This is to [`parport_open()`](miscellaneous.md#c.parport_open "parport_open") as [`parport_unregister_device()`](miscellaneous.md#c.parport_unregister_device "parport_unregister_device") is to
    parport_register_device().

# 16x50 UART Driver

struct uart_8250_port \*serial8250_get_port(int line)
:   retrieve struct uart_8250_port

**Parameters**

`int line`
:   serial line number

**Description**

This function retrieves struct uart_8250_port for the specific line.
This struct *must* *not* be used to perform a 8250 or serial core operation
which is not accessible otherwise. Its only purpose is to make the struct
accessible to the runtime-pm callbacks for context suspend/restore.
The lock assumption made here is none because runtime-pm suspend/resume
callbacks should not be invoked if there is any operation performed on the
port.

void serial8250_suspend_port(int line)
:   suspend one serial port

**Parameters**

`int line`
:   serial line number

    Suspend one serial port.

void serial8250_resume_port(int line)
:   resume one serial port

**Parameters**

`int line`
:   serial line number

    Resume one serial port.

int serial8250_register_8250_port(const struct uart_8250_port \*up)
:   register a serial port

**Parameters**

`const struct uart_8250_port *up`
:   serial port template

    Configure the serial port specified by the request. If the
    port exists and is in use, it is hung up and unregistered
    first.

    The port is then probed and if necessary the IRQ is autodetected
    If this fails an error is returned.

    On success the port is ready to use and the line number is returned.

void serial8250_unregister_port(int line)
:   remove a 16x50 serial port at runtime

**Parameters**

`int line`
:   serial line number

    Remove one serial port. This may not be called from interrupt
    context. We hand the port back to the our control.

See [Low Level Serial API](serial/driver.md) for related APIs.

# Pulse-Width Modulation (PWM)

Pulse-width modulation is a modulation technique primarily used to
control power supplied to electrical devices.

The PWM framework provides an abstraction for providers and consumers of
PWM signals. A controller that provides one or more PWM signals is
registered as [`struct pwm_chip`](miscellaneous.md#c.pwm_chip "pwm_chip"). Providers
are expected to embed this structure in a driver-specific structure.
This structure contains fields that describe a particular chip.

A chip exposes one or more PWM signal sources, each of which exposed as
a [`struct pwm_device`](miscellaneous.md#c.pwm_device "pwm_device"). Operations can be
performed on PWM devices to control the period, duty cycle, polarity and
active state of the signal.

Note that PWM devices are exclusive resources: they can always only be
used by one consumer at a time.

enum pwm_polarity
:   polarity of a PWM signal

**Constants**

`PWM_POLARITY_NORMAL`
:   a high signal for the duration of the duty-
    cycle, followed by a low signal for the remainder of the pulse
    period

`PWM_POLARITY_INVERSED`
:   a low signal for the duration of the duty-
    cycle, followed by a high signal for the remainder of the pulse
    period

struct pwm_args
:   board-dependent PWM arguments

**Definition**:

```
struct pwm_args {
    u64 period;
    enum pwm_polarity polarity;
};
```

**Members**

`period`
:   reference period

`polarity`
:   reference polarity

**Description**

This structure describes board-dependent arguments attached to a PWM
device. These arguments are usually retrieved from the PWM lookup table or
device tree.

Do not confuse this with the PWM state: PWM arguments represent the initial
configuration that users want to use on this PWM device rather than the
current PWM hardware state.

struct pwm_device
:   PWM channel object

**Definition**:

```
struct pwm_device {
    const char *label;
    unsigned long flags;
    unsigned int hwpwm;
    struct pwm_chip *chip;
    struct pwm_args args;
    struct pwm_state state;
    struct pwm_state last;
};
```

**Members**

`label`
:   name of the PWM device

`flags`
:   flags associated with the PWM device

`hwpwm`
:   per-chip relative index of the PWM device

`chip`
:   PWM chip providing this PWM device

`args`
:   PWM arguments

`state`
:   last applied state

`last`
:   last implemented state (for PWM_DEBUG)

void pwm_get_state(const struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, struct pwm_state \*state)
:   retrieve the current PWM state

**Parameters**

`const struct pwm_device *pwm`
:   PWM device

`struct pwm_state *state`
:   state to fill with the current PWM state

**Description**

The returned PWM state represents the state that was applied by a previous call to
[`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep"). Drivers may have to slightly tweak that state before programming it to
hardware. If [`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep") was never called, this returns either the current hardware
state (if supported) or the default settings.

void pwm_init_state(const struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, struct pwm_state \*state)
:   prepare a new state to be applied with [`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep")

**Parameters**

`const struct pwm_device *pwm`
:   PWM device

`struct pwm_state *state`
:   state to fill with the prepared PWM state

**Description**

This functions prepares a state that can later be tweaked and applied
to the PWM device with [`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep"). This is a convenient function
that first retrieves the current PWM state and the replaces the period
and polarity fields with the reference values defined in pwm->args.
Once the function returns, you can adjust the ->enabled and ->duty_cycle
fields according to your needs before calling [`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep").

->duty_cycle is initially set to zero to avoid cases where the current
->duty_cycle value exceed the pwm_args->period one, which would trigger
an error if the user calls [`pwm_apply_might_sleep()`](miscellaneous.md#c.pwm_apply_might_sleep "pwm_apply_might_sleep") without adjusting ->duty_cycle
first.

unsigned int pwm_get_relative_duty_cycle(const struct pwm_state \*state, unsigned int scale)
:   Get a relative duty cycle value

**Parameters**

`const struct pwm_state *state`
:   PWM state to extract the duty cycle from

`unsigned int scale`
:   target scale of the relative duty cycle

**Description**

This functions converts the absolute duty cycle stored in **state** (expressed
in nanosecond) into a value relative to the period.

For example if you want to get the duty_cycle expressed in percent, call:

pwm_get_state(pwm, `state`);
duty = pwm_get_relative_duty_cycle(`state`, 100);

int pwm_set_relative_duty_cycle(struct pwm_state \*state, unsigned int duty_cycle, unsigned int scale)
:   Set a relative duty cycle value

**Parameters**

`struct pwm_state *state`
:   PWM state to fill

`unsigned int duty_cycle`
:   relative duty cycle value

`unsigned int scale`
:   scale in which **duty_cycle** is expressed

**Description**

This functions converts a relative into an absolute duty cycle (expressed
in nanoseconds), and puts the result in state->duty_cycle.

For example if you want to configure a 50% duty cycle, call:

pwm_init_state(pwm, `state`);
pwm_set_relative_duty_cycle(`state`, 50, 100);
pwm_apply_might_sleep(pwm, `state`);

This functions returns -EINVAL if **duty_cycle** and/or **scale** are
inconsistent (**scale** == 0 or **duty_cycle** > **scale**).

struct pwm_capture
:   PWM capture data

**Definition**:

```
struct pwm_capture {
    unsigned int period;
    unsigned int duty_cycle;
};
```

**Members**

`period`
:   period of the PWM signal (in nanoseconds)

`duty_cycle`
:   duty cycle of the PWM signal (in nanoseconds)

struct pwm_ops
:   PWM controller operations

**Definition**:

```
struct pwm_ops {
    int (*request)(struct pwm_chip *chip, struct pwm_device *pwm);
    void (*free)(struct pwm_chip *chip, struct pwm_device *pwm);
    int (*capture)(struct pwm_chip *chip, struct pwm_device *pwm, struct pwm_capture *result, unsigned long timeout);
    int (*apply)(struct pwm_chip *chip, struct pwm_device *pwm, const struct pwm_state *state);
    int (*get_state)(struct pwm_chip *chip, struct pwm_device *pwm, struct pwm_state *state);
};
```

**Members**

`request`
:   optional hook for requesting a PWM

`free`
:   optional hook for freeing a PWM

`capture`
:   capture and report PWM signal

`apply`
:   atomically apply a new PWM config

`get_state`
:   get the current PWM state. This function is only
    called once per PWM device when the PWM chip is
    registered.

struct pwm_chip
:   abstract a PWM controller

**Definition**:

```
struct pwm_chip {
    struct device *dev;
    const struct pwm_ops *ops;
    struct module *owner;
    unsigned int id;
    unsigned int npwm;
    struct pwm_device * (*of_xlate)(struct pwm_chip *chip, const struct of_phandle_args *args);
    unsigned int of_pwm_n_cells;
    bool atomic;
    struct pwm_device *pwms;
};
```

**Members**

`dev`
:   device providing the PWMs

`ops`
:   callbacks for this PWM controller

`owner`
:   module providing this chip

`id`
:   unique number of this PWM chip

`npwm`
:   number of PWMs controlled by this chip

`of_xlate`
:   request a PWM device given a device tree PWM specifier

`of_pwm_n_cells`
:   number of cells expected in the device tree PWM specifier

`atomic`
:   can the driver's ->apply() be called in atomic context

`pwms`
:   array of PWM devices allocated by the framework

int pwm_config(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, int duty_ns, int period_ns)
:   change a PWM device configuration

**Parameters**

`struct pwm_device *pwm`
:   PWM device

`int duty_ns`
:   "on" time (in nanoseconds)

`int period_ns`
:   duration (in nanoseconds) of one cycle

**Return**

0 on success or a negative error code on failure.

int pwm_enable(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm)
:   start a PWM output toggling

**Parameters**

`struct pwm_device *pwm`
:   PWM device

**Return**

0 on success or a negative error code on failure.

void pwm_disable(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm)
:   stop a PWM output toggling

**Parameters**

`struct pwm_device *pwm`
:   PWM device

bool pwm_might_sleep(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm)
:   is [`pwm_apply_atomic()`](miscellaneous.md#c.pwm_apply_atomic "pwm_apply_atomic") supported?

**Parameters**

`struct pwm_device *pwm`
:   PWM device

**Return**

false if [`pwm_apply_atomic()`](miscellaneous.md#c.pwm_apply_atomic "pwm_apply_atomic") can be called from atomic context.

int __pwmchip_add(struct [pwm_chip](miscellaneous.md#c.pwm_chip "pwm_chip") \*chip, struct module \*owner)
:   register a new PWM chip

**Parameters**

`struct pwm_chip *chip`
:   the PWM chip to add

`struct module *owner`
:   reference to the module providing the chip.

**Description**

Register a new PWM chip. **owner** is supposed to be THIS_MODULE, use the
pwmchip_add wrapper to do this right.

**Return**

0 on success or a negative error code on failure.

void pwmchip_remove(struct [pwm_chip](miscellaneous.md#c.pwm_chip "pwm_chip") \*chip)
:   remove a PWM chip

**Parameters**

`struct pwm_chip *chip`
:   the PWM chip to remove

**Description**

Removes a PWM chip.

struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm_request_from_chip(struct [pwm_chip](miscellaneous.md#c.pwm_chip "pwm_chip") \*chip, unsigned int index, const char \*label)
:   request a PWM device relative to a PWM chip

**Parameters**

`struct pwm_chip *chip`
:   PWM chip

`unsigned int index`
:   per-chip index of the PWM to request

`const char *label`
:   a literal description string of this PWM

**Return**

A pointer to the PWM device at the given index of the given PWM
chip. A negative error code is returned if the index is not valid for the
specified PWM chip or if the PWM device cannot be requested.

int pwm_apply_might_sleep(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, const struct pwm_state \*state)
:   atomically apply a new state to a PWM device Cannot be used in atomic context.

**Parameters**

`struct pwm_device *pwm`
:   PWM device

`const struct pwm_state *state`
:   new state to apply

int pwm_apply_atomic(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, const struct pwm_state \*state)
:   apply a new state to a PWM device from atomic context Not all PWM devices support this function, check with [`pwm_might_sleep()`](miscellaneous.md#c.pwm_might_sleep "pwm_might_sleep").

**Parameters**

`struct pwm_device *pwm`
:   PWM device

`const struct pwm_state *state`
:   new state to apply

int pwm_capture(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm, struct [pwm_capture](miscellaneous.md#c.pwm_capture "pwm_capture") \*result, unsigned long timeout)
:   capture and report a PWM signal

**Parameters**

`struct pwm_device *pwm`
:   PWM device

`struct pwm_capture *result`
:   structure to fill with capture result

`unsigned long timeout`
:   time to wait, in milliseconds, before giving up on capture

**Return**

0 on success or a negative error code on failure.

int pwm_adjust_config(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm)
:   adjust the current PWM config to the PWM arguments

**Parameters**

`struct pwm_device *pwm`
:   PWM device

**Description**

This function will adjust the PWM config to the PWM arguments provided
by the DT or PWM lookup table. This is particularly useful to adapt
the bootloader config to the Linux one.

struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*con_id)
:   look up and request a PWM device

**Parameters**

`struct device *dev`
:   device for PWM consumer

`const char *con_id`
:   consumer name

**Description**

Lookup is first attempted using DT. If the device was not instantiated from
a device tree, a PWM chip and a relative index is looked up via a table
supplied by board setup code (see pwm_add_table()).

Once a PWM chip has been found the specified PWM device will be requested
and is ready to be used.

**Return**

A pointer to the requested PWM device or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR")-encoded
error code on failure.

void pwm_put(struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*pwm)
:   release a PWM device

**Parameters**

`struct pwm_device *pwm`
:   PWM device

struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*devm_pwm_get(struct [device](infrastructure.md#c.device "device") \*dev, const char \*con_id)
:   resource managed [`pwm_get()`](miscellaneous.md#c.pwm_get "pwm_get")

**Parameters**

`struct device *dev`
:   device for PWM consumer

`const char *con_id`
:   consumer name

**Description**

This function performs like [`pwm_get()`](miscellaneous.md#c.pwm_get "pwm_get") but the acquired PWM device will
automatically be released on driver detach.

**Return**

A pointer to the requested PWM device or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR")-encoded
error code on failure.

struct [pwm_device](miscellaneous.md#c.pwm_device "pwm_device") \*devm_fwnode_pwm_get(struct [device](infrastructure.md#c.device "device") \*dev, struct fwnode_handle \*fwnode, const char \*con_id)
:   request a resource managed PWM from firmware node

**Parameters**

`struct device *dev`
:   device for PWM consumer

`struct fwnode_handle *fwnode`
:   firmware node to get the PWM from

`const char *con_id`
:   consumer name

**Description**

Returns the PWM device parsed from the firmware node. See of_pwm_get() and
acpi_pwm_get() for a detailed description.

**Return**

A pointer to the requested PWM device or an [`ERR_PTR()`](../core-api/kernel-api.md#c.ERR_PTR "ERR_PTR")-encoded
error code on failure.
