---
collection: kernel
version: "6.8"
title: "Steps for sending 'break' on sunhv console"
source_url: https://www.kernel.org/doc/html/v6.8/arch/sparc/console.html
fetched_at: 2026-08-21T03:37:01+00:00
---
# Steps for sending 'break' on sunhv console

On Baremetal:
:   1. press Esc + 'B'

On LDOM:
:   1. press Ctrl + ']'
    2. telnet> send break
