---
collection: libvirt
version: "12.7.0"
title: "Libvirt does not work after installation"
source_url: https://libvirt.org/kbase/failed_connection_after_install.html
fetched_at: 2026-08-21T04:09:56+00:00
---
# Libvirt does not work after installation

Contents

- [TL;DR](failed_connection_after_install.md#tl-dr)
- [Symptom](failed_connection_after_install.md#symptom)
- [Root cause](failed_connection_after_install.md#root-cause)
- [Solution](failed_connection_after_install.md#solution)

# [TL;DR](failed_connection_after_install.md#id1)

Most probably you want to start a virtqemud socket:

```
# systemctl start virtqemud.socket
```

If you are unsure whether to do this, please read the rest of this document.

# [Symptom](failed_connection_after_install.md#id2)

After installing libvirt or a virt tool that uses libvirt, commands do
not work when run as root:

```
# virsh list
error: failed to connect to the hypervisor
error: Operation not supported: Cannot use direct socket mode if no URI is set.
For more information see https://libvirt.org/kbase/failed_connection_after_install.html
```

Or

```
# virsh list
error: failed to connect to the hypervisor
error: Operation not supported: No URI is provided and cannot identify any listening
daemon socket path to attempt to connect to. For more information see
https://libvirt.org/kbase/failed_connection_after_install.html
```

# [Root cause](failed_connection_after_install.md#id3)

Distribution guidelines and/or configurations may discourage or prohibit
starting services as part of a package installation. And because libvirt cannot
know where you might want to connect it cannot start it on its own.

# [Solution](failed_connection_after_install.md#id4)

After installing libvirt you may need to start a particular libvirt daemon on
the local machine, set a (default) URI to connect to or, alternatively,
rebooting the machine might work.

If you are trying to connect to a remote libvirt daemon you need to specify a [connection URI](../uri.md).

If you are trying to control a local hypervisor, then the solution depends on various factors. You should know:

- what hypervisor driver you want to connect to, whether it is virtqemud for QEMU, virtchd for Cloud Hypervisor, etc. and
- how to start a service or socket (in case of systemd) on you system.

Example of the most common solution, trying to use QEMU/KVM on Linux with systemd as an init system, is:

```
# systemctl start virtqemud.socket
```

also provided on the top of the page.
