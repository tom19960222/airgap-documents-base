---
collection: ceph
version: "19.2.2"
title: "Ceph Object Gateway IAM API"
source_url: https://docs.ceph.com/en/squid/radosgw/iam/
fetched_at: 2026-07-27T16:40:33+00:00
---
# Ceph Object Gateway IAM API

New in version Squid.

The Ceph Object Gateway supports a subset of the [Amazon IAM API](https://docs.aws.amazon.com/IAM/latest/APIReference/welcome.html) for
the RESTful management of account users, roles, and associated policies.

This REST API is served by the same HTTP endpoint as the
[Ceph Object Gateway S3 API](../s3/index.md).

## Authorization

By default, only [Account Root Users](../account/index.md#radosgw-account-root-user) are
authorized to use the IAM API, and can only see the resources under their own
account. The account root user can use policies to delegate these permissions
to other users or roles in the account.

## Feature Support

The following tables describe the currently supported IAM actions.

### Users

| Action | Remarks |
| --- | --- |
| **CreateUser** |  |
| **GetUser** |  |
| **UpdateUser** |  |
| **DeleteUser** |  |
| **ListUsers** |  |
| **CreateAccessKey** |  |
| **UpdateAccessKey** |  |
| **DeleteAccessKey** |  |
| **ListAccessKeys** |  |
| **PutUserPolicy** |  |
| **GetUserPolicy** |  |
| **DeleteUserPolicy** |  |
| **ListUserPolicies** |  |
| **AttachUserPolicies** |  |
| **DetachUserPolicy** |  |
| **ListAttachedUserPolicies** |  |

### Groups

| Action | Remarks |
| --- | --- |
| **CreateGroup** |  |
| **GetGroup** |  |
| **UpdateGroup** |  |
| **DeleteGroup** |  |
| **ListGroups** |  |
| **AddUserToGroup** |  |
| **RemoveUserFromGroup** |  |
| **ListGroupsForUser** |  |
| **PutGroupPolicy** |  |
| **GetGroupPolicy** |  |
| **DeleteGroupPolicy** |  |
| **ListGroupPolicies** |  |
| **AttachGroupPolicies** |  |
| **DetachGroupPolicy** |  |
| **ListAttachedGroupPolicies** |  |

### Roles

| Action | Remarks |
| --- | --- |
| **CreateRole** |  |
| **GetRole** |  |
| **UpdateRole** |  |
| **UpdateAssumeRolePolicy** |  |
| **DeleteRole** |  |
| **ListRoles** |  |
| **TagRole** |  |
| **UntagRole** |  |
| **ListRoleTags** |  |
| **PutRolePolicy** |  |
| **GetRolePolicy** |  |
| **DeleteRolePolicy** |  |
| **ListRolePolicies** |  |
| **AttachRolePolicies** |  |
| **DetachRolePolicy** |  |
| **ListAttachedRolePolicies** |  |

### OpenIDConnectProvider

| Action | Remarks |
| --- | --- |
| **CreateOpenIDConnectProvider** |  |
| **GetOpenIDConnectProvider** |  |
| **DeleteOpenIDConnectProvider** |  |
| **ListOpenIDConnectProviders** |  |

### Managed Policies

The following managed policies are available for use with `AttachGroupPolicy`,
`AttachRolePolicy` and `AttachUserPolicy`:

IAMFullAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/IAMFullAccess`

    Version:
    :   v2 (default)

IAMReadOnlyAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/IAMReadOnlyAccess`

    Version:
    :   v4 (default)

AmazonSNSFullAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/AmazonSNSFullAccess`

    Version:
    :   v1 (default)

AmazonSNSReadOnlyAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/AmazonSNSReadOnlyAccess`

    Version:
    :   v1 (default)

AmazonS3FullAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/AmazonS3FullAccess`

    Version:
    :   v2 (default)

AmazonS3ReadOnlyAccess
:   Arn:
    :   `arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess`

    Version:
    :   v3 (default)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
