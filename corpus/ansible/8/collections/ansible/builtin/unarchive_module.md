---
collection: ansible
version: "8"
title: "ansible.builtin.unarchive module – Unpacks an archive after (optionally) copying it from the local machine"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/unarchive_module.html
fetched_at: 2026-07-28T01:04:14+00:00
---
# ansible.builtin.unarchive module – Unpacks an archive after (optionally) copying it from the local machine

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `unarchive` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.unarchive` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](unarchive_module.md#synopsis)
- [Parameters](unarchive_module.md#parameters)
- [Attributes](unarchive_module.md#attributes)
- [Notes](unarchive_module.md#notes)
- [See Also](unarchive_module.md#see-also)
- [Examples](unarchive_module.md#examples)
- [Return Values](unarchive_module.md#return-values)

## [Synopsis](unarchive_module.md#id1)

- The `unarchive` module unpacks an archive. It will not unpack a compressed file that does not contain an archive.
- By default, it will copy the source file from the local system to the target before unpacking.
- Set `remote_src=yes` to unpack an archive which already exists on the target.
- If checksum validation is desired, use [ansible.builtin.get_url](get_url_module.md#ansible-collections-ansible-builtin-get-url-module) or [ansible.builtin.uri](uri_module.md#ansible-collections-ansible-builtin-uri-module) instead to fetch the file and set `remote_src=yes`.
- For Windows targets, use the [community.windows.win_unzip](../../community/windows/win_unzip_module.md#ansible-collections-community-windows-win-unzip-module) module instead.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](unarchive_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **copy**  boolean | If true, the file is copied from local controller to the managed (remote) node, otherwise, the plugin will look for src archive on the managed machine.  This option has been deprecated in favor of `remote_src`.  This option is mutually exclusive with `remote_src`.  **Choices:**   - `false` - `true` ← (default) |
| **creates**  path | If the specified absolute path (file or directory) already exists, this step will **not** be run.  The specified absolute path (file or directory) must be below the base path given with `dest:`. |
| **decrypt**  boolean | This option controls the autodecryption of source files using vault.  **Choices:**   - `false` - `true` ← (default) |
| **dest**  path / required | Remote absolute path where the archive should be unpacked.  The given path must exist. Base directory is not created by this module. |
| **exclude**  list / elements=string | List the directory and file entries that you would like to exclude from the unarchive action.  Mutually exclusive with `include`.  **Default:** `[]` |
| **extra_opts**  list / elements=string | Specify additional options by passing in an array.  Each space-separated command-line option should be a new element of the array. See examples.  Command-line options with multiple elements must use multiple lines in the array, one for each element.  **Default:** `[]` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **include**  list / elements=string  *added in ansible-core 2.11* | List of directory and file entries that you would like to extract from the archive. If `include` is not empty, only files listed here will be extracted.  Mutually exclusive with `exclude`.  **Default:** `[]` |
| **io_buffer_size**  integer  *added in ansible-core 2.12* | Size of the volatile memory buffer that is used for extracting files from the archive in bytes.  **Default:** `65536` |
| **keep_newer**  boolean | Do not replace existing files that are newer than files from the archive.  **Choices:**   - `false` ← (default) - `true` |
| **list_files**  boolean | If set to True, return the list of files that are contained in the tarball.  **Choices:**   - `false` ← (default) - `true` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must give Ansible enough information to parse them correctly. For consistent results, quote octal numbers (for example, `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number. Adding a leading zero (for example, `0755`) works sometimes, but can fail in loops and some other circumstances.  Giving Ansible a number without following either of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership.  Specifying a numeric username will be assumed to be a user ID and not a username. Avoid numeric usernames to avoid this confusion. |
| **remote_src**  boolean | Set to `true` to indicate the archived file is already on the remote system and not local to the Ansible controller.  This option is mutually exclusive with `copy`.  **Choices:**   - `false` ← (default) - `true` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **src**  path / required | If `remote_src=no` (default), local path to archive file to copy to the target server; can be absolute or relative. If `remote_src=yes`, path on the target server to existing archive file to unpack.  If `remote_src=yes` and `src` contains `://`, the remote machine will download the file from the URL first. (version_added 2.0). This is only for simple cases, for full download support use the [ansible.builtin.get_url](get_url_module.md#ansible-collections-ansible-builtin-get-url-module) module. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | This only applies if using a https URL as the source of the file.  This should only set to `false` used on personally controlled sites using self-signed certificate.  Prior to 2.2 the code worked as if this was set to `true`.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](unarchive_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action** | **Support:** **full** | Indicates this has a corresponding action plugin so some parts of the options can be executed on the controller |
| **async** | **Support:** **none** | Supports being used with the `async` keyword |
| **bypass_host_loop** | **Support:** **none** | Forces a ‘global’ task that does not execute per host, this bypasses per host templating and serial, throttle and other loop considerations  Conditionals will work as if `run_once` is being used, variables used will be from the first available host  This action will not work normally outside of lockstep strategies |
| **check_mode** | **Support:** **partial**  Not supported for gzipped tar files. | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **partial**  Uses gtar’s `--diff` arg to calculate if changed or not. If this `arg` is not supported, it will always unpack the archive. | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |
| **safe_file_operations** | **Support:** **none** | Uses Ansible’s strict file operation functions to ensure proper permissions and avoid data corruption |
| **vault** | **Support:** **full** | Can automatically decrypt Ansible vaulted files |

## [Notes](unarchive_module.md#id4)

> **Note:**
>
> - Requires `zipinfo` and `gtar`/`unzip` command on target host.
> - Requires `zstd` command on target host to expand *.tar.zst* files.
> - Can handle *.zip* files using `unzip` as well as *.tar*, *.tar.gz*, *.tar.bz2*, *.tar.xz*, and *.tar.zst* files using `gtar`.
> - Does not handle *.gz* files, *.bz2* files, *.xz*, or *.zst* files that do not contain a *.tar* archive.
> - Existing files/directories in the destination which are not in the archive are not touched. This is the same behavior as a normal archive extraction.
> - Existing files/directories in the destination which are not in the archive are ignored for purposes of deciding if the archive should be unpacked or not.

## [See Also](unarchive_module.md#id5)

> **See also:**
>
> [community.general.archive](../../community/general/archive_module.md#ansible-collections-community-general-archive-module)
> :   Creates a compressed archive of one or more files or trees.
>
> [community.general.iso_extract](../../community/general/iso_extract_module.md#ansible-collections-community-general-iso-extract-module)
> :   Extract files from an ISO image.
>
> [community.windows.win_unzip](../../community/windows/win_unzip_module.md#ansible-collections-community-windows-win-unzip-module)
> :   Unzips compressed files and archives on the Windows node.

## [Examples](unarchive_module.md#id6)

```yaml+jinja
- name: Extract foo.tgz into /var/lib/foo
  ansible.builtin.unarchive:
    src: foo.tgz
    dest: /var/lib/foo

- name: Unarchive a file that is already on the remote machine
  ansible.builtin.unarchive:
    src: /tmp/foo.zip
    dest: /usr/local/bin
    remote_src: yes

- name: Unarchive a file that needs to be downloaded (added in 2.0)
  ansible.builtin.unarchive:
    src: https://example.com/example.zip
    dest: /usr/local/bin
    remote_src: yes

- name: Unarchive a file with extra options
  ansible.builtin.unarchive:
    src: /tmp/foo.zip
    dest: /usr/local/bin
    extra_opts:
    - --transform
    - s/^xxx/yyy/
```

## [Return Values](unarchive_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dest**  string | Path to the destination directory.  **Returned:** always  **Sample:** `"/opt/software"` |
| **files**  list / elements=string | List of all the files in the archive.  **Returned:** When *list_files* is True  **Sample:** `["[\"file1\"", " \"file2\"]"]` |
| **gid**  integer | Numerical ID of the group that owns the destination directory.  **Returned:** always  **Sample:** `1000` |
| **group**  string | Name of the group that owns the destination directory.  **Returned:** always  **Sample:** `"librarians"` |
| **handler**  string | Archive software handler used to extract and decompress the archive.  **Returned:** always  **Sample:** `"TgzArchive"` |
| **mode**  string | String that represents the octal permissions of the destination directory.  **Returned:** always  **Sample:** `"0755"` |
| **owner**  string | Name of the user that owns the destination directory.  **Returned:** always  **Sample:** `"paul"` |
| **size**  integer | The size of destination directory in bytes. Does not include the size of files or subdirectories contained within.  **Returned:** always  **Sample:** `36` |
| **src**  string | The source archive’s path.  If *src* was a remote web URL, or from the local ansible controller, this shows the temporary location where the download was stored.  **Returned:** always  **Sample:** `"/home/paul/test.tar.gz"` |
| **state**  string | State of the destination. Effectively always “directory”.  **Returned:** always  **Sample:** `"directory"` |
| **uid**  integer | Numerical ID of the user that owns the destination directory.  **Returned:** always  **Sample:** `1000` |

### Authors

- Michael DeHaan

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
