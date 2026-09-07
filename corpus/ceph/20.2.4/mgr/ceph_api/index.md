---
collection: ceph
version: "20.2.4"
title: "Ceph RESTful API"
source_url: https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/mgr/ceph_api/index.rst
fetched_at: 2026-08-18T01:32:45Z
---
<a id="mgr-ceph-api"></a>

# Ceph RESTful API

## Introduction
The **Ceph RESTful API** (henceforth **Ceph API**) is provided by the
[mgr-dashboard](../dashboard.md#mgr-dashboard) module. The Ceph API
service is available at the same URL as the regular Ceph Dashboard, under the
``/api`` base path (please refer to [dashboard-host-name-and-port](../dashboard.md#dashboard-host-name-and-port)):

```
http://<server_addr>:<server_port>/api
```

or, if HTTPS is enabled (please refer to [dashboard-ssl-tls-support](../dashboard.md#dashboard-ssl-tls-support)):

```
https://<server_addr>:<ssl_server_port>/api
```

The Ceph API leverages the following standards:

* [HTTP 1.1](https://tools.ietf.org/html/rfc7231) for API syntax and semantics,
* [JSON](https://tools.ietf.org/html/rfc8259) for content encoding,
* [HTTP Content Negotiation](https://tools.ietf.org/html/rfc2295) and [MIME](https://tools.ietf.org/html/rfc2045) for versioning,
* [OAuth 2.0](https://tools.ietf.org/html/rfc6750) and [JWT](https://tools.ietf.org/html/rfc7519) for authentication and authorization.

> **Warning:**
> Some endpoints are still under active development, and should be carefully
> used since new Ceph releases could bring backward incompatible changes.

## Authentication and Authorization

Requests to the Ceph API pass through two access control checkpoints:

* **Authentication**: ensures that the request is performed on behalf of an existing and valid user account.
* **Authorization**: ensures that the previously authenticated user can in fact perform a specific action (create, read, update or delete) on the target endpoint.

So, prior to start consuming the Ceph API, a valid JSON Web Token (JWT) has to
be obtained, and it may then be reused for subsequent requests. The
``/api/auth`` endpoint will provide the valid token:

```bash
curl -X POST "https://example.com:8443/api/auth" \
-H  "Accept: application/vnd.ceph.api.v1.0+json" \
-H  "Content-Type: application/json" \
-d '{"username": <username>, "password": <password>}'
```

:

```
{ "token": "<redacted_token>", ...}
```

The token obtained must be passed together with every API request in the
``Authorization`` HTTP header:

```bash
curl -H "Authorization: Bearer <token>" ...
```

Authentication and authorization can be further configured from the
Ceph CLI, the Ceph-Dashboard UI and the Ceph API itself (please refer to
[dashboard-user-role-management](../dashboard.md#dashboard-user-role-management)).

## Versioning

One of the main goals of the Ceph API is to keep a stable interface. For this
purpose, Ceph API is built upon the following principles:

* **Mandatory**: in order to avoid implicit defaults, all endpoints require an explicit default version (starting with ``1.0``).
* **Per-endpoint**: as this API wraps many different Ceph components, this allows for a finer-grained change control.
   * **Content/MIME Type**: the version expected from a specific endpoint is stated by the ``Accept: application/vnd.ceph.api.v<major>.<minor>+json`` HTTP header. If the current Ceph API server is not able to address that specific major version, a [415 - Unsupported Media Type](https://tools.ietf.org/html/rfc7231#section-6.5.13) response will be returned.
* **Semantic Versioning**: with a ``major.minor`` version:
   * Major changes are backward incompatible: they might result in non-additive changes to the request and/or response formats of a specific endpoint.
   * Minor changes are backward/forward compatible: they basically consists of additive changes to the request or response formats of a specific endpoint.

An example:

```bash
curl -X GET "https://example.com:8443/api/osd" \
-H  "Accept: application/vnd.ceph.api.v1.0+json" \
-H  "Authorization: Bearer <token>"
```

## Specification

.. openapi:: ../../../src/pybind/mgr/dashboard/openapi.yaml
   :group:
   :examples:
   :encoding: utf-8
