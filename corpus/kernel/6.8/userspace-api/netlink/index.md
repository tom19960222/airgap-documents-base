---
collection: kernel
version: "6.8"
title: "Netlink Handbook"
source_url: https://www.kernel.org/doc/html/v6.8/userspace-api/netlink/index.html
fetched_at: 2026-08-21T03:35:27+00:00
---
# Netlink Handbook

Netlink documentation for users.

- [Introduction to Netlink](intro.md)
  - [Opening a socket](intro.md#opening-a-socket)
  - [Generic Netlink](intro.md#generic-netlink)
  - [Advanced topics](intro.md#advanced-topics)
  - [Classic Netlink](intro.md#classic-netlink)
  - [uAPI reference](intro.md#uapi-reference)
- [Using Netlink protocol specifications](intro-specs.md)
  - [Simple CLI](intro-specs.md#simple-cli)
  - [Generating kernel code](intro-specs.md#generating-kernel-code)
  - [YNL lib](intro-specs.md#ynl-lib)
- [Netlink protocol specifications (in YAML)](specs.md)
  - [Compatibility levels](specs.md#compatibility-levels)
  - [Schema structure](specs.md#schema-structure)
  - [genetlink](specs.md#genetlink)
  - [Attribute types](specs.md#attribute-types)
- [Netlink spec C code generation](c-code-gen.md)
  - [Globals](c-code-gen.md#globals)
  - [Definitions](c-code-gen.md#definitions)
  - [Attributes](c-code-gen.md#attributes)
  - [Operations](c-code-gen.md#operations)
  - [Multicast groups](c-code-gen.md#multicast-groups)
  - [Code generation](c-code-gen.md#code-generation)
- [Netlink specification support for legacy Generic Netlink families](genetlink-legacy.md)
  - [Specification](genetlink-legacy.md#specification)
  - [Operations](genetlink-legacy.md#operations)
  - [Other quirks](genetlink-legacy.md#other-quirks)
- [Netlink specification support for raw Netlink families](netlink-raw.md)
  - [Specification](netlink-raw.md#specification)

See also:
:   - [Documentation/core-api/netlink.rst](../../core-api/netlink.md#kernel-netlink)
    - [Documentation/networking/netlink_spec/index.rst](../../networking/netlink_spec/index.md#specs)
