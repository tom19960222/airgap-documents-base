---
collection: kernel
version: "6.8"
title: "Devicetree Dynamic Resolver Notes"
source_url: https://www.kernel.org/doc/html/v6.8/devicetree/dynamic-resolution-notes.html
fetched_at: 2026-08-21T03:35:49+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/devicetree/dynamic-resolution-notes.md)

# Devicetree Dynamic Resolver Notes

This document describes the implementation of the in-kernel
DeviceTree resolver, residing in drivers/of/resolver.c

## How the resolver works

The resolver is given as an input an arbitrary tree compiled with the
proper dtc option and having a /plugin/ tag. This generates the
appropriate __fixups__ & __local_fixups__ nodes.

In sequence the resolver works by the following steps:

1. Get the maximum device tree phandle value from the live tree + 1.
2. Adjust all the local phandles of the tree to resolve by that amount.
3. Using the __local__fixups__ node information adjust all local references
   by the same amount.
4. For each property in the __fixups__ node locate the node it references
   in the live tree. This is the label used to tag the node.
5. Retrieve the phandle of the target of the fixup.
6. For each fixup in the property locate the node:property:offset location
   and replace it with the phandle value.
