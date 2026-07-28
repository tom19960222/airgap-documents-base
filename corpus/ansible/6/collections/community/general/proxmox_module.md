---
collection: ansible
version: "6"
title: "community.general.proxmox module – Management of instances in Proxmox VE cluster"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/proxmox_module.html
fetched_at: 2026-07-27T17:12:06+00:00
---
# community.general.proxmox module – Management of instances in Proxmox VE cluster

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
> see [Requirements](proxmox_module.md#ansible-collections-community-general-proxmox-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox`.

- [Synopsis](proxmox_module.md#synopsis)
- [Requirements](proxmox_module.md#requirements)
- [Parameters](proxmox_module.md#parameters)
- [Examples](proxmox_module.md#examples)

## [Synopsis](proxmox_module.md#id1)

- allows you to create/delete/stop instances in Proxmox VE cluster
- Starting in Ansible 2.1, it automatically detects containerization type (lxc for PVE 4, openvz for older)
- Since community.general 4.0.0 on, there are no more default values, see *proxmox_default_behavior*.

## [Requirements](proxmox_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use `PROXMOX_PASSWORD` environment variable. |
| **api_token_id**  string  added in community.general 1.3.0 | Specify the token ID. |
| **api_token_secret**  string  added in community.general 1.3.0 | Specify the token secret. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **clone**  integer  added in community.general 4.3.0 | ID of the container to be cloned.  *description*, *hostname*, and *pool* will be copied from the cloned container if not specified.  The type of clone created is defined by the *clone_type* parameter.  This operator is only supported for Proxmox clusters that use LXC containerization (PVE version >= 4). |
| **clone_type**  string  added in community.general 4.3.0 | Type of the clone created.  `full` creates a full clone, and *storage* must be specified.  `linked` creates a linked clone, and the cloned container must be a template container.  `opportunistic` creates a linked clone if the cloned container is a template container, and a full clone if not. *storage* may be specified, if not it will fall back to the default.  Choices:   - `"full"` - `"linked"` - `"opportunistic"` ← (default) |
| **cores**  integer | Specify number of cores per socket.  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `1`. |
| **cpus**  integer | numbers of allocated cpus for instance  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `1`. |
| **cpuunits**  integer | CPU weight for a VM  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `1000`. |
| **description**  string  added in community.general 0.2.0 | Specify the description for the container. Only used on the configuration web interface.  This is saved as a comment inside the configuration file. |
| **disk**  string | This option was previously described as “hard disk size in GB for instance” however several formats describing a lxc mount are permitted.  Older versions of Proxmox will accept a numeric value for size using the *storage* parameter to automatically choose which storage to allocate from, however new versions enforce the `<STORAGE>:<SIZE>` syntax.  Additional options are available by using some combination of the following key-value pairs as a comma-delimited list `[volume=]<volume> [,acl=<1|0>] [,mountoptions=<opt[;opt...]>] [,quota=<1|0>] [,replicate=<1|0>] [,ro=<1|0>] [,shared=<1|0>] [,size=<DiskSize>]`.  See <https://pve.proxmox.com/wiki/Linux_Container> for a full description.  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `3`. |
| **features**  list / elements=string  added in community.general 2.0.0 | Specifies a list of features to be enabled. For valid options, see <https://pve.proxmox.com/wiki/Linux_Container#pct_options>.  Some features require the use of a privileged container. |
| **force**  boolean | forcing operations  can be used only with states `present`, `stopped`, `restarted`  with `state=present` force option allow to overwrite existing container  with states `stopped` , `restarted` allow to force stop instance  Choices:   - `false` ← (default) - `true` |
| **hookscript**  string  added in community.general 0.2.0 | Script that will be executed during various steps in the containers lifetime. |
| **hostname**  string | the instance hostname  required only for `state=present`  must be unique if vmid is not passed |
| **ip_address**  string | specifies the address the container will be assigned |
| **memory**  integer | memory size in MB for instance  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `512`. |
| **mounts**  dictionary | specifies additional mounts (separate disks) for the container. As a hash/dictionary defining mount points |
| **nameserver**  string | sets DNS server IP address for a container |
| **netif**  dictionary | specifies network interfaces for the container. As a hash/dictionary defining interfaces. |
| **node**  string | Proxmox VE node on which to operate.  Only required for *state=present*.  For every other states it will be autodiscovered. |
| **onboot**  boolean | specifies whether a VM will be started during system bootup  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `false`.  Choices:   - `false` - `true` |
| **ostemplate**  string | the template for VM creating  required only for `state=present` |
| **password**  string | the instance root password |
| **pool**  string | Add the new VM to the specified pool. |
| **proxmox_default_behavior**  string  added in community.general 1.3.0 | As of community.general 4.0.0, various options no longer have default values. These default values caused problems when users expected different behavior from Proxmox by default or filled options which caused problems when set.  The value `compatibility` (default before community.general 4.0.0) will ensure that the default values are used when the values are not explicitly specified by the user. The new default is `no_defaults`, which makes sure these options have no defaults.  This affects the *disk*, *cores*, *cpus*, *memory*, *onboot*, *swap*, *cpuunits* options.  Choices:   - `"compatibility"` - `"no_defaults"` ← (default) |
| **pubkey**  string | Public key to add to /root/.ssh/authorized_keys. This was added on Proxmox 4.2, it is ignored for earlier versions |
| **purge**  boolean  added in community.general 2.3.0 | Remove container from all related configurations.  For example backup jobs, replication jobs, or HA.  Related ACLs and Firewall entries will always be removed.  Used with state `absent`.  Choices:   - `false` ← (default) - `true` |
| **searchdomain**  string | sets DNS search domain for a container |
| **state**  string | Indicate desired state of the instance  Choices:   - `"present"` ← (default) - `"started"` - `"absent"` - `"stopped"` - `"restarted"` |
| **storage**  string | target storage  Default: `"local"` |
| **swap**  integer | swap memory size in MB for instance  This option has no default unless *proxmox_default_behavior* is set to `compatiblity`; then the default is `0`. |
| **timeout**  integer | timeout for operations  Default: `30` |
| **unprivileged**  boolean | Indicate if the container should be unprivileged.  The default value for this parameter is `false` but that is deprecated and it will be replaced with `true` in community.general 7.0.0.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` ← (default) - `true` |
| **vmid**  integer | Specifies the instance ID.  If not set the next available ID will be fetched from ProxmoxAPI. |

## [Examples](proxmox_module.md#id4)

```yaml+jinja
- name: Create new container with minimal options
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

- name: Create new container with hookscript and description
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    hookscript: 'local:snippets/vm_hook.sh'
    description: created with ansible

- name: Create new container automatically selecting the next available vmid.
  community.general.proxmox:
    node: 'uk-mc02'
    api_user: 'root@pam'
    api_password: '1q2w3e'
    api_host: 'node1'
    password: '123456'
    hostname: 'example.org'
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

- name: Create new container with minimal options with force(it will rewrite existing container)
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    force: true

- name: Create new container with minimal options use environment PROXMOX_PASSWORD variable(you should export it before)
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'

- name: Create new container with minimal options defining network interface with dhcp
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    netif: '{"net0":"name=eth0,ip=dhcp,ip6=dhcp,bridge=vmbr0"}'

- name: Create new container with minimal options defining network interface with static ip
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: 'local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    netif: '{"net0":"name=eth0,gw=192.168.0.1,ip=192.168.0.2/24,bridge=vmbr0"}'

- name: Create new container with minimal options defining a mount with 8GB
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    mounts: '{"mp0":"local:8,mp=/mnt/test/"}'

- name: Create new container with minimal options defining a cpu core limit
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    cores: 2

- name: Create a new container with nesting enabled and allows the use of CIFS/NFS inside the container.
  community.general.proxmox:
    vmid: 100
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    password: 123456
    hostname: example.org
    ostemplate: local:vztmpl/ubuntu-14.04-x86_64.tar.gz'
    features:
     - nesting=1
     - mount=cifs,nfs

- name: >
    Create a linked clone of the template container with id 100. The newly created container with be a
    linked clone, because no storage parameter is defined
  community.general.proxmox:
    vmid: 201
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    clone: 100
    hostname: clone.example.org

- name: Create a full clone of the container with id 100
  community.general.proxmox:
    vmid: 201
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    clone: 100
    hostname: clone.example.org
    storage: local

- name: Start container
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: started

- name: >
    Start container with mount. You should enter a 90-second timeout because servers
    with additional disks take longer to boot
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: started
    timeout: 90

- name: Stop container
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: stopped

- name: Stop container with force
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    force: true
    state: stopped

- name: Restart container(stopped or mounted container you can't restart)
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: restarted

- name: Remove container
  community.general.proxmox:
    vmid: 100
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    state: absent
```

### Authors

- Sergei Antipov (@UnderGreen)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
