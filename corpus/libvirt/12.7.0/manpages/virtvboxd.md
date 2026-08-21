---
collection: libvirt
version: "12.7.0"
title: "virtvboxd"
source_url: https://libvirt.org/manpages/virtvboxd.html
fetched_at: 2026-08-21T04:10:29+00:00
---
# virtvboxd

libvirt VirtualBox management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtvboxd.md#synopsis)
- [DESCRIPTION](virtvboxd.md#description)
- [DAEMON STARTUP MODES](virtvboxd.md#daemon-startup-modes)

  - [Socket activation mode](virtvboxd.md#socket-activation-mode)
  - [Traditional service mode](virtvboxd.md#traditional-service-mode)
- [OPTIONS](virtvboxd.md#options)
- [SIGNALS](virtvboxd.md#signals)
- [FILES](virtvboxd.md#files)

  - [When run as *root*](virtvboxd.md#when-run-as-root)
  - [When run as *non-root*](virtvboxd.md#when-run-as-non-root)
- [EXAMPLES](virtvboxd.md#examples)
- [BUGS](virtvboxd.md#bugs)
- [AUTHORS](virtvboxd.md#authors)
- [COPYRIGHT](virtvboxd.md#copyright)
- [LICENSE](virtvboxd.md#license)
- [SEE ALSO](virtvboxd.md#see-also)

# [SYNOPSIS](virtvboxd.md#id1)

virtvboxd [*OPTION*]...

# [DESCRIPTION](virtvboxd.md#id2)

The virtvboxd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for VirtualBox
virtual machines.

The virtvboxd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtvboxd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup.

# [DAEMON STARTUP MODES](virtvboxd.md#id3)

The virtvboxd daemon is capable of starting in two modes.

## [Socket activation mode](virtvboxd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtvboxd.conf will no longer have any effect.

## [Traditional service mode](virtvboxd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtvboxd.md#id6)

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

# [SIGNALS](virtvboxd.md#id7)

On receipt of SIGHUP virtvboxd will reload its configuration.

# [FILES](virtvboxd.md#id8)

## [When run as *root*](virtvboxd.md#id9)

- /etc/libvirt/virtvboxd.conf

The default configuration file used by virtvboxd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtvboxd-sock
- /run/libvirt/virtvboxd-sock-ro
- /run/libvirt/virtvboxd-admin-sock

The sockets virtvboxd will use.

The TLS **Server** private key virtvboxd will use.

- /run/virtvboxd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtvboxd.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtvboxd.conf

The default configuration file used by virtvboxd, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtvboxd-sock
- $XDG_RUNTIME_DIR/libvirt/virtvboxd-admin-sock

The sockets virtvboxd will use.

- $XDG_RUNTIME_DIR/libvirt/virtvboxd.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtvboxd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtvboxd will use
$HOME/.cache

# [EXAMPLES](virtvboxd.md#id11)

To retrieve the version of virtvboxd:

```
# virtvboxd --version
virtvboxd (libvirt) 12.7.0
```

To start virtvboxd, instructing it to daemonize and create a PID file:

```
# virtvboxd -d
# ls -la /run/virtvboxd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtvboxd.pid
```

# [BUGS](virtvboxd.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtvboxd.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtvboxd.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtvboxd.md#id15)

virtvboxd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtvboxd.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvvbox.html](../drvvbox.md)
