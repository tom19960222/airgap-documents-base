---
collection: ansible
version: "6"
title: "community.digitalocean.digital_ocean_firewall module – Manage cloud firewalls within DigitalOcean"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/digitalocean/digital_ocean_firewall_module.html
fetched_at: 2026-07-27T17:06:43+00:00
---
# community.digitalocean.digital_ocean_firewall module – Manage cloud firewalls within DigitalOcean

> **Note:**
>
> This module is part of the [community.digitalocean collection](https://galaxy.ansible.com/community/digitalocean) (version 1.22.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.digitalocean`.
>
> To use it in a playbook, specify: `community.digitalocean.digital_ocean_firewall`.

New in community.digitalocean 1.1.0

- [Synopsis](digital_ocean_firewall_module.md#synopsis)
- [Parameters](digital_ocean_firewall_module.md#parameters)
- [Examples](digital_ocean_firewall_module.md#examples)
- [Return Values](digital_ocean_firewall_module.md#return-values)

## [Synopsis](digital_ocean_firewall_module.md#id1)

- This module can be used to add or remove firewalls on the DigitalOcean cloud platform.

## [Parameters](digital_ocean_firewall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **baseurl**  string | DigitalOcean API base url.  Default: `"https://api.digitalocean.com/v2"` |
| **droplet_ids**  list / elements=string | List of droplet ids to be assigned to the firewall |
| **inbound_rules**  list / elements=dictionary | Firewall rules specifically targeting inbound network traffic into DigitalOcean |
| **ports**  string / required | The ports on which traffic will be allowed, single, range, or all |
| **protocol**  string | Network protocol to be accepted.  Choices:   - `"udp"` - `"tcp"` ← (default) - `"icmp"` |
| **sources**  dictionary / required | Dictionary of locations from which inbound traffic will be accepted |
| **addresses**  list / elements=string | List of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the firewall will allow traffic |
| **droplet_ids**  list / elements=string | List of integers containing the IDs of the Droplets to which the firewall will allow traffic |
| **load_balancer_uids**  list / elements=string | List of strings containing the IDs of the Load Balancers to which the firewall will allow traffic |
| **tags**  list / elements=string | List of strings containing the names of Tags corresponding to groups of Droplets to which the Firewall will allow traffic |
| **name**  string / required | Name of the firewall rule to create or manage |
| **oauth_token**  aliases: api_token  string | DigitalOcean OAuth token.  There are several other environment variables which can be used to provide this value.  i.e., - ‘DO_API_TOKEN’, ‘DO_API_KEY’, ‘DO_OAUTH_TOKEN’ and ‘OAUTH_TOKEN’ |
| **outbound_rules**  list / elements=dictionary | Firewall rules specifically targeting outbound network traffic from DigitalOcean |
| **destinations**  dictionary / required | Dictionary of locations from which outbound traffic will be allowed |
| **addresses**  list / elements=string | List of strings containing the IPv4 addresses, IPv6 addresses, IPv4 CIDRs, and/or IPv6 CIDRs to which the firewall will allow traffic |
| **droplet_ids**  list / elements=string | List of integers containing the IDs of the Droplets to which the firewall will allow traffic |
| **load_balancer_uids**  list / elements=string | List of strings containing the IDs of the Load Balancers to which the firewall will allow traffic |
| **tags**  list / elements=string | List of strings containing the names of Tags corresponding to groups of Droplets to which the Firewall will allow traffic |
| **ports**  string / required | The ports on which traffic will be allowed, single, range, or all |
| **protocol**  string | Network protocol to be accepted.  Choices:   - `"udp"` - `"tcp"` ← (default) - `"icmp"` |
| **state**  string | Assert the state of the firewall rule. Set to ‘present’ to create or update and ‘absent’ to remove.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags to be assigned to the firewall |
| **timeout**  integer | The timeout in seconds used for polling DigitalOcean’s API.  Default: `30` |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `no` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](digital_ocean_firewall_module.md#id3)

```yaml+jinja
# Allows tcp connections to port 22 (SSH) from specific sources
# Allows tcp connections to ports 80 and 443 from any source
# Allows outbound access to any destination for protocols tcp, udp and icmp
# The firewall rules will be applied to any droplets with the tag "sample"
- name: Create a Firewall named my-firewall
  digital_ocean_firewall:
    name: my-firewall
    state: present
    inbound_rules:
      - protocol: "tcp"
        ports: "22"
        sources:
          addresses: ["1.2.3.4"]
          droplet_ids: ["my_droplet_id_1", "my_droplet_id_2"]
          load_balancer_uids: ["my_lb_id_1", "my_lb_id_2"]
          tags: ["tag_1", "tag_2"]
      - protocol: "tcp"
        ports: "80"
        sources:
          addresses: ["0.0.0.0/0", "::/0"]
      - protocol: "tcp"
        ports: "443"
        sources:
          addresses: ["0.0.0.0/0", "::/0"]
    outbound_rules:
      - protocol: "tcp"
        ports: "1-65535"
        destinations:
          addresses: ["0.0.0.0/0", "::/0"]
      - protocol: "udp"
        ports: "1-65535"
        destinations:
          addresses: ["0.0.0.0/0", "::/0"]
      - protocol: "icmp"
        ports: "1-65535"
        destinations:
          addresses: ["0.0.0.0/0", "::/0"]
    droplet_ids: []
    tags: ["sample"]
```

## [Return Values](digital_ocean_firewall_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | DigitalOcean firewall resource  Returned: success  Sample: `{"created_at": "2020-08-11T18:41:30Z", "droplet_ids": [], "id": "7acd6ee2-257b-434f-8909-709a5816d4f9", "inbound_rules": [{"ports": "443", "protocol": "tcp", "sources": {"addresses": ["1.2.3.4"], "droplet_ids": ["my_droplet_id_1", "my_droplet_id_2"], "load_balancer_uids": ["my_lb_id_1", "my_lb_id_2"], "tags": ["tag_1", "tag_2"]}}, {"ports": "80", "protocol": "tcp", "sources": {"addresses": ["0.0.0.0/0", "::/0"]}}, {"ports": "443", "protocol": "tcp", "sources": {"addresses": ["0.0.0.0/0", "::/0"]}}], "name": "my-firewall", "outbound_rules": [{"destinations": {"addresses": ["0.0.0.0/0", "::/0"]}, "ports": "1-65535", "protocol": "tcp"}, {"destinations": {"addresses": ["0.0.0.0/0", "::/0"]}, "ports": "1-65535", "protocol": "udp"}, {"destinations": {"addresses": ["0.0.0.0/0", "::/0"]}, "ports": "1-65535", "protocol": "icmp"}], "pending_changes": [], "status": "succeeded", "tags": ["sample"]}` |

### Authors

- Anthony Bond (@BondAnthony)
- Lucas Basquerotto (@lucasbasquerotto)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.digitalocean/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.digitalocean)
