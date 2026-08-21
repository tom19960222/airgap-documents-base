---
collection: libvirt
version: "12.7.0"
title: "virtlxcd"
source_url: https://libvirt.org/manpages/virtlxcd.html
fetched_at: 2026-08-21T04:10:25+00:00
---
# virtlxcd

libvirt LXC management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtlxcd.md#synopsis)
- [DESCRIPTION](virtlxcd.md#description)
- [DAEMON STARTUP MODES](virtlxcd.md#daemon-startup-modes)

  - [Socket activation mode](virtlxcd.md#socket-activation-mode)
  - [Traditional service mode](virtlxcd.md#traditional-service-mode)
- [OPTIONS](virtlxcd.md#options)
- [SIGNALS](virtlxcd.md#signals)
- [FILES](virtlxcd.md#files)
- [EXAMPLES](virtlxcd.md#examples)
- [BUGS](virtlxcd.md#bugs)
- [AUTHORS](virtlxcd.md#authors)
- [COPYRIGHT](virtlxcd.md#copyright)
- [LICENSE](virtlxcd.md#license)
- [SEE ALSO](virtlxcd.md#see-also)

# [SYNOPSIS](virtlxcd.md#id1)

virtlxcd [*OPTION*]...

# [DESCRIPTION](virtlxcd.md#id2)

The virtlxcd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for LXC
containers.

The virtlxcd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtlxcd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtlxcd.md#id3)

The virtlxcd daemon is capable of starting in two modes.

## [Socket activation mode](virtlxcd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtlxcd.conf will no longer have any effect.

## [Traditional service mode](virtlxcd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtlxcd.md#id6)

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

# [SIGNALS](virtlxcd.md#id7)

On receipt of SIGHUP virtlxcd will reload its configuration.

# [FILES](virtlxcd.md#id8)

The virtlxcd program must be ran as root. Trying to start the program under
a different user results in error.

- /etc/libvirt/virtlxcd.conf

The default configuration file used by virtlxcd, unless overridden on the
command line using the -f | --config option.

In addition to the default configuration file, virtlxcd reads
configuration for the LXC driver from:

- /etc/libvirt/lxc.conf

This file contains various knobs and default values for virtual machines
created within LXC driver, and offers a way to override the built in defaults,
Location of this file can't be overridden by any command line switch.

- /run/libvirt/virtlxcd-sock
- /run/libvirt/virtlxcd-sock-ro
- /run/libvirt/virtlxcd-admin-sock

The sockets virtlxcd will use.

The TLS **Server** private key virtlxcd will use.

- /run/virtlxcd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

# [EXAMPLES](virtlxcd.md#id9)

To retrieve the version of virtlxcd:

```
# virtlxcd --version
virtlxcd (libvirt) 12.7.0
```

To start virtlxcd, instructing it to daemonize and create a PID file:

```
# virtlxcd -d
# ls -la /run/virtlxcd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtlxcd.pid
```

# [BUGS](virtlxcd.md#id10)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtlxcd.md#id11)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtlxcd.md#id12)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtlxcd.md#id13)

virtlxcd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtlxcd.md#id14)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvlxc.html](../drvlxc.md)
