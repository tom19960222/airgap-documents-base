---
collection: ceph
version: "20.2.4"
title: "Bucket Policies"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/radosgw/bucketpolicy.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Bucket Policies

*Bucket policies were added in the Luminous release of Ceph.*

The Ceph Object Gateway supports a subset of the Amazon S3 policy
language applied to buckets.

## Creation and Removal

Bucket policies are managed through standard S3 operations rather than
radosgw-admin.

For example, one may use s3cmd to set or delete a policy thus:

```
$ cat > examplepol
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": {"AWS": ["arn:aws:iam::usfolks:user/fred:subuser"]},
    "Action": "s3:PutObjectAcl",
    "Resource": [
      "arn:aws:s3:::happybucket/*"
    ]
  }]
}

$ s3cmd setpolicy examplepol s3://happybucket
$ s3cmd delpolicy s3://happybucket
```

## Limitations

Currently, we support only the following actions:

- s3:AbortMultipartUpload
- s3:CreateBucket
- s3:DeleteBucketPolicy
- s3:DeleteBucket
- s3:DeleteBucketWebsite
- s3:DeleteObject
- s3:DeleteObjectVersion
- s3:DeleteReplicationConfiguration
- s3:GetAccelerateConfiguration
- s3:GetBucketAcl
- s3:GetBucketCORS
- s3:GetBucketLocation
- s3:GetBucketLogging
- s3:GetBucketNotification
- s3:GetBucketPolicy
- s3:GetBucketRequestPayment
- s3:GetBucketTagging
- s3:GetBucketVersioning
- s3:GetBucketWebsite
- s3:GetLifecycleConfiguration
- s3:GetObjectAcl
- s3:GetObject
- s3:GetObjectTorrent
- s3:GetObjectVersionAcl
- s3:GetObjectVersion
- s3:GetObjectVersionTorrent
- s3:GetReplicationConfiguration
- s3:IPAddress
- s3:NotIpAddress
- s3:ListAllMyBuckets
- s3:ListBucketMultipartUploads
- s3:ListBucket
- s3:ListBucketVersions
- s3:ListMultipartUploadParts
- s3:PutAccelerateConfiguration
- s3:PutBucketAcl
- s3:PutBucketCORS
- s3:PutBucketLogging
- s3:PutBucketNotification
- s3:PutBucketPolicy
- s3:PutBucketRequestPayment
- s3:PutBucketTagging
- s3:PutBucketVersioning
- s3:PutBucketWebsite
- s3:PutLifecycleConfiguration
- s3:PutObjectAcl
- s3:PutObject
- s3:PutObjectVersionAcl
- s3:PutReplicationConfiguration
- s3:RestoreObject

We do not yet support setting policies on users, groups, or roles.

We use the RGW ‘tenant’ identifier in place of the Amazon twelve-digit
account ID. In the future we may allow you to assign an account ID to
a tenant, but for now if you want to use policies between AWS S3 and
RGW S3 you will have to use the Amazon account ID as the tenant ID when
creating users.

Under AWS, all tenants share a single namespace. RGW gives every
tenant its own namespace of buckets. There may be an option to enable
an AWS-like 'flat' bucket namespace in future versions. At present, to
access a bucket belonging to another tenant, address it as
"tenant:bucket" in the S3 request.

In AWS, a bucket policy can grant access to another account, and that
account owner can then grant access to individual users with user
permissions. Since we do not yet support user, role, and group
permissions, account owners will currently need to grant access
directly to individual users, and granting an entire account access to
a bucket grants access to all users in that account.

Bucket policies do not yet support string interpolation.

For all requests, condition keys we support are:
- aws:CurrentTime
- aws:EpochTime
- aws:PrincipalType
- aws:Referer
- aws:SecureTransport
- aws:SourceIp
- aws:UserAgent
- aws:username

We support certain s3 condition keys for bucket and object requests.

*Support for the following bucket-related operations was added in the Mimic
release of Ceph.*

### Bucket Related Operations

| Permission | Condition Keys | Comments |
| --- | --- | --- |
| <br> <br>s3:createBucket <br> <br> <br> | s3:x-amz-acl <br> s3:x-amz-grant-<perm><br> where perm is one of <br> read/write/read-acp <br> write-acp/ <br> full-control | <br> <br> <br> <br> <br> |
|  | s3:prefix |  |
| s3:ListBucket & | s3:delimiter |  |
| s3:ListBucketVersions | s3:max-keys |  |
| s3:PutBucketAcl <br> | s3:x-amz-acl <br> s3:x-amz-grant-<perm> | <br> |

<a id="tag_policy"></a>

### Object Related Operations

| Permission <br> | Condition Keys <br> | Comments <br> |
| --- | --- | --- |
| <br> | s3:x-amz-acl & s3:x-amz-grant-<perm> <br> | <br> |
| <br> | s3:x-amz-copy-source <br> | <br> |
| <br> | s3:x-amz-server-side-encryption <br> | <br> |
| s3:PutObject <br> | s3:x-amz-server-side-encryption-aws-kms-key-id <br> | <br> |
| <br> | s3:x-amz-server-side-encryption-customer-algorithm <br> | <br> |
| <br> <br> <br> | s3:x-amz-metadata-directive <br> <br> <br> | PUT & COPY to <br>overwrite/preserve <br>metadata in COPY <br>requests |
| <br> | s3:RequestObjectTag/<tag-key> <br> | <br> |
| s3:PutObjectAcl <br>s3:PutObjectVersionAcl | s3:x-amz-acl & s3-amz-grant-<perm> <br> | <br> |
| <br> | s3:ExistingObjectTag/<tag-key> <br> | <br> |
| <br>s3:PutObjectTagging & <br>s3:PutObjectVersionTagging <br> | s3:RequestObjectTag/<tag-key> <br><br>s3:ExistingObjectTag/<tag-key> <br> | <br><br> <br> |
| s3:GetObject & <br>s3:GetObjectVersion | s3:ExistingObjectTag/<tag-key> <br> | <br> |
| s3:GetObjectAcl & <br>s3:GetObjectVersionAcl | s3:ExistingObjectTag/<tag-key> <br> | <br> |
| s3:GetObjectTagging & <br>s3:GetObjectVersionTagging | s3:ExistingObjectTag/<tag-key> <br> | <br> |
| s3:DeleteObjectTagging & <br>s3:DeleteObjectVersionTagging | s3:ExistingObjectTag/<tag-key> <br> | <br> |

More may be supported soon as we integrate with the recently rewritten
Authentication/Authorization subsystem.

## Swift

There is no way to set bucket policies under Swift, but bucket
policies that have been set govern Swift as well as S3 operations.

Swift credentials are matched against Principals specified in a policy
in a way specific to whatever backend is being used.
