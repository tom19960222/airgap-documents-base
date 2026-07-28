---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_host module – Manage hosts on Pure Storage FlashArrays"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_host_module.html
fetched_at: 2026-07-28T00:18:14+00:00
---
# purestorage.flasharray.purefa_host module – Manage hosts on Pure Storage FlashArrays

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/purestorage/flasharray) (version 1.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_host_module.md#ansible-collections-purestorage-flasharray-purefa-host-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_host`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_host_module.md#synopsis)
- [Requirements](purefa_host_module.md#requirements)
- [Parameters](purefa_host_module.md#parameters)
- [Notes](purefa_host_module.md#notes)
- [Examples](purefa_host_module.md#examples)

## [Synopsis](purefa_host_module.md#id1)

- Create, delete or modify hosts on Pure Storage FlashArrays.

## [Requirements](purefa_host_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_host_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **count**  integer | Number of hosts to be created in a multiple host creation  Only supported from Purity//FA v6.0.0 and higher |
| **digits**  integer | Number of digits to use for multiple host count. This will pad the index number with zeros where necessary  Only supported from Purity//FA v6.0.0 and higher  Range is between 1 and 10  Default: `1` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **host_password**  string | Sets the host password for CHAP authentication  Password length between 12 and 255 characters  To clear the username/password pair use *clear* as the password  SETTING A PASSWORD IS NON-IDEMPOTENT |
| **host_user**  string | Sets the host user name for CHAP authentication  Required with *host_password*  To clear the username/password pair use *clear* as the password |
| **iqn**  list / elements=string | List of IQNs of the host. |
| **lun**  integer | LUN ID to assign to volume for host. Must be unique.  If not provided the ID will be automatically assigned.  Range for LUN ID is 1 to 4095. |
| **name**  aliases: host  string / required | The name of the host.  Note that hostnames are case-sensitive however FlashArray hostnames are unique and ignore case - you cannot have *hosta* and *hostA*  Multi-host support available from Purity//FA 6.0.0 **\*\*\*NOTE\*\*\*** Manual deletion of individual hosts created using multi-host will cause idempotency to fail  Multi-host support only exists for host creation |
| **nqn**  list / elements=string | List of NQNs of the host. |
| **personality**  string | Define which operating system the host is. Recommended for ActiveCluster integration.  Choices:   - `"hpux"` - `"vms"` - `"aix"` - `"esxi"` - `"solaris"` - `"hitachi-vsp"` - `"oracle-vm-server"` - `"delete"` - `""` ← (default) |
| **preferred_array**  list / elements=string | List of preferred arrays in an ActiveCluster environment.  To remove existing preferred arrays from the host, specify *delete*. |
| **protocol**  string | Defines the host connection protocol for volumes.  DEPRECATED No longer a necessary parameter  Choices:   - `"fc"` - `"iscsi"` - `"nvme"` - `"mixed"` |
| **rename**  string | The name to rename to.  Note that hostnames are case-sensitive however FlashArray hostnames are unique and ignore case - you cannot have *hosta* and *hostA* |
| **start**  integer | Number at which to start the multiple host creation index  Only supported from Purity//FA v6.0.0 and higher  Default: `0` |
| **state**  string | Define whether the host should exist or not.  When removing host all connected volumes will be disconnected.  Choices:   - `"absent"` - `"present"` ← (default) |
| **suffix**  string | Suffix string, if required, for multiple host create  Host names will be formed as *<name>#<suffix>*, where *#* is a placeholder for the host index See associated descriptions  Suffix string is optional  Only supported from Purity//FA v6.0.0 and higher |
| **target_password**  string | Sets the target password for CHAP authentication  Password length between 12 and 255 characters  To clear the username/password pair use *clear* as the password  SETTING A PASSWORD IS NON-IDEMPOTENT |
| **target_user**  string | Sets the target user name for CHAP authentication  Required with *target_password*  To clear the username/password pair use *clear* as the password |
| **volume**  string | Volume name to map to the host. |
| **wwns**  list / elements=string | List of wwns of the host. |

## [Notes](purefa_host_module.md#id4)

> **Note:**
>
> - If specifying `lun` option ensure host support requested value
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_host_module.md#id5)

```yaml+jinja
- name: Create new AIX host
  purestorage.flasharray.purefa_host:
    name: foo
    personality: aix
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create 10 hosts with index starting at 10 but padded with 3 digits
  purestorage.flasharray.purefa_host:
    name: foo
    personality: vms
    suffix: bar
    count: 10
    start: 10
    digits: 3
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Rename host foo to bar
  purestorage.flasharray.purefa_host:
    name: foo
    rename: bar
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete host
  purestorage.flasharray.purefa_host:
    name: foo
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Make host bar with wwn ports
  purestorage.flasharray.purefa_host:
    name: bar
    wwns:
    - 00:00:00:00:00:00:00
    - 11:11:11:11:11:11:11
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Make host bar with iSCSI ports
  purestorage.flasharray.purefa_host:
    name: bar
    iqn:
    - iqn.1994-05.com.redhat:7d366003913
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Make host bar with NVMe ports
  purestorage.flasharray.purefa_host:
    name: bar
    nqn:
    - nqn.2014-08.com.vendor:nvme:nvm-subsystem-sn-d78432
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Make mixed protocol host
  purestorage.flasharray.purefa_host:
    name: bar
    nqn:
    - nqn.2014-08.com.vendor:nvme:nvm-subsystem-sn-d78432
    iqn:
    - iqn.1994-05.com.redhat:7d366003914
    wwns:
    - 00:00:00:00:00:00:01
    - 11:11:11:11:11:11:12
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Map host foo to volume bar as LUN ID 12
  purestorage.flasharray.purefa_host:
    name: foo
    volume: bar
    lun: 12
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disconnect volume bar from host foo
  purestorage.flasharray.purefa_host:
    name: foo
    volume: bar
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add preferred arrays to host foo
  purestorage.flasharray.purefa_host:
    name: foo
    preferred_array:
    - array1
    - array2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete preferred arrays from host foo
  purestorage.flasharray.purefa_host:
    name: foo
    preferred_array: delete
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete exisitng WWNs from host foo (does not delete host object)
  purestorage.flasharray.purefa_host:
    name: foo
    wwns: ""
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Set CHAP target and host username/password pairs
  purestorage.flasharray.purefa_host:
    name: foo
    target_user: user1
    target_password: passwrodpassword
    host_user: user2
    host_password: passwrodpassword
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete CHAP target and host username/password pairs
  purestorage.flasharray.purefa_host:
    name: foo
    target_user: user
    target_password: clear
    host_user: user
    host_password: clear
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
[Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
[Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
[Communication](index.md#communication-for-purestorage-flasharray)
