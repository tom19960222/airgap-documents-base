---
collection: kernel
version: "6.17"
title: "3.4. Inode Table"
source_url: https://www.kernel.org/doc/html/v6.17/filesystems/ext4/inode_table.html
fetched_at: 2026-09-16T16:53:24+00:00
---
# 3.4. Inode Table

Inode tables are statically allocated at mkfs time. Each block group
descriptor points to the start of the table, and the superblock records
the number of inodes per group. See [inode documentation](inodes.md)
for more information on inode table layout.
