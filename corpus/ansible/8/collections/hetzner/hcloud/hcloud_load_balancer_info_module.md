---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_load_balancer_info module – Gather infos about your Hetzner Cloud Load Balancers."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_load_balancer_info_module.html
fetched_at: 2026-07-28T02:34:00+00:00
---
# hetzner.hcloud.hcloud_load_balancer_info module – Gather infos about your Hetzner Cloud Load Balancers.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_load_balancer_info_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-info-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer_info`.

- [Synopsis](hcloud_load_balancer_info_module.md#synopsis)
- [Requirements](hcloud_load_balancer_info_module.md#requirements)
- [Parameters](hcloud_load_balancer_info_module.md#parameters)
- [See Also](hcloud_load_balancer_info_module.md#see-also)
- [Examples](hcloud_load_balancer_info_module.md#examples)
- [Return Values](hcloud_load_balancer_info_module.md#return-values)

## [Synopsis](hcloud_load_balancer_info_module.md#id1)

- Gather infos about your Hetzner Cloud Load Balancers..

## [Requirements](hcloud_load_balancer_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_load_balancer_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Load Balancers you want to get. |
| **label_selector**  string | The label selector for the Load Balancers you want to get. |
| **name**  string | The name of the Load Balancers you want to get. |

## [See Also](hcloud_load_balancer_info_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_info_module.md#id5)

```yaml+jinja
- name: Gather hcloud load_balancer infos
  hcloud_load_balancer_info:
  register: output

- name: Print the gathered infos
  debug:
    var: output
```

## [Return Values](hcloud_load_balancer_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer_info**  complex | The load_balancer infos as list  **Returned:** always |
| **delete_protection**  boolean | True if Load Balancer is protected for deletion  **Returned:** always  **Sample:** `false` |
| **disable_public_interface**  boolean | True if Load Balancer public interface is disabled  **Returned:** always  **Sample:** `false` |
| **id**  integer | Numeric identifier of the Load Balancer  **Returned:** always  **Sample:** `1937415` |
| **ipv4_address**  string | Public IPv4 address of the Load Balancer  **Returned:** always  **Sample:** `"116.203.104.109"` |
| **ipv6_address**  string | Public IPv6 address of the Load Balancer  **Returned:** always  **Sample:** `"2a01:4f8:1c1c:c140::1"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always |
| **load_balancer_type**  string | Name of the Load Balancer type of the Load Balancer  **Returned:** always  **Sample:** `"cx11"` |
| **location**  string | Name of the location of the Load Balancer  **Returned:** always  **Sample:** `"fsn1"` |
| **name**  string | Name of the Load Balancer  **Returned:** always  **Sample:** `"my-Load-Balancer"` |
| **services**  complex | all services from this Load Balancer  **Returned:** Always |
| **destination_port**  integer | The port traffic is forwarded to, i.e. the port the targets are listening and accepting connections on.  **Returned:** always  **Sample:** `80` |
| **health_check**  complex | Configuration for health checks  **Returned:** always |
| **http**  complex | Additional Configuration of health checks with protocol http/https  **Returned:** always |
| **domain**  string | Domain we will set within the HTTP HOST header  **Returned:** always  **Sample:** `"example.com"` |
| **path**  string | Path we will try to access  **Returned:** always  **Sample:** `"/"` |
| **response**  string | Response we expect, if response is not within the health check response the target is unhealthy  **Returned:** always |
| **status_codes**  list / elements=string | List of HTTP status codes we expect to get when we perform the health check.  **Returned:** always  **Sample:** `["2??", "3??"]` |
| **tls**  boolean | Verify the TLS certificate, only available if health check protocol is https  **Returned:** always  **Sample:** `false` |
| **interval**  integer | Interval of health checks, in seconds  **Returned:** always  **Sample:** `15` |
| **port**  integer | Port the health check will be performed on  **Returned:** always  **Sample:** `80` |
| **protocol**  string | Protocol the health checks will be performed over  **Returned:** always  **Sample:** `"http"` |
| **retries**  integer | Number of retries until a target is marked as unhealthy  **Returned:** always  **Sample:** `3` |
| **timeout**  integer | Timeout of health checks, in seconds  **Returned:** always  **Sample:** `10` |
| **http**  complex | Configuration for HTTP and HTTPS services  **Returned:** always |
| **certificates**  list / elements=string | List of Names or IDs of certificates  **Returned:** always |
| **cookie_lifetime**  integer | Lifetime of the cookie which will be set when you enable sticky sessions, in seconds  **Returned:** always  **Sample:** `3600` |
| **cookie_name**  string | Name of the cookie which will be set when you enable sticky sessions  **Returned:** always  **Sample:** `"HCLBSTICKY"` |
| **redirect_http**  boolean | Redirect Traffic from Port 80 to Port 443, only available if protocol is https  **Returned:** always  **Sample:** `false` |
| **sticky_sessions**  boolean | Enable or disable sticky_sessions  **Returned:** always  **Sample:** `true` |
| **listen_port**  integer | The port the service listens on, i.e. the port users can connect to.  **Returned:** always  **Sample:** `443` |
| **protocol**  string | Protocol of the service  **Returned:** always  **Sample:** `"http"` |
| **proxyprotocol**  boolean | Enable the PROXY protocol.  **Returned:** always  **Sample:** `false` |
| **status**  string | Status of the Load Balancer  **Returned:** always  **Sample:** `"running"` |
| **targets**  complex | The targets of the Load Balancer  **Returned:** always |
| **ip**  string | IP of the dedicated server  **Returned:** if *type* is ip  **Sample:** `"127.0.0.1"` |
| **label_selector**  string | Label Selector  **Returned:** if *type* is label_selector  **Sample:** `"application=backend"` |
| **load_balancer**  string | Name of the Load Balancer  **Returned:** always  **Sample:** `"my-LoadBalancer"` |
| **server**  string | Name of the Server  **Returned:** if *type* is server  **Sample:** `"my-server"` |
| **type**  string | Type of the Load Balancer Target  **Returned:** always  **Sample:** `"server"` |
| **use_private_ip**  boolean | Route the traffic over the private IP of the Load Balancer through a Hetzner Cloud Network.  Load Balancer needs to be attached to a network. See hetzner.hcloud.hcloud.hcloud_load_balancer_network  **Returned:** always  **Sample:** `true` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
