---
collection: python
version: "3.10.21"
title: "http — HTTP modules"
source_url: https://docs.python.org/3.10/library/http.html
fetched_at: 2026-09-17T15:14:29+00:00
---
# `http` — HTTP modules

**Source code:** [Lib/http/__init__.py](https://github.com/python/cpython/tree/3.10/Lib/http/__init__.py)

---

[`http`](http.md#module-http "http: HTTP status codes and messages") is a package that collects several modules for working with the
HyperText Transfer Protocol:

- [`http.client`](http.client.md#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") is a low-level HTTP protocol client; for high-level URL
  opening use [`urllib.request`](urllib.request.md#module-urllib.request "urllib.request: Extensible library for opening URLs.")
- [`http.server`](http.server.md#module-http.server "http.server: HTTP server and request handlers.") contains basic HTTP server classes based on [`socketserver`](socketserver.md#module-socketserver "socketserver: A framework for network servers.")
- [`http.cookies`](http.cookies.md#module-http.cookies "http.cookies: Support for HTTP state management (cookies).") has utilities for implementing state management with cookies
- [`http.cookiejar`](http.cookiejar.md#module-http.cookiejar "http.cookiejar: Classes for automatic handling of HTTP cookies.") provides persistence of cookies

[`http`](http.md#module-http "http: HTTP status codes and messages") is also a module that defines a number of HTTP status codes and
associated messages through the [`http.HTTPStatus`](http.md#http.HTTPStatus "http.HTTPStatus") enum:

`class http.HTTPStatus`
:   New in version 3.5.

    A subclass of [`enum.IntEnum`](enum.md#enum.IntEnum "enum.IntEnum") that defines a set of HTTP status codes,
    reason phrases and long descriptions written in English.

    Usage:

    ```python3
    >>> from http import HTTPStatus
    >>> HTTPStatus.OK
    <HTTPStatus.OK: 200>
    >>> HTTPStatus.OK == 200
    True
    >>> HTTPStatus.OK.value
    200
    >>> HTTPStatus.OK.phrase
    'OK'
    >>> HTTPStatus.OK.description
    'Request fulfilled, document follows'
    >>> list(HTTPStatus)
    [<HTTPStatus.CONTINUE: 100>, <HTTPStatus.SWITCHING_PROTOCOLS:101>, ...]
    ```

## HTTP status codes

Supported,
[IANA-registered](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml)
status codes available in [`http.HTTPStatus`](http.md#http.HTTPStatus "http.HTTPStatus") are:

| Code | Enum Name | Details |
| --- | --- | --- |
| `100` | `CONTINUE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.2.1 |
| `101` | `SWITCHING_PROTOCOLS` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.2.2 |
| `102` | `PROCESSING` | WebDAV [**RFC 2518**](https://datatracker.ietf.org/doc/html/rfc2518.html), Section 10.1 |
| `103` | `EARLY_HINTS` | An HTTP Status Code for Indicating Hints [**RFC 8297**](https://datatracker.ietf.org/doc/html/rfc8297.html) |
| `200` | `OK` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.1 |
| `201` | `CREATED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.2 |
| `202` | `ACCEPTED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.3 |
| `203` | `NON_AUTHORITATIVE_INFORMATION` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.4 |
| `204` | `NO_CONTENT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.5 |
| `205` | `RESET_CONTENT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.3.6 |
| `206` | `PARTIAL_CONTENT` | HTTP/1.1 [**RFC 7233**](https://datatracker.ietf.org/doc/html/rfc7233.html), Section 4.1 |
| `207` | `MULTI_STATUS` | WebDAV [**RFC 4918**](https://datatracker.ietf.org/doc/html/rfc4918.html), Section 11.1 |
| `208` | `ALREADY_REPORTED` | WebDAV Binding Extensions [**RFC 5842**](https://datatracker.ietf.org/doc/html/rfc5842.html), Section 7.1 (Experimental) |
| `226` | `IM_USED` | Delta Encoding in HTTP [**RFC 3229**](https://datatracker.ietf.org/doc/html/rfc3229.html), Section 10.4.1 |
| `300` | `MULTIPLE_CHOICES` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.1 |
| `301` | `MOVED_PERMANENTLY` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.2 |
| `302` | `FOUND` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.3 |
| `303` | `SEE_OTHER` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.4 |
| `304` | `NOT_MODIFIED` | HTTP/1.1 [**RFC 7232**](https://datatracker.ietf.org/doc/html/rfc7232.html), Section 4.1 |
| `305` | `USE_PROXY` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.5 |
| `307` | `TEMPORARY_REDIRECT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.4.7 |
| `308` | `PERMANENT_REDIRECT` | Permanent Redirect [**RFC 7238**](https://datatracker.ietf.org/doc/html/rfc7238.html), Section 3 (Experimental) |
| `400` | `BAD_REQUEST` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.1 |
| `401` | `UNAUTHORIZED` | HTTP/1.1 Authentication [**RFC 7235**](https://datatracker.ietf.org/doc/html/rfc7235.html), Section 3.1 |
| `402` | `PAYMENT_REQUIRED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.2 |
| `403` | `FORBIDDEN` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.3 |
| `404` | `NOT_FOUND` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.4 |
| `405` | `METHOD_NOT_ALLOWED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.5 |
| `406` | `NOT_ACCEPTABLE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.6 |
| `407` | `PROXY_AUTHENTICATION_REQUIRED` | HTTP/1.1 Authentication [**RFC 7235**](https://datatracker.ietf.org/doc/html/rfc7235.html), Section 3.2 |
| `408` | `REQUEST_TIMEOUT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.7 |
| `409` | `CONFLICT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.8 |
| `410` | `GONE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.9 |
| `411` | `LENGTH_REQUIRED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.10 |
| `412` | `PRECONDITION_FAILED` | HTTP/1.1 [**RFC 7232**](https://datatracker.ietf.org/doc/html/rfc7232.html), Section 4.2 |
| `413` | `REQUEST_ENTITY_TOO_LARGE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.11 |
| `414` | `REQUEST_URI_TOO_LONG` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.12 |
| `415` | `UNSUPPORTED_MEDIA_TYPE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.13 |
| `416` | `REQUESTED_RANGE_NOT_SATISFIABLE` | HTTP/1.1 Range Requests [**RFC 7233**](https://datatracker.ietf.org/doc/html/rfc7233.html), Section 4.4 |
| `417` | `EXPECTATION_FAILED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.14 |
| `418` | `IM_A_TEAPOT` | HTCPCP/1.0 [**RFC 2324**](https://datatracker.ietf.org/doc/html/rfc2324.html), Section 2.3.2 |
| `421` | `MISDIRECTED_REQUEST` | HTTP/2 [**RFC 7540**](https://datatracker.ietf.org/doc/html/rfc7540.html), Section 9.1.2 |
| `422` | `UNPROCESSABLE_ENTITY` | WebDAV [**RFC 4918**](https://datatracker.ietf.org/doc/html/rfc4918.html), Section 11.2 |
| `423` | `LOCKED` | WebDAV [**RFC 4918**](https://datatracker.ietf.org/doc/html/rfc4918.html), Section 11.3 |
| `424` | `FAILED_DEPENDENCY` | WebDAV [**RFC 4918**](https://datatracker.ietf.org/doc/html/rfc4918.html), Section 11.4 |
| `425` | `TOO_EARLY` | Using Early Data in HTTP [**RFC 8470**](https://datatracker.ietf.org/doc/html/rfc8470.html) |
| `426` | `UPGRADE_REQUIRED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.5.15 |
| `428` | `PRECONDITION_REQUIRED` | Additional HTTP Status Codes [**RFC 6585**](https://datatracker.ietf.org/doc/html/rfc6585.html) |
| `429` | `TOO_MANY_REQUESTS` | Additional HTTP Status Codes [**RFC 6585**](https://datatracker.ietf.org/doc/html/rfc6585.html) |
| `431` | `REQUEST_HEADER_FIELDS_TOO_LARGE` | Additional HTTP Status Codes [**RFC 6585**](https://datatracker.ietf.org/doc/html/rfc6585.html) |
| `451` | `UNAVAILABLE_FOR_LEGAL_REASONS` | An HTTP Status Code to Report Legal Obstacles [**RFC 7725**](https://datatracker.ietf.org/doc/html/rfc7725.html) |
| `500` | `INTERNAL_SERVER_ERROR` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.1 |
| `501` | `NOT_IMPLEMENTED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.2 |
| `502` | `BAD_GATEWAY` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.3 |
| `503` | `SERVICE_UNAVAILABLE` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.4 |
| `504` | `GATEWAY_TIMEOUT` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.5 |
| `505` | `HTTP_VERSION_NOT_SUPPORTED` | HTTP/1.1 [**RFC 7231**](https://datatracker.ietf.org/doc/html/rfc7231.html), Section 6.6.6 |
| `506` | `VARIANT_ALSO_NEGOTIATES` | Transparent Content Negotiation in HTTP [**RFC 2295**](https://datatracker.ietf.org/doc/html/rfc2295.html), Section 8.1 (Experimental) |
| `507` | `INSUFFICIENT_STORAGE` | WebDAV [**RFC 4918**](https://datatracker.ietf.org/doc/html/rfc4918.html), Section 11.5 |
| `508` | `LOOP_DETECTED` | WebDAV Binding Extensions [**RFC 5842**](https://datatracker.ietf.org/doc/html/rfc5842.html), Section 7.2 (Experimental) |
| `510` | `NOT_EXTENDED` | An HTTP Extension Framework [**RFC 2774**](https://datatracker.ietf.org/doc/html/rfc2774.html), Section 7 (Experimental) |
| `511` | `NETWORK_AUTHENTICATION_REQUIRED` | Additional HTTP Status Codes [**RFC 6585**](https://datatracker.ietf.org/doc/html/rfc6585.html), Section 6 |

In order to preserve backwards compatibility, enum values are also present
in the [`http.client`](http.client.md#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") module in the form of constants. The enum name is
equal to the constant name (i.e. `http.HTTPStatus.OK` is also available as
`http.client.OK`).

Changed in version 3.7: Added `421 MISDIRECTED_REQUEST` status code.

New in version 3.8: Added `451 UNAVAILABLE_FOR_LEGAL_REASONS` status code.

New in version 3.9: Added `103 EARLY_HINTS`, `418 IM_A_TEAPOT` and `425 TOO_EARLY` status codes.
