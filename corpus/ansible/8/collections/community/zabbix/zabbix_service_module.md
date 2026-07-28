---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_service module – Create/update/delete Zabbix service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_service_module.html
fetched_at: 2026-07-28T02:02:53+00:00
---
# community.zabbix.zabbix_service module – Create/update/delete Zabbix service

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_service_module.md#ansible-collections-community-zabbix-zabbix-service-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_service`.

- [Synopsis](zabbix_service_module.md#synopsis)
- [Requirements](zabbix_service_module.md#requirements)
- [Parameters](zabbix_service_module.md#parameters)
- [Examples](zabbix_service_module.md#examples)

## [Synopsis](zabbix_service_module.md#id1)

- Create/update/delete Zabbix service.

## [Requirements](zabbix_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **algorithm**  string | Status calculation rule. Only applicable if child services exists.  - `status_to_ok`, set status to OK with - `most_crit_if_all_children`, most critical if all children have problems - `most_crit_of_child_serv`, most critical of child services with  **Choices:**   - `"status_to_ok"` ← (default) - `"most_crit_if_all_children"` - `"most_crit_of_child_serv"` |
| **children**  list / elements=string | Child services to be linked to the service. |
| **description**  string | Description of the service. |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **name**  string / required | Name of Zabbix service |
| **parents**  list / elements=string | Parent services to be linked to the service. |
| **problem_tags**  list / elements=dictionary | Problem tags to be created for the service. |
| **operator**  string | Mapping condition operator.  `equals`  `like`  **Choices:**   - `"equals"` ← (default) - `"like"` |
| **tag**  string / required | Problem tag name. |
| **value**  string | Problem tag value.  **Default:** `""` |
| **propagation_rule**  string | Status propagation value. Must be set together with propagation_rule.  `as_is` propagate service status as is - without any changes  `increase` increase the propagated status by a given propagation_value (by 1 to 5 severities)  `decrease` decrease the propagated status by a given propagation_value (by 1 to 5 severities)  `ignore` ignore this service - the status is not propagated to the parent service at all  `fixed` set fixed service status using a given propagation_value  Required with `propagation_value`  **Default:** `"as_is"` |
| **propagation_value**  string | Status propagation value. Must be set together with propagation_rule.  Possible values when *propagation_rule=as_is or ignore*:  - `not_classified`  Possible values when *propagation_rule=increase or decrease*:  - `information` - `warning` - `average` - `high` - `disaster`  Possible values when *propagation_rule=fixed*:  - `ok` - `not_classified` - `information` - `warning` - `average` - `high` - `disaster`  Required with `propagation_rule` |
| **sortorder**  string / required | Position of the service used for sorting. |
| **state**  string | State: present - create/update service; absent - delete service.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status_rules**  list / elements=dictionary | Status rules for the service. |
| **limit_status**  string / required | Limit status.  `ok` OK  `not_classified` Not classified  `information` Information  `warning` Warning  `average` Average  `high` High  `disaster` Disaster |
| **limit_value**  integer / required | Limit value: N, N% or W  Possible values: 1-100000 for N and W, 1-100 for N% |
| **new_status**  string / required | New status value.  `not_classified` Not classified  `information` Information  `warning` Warning  `average` Average  `high` High  `disaster` Disaster |
| **type**  string / required | Condition for setting (New status) status.  `at_least_n_child_services_have_status_or_above` if at least (N) child services have (Status) status or above  `at_least_npct_child_services_have_status_or_above` if at least (N%) of child services have (Status) status or above  `less_than_n_child_services_have_status_or_below` if less than (N) child services have (Status) status or below  `less_than_npct_child_services_have_status_or_below` if less than (N%) of child services have (Status) status or below  `weight_child_services_with_status_or_above_at_least_w` if weight of child services with (Status) status or above is at least (W)  `weight_child_services_with_status_or_above_at_least_npct` if weight of child services with (Status) status or above is at least (N%)  `weight_child_services_with_status_or_below_less_w` if weight of child services with (Status) status or below is less than (W)  `weight_child_services_with_status_or_below_less_npct` if weight of child services with (Status) status or below is less than (N%) |
| **tags**  list / elements=dictionary | Service tags to be created for the service. |
| **tag**  string / required | Service tag name. |
| **value**  string | Service tag value. |
| **weight**  string | Service weight.  **Default:** `"0"` |

## [Examples](zabbix_service_module.md#id4)

```yaml+jinja
---
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

# Creates a new Zabbix service
- name: Create Zabbix service monitoring Apache2 in DCs in Toronto area
  # set task level variables
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_service:
    name: "apache2 service Toronto"
    description: Apache2 services in Toronto area
    sortorder: 0
    propagation_rule: increase
    propagation_value: warning
    weight: 1
    state: present
    tags:
      - tag: zabbix_service
        value: apache2
      - tag: area
        value: Toronto
    problem_tags:
      - tag: service_name
        value: httpd
      - tag: area
        operator: like
        value: toronto
    status_rules:
      - type: at_least_n_child_services_have_status_or_above
        limit_value: 4242
        limit_status: ok
        new_status: average

- name: Create Zabbix service monitoring all Apache2 services
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: "zabbixeu"  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_service:
    name: apache2 service
    description: Apache2 services
    tags:
      - tag: zabbix_service
        value: apache2
      - tag: area
        value: global
    children:
      - "apache2 service Toronto"
```

### Authors

- Emmanuel Riviere (@emriver)
- Evgeny Yurchenko (@BGmot)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
