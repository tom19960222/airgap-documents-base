---
collection: cilium
version: "1.16.7"
title: "Key-Value Store"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/cmdref/kvstore.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="install_kvstore"></a>

# Key-Value Store

| Option | Description | Default |
| --- | --- | --- |
| --kvstore TYPE <br> | Key Value Store Type: <br> (consul, etcd) | <br> |
| --kvstore-opt OPTS |  |  |

## etcd

When using etcd, one of the following options need to be provided to configure the
etcd endpoints:

| Option | Type | Description |
| --- | --- | --- |
| etcd.address | Address | Address of etcd endpoint |
| etcd.config | Path | Path to an etcd configuration file. |

Example of the etcd configuration file:

```yaml
---
endpoints:
- https://192.168.0.1:2379
- https://192.168.0.2:2379
trusted-ca-file: '/var/lib/cilium/etcd-ca.pem'
# In case you want client to server authentication
key-file: '/var/lib/cilium/etcd-client.key'
cert-file: '/var/lib/cilium/etcd-client.crt'
```
