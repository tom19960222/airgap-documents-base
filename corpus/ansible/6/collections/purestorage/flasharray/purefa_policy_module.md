---
collection: ansible
version: "6"
title: "purestorage.flasharray.purefa_policy module – Manage FlashArray File System Policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flasharray/purefa_policy_module.html
fetched_at: 2026-07-28T00:18:24+00:00
---
# purestorage.flasharray.purefa_policy module – Manage FlashArray File System Policies

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
> see [Requirements](purefa_policy_module.md#ansible-collections-purestorage-flasharray-purefa-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_policy`.

New in purestorage.flasharray 1.5.0

- [Synopsis](purefa_policy_module.md#synopsis)
- [Requirements](purefa_policy_module.md#requirements)
- [Parameters](purefa_policy_module.md#parameters)
- [Notes](purefa_policy_module.md#notes)
- [Examples](purefa_policy_module.md#examples)

## [Synopsis](purefa_policy_module.md#id1)

- Manage FlashArray file system policies for NFS, SMB and snapshot

## [Requirements](purefa_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **anongid**  string  added in purestorage.flasharray 1.14.0 | The ID to which any users whose GID is affected by *access* of *root-squash* or *all-squash* will be mapped to.  This is ignored when *user_mapping* is enabled.  Clear using “”.  Default: `"65534"` |
| **anonuid**  string  added in purestorage.flasharray 1.14.0 | The ID to which any users whose UID is affected by *access* of *root-squash* or *all-squash* will be mapped to.  Clear using “”.  Default: `"65534"` |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **client**  string | Specifies which SMB or NFS clients are given access  Accepted notation, IP, IP mask, or hostname |
| **directory**  list / elements=string  added in purestorage.flasharray 1.9.0 | Directories to have the quota rule applied to. |
| **enabled**  boolean | Define if policy is enabled or not  Choices:   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **ignore_usage**  boolean  added in purestorage.flasharray 1.9.0 | Flag used to override checks for quota management operations.  If set to true, directory usage is not checked against the quota_limits that are set.  If set to false, the actual logical bytes in use are prevented from exceeding the limits set on the directory.  Client operations might be impacted.  If the limit exceeds the quota, the client operation is not allowed.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the policy |
| **nfs_access**  string | Specifies access control for the export  Choices:   - `"root-squash"` - `"no-root-squash"` ← (default) - `"all-squash"` |
| **nfs_permission**  string | Specifies which read-write client access permissions are allowed for the export  Choices:   - `"ro"` - `"rw"` ← (default) |
| **policy**  string / required | The type of policy to use  Choices:   - `"nfs"` - `"smb"` - `"snapshot"` - `"quota"` |
| **quota_enforced**  boolean | Defines if the directory quota is enforced.  Choices:   - `false` - `true` ← (default) |
| **quota_limit**  string  added in purestorage.flasharray 1.9.0 | Logical space limit of the share in M, G, T or P units. See examples.  If size is not set at filesystem creation time the filesystem size becomes unlimited.  This value cannot be set to 0. |
| **quota_notifications**  list / elements=string  added in purestorage.flasharray 1.9.0 | Targets to notify when usage approaches the quota limit.  The list of notification targets is a comma-separated string  If not specified, notification targets are not assigned.  Choices:   - `"user"` - `"group"` |
| **rename**  string | New name of policy |
| **smb_anon_allowed**  boolean | Specifies whether access to information is allowed for anonymous users  Choices:   - `false` ← (default) - `true` |
| **smb_encrypt**  boolean | Specifies whether the remote client is required to use SMB encryption  Choices:   - `false` ← (default) - `true` |
| **snap_at**  string | Specifies the number of hours since midnight at which to take a snapshot or the hour including AM/PM  Can only be set on the rule with the smallest *snap_every* value.  Cannot be set if the *snap_every* value is not measured in days.  Can only be set for at most one rule in the same policy. |
| **snap_client_name**  string | The customizable portion of the client visible snapshot name. |
| **snap_every**  integer | Specifies the interval between snapshots, in minutes.  The value for all rules must be multiples of one another.  Must be unique for each rule in the same policy.  Value must be between 5 and 525600. |
| **snap_keep_for**  integer | Specifies the period that snapshots are retained before they are eradicated, in minutes.  Cannot be less than the *snap_every* value of the rule.  Value must be unique for each rule in the same policy.  Value must be between 5 and 525600. |
| **snap_suffix**  string  added in purestorage.flasharray 1.10.0 | The snapshot suffix name  The suffix value can only be set for one rule in the same policy  The suffix value can only be set on a rule with the same ``keep_for`` value and ``every`` value  The suffix value can only be set on the rule with the largest ``keep_for`` value  If not specified, defaults to a monotonically increasing number generated by the system. |
| **state**  string | Define whether the policy should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **user_mapping**  boolean  added in purestorage.flasharray 1.14.0 | Defines if user mapping is enabled  Choices:   - `false` - `true` |

## [Notes](purefa_policy_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_policy_module.md#id5)

```yaml+jinja
- name: Create an NFS policy with initial rule
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    nfs_access: root-squash
    nfs_permission: ro
    client: client1
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create an empty NFS policy with no rules
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create an empty snapshot policy with no rules
  purestorage.flasharray.purefa_policy:
    name: snap1
    policy: snapshot
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create an empty snapshot policy with single directory member
  purestorage.flasharray.purefa_policy:
    name: snap1
    policy: snapshot
    directory: "foo:bar"
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable a policy
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    enabled: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add rule to existing NFS export policy
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    nfs_access: root-squash
    nfs_permission: ro
    client: client2
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add rule to existing SMB export policy
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: smb
    smb_encrypt: yes
    smb_anon_allowed: no
    client: client1
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add non-suffix rule to existing snapshot export policy
  purestorage.flasharray.purefa_policy:
    name: snap1
    policy: snapshot
    snap_client_name: foo
    snap_every: 15
    snap_keep_for: 1440
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Add suffix rule to existing snapshot export policy
  purestorage.flasharray.purefa_policy:
    name: snap1
    policy: snapshot
    snap_client_name: foo
    snap_suffix: bar
    snap_every: 1440
    snap_keep_for: 1440
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete policy rule for a client
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    client: client2
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete policy
  purestorage.flasharray.purefa_policy:
    name: export1
    policy: nfs
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory quota policy for directory bar
  purestorage.flasharray.purefa_policy:
    name: foo
    directory:
     - "foo:root"
     - "bar:bin"
    policy: quota
    quota_limit: 10G
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete directory quota policy foo
  purestorage.flasharray.purefa_policy:
    name: foo
    policy: quota
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create empty directory quota policy foo
  purestorage.flasharray.purefa_policy:
    name: foo
    policy: quota
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Detach directory "foo:bar" from quota policy quota1
  purestorage.flasharray.purefa_policy:
    name: quota1
    directory:
     - "foo:bar"
    state: absent
    policy: quota
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Remove quota rule from quota policy foo
  purestorage.flasharray.purefa_policy:
    name: foo
    policy: quota
    quota_limit: 10G
    state: absent
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
