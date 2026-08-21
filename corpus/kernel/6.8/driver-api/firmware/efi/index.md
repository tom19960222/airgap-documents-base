---
collection: kernel
version: "6.8"
title: "UEFI Support"
source_url: https://www.kernel.org/doc/html/v6.8/driver-api/firmware/efi/index.html
fetched_at: 2026-08-21T03:32:13+00:00
---
# UEFI Support

## UEFI stub library functions

efi_status_t efi_get_memory_map(struct efi_boot_memmap \*\*map, bool install_cfg_tbl)
:   get memory map

**Parameters**

`struct efi_boot_memmap **map`
:   pointer to memory map pointer to which to assign the
    newly allocated memory map

`bool install_cfg_tbl`
:   whether or not to install the boot memory map as a
    configuration table

**Description**

Retrieve the UEFI memory map. The allocated memory leaves room for
up to EFI_MMAP_NR_SLACK_SLOTS additional memory map entries.

**Return**

status code

efi_status_t efi_allocate_pages(unsigned long size, unsigned long \*addr, unsigned long max)
:   Allocate memory pages

**Parameters**

`unsigned long size`
:   minimum number of bytes to allocate

`unsigned long *addr`
:   On return the address of the first allocated page. The first
    allocated page has alignment EFI_ALLOC_ALIGN which is an
    architecture dependent multiple of the page size.

`unsigned long max`
:   the address that the last allocated memory page shall not
    exceed

**Description**

Allocate pages as EFI_LOADER_DATA. The allocated pages are aligned according
to EFI_ALLOC_ALIGN. The last allocated page will not exceed the address
given by **max**.

**Return**

status code

void efi_free(unsigned long size, unsigned long addr)
:   free memory pages

**Parameters**

`unsigned long size`
:   size of the memory area to free in bytes

`unsigned long addr`
:   start of the memory area to free (must be EFI_PAGE_SIZE
    aligned)

**Description**

**size** is rounded up to a multiple of EFI_ALLOC_ALIGN which is an
architecture specific multiple of EFI_PAGE_SIZE. So this function should
only be used to return pages allocated with [`efi_allocate_pages()`](index.md#c.efi_allocate_pages "efi_allocate_pages") or
efi_low_alloc_above().
