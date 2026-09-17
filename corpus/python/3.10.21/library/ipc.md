---
collection: python
version: "3.10.21"
title: "Networking and Interprocess Communication"
source_url: https://docs.python.org/3.10/library/ipc.html
fetched_at: 2026-09-17T15:14:12+00:00
---
# Networking and Interprocess Communication

The modules described in this chapter provide mechanisms for
networking and inter-processes communication.

Some modules only work for two processes that are on the same machine, e.g.
[`signal`](signal.md#module-signal "signal: Set handlers for asynchronous events.") and [`mmap`](mmap.md#module-mmap "mmap: Interface to memory-mapped files for Unix and Windows."). Other modules support networking protocols
that two or more processes can use to communicate across machines.

The list of modules described in this chapter is:

- [`asyncio` — Asynchronous I/O](asyncio.md)
- [`socket` — Low-level networking interface](socket.md)
- [`ssl` — TLS/SSL wrapper for socket objects](ssl.md)
- [`select` — Waiting for I/O completion](select.md)
- [`selectors` — High-level I/O multiplexing](selectors.md)
- [`signal` — Set handlers for asynchronous events](signal.md)
- [`mmap` — Memory-mapped file support](mmap.md)
