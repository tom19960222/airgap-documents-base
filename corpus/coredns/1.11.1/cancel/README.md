---
collection: coredns
version: "1.11.1"
title: "cancel"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/cancel/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# cancel

## Name

*cancel* - cancels a request's context after 5001 milliseconds.

## Description

The *cancel* plugin creates a canceling context for each request. It adds a timeout that gets
triggered after 5001 milliseconds.

The 5001 number was chosen because the default timeout for DNS clients is 5 seconds, after that they
give up.

A plugin interested in the cancellation status should call `plugin.Done()` on the context. If the
context was canceled due to a timeout the plugin should not write anything back to the client and
return a value indicating CoreDNS should not either; a zero return value should suffice for that.

## Syntax

~~~ txt
cancel [TIMEOUT]
~~~

* **TIMEOUT** allows setting a custom timeout. The default timeout is 5001 milliseconds (`5001 ms`)

## Examples

~~~ corefile
example.org {
    cancel
    whoami
}
~~~

Or with a custom timeout:

~~~ corefile
example.org {
    cancel 1s
    whoami
}
~~~

## See Also

The Go documentation for the context package.
