---
collection: ansible
version: "8"
title: "community.general.apache2_mod_proxy module – Set and/or get members’ attributes of an Apache httpd 2.4 mod_proxy balancer pool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/apache2_mod_proxy_module.html
fetched_at: 2026-07-28T01:44:39+00:00
---
# community.general.apache2_mod_proxy module – Set and/or get members’ attributes of an Apache httpd 2.4 mod_proxy balancer pool

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.apache2_mod_proxy`.

- [Synopsis](apache2_mod_proxy_module.md#synopsis)
- [Parameters](apache2_mod_proxy_module.md#parameters)
- [Attributes](apache2_mod_proxy_module.md#attributes)
- [Examples](apache2_mod_proxy_module.md#examples)
- [Return Values](apache2_mod_proxy_module.md#return-values)

## [Synopsis](apache2_mod_proxy_module.md#id1)

- Set and/or get members’ attributes of an Apache httpd 2.4 mod_proxy balancer pool, using HTTP POST and GET requests. The httpd mod_proxy balancer-member status page has to be enabled and accessible, as this module relies on parsing this page. This module supports ansible check_mode, and requires BeautifulSoup python module.

Aliases: web_infrastructure.apache2_mod_proxy

## [Parameters](apache2_mod_proxy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **balancer_url_suffix**  string | Suffix of the balancer pool url required to access the balancer pool status page (e.g. balancer_vhost[:port]/balancer_url_suffix).  **Default:** `"/balancer-manager/"` |
| **balancer_vhost**  string / required | (ipv4|ipv6|fqdn):port of the Apache httpd 2.4 mod_proxy balancer pool. |
| **member_host**  string | (ipv4|ipv6|fqdn) of the balancer member to get or to set attributes to. Port number is autodetected and should not be specified here. If undefined, apache2_mod_proxy module will return a members list of dictionaries of all the current balancer pool members’ attributes. |
| **state**  string | Desired state of the member host. (absent|disabled),drained,hot_standby,ignore_errors can be simultaneously invoked by separating them with a comma (e.g. state=drained,ignore_errors).  Accepted state values: [“present”, “absent”, “enabled”, “disabled”, “drained”, “hot_standby”, “ignore_errors”] |
| **tls**  boolean | Use https to access balancer management page.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Validate ssl/tls certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](apache2_mod_proxy_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](apache2_mod_proxy_module.md#id4)

```yaml+jinja
- name: Get all current balancer pool members attributes
  community.general.apache2_mod_proxy:
    balancer_vhost: 10.0.0.2

- name: Get a specific member attributes
  community.general.apache2_mod_proxy:
    balancer_vhost: myws.mydomain.org
    balancer_suffix: /lb/
    member_host: node1.myws.mydomain.org

# Enable all balancer pool members:
- name: Get attributes
  community.general.apache2_mod_proxy:
    balancer_vhost: '{{ myloadbalancer_host }}'
  register: result

- name: Enable all balancer pool members
  community.general.apache2_mod_proxy:
    balancer_vhost: '{{ myloadbalancer_host }}'
    member_host: '{{ item.host }}'
    state: present
  with_items: '{{ result.members }}'

# Gracefully disable a member from a loadbalancer node:
- name: Step 1
  community.general.apache2_mod_proxy:
    balancer_vhost: '{{ vhost_host }}'
    member_host: '{{ member.host }}'
    state: drained
  delegate_to: myloadbalancernode

- name: Step 2
  ansible.builtin.wait_for:
    host: '{{ member.host }}'
    port: '{{ member.port }}'
    state: drained
  delegate_to: myloadbalancernode

- name: Step 3
  community.general.apache2_mod_proxy:
    balancer_vhost: '{{ vhost_host }}'
    member_host: '{{ member.host }}'
    state: absent
  delegate_to: myloadbalancernode
```

## [Return Values](apache2_mod_proxy_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **member**  dictionary | specific balancer member information dictionary, returned when apache2_mod_proxy module is invoked with member_host parameter.  **Returned:** success  **Sample:** `{"attributes": {"Busy": "0", "Elected": "42", "Factor": "1", "From": "136K", "Load": "0", "Route": null, "RouteRedir": null, "Set": "0", "Status": "Init Ok ", "To": " 47K", "Worker URL": null}, "balancer_url": "http://10.10.0.2/balancer-manager/", "host": "10.10.0.20", "management_url": "http://10.10.0.2/lb/?b=mywsbalancer&w=http://10.10.0.20:8080/ws&nonce=8925436c-79c6-4841-8936-e7d13b79239b", "path": "/ws", "port": 8080, "protocol": "http", "status": {"disabled": false, "drained": false, "hot_standby": false, "ignore_errors": false}}` |
| **members**  list / elements=string | list of member (defined above) dictionaries, returned when apache2_mod_proxy is invoked with no member_host and state args.  **Returned:** success  **Sample:** `[{"attributes": {"Busy": "0", "Elected": "42", "Factor": "1", "From": "136K", "Load": "0", "Route": null, "RouteRedir": null, "Set": "0", "Status": "Init Ok ", "To": " 47K", "Worker URL": null}, "balancer_url": "http://10.10.0.2/balancer-manager/", "host": "10.10.0.20", "management_url": "http://10.10.0.2/lb/?b=mywsbalancer&w=http://10.10.0.20:8080/ws&nonce=8925436c-79c6-4841-8936-e7d13b79239b", "path": "/ws", "port": 8080, "protocol": "http", "status": {"disabled": false, "drained": false, "hot_standby": false, "ignore_errors": false}}, {"attributes": {"Busy": "0", "Elected": "42", "Factor": "1", "From": "136K", "Load": "0", "Route": null, "RouteRedir": null, "Set": "0", "Status": "Init Ok ", "To": " 47K", "Worker URL": null}, "balancer_url": "http://10.10.0.2/balancer-manager/", "host": "10.10.0.21", "management_url": "http://10.10.0.2/lb/?b=mywsbalancer&w=http://10.10.0.21:8080/ws&nonce=8925436c-79c6-4841-8936-e7d13b79239b", "path": "/ws", "port": 8080, "protocol": "http", "status": {"disabled": false, "drained": false, "hot_standby": false, "ignore_errors": false}}]` |

### Authors

- Olivier Boukili (@oboukili)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
