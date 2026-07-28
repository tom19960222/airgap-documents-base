---
collection: ansible
version: "6"
title: "community.general.filesize module – Create a file with a given size, or resize it if it exists"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/filesize_module.html
fetched_at: 2026-07-27T17:08:54+00:00
---
# community.general.filesize module – Create a file with a given size, or resize it if it exists

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](filesize_module.md#ansible-collections-community-general-filesize-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.filesize`.

New in community.general 3.0.0

- [Synopsis](filesize_module.md#synopsis)
- [Requirements](filesize_module.md#requirements)
- [Parameters](filesize_module.md#parameters)
- [Notes](filesize_module.md#notes)
- [See Also](filesize_module.md#see-also)
- [Examples](filesize_module.md#examples)
- [Return Values](filesize_module.md#return-values)

## [Synopsis](filesize_module.md#id1)

- This module is a simple wrapper around `dd` to create, extend or truncate a file, given its size. It can be used to manage swap files (that require contiguous blocks) or alternatively, huge sparse files.

## [Requirements](filesize_module.md#id2)

The below requirements are needed on the host that executes this module.

- dd (Data Duplicator) in PATH

## [Parameters](filesize_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **blocksize**  any | Size of blocks, in bytes if not followed by a multiplicative suffix.  The numeric value (before the unit) `MUST` be an integer (or a `float` if it equals an integer).  If not set, the size of blocks is guessed from the OS and commonly results in `512` or `4096` bytes, that is used internally by the module or when *size* has no unit. |
| **force**  boolean | Whether or not to overwrite the file if it exists, in other words, to truncate it from 0. When `true`, the module is not idempotent, that means it always reports *changed=true*.  *force=true* and *sparse=true* are mutually exclusive.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **path**  path / required | Path of the regular file to create or resize. |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **size**  any / required | Requested size of the file.  The value is a number (either `int` or `float`) optionally followed by a multiplicative suffix, that can be one of `B` (bytes), `KB` or `kB` (= 1000B), `MB` or `mB` (= 1000kB), `GB` or `gB` (= 1000MB), and so on for `T`, `P`, `E`, `Z` and `Y`; or alternatively one of `K`, `k` or `KiB` (= 1024B); `M`, `m` or `MiB` (= 1024KiB); `G`, `g` or `GiB` (= 1024MiB); and so on.  If the multiplicative suffix is not provided, the value is treated as an integer number of blocks of *blocksize* bytes each (float values are rounded to the closest integer).  When the *size* value is equal to the current file size, does nothing.  When the *size* value is bigger than the current file size, bytes from *source* (if *sparse* is not `false`) are appended to the file without truncating it, in other words, without modifying the existing bytes of the file.  When the *size* value is smaller than the current file size, it is truncated to the requested value without modifying bytes before this value.  That means that a file of any arbitrary size can be grown to any other arbitrary size, and then resized down to its initial size without modifying its initial content. |
| **source**  path | Device or file that provides input data to provision the file.  This parameter is ignored when *sparse=true*.  Default: `"/dev/zero"` |
| **sparse**  boolean | Whether or not the file to create should be a sparse file.  This option is effective only on newly created files, or when growing a file, only for the bytes to append.  This option is not supported on OSes or filesystems not supporting sparse files.  *force=true* and *sparse=true* are mutually exclusive.  Choices:   - `false` ← (default) - `true` |
| **unsafe_writes**  boolean | This option is silently ignored. This module always modifies file size in-place.  Choices:   - `false` ← (default) - `true` |

## [Notes](filesize_module.md#id4)

> **Note:**
>
> - This module supports `check_mode` and `diff`.

## [See Also](filesize_module.md#id5)

> **See also:**
>
> [dd(1) manpage for Linux](https://man7.org/linux/man-pages/man1/dd.1.html)
> :   Manual page of the GNU/Linux’s dd implementation (from GNU coreutils).
>
> [dd(1) manpage for IBM AIX](https://www.ibm.com/support/knowledgecenter/ssw_aix_72/d_commands/dd.html)
> :   Manual page of the IBM AIX’s dd implementation.
>
> [dd(1) manpage for Mac OSX](https://www.unix.com/man-page/osx/1/dd/)
> :   Manual page of the Mac OSX’s dd implementation.
>
> [dd(1M) manpage for Solaris](https://docs.oracle.com/cd/E36784_01/html/E36871/dd-1m.html)
> :   Manual page of the Oracle Solaris’s dd implementation.
>
> [dd(1) manpage for FreeBSD](https://www.freebsd.org/cgi/man.cgi?dd(1))
> :   Manual page of the FreeBSD’s dd implementation.
>
> [dd(1) manpage for OpenBSD](https://man.openbsd.org/dd)
> :   Manual page of the OpenBSD’s dd implementation.
>
> [dd(1) manpage for NetBSD](https://man.netbsd.org/dd.1)
> :   Manual page of the NetBSD’s dd implementation.
>
> [busybox(1) manpage for Linux](https://www.unix.com/man-page/linux/1/busybox)
> :   Manual page of the GNU/Linux’s busybox, that provides its own dd implementation.

## [Examples](filesize_module.md#id6)

```yaml+jinja
- name: Create a file of 1G filled with null bytes
  community.general.filesize:
    path: /var/bigfile
    size: 1G

- name: Extend the file to 2G (2*1024^3)
  community.general.filesize:
    path: /var/bigfile
    size: 2G

- name: Reduce the file to 2GB (2*1000^3)
  community.general.filesize:
    path: /var/bigfile
    size: 2GB

- name: Fill a file with random bytes for backing a LUKS device
  community.general.filesize:
    path: ~/diskimage.luks
    size: 512.0 MiB
    source: /dev/urandom

- name: Take a backup of MBR boot code into a file, overwriting it if it exists
  community.general.filesize:
    path: /media/sdb1/mbr.bin
    size: 440B
    source: /dev/sda
    force: true

- name: Create/resize a sparse file of/to 8TB
  community.general.filesize:
    path: /var/local/sparsefile
    size: 8TB
    sparse: true

- name: Create a file with specific size and attributes, to be used as swap space
  community.general.filesize:
    path: /var/swapfile
    size: 2G
    blocksize: 512B
    mode: u=rw,go=
    owner: root
    group: root
```

## [Return Values](filesize_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cmd**  string | Command executed to create or resize the file.  Returned: when changed or failed  Sample: `"/usr/bin/dd if=/dev/zero of=/var/swapfile bs=1048576 seek=3072 count=1024"` |
| **filesize**  dictionary | Dictionary of sizes related to the file.  Returned: always |
| **blocks**  integer | Number of blocks in the file.  Returned: success  Sample: `500` |
| **blocksize**  integer | Size of the blocks in bytes.  Returned: success  Sample: `1024` |
| **bytes**  integer | Size of the file, in bytes, as the product of `blocks` and `blocksize`.  Returned: success  Sample: `512000` |
| **iec**  string | Size of the file, in human-readable format, following IEC standard.  Returned: success  Sample: `"500.0 KiB"` |
| **si**  string | Size of the file, in human-readable format, following SI standard.  Returned: success  Sample: `"512.0 kB"` |
| **path**  string | Realpath of the file if it is a symlink, otherwise the same than module’s param.  Returned: always  Sample: `"/var/swap0"` |
| **size_diff**  integer | Difference (positive or negative) between old size and new size, in bytes.  Returned: always  Sample: `-1234567890` |

### Authors

- quidame (@quidame)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
