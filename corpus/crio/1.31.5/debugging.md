---
collection: crio
version: "1.31.5"
title: "Debugging CRI-O"
source_url: https://github.com/cri-o/cri-o/blob/5184b74964ef620d64169a41fd27afdba6fe130e/tutorials/debugging.md
fetched_at: 2025-02-03T17:22:57Z
---
# Debugging CRI-O

Below is a non-comprehensive document on some tips and tricks for
troubleshooting/debugging/inspecting the behavior of CRI-O.

## Printing go routines

Often with a long-running process, it can be useful to know what that
process is up to.
CRI-O has built-in functionality to print the go routine stacks to provide such information.
All one has to do is send SIGUSR1 to CRI-O, either with `kill` or `systemctl`
(if running CRI-O as a systemd unit):

```shell
kill -USR1 $crio-pid
systemctl kill -s USR1 crio.service
```

CRI-O will catch the signal, and write the routine stacks to `/tmp/crio-goroutine-stacks-$timestamp.log`

### Forcing Go Garbage Collection

You may have a need to manually run Go garbage collection for CRI-O.
To force garbage collection, send CRI-O SIGUSR2 using `kill` or `systemctl`
(if running CRI-O as a systemd unit).

```shell
kill -s SIGUSR2 $crio-pid

systemctl kill -s USR2 crio.service
```
