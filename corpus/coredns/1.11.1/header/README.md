---
collection: coredns
version: "1.11.1"
title: "header"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/header/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# header

## Name

*header* - modifies the header for queries and responses.

## Description

*header* ensures that the flags are in the desired state for queries and responses.
The modifications are made transparently for the client and subsequent plugins.

## Syntax

~~~
header {
    [SELECTOR] ACTION FLAGS...
    [SELECTOR] ACTION FLAGS...
}
~~~

* **SELECTOR** defines if the action should be applied on `query` or `response`. In future CoreDNS version the selector will be mandatory. For backwards compatibility the action will be applied on `response` if the selector is undefined.

* **ACTION** defines the state for DNS message header flags. Actions are evaluated in the order they are defined so last one has the
  most precedence. Allowed values are:
    * `set`
    * `clear`
* **FLAGS** are the DNS header flags that will be modified. Current supported flags include:
    * `aa` - Authoritative(Answer)
    * `ra` - RecursionAvailable
    * `rd` - RecursionDesired

## Examples

Make sure recursive available `ra` flag is set in all the responses:

~~~ corefile
. {
    header {
        response set ra
    }
}
~~~

Make sure "recursion available" `ra` and "authoritative answer" `aa` flags are set and "recursion desired" is cleared in all responses:

~~~ corefile
. {
    header {
        response set ra aa
        response clear rd
    }
}
~~~

Make sure "recursion desired" `rd` is set for all subsequent plugins::

~~~ corefile
. {
    header {
        query set rd
    }
}
~~~
