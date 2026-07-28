---
collection: ansible
version: "8"
title: "community.digitalocean.digital_ocean_load_balancer module – Manage DigitalOcean Load Balancers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/digitalocean/digital_ocean_load_balancer_module.html
fetched_at: 2026-07-28T01:43:06+00:00
---
# community.digitalocean.digital_ocean_load_balancer module – Manage DigitalOcean Load Balancers

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/ui/repo/published/community/digitalocean/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_load_balancer`.

New in community.digitalocean 1.10.0

- [Synopsis](digital_ocean_load_balancer_module.md#synopsis)
- [Parameters](digital_ocean_load_balancer_module.md#parameters)
- [Examples](digital_ocean_load_balancer_module.md#examples)
- [Return Values](digital_ocean_load_balancer_module.md#return-values)

## [Synopsis](digital_ocean_load_balancer_module.md#id1)

- Manage DigitalOcean Load Balancers

## [Parameters](digital_ocean_load_balancer_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  **Default:** `"https://api.digitalocean.com/v2"` |
| **droplet_ids**  list / elements=integer | An array containing the IDs of the Droplets assigned to the load balancer.  Required when creating load balancers.  Mutually exclusive with tag, you can either define tag or droplet_ids but not both. |
| **enable_backend_keepalive**  boolean | A boolean value indicating whether HTTP keepalive connections are maintained to target Droplets.  **Choices:**   - `false` ← (default) - `true` |
| **enable_proxy_protocol**  boolean | A boolean value indicating whether PROXY Protocol is in use.  **Choices:**   - `false` ← (default) - `true` |
| **forwarding_rules**  list / elements=dictionary | An array of objects specifying the forwarding rules for a load balancer.  Required when creating load balancers.  **Default:** `[{"certificate_id": "", "entry_port": 8080, "entry_protocol": "http", "target_port": 8080, "target_protocol": "http", "tls_passthrough": false}]` |
| **certificate_id**  string | Certificate ID  **Default:** `""` |
| **entry_port**  integer | Entry port  **Default:** `8080` |
| **entry_protocol**  string | Entry protocol  **Default:** `"http"` |
| **target_port**  integer | Target port  **Default:** `8080` |
| **target_protocol**  string | Target protocol  **Default:** `"http"` |
| **tls_passthrough**  boolean | TLS passthrough  **Choices:**   - `false` ← (default) - `true` |
| **health_check**  dictionary | An object specifying health check settings for the load balancer.  **Default:** `{"check_interval_seconds": 10, "healthy_threshold": 5, "path": "/", "port": 80, "protocol": "http", "response_timeout_seconds": 5, "unhealthy_threshold": 3}` |
| **check_interval_seconds**  integer | Check interval seconds  **Default:** `10` |
| **healthy_threshold**  integer | Healthy threshold  **Default:** `5` |
| **path**  string | Path  **Default:** `"/"` |
| **port**  integer | Port  **Default:** `80` |
| **protocol**  string | Protocol  **Default:** `"http"` |
| **response_timeout_seconds**  integer | Response timeout seconds  **Default:** `5` |
| **unhealthy_threshold**  integer | Unhealthy threshold  **Default:** `3` |
| **name**  string / required | A human-readable name for a load balancer instance.  Required and must be unique (current API documentation is not up-to-date for this parameter). |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **project_name**  aliases: project  string | Project to assign the resource to (project name, not UUID).  Defaults to the default project of the account (empty string).  Currently only supported when creating.  **Default:** `""` |
| **redirect_http_to_https**  boolean | A boolean value indicating whether HTTP requests to the load balancer on port 80 will be redirected to HTTPS on port 443.  **Choices:**   - `false` ← (default) - `true` |
| **region**  aliases: region_id  string | The slug identifier for the region where the resource will initially be available. |
| **size**  string | The size of the load balancer.  The available sizes are `lb-small`, `lb-medium`, or `lb-large`.  You can resize load balancers after creation up to once per hour.  You cannot resize a load balancer within the first hour of its creation.  This field has been replaced by the `size_unit` field for all regions except in `ams2`, `nyc2`, and `sfo1`.  Each available load balancer size now equates to the load balancer having a set number of nodes.  The formula is `lb-small` = 1 node, `lb-medium` = 3 nodes, `lb-large` = 6 nodes.  **Choices:**   - `"lb-small"` ← (default) - `"lb-medium"` - `"lb-large"` |
| **size_unit**  integer | How many nodes the load balancer contains.  Each additional node increases the load balancer’s ability to manage more connections.  Load balancers can be scaled up or down, and you can change the number of nodes after creation up to once per hour.  This field is currently not available in the `ams2`, `nyc2`, or `sfo1` regions.  Use the `size` field to scale load balancers that reside in these regions.  The value must be in the range 1-100.  **Default:** `1` |
| **state**  string | The usual, `present` to create, `absent` to destroy  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **sticky_sessions**  dictionary | An object specifying sticky sessions settings for the load balancer.  **Default:** `{"type": "none"}` |
| **type**  string | Type  **Default:** `"none"` |
| **tag**  string | A tag associated with the droplets that you want to dynamically assign to the load balancer.  Required when creating load balancers.  Mutually exclusive with droplet_ids, you can either define tag or droplet_ids but not both. |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  **Default:** `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **vpc_uuid**  string | A string specifying the UUID of the VPC to which the load balancer is assigned.  If unspecified, uses the default VPC in the region. |
| **wait**  boolean | Wait for the Load Balancer to be running before returning.  **Choices:**   - `false` - `true` ← (default) |
| **wait_timeout**  integer | How long before wait gives up, in seconds, when creating a Load Balancer.  **Default:** `600` |

## [Examples](digital_ocean_load_balancer_module.md#id3)

```yaml+jinja
- name: Create a Load Balancer
  community.digitalocean.digital_ocean_load_balancer:
    state: present
    name: test-loadbalancer-1
    droplet_ids:
      - 12345678
    region: nyc1
    forwarding_rules:
      - entry_protocol: http
        entry_port: 8080
        target_protocol: http
        target_port: 8080
        certificate_id: ""
        tls_passthrough: false

- name: Create a Load Balancer (and assign to Project "test")
  community.digitalocean.digital_ocean_load_balancer:
    state: present
    name: test-loadbalancer-1
    droplet_ids:
      - 12345678
    region: nyc1
    forwarding_rules:
      - entry_protocol: http
        entry_port: 8080
        target_protocol: http
        target_port: 8080
        certificate_id: ""
        tls_passthrough: false
    project: test

- name: Create a Load Balancer and associate it with a tag
  community.digitalocean.digital_ocean_load_balancer:
    state: present
    name: test-loadbalancer-1
    tag: test-tag
    region: tor1
```

## [Return Values](digital_ocean_load_balancer_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_status**  string | Assignment status (ok, not_found, assigned, already_assigned, service_down)  **Returned:** changed  **Sample:** `"assigned"` |
| **data**  dictionary | A DigitalOcean Load Balancer  **Returned:** changed  **Sample:** `{"load_balancer": {"algorithm": "round_robin", "created_at": "2021-08-22T14:23:41Z", "droplet_ids": [261172461], "enable_backend_keepalive": false, "enable_proxy_protocol": false, "forwarding_rules": [{"certificate_id": "", "entry_port": 8080, "entry_protocol": "http", "target_port": 8080, "target_protocol": "http", "tls_passthrough": false}], "health_check": {"check_interval_seconds": 10, "healthy_threshold": 5, "path": "/", "port": 80, "protocol": "http", "response_timeout_seconds": 5, "unhealthy_threshold": 3}, "id": "b4fdb507-70e8-4325-a89e-d02271b93618", "ip": "159.203.150.113", "name": "test-loadbalancer-1", "redirect_http_to_https": false, "region": {"available": true, "features": ["backups", "ipv6", "metadata", "install_agent", "storage", "image_transfer"], "name": "New York 3", "sizes": ["s-1vcpu-1gb", "s-1vcpu-1gb-amd", "s-1vcpu-1gb-intel", "s-1vcpu-2gb", "s-1vcpu-2gb-amd", "s-1vcpu-2gb-intel", "s-2vcpu-2gb", "s-2vcpu-2gb-amd", "s-2vcpu-2gb-intel", "s-2vcpu-4gb", "s-2vcpu-4gb-amd", "s-2vcpu-4gb-intel", "s-4vcpu-8gb", "c-2", "c2-2vcpu-4gb", "s-4vcpu-8gb-amd", "s-4vcpu-8gb-intel", "g-2vcpu-8gb", "gd-2vcpu-8gb", "s-8vcpu-16gb", "m-2vcpu-16gb", "c-4", "c2-4vcpu-8gb", "s-8vcpu-16gb-amd", "s-8vcpu-16gb-intel", "m3-2vcpu-16gb", "g-4vcpu-16gb", "so-2vcpu-16gb", "m6-2vcpu-16gb", "gd-4vcpu-16gb", "so1_5-2vcpu-16gb", "m-4vcpu-32gb", "c-8", "c2-8vcpu-16gb", "m3-4vcpu-32gb", "g-8vcpu-32gb", "so-4vcpu-32gb", "m6-4vcpu-32gb", "gd-8vcpu-32gb", "so1_5-4vcpu-32gb", "m-8vcpu-64gb", "c-16", "c2-16vcpu-32gb", "m3-8vcpu-64gb", "g-16vcpu-64gb", "so-8vcpu-64gb", "m6-8vcpu-64gb", "gd-16vcpu-64gb", "so1_5-8vcpu-64gb", "m-16vcpu-128gb", "c-32", "c2-32vcpu-64gb", "m3-16vcpu-128gb", "m-24vcpu-192gb", "g-32vcpu-128gb", "so-16vcpu-128gb", "m6-16vcpu-128gb", "gd-32vcpu-128gb", "m3-24vcpu-192gb", "g-40vcpu-160gb", "so1_5-16vcpu-128gb", "m-32vcpu-256gb", "gd-40vcpu-160gb", "so-24vcpu-192gb", "m6-24vcpu-192gb", "m3-32vcpu-256gb", "so1_5-24vcpu-192gb", "m6-32vcpu-256gb"], "slug": "nyc3"}, "size": "lb-small", "status": "active", "sticky_sessions": {"type": "none"}, "tag": "", "vpc_uuid": "b8fd9a58-d93d-4329-b54a-78a397d64855"}}` |
| **msg**  string | Informational or error message encountered during execution  **Returned:** changed  **Sample:** `"No project named test2 found"` |
| **resources**  dictionary | Resource assignment involved in project assignment  **Returned:** changed  **Sample:** `{"assigned_at": "2021-10-25T17:39:38Z", "links": {"self": "https://api.digitalocean.com/v2/load_balancers/17d171d0-8a8b-4251-9c18-c96cc515d36d"}, "status": "assigned", "urn": "do:loadbalancer:17d171d0-8a8b-4251-9c18-c96cc515d36d"}` |

### Authors

- Mark Mercado (@mamercad)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
