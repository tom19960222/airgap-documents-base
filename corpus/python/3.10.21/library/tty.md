---
collection: python
version: "3.10.21"
title: "tty — Terminal control functions"
source_url: https://docs.python.org/3.10/library/tty.html
fetched_at: 2026-09-17T15:15:15+00:00
---
# `tty` — Terminal control functions

**Source code:** [Lib/tty.py](https://github.com/python/cpython/tree/3.10/Lib/tty.py)

---

The [`tty`](tty.md#module-tty "tty: Utility functions that perform common terminal control operations. (Unix)") module defines functions for putting the tty into cbreak and raw
modes.

Because it requires the [`termios`](termios.md#module-termios "termios: POSIX style tty control. (Unix)") module, it will work only on Unix.

The [`tty`](tty.md#module-tty "tty: Utility functions that perform common terminal control operations. (Unix)") module defines the following functions:

`tty.setraw(fd, when=termios.TCSAFLUSH)`
:   Change the mode of the file descriptor *fd* to raw. If *when* is omitted, it
    defaults to `termios.TCSAFLUSH`, and is passed to
    [`termios.tcsetattr()`](termios.md#termios.tcsetattr "termios.tcsetattr").

`tty.setcbreak(fd, when=termios.TCSAFLUSH)`
:   Change the mode of file descriptor *fd* to cbreak. If *when* is omitted, it
    defaults to `termios.TCSAFLUSH`, and is passed to
    [`termios.tcsetattr()`](termios.md#termios.tcsetattr "termios.tcsetattr").

> **See also:**
>
> Module [`termios`](termios.md#module-termios "termios: POSIX style tty control. (Unix)")
> :   Low-level terminal control interface.
