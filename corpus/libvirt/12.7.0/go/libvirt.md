---
collection: libvirt
version: "12.7.0"
title: "Libvirt Go Language API (with Go modules)"
source_url: https://libvirt.org/go/libvirt.html
fetched_at: 2026-08-21T04:10:46+00:00
---
# Libvirt Go Language API (with Go modules)

The [Go](https://golang.org/) package libvirt.org/go/libvirt provides
[CGo](https://golang.org/cmd/cgo/) binding from the OS native Libvirt API.

This package replaces the obsolete [libvirt.org/libvirt-go](../libvirt-go.md) package in order to switch to using [semver](https://semver.org/) and [Go modules](https://golang.org/ref/mod).
Aside from the changed import path and versioning scheme, the API is fully
compatible with the legacy package.

In general the Go representation is a direct 1-1 mapping from native API
concepts to Go, so the native API documentation should serve as a reference
for most behaviour.

For details of Go specific behaviour consult the
[Go package documentation](https://pkg.go.dev/libvirt.org/go/libvirt).
