---
collection: qemu
version: "11.1.0"
title: "QTest Device Emulation Testing Framework"
source_url: https://www.qemu.org/docs/master/devel/testing/qtest.html
fetched_at: 2026-08-21T03:25:41+00:00
---
# QTest Device Emulation Testing Framework

- [Qtest Driver Framework](qgraph.md)
  - [QGraph concepts](qgraph.md#qgraph-concepts)
    - [Nodes](qgraph.md#nodes)
    - [Edges](qgraph.md#edges)
    - [Execution steps](qgraph.md#execution-steps)
    - [Command line](qgraph.md#command-line)
    - [Troubleshooting unavailable tests](qgraph.md#troubleshooting-unavailable-tests)
  - [Creating a new driver and its interface](qgraph.md#creating-a-new-driver-and-its-interface)
  - [Adding a new test](qgraph.md#adding-a-new-test)
  - [Qgraph API reference](qgraph.md#qgraph-api-reference)

QTest is a device emulation testing framework. It can be very useful to test
device models; it could also control certain aspects of QEMU (such as virtual
clock stepping), with a special purpose “qtest” protocol. Refer to
[QTest Protocol](qtest.md#qtest-protocol) for more details of the protocol.

QTest cases can be executed with

```
make check-qtest
```

The QTest library is implemented by `tests/qtest/libqtest.c` and the API is
defined in `tests/qtest/libqtest.h`.

Consider adding a new QTest case when you are introducing a new virtual
hardware, or extending one if you are adding functionalities to an existing
virtual device.

On top of libqtest, a higher level library, `libqos`, was created to
encapsulate common tasks of device drivers, such as memory management and
communicating with system buses or devices. Many virtual device tests use
libqos instead of directly calling into libqtest.
Libqos also offers the Qgraph API to increase each test coverage and
automate QEMU command line arguments and devices setup.
Refer to [Qtest Driver Framework](qgraph.md#qgraph) for Qgraph explanation and API.

Steps to add a new QTest case are:

1. Create a new source file for the test. (More than one file can be added as
   necessary.) For example, `tests/qtest/foo-test.c`.
2. Write the test code with the glib and libqtest/libqos API. See also existing
   tests and the library headers for reference.
3. Register the new test in `tests/qtest/meson.build`. Add the test
   executable name to an appropriate `qtests_*` variable. There is
   one variable per architecture, plus `qtests_generic` for tests
   that can be run for all architectures. For example:

   ```
   qtests_generic = [
     ...
     'foo-test',
     ...
   ]
   ```
4. If the test has more than one source file or needs to be linked with any
   dependency other than `qemuutil` and `qos`, list them in the `qtests`
   dictionary. For example a test that needs to use the `QIO` library
   will have an entry like:

   ```
   {
     ...
     'foo-test': [io],
     ...
   }
   ```

Debugging a QTest failure is slightly harder than the unit test because the
tests look up QEMU program names in the environment variables, such as
`QTEST_QEMU_BINARY` and `QTEST_QEMU_IMG`, and also because it is not easy
to attach gdb to the QEMU process spawned from the test. But manual invoking
and using gdb on the test is still simple to do: find out the actual command
from the output of

```
make check-qtest V=1
```

which you can run manually.

## QTest Protocol

Line based protocol, request/response based. Server can send async messages
so clients should always handle many async messages before the response
comes in.

Extra ASCII space characters in command inputs are permitted and ignored.
Lines containing only spaces are permitted and ignored.
Lines that start with a ‘#’ character (comments) are permitted and ignored.

### Valid requests

#### Clock management:

The qtest client is completely in charge of the QEMU_CLOCK_VIRTUAL. qtest commands
let you adjust the value of the clock (monotonically). All the commands
return the current value of the clock in nanoseconds.

If the commands FAIL then time wasn’t advanced which is likely
because the machine was in a paused state or no timer events exist
in the future. This will cause qtest to abort and the test will
need to check its assumptions.

```
> clock_step
< OK VALUE
```

Advance the clock to the next deadline. Useful when waiting for
asynchronous events.

```
> clock_step NS
< OK VALUE
```

Advance the clock by NS nanoseconds.

```
> clock_set NS
< OK VALUE
```

Advance the clock to NS nanoseconds (do nothing if it’s already past).

#### PIO and memory access:

```
> outb ADDR VALUE
< OK
```

```
> outw ADDR VALUE
< OK
```

```
> outl ADDR VALUE
< OK
```

```
> inb ADDR
< OK VALUE
```

```
> inw ADDR
< OK VALUE
```

```
> inl ADDR
< OK VALUE
```

```
> writeb ADDR VALUE
< OK
```

```
> writew ADDR VALUE
< OK
```

```
> writel ADDR VALUE
< OK
```

```
> writeq ADDR VALUE
< OK
```

```
> readb ADDR
< OK VALUE
```

```
> readw ADDR
< OK VALUE
```

```
> readl ADDR
< OK VALUE
```

```
> readq ADDR
< OK VALUE
```

```
> read ADDR SIZE
< OK DATA
```

```
> write ADDR SIZE DATA
< OK
```

```
> b64read ADDR SIZE
< OK B64_DATA
```

```
> b64write ADDR SIZE B64_DATA
< OK
```

```
> memset ADDR SIZE VALUE
< OK
```

ADDR, SIZE, VALUE are all integers parsed with strtoul() with a base of 0.
For ‘memset’ a zero size is permitted and does nothing.

DATA is an arbitrarily long hex number prefixed with ‘0x’. If it’s smaller
than the expected size, the value will be zero filled at the end of the data
sequence.

B64_DATA is an arbitrarily long base64 encoded string.
If the sizes do not match, the data will be truncated.

#### IRQ management:

```
> irq_intercept_in QOM-PATH
< OK
```

```
> irq_intercept_out QOM-PATH
< OK
```

Attach to the gpio-in (resp. gpio-out) pins exported by the device at
QOM-PATH. When the pin is triggered, one of the following async messages
will be printed to the qtest stream:

```
IRQ raise NUM
IRQ lower NUM
```

where NUM is an IRQ number. For the PC, interrupts can be intercepted
simply with “irq_intercept_in ioapic” (note that IRQ0 comes out with
NUM=0 even though it is remapped to GSI 2).

#### Setting interrupt level:

```
> set_irq_in QOM-PATH NAME NUM LEVEL
< OK
```

where NAME is the name of the irq/gpio list, NUM is an IRQ number and
LEVEL is an signed integer IRQ level.

Forcibly set the given interrupt pin to the given level.

## libqtest API reference

QTestState \*qtest_initf(const char \*fmt, ...)

**Parameters**

`const char *fmt`
:   Format for creating other arguments to pass to QEMU, formatted
    like sprintf().

`...`
:   variable arguments

**Description**

Convenience wrapper around qtest_init().

**Return**

`QTestState` instance.

QTestState \*qtest_vinitf(const char \*fmt, va_list ap)

**Parameters**

`const char *fmt`
:   Format for creating other arguments to pass to QEMU, formatted
    like vsprintf().

`va_list ap`
:   Format arguments.

**Description**

Convenience wrapper around qtest_init().

**Return**

`QTestState` instance.

const char \*qtest_qemu_binary(const char \*var)

**Parameters**

`const char *var`
:   environment variable name

**Description**

Look up **var** and return its value as the qemu binary path.
If **var** is NULL, look up the default var name.

QTestState \*qtest_init_after_exec(QTestState \*qts)

**Parameters**

`QTestState *qts`
:   the previous QEMU state

**Description**

Return a test state representing new QEMU after **qts** exec’s it.

gchar \*qtest_qemu_args(const char \*extra_args)

**Parameters**

`const char *extra_args`
:   Other arguments to pass to QEMU.

**Description**

Return the command line used to start QEMU, sans binary.

QTestState \*qtest_init(const char \*extra_args)

**Parameters**

`const char *extra_args`
:   other arguments to pass to QEMU. CAUTION: these
    arguments are subject to word splitting and shell evaluation.

**Return**

`QTestState` instance.

QTestState \*qtest_init_ext(const char \*var, const char \*extra_args, QList \*capabilities, bool do_connect)

**Parameters**

`const char *var`
:   Environment variable from where to take the QEMU binary

`const char *extra_args`
:   Other arguments to pass to QEMU. CAUTION: these
    arguments are subject to word splitting and shell evaluation.

`QList *capabilities`
:   list of QMP capabilities (strings) to enable

`bool do_connect`
:   connect to qemu monitor and qtest socket.

**Description**

Like qtest_init(), but use a different environment variable for the
QEMU binary, allow specify capabilities and skip connecting
to QEMU monitor.

**Return**

`QTestState` instance.

QTestState \*qtest_init_without_qmp_handshake(const char \*extra_args)

**Parameters**

`const char *extra_args`
:   other arguments to pass to QEMU. CAUTION: these
    arguments are subject to word splitting and shell evaluation.

**Return**

`QTestState` instance.

void qtest_connect(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to connect
    Connect to qemu monitor and qtest socket, after skipping them in
    qtest_init_ext. Does not handshake with the monitor.

void qtest_qmp_handshake(QTestState \*s, QList \*capabilities)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`QList *capabilities`
:   list of QMP capabilities (strings) to enable
    Perform handshake after connecting to qemu monitor.

QTestState \*qtest_init_with_serial(const char \*extra_args, int \*sock_fd)

**Parameters**

`const char *extra_args`
:   other arguments to pass to QEMU. CAUTION: these
    arguments are subject to word splitting and shell evaluation.

`int *sock_fd`
:   pointer to store the socket file descriptor for
    connection with serial.

**Return**

`QTestState` instance.

void qtest_system_reset(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Send a “system_reset” command to the QEMU under test, and wait for
the reset to complete before returning.

void qtest_system_reset_nowait(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Send a “system_reset” command to the QEMU under test, but do not
wait for the reset to complete before returning. The caller is
responsible for waiting for either the RESET event or some other
event of interest to them before proceeding.

This function should only be used if you’re specifically testing
for some other event; in that case you can’t use qtest_system_reset()
because it will read and discard any other QMP events that arrive
before the RESET event.

void qtest_wait_qemu(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Wait for the QEMU process to terminate. It is safe to call this function
multiple times.

void qtest_kill_qemu(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Kill the QEMU process and wait for it to terminate. It is safe to call this
function multiple times. Normally qtest_quit() is used instead because it
also frees QTestState. Use qtest_kill_qemu() when you just want to kill QEMU
and qtest_quit() will be called later.

void qtest_quit(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Shut down the QEMU process associated to **s**.

QDict \*qtest_qmp_fds(QTestState \*s, int \*fds, size_t fds_num, const char \*fmt, ...)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`int *fds`
:   array of file descriptors

`size_t fds_num`
:   number of elements in **fds**

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU with fds and returns the response.

QDict \*qtest_qmp(QTestState \*s, const char \*fmt, ...)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU and returns the response.

void qtest_qmp_send(QTestState \*s, const char \*fmt, ...)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU and leaves the response in the stream.

void qtest_qmp_send_raw(QTestState \*s, const char \*fmt, ...)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   text to send, formatted like sprintf()

`...`
:   variable arguments

**Description**

Sends text to the QMP monitor verbatim. Need not be valid JSON;
this is useful for negative tests.

int qtest_socket_server(const char \*socket_path)

**Parameters**

`const char *socket_path`
:   the UNIX domain socket path

**Description**

Create and return a listen socket file descriptor, or abort on failure.

QDict \*qtest_vqmp_fds(QTestState \*s, int \*fds, size_t fds_num, const char \*fmt, va_list ap)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`int *fds`
:   array of file descriptors

`size_t fds_num`
:   number of elements in **fds**

`const char *fmt`
:   QMP message to send to QEMU, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list ap`
:   QMP message arguments

**Description**

Sends a QMP message to QEMU with fds and returns the response.

QDict \*qtest_vqmp(QTestState \*s, const char \*fmt, va_list ap)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   QMP message to send to QEMU, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list ap`
:   QMP message arguments

**Description**

Sends a QMP message to QEMU and returns the response.

void qtest_qmp_vsend_fds(QTestState \*s, int \*fds, size_t fds_num, const char \*fmt, va_list ap)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`int *fds`
:   array of file descriptors

`size_t fds_num`
:   number of elements in **fds**

`const char *fmt`
:   QMP message to send to QEMU, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list ap`
:   QMP message arguments

**Description**

Sends a QMP message to QEMU and leaves the response in the stream.

void qtest_qmp_vsend(QTestState \*s, const char \*fmt, va_list ap)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   QMP message to send to QEMU, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list ap`
:   QMP message arguments

**Description**

Sends a QMP message to QEMU and leaves the response in the stream.

QDict \*qtest_qmp_receive_dict(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Reads a QMP message from QEMU and returns the response.

QDict \*qtest_qmp_receive(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Reads a QMP message from QEMU and returns the response.

If a callback is registered with qtest_qmp_set_event_callback,
it will be invoked for every event seen, otherwise events
will be buffered until a call to one of the qtest_qmp_eventwait
family of functions.

void qtest_qmp_set_event_callback(QTestState \*s, QTestQMPEventCallback cb, void \*opaque)

**Parameters**

`QTestState *s`
:   `QTestSTate` instance to operate on

`QTestQMPEventCallback cb`
:   callback to invoke for events

`void *opaque`
:   data to pass to **cb**

**Description**

Register a callback to be invoked whenever an event arrives

void qtest_qmp_eventwait(QTestState \*s, const char \*event)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *event`
:   event to wait for.

**Description**

Continuously polls for QMP responses until it receives the desired event.

Any callback registered with qtest_qmp_set_event_callback will
be invoked for every event seen.

QDict \*qtest_qmp_eventwait_ref(QTestState \*s, const char \*event)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *event`
:   event to wait for.

**Description**

Continuously polls for QMP responses until it receives the desired event.

Any callback registered with qtest_qmp_set_event_callback will
be invoked for every event seen.

Returns a copy of the event for further investigation.

QDict \*qtest_qmp_event_ref(QTestState \*s, const char \*event)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *event`
:   event to return.

**Description**

Removes non-matching events from the buffer that was set by
qtest_qmp_receive, until an event bearing the given name is found,
and returns it.
If no event matches, clears the buffer and returns NULL.

char \*qtest_hmp(QTestState \*s, const char \*fmt, ...)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   HMP command to send to QEMU, formats arguments like sprintf().

`...`
:   variable arguments

**Description**

Send HMP command to QEMU via QMP’s human-monitor-command.
QMP events are discarded.

**Return**

the command’s output. The caller should g_free() it.

char \*qtest_vhmp(QTestState \*s, const char \*fmt, va_list ap)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *fmt`
:   HMP command to send to QEMU, formats arguments like vsprintf().

`va_list ap`
:   HMP command arguments

**Description**

Send HMP command to QEMU via QMP’s human-monitor-command.
QMP events are discarded.

**Return**

the command’s output. The caller should g_free() it.

void qtest_qom_tests(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Run QOM property get/set round-trip tests on all non-abstract types.

bool qtest_get_irq(QTestState \*s, int num)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`int num`
:   Interrupt to observe.

**Return**

The level of the **num** interrupt.

void qtest_irq_intercept_in(QTestState \*s, const char \*string)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *string`
:   QOM path of a device.

**Description**

Associate qtest irqs with the GPIO-in pins of the device
whose path is specified by **string**.

void qtest_irq_intercept_out(QTestState \*s, const char \*string)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *string`
:   QOM path of a device.

**Description**

Associate qtest irqs with the GPIO-out pins of the device
whose path is specified by **string**.

void qtest_irq_intercept_out_named(QTestState \*s, const char \*qom_path, const char \*name)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *qom_path`
:   QOM path of a device.

`const char *name`
:   Name of the GPIO out pin

**Description**

Associate a qtest irq with the named GPIO-out pin of the device
whose path is specified by **string** and whose name is **name**.

void qtest_set_irq_in(QTestState \*s, const char \*string, const char \*name, int irq, int level)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`const char *string`
:   QOM path of a device

`const char *name`
:   IRQ name

`int irq`
:   IRQ number

`int level`
:   IRQ level

**Description**

Force given device/irq GPIO-in pin to the given level.

void qtest_outb(QTestState \*s, uint16_t addr, uint8_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to write to.

`uint8_t value`
:   Value being written.

**Description**

Write an 8-bit value to an I/O port.

void qtest_outw(QTestState \*s, uint16_t addr, uint16_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to write to.

`uint16_t value`
:   Value being written.

**Description**

Write a 16-bit value to an I/O port.

void qtest_outl(QTestState \*s, uint16_t addr, uint32_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to write to.

`uint32_t value`
:   Value being written.

**Description**

Write a 32-bit value to an I/O port.

uint8_t qtest_inb(QTestState \*s, uint16_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to read from.

**Description**

Returns an 8-bit value from an I/O port.

uint16_t qtest_inw(QTestState \*s, uint16_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to read from.

**Description**

Returns a 16-bit value from an I/O port.

uint32_t qtest_inl(QTestState \*s, uint16_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint16_t addr`
:   I/O port to read from.

**Description**

Returns a 32-bit value from an I/O port.

void qtest_writeb(QTestState \*s, uint64_t addr, uint8_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`uint8_t value`
:   Value being written.

**Description**

Writes an 8-bit value to memory.

void qtest_writew(QTestState \*s, uint64_t addr, uint16_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`uint16_t value`
:   Value being written.

**Description**

Writes a 16-bit value to memory.

void qtest_writel(QTestState \*s, uint64_t addr, uint32_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`uint32_t value`
:   Value being written.

**Description**

Writes a 32-bit value to memory.

void qtest_writeq(QTestState \*s, uint64_t addr, uint64_t value)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`uint64_t value`
:   Value being written.

**Description**

Writes a 64-bit value to memory.

uint8_t qtest_readb(QTestState \*s, uint64_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

**Description**

Reads an 8-bit value from memory.

**Return**

Value read.

uint16_t qtest_readw(QTestState \*s, uint64_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

**Description**

Reads a 16-bit value from memory.

**Return**

Value read.

uint32_t qtest_readl(QTestState \*s, uint64_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

**Description**

Reads a 32-bit value from memory.

**Return**

Value read.

uint64_t qtest_readq(QTestState \*s, uint64_t addr)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

**Description**

Reads a 64-bit value from memory.

**Return**

Value read.

void qtest_memread(QTestState \*s, uint64_t addr, void \*data, size_t size)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

`void *data`
:   Pointer to where memory contents will be stored.

`size_t size`
:   Number of bytes to read.

**Description**

Read guest memory into a buffer.

uint64_t qtest_rtas_call(QTestState \*s, const char \*name, uint32_t nargs, uint64_t args, uint32_t nret, uint64_t ret)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *name`
:   name of the command to call.

`uint32_t nargs`
:   Number of args.

`uint64_t args`
:   Guest address to read args from.

`uint32_t nret`
:   Number of return value.

`uint64_t ret`
:   Guest address to write return values to.

**Description**

Call an RTAS function

uint64_t qtest_csr_call(QTestState \*s, const char \*name, uint64_t cpu, int csr, uint64_t \*val)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`const char *name`
:   name of the command to call.

`uint64_t cpu`
:   hart number.

`int csr`
:   CSR number.

`uint64_t *val`
:   Value for reading/writing.

**Description**

Call an RISC-V CSR read/write function

void qtest_bufread(QTestState \*s, uint64_t addr, void \*data, size_t size)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to read from.

`void *data`
:   Pointer to where memory contents will be stored.

`size_t size`
:   Number of bytes to read.

**Description**

Read guest memory into a buffer and receive using a base64 encoding.

void qtest_memwrite(QTestState \*s, uint64_t addr, const void \*data, size_t size)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`const void *data`
:   Pointer to the bytes that will be written to guest memory.

`size_t size`
:   Number of bytes to write.

**Description**

Write a buffer to guest memory.

void qtest_bufwrite(QTestState \*s, uint64_t addr, const void \*data, size_t size)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`const void *data`
:   Pointer to the bytes that will be written to guest memory.

`size_t size`
:   Number of bytes to write.

**Description**

Write a buffer to guest memory and transmit using a base64 encoding.

void qtest_memset(QTestState \*s, uint64_t addr, uint8_t patt, size_t size)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

`uint64_t addr`
:   Guest address to write to.

`uint8_t patt`
:   Byte pattern to fill the guest memory region with.

`size_t size`
:   Number of bytes to write.

**Description**

Write a pattern to guest memory.

int64_t qtest_clock_step_next(QTestState \*s)

**Parameters**

`QTestState *s`
:   `QTestState` instance to operate on.

**Description**

Advance the QEMU_CLOCK_VIRTUAL to the next deadline.

**Return**

The current value of the QEMU_CLOCK_VIRTUAL in nanoseconds.

int64_t qtest_clock_step(QTestState \*s, int64_t step)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`int64_t step`
:   Number of nanoseconds to advance the clock by.

**Description**

Advance the QEMU_CLOCK_VIRTUAL by **step** nanoseconds.

**Return**

The current value of the QEMU_CLOCK_VIRTUAL in nanoseconds.

int64_t qtest_clock_set(QTestState \*s, int64_t val)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`int64_t val`
:   Nanoseconds value to advance the clock to.

**Description**

Advance the QEMU_CLOCK_VIRTUAL to **val** nanoseconds since the VM was launched.

**Return**

The current value of the QEMU_CLOCK_VIRTUAL in nanoseconds.

bool qtest_big_endian(QTestState \*s)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

**Return**

True if the architecture under test has a big endian configuration.

const char \*qtest_get_arch(void)

**Parameters**

`void`
:   no arguments

**Return**

The architecture for the QEMU executable under test.

bool qtest_has_accel(const char \*accel_name)

**Parameters**

`const char *accel_name`
:   Accelerator name to check for.

**Return**

true if the accelerator is built in.

void qtest_add_func(const char \*str, void (\*fn)(void))

**Parameters**

`const char *str`
:   Test case path.

`void (*fn)(void)`
:   Test case function

**Description**

Add a GTester testcase with the given name and function.
The path is prefixed with the architecture under test, as
returned by qtest_get_arch().

void qtest_add_data_func(const char \*str, const void \*data, void (\*fn)(const void\*))

**Parameters**

`const char *str`
:   Test case path.

`const void *data`
:   Test case data

`void (*fn)(const void *)`
:   Test case function

**Description**

Add a GTester testcase with the given name, data and function.
The path is prefixed with the architecture under test, as
returned by qtest_get_arch().

void qtest_add_data_func_full(const char \*str, void \*data, void (\*fn)(const void\*), GDestroyNotify data_free_func)

**Parameters**

`const char *str`
:   Test case path.

`void *data`
:   Test case data

`void (*fn)(const void *)`
:   Test case function

`GDestroyNotify data_free_func`
:   GDestroyNotify for data

**Description**

Add a GTester testcase with the given name, data and function.
The path is prefixed with the architecture under test, as
returned by qtest_get_arch().

**data** is passed to **data_free_func()** on test completion.

qtest_add

`qtest_add (testpath, Fixture, tdata, fsetup, ftest, fteardown)`

**Parameters**

`testpath`
:   Test case path

`Fixture`
:   Fixture type

`tdata`
:   Test case data

`fsetup`
:   Test case setup function

`ftest`
:   Test case function

`fteardown`
:   Test case teardown function

**Description**

Add a GTester testcase with the given name, data and functions.
The path is prefixed with the architecture under test, as
returned by qtest_get_arch().

void qtest_add_abrt_handler(GHookFunc fn, const void \*data)

**Parameters**

`GHookFunc fn`
:   Handler function

`const void *data`
:   Argument that is passed to the handler

**Description**

Add a handler function that is invoked on SIGABRT. This can be used to
terminate processes and perform other cleanup. The handler can be removed
with qtest_remove_abrt_handler().

void qtest_remove_abrt_handler(void \*data)

**Parameters**

`void *data`
:   Argument previously passed to qtest_add_abrt_handler()

**Description**

Remove an abrt handler that was previously added with
qtest_add_abrt_handler().

QDict \*qtest_vqmp_assert_success_ref(QTestState \*qts, const char \*fmt, va_list args)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list args`
:   variable arguments for **fmt**

**Description**

Sends a QMP message to QEMU, asserts that a ‘return’ key is present in
the response, and returns the response.

void qtest_vqmp_assert_success(QTestState \*qts, const char \*fmt, va_list args)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list args`
:   variable arguments for **fmt**

**Description**

Sends a QMP message to QEMU and asserts that a ‘return’ key is present in
the response.

QDict \*qtest_vqmp_fds_assert_success_ref(QTestState \*qts, int \*fds, size_t nfds, const char \*fmt, va_list args)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`int *fds`
:   the file descriptors to send

`size_t nfds`
:   number of **fds** to send

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list args`
:   variable arguments for **fmt**

**Description**

Sends a QMP message with file descriptors to QEMU,
asserts that a ‘return’ key is present in the response,
and returns the response.

void qtest_vqmp_fds_assert_success(QTestState \*qts, int \*fds, size_t nfds, const char \*fmt, va_list args)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`int *fds`
:   the file descriptors to send

`size_t nfds`
:   number of **fds** to send

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list args`
:   variable arguments for **fmt**

**Description**

Sends a QMP message with file descriptors to QEMU and
asserts that a ‘return’ key is present in the response.

QDict \*qtest_qmp_assert_failure_ref(QTestState \*qts, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU, asserts that an ‘error’ key is present in
the response, and returns the response.

QDict \*qtest_vqmp_assert_failure_ref(QTestState \*qts, const char \*fmt, va_list args)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`va_list args`
:   variable arguments for **fmt**

**Description**

Sends a QMP message to QEMU, asserts that an ‘error’ key is present in
the response, and returns the response.

QDict \*qtest_qmp_assert_success_ref(QTestState \*qts, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU, asserts that a ‘return’ key is present in
the response, and returns the response.

void qtest_qmp_assert_success(QTestState \*qts, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message to QEMU and asserts that a ‘return’ key is present in
the response.

QDict \*qtest_qmp_fds_assert_success_ref(QTestState \*qts, int \*fds, size_t nfds, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`int *fds`
:   the file descriptors to send

`size_t nfds`
:   number of **fds** to send

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message with file descriptors to QEMU,
asserts that a ‘return’ key is present in the response,
and returns the response.

void qtest_qmp_fds_assert_success(QTestState \*qts, int \*fds, size_t nfds, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`int *fds`
:   the file descriptors to send

`size_t nfds`
:   number of **fds** to send

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Sends a QMP message with file descriptors to QEMU and
asserts that a ‘return’ key is present in the response.

void qtest_cb_for_every_machine(void (\*cb)(const char \*machine), bool skip_old_versioned)

**Parameters**

`void (*cb)(const char *machine)`
:   Pointer to the callback function

`bool skip_old_versioned`
:   true if versioned old machine types should be skipped

**Description**

Call a callback function for every name of all available machines.

char \*qtest_resolve_machine_alias(const char \*var, const char \*alias)

**Parameters**

`const char *var`
:   Environment variable from where to take the QEMU binary

`const char *alias`
:   The alias to resolve

**Return**

the machine type corresponding to the alias if any,
otherwise NULL.

bool qtest_has_machine(const char \*machine)

**Parameters**

`const char *machine`
:   The machine to look for

**Return**

true if the machine is available in the target binary.

bool qtest_has_machine_with_env(const char \*var, const char \*machine)

**Parameters**

`const char *var`
:   Environment variable from where to take the QEMU binary

`const char *machine`
:   The machine to look for

**Return**

true if the machine is available in the specified binary.

bool qtest_has_cpu_model(const char \*cpu)

**Parameters**

`const char *cpu`
:   The cpu to look for

**Return**

true if the cpu is available in the target binary.

bool qtest_has_device(const char \*device)

**Parameters**

`const char *device`
:   The device to look for

**Return**

true if the device is available in the target binary.

void qtest_qmp_device_add_qdict(QTestState \*qts, const char \*drv, const QDict \*arguments)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *drv`
:   Name of the device that should be added

`const QDict *arguments`
:   QDict with properties for the device to initialize

**Description**

Generic hot-plugging test via the device_add QMP command with properties
supplied in form of QDict. Use NULL for empty properties list.

void qtest_qmp_device_add(QTestState \*qts, const char \*driver, const char \*id, const char \*fmt, ...)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *driver`
:   Name of the device that should be added

`const char *id`
:   Identification string

`const char *fmt`
:   QMP message to send to qemu, formatted like
    qobject_from_jsonf_nofail(). See parse_interpolation() for what’s
    supported after ‘%’.

`...`
:   variable arguments

**Description**

Generic hot-plugging test via the device_add QMP command.

void qtest_qmp_add_client(QTestState \*qts, const char \*protocol, int fd)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *protocol`
:   the protocol to add to

`int fd`
:   the client file-descriptor

**Description**

Call QMP `getfd` (on Windows `get-win32-socket`) followed by
`add_client` with the given **fd**.

void qtest_qmp_device_del_send(QTestState \*qts, const char \*id)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *id`
:   Identification string

**Description**

Generic hot-unplugging test via the device_del QMP command.

void qtest_qmp_device_del(QTestState \*qts, const char \*id)

**Parameters**

`QTestState *qts`
:   QTestState instance to operate on

`const char *id`
:   Identification string

**Description**

Generic hot-unplugging test via the device_del QMP command.
Waiting for command completion event.

bool qtest_probe_child(QTestState \*s)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

**Return**

true if the child is still alive.

void qtest_set_expected_status(QTestState \*s, int status)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`int status`
:   an expected exit status.

**Description**

Set expected exit status of the child.

void qtest_qom_set_bool(QTestState \*s, const char \*path, const char \*property, bool value)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`const char *path`
:   Path to the property being set.

`const char *property`
:   Property being set.

`bool value`
:   Value to set the property.

**Description**

Set the property with passed in value.

bool qtest_qom_get_bool(QTestState \*s, const char \*path, const char \*property)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

`const char *path`
:   Path to the property being retrieved.

`const char *property`
:   Property from where the value is being retrieved.

**Return**

Value retrieved from property.

pid_t qtest_pid(QTestState \*s)

**Parameters**

`QTestState *s`
:   QTestState instance to operate on.

**Return**

the PID of the QEMU process, or <= 0

bool have_qemu_img(void)

**Parameters**

`void`
:   no arguments

**Return**

true if “qemu-img” is available.

bool mkimg(const char \*file, const char \*fmt, unsigned size_mb)

**Parameters**

`const char *file`
:   File name of the image that should be created

`const char *fmt`
:   Format, e.g. “qcow2” or “raw”

`unsigned size_mb`
:   Size of the image in megabytes

**Description**

Create a disk image with qemu-img. Note that the QTEST_QEMU_IMG
environment variable must point to the qemu-img file.

**Return**

true if the image has been created successfully.

bool qtest_verbose(const char \*domain)

**Parameters**

`const char *domain`
:   The logging domain

**Description**

Read the QTEST_LOG environment variable and return whether the
specified domain is enabled for verbose logging. Enable specific
logging domains with QTEST_LOG=<domain> or use QTEST_LOG=-<domain> to
enable all domains except for the specific one.

## QTest valid environment variables

A few environment variables are used to point QTest at artifacts to be
used in the tests, mostly QEMU binaries or to control the behavior of
the tests. Environment variables are set automatically by the build
system, but it can be useful to alter them when running tests
manually. The following are the environment variables recognized by
QTest, not including test-specific ones:

`QTEST_QEMU_BINARY`
:   The QEMU binary itself (generally a `qemu-system-<arch>` binary).

`QTEST_QEMU_ARGS`
:   Extra arguments for the QEMU command line.

`QTEST_QEMU_IMG`
:   The `qemu-img` binary.

`QTEST_QEMU_STORAGE_DAEMON_BINARY`
:   The `qemu-storage-daemon` binary.

`QTEST_STOP`
:   Instruct QTest to stop the QEMU process with SIGSTOP before continuing
    execution.

`QTEST_LOG`
:   Comma-separated list of log domains to allow verbose logging.
    The currently-defined log domains are:

    `qmp`
    :   controls verbose output of QMP command invocations.

    `qtest`
    :   controls verbose output of QTest operations.

    `test`
    :   controls verbose output of tests.

    A dash `-` used in front of a log domain name has the effect
    of enabling verbose logging for all other domains while
    keeping it disabled for the specified domain.
