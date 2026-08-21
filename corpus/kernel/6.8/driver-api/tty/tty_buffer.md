---
collection: kernel
version: "6.8"
title: "TTY Buffer"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/tty/tty_buffer.html
fetched_at: 2026-08-21T03:38:28+00:00
---
# TTY Buffer

- [Flip Buffer Management](tty_buffer.md#flip-buffer-management)
- [Other Functions](tty_buffer.md#other-functions)
- [Buffer Locking](tty_buffer.md#buffer-locking)
- [Internal Functions](tty_buffer.md#internal-functions)

Here, we document functions for taking care of tty buffer and their flipping.
Drivers are supposed to fill the buffer by one of those functions below and
then flip the buffer, so that the data are passed to [line discipline](tty_ldisc.md) for further processing.

## [Flip Buffer Management](tty_buffer.md#id1)

size_t tty_prepare_flip_string(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, u8 \*\*chars, size_t size)
:   make room for characters

**Parameters**

`struct tty_port *port`
:   tty port

`u8 **chars`
:   return pointer for character write area

`size_t size`
:   desired size

**Description**

Prepare a block of space in the buffer for data.

This is used for drivers that need their own block copy routines into the
buffer. There is no guarantee the buffer is a DMA target!

**Return**

the length available and buffer pointer (**chars**) to the space which
is now allocated and accounted for as ready for normal characters.

size_t tty_ldisc_receive_buf(struct tty_ldisc \*ld, const u8 \*p, const u8 \*f, size_t count)
:   forward data to line discipline

**Parameters**

`struct tty_ldisc *ld`
:   line discipline to process input

`const u8 *p`
:   char buffer

`const u8 *f`
:   `TTY_NORMAL`, `TTY_BREAK`, etc. flags buffer

`size_t count`
:   number of bytes to process

**Description**

Callers other than [`flush_to_ldisc()`](tty_buffer.md#c.flush_to_ldisc "flush_to_ldisc") need to exclude the kworker from
concurrent use of the line discipline, see paste_selection().

**Return**

the number of bytes processed.

void tty_flip_buffer_push(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   push terminal buffers

**Parameters**

`struct tty_port *port`
:   tty port to push

**Description**

Queue a push of the terminal flip buffers to the line discipline. Can be
called from IRQ/atomic context.

In the event of the queue being busy for flipping the work will be held off
and retried later.

size_t tty_insert_flip_string_fixed_flag(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, const u8 \*chars, u8 flag, size_t size)
:   add characters to the tty buffer

**Parameters**

`struct tty_port *port`
:   tty port

`const u8 *chars`
:   characters

`u8 flag`
:   flag value for each character

`size_t size`
:   size

**Description**

Queue a series of bytes to the tty buffering. All the characters passed are
marked with the supplied flag.

**Return**

the number added.

size_t tty_insert_flip_string_flags(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, const u8 \*chars, const u8 \*flags, size_t size)
:   add characters to the tty buffer

**Parameters**

`struct tty_port *port`
:   tty port

`const u8 *chars`
:   characters

`const u8 *flags`
:   flag bytes

`size_t size`
:   size

**Description**

Queue a series of bytes to the tty buffering. For each character the flags
array indicates the status of the character.

**Return**

the number added.

size_t tty_insert_flip_char(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, u8 ch, u8 flag)
:   add one character to the tty buffer

**Parameters**

`struct tty_port *port`
:   tty port

`u8 ch`
:   character

`u8 flag`
:   flag byte

**Description**

Queue a single byte **ch** to the tty buffering, with an optional flag.

---

## [Other Functions](tty_buffer.md#id2)

unsigned int tty_buffer_space_avail(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   return unused buffer space

**Parameters**

`struct tty_port *port`
:   tty port owning the flip buffer

**Return**

the # of bytes which can be written by the driver without reaching
the buffer limit.

**Note**

this does not guarantee that memory is available to write the returned
# of bytes (use [`tty_prepare_flip_string()`](tty_buffer.md#c.tty_prepare_flip_string "tty_prepare_flip_string") to pre-allocate if memory
guarantee is required).

int tty_buffer_set_limit(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, int limit)
:   change the tty buffer memory limit

**Parameters**

`struct tty_port *port`
:   tty port to change

`int limit`
:   memory limit to set

**Description**

Change the tty buffer memory limit.

Must be called before the other tty buffer functions are used.

---

## [Buffer Locking](tty_buffer.md#id3)

These are used only in special circumstances. Avoid them.

void tty_buffer_lock_exclusive(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   gain exclusive access to buffer

**Parameters**

`struct tty_port *port`
:   tty port owning the flip buffer

**Description**

Guarantees safe use of the [`tty_ldisc_ops.receive_buf()`](tty_ldisc.md#c.tty_ldisc_ops "tty_ldisc_ops") method by excluding
the buffer work and any pending flush from using the flip buffer. Data can
continue to be added concurrently to the flip buffer from the driver side.

See also [`tty_buffer_unlock_exclusive()`](tty_buffer.md#c.tty_buffer_unlock_exclusive "tty_buffer_unlock_exclusive").

void tty_buffer_unlock_exclusive(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   release exclusive access

**Parameters**

`struct tty_port *port`
:   tty port owning the flip buffer

**Description**

The buffer work is restarted if there is data in the flip buffer.

See also [`tty_buffer_lock_exclusive()`](tty_buffer.md#c.tty_buffer_lock_exclusive "tty_buffer_lock_exclusive").

---

## [Internal Functions](tty_buffer.md#id4)

void tty_buffer_free_all(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   free buffers used by a tty

**Parameters**

`struct tty_port *port`
:   tty port to free from

**Description**

Remove all the buffers pending on a tty whether queued with data or in the
free ring. Must be called when the tty is no longer in use.

struct tty_buffer \*tty_buffer_alloc(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, size_t size)
:   allocate a tty buffer

**Parameters**

`struct tty_port *port`
:   tty port

`size_t size`
:   desired size (characters)

**Description**

Allocate a new tty buffer to hold the desired number of characters. We
round our buffers off in 256 character chunks to get better allocation
behaviour.

**Return**

`NULL` if out of memory or the allocation would exceed the per
device queue.

void tty_buffer_free(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, struct tty_buffer \*b)
:   free a tty buffer

**Parameters**

`struct tty_port *port`
:   tty port owning the buffer

`struct tty_buffer *b`
:   the buffer to free

**Description**

Free a tty buffer, or add it to the free list according to our internal
strategy.

void tty_buffer_flush(struct [tty_struct](tty_struct.md#c.tty_struct "tty_struct") \*tty, struct tty_ldisc \*ld)
:   flush full tty buffers

**Parameters**

`struct tty_struct *tty`
:   tty to flush

`struct tty_ldisc *ld`
:   optional ldisc ptr (must be referenced)

**Description**

Flush all the buffers containing receive data. If **ld** != `NULL`, flush the
ldisc input buffer.

Locking: takes buffer lock to ensure single-threaded flip buffer 'consumer'.

int __tty_buffer_request_room(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, size_t size, bool flags)
:   grow tty buffer if needed

**Parameters**

`struct tty_port *port`
:   tty port

`size_t size`
:   size desired

`bool flags`
:   buffer has to store flags along character data

**Description**

Make at least **size** bytes of linear space available for the tty buffer.

Will change over to a new buffer if the current buffer is encoded as
`TTY_NORMAL` (so has no flags buffer) and the new buffer requires a flags
buffer.

**Return**

the size we managed to find.

void flush_to_ldisc(struct work_struct \*work)
:   flush data from buffer to ldisc

**Parameters**

`struct work_struct *work`
:   tty structure passed from work queue.

**Description**

This routine is called out of the software interrupt to flush data from the
buffer chain to the line discipline.

The receive_buf() method is single threaded for each tty instance.

Locking: takes buffer lock to ensure single-threaded flip buffer 'consumer'.

int tty_insert_flip_string_and_push_buffer(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port, const u8 \*chars, size_t size)
:   add characters to the tty buffer and push

**Parameters**

`struct tty_port *port`
:   tty port

`const u8 *chars`
:   characters

`size_t size`
:   size

**Description**

The function combines tty_insert_flip_string() and [`tty_flip_buffer_push()`](tty_buffer.md#c.tty_flip_buffer_push "tty_flip_buffer_push")
with the exception of properly holding the **port->lock**.

To be used only internally (by pty currently).

**Return**

the number added.

void tty_buffer_init(struct [tty_port](tty_port.md#c.tty_port "tty_port") \*port)
:   prepare a tty buffer structure

**Parameters**

`struct tty_port *port`
:   tty port to initialise

**Description**

Set up the initial state of the buffer management for a tty device. Must be
called before the other tty buffer functions are used.
