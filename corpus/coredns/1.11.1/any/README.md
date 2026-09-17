---
collection: coredns
version: "1.11.1"
title: "any"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/any/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# any

## Name

*any* - gives a minimal response to ANY queries.

## Description

*any* basically blocks ANY queries by responding to them with a short HINFO reply. See [RFC
8482](https://tools.ietf.org/html/rfc8482) for details.

## Syntax

~~~ txt
any
~~~

## Examples

~~~ corefile
example.org {
    whoami
    any
}
~~~

A `dig +nocmd ANY example.org +noall +answer` now returns:

~~~ txt
example.org.  8482	IN	HINFO	"ANY obsoleted" "See RFC 8482"
~~~

## See Also

[RFC 8482](https://tools.ietf.org/html/rfc8482).
