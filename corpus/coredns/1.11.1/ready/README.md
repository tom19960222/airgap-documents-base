---
collection: coredns
version: "1.11.1"
title: "ready"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/ready/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# ready

## Name

*ready* - enables a readiness check HTTP endpoint.

## Description

By enabling *ready* an HTTP endpoint on port 8181 will return 200 OK, when all plugins that are able
to signal readiness have done so. If some are not ready yet the endpoint will return a 503 with the
body containing the list of plugins that are not ready. Once a plugin has signaled it is ready it
will not be queried again.

Each Server Block that enables the *ready* plugin will have the plugins *in that server block*
report readiness into the /ready endpoint that runs on the same port. This also means that the
*same* plugin with different configurations (in potentially *different* Server Blocks) will have
their readiness reported as the union of their respective readinesses.

## Syntax

~~~
ready [ADDRESS]
~~~

*ready* optionally takes an address; the default is `:8181`. The path is fixed to `/ready`. The
readiness endpoint returns a 200 response code and the word "OK" when this server is ready. It
returns a 503 otherwise *and* the list of plugins that are not ready.

## Plugins

Any plugin wanting to signal readiness will need to implement the `ready.Readiness` interface by
implementing a method `Ready() bool` that returns true when the plugin is ready and false otherwise.

## Examples

Let *ready* report readiness for both the `.` and `example.org` servers (assuming the *whois*
plugin also exports readiness):

~~~ txt
. {
    ready
    erratic
}

example.org {
    ready
    whoami
}

~~~

Run *ready* on a different port.

~~~ txt
. {
    ready localhost:8091
}
~~~
