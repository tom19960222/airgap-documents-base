---
collection: libvirt
version: "12.7.0"
title: "Libvirt Go XML parsing API (with Go modules)"
source_url: https://libvirt.org/go/libvirtxml.html
fetched_at: 2026-08-21T04:10:46+00:00
---
# Libvirt Go XML parsing API (with Go modules)

The [Go](https://golang.org/) package libvirt.org/go/libvirtxml provides
annotated Go struct definitions for parsing (and formatting) XML documents used
with libvirt APIs.

This package replaces the obsolete [libvirt.org/libvirt-go-xml](../libvirt-go-xml.md) package in order to switch to using [semver](https://semver.org/) and [Go modules](https://golang.org/ref/mod).
Aside from the changed import path and versioning scheme, the API is fully
compatible with the original package.

For details of Go specific behaviour consult the
[Go package documentation](https://pkg.go.dev/libvirt.org/go/libvirtxml).
