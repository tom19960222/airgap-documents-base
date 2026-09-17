---
collection: python
version: "3.12.14"
title: "asyncio — Asynchronous I/O"
source_url: https://docs.python.org/3.12/library/asyncio.html
fetched_at: 2026-09-17T15:33:37+00:00
---
# `asyncio` — Asynchronous I/O

---

Hello World!

```python3
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

asyncio.run(main())
```

asyncio is a library to write **concurrent** code using
the **async/await** syntax.

asyncio is used as a foundation for multiple Python asynchronous
frameworks that provide high-performance network and web-servers,
database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level
**structured** network code.

asyncio provides a set of **high-level** APIs to:

- [run Python coroutines](asyncio-task.md#coroutine) concurrently and
  have full control over their execution;
- perform [network IO and IPC](asyncio-stream.md#asyncio-streams);
- control [subprocesses](asyncio-subprocess.md#asyncio-subprocess);
- distribute tasks via [queues](asyncio-queue.md#asyncio-queues);
- [synchronize](asyncio-sync.md#asyncio-sync) concurrent code;

Additionally, there are **low-level** APIs for
*library and framework developers* to:

- create and manage [event loops](asyncio-eventloop.md#asyncio-event-loop), which
  provide asynchronous APIs for [networking](asyncio-eventloop.md#loop-create-server),
  running [subprocesses](asyncio-eventloop.md#loop-subprocess-exec),
  handling [OS signals](asyncio-eventloop.md#loop-add-signal-handler), etc;
- implement efficient protocols using
  [transports](asyncio-protocol.md#asyncio-transports-protocols);
- [bridge](asyncio-future.md#asyncio-futures) callback-based libraries and code
  with async/await syntax.

[Availability](intro.md#availability): not Emscripten, not WASI.

This module does not work or is not available on WebAssembly platforms
`wasm32-emscripten` and `wasm32-wasi`. See
[WebAssembly platforms](intro.md#wasm-availability) for more information.

asyncio REPL

You can experiment with an `asyncio` concurrent context in the REPL:

```pycon
$ python -m asyncio
asyncio REPL ...
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> await asyncio.sleep(10, result='hello')
'hello'
```

Raises an [auditing event](sys.md#auditing) `cpython.run_stdin` with no arguments.

Changed in version 3.12.5: (also 3.11.10, 3.10.15, 3.9.20, and 3.8.20)
Emits audit events.

Reference

High-level APIs

- [Runners](asyncio-runner.md)
- [Coroutines and Tasks](asyncio-task.md)
- [Streams](asyncio-stream.md)
- [Synchronization Primitives](asyncio-sync.md)
- [Subprocesses](asyncio-subprocess.md)
- [Queues](asyncio-queue.md)
- [Exceptions](asyncio-exceptions.md)

Low-level APIs

- [Event Loop](asyncio-eventloop.md)
- [Futures](asyncio-future.md)
- [Transports and Protocols](asyncio-protocol.md)
- [Policies](asyncio-policy.md)
- [Platform Support](asyncio-platforms.md)
- [Extending](asyncio-extending.md)

Guides and Tutorials

- [High-level API Index](asyncio-api-index.md)
- [Low-level API Index](asyncio-llapi-index.md)
- [Developing with asyncio](asyncio-dev.md)

> **Note:**
>
> The source code for asyncio can be found in [Lib/asyncio/](https://github.com/python/cpython/tree/3.12/Lib/asyncio/).
