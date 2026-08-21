---
collection: libvirt
version: "12.7.0"
title: "virtstoraged"
source_url: https://libvirt.org/manpages/virtstoraged.html
fetched_at: 2026-08-21T04:10:29+00:00
---
# virtstoraged

libvirt storage pool management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtstoraged.md#synopsis)
- [DESCRIPTION](virtstoraged.md#description)
- [DAEMON STARTUP MODES](virtstoraged.md#daemon-startup-modes)

  - [Socket activation mode](virtstoraged.md#socket-activation-mode)
  - [Traditional service mode](virtstoraged.md#traditional-service-mode)
- [OPTIONS](virtstoraged.md#options)
- [SIGNALS](virtstoraged.md#signals)
- [FILES](virtstoraged.md#files)

  - [When run as *root*](virtstoraged.md#when-run-as-root)
  - [When run as *non-root*](virtstoraged.md#when-run-as-non-root)
- [EXAMPLES](virtstoraged.md#examples)
- [BUGS](virtstoraged.md#bugs)
- [AUTHORS](virtstoraged.md#authors)
- [COPYRIGHT](virtstoraged.md#copyright)
- [LICENSE](virtstoraged.md#license)
- [SEE ALSO](virtstoraged.md#see-also)

# [SYNOPSIS](virtstoraged.md#id1)

virtstoraged [*OPTION*]...

# [DESCRIPTION](virtstoraged.md#id2)

The virtstoraged program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for storage
pools.

The virtstoraged daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtstoraged does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtstoraged.md#id3)

The virtstoraged daemon is capable of starting in two modes.

## [Socket activation mode](virtstoraged.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtstoraged.conf will no longer have any effect.

## [Traditional service mode](virtstoraged.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtstoraged.md#id6)

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

# [SIGNALS](virtstoraged.md#id7)

On receipt of SIGHUP virtstoraged will reload its configuration.

# [FILES](virtstoraged.md#id8)

## [When run as *root*](virtstoraged.md#id9)

- /etc/libvirt/virtstoraged.conf

The default configuration file used by virtstoraged, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtstoraged-sock
- /run/libvirt/virtstoraged-sock-ro
- /run/libvirt/virtstoraged-admin-sock

The sockets virtstoraged will use.

The TLS **Server** private key virtstoraged will use.

- /run/virtstoraged.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtstoraged.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtstoraged.conf

The default configuration file used by virtstoraged, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtstoraged-sock
- $XDG_RUNTIME_DIR/libvirt/virtstoraged-admin-sock

The sockets virtstoraged will use.

- $XDG_RUNTIME_DIR/libvirt/virtstoraged.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtstoraged will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtstoraged will use
$HOME/.cache

# [EXAMPLES](virtstoraged.md#id11)

To retrieve the version of virtstoraged:

```
# virtstoraged --version
virtstoraged (libvirt) 12.7.0
```

To start virtstoraged, instructing it to daemonize and create a PID file:

```
# virtstoraged -d
# ls -la /run/virtstoraged.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtstoraged.pid
```

# [BUGS](virtstoraged.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtstoraged.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtstoraged.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtstoraged.md#id15)

virtstoraged is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtstoraged.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/storage.html](../storage.md)
