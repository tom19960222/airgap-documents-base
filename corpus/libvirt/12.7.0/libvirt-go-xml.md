---
collection: libvirt
version: "12.7.0"
title: "Obsolete libvirt Go XML parsing API (no Go modules)"
source_url: https://libvirt.org/libvirt-go-xml.html
fetched_at: 2026-08-21T04:10:48+00:00
---
# Obsolete libvirt Go XML parsing API (no Go modules)

The obsolete [Go](https://golang.org/) package libvirt.org/libvirt-go-xml
provided annotated Go struct definitions for parsing (and formatting) XML
documents used with libvirt APIs.

This package is replaced by the new [libvirt.org/go/libvirtxml](go/libvirtxml.md) package in order to switch to using [semver](https://semver.org/) and [Go modules](https://golang.org/ref/mod).
Aside from the changed import path and versioning scheme, the new package API
is fully compatible with this legacy package.

Software currently using this package will keep working, but no further
development will take place. libvirt XML scheme elements/attributes introduced
after 7.4.0 will never be available. Authors are strongly recommended to switch
imports to point to the new package, to prepare for future Go toolchains
which will mandate Go module support and semver.

For details of Go specific behaviour consult the
[Go package documentation](https://pkg.go.dev/libvirt.org/libvirt-go-xml).
