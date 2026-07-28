---
collection: ansible
version: "6"
title: "community.zabbix.zabbix_service module – Create/update/delete Zabbix service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_service_module.html
fetched_at: 2026-07-27T17:24:20+00:00
---
# community.zabbix.zabbix_service module – Create/update/delete Zabbix service

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
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
- [Notes](zabbix_service_module.md#notes)
- [Examples](zabbix_service_module.md#examples)

## [Synopsis](zabbix_service_module.md#id1)

- Create/update/delete Zabbix service.

## [Requirements](zabbix_service_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](zabbix_service_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **algorithm**  string | Algorithm used to calculate the sla with < Zabbix 6.0  - `no`, sla is not calculated - `one_child`, problem if at least one child has a problem - `all_children`, problem if all children have problems  Status calculation rule. Only applicable if child services exists with >= Zabbix 6.0  - `status_to_ok`, set status to OK with - `most_crit_if_all_children`, most critical if all children have problems - `most_crit_of_child_serv`, most critical of child services with  Choices:   - `"no"` - `"one_child"` ← (default) - `"all_children"` - `"status_to_ok"` - `"most_crit_if_all_children"` - `"most_crit_of_child_serv"` |
| **calculate_sla**  boolean | If yes, calculate the SLA value for this service, showsla in Zabbix API  With >= Zabbix 6.0 this field is removed from the API and is dropped silently by module.  Choices:   - `false` ← (default) - `true` |
| **children**  list / elements=string | Child services to be linked to the service.  New field with >= Zabbix 6.0. |
| **description**  string | Description of the service.  New field with >= Zabbix 6.0. |
| **login_password**  string | Zabbix user password.  If not set the environment variable `ZABBIX_PASSWORD` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **login_user**  string | Zabbix user name.  If not set the environment variable `ZABBIX_USERNAME` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **name**  string / required | Name of Zabbix service |
| **parent**  string | Name of Zabbix service parent  With >= Zabbix 6.0 this field is removed from the API and is dropped silently by module. |
| **parents**  list / elements=string | Parent services to be linked to the service.  New field with >= Zabbix 6.0. |
| **problem_tags**  list / elements=dictionary | Problem tags to be created for the service.  New field with >= Zabbix 6.0. |
| **operator**  string | Mapping condition operator.  `equals`  `like`  Choices:   - `"equals"` ← (default) - `"like"` |
| **tag**  string / required | Problem tag name. |
| **value**  string | Problem tag value.  Default: `""` |
| **propagation_rule**  string | Status propagation value. Must be set together with propagation_rule.  New field with >= Zabbix 6.0.  `as_is` propagate service status as is - without any changes  `increase` increase the propagated status by a given propagation_value (by 1 to 5 severities)  `decrease` decrease the propagated status by a given propagation_value (by 1 to 5 severities)  `ignore` ignore this service - the status is not propagated to the parent service at all  `fixed` set fixed service status using a given propagation_value  Required with `propagation_value`  Default: `"as_is"` |
| **propagation_value**  string | Status propagation value. Must be set together with propagation_rule.  New field with >= Zabbix 6.0.  Possible values when *propagation_rule=as_is or ignore*:  - `not_classified`  Possible values when *propagation_rule=increase or decrease*:  - `information` - `warning` - `average` - `high` - `disaster`  Possible values when *propagation_rule=fixed*:  - `ok` - `not_classified` - `information` - `warning` - `average` - `high` - `disaster`  Required with `propagation_rule` |
| **server_url**  aliases: url  string | URL of Zabbix server, with protocol (http or https). `url` is an alias for `server_url`.  If not set the environment variable `ZABBIX_SERVER` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release |
| **sla**  float | Sla value (i.e 99.99), goodsla in Zabbix API  With >= Zabbix 6.0 this field is removed from the API and is dropped silently by module. |
| **sortorder**  string / required | Position of the service used for sorting. |
| **state**  string | State: present - create/update service; absent - delete service.  Choices:   - `"present"` ← (default) - `"absent"` |
| **status_rules**  list / elements=dictionary | Status rules for the service.  New field with >= Zabbix 6.0. |
| **limit_status**  string / required | Limit status.  `ok` OK  `not_classified` Not classified  `information` Information  `warning` Warning  `average` Average  `high` High  `disaster` Disaster |
| **limit_value**  integer / required | Limit value: N, N% or W  Possible values: 1-100000 for N and W, 1-100 for N% |
| **new_status**  string / required | New status value.  `not_classified` Not classified  `information` Information  `warning` Warning  `average` Average  `high` High  `disaster` Disaster |
| **type**  string / required | Condition for setting (New status) status.  `at_least_n_child_services_have_status_or_above` if at least (N) child services have (Status) status or above  `at_least_npct_child_services_have_status_or_above` if at least (N%) of child services have (Status) status or above  `less_than_n_child_services_have_status_or_below` if less than (N) child services have (Status) status or below  `less_than_npct_child_services_have_status_or_below` if less than (N%) of child services have (Status) status or below  `weight_child_services_with_status_or_above_at_least_w` if weight of child services with (Status) status or above is at least (W)  `weight_child_services_with_status_or_above_at_least_npct` if weight of child services with (Status) status or above is at least (N%)  `weight_child_services_with_status_or_below_less_w` if weight of child services with (Status) status or below is less than (W)  `weight_child_services_with_status_or_below_less_npct` if weight of child services with (Status) status or below is less than (N%) |
| **tags**  list / elements=dictionary | Service tags to be created for the service.  New field with >= Zabbix 6.0. |
| **tag**  string / required | Service tag name. |
| **value**  string | Service tag value. |
| **timeout**  integer | The timeout of API request (seconds).  This option is deprecated with the move to httpapi connection and will be removed in the next release  Default: `10` |
| **trigger_host**  string | Name of host linked to the service.  With >= Zabbix 6.0 this field is removed from the API and is dropped silently by module. |
| **trigger_name**  string | Name of trigger linked to the service.  With >= Zabbix 6.0 this field is removed from the API and is dropped silently by module. |
| **validate_certs**  boolean | If set to False, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If not set the environment variable `ZABBIX_VALIDATE_CERTS` will be used.  This option is deprecated with the move to httpapi connection and will be removed in the next release  Choices:   - `false` - `true` ← (default) |
| **weight**  string | Service weight.  New field with >= Zabbix 6.0.  Default: `"0"` |

## [Notes](zabbix_service_module.md#id4)

> **Note:**
>
> - If you use *login_password=zabbix*, the word “zabbix” is replaced by “\*\*\*\*\*\*\*\*” in all module output, because *login_password* uses `no_log`. See [this FAQ](https://docs.ansible.com/ansible/latest/network/user_guide/faq.html#why-is-my-output-sometimes-replaced-with) for more information.

## [Examples](zabbix_service_module.md#id5)

```yaml+jinja
---
# Set following variables for Zabbix Server host in play or inventory
- name: Set connection specific variables
  set_fact:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 80
    ansible_httpapi_use_ssl: false
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu

# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

# Creates a new Zabbix service with Zabbix < 6.0
- name: Manage services
  community.zabbix.zabbix_service:
    name: apache2 service
    sla: 99.99
    calculate_sla: yes
    algorithm: one_child
    trigger_name: apache2 service status
    trigger_host: webserver01
    state: present

# Creates a new Zabbix service with Zabbix >= 6.0
- name: Create Zabbix service monitoring Apache2 in DCs in Toronto area
  community.zabbix.zabbix_service:
    name: 'apache2 service Toronto'
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
  community.zabbix.zabbix_service:
    name: apache2 service
    description: Apache2 services
    tags:
      - tag: zabbix_service
        value: apache2
      - tag: area
        value: global
    children:
      - 'apache2 service Toronto'
```

### Authors

- Emmanuel Riviere (@emriver)
- Evgeny Yurchenko (@BGmot)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
