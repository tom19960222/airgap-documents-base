---
collection: coredns
version: "1.11.1"
title: "minimal"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/minimal/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# minimal

## Name

*minimal* - minimizes size of the DNS response message whenever possible.

## Description

The *minimal* plugin tries to minimize the size of the response. Depending on the response type it
removes resource records from the AUTHORITY and ADDITIONAL sections.

Specifically this plugin looks at successful responses (this excludes negative responses, i.e.
nodata or name error). If the successful response isn't a delegation only the RRs in the answer
section are written to the client.

## Syntax

~~~ txt
minimal
~~~

## Examples

Enable minimal responses:

~~~ corefile
example.org {
    whoami
    forward . 8.8.8.8
    minimal
}
~~~

## See Also

[BIND 9 Configuration Reference](https://bind9.readthedocs.io/en/latest/reference.html#boolean-options)
