---
collection: ansible
version: "6"
title: "community.okd.openshift_adm_groups_sync module – Sync OpenShift Groups with records from an external provider."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_adm_groups_sync_module.html
fetched_at: 2026-07-27T17:20:08+00:00
---
# community.okd.openshift_adm_groups_sync module – Sync OpenShift Groups with records from an external provider.

> **Note:**
>
> This module is part of the [community.okd collection](https://galaxy.ansible.com/community/okd) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.okd`.
> You need further requirements to be able to use this module,
> see [Requirements](openshift_adm_groups_sync_module.md#ansible-collections-community-okd-openshift-adm-groups-sync-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_adm_groups_sync`.

New in community.okd 2.1.0

- [Synopsis](openshift_adm_groups_sync_module.md#synopsis)
- [Requirements](openshift_adm_groups_sync_module.md#requirements)
- [Parameters](openshift_adm_groups_sync_module.md#parameters)
- [Notes](openshift_adm_groups_sync_module.md#notes)
- [Examples](openshift_adm_groups_sync_module.md#examples)
- [Return Values](openshift_adm_groups_sync_module.md#return-values)

## [Synopsis](openshift_adm_groups_sync_module.md#id1)

- In order to sync/prune OpenShift Group records with those from an external provider, determine which Groups you wish to sync and where their records live.
- Analogous to `oc adm prune groups` and `oc adm group sync`.
- LDAP sync configuration file syntax can be found here <https://docs.openshift.com/container-platform/4.9/authentication/ldap-syncing.html>.
- The bindPassword attribute of the LDAP sync configuration is expected to be a string, please use ansible-vault encryption to secure this information.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](openshift_adm_groups_sync_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- kubernetes >= 12.0.0
- python-ldap

## [Parameters](openshift_adm_groups_sync_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **allow_groups**  list / elements=string | Allowed groups, could be openshift group name or LDAP group dn value.  When parameter `type` is set to *ldap* this should contains only LDAP group definition like *cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat*. |
| **api_key**  string | Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable. |
| **client_cert**  aliases: cert_file  path | Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable. |
| **client_key**  aliases: key_file  path | Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment variable. |
| **context**  string | The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable. |
| **deny_groups**  list / elements=string | Denied groups, could be openshift group name or LDAP group dn value.  When parameter `type` is set to *ldap* this should contains only LDAP group definition like *cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat*.  The elements specified in this list will override the ones specified in `allow_groups`. |
| **host**  string | Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable. |
| **impersonate_groups**  list / elements=string  added in kubernetes.core 2.3.0 | Group(s) to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_GROUPS environment. Example: Group1,Group2 |
| **impersonate_user**  string  added in kubernetes.core 2.3.0 | Username to impersonate for the operation.  Can also be specified via K8S_AUTH_IMPERSONATE_USER environment. |
| **kubeconfig**  any | Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the Kubernetes client will attempt to load the default configuration file from *~/.kube/config*. Can also be specified via K8S_AUTH_KUBECONFIG environment variable.  The kubernetes configuration can be provided as dictionary. This feature requires a python kubernetes client version >= 17.17.0. Added in version 2.2.0. |
| **no_proxy**  string  added in kubernetes.core 2.3.0 | The comma separated list of hosts/domains/IP/CIDR that shouldn’t go through proxy. Can also be specified via K8S_AUTH_NO_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. NO_PROXY).  This feature requires kubernetes>=19.15.0. When kubernetes library is less than 19.15.0, it fails even no_proxy set in correct.  example value is “localhost,.local,.example.com,127.0.0.1,127.0.0.0/8,10.0.0.0/8,172.16.0.0/12,192.168.0.0/16” |
| **password**  string | Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.  Please read the description of the `username` option for a discussion of when this option is applicable. |
| **persist_config**  boolean | Whether or not to save the kube config refresh tokens. Can also be specified via K8S_AUTH_PERSIST_CONFIG environment variable.  When the k8s context is using a user credentials with refresh tokens (like oidc or gke/gcloud auth), the token is refreshed by the k8s python client library but not saved by default. So the old refresh token can expire and the next auth might fail. Setting this flag to true will tell the k8s python client to save the new refresh token to the kube config file.  Default to false.  Please note that the current version of the k8s python client library does not support setting this flag to True yet.  The fix for this k8s python library is here: <https://github.com/kubernetes-client/python-base/pull/169>  Choices:   - `false` - `true` |
| **proxy**  string | The URL of an HTTP proxy to use for the connection. Can also be specified via K8S_AUTH_PROXY environment variable.  Please note that this module does not pick up typical proxy settings from the environment (e.g. HTTP_PROXY). |
| **proxy_headers**  dictionary  added in kubernetes.core 2.0.0 | The Header used for the HTTP proxy.  Documentation can be found here <https://urllib3.readthedocs.io/en/latest/reference/urllib3.util.html?highlight%3Dproxy_headers#urllib3.util.make_headers>. |
| **basic_auth**  string | Colon-separated username:password for basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_BASIC_AUTH environment. |
| **proxy_basic_auth**  string | Colon-separated username:password for proxy basic authentication header.  Can also be specified via K8S_AUTH_PROXY_HEADERS_PROXY_BASIC_AUTH environment. |
| **user_agent**  string | String representing the user-agent you want, such as foo/1.0.  Can also be specified via K8S_AUTH_PROXY_HEADERS_USER_AGENT environment. |
| **state**  string | Determines if the group should be sync when set to `present` or pruned when set to `absent`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **sync_config**  aliases: config, src  dictionary / required | Provide a valid YAML definition of an LDAP sync configuration. |
| **type**  string | which groups allow and deny list entries refer to.  Choices:   - `"ldap"` ← (default) - `"openshift"` |
| **username**  string | Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.  Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you should look into the [community.okd.k8s_auth](k8s_auth_module.md#ansible-collections-community-okd-k8s-auth-module) module, as that might do what you need. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable.  Choices:   - `false` - `true` |

## [Notes](openshift_adm_groups_sync_module.md#id4)

> **Note:**
>
> - To avoid SSL certificate validation errors when `validate_certs` is *True*, the full certificate chain for the API server must be provided via `ca_cert` or in the kubeconfig file.

## [Examples](openshift_adm_groups_sync_module.md#id5)

```yaml+jinja
# Prune all orphaned groups
- name: Prune all orphan groups
  openshift_adm_groups_sync:
    state: absent
    src: "{{ lookup('file', '/path/to/ldap-sync-config.yaml') | from_yaml }}"

# Prune all orphaned groups from a list of specific groups specified in allow_groups
- name: Prune all orphan groups from a list of specific groups specified in allow_groups
  openshift_adm_groups_sync:
    state: absent
    src: "{{ lookup('file', '/path/to/ldap-sync-config.yaml') | from_yaml }}"
    allow_groups:
      - cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat
      - cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat

# Sync all groups from an LDAP server
- name: Sync all groups from an LDAP server
  openshift_adm_groups_sync:
    src:
        kind: LDAPSyncConfig
        apiVersion: v1
        url: ldap://localhost:1390
        insecure: true
        bindDN: cn=admin,dc=example,dc=org
        bindPassword: adminpassword
        rfc2307:
            groupsQuery:
                baseDN: "cn=admins,ou=groups,dc=example,dc=org"
                scope: sub
                derefAliases: never
                filter: (objectClass=*)
                pageSize: 0
            groupUIDAttribute: dn
            groupNameAttributes: [ cn ]
            groupMembershipAttributes: [ member ]
            usersQuery:
                baseDN: "ou=users,dc=example,dc=org"
                scope: sub
                derefAliases: never
                pageSize: 0
            userUIDAttribute: dn
            userNameAttributes: [ mail ]
            tolerateMemberNotFoundErrors: true
            tolerateMemberOutOfScopeErrors: true

# Sync all groups except the ones from the deny_groups  from an LDAP server
- name: Sync all groups from an LDAP server using deny_groups
  openshift_adm_groups_sync:
    src: "{{ lookup('file', '/path/to/ldap-sync-config.yaml') | from_yaml }}"
    deny_groups:
      - cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat
      - cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat

# Sync all OpenShift Groups that have been synced previously with an LDAP server
- name: Sync all OpenShift Groups that have been synced previously with an LDAP server
  openshift_adm_groups_sync:
    src: "{{ lookup('file', '/path/to/ldap-sync-config.yaml') | from_yaml }}"
    type: openshift
```

## [Return Values](openshift_adm_groups_sync_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **builds**  list / elements=dictionary | The groups that were created, updated or deleted  Returned: success  Sample: `[{"apiVersion": "user.openshift.io/v1", "kind": "Group", "metadata": {"annotations": {"openshift.io/ldap.sync-time": "2021-12-17T12:20:28.125282", "openshift.io/ldap.uid": "cn=developers,ou=groups,ou=rfc2307,dc=ansible,dc=redhat", "openshift.io/ldap.url": "localhost:1390"}, "creationTimestamp": "2021-12-17T11:09:49Z", "labels": {"openshift.io/ldap.host": "localhost"}, "managedFields": [{"apiVersion": "user.openshift.io/v1", "fieldsType": "FieldsV1", "fieldsV1": {"f:metadata": {"f:annotations": {".": {}, "f:openshift.io/ldap.sync-time": {}, "f:openshift.io/ldap.uid": {}, "f:openshift.io/ldap.url": {}}, "f:labels": {".": {}, "f:openshift.io/ldap.host": {}}}, "f:users": {}}, "manager": "OpenAPI-Generator", "operation": "Update", "time": "2021-12-17T11:09:49Z"}], "name": "developers", "resourceVersion": "2014696", "uid": "8dc211cb-1544-41e1-96b1-efffeed2d7d7"}, "users": ["jordanbulls@ansible.org"]}]` |

### Authors

- Aubin Bikouo (@abikouo)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
