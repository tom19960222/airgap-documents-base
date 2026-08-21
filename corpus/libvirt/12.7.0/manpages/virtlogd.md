---
collection: libvirt
version: "12.7.0"
title: "virtlogd"
source_url: https://libvirt.org/manpages/virtlogd.html
fetched_at: 2026-08-21T04:10:23+00:00
---
# virtlogd

libvirt log management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtlogd.md#synopsis)
- [DESCRIPTION](virtlogd.md#description)
- [OPTIONS](virtlogd.md#options)
- [SIGNALS](virtlogd.md#signals)
- [FILES](virtlogd.md#files)

  - [When run as *root*](virtlogd.md#when-run-as-root)
  - [When run as *non-root*](virtlogd.md#when-run-as-non-root)
- [EXAMPLES](virtlogd.md#examples)
- [BUGS](virtlogd.md#bugs)
- [AUTHORS](virtlogd.md#authors)
- [COPYRIGHT](virtlogd.md#copyright)
- [LICENSE](virtlogd.md#license)
- [SEE ALSO](virtlogd.md#see-also)

# [SYNOPSIS](virtlogd.md#id1)

virtlogd [*OPTION*]...

# [DESCRIPTION](virtlogd.md#id2)

The virtlogd program is a server side daemon component of the libvirt
virtualization management system that is used to manage logs from virtual
machine consoles.

This daemon is not used directly by libvirt client applications, rather it
is called on their behalf by libvirtd. By maintaining the logs in a
standalone daemon, the main libvirtd daemon can be restarted without risk
of losing logs. The virtlogd daemon has the ability to re-exec()
itself upon receiving SIGUSR1, to allow live upgrades without downtime.

The virtlogd daemon listens for requests on a local Unix domain socket.

# [OPTIONS](virtlogd.md#id3)

-h, --help

Display command line help usage then exit.

-d, --daemon

Run as a daemon and write PID file.

-f, --config *FILE*

Use this configuration file, overriding the default value.

-t, --timeout *SECONDS*

Automatically shutdown after *SECONDS* have elapsed with
no active console log.

-p, --pid-file *FILE*

Use this name for the PID file, overriding the default value.

-v, --verbose

Enable output of verbose messages.

-V, --version

Display version information then exit.

# [SIGNALS](virtlogd.md#id4)

On receipt of SIGUSR1, virtlogd will re-exec() its binary, while
maintaining all current logs and clients. This allows for live
upgrades of the virtlogd service.

# [FILES](virtlogd.md#id5)

## [When run as *root*](virtlogd.md#id6)

- /etc/libvirt/virtlogd.conf

The default configuration file used by virtlogd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtlogd-sock

The sockets virtlogd will use.

- /run/virtlogd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtlogd.md#id7)

- $XDG_CONFIG_HOME/libvirt/virtlogd.conf

The default configuration file used by virtlogd, unless overridden on the
command line using the -f | --config option.

- $XDG_RUNTIME_DIR/libvirt/virtlogd-sock

The socket virtlogd will use.

- $XDG_RUNTIME_DIR/libvirt/virtlogd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

If $XDG_CONFIG_HOME is not set in your environment, virtlogd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtlogd will use
$HOME/.cache

# [EXAMPLES](virtlogd.md#id8)

To retrieve the version of virtlogd:

```
# virtlogd --version
virtlogd (libvirt) 12.7.0
```

To start virtlogd, instructing it to daemonize and create a PID file:

```
# virtlogd -d
# ls -la /run/virtlogd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtlogd.pid
```

# [BUGS](virtlogd.md#id9)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtlogd.md#id10)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtlogd.md#id11)

Copyright (C) 2006-2015 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtlogd.md#id12)

virtlogd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtlogd.md#id13)

libvirtd(8), [https://libvirt.org/](../index.md)
