---
collection: libvirt
version: "12.7.0"
title: "virtnodedevd"
source_url: https://libvirt.org/manpages/virtnodedevd.html
fetched_at: 2026-08-21T04:10:26+00:00
---
# virtnodedevd

libvirt host device management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtnodedevd.md#synopsis)
- [DESCRIPTION](virtnodedevd.md#description)
- [DAEMON STARTUP MODES](virtnodedevd.md#daemon-startup-modes)

  - [Socket activation mode](virtnodedevd.md#socket-activation-mode)
  - [Traditional service mode](virtnodedevd.md#traditional-service-mode)
- [OPTIONS](virtnodedevd.md#options)
- [SIGNALS](virtnodedevd.md#signals)
- [FILES](virtnodedevd.md#files)

  - [When run as *root*](virtnodedevd.md#when-run-as-root)
  - [When run as *non-root*](virtnodedevd.md#when-run-as-non-root)
- [EXAMPLES](virtnodedevd.md#examples)
- [BUGS](virtnodedevd.md#bugs)
- [AUTHORS](virtnodedevd.md#authors)
- [COPYRIGHT](virtnodedevd.md#copyright)
- [LICENSE](virtnodedevd.md#license)
- [SEE ALSO](virtnodedevd.md#see-also)

# [SYNOPSIS](virtnodedevd.md#id1)

virtnodedevd [*OPTION*]...

# [DESCRIPTION](virtnodedevd.md#id2)

The virtnodedevd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for host devices.

The virtnodedevd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtnodedevd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtnodedevd.md#id3)

The virtnodedevd daemon is capable of starting in two modes.

## [Socket activation mode](virtnodedevd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtnodedevd.conf will no longer have any effect.

## [Traditional service mode](virtnodedevd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtnodedevd.md#id6)

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

# [SIGNALS](virtnodedevd.md#id7)

On receipt of SIGHUP virtnodedevd will reload its configuration.

# [FILES](virtnodedevd.md#id8)

## [When run as *root*](virtnodedevd.md#id9)

- /etc/libvirt/virtnodedevd.conf

The default configuration file used by virtnodedevd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtnodedevd-sock
- /run/libvirt/virtnodedevd-sock-ro
- /run/libvirt/virtnodedevd-admin-sock

The sockets virtnodedevd will use.

The TLS **Server** private key virtnodedevd will use.

- /run/virtnodedevd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtnodedevd.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtnodedevd.conf

The default configuration file used by virtnodedevd, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtnodedevd-sock
- $XDG_RUNTIME_DIR/libvirt/virtnodedevd-admin-sock

The sockets virtnodedevd will use.

- $XDG_RUNTIME_DIR/libvirt/virtnodedevd.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtnodedevd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtnodedevd will use
$HOME/.cache

# [EXAMPLES](virtnodedevd.md#id11)

To retrieve the version of virtnodedevd:

```
# virtnodedevd --version
virtnodedevd (libvirt) 12.7.0
```

To start virtnodedevd, instructing it to daemonize and create a PID file:

```
# virtnodedevd -d
# ls -la /run/virtnodedevd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtnodedevd.pid
```

# [BUGS](virtnodedevd.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtnodedevd.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtnodedevd.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtnodedevd.md#id15)

virtnodedevd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtnodedevd.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvnodedev.html](../drvnodedev.md)
