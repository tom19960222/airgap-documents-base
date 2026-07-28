---
collection: ansible
version: "8"
title: "community.general.consul module – Add, modify & delete services within a consul cluster"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/consul_module.html
fetched_at: 2026-07-28T01:45:10+00:00
---
# community.general.consul module – Add, modify & delete services within a consul cluster

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](consul_module.md#ansible-collections-community-general-consul-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.consul`.

- [Synopsis](consul_module.md#synopsis)
- [Requirements](consul_module.md#requirements)
- [Parameters](consul_module.md#parameters)
- [Attributes](consul_module.md#attributes)
- [Examples](consul_module.md#examples)

## [Synopsis](consul_module.md#id1)

- Registers services and checks for an agent with a consul cluster. A service is some process running on the agent node that should be advertised by consul’s discovery mechanism. It may optionally supply a check definition, a periodic service test to notify the consul cluster of service’s health.
- Checks may also be registered per node e.g. disk usage, or cpu usage and notify the health of the entire node to the cluster. Service level checks do not require a check name or id as these are derived by Consul from the Service name and id respectively by appending ‘service:’ Node level checks require a `check_name` and optionally a `check_id`.
- Currently, there is no complete way to retrieve the script, interval or TTL metadata for a registered check. Without this metadata it is not possible to tell if the data supplied with ansible represents a change to a check. As a result this does not attempt to determine changes and will always report a changed occurred. An API method is planned to supply this metadata so at that stage change management will be added.
- See <http://consul.io> for more details.

Aliases: clustering.consul.consul

## [Requirements](consul_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-consul
- requests

## [Parameters](consul_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ack_params_state_absent**  boolean | Disable deprecation warning when using parameters incompatible with `state=absent`.  **Choices:**   - `false` - `true` |
| **check_id**  string | An ID for the service check. If `state=absent`, defaults to `check_name`. Ignored if part of a service definition. |
| **check_name**  string | Name for the service check. Required if standalone, ignored if part of service definition. |
| **host**  string | Host of the consul agent defaults to localhost.  **Default:** `"localhost"` |
| **http**  string | Checks can be registered with an HTTP endpoint. This means that consul will check that the http endpoint returns a successful HTTP status.  Requires `interval` to be provided. |
| **interval**  string | The interval at which the service check will be run. This is a number with a `s` or `m` suffix to signify the units of seconds or minutes, for example `15s` or `1m`. If no suffix is supplied `s` will be used by default, for example `10` will be `10s`.  Required if one of the parameters `script`, `http`, or `tcp` is specified. |
| **notes**  string | Notes to attach to check when registering it. |
| **port**  integer | The port on which the consul agent is running.  **Default:** `8500` |
| **scheme**  string | The protocol scheme on which the consul agent is running.  **Default:** `"http"` |
| **script**  string | The script/command that will be run periodically to check the health of the service.  Requires `interval` to be provided. |
| **service_address**  string | The address to advertise that the service will be listening on. This value will be passed as the `address` parameter to Consul’s `/v1/agent/service/register` API method, so refer to the Consul API documentation for further details. |
| **service_id**  string | The ID for the service, must be unique per node. If `state=absent`, defaults to the service name if supplied. |
| **service_name**  string | Unique name for the service on a node, must be unique per node, required if registering a service. May be omitted if registering a node level check. |
| **service_port**  integer | The port on which the service is listening. Can optionally be supplied for registration of a service, that is if `service_name` or `service_id` is set. |
| **state**  string | Register or deregister the consul service, defaults to present.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | Tags that will be attached to the service registration. |
| **tcp**  string  *added in community.general 1.3.0* | Checks can be registered with a TCP port. This means that consul will check if the connection attempt to that port is successful (that is, the port is currently accepting connections). The format is `host:port`, for example `localhost:80`.  Requires `interval` to be provided. |
| **timeout**  string | A custom HTTP check timeout. The consul default is 10 seconds. Similar to the interval this is a number with a `s` or `m` suffix to signify the units of seconds or minutes, for example `15s` or `1m`. If no suffix is supplied `s` will be used by default, for example `10` will be `10s`. |
| **token**  string | The token key identifying an ACL rule set. May be required to register services. |
| **ttl**  string | Checks can be registered with a TTL instead of a `script` and `interval` this means that the service will check in with the agent before the TTL expires. If it doesn’t the check will be considered failed. Required if registering a check and the script an interval are missing Similar to the interval this is a number with a `s` or `m` suffix to signify the units of seconds or minutes, for example `15s` or `1m`. If no suffix is supplied `s` will be used by default, for example `10` will be `10s`. |
| **validate_certs**  boolean | Whether to verify the TLS certificate of the consul agent.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](consul_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](consul_module.md#id5)

```yaml+jinja
- name: Register nginx service with the local consul agent
  community.general.consul:
    service_name: nginx
    service_port: 80

- name: Register nginx service with curl check
  community.general.consul:
    service_name: nginx
    service_port: 80
    script: curl http://localhost
    interval: 60s

- name: register nginx with a tcp check
  community.general.consul:
    service_name: nginx
    service_port: 80
    interval: 60s
    tcp: localhost:80

- name: Register nginx with an http check
  community.general.consul:
    service_name: nginx
    service_port: 80
    interval: 60s
    http: http://localhost:80/status

- name: Register external service nginx available at 10.1.5.23
  community.general.consul:
    service_name: nginx
    service_port: 80
    service_address: 10.1.5.23

- name: Register nginx with some service tags
  community.general.consul:
    service_name: nginx
    service_port: 80
    tags:
      - prod
      - webservers

- name: Remove nginx service
  community.general.consul:
    service_name: nginx
    state: absent

- name: Register celery worker service
  community.general.consul:
    service_name: celery-worker
    tags:
      - prod
      - worker

- name: Create a node level check to test disk usage
  community.general.consul:
    check_name: Disk usage
    check_id: disk_usage
    script: /opt/disk_usage.py
    interval: 5m

- name: Register an http check against a service that's already registered
  community.general.consul:
    check_name: nginx-check2
    check_id: nginx-check2
    service_id: nginx
    interval: 60s
    http: http://localhost:80/morestatus
```

### Authors

- Steve Gargan (@sgargan)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
