---
collection: ceph
version: "20.2.4"
title: "Rados Gateway S3 API Compliance"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/dev/radosgw/s3_compliance.rst
fetched_at: 2026-08-18T01:32:45Z
---
# Rados Gateway S3 API Compliance

> **Warning:**
> This document is a draft, it might not be accurate

## Naming code reference

Here comes a BNF definition on how to name a feature in the code for referencing purpose : :

```
name ::= request_type "_" ( header | operation ) ( "_" header_option )?

request_type ::= "req" | "res"

header ::= string

operation ::= method resource

method ::= "GET" | "PUT" | "POST" | "DELETE" | "OPTIONS" | "HEAD"

resource ::= string

header_option ::= string
```

## Common Request Headers

S3 Documentation reference : http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html

| Header | Supported? | Code Links | Tests links |
| --- | --- | --- | --- |
| Authorization <br> | Yes <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1962 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L2051 | <br> |
| Content-Length | Yes |  |  |
| Content-Type | Yes |  |  |
| Content-MD5 <br> | Yes <br> | https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1249 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1306 | <br> |
| Date | Yes | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_auth_s3.cc#L164 |  |
| Expect <br> <br> | Yes <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest.cc#L1227 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L802 <br> https://github.com/ceph/ceph/blob/76040d90f7eb9f9921a3b8dcd0f821ac2cd9c492/src/rgw/rgw_main.cc#L372 | <br> <br> |
| Host | ? |  |  |
| x-amz-date <br> <br> | Yes <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_auth_s3.cc#L169 <br> should take precedence over DATE as mentioned here -> <br> http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html | <br> <br> |
| x-amz-security-token | No |  |  |

## Common Response Headers

S3 Documentation reference : http://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonResponseHeaders.html

| Header | Supported? | Code Links | Tests links |
| --- | --- | --- | --- |
| Content-Length | Yes |  |  |
| Connection | ? |  |  |
| Date | ? |  |  |
| ETag <br> <br> <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1312 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1436 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L2222 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L118 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L268 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L516 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1336 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1486 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1548 | <br> <br> <br> <br> <br> <br> <br> <br> |
| Server | No |  |  |
| x-amz-delete-marker | No |  |  |
| x-amz-id-2 | No |  |  |
| x-amz-request-id | Yes | https://github.com/ceph/ceph/commit/b711e3124f8f73c17ebd19b38807a1b77f201e44 |  |
| x-amz-version-id | No |  |  |

## Operations on the Service

S3 Documentation reference : http://docs.aws.amazon.com/AmazonS3/latest/API/RESTServiceOps.html

| Type | Operation | Supported? | Code links | Tests links |
| --- | --- | --- | --- | --- |
| GET <br> <br> | Service <br> <br> | Yes <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L2094 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1676 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L185 | <br> <br> |

## Operations on Buckets

S3 Documentation reference : http://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketOps.html

| Type | Operation | Supported? | Code links | Tests links |
| --- | --- | --- | --- | --- |
| DELETE <br> <br> <br> <br> <br> <br> | Bucket <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1728 <br> https://github.com/ceph/ceph/blob/e91042171939b6bf82a56a1015c5cae792d228ad/src/rgw/rgw_rest_bucket.cc#L250 <br> https://github.com/ceph/ceph/blob/e91042171939b6bf82a56a1015c5cae792d228ad/src/rgw/rgw_rest_bucket.cc#L212 <br> https://github.com/ceph/ceph/blob/25948319c4d256c4aeb0137eb88947e54d14cc79/src/rgw/rgw_bucket.cc#L856 <br> https://github.com/ceph/ceph/blob/25948319c4d256c4aeb0137eb88947e54d14cc79/src/rgw/rgw_bucket.cc#L513 <br> https://github.com/ceph/ceph/blob/25948319c4d256c4aeb0137eb88947e54d14cc79/src/rgw/rgw_bucket.cc#L286 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L461 | <br> <br> <br> <br> <br> <br> |
| DELETE <br> | Bucket cors <br> | ? <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1731 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1916 | <br> |
| DELETE | Bucket lifecycle | No |  |  |
| DELETE | Bucket policy | ? |  |  |
| DELETE | Bucket tagging | ? |  |  |
| DELETE | Bucket website | No |  |  |
| GET <br> | Bucket <br> | Yes <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1676 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L185 | <br> |
| GET <br> <br> | Bucket acl <br> <br> | Yes <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1697 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1728 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1344 | <br> <br> |
| GET <br> <br> | Bucket cors <br> <br> | ? <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1698 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1845 <br> https://github.com/ceph/ceph/blob/76040d90f7eb9f9921a3b8dcd0f821ac2cd9c492/src/rgw/rgw_main.cc#L345 | <br> <br> |
| GET | Bucket lifecycle | No |  |  |
| GET | Bucket location | No |  |  |
| GET <br> | Bucket policy <br> | ? <br> | https://github.com/ceph/ceph/blob/e91042171939b6bf82a56a1015c5cae792d228ad/src/rgw/rgw_rest_bucket.cc#L232 <br> https://github.com/ceph/ceph/blob/e91042171939b6bf82a56a1015c5cae792d228ad/src/rgw/rgw_rest_bucket.cc#L58 | <br> |
| GET <br> | Bucket logging <br> | ? <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1695 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L287 | <br> |
| GET | Bucket notification | No |  |  |
| GET | Bucket tagging | No |  |  |
| GET | Bucket Object versions | No |  |  |
| GET | Bucket requestPayment | No |  |  |
| GET | Bucket versioning | No |  |  |
| GET | Bucket website | No |  |  |
| GET <br> <br> <br> | List Multipart uploads <br> <br> <br> | Yes <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1701 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest.cc#L877 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L2355 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L2363 | <br> <br> <br> |
| HEAD <br> <br> <br> | Bucket <br> <br> <br> | Yes <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1713 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1689 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L826 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L834 | <br> <br> <br> |
| PUT <br> <br> <br> <br> | Bucket <br> <br> <br> <br> | Yes <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1725 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L382 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L437 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L901 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L945 | <br> <br> <br> <br> |
| PUT <br> <br> <br> <br> | Bucket acl <br> <br> <br> <br> | Yes <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1721 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1354 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1373 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1739 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1753 | <br> <br> <br> <br> |
| PUT <br> <br> <br> | Bucket cors <br> <br> <br> | ? <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1723 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1398 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1858 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1866 | <br> <br> <br> |
| PUT | Bucket lifecycle | No |  |  |
| PUT | Bucket policy | ? |  |  |
| PUT | Bucket logging | ? |  |  |
| PUT | Bucket notification | No |  |  |
| PUT | Bucket tagging | ? |  |  |
| PUT | Bucket requestPayment | No |  |  |
| PUT | Bucket versioning | No |  |  |
| PUT | Bucket website | No |  |  |

## Operations on Objects

S3 Documentation reference : http://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectOps.html

| Type | Operation | Supported? | Code links | Tests links |
| --- | --- | --- | --- | --- |
| DELETE <br> <br> | Object <br> <br> | Yes <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1796 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1516 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1524 | <br> <br> |
| DELETE <br> <br> <br> <br> <br> <br> | Multiple objects <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1739 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1616 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1626 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1641 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1667 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1516 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1524 | <br> <br> <br> <br> <br> <br> |
| GET <br> <br> <br> <br> <br> <br> <br> <br> | Object <br> <br> <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1767 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L71 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L397 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L424 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L497 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L562 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L626 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L641 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L706 | <br> <br> <br> <br> <br> <br> <br> <br> |
| GET | Object acl | Yes |  |  |
| GET | Object torrent | No |  |  |
| HEAD <br> <br> <br> <br> <br> <br> <br> <br> | Object <br> <br> <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1777 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L71 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L397 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L424 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L497 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L562 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L626 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L641 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L706 | <br> <br> <br> <br> <br> <br> <br> <br> |
| OPTIONS <br> <br> <br> <br> | Object <br> <br> <br> <br> | Yes <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1814 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1418 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1951 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1968 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1993 | <br> <br> <br> <br> |
| POST <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | Object <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1742 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L631 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L694 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L700 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L707 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L759 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L771 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L781 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L795 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L929 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1037 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1059 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1134 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1344 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1360 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1365 | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> |
| POST | Object restore | ? |  |  |
| PUT <br> <br> <br> <br> <br> <br> | Object <br> <br> <br> <br> <br> <br> | Yes <br> <br> <br> <br> <br> <br> | https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L481 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L493 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L507 <br> https://github.com/ceph/ceph/blob/8a2eb18494005aa968b71f18121da8ebab48e950/src/rgw/rgw_rest_s3.cc#L1786 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1119 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1217 <br> https://github.com/ceph/ceph/blob/b139a7cd34b4e203ab164ada7a8fa590b50d8b13/src/rgw/rgw_op.cc#L1222 | <br> <br> <br> <br> <br> <br> |
| PUT | Object acl | Yes |  |  |
| PUT | Object copy | Yes |  |  |
| PUT | Initiate multipart upload | Yes |  |  |
| PUT | Upload Part | Yes |  |  |
| PUT | Upload Part copy | ? |  |  |
| PUT | Complete multipart upload | Yes |  |  |
| PUT | Abort multipart upload | Yes |  |  |
| PUT | List parts | Yes |  |  |
