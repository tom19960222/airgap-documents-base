---
collection: ansible
version: "8"
title: "netapp.storagegrid.na_sg_grid_gateway module – Manage Load balancer (gateway) endpoints on StorageGRID."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/storagegrid/na_sg_grid_gateway_module.html
fetched_at: 2026-07-28T02:43:49+00:00
---
# netapp.storagegrid.na_sg_grid_gateway module – Manage Load balancer (gateway) endpoints on StorageGRID.

> **Note:**
>
> This module is part of the [netapp.storagegrid collection](https://galaxy.ansible.com/ui/repo/published/netapp/storagegrid/) (version 21.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.storagegrid`.
>
> To use it in a playbook, specify: `netapp.storagegrid.na_sg_grid_gateway`.

New in netapp.storagegrid 21.7.0

- [Synopsis](na_sg_grid_gateway_module.md#synopsis)
- [Parameters](na_sg_grid_gateway_module.md#parameters)
- [Notes](na_sg_grid_gateway_module.md#notes)
- [Examples](na_sg_grid_gateway_module.md#examples)
- [Return Values](na_sg_grid_gateway_module.md#return-values)

## [Synopsis](na_sg_grid_gateway_module.md#id1)

- Create or Update Load Balancer Endpoints on StorageGRID.
- This module is idempotent if *private_key* is not specified.
- The module will match an existing config based on *port* and *display_name*.
- If multiple load balancer endpoints exist utilizing the same port and display name, use *gateway_id* to select the intended endpoint.

## [Parameters](na_sg_grid_gateway_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string / required | The url to the StorageGRID Admin Node REST API. |
| **auth_token**  string / required | The authorization token for the API request |
| **binding_mode**  string  *added in netapp.storagegrid 21.9.0* | Binding mode to restrict accessibility of the load balancer endpoint.  A binding mode other than *global* requires StorageGRID 11.5 or greater.  **Choices:**   - `"global"` ← (default) - `"ha-groups"` - `"node-interfaces"` |
| **ca_bundle**  string | Intermediate CA certificate bundle in concatenated PEM-encoding.  Omit when there is no intermediate CA. |
| **default_service_type**  string | The type of service to proxy through the load balancer.  **Choices:**   - `"s3"` ← (default) - `"swift"` |
| **display_name**  string | A display name for the configuration.  This parameter can be modified if *gateway_id* is also specified. |
| **enable_ipv4**  boolean | Indicates whether to listen for connections on IPv4.  **Choices:**   - `false` - `true` ← (default) |
| **enable_ipv6**  boolean | Indicates whether to listen for connections on IPv6.  **Choices:**   - `false` - `true` ← (default) |
| **gateway_id**  string  *added in netapp.storagegrid 21.9.0* | ID of the load balancer endpoint. |
| **ha_groups**  list / elements=string  *added in netapp.storagegrid 21.9.0* | A set of StorageGRID HA Groups by name or UUID to bind the load balancer endpoint to.  Option is ignored unless *binding_mode=ha-groups*. |
| **node_interfaces**  list / elements=dictionary  *added in netapp.storagegrid 21.9.0* | A set of StorageGRID node interfaces to bind the load balancer endpoint to. |
| **interface**  string | The interface to bind to. eth0 corresponds to the Grid Network, eth1 to the Admin Network, and eth2 to the Client Network. |
| **node**  string | Name of the StorageGRID node. |
| **port**  integer / required | The TCP port to serve traffic on.  This parameter cannot be modified after the load balancer endpoint has been created. |
| **private_key**  string | Certficate private key in PEM-encoding.  Required if *server_certificate* is not empty. |
| **secure**  boolean | Whether the load balancer endpoint serves HTTP or HTTPS traffic.  This parameter cannot be modified after the load balancer endpoint has been created.  **Choices:**   - `false` - `true` ← (default) |
| **server_certificate**  string | X.509 server certificate in PEM-encoding.  Omit if using default certificates. |
| **state**  string | Whether the specified load balancer endpoint should be configured.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_sg_grid_gateway_module.md#id3)

> **Note:**
>
> - The modules prefixed with `na_sg` are built to manage NetApp StorageGRID.

## [Examples](na_sg_grid_gateway_module.md#id4)

```yaml+jinja
- name: Create and Upload Certificate to a Gateway Endpoint with global binding
  netapp.storagegrid.na_sg_grid_gateway:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    displayName: "FabricPool Endpoint"
    port: 10443
    secure: True
    enable_ipv4: True
    enable_ipv6: True
    default_service_type: "s3"
    server_certificate: |
      -----BEGIN CERTIFICATE-----
      MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2..swCQYDVQQGEwJB
      BAMMHnNnYW4wMS5kZXYubWljcm9icmV3Lm5ldGFwcC5hdTCC..IwDQYJKoZIhvcN
      AQEBBQADggEPADCCAQoCggEBAMvjm9I35lmKcC7ITVL8+QiZ..lvdkbfZCUQrfdy
      71inP+XmPjs0rnkhICA9ItODteRcVlO+t7nDTfm7HgG0mJFk..m0ffyEYrcx24qu
      S7gXYQjRsJmrep1awoaCa20BMGuqK2WKI3IvZ7YiT22qkBqK..+hIFffX6u3Jy+B
      77pR6YcATtpMHW/AaOx+OX9l80dIRsRZKMDxYQ==
      -----END CERTIFICATE-----
    private_key: |
      -----BEGIN PRIVATE KEY-----
      MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIB..DL45vSN+ZZinAu
      L25W0+cz1Oi69AKkI7d9nbFics2ay5+7o+4rKqf3en2R4MSx..vy+iDlOmATib5O
      x8TN5pJ9AgMBAAECggEADDLM8tHXXUoUFihzv+BUwff8p8Yc..cXFcSes+xTd5li
      po8lNsx/v2pQx4ByBkuaYLZGIEXOWS6gkp44xhIXgQKBgQD4..7862u5HLbmhrV3
      vs8nC69b3QKBgQDacCD8d8JpwPbg8t2VjXM3UvdmgAaLUfU7..DWV+W3jqzmDOoN
      zWVgPbPNj0UmzvLDbgxLoxe77wjn2BHsAJVAfJ9VeQKBgGqF..gYO+wHR8lJUoa5
      ZEe8Upy2oBtvND/0dnwO2ym2FGsBJN0Gr4NKdG5vkzLsthKk..Rm0ikwEUOUZQKE
      K8J5yEVeo9K2v3wggtq8fYn6
      -----END PRIVATE KEY-----
    validate_certs: false

- name: Create a HTTP Gateway Endpoint with HA Group Binding
  netapp.storagegrid.na_sg_grid_gateway:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    displayName: "App Endpoint 1"
    port: 10501
    secure: false
    enable_ipv4: True
    enable_ipv6: True
    default_service_type: "s3"
    binding_mode: ha-groups
    ha_groups: site1_ha_group
    validate_certs: false

- name: Create a HTTP Gateway Endpoint with Node Interface Binding
  netapp.storagegrid.na_sg_grid_gateway:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    displayName: "App Endpoint 2"
    port: 10502
    secure: false
    enable_ipv4: True
    enable_ipv6: True
    default_service_type: "s3"
    binding_mode: node-interfaces
    node_interfaecs:
    - node: SITE1_ADM1
      interface: eth2
    - node: SITE2_ADM1
      interface: eth2
    validate_certs: false

- name: Delete Gateway Endpoint
  netapp.storagegrid.na_sg_grid_gateway:
    api_url: "https://<storagegrid-endpoint-url>"
    auth_token: "storagegrid-auth-token"
    displayName: "App Endpoint 2"
    port: 10502
    default_service_type: "s3"
    validate_certs: false
```

## [Return Values](na_sg_grid_gateway_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **resp**  dictionary | Returns information about the StorageGRID Load Balancer Endpoint.  **Returned:** success  **Sample:** `{"accountId": "0", "certSource": "plaintext", "defaultServiceType": "s3", "displayName": "ansibletest-secure", "enableIPv4": true, "enableIPv6": true, "id": "ffffffff-ffff-ffff-ffff-ffffffffffff", "plaintextCertData": {"caBundleEncoded": "-----BEGIN CERTIFICATE-----MIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELM...-----END CERTIFICATE-----", "metadata": {"...": null}, "serverCertificateEncoded": "-----BEGIN CERTIFICATE-----MIIC6DCCAdACCQC7l4WukhKD0zANBgkqhkiG9w0BAQsFADA2MQswCQYDVQQGE...-----END CERTIFICATE-----"}, "port": 10443, "secure": true}` |

### Authors

- NetApp Ansible Team (@jkandati)

### Collection links

- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.storagegrid)
