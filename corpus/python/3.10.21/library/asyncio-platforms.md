---
collection: python
version: "3.10.21"
title: "Platform Support"
source_url: https://docs.python.org/3.10/library/asyncio-platforms.html
fetched_at: 2026-09-17T15:15:32+00:00
---
# Platform Support

The [`asyncio`](asyncio.md#module-asyncio "asyncio: Asynchronous I/O.") module is designed to be portable,
but some platforms have subtle differences and limitations
due to the platforms’ underlying architecture and capabilities.

## All Platforms

- [`loop.add_reader()`](asyncio-eventloop.md#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](asyncio-eventloop.md#asyncio.loop.add_writer "asyncio.loop.add_writer")
  cannot be used to monitor file I/O.

## Windows

**Source code:** [Lib/asyncio/proactor_events.py](https://github.com/python/cpython/tree/3.10/Lib/asyncio/proactor_events.py),
[Lib/asyncio/windows_events.py](https://github.com/python/cpython/tree/3.10/Lib/asyncio/windows_events.py),
[Lib/asyncio/windows_utils.py](https://github.com/python/cpython/tree/3.10/Lib/asyncio/windows_utils.py)

---

Changed in version 3.8: On Windows, [`ProactorEventLoop`](asyncio-eventloop.md#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") is now the default event loop.

All event loops on Windows do not support the following methods:

- [`loop.create_unix_connection()`](asyncio-eventloop.md#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection") and
  [`loop.create_unix_server()`](asyncio-eventloop.md#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server") are not supported.
  The [`socket.AF_UNIX`](socket.md#socket.AF_UNIX "socket.AF_UNIX") socket family is specific to Unix.
- [`loop.add_signal_handler()`](asyncio-eventloop.md#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler") and
  [`loop.remove_signal_handler()`](asyncio-eventloop.md#asyncio.loop.remove_signal_handler "asyncio.loop.remove_signal_handler") are not supported.

[`SelectorEventLoop`](asyncio-eventloop.md#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") has the following limitations:

- [`SelectSelector`](selectors.md#selectors.SelectSelector "selectors.SelectSelector") is used to wait on socket events:
  it supports sockets and is limited to 512 sockets.
- [`loop.add_reader()`](asyncio-eventloop.md#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](asyncio-eventloop.md#asyncio.loop.add_writer "asyncio.loop.add_writer") only accept
  socket handles (e.g. pipe file descriptors are not supported).
- Pipes are not supported, so the [`loop.connect_read_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
  and [`loop.connect_write_pipe()`](asyncio-eventloop.md#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") methods are not implemented.
- [Subprocesses](asyncio-subprocess.md#asyncio-subprocess) are not supported, i.e.
  [`loop.subprocess_exec()`](asyncio-eventloop.md#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") and [`loop.subprocess_shell()`](asyncio-eventloop.md#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
  methods are not implemented.

[`ProactorEventLoop`](asyncio-eventloop.md#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") has the following limitations:

- The [`loop.add_reader()`](asyncio-eventloop.md#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](asyncio-eventloop.md#asyncio.loop.add_writer "asyncio.loop.add_writer")
  methods are not supported.

The resolution of the monotonic clock on Windows is usually around 15.6
msec. The best resolution is 0.5 msec. The resolution depends on the
hardware (availability of [HPET](https://en.wikipedia.org/wiki/High_Precision_Event_Timer)) and on the
Windows configuration.

### Subprocess Support on Windows

On Windows, the default event loop [`ProactorEventLoop`](asyncio-eventloop.md#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") supports
subprocesses, whereas [`SelectorEventLoop`](asyncio-eventloop.md#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") does not.

The [`policy.set_child_watcher()`](asyncio-policy.md#asyncio.AbstractEventLoopPolicy.set_child_watcher "asyncio.AbstractEventLoopPolicy.set_child_watcher") function is also
not supported, as [`ProactorEventLoop`](asyncio-eventloop.md#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") has a different mechanism
to watch child processes.

## macOS

Modern macOS versions are fully supported.

macOS <= 10.8

On macOS 10.6, 10.7 and 10.8, the default event loop
uses [`selectors.KqueueSelector`](selectors.md#selectors.KqueueSelector "selectors.KqueueSelector"), which does not support
character devices on these versions. The [`SelectorEventLoop`](asyncio-eventloop.md#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
can be manually configured to use [`SelectSelector`](selectors.md#selectors.SelectSelector "selectors.SelectSelector")
or [`PollSelector`](selectors.md#selectors.PollSelector "selectors.PollSelector") to support character devices on
these older versions of macOS. Example:

```python3
import asyncio
import selectors

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)
```
