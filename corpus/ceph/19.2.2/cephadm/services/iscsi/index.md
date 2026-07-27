---
collection: ceph
version: "19.2.2"
title: "iSCSI Service"
source_url: https://docs.ceph.com/en/squid/cephadm/services/iscsi/
fetched_at: 2026-07-27T16:39:23+00:00
---
# iSCSI Service

## Deploying iSCSI

To deploy an iSCSI gateway, create a yaml file containing a
service specification for iscsi:

```yaml
service_type: iscsi
service_id: iscsi
placement:
  hosts:
    - host1
    - host2
spec:
  pool: mypool  # RADOS pool where ceph-iscsi config data is stored.
  trusted_ip_list: "IP_ADDRESS_1,IP_ADDRESS_2"
  api_port: ... # optional
  api_user: ... # optional
  api_password: ... # optional
  api_secure: true/false # optional
  ssl_cert: | # optional
    ...
  ssl_key: | # optional
    ...
```

For example:

```yaml
service_type: iscsi
service_id: iscsi
placement:
  hosts:
  - [...]
spec:
  pool: iscsi_pool
  trusted_ip_list: "IP_ADDRESS_1,IP_ADDRESS_2,IP_ADDRESS_3,..."
  api_user: API_USERNAME
  api_password: API_PASSWORD
  ssl_cert: |
    -----BEGIN CERTIFICATE-----
    MIIDtTCCAp2gAwIBAgIYMC4xNzc1NDQxNjEzMzc2MjMyXzxvQ7EcMA0GCSqGSIb3
    DQEBCwUAMG0xCzAJBgNVBAYTAlVTMQ0wCwYDVQQIDARVdGFoMRcwFQYDVQQHDA5T
    [...]
    -----END CERTIFICATE-----
  ssl_key: |
    -----BEGIN PRIVATE KEY-----
    MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC5jdYbjtNTAKW4
    /CwQr/7wOiLGzVxChn3mmCIF3DwbL/qvTFTX2d8bDf6LjGwLYloXHscRfxszX/4h
    [...]
    -----END PRIVATE KEY-----
```

*class* ceph.deployment.service_spec.IscsiServiceSpec(*service_type='iscsi'*, *service_id=None*, *pool=None*, *trusted_ip_list=None*, *api_port=5000*, *api_user='admin'*, *api_password='admin'*, *api_secure=None*, *ssl_cert=None*, *ssl_key=None*, *placement=None*, *unmanaged=False*, *preview_only=False*, *config=None*, *networks=None*, *extra_container_args=None*, *extra_entrypoint_args=None*, *custom_configs=None*)
:   api_password
    :   `api_password` as defined in the `iscsi-gateway.cfg`

    api_port
    :   `api_port` as defined in the `iscsi-gateway.cfg`

    api_secure
    :   `api_secure` as defined in the `iscsi-gateway.cfg`

    api_user
    :   `api_user` as defined in the `iscsi-gateway.cfg`

    networks*: List[str]*
    :   A list of network identities instructing the daemons to only bind
        on the particular networks in that list. In case the cluster is distributed
        across multiple networks, you can add multiple networks. See
        [Networks and Ports](../monitoring/index.md#cephadm-monitoring-networks-ports),
        [Specifying Networks](../rgw/index.md#cephadm-rgw-networks) and [Specifying Networks](../mgr/index.md#cephadm-mgr-networks).

    placement*: [PlacementSpec](../../../mgr/orchestrator_modules/index.md#ceph.deployment.service_spec.PlacementSpec "ceph.deployment.service_spec.PlacementSpec")*
    :   See [Daemon Placement](../index.md#orchestrator-cli-placement-spec).

    pool
    :   RADOS pool where ceph-iscsi config data is stored.

    ssl_cert
    :   SSL certificate

    ssl_key
    :   SSL private key

    trusted_ip_list
    :   list of trusted IP addresses

The specification can then be applied using:

```
ceph orch apply -i iscsi.yaml
```

See [Daemon Placement](../index.md#orchestrator-cli-placement-spec) for details of the placement specification.

See also: [Service Specification](../index.md#orchestrator-cli-service-spec).

## Configuring iSCSI client

The containerized iscsi service can be used from any host by
[Configuring the iSCSI Initiators](../../../rbd/iscsi-initiators/index.md#configuring-the-iscsi-initiators), which will use TCP/IP to send SCSI
commands to the iSCSI target (gateway).

## Further Reading

- Ceph iSCSI Overview: [Ceph iSCSI Gateway](../../../rbd/iscsi-overview/index.md#ceph-iscsi)

> **Brought to you by the Ceph Foundation:**
>
> The Ceph Documentation is a community resource funded and hosted by the non-profit [Ceph Foundation](https://ceph.io/en/foundation/). If you would like to support this and our other efforts, please consider [joining now](https://ceph.io/en/foundation/join/).
