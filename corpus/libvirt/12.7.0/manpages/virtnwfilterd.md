---
collection: libvirt
version: "12.7.0"
title: "virtnwfilterd"
source_url: https://libvirt.org/manpages/virtnwfilterd.html
fetched_at: 2026-08-21T04:10:27+00:00
---
# virtnwfilterd

libvirt network filter management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtnwfilterd.md#synopsis)
- [DESCRIPTION](virtnwfilterd.md#description)
- [DAEMON STARTUP MODES](virtnwfilterd.md#daemon-startup-modes)

  - [Socket activation mode](virtnwfilterd.md#socket-activation-mode)
  - [Traditional service mode](virtnwfilterd.md#traditional-service-mode)
- [OPTIONS](virtnwfilterd.md#options)
- [SIGNALS](virtnwfilterd.md#signals)
- [FILES](virtnwfilterd.md#files)

  - [When run as *root*](virtnwfilterd.md#when-run-as-root)
  - [When run as *non-root*](virtnwfilterd.md#when-run-as-non-root)
- [EXAMPLES](virtnwfilterd.md#examples)
- [BUGS](virtnwfilterd.md#bugs)
- [AUTHORS](virtnwfilterd.md#authors)
- [COPYRIGHT](virtnwfilterd.md#copyright)
- [LICENSE](virtnwfilterd.md#license)
- [SEE ALSO](virtnwfilterd.md#see-also)

# [SYNOPSIS](virtnwfilterd.md#id1)

virtnwfilterd [*OPTION*]...

# [DESCRIPTION](virtnwfilterd.md#id2)

The virtnwfilterd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for network
filters.

The virtnwfilterd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtnwfilterd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtnwfilterd.md#id3)

The virtnwfilterd daemon is capable of starting in two modes.

## [Socket activation mode](virtnwfilterd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtnwfilterd.conf will no longer have any effect.

## [Traditional service mode](virtnwfilterd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtnwfilterd.md#id6)

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

# [SIGNALS](virtnwfilterd.md#id7)

On receipt of SIGHUP virtnwfilterd will reload its configuration.

# [FILES](virtnwfilterd.md#id8)

## [When run as *root*](virtnwfilterd.md#id9)

- /etc/libvirt/virtnwfilterd.conf

The default configuration file used by virtnwfilterd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtnwfilterd-sock
- /run/libvirt/virtnwfilterd-sock-ro
- /run/libvirt/virtnwfilterd-admin-sock

The sockets virtnwfilterd will use.

The TLS **Server** private key virtnwfilterd will use.

- /run/virtnwfilterd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtnwfilterd.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtnwfilterd.conf

The default configuration file used by virtnwfilterd, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtnwfilterd-sock
- $XDG_RUNTIME_DIR/libvirt/virtnwfilterd-admin-sock

The sockets virtnwfilterd will use.

- $XDG_RUNTIME_DIR/libvirt/virtnwfilterd.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtnwfilterd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtnwfilterd will use
$HOME/.cache

# [EXAMPLES](virtnwfilterd.md#id11)

To retrieve the version of virtnwfilterd:

```
# virtnwfilterd --version
virtnwfilterd (libvirt) 12.7.0
```

To start virtnwfilterd, instructing it to daemonize and create a PID file:

```
# virtnwfilterd -d
# ls -la /run/virtnwfilterd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtnwfilterd.pid
```

# [BUGS](virtnwfilterd.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtnwfilterd.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtnwfilterd.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtnwfilterd.md#id15)

virtnwfilterd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtnwfilterd.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
