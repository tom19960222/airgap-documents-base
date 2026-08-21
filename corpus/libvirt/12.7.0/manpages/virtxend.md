---
collection: libvirt
version: "12.7.0"
title: "virtxend"
source_url: https://libvirt.org/manpages/virtxend.html
fetched_at: 2026-08-21T04:10:30+00:00
---
# virtxend

libvirt Xen management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtxend.md#synopsis)
- [DESCRIPTION](virtxend.md#description)
- [DAEMON STARTUP MODES](virtxend.md#daemon-startup-modes)

  - [Socket activation mode](virtxend.md#socket-activation-mode)
  - [Traditional service mode](virtxend.md#traditional-service-mode)
- [OPTIONS](virtxend.md#options)
- [SIGNALS](virtxend.md#signals)
- [FILES](virtxend.md#files)
- [EXAMPLES](virtxend.md#examples)
- [BUGS](virtxend.md#bugs)
- [AUTHORS](virtxend.md#authors)
- [COPYRIGHT](virtxend.md#copyright)
- [LICENSE](virtxend.md#license)
- [SEE ALSO](virtxend.md#see-also)

# [SYNOPSIS](virtxend.md#id1)

virtxend [*OPTION*]...

# [DESCRIPTION](virtxend.md#id2)

The virtxend program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for Xen virtual
machines.

The virtxend daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtxend does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtxend.md#id3)

The virtxend daemon is capable of starting in two modes.

## [Socket activation mode](virtxend.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtxend.conf will no longer have any effect.

## [Traditional service mode](virtxend.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtxend.md#id6)

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

# [SIGNALS](virtxend.md#id7)

On receipt of SIGHUP virtxend will reload its configuration.

# [FILES](virtxend.md#id8)

The virtxend program must be ran as root. Trying to start the program under
a different user results in error.

- /etc/libvirt/virtxend.conf

The default configuration file used by virtxend, unless overridden on the
command line using the -f | --config option.

In addition to the default configuration file, virtxend reads
configuration for the libxl driver from:

- /etc/libvirt/libxl.conf

This file contains various knobs and default values for virtual machines
created within libxl driver, and offers a way to override the built in
defaults, Location of this file can't be overridden by any command line switch.

- /run/libvirt/virtxend-sock
- /run/libvirt/virtxend-sock-ro
- /run/libvirt/virtxend-admin-sock

The sockets virtxend will use.

The TLS **Server** private key virtxend will use.

- /run/virtxend.pid

The PID file to use, unless overridden by the -p | --pid-file option.

# [EXAMPLES](virtxend.md#id9)

To retrieve the version of virtxend:

```
# virtxend --version
virtxend (libvirt) 12.7.0
```

To start virtxend, instructing it to daemonize and create a PID file:

```
# virtxend -d
# ls -la /run/virtxend.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtxend.pid
```

# [BUGS](virtxend.md#id10)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtxend.md#id11)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtxend.md#id12)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtxend.md#id13)

virtxend is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtxend.md#id14)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvxen.html](../drvxen.md)
