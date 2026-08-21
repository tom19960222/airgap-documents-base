---
collection: qemu
version: "11.1.0"
title: "Keys in the character backend multiplexer"
source_url: https://www.qemu.org/docs/master/system/mux-chardev.html
fetched_at: 2026-08-21T03:21:27+00:00
---
# Keys in the character backend multiplexer

During emulation, if you are using a character backend multiplexer
(which is the default if you are using `-nographic`) then several
commands are available via an escape sequence. These key sequences all
start with an escape character, which is `Ctrl+a` by default, but can be
changed with `-echr`. The list below assumes you’re using the default.

Multiplexer Keys

| Key Sequence | Action |
| --- | --- |
| `Ctrl+a h` | Print this help |
| `Ctrl+a x` | Exit emulator |
| `Ctrl+a s` | Save disk data back to file (if -snapshot) |
| `Ctrl+a t` | Toggle console timestamps |
| `Ctrl+a b` | Send break (magic sysrq in Linux) |
| `Ctrl+a c` | Rotate between the frontends connected to the multiplexer (usually this switches between the monitor and the console) |
| `Ctrl+a Ctrl+a` | Send the escape character to the frontend |
