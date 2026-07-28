---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_policy module – Manage FlashBlade policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_policy_module.html
fetched_at: 2026-07-28T00:18:55+00:00
---
# purestorage.flashblade.purefb_policy module – Manage FlashBlade policies

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_policy_module.md#ansible-collections-purestorage-flashblade-purefb-policy-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_policy`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_policy_module.md#synopsis)
- [Requirements](purefb_policy_module.md#requirements)
- [Parameters](purefb_policy_module.md#parameters)
- [Notes](purefb_policy_module.md#notes)
- [Examples](purefb_policy_module.md#examples)

## [Synopsis](purefb_policy_module.md#id1)

- Manage policies for filesystem, file replica links and object store access

## [Requirements](purefb_policy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_policy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  string  added in purestorage.flashblade 1.9.0 | Specifies access control for the export policy rule  Choices:   - `"root-squash"` ← (default) - `"all-squash"` - `"no-squash"` |
| **account**  string  added in purestorage.flashblade 1.9.0 | Name of Object Store account policy applies to.  **Special Case** *pure:policy* is used for the system-wide S3 policies |
| **actions**  list / elements=string  added in purestorage.flashblade 1.9.0 | List of permissions to grant.  System-wide policy rules cannot be deleted or modified  Choices:   - `"s3:*"` - `"s3:AbortMultipartUpload"` - `"s3:CreateBucket"` - `"s3:DeleteBucket"` - `"s3:DeleteObject"` - `"s3:DeleteObjectVersion"` - `"s3:ExtendSafemodeRetentionPeriod"` - `"s3:GetBucketAcl"` - `"s3:GetBucketLocation"` - `"s3:GetBucketVersioning"` - `"s3:GetLifecycleConfiguration"` - `"s3:GetObject"` - `"s3:GetObjectAcl"` - `"s3:GetObjectVersion"` - `"s3:ListAllMyBuckets"` - `"s3:ListBucket"` - `"s3:ListBucketMultipartUploads"` - `"s3:ListBucketVersions"` - `"s3:ListMultipartUploadParts"` - `"s3:PutBucketVersioning"` - `"s3:PutLifecycleConfiguration"` - `"s3:PutObject"` |
| **anongid**  string  added in purestorage.flashblade 1.9.0 | Any user whose GID is affected by an *access* of `root_squash` or `all_squash` will have their GID mapped to anongid. The default anongid is null, which means 65534. Use “” to clear. |
| **anonuid**  string  added in purestorage.flashblade 1.9.0 | Any user whose UID is affected by an *access* of `root_squash` or `all_squash` will have their UID mapped to anonuid. The defaultis null, which means 65534. Use “” to clear. |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **at**  string | Provide a time in 12-hour AM/PM format, eg. 11AM |
| **atime**  boolean  added in purestorage.flashblade 1.9.0 | After a read operation has occurred, the inode access time is updated only if any of the following conditions is true; the previous access time is less than the inode modify time, the previous access time is less than the inode change time, or the previous access time is more than 24 hours ago.  If set to false, disables the update of inode access times after read operations.  Choices:   - `false` - `true` ← (default) |
| **before_rule**  integer  added in purestorage.flashblade 1.9.0 | The index of the client rule to insert or move a client rule before. |
| **client**  string  added in purestorage.flashblade 1.9.0 | Specifies the clients that will be permitted to access the export.  Accepted notation is a single IP address, subnet in CIDR notation, netgroup, or anonymous (\*).  Default: `"*"` |
| **effect**  string  added in purestorage.flashblade 1.9.0 | Allow S3 requests that match all of the *actions* item selected. Rules are additive.  Choices:   - `"allow"` ← (default) |
| **enabled**  boolean | State of policy  Choices:   - `false` - `true` ← (default) |
| **every**  integer | Interval between snapshots in seconds  Range available 300 - 31536000 (equates to 5m to 365d) |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **fileid_32bit**  boolean  added in purestorage.flashblade 1.9.0 | Whether the file id is 32 bits or not.  Choices:   - `false` ← (default) - `true` |
| **filesystem**  list / elements=string | List of filesystems to add to a policy on creation  To amend policy members use the *purestorage.flashblade.purefb_fs* module |
| **force_delete**  boolean  added in purestorage.flashblade 1.9.0 | Force the deletion of a Object Store Access Policy is this has attached users.  WARNING This can have undesired side-effects.  System-wide policies cannot be deleted  Choices:   - `false` ← (default) - `true` |
| **ignore_enforcement**  boolean  added in purestorage.flashblade 1.9.0 | Certain combinations of actions and other rule elements are inherently ignored if specified together in a rule.  If set to true, operations which attempt to set these combinations will fail.  If set to false, such operations will instead be allowed.  Choices:   - `false` - `true` ← (default) |
| **keep_for**  integer | How long to keep snapshots for  Range available 300 - 31536000 (equates to 5m to 365d)  Must not be set less than *every* |
| **name**  string | Name of the policy |
| **object_resources**  list / elements=string  added in purestorage.flashblade 1.9.0 | List of bucket names and object paths, with a wildcard (\*) to specify objects in a bucket; e.g., bucket1, bucket1/\*, bucket2, bucket2/\*.  System-wide policy rules cannot be deleted or modified |
| **permission**  string  added in purestorage.flashblade 1.9.0 | Specifies which read-write client access permissions are allowed for the export.  Choices:   - `"rw"` - `"ro"` ← (default) |
| **policy_type**  string  added in purestorage.flashblade 1.9.0 | Type of policy  Choices:   - `"snapshot"` ← (default) - `"access"` - `"nfs"` |
| **rename**  string  added in purestorage.flashblade 1.10.0 | New name for export policy  Only applies to NFS export policies |
| **replica_link**  list / elements=string | List of filesystem replica links to add to a policy on creation  To amend policy members use the *purestorage.flashblade.purefb_fs_replica* module |
| **rule**  string  added in purestorage.flashblade 1.9.0 | Name of the rule for the Object Store Access Policy  Rules in system-wide policies cannot be deleted or modified |
| **s3_delimiters**  list / elements=string  added in purestorage.flashblade 1.9.0 | List of delimiter characters allowed in object list requests.  Grants permissions to list ‘folder names’ (prefixes ending in a delimiter) instead of object keys.  System-wide policy rules cannot be deleted or modified |
| **s3_prefixes**  list / elements=string  added in purestorage.flashblade 1.9.0 | List of ‘folders’ (object key prefixes) for which object listings may be requested.  System-wide policy rules cannot be deleted or modified |
| **secure**  boolean  added in purestorage.flashblade 1.9.0 | If true, this prevents NFS access to client connections coming from non-reserved ports.  If false, allows NFS access to client connections coming from non-reserved ports.  Applies to NFSv3, NFSv4.1, and auxiliary protocols MOUNT and NLM.  Choices:   - `false` ← (default) - `true` |
| **security**  list / elements=string  added in purestorage.flashblade 1.9.0 | The security flavors to use for accessing files on this mount point.  If the server does not support the requested flavor, the mount operation fails.  *sys* trusts the client to specify users identity.  *krb* provides cryptographic proof of a users identity in each RPC request.  *krb5i* adds integrity checking to krb5, to ensure the data has not been tampered with.  *krb5p* adds integrity checking and encryption to krb5.  Choices:   - `"sys"` ← (default) - `"krb5"` - `"krb5i"` - `"krb5p"`   Default: `["sys"]` |
| **source_ips**  list / elements=string  added in purestorage.flashblade 1.9.0 | List of IPs and subnets from which this rule should allow requests; e.g., 10.20.30.40, 10.20.30.0/24, 2001:DB8:1234:5678::/64.  System-wide policy rules cannot be deleted or modified |
| **state**  string | Create or delete policy.  Copy is applicable only to Object Store Access Policies Rules  Choices:   - `"absent"` - `"present"` ← (default) - `"copy"` |
| **target**  string  added in purestorage.flashblade 1.9.0 | Name of policy to copy rule to |
| **target_rule**  string  added in purestorage.flashblade 1.9.0 | Name of the rule to copy the exisitng rule to.  If not defined the existing rule name is used. |
| **timezone**  string | Time Zone used for the *at* parameter  If not provided, the module will attempt to get the current local timezone from the server |
| **user**  string  added in purestorage.flashblade 1.9.0 | User in the *account* that the policy is granted to. |

## [Notes](purefb_policy_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_policy_module.md#id5)

```yaml+jinja
- name: Create a simple snapshot policy with no rules
  purestorage.flashblade.purefb_policy:
    name: test_policy
    policy_type: snapshot
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create a snapshot policy and connect to existing filesystems and filesystem replica links
  purestorage.flashblade.purefb_policy:
    name: test_policy_with_members
    policy_type: snapshot
    filesystem:
    - fs1
    - fs2
    replica_link:
    - rl1
    - rl2
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create a snapshot policy with rules
  purestorage.flashblade.purefb_policy:
    name: test_policy2
    policy_type: snapshot
    at: 11AM
    keep_for: 86400
    every: 86400
    timezone: Asia/Shanghai
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete a snapshot policy
  purestorage.flashblade.purefb_policy:
    name: test_policy
    policy_type: snapshot
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create an empty object store access policy
  purestorage.flashblade.purefb_policy:
    name: test_os_policy
    account: test
    policy_type: access
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create an empty object store access policy and assign user
  purestorage.flashblade.purefb_policy:
    name: test_os_policy
    account: test
    policy_type: access
    user: fred
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create a object store access policy with simple rule
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    policy_type: access
    account: test
    rule: rule1
    actions: "s3:*"
    object_resources: "*"
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create an empty NFS export policy
  purestorage.flashblade.purefb_policy:
    name: test_nfs_export
    policy_type: nfs
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create an NFS export policy with a client rule
  purestorage.flashblade.purefb_policy:
    name: test_nfs_export
    policy_type: nfs
    atime: true
    client: "10.0.1.0/24"
    secure: true
    security: [sys, krb5]
    permission: rw
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create a new rule for an existing NFS export policy
  purestorage.flashblade.purefb_policy:
    name: test_nfs_export
    policy_type: nfs
    atime: true
    client: "10.0.2.0/24"
    security: sys
    permission: ro
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete a client rule from an NFS export policy
  purestorage.flashblade.purefb_policy:
    name: test_nfs_export
    client: "10.0.1.0/24"
    policy_type: nfs
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete an NFS export policy and all associated rules
  purestorage.flashblade.purefb_policy:
    name: test_nfs_export
    state: absent
    policy_type: nfs
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete a rule from an object store access policy
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    account: test
    policy_type: access
    rule: rule1
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete a user from an object store access policy
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    account: test
    user: fred
    policy_type: access
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete an object store access policy with attached users (USE WITH CAUTION)
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    account: test
    policy_type: access
    force_delete: true
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete an object store access policy with no attached users
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    account: test
    policy_type: access
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Copy an object store access policy rule to another exisitng policy
  purestorage.flashblade.purefb_policy:
    name: test_os_policy_rule
    policy_type: access
    account: test
    target: "account2/anotherpolicy"
    target_rule: new_rule1
    state: copy
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name:  Rename an NFS Export Policy
  purestorage.flashblade.purefb_policy:
    name: old_name
    policy_type: nfs
    rename: new_name
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
