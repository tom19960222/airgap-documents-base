---
collection: kernel
version: "6.17"
title: "4. Dynamic Structures"
source_url: https://www.kernel.org/doc/html/v6.17/filesystems/ext4/dynamic.html
fetched_at: 2026-09-16T16:42:09+00:00
---
# 4. Dynamic Structures

Dynamic metadata are created on the fly when files and blocks are
allocated to files.

- [4.1. Index Nodes](inodes.md)
  - [4.1.1. Inode Size](inodes.md#inode-size)
  - [4.1.2. Finding an Inode](inodes.md#finding-an-inode)
  - [4.1.3. Inode Timestamps](inodes.md#inode-timestamps)
- [4.2. The Contents of inode.i_block](ifork.md)
  - [4.2.1. Symbolic Links](ifork.md#symbolic-links)
  - [4.2.2. Direct/Indirect Block Addressing](ifork.md#direct-indirect-block-addressing)
  - [4.2.3. Extent Tree](ifork.md#extent-tree)
  - [4.2.4. Inline Data](ifork.md#inline-data)
- [4.3. Directory Entries](directory.md)
  - [4.3.1. Linear (Classic) Directories](directory.md#linear-classic-directories)
  - [4.3.2. Hash Tree Directories](directory.md#hash-tree-directories)
- [4.4. Extended Attributes](attributes.md)
  - [4.4.1. Attribute Name Indices](attributes.md#attribute-name-indices)
  - [4.4.2. POSIX ACLs](attributes.md#posix-acls)
