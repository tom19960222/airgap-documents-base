---
collection: ansible
version: "8"
title: "ansible.posix.mount module – Control active and configured mount points"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/mount_module.html
fetched_at: 2026-07-28T01:09:28+00:00
---
# ansible.posix.mount module – Control active and configured mount points

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
>
> To use it in a playbook, specify: `ansible.posix.mount`.

New in ansible.posix 1.0.0

- [Synopsis](mount_module.md#synopsis)
- [Parameters](mount_module.md#parameters)
- [Notes](mount_module.md#notes)
- [Examples](mount_module.md#examples)

## [Synopsis](mount_module.md#id1)

- This module controls active and configured mount points in `/etc/fstab`.

## [Parameters](mount_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **boot**  boolean | Determines if the filesystem should be mounted on boot.  Only applies to Solaris and Linux systems.  For Solaris systems, `true` will set `yes` as the value of mount at boot in */etc/vfstab*.  For Linux, FreeBSD, NetBSD and OpenBSD systems, `false` will add `noauto` to mount options in */etc/fstab*.  To avoid mount option conflicts, if `noauto` specified in `opts`, mount module will ignore `boot`.  This parameter is ignored when *state* is set to `ephemeral`.  **Choices:**   - `false` - `true` ← (default) |
| **dump**  string | Dump (see fstab(5)).  Note that if set to `null` and *state* set to `present`, it will cease to work and duplicate entries will be made with subsequent runs.  Has no effect on Solaris systems or when used with `ephemeral`.  **Default:** `"0"` |
| **fstab**  string | File to use instead of `/etc/fstab`.  You should not use this option unless you really know what you are doing.  This might be useful if you need to configure mountpoints in a chroot environment.  OpenBSD does not allow specifying alternate fstab files with mount so do not use this on OpenBSD with any state that operates on the live filesystem.  This parameter defaults to /etc/fstab or /etc/vfstab on Solaris.  This parameter is ignored when *state* is set to `ephemeral`. |
| **fstype**  string | Filesystem type.  Required when *state* is `present`, `mounted` or `ephemeral`. |
| **opts**  string | Mount options (see fstab(5), or vfstab(4) on Solaris). |
| **passno**  string | Passno (see fstab(5)).  Note that if set to `null` and *state* set to `present`, it will cease to work and duplicate entries will be made with subsequent runs.  Deprecated on Solaris systems. Has no effect when used with `ephemeral`.  **Default:** `"0"` |
| **path**  aliases: name  path / required | Path to the mount point (e.g. `/mnt/files`).  Before Ansible 2.3 this option was only usable as *dest*, *destfile* and *name*. |
| **src**  path | Device (or NFS volume, or something else) to be mounted on *path*.  Required when *state* set to `present`, `mounted` or `ephemeral`. |
| **state**  string / required | If `mounted`, the device will be actively mounted and appropriately configured in *fstab*. If the mount point is not present, the mount point will be created.  If `unmounted`, the device will be unmounted without changing *fstab*.  `present` only specifies that the device is to be configured in *fstab* and does not trigger or require a mount.  `ephemeral` only specifies that the device is to be mounted, without changing *fstab*. If it is already mounted, a remount will be triggered. This will always return changed=True. If the mount point *path* has already a device mounted on, and its source is different than *src*, the module will fail to avoid unexpected unmount or mount point override. If the mount point is not present, the mount point will be created. The *fstab* is completely ignored. This option is added in version 1.5.0.  `absent` specifies that the device mount’s entry will be removed from *fstab* and will also unmount the device and remove the mount point.  `remounted` specifies that the device will be remounted for when you want to force a refresh on the mount itself (added in 2.9). This will always return changed=true. If *opts* is set, the options will be applied to the remount, but will not change *fstab*. Additionally, if *opts* is set, and the remount command fails, the module will error to prevent unexpected mount changes. Try using `mounted` instead to work around this issue. `remounted` expects the mount point to be present in the *fstab*. To remount a mount point not registered in *fstab*, use `ephemeral` instead, especially with BSD nodes.  `absent_from_fstab` specifies that the device mount’s entry will be removed from *fstab*. This option does not unmount it or delete the mountpoint.  **Choices:**   - `"absent"` - `"absent_from_fstab"` - `"mounted"` - `"present"` - `"unmounted"` - `"remounted"` - `"ephemeral"` |

## [Notes](mount_module.md#id3)

> **Note:**
>
> - As of Ansible 2.3, the *name* option has been changed to *path* as default, but *name* still works as well.
> - Using `remounted` with *opts* set may create unexpected results based on the existing options already defined on mount, so care should be taken to ensure that conflicting options are not present before hand.

## [Examples](mount_module.md#id4)

```yaml+jinja
# Before 2.3, option 'name' was used instead of 'path'
- name: Mount DVD read-only
  ansible.posix.mount:
    path: /mnt/dvd
    src: /dev/sr0
    fstype: iso9660
    opts: ro,noauto
    state: present

- name: Mount up device by label
  ansible.posix.mount:
    path: /srv/disk
    src: LABEL=SOME_LABEL
    fstype: ext4
    state: present

- name: Mount up device by UUID
  ansible.posix.mount:
    path: /home
    src: UUID=b3e48f45-f933-4c8e-a700-22a159ec9077
    fstype: xfs
    opts: noatime
    state: present

- name: Unmount a mounted volume
  ansible.posix.mount:
    path: /tmp/mnt-pnt
    state: unmounted

- name: Remount a mounted volume
  ansible.posix.mount:
    path: /tmp/mnt-pnt
    state: remounted

# The following will not save changes to fstab, and only be temporary until
# a reboot, or until calling "state: unmounted" followed by "state: mounted"
# on the same "path"
- name: Remount a mounted volume and append exec to the existing options
  ansible.posix.mount:
    path: /tmp
    state: remounted
    opts: exec

- name: Mount and bind a volume
  ansible.posix.mount:
    path: /system/new_volume/boot
    src: /boot
    opts: bind
    state: mounted
    fstype: none

- name: Mount an NFS volume
  ansible.posix.mount:
    src: 192.168.1.100:/nfs/ssd/shared_data
    path: /mnt/shared_data
    opts: rw,sync,hard
    state: mounted
    fstype: nfs

- name: Mount NFS volumes with noauto according to boot option
  ansible.posix.mount:
    src: 192.168.1.100:/nfs/ssd/shared_data
    path: /mnt/shared_data
    opts: rw,sync,hard
    boot: false
    state: mounted
    fstype: nfs

- name: Mount ephemeral SMB volume
  ansible.posix.mount:
    src: //192.168.1.200/share
    path: /mnt/smb_share
    opts: "rw,vers=3,file_mode=0600,dir_mode=0700,dom={{ ad_domain }},username={{ ad_username }},password={{ ad_password }}"
    fstype: cifs
    state: ephemeral
```

### Authors

- Ansible Core Team
- Seth Vidal (@skvidal)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
