---
collection: libvirt
version: "12.7.0"
title: "Documentation"
source_url: https://libvirt.org/docs.html
fetched_at: 2026-08-21T04:09:31+00:00
---
# Documentation

# Deployment / operation

[Applications](apps.md)
:   Applications known to use libvirt

[Manual pages](manpages/index.md)
:   Manual pages for libvirt tools / daemons

[Windows](windows.md)
:   Downloads for Windows

[macOS](macos.md)
:   Working with libvirt on macOS

[Migration](migration.md)
:   Migrating guests between machines

[Daemons](daemons.md)
:   Overview of the daemons provided by libvirt

[Remote access](remote.md)
:   Enable remote access over TCP

[TLS certs](kbase/tlscerts.md)
:   Generate and deploy x509 certificates for TLS

[Authentication](auth.md)
:   Configure authentication for the libvirt daemon

[Access control](acl.md)
:   Configure access control libvirt APIs with [polkit](aclpolkit.md)

[Logging](logging.md)
:   The library and the daemon logging support

[Audit log](auditlog.md)
:   Audit trail logs for host operations

[Firewall](firewall.md)
:   Firewall and network filter configuration

[Hooks](hooks.md)
:   Hooks for system specific management

[SSH Proxy](ssh-proxy.md)
:   Enable SSH into guests over a VSOCK

[NSS module](nss.md)
:   Enable domain host name translation to IP addresses

[FAQ](https://wiki.libvirt.org/page/FAQ)
:   Frequently asked questions

# Application development

[API reference](https://libvirt.org/html/index.html)
:   Reference manual for the C public API, split in:

    - [common](https://libvirt.org/html/libvirt-libvirt-common.html)
    - [domain](https://libvirt.org/html/libvirt-libvirt-domain.html)
    - [domain checkpoint](https://libvirt.org/html/libvirt-libvirt-domain-checkpoint.html)
    - [domain snapshot](https://libvirt.org/html/libvirt-libvirt-domain-snapshot.html)
    - [error](https://libvirt.org/html/libvirt-virterror.html)
    - [event](https://libvirt.org/html/libvirt-libvirt-event.html)
    - [host](https://libvirt.org/html/libvirt-libvirt-host.html)
    - [interface](https://libvirt.org/html/libvirt-libvirt-interface.html)
    - [network](https://libvirt.org/html/libvirt-libvirt-network.html)
    - [node device](https://libvirt.org/html/libvirt-libvirt-nodedev.html)
    - [network filter](https://libvirt.org/html/libvirt-libvirt-nwfilter.html)
    - [secret](https://libvirt.org/html/libvirt-libvirt-secret.html)
    - [storage](https://libvirt.org/html/libvirt-libvirt-storage.html)
    - [stream](https://libvirt.org/html/libvirt-libvirt-stream.html)

    and the documentation for the API of the additional libs:

    - [admin](https://libvirt.org/html/libvirt-libvirt-admin.html)
    - [QEMU](https://libvirt.org/html/libvirt-libvirt-qemu.html)
    - [LXC](https://libvirt.org/html/libvirt-libvirt-lxc.html)

[XML schemas](format.md)
:   Description of the XML schemas for

    - [domains](formatdomain.md)
    - [networks](formatnetwork.md)
    - [network ports](formatnetworkport.md)
    - [network filtering](formatnwfilter.md)
    - [storage](formatstorage.md)
    - [storage encryption](formatstorageencryption.md)
    - [capabilities](formatcaps.md)
    - [domain capabilities](formatdomaincaps.md)
    - [storage pool capabilities](formatstoragecaps.md)
    - [node devices](formatnode.md)
    - [secrets](formatsecret.md)
    - [snapshots](formatsnapshot.md)
    - [checkpoints](formatcheckpoint.md)
    - [backup jobs](formatbackup.md)

[Language bindings and API modules](bindings.md)
:   Bindings of the libvirt API for
    [c#](csharp.md),
    [go](https://pkg.go.dev/libvirt.org/go/libvirt) ([all go modules](golang.md)),
    [java](https://java.libvirt.org/),
    [ocaml](https://ocaml.libvirt.org/),
    [perl](https://search.cpan.org/dist/Sys-Virt/),
    [python](python.md),
    [php](https://php.libvirt.org),
    [ruby](https://ruby.libvirt.org/)
    and integration API modules for
    [D-Bus](dbus.md)

[URI format](uri.md)
:   The URI formats used for connecting to libvirt

[CGroups](cgroups.md)
:   Control groups integration

[Drivers](drivers.md)
:   Hypervisor specific driver information

[Support guarantees](support.md)
:   Details of support status for various interfaces

[Driver support](hvsupport.md)
:   matrix of API support per hypervisor per release

[Knowledge Base](kbase/index.md)
:   Task oriented guides to key features

# Project development

[Contributor guidelines](hacking.md)
:   General hacking guidelines for contributors

[Docs style guide](styleguide.md)
:   Style guidelines for reStructuredText docs

[Project strategy](strategy.md)
:   Sets a vision for future direction & technical choices

[CI](https://libvirt.org/ci.html)
:   Details on our Continuous Integration

[Upstream issue handling](issue-handling.md)
:   Outlines the process of handling issues as well as describes the supported
    issue types along with their life cycle.

[Bug reports](bugs.md)
:   How and where to report bugs and request features

[Compiling](compiling.md)
:   How to compile libvirt

[Goals](goals.md)
:   Terminology and goals of libvirt API

[API concepts](api.md)
:   The libvirt API concepts

[API extensions](api_extension.md)
:   Adding new public libvirt APIs

[Testing](testing.md)
:   Details various types of testing available for libvirt

[New repo setup](newreposetup.md)
:   Procedure for configuring new git repositories for libvirt

[Libvirt logos](logos/index.md)
:   Libvirt logo files and guideline how to use them
