---
collection: libvirt
version: "12.7.0"
title: "virtnetworkd"
source_url: https://libvirt.org/manpages/virtnetworkd.html
fetched_at: 2026-08-21T04:10:26+00:00
---
# virtnetworkd

libvirt virtual network management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtnetworkd.md#synopsis)
- [DESCRIPTION](virtnetworkd.md#description)
- [DAEMON STARTUP MODES](virtnetworkd.md#daemon-startup-modes)

  - [Socket activation mode](virtnetworkd.md#socket-activation-mode)
  - [Traditional service mode](virtnetworkd.md#traditional-service-mode)
- [OPTIONS](virtnetworkd.md#options)
- [SIGNALS](virtnetworkd.md#signals)
- [FILES](virtnetworkd.md#files)

  - [When run as *root*](virtnetworkd.md#when-run-as-root)
  - [When run as *non-root*](virtnetworkd.md#when-run-as-non-root)
- [EXAMPLES](virtnetworkd.md#examples)
- [BUGS](virtnetworkd.md#bugs)
- [AUTHORS](virtnetworkd.md#authors)
- [COPYRIGHT](virtnetworkd.md#copyright)
- [LICENSE](virtnetworkd.md#license)
- [SEE ALSO](virtnetworkd.md#see-also)

# [SYNOPSIS](virtnetworkd.md#id1)

virtnetworkd [*OPTION*]...

# [DESCRIPTION](virtnetworkd.md#id2)

The virtnetworkd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for virtual
networks.

The virtnetworkd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtnetworkd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtnetworkd.md#id3)

The virtnetworkd daemon is capable of starting in two modes.

## [Socket activation mode](virtnetworkd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtnetworkd.conf will no longer have any effect.

## [Traditional service mode](virtnetworkd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtnetworkd.md#id6)

-h, --help

Display command line help usage then exit.

-d, --daemon

Run as a daemon & write PID file.

-f, --config \*FILE\*

Use this configuration file, overriding the default value.

-p, --pid-file \*FILE\*

Use this name for the PID file, overriding the default value.

-t, --timeout \*SECONDS\*

Exit after timeout period (in seconds), provided there are no client
connections.

-v, --verbose

Enable output of verbose messages.

--version

Display version information then exit.

# [SIGNALS](virtnetworkd.md#id7)

On receipt of SIGHUP virtnetworkd will reload its configuration.

# [FILES](virtnetworkd.md#id8)

## [When run as *root*](virtnetworkd.md#id9)

- /etc/libvirt/virtnetworkd.conf

The default configuration file used by virtnetworkd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtnetworkd-sock
- /run/libvirt/virtnetworkd-sock-ro
- /run/libvirt/virtnetworkd-admin-sock

The sockets virtnetworkd will use.

The TLS **Server** private key virtnetworkd will use.

- /run/virtnetworkd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtnetworkd.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtnetworkd.conf

The default configuration file used by virtnetworkd, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtnetworkd-sock
- $XDG_RUNTIME_DIR/libvirt/virtnetworkd-admin-sock

The sockets virtnetworkd will use.

- $XDG_RUNTIME_DIR/libvirt/virtnetworkd.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtnetworkd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtnetworkd will use
$HOME/.cache

# [EXAMPLES](virtnetworkd.md#id11)

To retrieve the version of virtnetworkd:

```
# virtnetworkd --version
virtnetworkd (libvirt) 12.7.0
```

To start virtnetworkd, instructing it to daemonize and create a PID file:

```
# virtnetworkd -d
# ls -la /run/virtnetworkd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtnetworkd.pid
```

# [BUGS](virtnetworkd.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtnetworkd.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtnetworkd.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtnetworkd.md#id15)

virtnetworkd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtnetworkd.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
