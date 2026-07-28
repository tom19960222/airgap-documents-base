---
collection: ansible
version: "6"
title: "theforeman.foreman.activation_key module – Manage Activation Keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/theforeman/foreman/activation_key_module.html
fetched_at: 2026-07-28T00:20:27+00:00
---
# theforeman.foreman.activation_key module – Manage Activation Keys

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/theforeman/foreman) (version 3.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](activation_key_module.md#ansible-collections-theforeman-foreman-activation-key-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.activation_key`.

New in theforeman.foreman 1.0.0

- [Synopsis](activation_key_module.md#synopsis)
- [Requirements](activation_key_module.md#requirements)
- [Parameters](activation_key_module.md#parameters)
- [Examples](activation_key_module.md#examples)
- [Return Values](activation_key_module.md#return-values)

## [Synopsis](activation_key_module.md#id1)

- Create and manage activation keys

## [Requirements](activation_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](activation_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auto_attach**  boolean | Set Auto-Attach on or off  Choices:   - `false` - `true` |
| **content_overrides**  list / elements=dictionary | List of content overrides that include label and override state  Label refers to repository `content_label`, e.g. rhel-7-server-rpms  Override state (‘enabled’, ‘disabled’, or ‘default’) sets initial state of repository for newly registered hosts |
| **label**  string / required | Repository `content_label` to override when registering hosts with the activation key |
| **override**  string / required | Override value to use for the repository when registering hosts with the activation key  Choices:   - `"enabled"` - `"disabled"` - `"default"` |
| **content_view**  string | Name of the content view |
| **description**  string | Description of the activation key |
| **host_collections**  list / elements=string | List of host collections to add to activation key |
| **lifecycle_environment**  string | Name of the lifecycle environment |
| **max_hosts**  integer | Maximum number of registered content hosts.  Required if *unlimited_hosts=false* |
| **name**  string / required | Name of the activation key |
| **new_name**  string | Name of the new activation key when state == copied |
| **organization**  string / required | Organization that the entity is in |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **purpose_addons**  list / elements=string | Sets the system purpose add-ons |
| **purpose_role**  string | Sets the system purpose role |
| **purpose_usage**  string | Sets the system purpose usage |
| **release_version**  string | Set the content release version |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **service_level**  string | Set the service level  Choices:   - `"Self-Support"` - `"Standard"` - `"Premium"` |
| **state**  string | State of the Activation Key  If `copied` the key will be copied to a new one with *new_name* as the name and all other fields left untouched  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  Choices:   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` - `"copied"` |
| **subscriptions**  list / elements=dictionary | List of subscriptions that include either Name, Pool ID, or Upstream Pool ID.  Pool IDs are preferred since Names and Upstream Pool IDs are not guaranteed to be unique. The module will fail if it finds more than one match. |
| **name**  string | Name of the Subscription to be added.  Mutually exclusive with *pool_id* and *upstream_pool_id*. |
| **pool_id**  string | Pool ID of the Subscription to be added.  Mutually exclusive with *name* and *upstream_pool_id*.  Also named `Candlepin Id` in the CSV export of the subscriptions,  it is as well the `UUID` as output by `hammer subscription list`. |
| **upstream_pool_id**  string | Upstream Pool ID of the Subscription to be added.  Mutually exclusive with *name* and *pool_id*.  Also named `Master Pools` in the Red Hat Portal. |
| **unlimited_hosts**  boolean | Can the activation key have unlimited hosts  Choices:   - `false` - `true` |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  Choices:   - `false` - `true` ← (default) |

## [Examples](activation_key_module.md#id4)

```yaml+jinja
- name: "Create client activation key"
  theforeman.foreman.activation_key:
    username: "admin"
    password: "changeme"
    server_url: "https://foreman.example.com"
    name: "Clients"
    organization: "Default Organization"
    lifecycle_environment: "Library"
    content_view: 'client content view'
    host_collections:
        - rhel7-servers
        - rhel7-production
    subscriptions:
      - pool_id: "8a88e9826db22df5016dd018abdd029b"
      - pool_id: "8a88e9826db22df5016dd01a23270344"
      - name: "Red Hat Enterprise Linux"
    content_overrides:
        - label: rhel-7-server-optional-rpms
          override: enabled
    auto_attach: False
    release_version: 7Server
    service_level: Standard
```

## [Return Values](activation_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  Returned: success |
| **activation_keys**  list / elements=dictionary | List of activation keys.  Returned: success |

### Authors

- Andrew Kofink (@akofink)

### Collection links

[Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
[Homepage](https://theforeman.org/)
[Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
