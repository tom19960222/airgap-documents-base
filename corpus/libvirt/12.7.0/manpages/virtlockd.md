---
collection: libvirt
version: "12.7.0"
title: "virtlockd"
source_url: https://libvirt.org/manpages/virtlockd.html
fetched_at: 2026-08-21T04:10:22+00:00
---
# virtlockd

libvirt lock management daemon

Manual section
:   8

Manual group
:   Virtualization Support

Contents

- [SYNOPSIS](virtlockd.md#synopsis)
- [DESCRIPTION](virtlockd.md#description)
- [OPTIONS](virtlockd.md#options)
- [SIGNALS](virtlockd.md#signals)
- [FILES](virtlockd.md#files)

  - [When run as *root*](virtlockd.md#when-run-as-root)
  - [When run as *non-root*](virtlockd.md#when-run-as-non-root)
- [EXAMPLES](virtlockd.md#examples)
- [BUGS](virtlockd.md#bugs)
- [AUTHORS](virtlockd.md#authors)
- [COPYRIGHT](virtlockd.md#copyright)
- [LICENSE](virtlockd.md#license)
- [SEE ALSO](virtlockd.md#see-also)

# [SYNOPSIS](virtlockd.md#id1)

virtlockd [*OPTION*]...

# [DESCRIPTION](virtlockd.md#id2)

The virtlockd program is a server side daemon component of the libvirt
virtualization management system that is used to manage locks held against
virtual machine resources, such as their disks.

This daemon is not used directly by libvirt client applications, rather it
is called on their behalf by libvirtd. By maintaining the locks in a
standalone daemon, the main libvirtd daemon can be restarted without risk
of losing locks. The virtlockd daemon has the ability to re-exec()
itself upon receiving SIGUSR1, to allow live upgrades without downtime.

The virtlockd daemon listens for requests on a local Unix domain socket.

# [OPTIONS](virtlockd.md#id3)

-h, --help

Display command line help usage then exit.

-d, --daemon

Run as a daemon and write PID file.

-f, --config *FILE*

Use this configuration file, overriding the default value.

-t, --timeout *SECONDS*

Automatically shutdown after *SECONDS* have elapsed with
no active client or lock.

-p, --pid-file *FILE*

Use this name for the PID file, overriding the default value.

-v, --verbose

Enable output of verbose messages.

-V, --version

Display version information then exit.

# [SIGNALS](virtlockd.md#id4)

On receipt of SIGUSR1, virtlockd will re-exec() its binary, while
maintaining all current locks and clients. This allows for live
upgrades of the virtlockd service.

# [FILES](virtlockd.md#id5)

## [When run as *root*](virtlockd.md#id6)

- /etc/libvirt/virtlockd.conf

The default configuration file used by virtlockd, unless overridden on the
command line using the -f | --config option.

- /run/libvirt/virtlockd-sock

The sockets virtlockd will use.

- /run/virtlockd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

## [When run as *non-root*](virtlockd.md#id7)

- $XDG_CONFIG_HOME/libvirt/virtlockd.conf

The default configuration file used by virtlockd, unless overridden on the
command line using the -f | --config option.

- $XDG_RUNTIME_DIR/libvirt/virtlockd-sock

The socket virtlockd will use.

- $XDG_RUNTIME_DIR/libvirt/virtlockd.pid

The PID file to use, unless overridden by the -p | --pid-file option.

If $XDG_CONFIG_HOME is not set in your environment, virtlockd will use
$HOME/.config

If $XDG_RUNTIME_DIR is not set in your environment, virtlockd will use
$HOME/.cache

# [EXAMPLES](virtlockd.md#id8)

To retrieve the version of virtlockd:

```
# virtlockd --version
virtlockd (libvirt) 12.7.0
```

To start virtlockd, instructing it to daemonize and create a PID file:

```
# virtlockd -d
# ls -la /run/virtlockd.pid
-rw-r--r-- 1 root root 6 Jul  9 02:40 /run/virtlockd.pid
```

# [BUGS](virtlockd.md#id9)

Please report all bugs you discover. This should be done via either:

1. the mailing list

   <https://libvirt.org/contact.html>
2. the bug tracker

   [https://libvirt.org/bugs.html](../bugs.md)

Alternatively, you may report bugs to your software distributor / vendor.

# [AUTHORS](virtlockd.md#id10)

Please refer to the AUTHORS file distributed with libvirt.

# [COPYRIGHT](virtlockd.md#id11)

Copyright (C) 2006-2013 Red Hat, Inc., and the authors listed in the
libvirt AUTHORS file.

# [LICENSE](virtlockd.md#id12)

virtlockd is distributed under the terms of the GNU LGPL v2.1+.
This is free software; see the source for copying conditions. There
is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE

# [SEE ALSO](virtlockd.md#id13)

libvirtd(8), [https://libvirt.org/](../index.md)
