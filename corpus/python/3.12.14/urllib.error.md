---
collection: python
version: "3.12.14"
title: "urllib.error — Exception classes raised by urllib.request"
source_url: https://docs.python.org/3.12/library/urllib.error.html
fetched_at: 2026-09-17T15:34:03+00:00
---
# `urllib.error` — Exception classes raised by urllib.request

**Source code:** [Lib/urllib/error.py](https://github.com/python/cpython/tree/3.12/Lib/urllib/error.py)

---

The [`urllib.error`](urllib.error.md#module-urllib.error "urllib.error: Exception classes raised by urllib.request.") module defines the exception classes for exceptions
raised by [`urllib.request`](urllib.request.md#module-urllib.request "urllib.request: Extensible library for opening URLs."). The base exception class is [`URLError`](urllib.error.md#urllib.error.URLError "urllib.error.URLError").

The following exceptions are raised by [`urllib.error`](urllib.error.md#module-urllib.error "urllib.error: Exception classes raised by urllib.request.") as appropriate:

`exception urllib.error.URLError`
:   The handlers raise this exception (or derived exceptions) when they run into
    a problem. It is a subclass of [`OSError`](exceptions.md#OSError "OSError").

    `reason`
    :   The reason for this error. It can be a message string or another
        exception instance.

    Changed in version 3.3: [`URLError`](urllib.error.md#urllib.error.URLError "urllib.error.URLError") used to be a subtype of [`IOError`](exceptions.md#IOError "IOError"), which is now an
    alias of [`OSError`](exceptions.md#OSError "OSError").

`exception urllib.error.HTTPError(url, code, msg, hdrs, fp)`
:   Though being an exception (a subclass of [`URLError`](urllib.error.md#urllib.error.URLError "urllib.error.URLError")), an
    [`HTTPError`](urllib.error.md#urllib.error.HTTPError "urllib.error.HTTPError") can also function as a non-exceptional file-like return
    value (the same thing that [`urlopen()`](urllib.request.md#urllib.request.urlopen "urllib.request.urlopen") returns). This
    is useful when handling exotic HTTP errors, such as requests for
    authentication.

    `url`
    :   Contains the request URL.
        An alias for *filename* attribute.

    `code`
    :   An HTTP status code as defined in [**RFC 2616**](https://datatracker.ietf.org/doc/html/rfc2616.html). This numeric value corresponds
        to a value found in the dictionary of codes as found in
        [`http.server.BaseHTTPRequestHandler.responses`](http.server.md#http.server.BaseHTTPRequestHandler.responses "http.server.BaseHTTPRequestHandler.responses").

    `reason`
    :   This is usually a string explaining the reason for this error.
        An alias for *msg* attribute.

    `headers`
    :   The HTTP response headers for the HTTP request that caused the
        [`HTTPError`](urllib.error.md#urllib.error.HTTPError "urllib.error.HTTPError").
        An alias for *hdrs* attribute.

        Added in version 3.4.

    `fp`
    :   A file-like object where the HTTP error body can be read from.

`exception urllib.error.ContentTooShortError(msg, content)`
:   This exception is raised when the [`urlretrieve()`](urllib.request.md#urllib.request.urlretrieve "urllib.request.urlretrieve")
    function detects that
    the amount of the downloaded data is less than the expected amount (given by
    the *Content-Length* header).

    `content`
    :   The downloaded (and supposedly truncated) data.
