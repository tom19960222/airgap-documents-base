---
collection: ceph
version: "19.2.2"
title: "Ceph RESTful API"
source_url: https://docs.ceph.com/en/squid/mgr/ceph_api/
fetched_at: 2026-07-27T16:40:49+00:00
---
# Ceph RESTful API

## Introduction

The **Ceph RESTful API** (henceforth **Ceph API**) is provided by the
[Ceph Dashboard](../dashboard/index.md#mgr-dashboard) module. The Ceph API
service is available at the same URL as the regular Ceph Dashboard, under the
`/api` base path (please refer to [Host Name and Port](../dashboard/index.md#dashboard-host-name-and-port)):

```
http://<server_addr>:<server_port>/api
```

or, if HTTPS is enabled (please refer to [SSL/TLS Support](../dashboard/index.md#dashboard-ssl-tls-support)):

```
https://<server_addr>:<ssl_server_port>/api
```

The Ceph API leverages the following standards:

- [HTTP 1.1](https://tools.ietf.org/html/rfc7231) for API syntax and semantics,
- [JSON](https://tools.ietf.org/html/rfc8259) for content encoding,
- [HTTP Content Negotiation](https://tools.ietf.org/html/rfc2295) and [MIME](https://tools.ietf.org/html/rfc2045) for versioning,
- [OAuth 2.0](https://tools.ietf.org/html/rfc6750) and [JWT](https://tools.ietf.org/html/rfc7519) for authentication and authorization.

> **Warning:**
>
> Some endpoints are still under active development, and should be carefully
> used since new Ceph releases could bring backward incompatible changes.

## Authentication and Authorization

Requests to the Ceph API pass through two access control checkpoints:

- **Authentication**: ensures that the request is performed on behalf of an existing and valid user account.
- **Authorization**: ensures that the previously authenticated user can in fact perform a specific action (create, read, update or delete) on the target endpoint.

So, prior to start consuming the Ceph API, a valid JSON Web Token (JWT) has to
be obtained, and it may then be reused for subsequent requests. The
`/api/auth` endpoint will provide the valid token:

```
curl -X POST "https://example.com:8443/api/auth" \
-H  "Accept: application/vnd.ceph.api.v1.0+json" \
-H  "Content-Type: application/json" \
-d '{"username": <username>, "password": <password>}'
```

```
{ "token": "<redacted_token>", ...}
```

The token obtained must be passed together with every API request in the
`Authorization` HTTP header:

```
curl -H "Authorization: Bearer <token>" ...
```

Authentication and authorization can be further configured from the
Ceph CLI, the Ceph-Dashboard UI and the Ceph API itself (please refer to
[User and Role Management](../dashboard/index.md#dashboard-user-role-management)).

## Versioning

One of the main goals of the Ceph API is to keep a stable interface. For this
purpose, Ceph API is built upon the following principles:

- **Mandatory**: in order to avoid implicit defaults, all endpoints require an explicit default version (starting with `1.0`).
- **Per-endpoint**: as this API wraps many different Ceph components, this allows for a finer-grained change control.
  :   - **Content/MIME Type**: the version expected from a specific endpoint is stated by the `Accept: application/vnd.ceph.api.v<major>.<minor>+json` HTTP header. If the current Ceph API server is not able to address that specific major version, a [415 - Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13) response will be returned.
- **Semantic Versioning**: with a `major.minor` version:
  :   - Major changes are backward incompatible: they might result in non-additive changes to the request and/or response formats of a specific endpoint.
      - Minor changes are backward/forward compatible: they basically consists of additive changes to the request or response formats of a specific endpoint.

An example:

```
curl -X GET "https://example.com:8443/api/osd" \
-H  "Accept: application/vnd.ceph.api.v1.0+json" \
-H  "Authorization: Bearer <token>"
```

## Specification

### Auth

POST /api/auth
:   **Example request:**

    ```http
    POST /api/auth HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "password": "string",
        "username": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/auth/check
:   **Check token Authentication**

    Query Parameters:
    :   - **token** (*string*) -- Authentication Token
          (Required)

    **Example request:**

    ```http
    POST /api/auth/check?token=string HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "token": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/auth/logout
:   Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CephFSSnapshotSchedule

POST /api/cephfs/snapshot/schedule
:   **Example request:**

    ```http
    POST /api/cephfs/snapshot/schedule HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "fs": "string",
        "group": "string",
        "path": "string",
        "retention_policy": "string",
        "snap_schedule": "string",
        "start": "string",
        "subvol": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/snapshot/schedule/{fs}
:   Parameters:
    :   - **fs** (*string*) --

    Query Parameters:
    :   - **path** (*string*) --
        - **recursive** (*boolean*) --

    **Example request:**

    ```http
    GET /api/cephfs/snapshot/schedule/{fs} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/snapshot/schedule/{fs}/{path}
:   Parameters:
    :   - **fs** (*string*) --
        - **path** (*string*) --

    **Example request:**

    ```http
    PUT /api/cephfs/snapshot/schedule/{fs}/{path} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group": "string",
        "retention_to_add": "string",
        "retention_to_remove": "string",
        "subvol": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs/snapshot/schedule/{fs}/{path}/activate
:   Parameters:
    :   - **fs** (*string*) --
        - **path** (*string*) --

    **Example request:**

    ```http
    POST /api/cephfs/snapshot/schedule/{fs}/{path}/activate HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group": "string",
        "schedule": "string",
        "start": "string",
        "subvol": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs/snapshot/schedule/{fs}/{path}/deactivate
:   Parameters:
    :   - **fs** (*string*) --
        - **path** (*string*) --

    **Example request:**

    ```http
    POST /api/cephfs/snapshot/schedule/{fs}/{path}/deactivate HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group": "string",
        "schedule": "string",
        "start": "string",
        "subvol": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/snapshot/schedule/{fs}/{path}/delete_snapshot
:   Parameters:
    :   - **fs** (*string*) --
        - **path** (*string*) --

    Query Parameters:
    :   - **schedule** (*string*) -- (Required)
        - **start** (*string*) -- (Required)
        - **retention_policy** (*string*) --
        - **subvol** (*string*) --
        - **group** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CephFSSubvolume

POST /api/cephfs/subvolume
:   **Example request:**

    ```http
    POST /api/cephfs/subvolume HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "subvol_name": "string",
        "vol_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/subvolume/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **subvol_name** (*string*) -- (Required)
        - **group_name** (*string*) --
        - **retain_snapshots** (*boolean*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **group_name** (*string*) --
        - **info** (*boolean*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/{vol_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/subvolume/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/cephfs/subvolume/{vol_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group_name": "string",
        "size": 1,
        "subvol_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/{vol_name}/exists
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **group_name** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/{vol_name}/exists HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/{vol_name}/info
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **subvol_name** (*string*) -- (Required)
        - **group_name** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/{vol_name}/info?subvol_name=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Cephfs

GET /api/cephfs
:   **Example request:**

    ```http
    GET /api/cephfs HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs
:   **Example request:**

    ```http
    POST /api/cephfs HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "name": "string",
        "service_spec": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/auth
:   **Set Ceph authentication capabilities for the specified user ID in the given path**

    **Example request:**

    ```http
    PUT /api/cephfs/auth HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "caps": "string",
        "client_id": "string",
        "fs_name": "string",
        "root_squash": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/remove/{name}
:   **Remove CephFS Volume**

    Parameters:
    :   - **name** (*string*) -- File System Name

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/rename
:   **Rename CephFS Volume**

    **Example request:**

    ```http
    PUT /api/cephfs/rename HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "name": "string",
        "new_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}
:   Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/{fs_id}/client/{client_id}
:   Parameters:
    :   - **fs_id** (*string*) --
        - **client_id** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/clients
:   Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/clients HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/get_root_directory
:   > The root directory that can’t be fetched using ls_dir (api).
    > :param fs_id: The filesystem identifier.
    > :return: The root directory
    > :rtype: dict

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/get_root_directory HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/ls_dir
:   > List directories of specified path.
    > :param fs_id: The filesystem identifier.
    > :param path: The path where to start listing the directory content.
    > Defaults to ‘/’ if not set.
    > :type path: str | bytes
    > :param depth: The number of steps to go down the directory tree.
    > :type depth: int | str
    > :return: The names of the directories below the specified path.
    > :rtype: list

    Parameters:
    :   - **fs_id** (*string*) --

    Query Parameters:
    :   - **path** (*string*) --
        - **depth** (*integer*) --

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/ls_dir HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/mds_counters
:   Parameters:
    :   - **fs_id** (*string*) --

    Query Parameters:
    :   - **counters** (*integer*) --

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/mds_counters HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/quota
:   **Get Cephfs Quotas of the specified path**

    > Get the quotas of the specified path.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory/file.
    > :return: Returns a dictionary containing ‘max_bytes’
    > and ‘max_files’.
    > :rtype: dict

    Parameters:
    :   - **fs_id** (*string*) -- File System Identifier

    Query Parameters:
    :   - **path** (*string*) -- File System Path
          (Required)

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/quota?path=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/{fs_id}/quota
:   > Set the quotas of the specified path.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory/file.
    > :param max_bytes: The byte limit.
    > :param max_files: The file limit.

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    PUT /api/cephfs/{fs_id}/quota HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "max_bytes": "string",
        "max_files": "string",
        "path": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/{fs_id}/rename-path
:   > Rename a file or directory.
    > :param fs_id: The filesystem identifier.
    > :param src_path: The path to the existing file or directory.
    > :param dst_path: The new name of the file or directory.

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    PUT /api/cephfs/{fs_id}/rename-path HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "dst_path": "string",
        "src_path": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/{fs_id}/snapshot
:   > Remove a snapshot.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory.
    > :param name: The name of the snapshot.

    Parameters:
    :   - **fs_id** (*string*) --

    Query Parameters:
    :   - **path** (*string*) -- (Required)
        - **name** (*string*) -- (Required)

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs/{fs_id}/snapshot
:   > Create a snapshot.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory.
    > :param name: The name of the snapshot. If not specified, a name using the
    > current time in RFC3339 UTC format will be generated.
    > :return: The name of the snapshot.
    > :rtype: str

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    POST /api/cephfs/{fs_id}/snapshot HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "name": "string",
        "path": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/{fs_id}/statfs
:   **Get Cephfs statfs of the specified path**

    > Get the statfs of the specified path.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory/file.
    > :return: Returns a dictionary containing ‘bytes’,
    > ‘files’ and ‘subdirs’.
    > :rtype: dict

    Parameters:
    :   - **fs_id** (*string*) -- File System Identifier

    Query Parameters:
    :   - **path** (*string*) -- File System Path
          (Required)

    **Example request:**

    ```http
    GET /api/cephfs/{fs_id}/statfs?path=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/{fs_id}/tree
:   > Remove a directory.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory.

    Parameters:
    :   - **fs_id** (*string*) --

    Query Parameters:
    :   - **path** (*string*) -- (Required)

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs/{fs_id}/tree
:   > Create a directory.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the directory.

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    POST /api/cephfs/{fs_id}/tree HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "path": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/{fs_id}/unlink
:   > Removes a file, link, or symbolic link.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the file or link to unlink.

    Parameters:
    :   - **fs_id** (*string*) --

    Query Parameters:
    :   - **path** (*string*) -- (Required)

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cephfs/{fs_id}/write_to_file
:   > Write some data to the specified path.
    > :param fs_id: The filesystem identifier.
    > :param path: The path of the file to write.
    > :param buf: The str to write to the buf.

    Parameters:
    :   - **fs_id** (*string*) --

    **Example request:**

    ```http
    POST /api/cephfs/{fs_id}/write_to_file HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "buf": "string",
        "path": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CephfsSnapshotClone

POST /api/cephfs/subvolume/snapshot/clone
:   **Create a clone of a subvolume snapshot**

    **Example request:**

    ```http
    POST /api/cephfs/subvolume/snapshot/clone HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "clone_name": "string",
        "group_name": "string",
        "snap_name": "string",
        "subvol_name": "string",
        "target_group_name": "string",
        "vol_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CephfsSubvolumeGroup

POST /api/cephfs/subvolume/group
:   **Example request:**

    ```http
    POST /api/cephfs/subvolume/group HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group_name": "string",
        "vol_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/subvolume/group/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **group_name** (*string*) -- (Required)

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/group/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **info** (*boolean*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/group/{vol_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cephfs/subvolume/group/{vol_name}
:   Parameters:
    :   - **vol_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/cephfs/subvolume/group/{vol_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group_name": "string",
        "size": 1
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/group/{vol_name}/info
:   Parameters:
    :   - **vol_name** (*string*) --

    Query Parameters:
    :   - **group_name** (*string*) -- (Required)

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/group/{vol_name}/info?group_name=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CephfsSubvolumeSnapshot

POST /api/cephfs/subvolume/snapshot
:   **Example request:**

    ```http
    POST /api/cephfs/subvolume/snapshot HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "group_name": "string",
        "snap_name": "string",
        "subvol_name": "string",
        "vol_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cephfs/subvolume/snapshot/{vol_name}/{subvol_name}
:   Parameters:
    :   - **vol_name** (*string*) --
        - **subvol_name** (*string*) --

    Query Parameters:
    :   - **snap_name** (*string*) -- (Required)
        - **group_name** (*string*) --
        - **force** (*boolean*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/snapshot/{vol_name}/{subvol_name}
:   Parameters:
    :   - **vol_name** (*string*) --
        - **subvol_name** (*string*) --

    Query Parameters:
    :   - **group_name** (*string*) --
        - **info** (*boolean*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/snapshot/{vol_name}/{subvol_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cephfs/subvolume/snapshot/{vol_name}/{subvol_name}/info
:   Parameters:
    :   - **vol_name** (*string*) --
        - **subvol_name** (*string*) --

    Query Parameters:
    :   - **snap_name** (*string*) -- (Required)
        - **group_name** (*string*) --

    **Example request:**

    ```http
    GET /api/cephfs/subvolume/snapshot/{vol_name}/{subvol_name}/info?snap_name=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Cluster

GET /api/cluster
:   **Get the cluster status**

    **Example request:**

    ```http
    GET /api/cluster HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster
:   **Update the cluster status**

    **Example request:**

    ```http
    PUT /api/cluster HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "status": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cluster/user
:   **Get list of ceph users**

    > Get list of ceph users and its associated data

    **Example request:**

    ```http
    GET /api/cluster/user HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cluster/user
:   **Create Ceph User**

    > Add a Ceph user, with its defined capabilities.

    **Example request:**

    ```http
    POST /api/cluster/user HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "capabilities": [
            {
                "cap": "string",
                "entity": "string"
            }
        ],
        "import_data": "string",
        "user_entity": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster/user
:   **Edit Ceph User Capabilities**

    > Change the ceph user capabilities.
    > Setting new capabilities will overwrite current ones.

    **Example request:**

    ```http
    PUT /api/cluster/user HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "capabilities": [
            {
                "cap": "string",
                "entity": "string"
            }
        ],
        "user_entity": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cluster/user/export
:   **Export Ceph Users**

    **Example request:**

    ```http
    POST /api/cluster/user/export HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "entities": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cluster/user/{user_entity}
:   **Delete Ceph User**

    > Delete a ceph user and it’s defined capabilities.

    Parameters:
    :   - **user_entity** (*string*) -- Entity to delete

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### ClusterConfiguration

GET /api/cluster_conf
:   **Example request:**

    ```http
    GET /api/cluster_conf HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cluster_conf
:   **Create/Update Cluster Configuration**

    **Example request:**

    ```http
    POST /api/cluster_conf HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "force_update": true,
        "name": "string",
        "value": [
            {
                "section": "string",
                "value": "string"
            }
        ]
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster_conf
:   **Example request:**

    ```http
    PUT /api/cluster_conf HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "options": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cluster_conf/filter
:   **Get Cluster Configuration by name**

    Query Parameters:
    :   - **names** (*string*) -- Config option names

    **Example request:**

    ```http
    GET /api/cluster_conf/filter HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/cluster_conf/{name}
:   Parameters:
    :   - **name** (*string*) --

    Query Parameters:
    :   - **section** (*string*) -- (Required)

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cluster_conf/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    GET /api/cluster_conf/{name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### CrushRule

GET /api/crush_rule
:   **List Crush Rule Configuration**

    **Example request:**

    ```http
    GET /api/crush_rule HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/crush_rule
:   **Example request:**

    ```http
    POST /api/crush_rule HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "device_class": "string",
        "failure_domain": "string",
        "name": "string",
        "pool_type": "string",
        "profile": "string",
        "root": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/crush_rule/{name}
:   Parameters:
    :   - **name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/crush_rule/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    GET /api/crush_rule/{name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Daemon

GET /api/daemon
:   List all daemons in the cluster. Also filter by the daemon types specified

    > param daemon_types:
    > :   List of daemon types to filter by.
    >
    > return:
    > :   Returns list of daemons.
    >
    > rtype:
    > :   list

    Query Parameters:
    :   - **daemon_types** (*string*) --

    **Example request:**

    ```http
    GET /api/daemon HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/daemon/{daemon_name}
:   Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/daemon/{daemon_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "action": "string",
        "container_image": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### ErasureCodeProfile

GET /api/erasure_code_profile
:   **List Erasure Code Profile Information**

    **Example request:**

    ```http
    GET /api/erasure_code_profile HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/erasure_code_profile
:   **Example request:**

    ```http
    POST /api/erasure_code_profile HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/erasure_code_profile/{name}
:   Parameters:
    :   - **name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/erasure_code_profile/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    GET /api/erasure_code_profile/{name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### FeatureTogglesEndpoint

GET /api/feature_toggles
:   **Get List Of Features**

    **Example request:**

    ```http
    GET /api/feature_toggles HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Grafana

POST /api/grafana/dashboards
:   Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/grafana/url
:   **List Grafana URL Instance**

    **Example request:**

    ```http
    GET /api/grafana/url HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/grafana/validation/{params}
:   Parameters:
    :   - **params** (*string*) --

    **Example request:**

    ```http
    GET /api/grafana/validation/{params} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Health

GET /api/health/full
:   **Example request:**

    ```http
    GET /api/health/full HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/health/get_cluster_capacity
:   **Example request:**

    ```http
    GET /api/health/get_cluster_capacity HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/health/get_cluster_fsid
:   **Example request:**

    ```http
    GET /api/health/get_cluster_fsid HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/health/get_telemetry_status
:   **Example request:**

    ```http
    GET /api/health/get_telemetry_status HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/health/minimal
:   **Get Cluster’s minimal health report**

    **Example request:**

    ```http
    GET /api/health/minimal HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Host

GET /api/host
:   **List Host Specifications**

    Query Parameters:
    :   - **sources** (*string*) -- Host Sources
        - **facts** (*boolean*) -- Host Facts
        - **offset** (*integer*) --
        - **limit** (*integer*) --
        - **search** (*string*) --
        - **sort** (*string*) --

    **Example request:**

    ```http
    GET /api/host HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/host
:   **Example request:**

    ```http
    POST /api/host HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "addr": "string",
        "hostname": "string",
        "labels": [
            "string"
        ],
        "status": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/host/{hostname}
:   Parameters:
    :   - **hostname** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/host/{hostname}
:   > Get the specified host.
    > :raises: cherrypy.HTTPError: If host not found.

    Parameters:
    :   - **hostname** (*string*) --

    **Example request:**

    ```http
    GET /api/host/{hostname} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/host/{hostname}
:   > Update the specified host.
    > Note, this is only supported when Ceph Orchestrator is enabled.
    > :param hostname: The name of the host to be processed.
    > :param update_labels: To update the labels.
    > :param labels: List of labels.
    > :param maintenance: Enter/Exit maintenance mode.
    > :param force: Force enter maintenance mode.
    > :param drain: Drain host

    Parameters:
    :   - **hostname** (*string*) -- Hostname

    **Example request:**

    ```http
    PUT /api/host/{hostname} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "drain": true,
        "force": true,
        "labels": [
            "string"
        ],
        "maintenance": true,
        "update_labels": true
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/host/{hostname}/daemons
:   Parameters:
    :   - **hostname** (*string*) --

    **Example request:**

    ```http
    GET /api/host/{hostname}/daemons HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/host/{hostname}/devices
:   Parameters:
    :   - **hostname** (*string*) --

    **Example request:**

    ```http
    GET /api/host/{hostname}/devices HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/host/{hostname}/identify_device
:   > Identify a device by switching on the device light for N seconds.
    > :param hostname: The hostname of the device to process.
    > :param device: The device identifier to process, e.g. `/dev/dm-0` or
    > `ABC1234DEF567-1R1234_ABC8DE0Q`.
    > :param duration: The duration in seconds how long the LED should flash.

    Parameters:
    :   - **hostname** (*string*) --

    **Example request:**

    ```http
    POST /api/host/{hostname}/identify_device HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "device": "string",
        "duration": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/host/{hostname}/inventory
:   **Get inventory of a host**

    Parameters:
    :   - **hostname** (*string*) -- Hostname

    Query Parameters:
    :   - **refresh** (*string*) -- Trigger asynchronous refresh

    **Example request:**

    ```http
    GET /api/host/{hostname}/inventory HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/host/{hostname}/smart
:   Parameters:
    :   - **hostname** (*string*) --

    **Example request:**

    ```http
    GET /api/host/{hostname}/smart HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Iscsi

GET /api/iscsi/discoveryauth
:   **Get Iscsi discoveryauth Details**

    **Example request:**

    ```http
    GET /api/iscsi/discoveryauth HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/iscsi/discoveryauth
:   **Set Iscsi discoveryauth**

    Query Parameters:
    :   - **user** (*string*) -- Username
          (Required)
        - **password** (*string*) -- Password
          (Required)
        - **mutual_user** (*string*) -- Mutual UserName
          (Required)
        - **mutual_password** (*string*) -- Mutual Password
          (Required)

    **Example request:**

    ```http
    PUT /api/iscsi/discoveryauth?user=string&password=string&mutual_user=string&mutual_password=string HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "mutual_password": "string",
        "mutual_user": "string",
        "password": "string",
        "user": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### IscsiTarget

GET /api/iscsi/target
:   **Example request:**

    ```http
    GET /api/iscsi/target HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/iscsi/target
:   **Example request:**

    ```http
    POST /api/iscsi/target HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "acl_enabled": "string",
        "auth": "string",
        "clients": "string",
        "disks": "string",
        "groups": "string",
        "portals": "string",
        "target_controls": "string",
        "target_iqn": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/iscsi/target/{target_iqn}
:   Parameters:
    :   - **target_iqn** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/iscsi/target/{target_iqn}
:   Parameters:
    :   - **target_iqn** (*string*) --

    **Example request:**

    ```http
    GET /api/iscsi/target/{target_iqn} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/iscsi/target/{target_iqn}
:   Parameters:
    :   - **target_iqn** (*string*) --

    **Example request:**

    ```http
    PUT /api/iscsi/target/{target_iqn} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "acl_enabled": "string",
        "auth": "string",
        "clients": "string",
        "disks": "string",
        "groups": "string",
        "new_target_iqn": "string",
        "portals": "string",
        "target_controls": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Logs

GET /api/logs/all
:   **Display Logs Configuration**

    **Example request:**

    ```http
    GET /api/logs/all HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### MdsPerfCounter

GET /api/perf_counters/mds/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/mds/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### MgrModule

GET /api/mgr/module
:   **List Mgr modules**

    > Get the list of managed modules.
    > :return: A list of objects with the fields ‘enabled’, ‘name’ and ‘options’.
    > :rtype: list

    **Example request:**

    ```http
    GET /api/mgr/module HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/mgr/module/{module_name}
:   > Retrieve the values of the persistent configuration settings.
    > :param module_name: The name of the Ceph Mgr module.
    > :type module_name: str
    > :return: The values of the module options.
    > :rtype: dict

    Parameters:
    :   - **module_name** (*string*) --

    **Example request:**

    ```http
    GET /api/mgr/module/{module_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/mgr/module/{module_name}
:   > Set the values of the persistent configuration settings.
    > :param module_name: The name of the Ceph Mgr module.
    > :type module_name: str
    > :param config: The values of the module options to be stored.
    > :type config: dict

    Parameters:
    :   - **module_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/mgr/module/{module_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "config": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/mgr/module/{module_name}/disable
:   > Disable the specified Ceph Mgr module.
    > :param module_name: The name of the Ceph Mgr module.
    > :type module_name: str

    Parameters:
    :   - **module_name** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/mgr/module/{module_name}/enable
:   > Enable the specified Ceph Mgr module.
    > :param module_name: The name of the Ceph Mgr module.
    > :type module_name: str

    Parameters:
    :   - **module_name** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/mgr/module/{module_name}/options
:   > Get the module options of the specified Ceph Mgr module.
    > :param module_name: The name of the Ceph Mgr module.
    > :type module_name: str
    > :return: The module options as list of dicts.
    > :rtype: list

    Parameters:
    :   - **module_name** (*string*) --

    **Example request:**

    ```http
    GET /api/mgr/module/{module_name}/options HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### MgrPerfCounter

GET /api/perf_counters/mgr/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/mgr/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### MonPerfCounter

GET /api/perf_counters/mon/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/mon/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Monitor

GET /api/monitor
:   **Get Monitor Details**

    **Example request:**

    ```http
    GET /api/monitor HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NFS-Ganesha

GET /api/nfs-ganesha/cluster
:   **Example request:**

    ```http
    GET /api/nfs-ganesha/cluster HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nfs-ganesha/export
:   **List all or cluster specific NFS-Ganesha exports**

    **Example request:**

    ```http
    GET /api/nfs-ganesha/export HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/nfs-ganesha/export
:   **Creates a new NFS-Ganesha export**

    **Example request:**

    ```http
    POST /api/nfs-ganesha/export HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_type": "string",
        "clients": [
            {
                "access_type": "string",
                "addresses": [
                    "string"
                ],
                "squash": "string"
            }
        ],
        "cluster_id": "string",
        "fsal": {
            "fs_name": "string",
            "name": "string",
            "sec_label_xattr": "string"
        },
        "path": "string",
        "protocols": [
            1
        ],
        "pseudo": "string",
        "security_label": "string",
        "squash": "string",
        "transports": [
            "string"
        ]
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/nfs-ganesha/export/{cluster_id}/{export_id}
:   **Deletes an NFS-Ganesha export**

    Parameters:
    :   - **cluster_id** (*string*) -- Cluster identifier
        - **export_id** (*integer*) -- Export ID

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nfs-ganesha/export/{cluster_id}/{export_id}
:   **Get an NFS-Ganesha export**

    Parameters:
    :   - **cluster_id** (*string*) -- Cluster identifier
        - **export_id** (*string*) -- Export ID

    **Example request:**

    ```http
    GET /api/nfs-ganesha/export/{cluster_id}/{export_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/nfs-ganesha/export/{cluster_id}/{export_id}
:   **Updates an NFS-Ganesha export**

    Parameters:
    :   - **cluster_id** (*string*) -- Cluster identifier
        - **export_id** (*integer*) -- Export ID

    **Example request:**

    ```http
    PUT /api/nfs-ganesha/export/{cluster_id}/{export_id} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_type": "string",
        "clients": [
            {
                "access_type": "string",
                "addresses": [
                    "string"
                ],
                "squash": "string"
            }
        ],
        "fsal": {
            "fs_name": "string",
            "name": "string",
            "sec_label_xattr": "string"
        },
        "path": "string",
        "protocols": [
            1
        ],
        "pseudo": "string",
        "security_label": "string",
        "squash": "string",
        "transports": [
            "string"
        ]
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Gateway

GET /api/nvmeof/gateway
:   **Get information about the NVMeoF gateway**

    Query Parameters:
    :   - **gw_group** (*string*) --

    **Example request:**

    ```http
    GET /api/nvmeof/gateway HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/gateway/group
:   **Example request:**

    ```http
    GET /api/nvmeof/gateway/group HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/gateway/log_level
:   Query Parameters:
    :   - **gw_group** (*string*) --

    **Example request:**

    ```http
    GET /api/nvmeof/gateway/log_level HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/nvmeof/gateway/log_level
:   **Example request:**

    ```http
    PUT /api/nvmeof/gateway/log_level HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "gw_group": "string",
        "log_level": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/gateway/version
:   Query Parameters:
    :   - **gw_group** (*string*) --

    **Example request:**

    ```http
    GET /api/nvmeof/gateway/version HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF SPDK

GET /api/nvmeof/spdk/log_level
:   Query Parameters:
    :   - **gw_group** (*string*) --

    **Example request:**

    ```http
    GET /api/nvmeof/spdk/log_level HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/nvmeof/spdk/log_level
:   **Example request:**

    ```http
    PUT /api/nvmeof/spdk/log_level HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "gw_group": "string",
        "log_level": "string",
        "print_level": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/nvmeof/spdk/log_level/disable
:   **Example request:**

    ```http
    PUT /api/nvmeof/spdk/log_level/disable HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "gw_group": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Subsystem

GET /api/nvmeof/subsystem
:   **List all NVMeoF subsystems**

    Query Parameters:
    :   - **gw_group** (*string*) --

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/nvmeof/subsystem
:   **Create a new NVMeoF subsystem**

    **Example request:**

    ```http
    POST /api/nvmeof/subsystem HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "enable_ha": true,
        "gw_group": "string",
        "max_namespaces": 1,
        "nqn": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/nvmeof/subsystem/{nqn}
:   **Delete an existing NVMeoF subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **force** (*boolean*) -- Force delete
        - **gw_group** (*string*) -- NVMeoF gateway group

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/subsystem/{nqn}
:   **Get information from a specific NVMeoF subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Subsystem Connection

GET /api/nvmeof/subsystem/{nqn}/connection
:   **List all NVMeoF Subsystem Connections**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/connection HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Subsystem Host Allowlist

GET /api/nvmeof/subsystem/{nqn}/host
:   **List all allowed hosts for an NVMeoF subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/host HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/nvmeof/subsystem/{nqn}/host
:   **Allow hosts to access an NVMeoF subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    **Example request:**

    ```http
    POST /api/nvmeof/subsystem/{nqn}/host HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "gw_group": "string",
        "host_nqn": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/nvmeof/subsystem/{nqn}/host/{host_nqn}
:   **Disallow hosts from accessing an NVMeoF subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **host_nqn** (*string*) -- NVMeoF host NQN. Use “\*” to disallow any host.

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Subsystem Listener

GET /api/nvmeof/subsystem/{nqn}/listener
:   **List all NVMeoF listeners**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/listener HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/nvmeof/subsystem/{nqn}/listener
:   **Create a new NVMeoF listener**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    **Example request:**

    ```http
    POST /api/nvmeof/subsystem/{nqn}/listener HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "adrfam": 1,
        "gw_group": "string",
        "host_name": "string",
        "traddr": "string",
        "trsvcid": 1
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/nvmeof/subsystem/{nqn}/listener/{host_name}/{traddr}
:   **Delete an existing NVMeoF listener**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **host_name** (*string*) -- NVMeoF hostname
        - **traddr** (*string*) -- NVMeoF transport address

    Query Parameters:
    :   - **trsvcid** (*integer*) -- NVMeoF transport service port
        - **adrfam** (*integer*) -- NVMeoF address family (0 - IPv4, 1 - IPv6)
        - **force** (*boolean*) --
        - **gw_group** (*string*) -- NVMeoF gateway group

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### NVMe-oF Subsystem Namespace

GET /api/nvmeof/subsystem/{nqn}/namespace
:   **List all NVMeoF namespaces in a subsystem**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/namespace HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/nvmeof/subsystem/{nqn}/namespace
:   **Create a new NVMeoF namespace**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN

    **Example request:**

    ```http
    POST /api/nvmeof/subsystem/{nqn}/namespace HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "block_size": 1,
        "create_image": true,
        "gw_group": "string",
        "load_balancing_group": 1,
        "rbd_image_name": "string",
        "rbd_image_size": 1,
        "rbd_pool": "string",
        "size": 1
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/nvmeof/subsystem/{nqn}/namespace/{nsid}
:   **Delete an existing NVMeoF namespace**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **nsid** (*string*) -- NVMeoF Namespace ID

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/subsystem/{nqn}/namespace/{nsid}
:   **Get info from specified NVMeoF namespace**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **nsid** (*string*) -- NVMeoF Namespace ID

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/namespace/{nsid} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PATCH /api/nvmeof/subsystem/{nqn}/namespace/{nsid}
:   **Update an existing NVMeoF namespace**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **nsid** (*string*) -- NVMeoF Namespace ID

    **Example request:**

    ```http
    PATCH /api/nvmeof/subsystem/{nqn}/namespace/{nsid} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "gw_group": "string",
        "load_balancing_group": 1,
        "r_mbytes_per_second": 1,
        "rbd_image_size": 1,
        "rw_ios_per_second": 1,
        "rw_mbytes_per_second": 1,
        "w_mbytes_per_second": 1
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/nvmeof/subsystem/{nqn}/namespace/{nsid}/io_stats
:   **Get IO stats from specified NVMeoF namespace**

    Parameters:
    :   - **nqn** (*string*) -- NVMeoF subsystem NQN
        - **nsid** (*string*) -- NVMeoF Namespace ID

    Query Parameters:
    :   - **gw_group** (*string*) -- NVMeoF gateway group

    **Example request:**

    ```http
    GET /api/nvmeof/subsystem/{nqn}/namespace/{nsid}/io_stats HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### OSD

GET /api/osd
:   Query Parameters:
    :   - **offset** (*integer*) --
        - **limit** (*integer*) --
        - **search** (*string*) --
        - **sort** (*string*) --

    **Example request:**

    ```http
    GET /api/osd HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/osd
:   **Example request:**

    ```http
    POST /api/osd HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "data": "string",
        "method": "string",
        "tracking_id": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/flags
:   **Display OSD Flags**

    **Example request:**

    ```http
    GET /api/osd/flags HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/osd/flags
:   **Sets OSD flags for the entire cluster.**

    > The recovery_deletes, sortbitwise and pglog_hardlimit flags cannot be unset.
    > purged_snapshots cannot even be set. It is therefore required to at
    > least include those four flags for a successful operation.

    **Example request:**

    ```http
    PUT /api/osd/flags HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "flags": [
            "string"
        ]
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/flags/individual
:   **Displays individual OSD flags**

    **Example request:**

    ```http
    GET /api/osd/flags/individual HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/osd/flags/individual
:   **Sets OSD flags for a subset of individual OSDs.**

    > Updates flags (noout, noin, nodown, noup) for an individual
    > subset of OSDs.

    **Example request:**

    ```http
    PUT /api/osd/flags/individual HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "flags": {
            "nodown": true,
            "noin": true,
            "noout": true,
            "noup": true
        },
        "ids": [
            1
        ]
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/safe_to_delete
:   > type ids:
    > :   int|[int]

    Query Parameters:
    :   - **svc_ids** (*string*) -- (Required)

    **Example request:**

    ```http
    GET /api/osd/safe_to_delete?svc_ids=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/safe_to_destroy
:   **Check If OSD is Safe to Destroy**

    > type ids:
    > :   int|[int]

    Query Parameters:
    :   - **ids** (*string*) -- OSD Service Identifier
          (Required)

    **Example request:**

    ```http
    GET /api/osd/safe_to_destroy?ids=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/settings
:   **Example request:**

    ```http
    GET /api/osd/settings HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/osd/{svc_id}
:   Parameters:
    :   - **svc_id** (*string*) --

    Query Parameters:
    :   - **preserve_id** (*string*) --
        - **force** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/{svc_id}
:   > Returns collected data about an OSD.
    >
    > return:
    > :   Returns the requested data.

    Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    GET /api/osd/{svc_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/osd/{svc_id}
:   Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    PUT /api/osd/{svc_id} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "device_class": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/osd/{svc_id}/destroy
:   > Mark osd as being destroyed. Keeps the ID intact (allowing reuse), but
    > removes cephx keys, config-key data and lockbox keys, rendering data
    > permanently unreadable.
    >
    > The osd must be marked down before being destroyed.

    Parameters:
    :   - **svc_id** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/{svc_id}/devices
:   Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    GET /api/osd/{svc_id}/devices HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/{svc_id}/histogram
:   > return:
    > :   Returns the histogram data.

    Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    GET /api/osd/{svc_id}/histogram HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/osd/{svc_id}/mark
:   **Mark OSD flags (out, in, down, lost, …)**

    > Note: osd must be marked down before marking lost.

    Parameters:
    :   - **svc_id** (*string*) -- SVC ID

    **Example request:**

    ```http
    PUT /api/osd/{svc_id}/mark HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "action": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/osd/{svc_id}/purge
:   > Note: osd must be marked down before removal.

    Parameters:
    :   - **svc_id** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/osd/{svc_id}/reweight
:   > Reweights the OSD temporarily.
    >
    > Note that ‘ceph osd reweight’ is not a persistent setting. When an OSD
    > gets marked out, the osd weight will be set to 0. When it gets marked
    > in again, the weight will be changed to 1.
    >
    > Because of this ‘ceph osd reweight’ is a temporary solution. You should
    > only use it to keep your cluster running while you’re ordering more
    > hardware.
    >
    > - Craig Lewis (<http://lists.ceph.com/pipermail/ceph-users-ceph.com/2014-June/040967.html>)

    Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    POST /api/osd/{svc_id}/reweight HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "weight": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/osd/{svc_id}/scrub
:   Parameters:
    :   - **svc_id** (*string*) --

    Query Parameters:
    :   - **deep** (*boolean*) --

    **Example request:**

    ```http
    POST /api/osd/{svc_id}/scrub HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "deep": true
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/osd/{svc_id}/smart
:   Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    GET /api/osd/{svc_id}/smart HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### OsdPerfCounter

GET /api/perf_counters/osd/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/osd/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### PerfCounters

GET /api/perf_counters
:   **Display Perf Counters**

    **Example request:**

    ```http
    GET /api/perf_counters HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Pool

GET /api/pool
:   **Display Pool List**

    Query Parameters:
    :   - **attrs** (*string*) -- Pool Attributes
        - **stats** (*boolean*) -- Pool Stats

    **Example request:**

    ```http
    GET /api/pool HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/pool
:   **Example request:**

    ```http
    POST /api/pool HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "pool": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/pool/{pool_name}
:   Parameters:
    :   - **pool_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/pool/{pool_name}
:   Parameters:
    :   - **pool_name** (*string*) --

    Query Parameters:
    :   - **attrs** (*string*) --
        - **stats** (*boolean*) --

    **Example request:**

    ```http
    GET /api/pool/{pool_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/pool/{pool_name}
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/pool/{pool_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "application_metadata": "string",
        "configuration": "string",
        "flags": "string",
        "rbd_mirroring": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/pool/{pool_name}/configuration
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    GET /api/pool/{pool_name}/configuration HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Prometheus

GET /api/prometheus
:   **Example request:**

    ```http
    GET /api/prometheus HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/prometheus/alertgroup
:   **Example request:**

    ```http
    GET /api/prometheus/alertgroup HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/prometheus/data
:   **Example request:**

    ```http
    GET /api/prometheus/data HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/prometheus/rules
:   **Example request:**

    ```http
    GET /api/prometheus/rules HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/prometheus/silence
:   Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/prometheus/silence/{s_id}
:   Parameters:
    :   - **s_id** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/prometheus/silences
:   **Example request:**

    ```http
    GET /api/prometheus/silences HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### PrometheusNotifications

GET /api/prometheus/notifications
:   **Example request:**

    ```http
    GET /api/prometheus/notifications HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RGW

GET /api/rgw/roles
:   **List RGW roles**

    **Example request:**

    ```http
    GET /api/rgw/roles HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/roles
:   **Create RGW role**

    **Example request:**

    ```http
    POST /api/rgw/roles HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "role_assume_policy_doc": "string",
        "role_name": "string",
        "role_path": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/roles
:   **Edit RGW role**

    **Example request:**

    ```http
    PUT /api/rgw/roles HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "max_session_duration": "string",
        "role_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/roles/{role_name}
:   **Delete RGW role**

    Parameters:
    :   - **role_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Rbd

GET /api/block/image
:   **Display Rbd Images**

    Query Parameters:
    :   - **pool_name** (*string*) -- Pool Name
        - **offset** (*integer*) -- offset
        - **limit** (*integer*) -- limit
        - **search** (*string*) --
        - **sort** (*string*) --

    **Example request:**

    ```http
    GET /api/block/image HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image
:   **Example request:**

    ```http
    POST /api/block/image HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "configuration": "string",
        "data_pool": "string",
        "features": "string",
        "metadata": "string",
        "mirror_mode": "string",
        "name": "string",
        "namespace": "string",
        "obj_size": 1,
        "pool_name": "string",
        "schedule_interval": "string",
        "size": 1,
        "stripe_count": 1,
        "stripe_unit": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/block/image/clone_format_version
:   Return the RBD clone format version.

    **Example request:**

    ```http
    GET /api/block/image/clone_format_version HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/block/image/default_features
:   **Example request:**

    ```http
    GET /api/block/image/default_features HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/block/image/{image_spec}
:   Parameters:
    :   - **image_spec** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/block/image/{image_spec}
:   **Get Rbd Image Info**

    Parameters:
    :   - **image_spec** (*string*) -- URL-encoded “pool/rbd_name”. e.g. “rbd%2Ffoo”

    Query Parameters:
    :   - **omit_usage** (*boolean*) -- When true, usage information is not returned

    **Example request:**

    ```http
    GET /api/block/image/{image_spec} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/block/image/{image_spec}
:   Parameters:
    :   - **image_spec** (*string*) --

    **Example request:**

    ```http
    PUT /api/block/image/{image_spec} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "configuration": "string",
        "enable_mirror": "string",
        "features": "string",
        "force": true,
        "image_mirror_mode": "string",
        "metadata": "string",
        "mirror_mode": "string",
        "name": "string",
        "primary": "string",
        "remove_scheduling": true,
        "resync": true,
        "schedule_interval": "string",
        "size": 1
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/{image_spec}/copy
:   Parameters:
    :   - **image_spec** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/{image_spec}/copy HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "configuration": "string",
        "data_pool": "string",
        "dest_image_name": "string",
        "dest_namespace": "string",
        "dest_pool_name": "string",
        "features": "string",
        "metadata": "string",
        "obj_size": 1,
        "snapshot_name": "string",
        "stripe_count": 1,
        "stripe_unit": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/{image_spec}/flatten
:   Parameters:
    :   - **image_spec** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/{image_spec}/move_trash
:   Move an image to the trash.
    :   Images, even ones actively in-use by clones,
        can be moved to the trash and deleted at a later time.

    Parameters:
    :   - **image_spec** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/{image_spec}/move_trash HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "delay": 1
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdMirroring

GET /api/block/mirroring/site_name
:   **Display Rbd Mirroring sitename**

    **Example request:**

    ```http
    GET /api/block/mirroring/site_name HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/block/mirroring/site_name
:   **Example request:**

    ```http
    PUT /api/block/mirroring/site_name HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "site_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdMirroringPoolBootstrap

POST /api/block/mirroring/pool/{pool_name}/bootstrap/peer
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    POST /api/block/mirroring/pool/{pool_name}/bootstrap/peer HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "direction": "string",
        "token": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/mirroring/pool/{pool_name}/bootstrap/token
:   Parameters:
    :   - **pool_name** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdMirroringPoolMode

GET /api/block/mirroring/pool/{pool_name}
:   **Display Rbd Mirroring Summary**

    Parameters:
    :   - **pool_name** (*string*) -- Pool Name

    **Example request:**

    ```http
    GET /api/block/mirroring/pool/{pool_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/block/mirroring/pool/{pool_name}
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/block/mirroring/pool/{pool_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "mirror_mode": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdMirroringPoolPeer

GET /api/block/mirroring/pool/{pool_name}/peer
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    GET /api/block/mirroring/pool/{pool_name}/peer HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/mirroring/pool/{pool_name}/peer
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    POST /api/block/mirroring/pool/{pool_name}/peer HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "client_id": "string",
        "cluster_name": "string",
        "key": "string",
        "mon_host": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/block/mirroring/pool/{pool_name}/peer/{peer_uuid}
:   Parameters:
    :   - **pool_name** (*string*) --
        - **peer_uuid** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/block/mirroring/pool/{pool_name}/peer/{peer_uuid}
:   Parameters:
    :   - **pool_name** (*string*) --
        - **peer_uuid** (*string*) --

    **Example request:**

    ```http
    GET /api/block/mirroring/pool/{pool_name}/peer/{peer_uuid} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/block/mirroring/pool/{pool_name}/peer/{peer_uuid}
:   Parameters:
    :   - **pool_name** (*string*) --
        - **peer_uuid** (*string*) --

    **Example request:**

    ```http
    PUT /api/block/mirroring/pool/{pool_name}/peer/{peer_uuid} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "client_id": "string",
        "cluster_name": "string",
        "key": "string",
        "mon_host": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdMirroringSummary

GET /api/block/mirroring/summary
:   **Display Rbd Mirroring Summary**

    **Example request:**

    ```http
    GET /api/block/mirroring/summary HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdNamespace

GET /api/block/pool/{pool_name}/namespace
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    GET /api/block/pool/{pool_name}/namespace HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/pool/{pool_name}/namespace
:   Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    POST /api/block/pool/{pool_name}/namespace HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "namespace": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/block/pool/{pool_name}/namespace/{namespace}
:   Parameters:
    :   - **pool_name** (*string*) --
        - **namespace** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdSnapshot

POST /api/block/image/{image_spec}/snap
:   Parameters:
    :   - **image_spec** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/{image_spec}/snap HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "mirrorImageSnapshot": "string",
        "snapshot_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/block/image/{image_spec}/snap/{snapshot_name}
:   Parameters:
    :   - **image_spec** (*string*) --
        - **snapshot_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/block/image/{image_spec}/snap/{snapshot_name}
:   Parameters:
    :   - **image_spec** (*string*) --
        - **snapshot_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/block/image/{image_spec}/snap/{snapshot_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "is_protected": true,
        "new_snap_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/{image_spec}/snap/{snapshot_name}/clone
:   > Clones a snapshot to an image

    Parameters:
    :   - **image_spec** (*string*) --
        - **snapshot_name** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/{image_spec}/snap/{snapshot_name}/clone HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "child_image_name": "string",
        "child_namespace": "string",
        "child_pool_name": "string",
        "configuration": "string",
        "data_pool": "string",
        "features": "string",
        "metadata": "string",
        "obj_size": 1,
        "stripe_count": 1,
        "stripe_unit": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/{image_spec}/snap/{snapshot_name}/rollback
:   Parameters:
    :   - **image_spec** (*string*) --
        - **snapshot_name** (*string*) --

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RbdTrash

GET /api/block/image/trash
:   **Get RBD Trash Details by pool name**

    List all entries from trash.

    Query Parameters:
    :   - **pool_name** (*string*) -- Name of the pool

    **Example request:**

    ```http
    GET /api/block/image/trash HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/trash/purge
:   Remove all expired images from trash.

    Query Parameters:
    :   - **pool_name** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/trash/purge HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "pool_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/block/image/trash/{image_id_spec}
:   Delete an image from trash.
    :   If image deferment time has not expired you can not removed it unless use force.
        But an actively in-use by clones or has snapshots can not be removed.

    Parameters:
    :   - **image_id_spec** (*string*) --

    Query Parameters:
    :   - **force** (*boolean*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/block/image/trash/{image_id_spec}/restore
:   Restore an image from trash.

    Parameters:
    :   - **image_id_spec** (*string*) --

    **Example request:**

    ```http
    POST /api/block/image/trash/{image_id_spec}/restore HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "new_image_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Report

GET /api/feedback
:   > List all issues details.

    **Example request:**

    ```http
    GET /api/feedback HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/feedback
:   > Create an issue.
    > :param project: The affected ceph component.
    > :param tracker: The tracker type.
    > :param subject: The title of the issue.
    > :param description: The description of the issue.
    > :param api_key: Ceph tracker api key.

    **Example request:**

    ```http
    POST /api/feedback HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "api_key": "string",
        "description": "string",
        "project": "string",
        "subject": "string",
        "tracker": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/feedback/api_key
:   > Deletes Ceph tracker API key.

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/feedback/api_key
:   > Returns Ceph tracker API key.

    **Example request:**

    ```http
    GET /api/feedback/api_key HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/feedback/api_key
:   > Sets Ceph tracker API key.
    > :param api_key: The Ceph tracker API key.

    **Example request:**

    ```http
    POST /api/feedback/api_key HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "api_key": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwBucket

GET /api/rgw/bucket
:   Query Parameters:
    :   - **stats** (*boolean*) --
        - **daemon_name** (*string*) --
        - **uid** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/bucket HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/bucket
:   **Example request:**

    ```http
    POST /api/rgw/bucket HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket": "string",
        "bucket_policy": "string",
        "canned_acl": "string",
        "daemon_name": "string",
        "encryption_state": "string",
        "encryption_type": "string",
        "key_id": "string",
        "lock_enabled": "string",
        "lock_mode": "string",
        "lock_retention_period_days": "string",
        "lock_retention_period_years": "string",
        "placement_target": "string",
        "replication": "string",
        "tags": "string",
        "uid": "string",
        "zonegroup": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/bucket/deleteEncryption
:   Query Parameters:
    :   - **bucket_name** (*string*) -- (Required)
        - **daemon_name** (*string*) --
        - **owner** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/bucket/getEncryption
:   Query Parameters:
    :   - **bucket_name** (*string*) -- (Required)
        - **daemon_name** (*string*) --
        - **owner** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/bucket/getEncryption?bucket_name=string HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/bucket/getEncryptionConfig
:   Query Parameters:
    :   - **daemon_name** (*string*) --
        - **owner** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/bucket/getEncryptionConfig HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/bucket/setEncryptionConfig
:   **Example request:**

    ```http
    PUT /api/rgw/bucket/setEncryptionConfig HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "address": "string",
        "auth_method": "string",
        "client_cert": "string",
        "client_key": "string",
        "daemon_name": "string",
        "encryption_type": "string",
        "kms_provider": "string",
        "namespace": "string",
        "owner": "string",
        "secret_engine": "string",
        "secret_path": "string",
        "ssl_cert": "string",
        "token": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/bucket/{bucket}
:   Parameters:
    :   - **bucket** (*string*) --

    Query Parameters:
    :   - **daemon_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/bucket/{bucket}
:   Parameters:
    :   - **bucket** (*string*) --

    Query Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/bucket/{bucket} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/bucket/{bucket}
:   Parameters:
    :   - **bucket** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/bucket/{bucket} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket_id": "string",
        "bucket_policy": "string",
        "canned_acl": "string",
        "daemon_name": "string",
        "encryption_state": "string",
        "encryption_type": "string",
        "key_id": "string",
        "lifecycle": "string",
        "lock_mode": "string",
        "lock_retention_period_days": "string",
        "lock_retention_period_years": "string",
        "mfa_delete": "string",
        "mfa_token_pin": "string",
        "mfa_token_serial": "string",
        "replication": "string",
        "tags": "string",
        "uid": "string",
        "versioning_state": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwDaemon

GET /api/rgw/daemon
:   **Display RGW Daemons**

    **Example request:**

    ```http
    GET /api/rgw/daemon HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/daemon/set_multisite_config
:   **Example request:**

    ```http
    PUT /api/rgw/daemon/set_multisite_config HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "daemon_name": "string",
        "realm_name": "string",
        "zone_name": "string",
        "zonegroup_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/daemon/{svc_id}
:   Parameters:
    :   - **svc_id** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/daemon/{svc_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwMirrorPerfCounter

GET /api/perf_counters/rbd-mirror/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/rbd-mirror/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwMultisite

PUT /api/rgw/multisite/sync-flow
:   **Create or update the sync flow**

    **Example request:**

    ```http
    PUT /api/rgw/multisite/sync-flow HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket_name": "string",
        "destination_zone": "string",
        "flow_id": "string",
        "flow_type": "string",
        "group_id": "string",
        "source_zone": "string",
        "zones": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/multisite/sync-flow/{flow_id}/{flow_type}/{group_id}
:   **Remove the sync flow**

    Parameters:
    :   - **flow_id** (*string*) --
        - **flow_type** (*string*) --
        - **group_id** (*string*) --

    Query Parameters:
    :   - **source_zone** (*string*) --
        - **destination_zone** (*string*) --
        - **zones** (*string*) --
        - **bucket_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/multisite/sync-pipe
:   **Create or update the sync pipe**

    **Example request:**

    ```http
    PUT /api/rgw/multisite/sync-pipe HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket_name": "string",
        "destination_bucket": "string",
        "destination_zones": "string",
        "group_id": "string",
        "mode": "string",
        "pipe_id": "string",
        "source_bucket": "string",
        "source_zones": "string",
        "user": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/multisite/sync-pipe/{group_id}/{pipe_id}
:   **Remove the sync pipe**

    Parameters:
    :   - **group_id** (*string*) --
        - **pipe_id** (*string*) --

    Query Parameters:
    :   - **source_zones** (*string*) --
        - **destination_zones** (*string*) --
        - **bucket_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/multisite/sync-policy
:   **Get the sync policy**

    Query Parameters:
    :   - **bucket_name** (*string*) --
        - **zonegroup_name** (*string*) --
        - **all_policy** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/multisite/sync-policy HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/multisite/sync-policy-group
:   **Create the sync policy group**

    **Example request:**

    ```http
    POST /api/rgw/multisite/sync-policy-group HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket_name": "string",
        "group_id": "string",
        "status": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/multisite/sync-policy-group
:   **Update the sync policy group**

    **Example request:**

    ```http
    PUT /api/rgw/multisite/sync-policy-group HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "bucket_name": "string",
        "group_id": "string",
        "status": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/multisite/sync-policy-group/{group_id}
:   **Remove the sync policy group**

    Parameters:
    :   - **group_id** (*string*) --

    Query Parameters:
    :   - **bucket_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/multisite/sync-policy-group/{group_id}
:   **Get the sync policy group**

    Parameters:
    :   - **group_id** (*string*) --

    Query Parameters:
    :   - **bucket_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/multisite/sync-policy-group/{group_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/multisite/sync_status
:   **Get the sync status**

    Query Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/multisite/sync_status HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwPerfCounter

GET /api/perf_counters/rgw/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/rgw/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwRealm

GET /api/rgw/realm
:   **Example request:**

    ```http
    GET /api/rgw/realm HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/realm
:   **Example request:**

    ```http
    POST /api/rgw/realm HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "default": "string",
        "realm_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/realm/get_all_realms_info
:   **Example request:**

    ```http
    GET /api/rgw/realm/get_all_realms_info HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/realm/get_realm_tokens
:   **Example request:**

    ```http
    GET /api/rgw/realm/get_realm_tokens HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/realm/import_realm_token
:   **Example request:**

    ```http
    POST /api/rgw/realm/import_realm_token HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "placement_spec": "string",
        "port": "string",
        "realm_token": "string",
        "zone_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/realm/{realm_name}
:   Parameters:
    :   - **realm_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/realm/{realm_name}
:   Parameters:
    :   - **realm_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/realm/{realm_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/realm/{realm_name}
:   Parameters:
    :   - **realm_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/realm/{realm_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "default": "string",
        "new_realm_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwSite

GET /api/rgw/site
:   Query Parameters:
    :   - **query** (*string*) --
        - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/site HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwUser

GET /api/rgw/user
:   **Display RGW Users**

    Query Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/user HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/user
:   **Example request:**

    ```http
    POST /api/rgw/user HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_key": "string",
        "daemon_name": "string",
        "display_name": "string",
        "email": "string",
        "generate_key": "string",
        "max_buckets": "string",
        "secret_key": "string",
        "suspended": "string",
        "system": "string",
        "uid": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/user/get_emails
:   Query Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/user/get_emails HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/user/{uid}
:   Parameters:
    :   - **uid** (*string*) --

    Query Parameters:
    :   - **daemon_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/user/{uid}
:   Parameters:
    :   - **uid** (*string*) --

    Query Parameters:
    :   - **daemon_name** (*string*) --
        - **stats** (*boolean*) --

    **Example request:**

    ```http
    GET /api/rgw/user/{uid} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/user/{uid}
:   Parameters:
    :   - **uid** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/user/{uid} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "daemon_name": "string",
        "display_name": "string",
        "email": "string",
        "max_buckets": "string",
        "suspended": "string",
        "system": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/user/{uid}/capability
:   Parameters:
    :   - **uid** (*string*) --

    Query Parameters:
    :   - **type** (*string*) -- (Required)
        - **perm** (*string*) -- (Required)
        - **daemon_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/user/{uid}/capability
:   Parameters:
    :   - **uid** (*string*) --

    **Example request:**

    ```http
    POST /api/rgw/user/{uid}/capability HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "daemon_name": "string",
        "perm": "string",
        "type": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/user/{uid}/key
:   Parameters:
    :   - **uid** (*string*) --

    Query Parameters:
    :   - **key_type** (*string*) --
        - **subuser** (*string*) --
        - **access_key** (*string*) --
        - **daemon_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/user/{uid}/key
:   Parameters:
    :   - **uid** (*string*) --

    **Example request:**

    ```http
    POST /api/rgw/user/{uid}/key HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_key": "string",
        "daemon_name": "string",
        "generate_key": "string",
        "key_type": "string",
        "secret_key": "string",
        "subuser": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/user/{uid}/quota
:   Parameters:
    :   - **uid** (*string*) --

    Query Parameters:
    :   - **daemon_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/user/{uid}/quota HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/user/{uid}/quota
:   Parameters:
    :   - **uid** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/user/{uid}/quota HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "daemon_name": "string",
        "enabled": "string",
        "max_objects": "string",
        "max_size_kb": 1,
        "quota_type": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/user/{uid}/subuser
:   Parameters:
    :   - **uid** (*string*) --

    **Example request:**

    ```http
    POST /api/rgw/user/{uid}/subuser HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access": "string",
        "access_key": "string",
        "daemon_name": "string",
        "generate_secret": "string",
        "key_type": "string",
        "secret_key": "string",
        "subuser": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/user/{uid}/subuser/{subuser}
:   > param purge_keys:
    > :   Set to False to do not purge the keys.
    >     Note, this only works for s3 subusers.

    Parameters:
    :   - **uid** (*string*) --
        - **subuser** (*string*) --

    Query Parameters:
    :   - **purge_keys** (*string*) --
        - **daemon_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwZone

GET /api/rgw/zone
:   **Example request:**

    ```http
    GET /api/rgw/zone HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/zone
:   **Example request:**

    ```http
    POST /api/rgw/zone HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_key": "string",
        "default": true,
        "master": true,
        "secret_key": "string",
        "zone_endpoints": "string",
        "zone_name": "string",
        "zonegroup_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/zone/create_system_user
:   **Example request:**

    ```http
    PUT /api/rgw/zone/create_system_user HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "userName": "string",
        "zoneName": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zone/get_all_zones_info
:   **Example request:**

    ```http
    GET /api/rgw/zone/get_all_zones_info HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zone/get_pool_names
:   **Example request:**

    ```http
    GET /api/rgw/zone/get_pool_names HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zone/get_user_list
:   Query Parameters:
    :   - **zoneName** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/zone/get_user_list HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/zone/{zone_name}
:   Parameters:
    :   - **zone_name** (*string*) --

    Query Parameters:
    :   - **delete_pools** (*string*) -- (Required)
        - **pools** (*string*) --
        - **zonegroup_name** (*string*) --
        - **realm_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zone/{zone_name}
:   Parameters:
    :   - **zone_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/zone/{zone_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/zone/{zone_name}
:   Parameters:
    :   - **zone_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/zone/{zone_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "access_key": "string",
        "compression": "string",
        "data_extra_pool": "string",
        "data_pool": "string",
        "data_pool_class": "string",
        "default": "string",
        "index_pool": "string",
        "master": "string",
        "new_zone_name": "string",
        "placement_target": "string",
        "secret_key": "string",
        "storage_class": "string",
        "zone_endpoints": "string",
        "zonegroup_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### RgwZonegroup

GET /api/rgw/zonegroup
:   **Example request:**

    ```http
    GET /api/rgw/zonegroup HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/rgw/zonegroup
:   **Example request:**

    ```http
    POST /api/rgw/zonegroup HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "default": "string",
        "master": "string",
        "realm_name": "string",
        "zonegroup_endpoints": "string",
        "zonegroup_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zonegroup/get_all_zonegroups_info
:   **Example request:**

    ```http
    GET /api/rgw/zonegroup/get_all_zonegroups_info HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/rgw/zonegroup/{zonegroup_name}
:   Parameters:
    :   - **zonegroup_name** (*string*) --

    Query Parameters:
    :   - **delete_pools** (*string*) -- (Required)
        - **pools** (*string*) --
        - **realm_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/rgw/zonegroup/{zonegroup_name}
:   Parameters:
    :   - **zonegroup_name** (*string*) --

    **Example request:**

    ```http
    GET /api/rgw/zonegroup/{zonegroup_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/rgw/zonegroup/{zonegroup_name}
:   Parameters:
    :   - **zonegroup_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/rgw/zonegroup/{zonegroup_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "add_zones": "string",
        "default": "string",
        "master": "string",
        "new_zonegroup_name": "string",
        "placement_targets": "string",
        "realm_name": "string",
        "remove_zones": "string",
        "zonegroup_endpoints": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Role

GET /api/role
:   **Display Role list**

    **Example request:**

    ```http
    GET /api/role HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/role
:   **Example request:**

    ```http
    POST /api/role HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "description": "string",
        "name": "string",
        "scopes_permissions": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/role/{name}
:   Parameters:
    :   - **name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/role/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    GET /api/role/{name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/role/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    PUT /api/role/{name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "description": "string",
        "scopes_permissions": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/role/{name}/clone
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    POST /api/role/{name}/clone HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "new_name": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Service

GET /api/service
:   Query Parameters:
    :   - **service_name** (*string*) --
        - **offset** (*integer*) --
        - **limit** (*integer*) --
        - **search** (*string*) --
        - **sort** (*string*) --

    **Example request:**

    ```http
    GET /api/service HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/service
:   > param service_spec:
    > :   The service specification as JSON.
    >
    > param service_name:
    > :   The service name, e.g. ‘alertmanager’.
    >
    > return:
    > :   None

    **Example request:**

    ```http
    POST /api/service HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "service_name": "string",
        "service_spec": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/service/known_types
:   > Get a list of known service types, e.g. ‘alertmanager’,
    > ‘node-exporter’, ‘osd’ or ‘rgw’.

    **Example request:**

    ```http
    GET /api/service/known_types HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/service/{service_name}
:   > param service_name:
    > :   The service name, e.g. ‘mds’ or ‘crash.foo’.
    >
    > return:
    > :   None

    Parameters:
    :   - **service_name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/service/{service_name}
:   Parameters:
    :   - **service_name** (*string*) --

    **Example request:**

    ```http
    GET /api/service/{service_name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/service/{service_name}
:   > param service_spec:
    > :   The service specification as JSON.
    >
    > param service_name:
    > :   The service name, e.g. ‘alertmanager’.
    >
    > return:
    > :   None

    Parameters:
    :   - **service_name** (*string*) --

    **Example request:**

    ```http
    PUT /api/service/{service_name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "service_spec": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/service/{service_name}/daemons
:   Parameters:
    :   - **service_name** (*string*) --

    **Example request:**

    ```http
    GET /api/service/{service_name}/daemons HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Settings

GET /api/settings
:   **Display Settings Information**

    > Get the list of available options.
    > :param names: A comma separated list of option names that should
    > be processed. Defaults to `None`.
    > :type names: None|str
    > :return: A list of available options.
    > :rtype: list[dict]

    Query Parameters:
    :   - **names** (*string*) -- Name of Settings

    **Example request:**

    ```http
    GET /api/settings HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/settings
:   Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/settings/{name}
:   Parameters:
    :   - **name** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/settings/{name}
:   > Get the given option.
    > :param name: The name of the option.
    > :return: Returns a dict containing the name, type,
    > default value and current value of the given option.
    > :rtype: dict

    Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    GET /api/settings/{name} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/settings/{name}
:   Parameters:
    :   - **name** (*string*) --

    **Example request:**

    ```http
    PUT /api/settings/{name} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "value": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Summary

GET /api/summary
:   **Display Summary**

    **Example request:**

    ```http
    GET /api/summary HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Task

GET /api/task
:   **Display Tasks**

    Query Parameters:
    :   - **name** (*string*) -- Task Name

    **Example request:**

    ```http
    GET /api/task HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### TcmuRunnerPerfCounter

GET /api/perf_counters/tcmu-runner/{service_id}
:   Parameters:
    :   - **service_id** (*string*) --

    **Example request:**

    ```http
    GET /api/perf_counters/tcmu-runner/{service_id} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Telemetry

PUT /api/telemetry
:   > Enables or disables sending data collected by the Telemetry
    > module.
    > :param enable: Enable or disable sending data
    > :type enable: bool
    > :param license_name: License string e.g. ‘sharing-1-0’ to
    > make sure the user is aware of and accepts the license
    > for sharing Telemetry data.
    > :type license_name: string

    **Example request:**

    ```http
    PUT /api/telemetry HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "enable": true,
        "license_name": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/telemetry/report
:   **Get Detailed Telemetry report**

    > Get Ceph and device report data
    > :return: Ceph and device report data
    > :rtype: dict

    **Example request:**

    ```http
    GET /api/telemetry/report HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### Upgrade

GET /api/cluster/upgrade
:   **Get the available versions to upgrade**

    Query Parameters:
    :   - **tags** (*boolean*) -- Show all image tags
        - **image** (*string*) -- Ceph Image
        - **show_all_versions** (*boolean*) -- Show all available versions

    **Example request:**

    ```http
    GET /api/cluster/upgrade HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster/upgrade/pause
:   **Pause the cluster upgrade**

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster/upgrade/resume
:   **Resume the cluster upgrade**

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/cluster/upgrade/start
:   **Start the cluster upgrade**

    **Example request:**

    ```http
    POST /api/cluster/upgrade/start HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "daemon_types": "string",
        "host_placement": "string",
        "image": "string",
        "limit": "string",
        "services": "string",
        "version": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/cluster/upgrade/status
:   **Get the cluster upgrade status**

    **Example request:**

    ```http
    GET /api/cluster/upgrade/status HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/cluster/upgrade/stop
:   **Stop the cluster upgrade**

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### User

GET /api/user
:   **Get List Of Users**

    **Example request:**

    ```http
    GET /api/user HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

POST /api/user
:   **Example request:**

    ```http
    POST /api/user HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "email": "string",
        "enabled": true,
        "name": "string",
        "password": "string",
        "pwdExpirationDate": "string",
        "pwdUpdateRequired": true,
        "roles": "string",
        "username": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

DELETE /api/user/{username}
:   Parameters:
    :   - **username** (*string*) --

    Status Codes:
    :   - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [204 No Content](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.5) -- Resource deleted.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

GET /api/user/{username}
:   Parameters:
    :   - **username** (*string*) --

    **Example request:**

    ```http
    GET /api/user/{username} HTTP/1.1
    Host: example.com
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- OK
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

PUT /api/user/{username}
:   Parameters:
    :   - **username** (*string*) --

    **Example request:**

    ```http
    PUT /api/user/{username} HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "email": "string",
        "enabled": "string",
        "name": "string",
        "password": "string",
        "pwdExpirationDate": "string",
        "pwdUpdateRequired": true,
        "roles": "string"
    }
    ```

    Status Codes:
    :   - [200 OK](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) -- Resource updated.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### UserChangePassword

POST /api/user/{username}/change_password
:   Parameters:
    :   - **username** (*string*) --

    **Example request:**

    ```http
    POST /api/user/{username}/change_password HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "new_password": "string",
        "old_password": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

### UserPasswordPolicy

POST /api/user/validate_password
:   > Check if the password meets the password policy.
    > :param password: The password to validate.
    > :param username: The name of the user (optional).
    > :param old_password: The old password (optional).
    > :return: An object with properties valid, credits and valuation.
    > ‘credits’ contains the password complexity credits and
    > ‘valuation’ the textual summary of the validation.

    **Example request:**

    ```http
    POST /api/user/validate_password HTTP/1.1
    Host: example.com
    Content-Type: application/json

    {
        "old_password": "string",
        "password": "string",
        "username": "string"
    }
    ```

    Status Codes:
    :   - [201 Created](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2) -- Resource created.
        - [202 Accepted](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.3) -- Operation is still executing. Please check the task queue.
        - [400 Bad Request](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) -- Operation exception. Please check the response body for details.
        - [401 Unauthorized](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) -- Unauthenticated access. Please login first.
        - [403 Forbidden](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) -- Unauthorized access. Please check your permissions.
        - [500 Internal Server Error](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) -- Unexpected error. Please check the response body for the stack trace.

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
