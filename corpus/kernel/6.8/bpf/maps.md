---
collection: kernel
version: "6.8"
title: "BPF maps"
source_url: https://www.kernel.org/doc/html/v6.8/bpf/maps.html
fetched_at: 2026-08-21T03:38:41+00:00
---
# BPF maps

BPF 'maps' provide generic storage of different types for sharing data between
kernel and user space. There are several storage types available, including
hash, array, bloom filter and radix-tree. Several of the map types exist to
support specific BPF helpers that perform actions based on the map contents. The
maps are accessed from BPF programs via BPF helpers which are documented in the
[man-pages](https://www.kernel.org/doc/man-pages/) for [bpf-helpers(7)](https://man7.org/linux/man-pages/man7/bpf-helpers.7.html).

BPF maps are accessed from user space via the `bpf` syscall, which provides
commands to create maps, lookup elements, update elements and delete elements.
More details of the BPF syscall are available in [ebpf-syscall](https://docs.kernel.org/userspace-api/ebpf/syscall.html) and in the
[man-pages](https://www.kernel.org/doc/man-pages/) for [bpf(2)](https://man7.org/linux/man-pages/man2/bpf.2.html).

## Map Types

- [BPF_MAP_TYPE_ARRAY and BPF_MAP_TYPE_PERCPU_ARRAY](map_array.md)
- [BPF_MAP_TYPE_BLOOM_FILTER](map_bloom_filter.md)
- [BPF_MAP_TYPE_CGROUP_STORAGE](map_cgroup_storage.md)
- [BPF_MAP_TYPE_CGRP_STORAGE](map_cgrp_storage.md)
- [BPF_MAP_TYPE_CPUMAP](map_cpumap.md)
- [BPF_MAP_TYPE_DEVMAP and BPF_MAP_TYPE_DEVMAP_HASH](map_devmap.md)
- [BPF_MAP_TYPE_HASH, with PERCPU and LRU Variants](map_hash.md)
- [BPF_MAP_TYPE_LPM_TRIE](map_lpm_trie.md)
- [BPF_MAP_TYPE_ARRAY_OF_MAPS and BPF_MAP_TYPE_HASH_OF_MAPS](map_of_maps.md)
- [BPF_MAP_TYPE_QUEUE and BPF_MAP_TYPE_STACK](map_queue_stack.md)
- [BPF_MAP_TYPE_SK_STORAGE](map_sk_storage.md)
- [BPF_MAP_TYPE_SOCKMAP and BPF_MAP_TYPE_SOCKHASH](map_sockmap.md)
- [BPF_MAP_TYPE_XSKMAP](map_xskmap.md)

## Usage Notes

int bpf(int command, union bpf_attr \*attr, u32 size)

Use the `bpf()` system call to perform the operation specified by
`command`. The operation takes parameters provided in `attr`. The `size`
argument is the size of the `union bpf_attr` in `attr`.

**BPF_MAP_CREATE**

Create a map with the desired type and attributes in `attr`:

```c
int fd;
union bpf_attr attr = {
        .map_type = BPF_MAP_TYPE_ARRAY;  /* mandatory */
        .key_size = sizeof(__u32);       /* mandatory */
        .value_size = sizeof(__u32);     /* mandatory */
        .max_entries = 256;              /* mandatory */
        .map_flags = BPF_F_MMAPABLE;
        .map_name = "example_array";
};

fd = bpf(BPF_MAP_CREATE, &attr, sizeof(attr));
```

Returns a process-local file descriptor on success, or negative error in case of
failure. The map can be deleted by calling `close(fd)`. Maps held by open
file descriptors will be deleted automatically when a process exits.

> **Note:**
>
> Valid characters for `map_name` are `A-Z`, `a-z`, `0-9`,
> `'_'` and `'.'`.

**BPF_MAP_LOOKUP_ELEM**

Lookup key in a given map using `attr->map_fd`, `attr->key`,
`attr->value`. Returns zero and stores found elem into `attr->value` on
success, or negative error on failure.

**BPF_MAP_UPDATE_ELEM**

Create or update key/value pair in a given map using `attr->map_fd`, `attr->key`,
`attr->value`. Returns zero on success or negative error on failure.

**BPF_MAP_DELETE_ELEM**

Find and delete element by key in a given map using `attr->map_fd`,
`attr->key`. Returns zero on success or negative error on failure.
