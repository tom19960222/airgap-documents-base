---
collection: libvirt
version: "12.7.0"
title: "virtqemud"
source_url: https://libvirt.org/manpages/virtqemud.html
fetched_at: 2026-08-21T04:10:28+00:00
---
# virtqemud

libvirt QEMU management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtqemud.md#synopsis)
- [DESCRIPTION](virtqemud.md#description)
- [DAEMON STARTUP MODES](virtqemud.md#daemon-startup-modes)

  - [Socket activation mode](virtqemud.md#socket-activation-mode)
  - [Traditional service mode](virtqemud.md#traditional-service-mode)
- [OPTIONS](virtqemud.md#options)
- [SIGNALS](virtqemud.md#signals)
- [FILES](virtqemud.md#files)

  - [When run as *root*](virtqemud.md#when-run-as-root)
  - [When run as *non-root*](virtqemud.md#when-run-as-non-root)
- [EXAMPLES](virtqemud.md#examples)
- [BUGS](virtqemud.md#bugs)
- [AUTHORS](virtqemud.md#authors)
- [COPYRIGHT](virtqemud.md#copyright)
- [LICENSE](virtqemud.md#license)
- [SEE ALSO](virtqemud.md#see-also)

# [SYNOPSIS](virtqemud.md#id1)

virtqemud [*OPTION*]...

# [DESCRIPTION](virtqemud.md#id2)

The virtqemud program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for QEMU virtual
machines.

The virtqemud daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtqemud does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtqemud.md#id3)

The virtqemud daemon is capable of starting in two modes.

## [Socket activation mode](virtqemud.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtqemud.conf will no longer have any effect.

## [Traditional service mode](virtqemud.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtqemud.md#id6)

-h, --help

Display command line help usage then exit.

-d, --daemon

Run as a daemon & write PID file.

-f, --config \*FILE\*

Use this configuration file, overriding the default value.

-p, --pid-file \*FILE\*

Use this name for the PID file, overriding the default value.

-t, --timeout \*SECONDS\*

Exit after timeout period (in seconds), provided there are neither any client
connections nor any running domains.

-v, --verbose

Enable output of verbose messages.

--version

Display version information then exit.

# [SIGNALS](virtqemud.md#id7)

On receipt of SIGHUP virtqemud will reload its configuration.

# [FILES](virtqemud.md#id8)

## [When run as *root*](virtqemud.md#id9)

- /etc/libvirt/virtqemud.conf

The default configuration file used by virtqemud, unless overridden on the
command line using the -f | --config option.

In addition to the default configuration file, virtqemud reads
configuration for the QEMU driver from:

- /etc/libvirt/qemu.conf

This file contains various knobs and default values for virtual machines
created within QEMU driver, and offers a way to override the built in defaults,
for instance (but not limited to): paths to various supplementary binaries, TLS
certificates location, graphical consoles configuration and others. Location of
this file can't be overridden by any command line switch.

- /run/libvirt/virtqemud-sock
- /run/libvirt/virtqemud-sock-ro
- /run/libvirt/virtqemud-admin-sock

The sockets virtqemud will use.

The TLS **Server** private key virtqemud will use.

- /run/virtqemud.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtqemud.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtqemud.conf

The default configuration file used by virtqemud, unless overridden on the
command line using the -f``|--config`` option.

In addition to the default configuration file, virtqemud reads
configuration for the qemu driver from:

- $XDG_CONFIG_HOME/libvirt/qemu.conf

If the file exists, it can contain various knobs and default values for virtual
machines created within QEMU driver, and offers a way to override the built in
defaults, for instance (but not limited to): paths to various supplementary
binaries, TLS certificates location, graphical consoles configuration and
others. Location of this file can't be overridden by any command line switch.

- $XDG_RUNTIME_DIR/libvirt/virtqemud-sock
- $XDG_RUNTIME_DIR/libvirt/virtqemud-admin-sock

The sockets virtqemud will use.

- $XDG_RUNTIME_DIR/libvirt/virtqemud.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtqemud will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtqemud will use
$HOME/.cache

# [EXAMPLES](virtqemud.md#id11)

To retrieve the version of virtqemud:

```
# virtqemud --version
virtqemud (libvirt) 12.7.0
```

To start virtqemud, instructing it to daemonize and create a PID file:

```
# virtqemud -d
# ls -la /run/virtqemud.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtqemud.pid
```

# [BUGS](virtqemud.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtqemud.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtqemud.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtqemud.md#id15)

virtqemud is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtqemud.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvqemu.html](../drvqemu.md)
