---
collection: coredns
version: "1.11.1"
title: "root"
source_url: https://github.com/coredns/coredns/blob/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144/plugin/root/README.md
fetched_at: 2023-08-15T15:30:32-04:00
---
# root

## Name

*root* - simply specifies the root of where to find (zone) files.

## Description

The default root is the current working directory of CoreDNS. The *root* plugin allows you to change
this. A relative root path is relative to the current working directory.

This plugin can only be used once per Server Block.

## Syntax

~~~ txt
root PATH
~~~

**PATH** is the directory to set as CoreDNS' root.

## Examples

Serve zone data (when the *file* plugin is used) from `/etc/coredns/zones`:

~~~ corefile
. {
    root /etc/coredns/zones
}
~~~
