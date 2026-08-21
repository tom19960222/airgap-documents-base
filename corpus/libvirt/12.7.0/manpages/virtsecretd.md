---
collection: libvirt
version: "12.7.0"
title: "virtsecretd"
source_url: https://libvirt.org/manpages/virtsecretd.html
fetched_at: 2026-08-21T04:10:28+00:00
---
# virtsecretd

libvirt secret data management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtsecretd.md#synopsis)
- [DESCRIPTION](virtsecretd.md#description)
- [DAEMON STARTUP MODES](virtsecretd.md#daemon-startup-modes)

  - [Socket activation mode](virtsecretd.md#socket-activation-mode)
  - [Traditional service mode](virtsecretd.md#traditional-service-mode)
- [OPTIONS](virtsecretd.md#options)
- [SIGNALS](virtsecretd.md#signals)
- [FILES](virtsecretd.md#files)

  - [When run as *root*](virtsecretd.md#when-run-as-root)
  - [When run as *non-root*](virtsecretd.md#when-run-as-non-root)
- [EXAMPLES](virtsecretd.md#examples)
- [BUGS](virtsecretd.md#bugs)
- [AUTHORS](virtsecretd.md#authors)
- [COPYRIGHT](virtsecretd.md#copyright)
- [LICENSE](virtsecretd.md#license)
- [SEE ALSO](virtsecretd.md#see-also)

# [SYNOPSIS](virtsecretd.md#id1)

virtsecretd [*OPTION*]...

# [DESCRIPTION](virtsecretd.md#id2)

The virtsecretd program is a server side daemon component of the libvirt
virtualization management system.

It is one of a collection of modular daemons that replace functionality
previously provided by the monolithic libvirtd daemon.

This daemon runs on virtualization hosts to provide management for secret data.

The virtsecretd daemon only listens for requests on a local Unix domain
socket. Remote access via TLS/TCP and backwards compatibility with legacy
clients expecting libvirtd is provided by the virtproxyd daemon.

Restarting virtsecretd does not interrupt running guests. Guests continue to
operate and changes in their state will generally be picked up automatically
during startup. None the less it is recommended to avoid restarting with
running guests whenever practical.

# [DAEMON STARTUP MODES](virtsecretd.md#id3)

The virtsecretd daemon is capable of starting in two modes.

## [Socket activation mode](virtsecretd.md#id4)

On hosts with systemd it is started in socket activation mode and it will rely
on systemd to create and listen on the UNIX sockets and pass them as pre-opened
file descriptors. In this mode most of the socket related config options in
/etc/libvirt/virtsecretd.conf will no longer have any effect.

## [Traditional service mode](virtsecretd.md#id5)

On hosts without systemd, it will create and listen on UNIX sockets itself.

# [OPTIONS](virtsecretd.md#id6)

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
connections nor any ephemeral secrets.

-v, --verbose

Enable output of verbose messages.

--version

Display version information then exit.

# [SIGNALS](virtsecretd.md#id7)

On receipt of SIGHUP virtsecretd will reload its configuration.

# [FILES](virtsecretd.md#id8)

## [When run as *root*](virtsecretd.md#id9)

- /etc/libvirt/virtsecretd.conf

The default configuration file used by virtsecretd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtsecretd-sock
- /run/libvirt/virtsecretd-sock-ro
- /run/libvirt/virtsecretd-admin-sock

The sockets virtsecretd will use.

The TLS **Server** private key virtsecretd will use.

- /run/virtsecretd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtsecretd.md#id10)

- $XDG_CONFIG_HOME/libvirt/virtsecretd.conf

The default configuration file used by virtsecretd, unless overridden on the
command line using the -f``|--config`` option.

- $XDG_RUNTIME_DIR/libvirt/virtsecretd-sock
- $XDG_RUNTIME_DIR/libvirt/virtsecretd-admin-sock

The sockets virtsecretd will use.

- $XDG_RUNTIME_DIR/libvirt/virtsecretd.pid

The PID file to use, unless overridden by the -p``|--pid-file`` option.

If $XDG_CONFIG_HOME is not set in your environment, virtsecretd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtsecretd will use
$HOME/.cache

# [EXAMPLES](virtsecretd.md#id11)

To retrieve the version of virtsecretd:

```
# virtsecretd --version
virtsecretd (libvirt) 12.7.0
```

To start virtsecretd, instructing it to daemonize and create a PID file:

```
# virtsecretd -d
# ls -la /run/virtsecretd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtsecretd.pid
```

# [BUGS](virtsecretd.md#id12)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtsecretd.md#id13)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtsecretd.md#id14)

Copyright (C) 2006-2020 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtsecretd.md#id15)

virtsecretd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtsecretd.md#id16)

virsh(1), libvirtd(8),
[https://libvirt.org/daemons.html](../daemons.md),
[https://libvirt.org/drvsecret.html](../drvsecret.md)
