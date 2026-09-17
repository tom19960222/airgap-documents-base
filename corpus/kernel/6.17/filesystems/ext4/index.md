---
collection: kernel
version: "6.17"
title: "ext4 Data Structures and Algorithms"
source_url: https://www.kernel.org/doc/html/v6.17/filesystems/ext4/index.html
fetched_at: 2026-09-16T16:42:06+00:00
---
# ext4 Data Structures and Algorithms

- [1. About this Book](about.md)
  - [1.1. License](about.md#license)
  - [1.2. Terminology](about.md#terminology)
  - [1.3. Other References](about.md#other-references)
- [2. High Level Design](overview.md)
  - [2.1. Blocks](blocks.md)
  - [2.2. Block Groups](blockgroup.md)
  - [2.3. Special inodes](special_inodes.md)
  - [2.4. Block and Inode Allocation Policy](allocators.md)
  - [2.5. Checksums](checksums.md)
  - [2.6. Bigalloc](bigalloc.md)
  - [2.7. Inline Data](inlinedata.md)
  - [2.8. Large Extended Attribute Values](eainode.md)
  - [2.9. Verity files](verity.md)
  - [2.10. Atomic Block Writes](atomic_writes.md)
- [3. Global Structures](globals.md)
  - [3.1. Super Block](super.md)
  - [3.2. Block Group Descriptors](group_descr.md)
  - [3.3. Block and inode Bitmaps](bitmaps.md)
  - [3.4. Inode Table](inode_table.md)
  - [3.5. Multiple Mount Protection](mmp.md)
  - [3.6. Journal (jbd2)](journal.md)
  - [3.7. Orphan file](orphan.md)
- [4. Dynamic Structures](dynamic.md)
  - [4.1. Index Nodes](inodes.md)
  - [4.2. The Contents of inode.i_block](ifork.md)
  - [4.3. Directory Entries](directory.md)
  - [4.4. Extended Attributes](attributes.md)
