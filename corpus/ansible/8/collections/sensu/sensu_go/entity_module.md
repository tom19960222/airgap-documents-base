---
collection: ansible
version: "8"
title: "sensu.sensu_go.entity module – Manage Sensu entities"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/entity_module.html
fetched_at: 2026-07-28T02:53:04+00:00
---
# sensu.sensu_go.entity module – Manage Sensu entities

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](entity_module.md#ansible-collections-sensu-sensu-go-entity-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.entity`.

New in sensu.sensu_go 1.0.0

- [Synopsis](entity_module.md#synopsis)
- [Requirements](entity_module.md#requirements)
- [Parameters](entity_module.md#parameters)
- [See Also](entity_module.md#see-also)
- [Examples](entity_module.md#examples)
- [Return Values](entity_module.md#return-values)

## [Synopsis](entity_module.md#id1)

- Create, update or delete Sensu entity.
- For more information, refer to the Sensu documentation at <https://docs.sensu.io/sensu-go/latest/reference/entities/>.

## [Requirements](entity_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](entity_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **annotations**  dictionary | Custom metadata fields with fewer restrictions, as key/value pairs.  These are preserved by Sensu but not accessible as tokens or identifiers, and are mainly intended for use with external tools.  **Default:** `{}` |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  *added in sensu.sensu_go 1.3.0* | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  *added in sensu.sensu_go 1.5.0* | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  **Default:** `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  **Default:** `"admin"` |
| **verify**  boolean  *added in sensu.sensu_go 1.5.0* | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **deregister**  boolean | If the entity should be removed when it stops sending keepalive messages.  **Choices:**   - `false` - `true` |
| **deregistration_handler**  string | The name of the handler to be called when an entity is deregistered. |
| **entity_class**  string | Entity class. Standard classes are `proxy` and `agent`, but you can use whatever you want.  Required if *state* is `present`. |
| **labels**  dictionary | Custom metadata fields that can be accessed within Sensu, as key/value pairs.  **Default:** `{}` |
| **last_seen**  integer | Timestamp the entity was last seen, in seconds since the Unix epoch. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **namespace**  string | RBAC namespace to operate in. If this is not set the value of the SENSU_NAMESPACE environment variable will be used.  **Default:** `"default"` |
| **redact**  list / elements=string | List of items to redact from log messages. If a value is provided, it overwrites the default list of items to be redacted. |
| **state**  string | Target state of the Sensu object.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **subscriptions**  list / elements=string | List of subscriptions for the entity. |
| **system**  dictionary | System information about the entity, such as operating system and platform. See <https://docs.sensu.io/sensu-go/5.13/reference/entities/#system-attributes> for more information. |
| **user**  string | Sensu RBAC username used by the entity. Agent entities require get, list, create, update, and delete permissions for events across all namespaces. |

## [See Also](entity_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.entity_info](entity_info_module.md#ansible-collections-sensu-sensu-go-entity-info-module)
> :   List Sensu entities.

## [Examples](entity_module.md#id5)

```yaml+jinja
- name: Create an entity
  sensu.sensu_go.entity:
    auth:
      url: http://localhost:8080
    name: entity
    entity_class: proxy
    subscriptions:
      - web
      - prod
    system:
      hostname: playbook-entity
      os: linux
      platform: ubutntu
      network:
        interfaces:
          - name: lo
            addresses:
              - 127.0.0.1/8
              - ::1/128
          - name: eth0
            mac: 52:54:00:20:1b:3c
            addresses:
              - 93.184.216.34/24
    last_seen: 1522798317
    deregister: yes
    deregistration_handler: email-handler
    redact:
      - password
      - pass
      - api_key
    user: agent

- name: Delete an entity
  sensu.sensu_go.entity:
    name: entity
    state: absent
```

## [Return Values](entity_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu entity.  **Returned:** success  **Sample:** `{"deregister": false, "deregistration": {}, "entity_class": "agent", "last_seen": 1542667231, "metadata": {"annotations": null, "labels": null, "name": "webserver01", "namespace": "default"}, "redact": ["password", "private_key", "secret"], "sensu_agent_version": "1.0.0", "subscriptions": ["entity:webserver01"], "system": {"arch": "amd64", "cloud_provider": null, "libc_type": "glibc", "network": {"interfaces": [{"addresses": ["127.0.0.1/8", "::1/128"], "name": "lo"}, {"addresses": ["172.28.128.3/24", "fe80::a00:27ff:febc:be60/64"], "mac": "08:00:27:bc:be:60", "name": "enp0s8"}]}, "os": "linux", "platform": "centos", "platform_family": "rhel", "platform_version": "7.4.1708", "vm_role": "host", "vm_system": "kvm"}, "user": "agent"}` |

### Authors

- Paul Arthur (@flowerysong)
- Aljaz Kosir (@aljazkosir)
- Miha Plesko (@miha-plesko)
- Tadej Borovsak (@tadeboro)

### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
