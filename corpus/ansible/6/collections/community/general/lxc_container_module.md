---
collection: ansible
version: "6"
title: "community.general.lxc_container module – Manage LXC Containers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lxc_container_module.html
fetched_at: 2026-07-27T17:10:38+00:00
---
# community.general.lxc_container module – Manage LXC Containers

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
> see [Requirements](lxc_container_module.md#ansible-collections-community-general-lxc-container-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lxc_container`.

- [Synopsis](lxc_container_module.md#synopsis)
- [Requirements](lxc_container_module.md#requirements)
- [Parameters](lxc_container_module.md#parameters)
- [Notes](lxc_container_module.md#notes)
- [Examples](lxc_container_module.md#examples)
- [Return Values](lxc_container_module.md#return-values)

## [Synopsis](lxc_container_module.md#id1)

- Management of LXC containers.

## [Requirements](lxc_container_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxc >= 2.0 # OS package
- python3 >= 3.5 # OS Package
- python3-lxc # OS Package

## [Parameters](lxc_container_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **archive**  boolean | Create an archive of a container.  This will create a tarball of the running container.  Choices:   - `false` ← (default) - `true` |
| **archive_compression**  string | Type of compression to use when creating an archive of a running container.  Choices:   - `"gzip"` ← (default) - `"bzip2"` - `"none"` |
| **archive_path**  path | Path the save the archived container.  If the path does not exist the archive method will attempt to create it. |
| **backing_store**  string | Backend storage type for the container.  Choices:   - `"dir"` ← (default) - `"lvm"` - `"loop"` - `"btrfs"` - `"overlayfs"` - `"zfs"` |
| **clone_name**  string | Name of the new cloned server.  This is only used when state is clone. |
| **clone_snapshot**  boolean | Create a snapshot a container when cloning.  This is not supported by all container storage backends.  Enabling this may fail if the backing store does not support snapshots.  Choices:   - `false` ← (default) - `true` |
| **config**  path | Path to the LXC configuration file. |
| **container_command**  string | Run a command within a container. |
| **container_config**  list / elements=string | A list of `key=value` options to use when configuring a container. |
| **container_log**  boolean | Enable a container log for host actions to the container.  Choices:   - `false` ← (default) - `true` |
| **container_log_level**  string | Set the log level for a container where *container_log* was set.  Choices:   - `"Info"` - `"info"` - `"INFO"` ← (default) - `"Error"` - `"error"` - `"ERROR"` - `"Debug"` - `"debug"` - `"DEBUG"` |
| **directory**  path | Place rootfs directory under DIR. |
| **fs_size**  string | File system Size.  Default: `"5G"` |
| **fs_type**  string | Create fstype TYPE.  Default: `"ext4"` |
| **lv_name**  string | Name of the logical volume, defaults to the container name.  If not specified, it defaults to `$CONTAINER_NAME`. |
| **lxc_path**  path | Place container under `PATH`. |
| **name**  string / required | Name of a container. |
| **state**  string | Define the state of a container.  If you clone a container using *clone_name* the newly cloned container created in a stopped state.  The running container will be stopped while the clone operation is happening and upon completion of the clone the original container state will be restored.  Choices:   - `"started"` ← (default) - `"stopped"` - `"restarted"` - `"absent"` - `"frozen"` - `"clone"` |
| **template**  string | Name of the template to use within an LXC create.  Default: `"ubuntu"` |
| **template_options**  string | Template options when building the container. |
| **thinpool**  string | Use LVM thin pool called TP. |
| **vg_name**  string | If backend store is lvm, specify the name of the volume group.  Default: `"lxc"` |
| **zfs_root**  string | Create zfs under given zfsroot. |

## [Notes](lxc_container_module.md#id4)

> **Note:**
>
> - Containers must have a unique name. If you attempt to create a container with a name that already exists in the users namespace the module will simply return as “unchanged”.
> - The *container_command* can be used with any state except `absent`. If used with state `stopped` the container will be `started`, the command executed, and then the container `stopped` again. Likewise if *state=stopped* and the container does not exist it will be first created, `started`, the command executed, and then `stopped`. If you use a “|” in the variable you can use common script formatting within the variable itself. The *container_command* option will always execute as BASH. When using *container_command*, a log file is created in the `/tmp/` directory which contains both `stdout` and `stderr` of any command executed.
> - If *archive=true* the system will attempt to create a compressed tarball of the running container. The *archive* option supports LVM backed containers and will create a snapshot of the running container when creating the archive.
> - If your distro does not have a package for `python3-lxc`, which is a requirement for this module, it can be installed from source at <https://github.com/lxc/python3-lxc> or installed via pip using the package name `lxc`.

## [Examples](lxc_container_module.md#id5)

```yaml+jinja
- name: Create a started container
  community.general.lxc_container:
    name: test-container-started
    container_log: true
    template: ubuntu
    state: started
    template_options: --release trusty

- name: Create a stopped container
  community.general.lxc_container:
    name: test-container-stopped
    container_log: true
    template: ubuntu
    state: stopped
    template_options: --release trusty

- name: Create a frozen container
  community.general.lxc_container:
    name: test-container-frozen
    container_log: true
    template: ubuntu
    state: frozen
    template_options: --release trusty
    container_command: |
      echo 'hello world.' | tee /opt/started-frozen

# Create filesystem container, configure it, and archive it, and start it.
- name: Create filesystem container
  community.general.lxc_container:
    name: test-container-config
    backing_store: dir
    container_log: true
    template: ubuntu
    state: started
    archive: true
    archive_compression: none
    container_config:
      - "lxc.aa_profile=unconfined"
      - "lxc.cgroup.devices.allow=a *:* rmw"
    template_options: --release trusty

# Create an lvm container, run a complex command in it, add additional
# configuration to it, create an archive of it, and finally leave the container
# in a frozen state. The container archive will be compressed using bzip2
- name: Create a frozen lvm container
  community.general.lxc_container:
    name: test-container-lvm
    container_log: true
    template: ubuntu
    state: frozen
    backing_store: lvm
    template_options: --release trusty
    container_command: |
      apt-get update
      apt-get install -y vim lxc-dev
      echo 'hello world.' | tee /opt/started
      if [[ -f "/opt/started" ]]; then
          echo 'hello world.' | tee /opt/found-started
      fi
    container_config:
      - "lxc.aa_profile=unconfined"
      - "lxc.cgroup.devices.allow=a *:* rmw"
    archive: true
    archive_compression: bzip2
  register: lvm_container_info

- name: Debug info on container "test-container-lvm"
  ansible.builtin.debug:
    var: lvm_container_info

- name: Run a command in a container and ensure its in a "stopped" state.
  community.general.lxc_container:
    name: test-container-started
    state: stopped
    container_command: |
      echo 'hello world.' | tee /opt/stopped

- name: Run a command in a container and ensure its it in a "frozen" state.
  community.general.lxc_container:
    name: test-container-stopped
    state: frozen
    container_command: |
      echo 'hello world.' | tee /opt/frozen

- name: Start a container
  community.general.lxc_container:
    name: test-container-stopped
    state: started

- name: Run a command in a container and then restart it
  community.general.lxc_container:
    name: test-container-started
    state: restarted
    container_command: |
      echo 'hello world.' | tee /opt/restarted

- name: Run a complex command within a "running" container
  community.general.lxc_container:
    name: test-container-started
    container_command: |
      apt-get update
      apt-get install -y curl wget vim apache2
      echo 'hello world.' | tee /opt/started
      if [[ -f "/opt/started" ]]; then
          echo 'hello world.' | tee /opt/found-started
      fi

# Create an archive of an existing container, save the archive to a defined
# path and then destroy it.
- name: Archive container
  community.general.lxc_container:
    name: test-container-started
    state: absent
    archive: true
    archive_path: /opt/archives

# Create a container using overlayfs, create an archive of it, create a
# snapshot clone of the container and and finally leave the container
# in a frozen state. The container archive will be compressed using gzip.
- name: Create an overlayfs container archive and clone it
  community.general.lxc_container:
    name: test-container-overlayfs
    container_log: true
    template: ubuntu
    state: started
    backing_store: overlayfs
    template_options: --release trusty
    clone_snapshot: true
    clone_name: test-container-overlayfs-clone-snapshot
    archive: true
    archive_compression: gzip
  register: clone_container_info

- name: Debug info on container "test-container"
  ansible.builtin.debug:
    var: clone_container_info

- name: Clone a container using snapshot
  community.general.lxc_container:
    name: test-container-overlayfs-clone-snapshot
    backing_store: overlayfs
    clone_name: test-container-overlayfs-clone-snapshot2
    clone_snapshot: true

- name: Create a new container and clone it
  community.general.lxc_container:
    name: test-container-new-archive
    backing_store: dir
    clone_name: test-container-new-archive-clone

- name: Archive and clone a container then destroy it
  community.general.lxc_container:
    name: test-container-new-archive
    state: absent
    clone_name: test-container-new-archive-destroyed-clone
    archive: true
    archive_compression: gzip

- name: Start a cloned container.
  community.general.lxc_container:
    name: test-container-new-archive-destroyed-clone
    state: started

- name: Destroy a container
  community.general.lxc_container:
    name: '{{ item }}'
    state: absent
  with_items:
    - test-container-stopped
    - test-container-started
    - test-container-frozen
    - test-container-lvm
    - test-container-config
    - test-container-overlayfs
    - test-container-overlayfs-clone
    - test-container-overlayfs-clone-snapshot
    - test-container-overlayfs-clone-snapshot2
    - test-container-new-archive
    - test-container-new-archive-clone
    - test-container-new-archive-destroyed-clone
```

## [Return Values](lxc_container_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **lxc_container**  complex | container information  Returned: success |
| **archive**  string | resulting state of the container  Returned: success, when archive is true  Sample: `"/tmp/test-container-config.tar"` |
| **clone**  boolean | if the container was cloned  Returned: success, when clone_name is specified  Sample: `true` |
| **init_pid**  integer | pid of the lxc init process  Returned: success  Sample: `19786` |
| **interfaces**  list / elements=string | list of the container’s network interfaces  Returned: success  Sample: `["eth0", "lo"]` |
| **ips**  list / elements=string | list of ips  Returned: success  Sample: `["10.0.3.3"]` |
| **name**  string | name of the lxc container  Returned: success  Sample: `"test_host"` |
| **state**  string | resulting state of the container  Returned: success  Sample: `"running"` |

### Authors

- Kevin Carter (@cloudnull)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
