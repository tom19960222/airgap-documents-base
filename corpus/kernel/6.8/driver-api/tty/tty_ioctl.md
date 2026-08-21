---
collection: kernel
version: "6.8"
title: "TTY IOCTL Helpers"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/tty/tty_ioctl.html
fetched_at: 2026-08-21T03:40:20+00:00
---
# TTY IOCTL Helpers

unsigned int tty_chars_in_buffer(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   characters pending

**Parameters**

`struct tty_struct *tty`
:   terminal

**Return**

the number of bytes of data in the device private output queue. If
no private method is supplied there is assumed to be no queue on the device.

unsigned int tty_write_room(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   write queue space

**Parameters**

`struct tty_struct *tty`
:   terminal

**Return**

the number of bytes that can be queued to this device at the present
time. The result should be treated as a guarantee and the driver cannot
offer a value it later shrinks by more than the number of bytes written. If
no method is provided, 2K is always returned and data may be lost as there
will be no flow control.

void tty_driver_flush_buffer(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   discard internal buffer

**Parameters**

`struct tty_struct *tty`
:   terminal

**Description**

Discard the internal output buffer for this device. If no method is provided,
then either the buffer cannot be hardware flushed or there is no buffer
driver side.

void tty_unthrottle(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   flow control

**Parameters**

`struct tty_struct *tty`
:   terminal

**Description**

Indicate that a **tty** may continue transmitting data down the stack. Takes
the [`tty_struct->termios_rwsem`](tty_struct.md#c.tty_struct "tty_struct") to protect against parallel
throttle/unthrottle and also to ensure the driver can consistently reference
its own termios data at this point when implementing software flow control.

Drivers should however remember that the stack can issue a throttle, then
change flow control method, then unthrottle.

bool tty_throttle_safe(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   flow control

**Parameters**

`struct tty_struct *tty`
:   terminal

**Description**

Indicate that a **tty** should stop transmitting data down the stack.
[`tty_throttle_safe()`](tty_ioctl.md#c.tty_throttle_safe "tty_throttle_safe") will only attempt throttle if **tty->flow_change** is
`TTY_THROTTLE_SAFE`. Prevents an accidental throttle due to race conditions
when throttling is conditional on factors evaluated prior to throttling.

**Return**

`true` if **tty** is throttled (or was already throttled)

bool tty_unthrottle_safe(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   flow control

**Parameters**

`struct tty_struct *tty`
:   terminal

**Description**

Similar to [`tty_unthrottle()`](tty_ioctl.md#c.tty_unthrottle "tty_unthrottle") but will only attempt unthrottle if
**tty->flow_change** is `TTY_UNTHROTTLE_SAFE`. Prevents an accidental unthrottle
due to race conditions when unthrottling is conditional on factors evaluated
prior to unthrottling.

**Return**

`true` if **tty** is unthrottled (or was already unthrottled)

void tty_wait_until_sent(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, long timeout)
:   wait for I/O to finish

**Parameters**

`struct tty_struct *tty`
:   tty we are waiting for

`long timeout`
:   how long we will wait

**Description**

Wait for characters pending in a tty driver to hit the wire, or for a
timeout to occur (eg due to flow control).

Locking: none

void tty_termios_copy_hw(struct ktermios \*new, const struct ktermios \*old)
:   copy hardware settings

**Parameters**

`struct ktermios *new`
:   new termios

`const struct ktermios *old`
:   old termios

**Description**

Propagate the hardware specific terminal setting bits from the **old** termios
structure to the **new** one. This is used in cases where the hardware does not
support reconfiguration or as a helper in some cases where only minimal
reconfiguration is supported.

bool tty_termios_hw_change(const struct ktermios \*a, const struct ktermios \*b)
:   check for setting change

**Parameters**

`const struct ktermios *a`
:   termios

`const struct ktermios *b`
:   termios to compare

**Description**

Check if any of the bits that affect a dumb device have changed between the
two termios structures, or a speed change is needed.

**Return**

`true` if change is needed

unsigned char tty_get_char_size(unsigned int cflag)
:   get size of a character

**Parameters**

`unsigned int cflag`
:   termios cflag value

**Return**

size (in bits) of a character depending on **cflag**'s `CSIZE` setting

unsigned char tty_get_frame_size(unsigned int cflag)
:   get size of a frame

**Parameters**

`unsigned int cflag`
:   termios cflag value

**Description**

Get the size (in bits) of a frame depending on **cflag**'s `CSIZE`, `CSTOPB`, and
`PARENB` setting. The result is a sum of character size, start and stop bits
-- one bit each -- second stop bit (if set), and parity bit (if set).

**Return**

size (in bits) of a frame depending on **cflag**'s setting.

int tty_set_termios(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, struct ktermios \*new_termios)
:   update termios values

**Parameters**

`struct tty_struct *tty`
:   tty to update

`struct ktermios *new_termios`
:   desired new value

**Description**

Perform updates to the termios values set on this **tty**. A master pty's
termios should never be set.

Locking: [`tty_struct->termios_rwsem`](tty_struct.md#c.tty_struct "tty_struct")

int set_termios(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, void __user \*arg, int opt)
:   set termios values for a tty

**Parameters**

`struct tty_struct *tty`
:   terminal device

`void __user *arg`
:   user data

`int opt`
:   option information

**Description**

Helper function to prepare termios data and run necessary other functions
before using [`tty_set_termios()`](tty_ioctl.md#c.tty_set_termios "tty_set_termios") to do the actual changes.

Locking: called functions take [`tty_struct->ldisc_sem`](tty_struct.md#c.tty_struct "tty_struct") and
[`tty_struct->termios_rwsem`](tty_struct.md#c.tty_struct "tty_struct") locks

**Return**

0 on success, an error otherwise

int set_sgttyb(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, struct [sgttyb](tty_ioctl.md#c.set_sgttyb "sgttyb") __user \*sgttyb)
:   set legacy terminal values

**Parameters**

`struct tty_struct *tty`
:   tty structure

`struct sgttyb __user *sgttyb`
:   pointer to old style terminal structure

**Description**

Updates a terminal from the legacy BSD style terminal information structure.

Locking: [`tty_struct->termios_rwsem`](tty_struct.md#c.tty_struct "tty_struct")

**Return**

0 on success, an error otherwise

int tty_change_softcar(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, bool enable)
:   carrier change ioctl helper

**Parameters**

`struct tty_struct *tty`
:   tty to update

`bool enable`
:   enable/disable `CLOCAL`

**Description**

Perform a change to the `CLOCAL` state and call into the driver layer to make
it visible.

Locking: [`tty_struct->termios_rwsem`](tty_struct.md#c.tty_struct "tty_struct").

**Return**

0 on success, an error otherwise

int tty_mode_ioctl(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, unsigned int cmd, unsigned long arg)
:   mode related ioctls

**Parameters**

`struct tty_struct *tty`
:   tty for the ioctl

`unsigned int cmd`
:   command

`unsigned long arg`
:   ioctl argument

**Description**

Perform non-line discipline specific mode control ioctls. This is designed
to be called by line disciplines to ensure they provide consistent mode
setting.

speed_t tty_get_baud_rate(const struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty)
:   get tty bit rates

**Parameters**

`const struct tty_struct *tty`
:   tty to query

**Return**

the baud rate as an integer for this terminal

**Description**

Locking: The termios lock must be held by the caller.
