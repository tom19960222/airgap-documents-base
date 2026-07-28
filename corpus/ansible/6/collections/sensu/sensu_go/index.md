---
collection: ansible
version: "6"
title: "Sensu.Sensu_Go"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/index.html
fetched_at: 2026-07-27T16:42:09+00:00
---
# Sensu.Sensu_Go

Collection version 1.13.1

- [Description](index.md#description)
- [Plugin Index](index.md#plugin-index)
- [Role Index](index.md#role-index)

## [Description](index.md#id1)

Roles and modules for installing and using Sensu Go

**Authors:**

- Paul Arthur <[paul.arthur@flowerysong.com](mailto:paul.arthur%40flowerysong.com)> (@flowerysong)
- XLAB Steampunk <[steampunk@xlab.si](mailto:steampunk%40xlab.si)>

**Supported ansible-core versions:**

- 2.9.0 or newer

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)

## [Plugin Index](index.md#id2)

These are the plugins in the sensu.sensu_go collection:

### Modules

- [ad_auth_provider module](ad_auth_provider_module.md#ansible-collections-sensu-sensu-go-ad-auth-provider-module) – Manage Sensu AD authentication provider
- [asset module](asset_module.md#ansible-collections-sensu-sensu-go-asset-module) – Manage Sensu assets
- [asset_info module](asset_info_module.md#ansible-collections-sensu-sensu-go-asset-info-module) – List Sensu assets
- [auth_provider_info module](auth_provider_info_module.md#ansible-collections-sensu-sensu-go-auth-provider-info-module) – List Sensu authentication providers
- [bonsai_asset module](bonsai_asset_module.md#ansible-collections-sensu-sensu-go-bonsai-asset-module) – Add Sensu assets from Bonsai
- [check module](check_module.md#ansible-collections-sensu-sensu-go-check-module) – Manage Sensu checks
- [check_info module](check_info_module.md#ansible-collections-sensu-sensu-go-check-info-module) – List Sensu checks
- [cluster module](cluster_module.md#ansible-collections-sensu-sensu-go-cluster-module) – Manage Sensu Go clusters
- [cluster_info module](cluster_info_module.md#ansible-collections-sensu-sensu-go-cluster-info-module) – List available Sensu Go clusters
- [cluster_role module](cluster_role_module.md#ansible-collections-sensu-sensu-go-cluster-role-module) – Manage Sensu cluster roles
- [cluster_role_binding module](cluster_role_binding_module.md#ansible-collections-sensu-sensu-go-cluster-role-binding-module) – Manage Sensu cluster role bindings
- [cluster_role_binding_info module](cluster_role_binding_info_module.md#ansible-collections-sensu-sensu-go-cluster-role-binding-info-module) – List Sensu cluster role bindings
- [cluster_role_info module](cluster_role_info_module.md#ansible-collections-sensu-sensu-go-cluster-role-info-module) – List Sensu cluster roles
- [datastore module](datastore_module.md#ansible-collections-sensu-sensu-go-datastore-module) – Manage Sensu external datastore providers
- [datastore_info module](datastore_info_module.md#ansible-collections-sensu-sensu-go-datastore-info-module) – List external Sensu datastore providers
- [entity module](entity_module.md#ansible-collections-sensu-sensu-go-entity-module) – Manage Sensu entities
- [entity_info module](entity_info_module.md#ansible-collections-sensu-sensu-go-entity-info-module) – List Sensu entities
- [etcd_replicator module](etcd_replicator_module.md#ansible-collections-sensu-sensu-go-etcd-replicator-module) – Manage Sensu Go etcd replicators
- [etcd_replicator_info module](etcd_replicator_info_module.md#ansible-collections-sensu-sensu-go-etcd-replicator-info-module) – List available Sensu Go etcd replicators
- [event module](event_module.md#ansible-collections-sensu-sensu-go-event-module) – Manage Sensu events
- [event_info module](event_info_module.md#ansible-collections-sensu-sensu-go-event-info-module) – List Sensu events
- [filter module](filter_module.md#ansible-collections-sensu-sensu-go-filter-module) – Manage Sensu filters
- [filter_info module](filter_info_module.md#ansible-collections-sensu-sensu-go-filter-info-module) – List Sensu info
- [handler_info module](handler_info_module.md#ansible-collections-sensu-sensu-go-handler-info-module) – List Sensu handlers
- [handler_set module](handler_set_module.md#ansible-collections-sensu-sensu-go-handler-set-module) – Manage Sensu handler set
- [hook module](hook_module.md#ansible-collections-sensu-sensu-go-hook-module) – Manage Sensu hooks
- [hook_info module](hook_info_module.md#ansible-collections-sensu-sensu-go-hook-info-module) – List Sensu hooks
- [ldap_auth_provider module](ldap_auth_provider_module.md#ansible-collections-sensu-sensu-go-ldap-auth-provider-module) – Manage Sensu LDAP authentication provider
- [mutator module](mutator_module.md#ansible-collections-sensu-sensu-go-mutator-module) – Manage Sensu mutators
- [mutator_info module](mutator_info_module.md#ansible-collections-sensu-sensu-go-mutator-info-module) – List Sensu mutators
- [namespace module](namespace_module.md#ansible-collections-sensu-sensu-go-namespace-module) – Manage Sensu namespaces
- [namespace_info module](namespace_info_module.md#ansible-collections-sensu-sensu-go-namespace-info-module) – List Sensu namespaces
- [oidc_auth_provider module](oidc_auth_provider_module.md#ansible-collections-sensu-sensu-go-oidc-auth-provider-module) – Manage Sensu OIDC authentication provider
- [pipe_handler module](pipe_handler_module.md#ansible-collections-sensu-sensu-go-pipe-handler-module) – Manage Sensu pipe handler
- [role module](role_module.md#ansible-collections-sensu-sensu-go-role-module) – Manage Sensu roles
- [role_binding module](role_binding_module.md#ansible-collections-sensu-sensu-go-role-binding-module) – Manage Sensu role bindings
- [role_binding_info module](role_binding_info_module.md#ansible-collections-sensu-sensu-go-role-binding-info-module) – List Sensu role bindings
- [role_info module](role_info_module.md#ansible-collections-sensu-sensu-go-role-info-module) – List Sensu roles
- [secret module](secret_module.md#ansible-collections-sensu-sensu-go-secret-module) – Manage Sensu Go secrets
- [secret_info module](secret_info_module.md#ansible-collections-sensu-sensu-go-secret-info-module) – List available Sensu Go secrets
- [secrets_provider_env module](secrets_provider_env_module.md#ansible-collections-sensu-sensu-go-secrets-provider-env-module) – Manage Sensu Env secrets provider
- [secrets_provider_info module](secrets_provider_info_module.md#ansible-collections-sensu-sensu-go-secrets-provider-info-module) – List Sensu secrets providers
- [secrets_provider_vault module](secrets_provider_vault_module.md#ansible-collections-sensu-sensu-go-secrets-provider-vault-module) – Manage Sensu VaultProvider secrets providers
- [silence module](silence_module.md#ansible-collections-sensu-sensu-go-silence-module) – Manage Sensu silences
- [silence_info module](silence_info_module.md#ansible-collections-sensu-sensu-go-silence-info-module) – List Sensu silence entries
- [socket_handler module](socket_handler_module.md#ansible-collections-sensu-sensu-go-socket-handler-module) – Manage Sensu TCP/UDP handler
- [tessen module](tessen_module.md#ansible-collections-sensu-sensu-go-tessen-module) – Manage Sensu’s Tessen configuration
- [user module](user_module.md#ansible-collections-sensu-sensu-go-user-module) – Manage Sensu users
- [user_info module](user_info_module.md#ansible-collections-sensu-sensu-go-user-info-module) – List Sensu users

## [Role Index](index.md#id3)

These are the roles in the sensu.sensu_go collection:

- [agent role](agent_role.md#ansible-collections-sensu-sensu-go-agent-role) – Install, configure, and start Sensu Go agent
- [backend role](backend_role.md#ansible-collections-sensu-sensu-go-backend-role) – Install, configure, and start Sensu Go backend
- [install role](install_role.md#ansible-collections-sensu-sensu-go-install-role) – Enable Sensu Go repos and install selected packages

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
