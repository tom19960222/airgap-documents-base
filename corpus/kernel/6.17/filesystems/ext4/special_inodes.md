---
collection: kernel
version: "6.17"
title: "2.3. Special inodes"
source_url: https://www.kernel.org/doc/html/v6.17/filesystems/ext4/special_inodes.html
fetched_at: 2026-09-16T16:53:17+00:00
---
# 2.3. Special inodes

ext4 reserves some inode for special features, as follows:

| inode Number | Purpose |
| --- | --- |
| 0 | Doesn’t exist; there is no inode 0. |
| 1 | List of defective blocks. |
| 2 | Root directory. |
| 3 | User quota. |
| 4 | Group quota. |
| 5 | Boot loader. |
| 6 | Undelete directory. |
| 7 | Reserved group descriptors inode. (“resize inode”) |
| 8 | Journal inode. |
| 9 | The “exclude” inode, for snapshots(?) |
| 10 | Replica inode, used for some non-upstream feature? |
| 11 | Traditional first non-reserved inode. Usually this is the lost+found directory. See s_first_ino in the superblock. |

Note that there are also some inodes allocated from non-reserved inode numbers
for other filesystem features which are not referenced from standard directory
hierarchy. These are generally reference from the superblock. They are:

| Superblock field | Description |
| --- | --- |
| s_lpf_ino | Inode number of lost+found directory. |
| s_prj_quota_inum | Inode number of quota file tracking project quotas |
| s_orphan_file_inum | Inode number of file tracking orphan inodes. |
