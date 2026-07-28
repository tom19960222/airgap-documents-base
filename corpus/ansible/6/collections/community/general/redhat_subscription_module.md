---
collection: ansible
version: "6"
title: "community.general.redhat_subscription module – Manage registration and subscriptions to RHSM using the subscription-manager command"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/redhat_subscription_module.html
fetched_at: 2026-07-27T17:12:38+00:00
---
# community.general.redhat_subscription module – Manage registration and subscriptions to RHSM using the `subscription-manager` command

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](redhat_subscription_module.md#ansible-collections-community-general-redhat-subscription-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.redhat_subscription`.

- [Synopsis](redhat_subscription_module.md#synopsis)
- [Requirements](redhat_subscription_module.md#requirements)
- [Parameters](redhat_subscription_module.md#parameters)
- [Notes](redhat_subscription_module.md#notes)
- [Examples](redhat_subscription_module.md#examples)
- [Return Values](redhat_subscription_module.md#return-values)

## [Synopsis](redhat_subscription_module.md#id1)

- Manage registration and subscription to the Red Hat Subscription Management entitlement platform using the `subscription-manager` command

## [Requirements](redhat_subscription_module.md#id2)

The below requirements are needed on the host that executes this module.

- subscription-manager

## [Parameters](redhat_subscription_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activationkey**  string | supply an activation key for use with registration |
| **auto_attach**  aliases: autosubscribe  boolean | Upon successful registration, auto-consume available subscriptions  Added in favor of deprecated autosubscribe in 2.5.  Choices:   - `false` - `true` |
| **consumer_id**  string | References an existing consumer ID to resume using a previous registration  for this system. If the system’s identity certificate is lost or corrupted, this option allows it to resume using its previous identity and subscriptions. The default is to not specify a consumer ID so a new ID is created. |
| **consumer_name**  string | Name of the system to register, defaults to the hostname |
| **consumer_type**  string | The type of unit to register, defaults to system |
| **environment**  string | Register with a specific environment in the destination org. Used with Red Hat Satellite or Katello |
| **force_register**  boolean | Register the system even if it is already registered  Choices:   - `false` ← (default) - `true` |
| **org_id**  string | Organization ID to use in conjunction with activationkey |
| **password**  string | access.redhat.com or Red Hat Satellite or Katello password |
| **pool**  string | Specify a subscription pool name to consume. Regular expressions accepted. Use *pool_ids* instead if  possible, as it is much faster. Mutually exclusive with *pool_ids*.  Default: `"^$"` |
| **pool_ids**  list / elements=any | Specify subscription pool IDs to consume. Prefer over *pool* when possible as it is much faster.  A pool ID may be specified as a `string` - just the pool ID (ex. `0123456789abcdef0123456789abcdef`), or as a `dict` with the pool ID as the key, and a quantity as the value (ex. `0123456789abcdef0123456789abcdef: 2`. If the quantity is provided, it is used to consume multiple entitlements from a pool (the pool must support this). Mutually exclusive with *pool*.  Default: `[]` |
| **release**  string | Set a release version |
| **rhsm_baseurl**  string | Specify CDN baseurl |
| **rhsm_repo_ca_cert**  string | Specify an alternative location for a CA certificate for CDN |
| **server_hostname**  string | Specify an alternative Red Hat Subscription Management or Red Hat Satellite or Katello server |
| **server_insecure**  string | Enable or disable https server certificate verification when connecting to `server_hostname` |
| **server_port**  string  added in community.general 3.3.0 | Specify the port when registering to the Red Hat Subscription Management or Red Hat Satellite or Katello server. |
| **server_prefix**  string  added in community.general 3.3.0 | Specify the prefix when registering to the Red Hat Subscription Management or Red Hat Satellite or Katello server. |
| **server_proxy_hostname**  string | Specify an HTTP proxy hostname. |
| **server_proxy_password**  string | Specify a password for HTTP proxy with basic authentication |
| **server_proxy_port**  string | Specify an HTTP proxy port. |
| **server_proxy_user**  string | Specify a user for HTTP proxy with basic authentication |
| **state**  string | whether to register and subscribe (`present`), or unregister (`absent`) a system  Choices:   - `"present"` ← (default) - `"absent"` |
| **syspurpose**  dictionary | Set syspurpose attributes in file `/etc/rhsm/syspurpose/syspurpose.json` and synchronize these attributes with RHSM server. Syspurpose attributes help attach the most appropriate subscriptions to the system automatically. When `syspurpose.json` file already contains some attributes, then new attributes overwrite existing attributes. When some attribute is not listed in the new list of attributes, the existing attribute will be removed from `syspurpose.json` file. Unknown attributes are ignored. |
| **addons**  list / elements=string | Syspurpose attribute addons |
| **role**  string | Syspurpose attribute role |
| **service_level_agreement**  string | Syspurpose attribute service_level_agreement |
| **sync**  boolean | When this option is true, then syspurpose attributes are synchronized with RHSM server immediately. When this option is false, then syspurpose attributes will be synchronized with RHSM server by rhsmcertd daemon.  Choices:   - `false` ← (default) - `true` |
| **usage**  string | Syspurpose attribute usage |
| **username**  string | access.redhat.com or Red Hat Satellite or Katello username |

## [Notes](redhat_subscription_module.md#id4)

> **Note:**
>
> - In order to register a system, subscription-manager requires either a username and password, or an activationkey and an Organization ID.
> - Since 2.5 values for *server_hostname*, *server_insecure*, *rhsm_baseurl*, *server_proxy_hostname*, *server_proxy_port*, *server_proxy_user* and *server_proxy_password* are no longer taken from the `/etc/rhsm/rhsm.conf` config file and default to None.

## [Examples](redhat_subscription_module.md#id5)

```yaml+jinja
- name: Register as user (joe_user) with password (somepass) and auto-subscribe to available content.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    auto_attach: true

- name: Same as above but subscribe to a specific pool by ID.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids: 0123456789abcdef0123456789abcdef

- name: Register and subscribe to multiple pools.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids:
      - 0123456789abcdef0123456789abcdef
      - 1123456789abcdef0123456789abcdef

- name: Same as above but consume multiple entitlements.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    pool_ids:
      - 0123456789abcdef0123456789abcdef: 2
      - 1123456789abcdef0123456789abcdef: 4

- name: Register and pull existing system data.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    consumer_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

- name: Register with activationkey and consume subscriptions matching Red Hat Enterprise Server or Red Hat Virtualization
  community.general.redhat_subscription:
    state: present
    activationkey: 1-222333444
    org_id: 222333444
    pool: '^(Red Hat Enterprise Server|Red Hat Virtualization)$'

- name: Update the consumed subscriptions from the previous example (remove Red Hat Virtualization subscription)
  community.general.redhat_subscription:
    state: present
    activationkey: 1-222333444
    org_id: 222333444
    pool: '^Red Hat Enterprise Server$'

- name: Register as user credentials into given environment (against Red Hat Satellite or Katello), and auto-subscribe.
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    environment: Library
    auto_attach: true

- name: Register as user (joe_user) with password (somepass) and a specific release
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    release: 7.4

- name: Register as user (joe_user) with password (somepass), set syspurpose attributes and synchronize them with server
  community.general.redhat_subscription:
    state: present
    username: joe_user
    password: somepass
    auto_attach: true
    syspurpose:
      usage: "Production"
      role: "Red Hat Enterprise Server"
      service_level_agreement: "Premium"
      addons:
        - addon1
        - addon2
      sync: true
```

## [Return Values](redhat_subscription_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **subscribed_pool_ids**  complex | List of pool IDs to which system is now subscribed  Returned: success  Sample: `{"8a85f9815ab905d3015ab928c7005de4": "1"}` |

### Authors

- Barnaby Court (@barnabycourt)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
