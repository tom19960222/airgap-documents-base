---
collection: libvirt
version: "12.7.0"
title: "virtbhyved"
source_url: https://libvirt.org/manpages/virtbhyved.html
fetched_at: 2026-08-21T04:10:24+00:00
---
# virtbhyved

libvirt bhyve management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtbhyved.md#synopsis)
- [DESCRIPTION](virtbhyved.md#description)
- [OPTIONS](virtbhyved.md#options)
- [SIGNALS](virtbhyved.md#signals)
- [FILES](virtbhyved.md#files)

  - [When run as *root*](virtbhyved.md#when-run-as-root)
  - [When run as *non-root*](virtbhyved.md#when-run-as-non-root)
- [EXAMPLES](virtbhyved.md#examples)
- [BUGS](virtbhyved.md#bugs)
- [AUTHORS](virtbhyved.md#authors)
- [COPYRIGHT](virtbhyved.md#copyright)
- [LICENSE](virtbhyved.md#license)
- [SEE ALSO](virtbhyved.md#see-also)

# [SYNOPSIS](virtbhyved.md#id1)

virtbhyved [*OPTION*]...

# [DESCRIPTION](virtbhyved.md#id2)

The virtbhyved program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for bhyve virtual
machines.

The virtbhyved daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtbhyved does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [OPTIONS](virtbhyved.md#id3)

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

# [SIGNALS](virtbhyved.md#id4)

On receipt of SIGHUP virtbhyved will reload its configuration.

# [FILES](virtbhyved.md#id5)

## [When run as *root*](virtbhyved.md#id6)

- /etc/libvirt/virtbhyved.conf

The default configuration file used by virtbhyved, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtbhyved-sock
- /run/libvirt/virtbhyved-sock-ro
- /run/libvirt/virtbhyved-admin-sock

The sockets virtbhyved will use.

The TLS **Server** private key virtbhyved will use.

- /run/virtbhyved.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtbhyved.md#id7)

- $XDG_CONFIG_HOME/libvirt/virtbhyved.conf

The default configuration file used by virtbhyved, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtbhyved-sock
- $XDG_RUNTIME_DIR/libvirt/virtbhyved-admin-sock

The sockets virtbhyved will use.

- $XDG_RUNTIME_DIR/libvirt/virtbhyved.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtbhyved will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtbhyved will use
$HOME/.cache

# [EXAMPLES](virtbhyved.md#id8)

To retrieve the version of virtbhyved:

```
# virtbhyved --version
virtbhyved (libvirt) 12.7.0
```

To start virtbhyved, instructing it to daemonize and create a PID file:

```
# virtbhyved -d
# ls -la /run/virtbhyved.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtbhyved.pid
```

# [BUGS](virtbhyved.md#id9)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtbhyved.md#id10)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtbhyved.md#id11)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtbhyved.md#id12)

virtbhyved is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtbhyved.md#id13)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvbhyve.html](../drvbhyve.md)
