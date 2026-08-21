---
collection: libvirt
version: "12.7.0"
title: "virtinterfaced"
source_url: https://libvirt.org/manpages/virtinterfaced.html
fetched_at: 2026-08-21T04:10:25+00:00
---
# virtinterfaced

libvirt host network interface management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtinterfaced.md#synopsis)
- [DESCRIPTION](virtinterfaced.md#description)
- [DAEMON STARTUP MODES](virtinterfaced.md#daemon-startup-modes)

  - [Socket activation mode](virtinterfaced.md#socket-activation-mode)
  - [Traditional service mode](virtinterfaced.md#traditional-service-mode)
- [OPTIONS](virtinterfaced.md#options)
- [SIGNALS](virtinterfaced.md#signals)
- [FILES](virtinterfaced.md#files)

  - [When run as *root*](virtinterfaced.md#when-run-as-root)
  - [When run as *non-root*](virtinterfaced.md#when-run-as-non-root)
- [EXAMPLES](virtinterfaced.md#examples)
- [BUGS](virtinterfaced.md#bugs)
- [AUTHORS](virtinterfaced.md#authors)
- [COPYRIGHT](virtinterfaced.md#copyright)
- [LICENSE](virtinterfaced.md#license)
- [SEE ALSO](virtinterfaced.md#see-also)

# [SYNOPSIS](virtinterfaced.md#id1)

virtinterfaced [*OPTION*]...

# [DESCRIPTION](virtinterfaced.md#id2)

The virtinterfaced program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for host network
interfaces.

The virtinterfaced daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtinterfaced does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtinterfaced.md#id3)

The virtinterfaced daemon is capable of starting in two modes.

## [Socket activation mode](virtinterfaced.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtinterfaced.conf will no longer have any effect.

## [Traditional service mode](virtinterfaced.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtinterfaced.md#id6)

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

# [SIGNALS](virtinterfaced.md#id7)

On receipt of SIGHUP virtinterfaced will reload its configuration.

# [FILES](virtinterfaced.md#id8)

## [When run as *root*](virtinterfaced.md#id9)

- /etc/libvirt/virtinterfaced.conf

The default configuration file used by virtinterfaced, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtinterfaced-sock
- /run/libvirt/virtinterfaced-sock-ro
- /run/libvirt/virtinterfaced-admin-sock

The sockets virtinterfaced will use.

The TLS **Server** private key virtinterfaced will use.

- /run/virtinterfaced.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtinterfaced.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtinterfaced.conf

The default configuration file used by virtinterfaced, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtinterfaced-sock
- $XDG_RUNTIME_DIR/libvirt/virtinterfaced-admin-sock

The sockets virtinterfaced will use.

- $XDG_RUNTIME_DIR/libvirt/virtinterfaced.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtinterfaced will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtinterfaced will use
$HOME/.cache

# [EXAMPLES](virtinterfaced.md#id11)

To retrieve the version of virtinterfaced:

```
# virtinterfaced --version
virtinterfaced (libvirt) 12.7.0
```

To start virtinterfaced, instructing it to daemonize and create a PID file:

```
# virtinterfaced -d
# ls -la /run/virtinterfaced.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtinterfaced.pid
```

# [BUGS](virtinterfaced.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtinterfaced.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtinterfaced.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtinterfaced.md#id15)

virtinterfaced is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtinterfaced.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
