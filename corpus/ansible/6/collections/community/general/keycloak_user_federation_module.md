---
collection: ansible
version: "6"
title: "community.general.keycloak_user_federation module – Allows administration of Keycloak user federations via Keycloak API"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/keycloak_user_federation_module.html
fetched_at: 2026-07-27T17:10:23+00:00
---
# community.general.keycloak_user_federation module – Allows administration of Keycloak user federations via Keycloak API

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.keycloak_user_federation`.

New in community.general 3.7.0

- [Synopsis](keycloak_user_federation_module.md#synopsis)
- [Parameters](keycloak_user_federation_module.md#parameters)
- [Examples](keycloak_user_federation_module.md#examples)
- [Return Values](keycloak_user_federation_module.md#return-values)

## [Synopsis](keycloak_user_federation_module.md#id1)

- This module allows you to add, remove or modify Keycloak user federations via the Keycloak REST API. It requires access to the REST API via OpenID Connect; the user connecting and the client being used must have the requisite access rights. In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with the scope tailored to your needs and a user having the expected roles.
- The names of module options are snake_cased versions of the camelCase ones found in the Keycloak API and its documentation at <https://www.keycloak.org/docs-api/15.0/rest-api/index.html>.

## [Parameters](keycloak_user_federation_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_client_id**  string | OpenID Connect *client_id* to authenticate to the API with.  Default: `"admin-cli"` |
| **auth_client_secret**  string | Client Secret to use in conjunction with *auth_client_id* (if required). |
| **auth_keycloak_url**  aliases: url  string / required | URL to the Keycloak instance. |
| **auth_password**  aliases: password  string | Password to authenticate for API access with. |
| **auth_realm**  string | Keycloak realm name to authenticate to for API access. |
| **auth_username**  aliases: username  string | Username to authenticate for API access with. |
| **config**  dictionary | Dict specifying the configuration options for the provider; the contents differ depending on the value of *provider_id*. Examples are given below for `ldap`, `kerberos` and `sssd`. It is easiest to obtain valid config values by dumping an already-existing user federation configuration through check-mode in the *existing* field.  The value `sssd` has been supported since community.general 4.2.0. |
| **allowKerberosAuthentication**  boolean | Enable/disable HTTP authentication of users with SPNEGO/Kerberos tokens. The data about authenticated users will be provisioned from this LDAP server.  Choices:   - `false` ← (default) - `true` |
| **allowPasswordAuthentication**  boolean | Enable/disable possibility of username/password authentication against Kerberos database.  Choices:   - `false` - `true` |
| **authType**  string | Type of the Authentication method used during LDAP Bind operation. It is used in most of the requests sent to the LDAP server.  Choices:   - `"none"` ← (default) - `"simple"` |
| **batchSizeForSync**  integer | Count of LDAP users to be imported from LDAP to Keycloak within a single transaction.  Default: `1000` |
| **bindCredential**  string | Password of LDAP admin. |
| **bindDn**  string | DN of LDAP user which will be used by Keycloak to access LDAP server. |
| **cachePolicy**  string | Cache Policy for this storage provider.  Choices:   - `"DEFAULT"` ← (default) - `"EVICT_DAILY"` - `"EVICT_WEEKLY"` - `"MAX_LIFESPAN"` - `"NO_CACHE"` |
| **changedSyncPeriod**  integer | Period for synchronization of changed or newly created LDAP users in seconds.  Default: `-1` |
| **connectionPooling**  boolean | Determines if Keycloak should use connection pooling for accessing LDAP server.  Choices:   - `false` - `true` ← (default) |
| **connectionPoolingAuthentication**  string | A list of space-separated authentication types of connections that may be pooled.  Choices:   - `"none"` - `"simple"` - `"DIGEST-MD5"` |
| **connectionPoolingDebug**  string | A string that indicates the level of debug output to produce. Example valid values are `fine` (trace connection creation and removal) and `all` (all debugging information). |
| **connectionPoolingInitSize**  integer | The number of connections per connection identity to create when initially creating a connection for the identity. |
| **connectionPoolingMaxSize**  integer | The maximum number of connections per connection identity that can be maintained concurrently. |
| **connectionPoolingPrefSize**  integer | The preferred number of connections per connection identity that should be maintained concurrently. |
| **connectionPoolingProtocol**  string | A list of space-separated protocol types of connections that may be pooled. Valid types are `plain` and `ssl`. |
| **connectionPoolingTimeout**  integer | The number of milliseconds that an idle connection may remain in the pool without being closed and removed from the pool. |
| **connectionTimeout**  integer | LDAP Connection Timeout in milliseconds. |
| **connectionUrl**  string | Connection URL to your LDAP server. |
| **customUserSearchFilter**  string | Additional LDAP Filter for filtering searched users. Leave this empty if you don’t need additional filter. |
| **debug**  boolean | Enable/disable debug logging to standard output for Krb5LoginModule.  Choices:   - `false` - `true` |
| **editMode**  string | `READ_ONLY` is a read-only LDAP store. `WRITABLE` means data will be synced back to LDAP on demand. `UNSYNCED` means user data will be imported, but not synced back to LDAP.  Choices:   - `"READ_ONLY"` - `"WRITABLE"` - `"UNSYNCED"` |
| **enabled**  boolean | Enable/disable this user federation.  Choices:   - `false` - `true` ← (default) |
| **evictionDay**  string | Day of the week the entry will become invalid on. |
| **evictionHour**  string | Hour of day the entry will become invalid on. |
| **evictionMinute**  string | Minute of day the entry will become invalid on. |
| **fullSyncPeriod**  integer | Period for full synchronization in seconds.  Default: `-1` |
| **importEnabled**  boolean | If `true`, LDAP users will be imported into Keycloak DB and synced by the configured sync policies.  Choices:   - `false` - `true` ← (default) |
| **kerberosRealm**  string | Name of kerberos realm. |
| **keyTab**  string | Location of Kerberos KeyTab file containing the credentials of server principal. For example `/etc/krb5.keytab`. |
| **maxLifespan**  integer | Max lifespan of cache entry in milliseconds. |
| **pagination**  boolean | Does the LDAP server support pagination.  Choices:   - `false` - `true` ← (default) |
| **priority**  integer | Priority of provider when doing a user lookup. Lowest first.  Default: `0` |
| **rdnLDAPAttribute**  string | Name of LDAP attribute, which is used as RDN (top attribute) of typical user DN. Usually it’s the same as Username LDAP attribute, however it is not required. For example for Active directory, it is common to use `cn` as RDN attribute when username attribute might be `sAMAccountName`. |
| **readTimeout**  integer | LDAP Read Timeout in milliseconds. This timeout applies for LDAP read operations. |
| **searchScope**  string | For one level, the search applies only for users in the DNs specified by User DNs. For subtree, the search applies to the whole subtree. See LDAP documentation for more details.  Choices:   - `"1"` ← (default) - `"2"` |
| **serverPrincipal**  string | Full name of server principal for HTTP service including server and domain name. For example `HTTP/host.foo.org@FOO.ORG`. Use `*` to accept any service principal in the KeyTab file. |
| **startTls**  boolean | Encrypts the connection to LDAP using STARTTLS, which will disable connection pooling.  Choices:   - `false` ← (default) - `true` |
| **syncRegistrations**  boolean | Should newly created users be created within LDAP store? Priority effects which provider is chosen to sync the new user.  Choices:   - `false` ← (default) - `true` |
| **trustEmail**  boolean | If enabled, email provided by this provider is not verified even if verification is enabled for the realm.  Choices:   - `false` ← (default) - `true` |
| **updateProfileFirstLogin**  boolean | Update profile on first login.  Choices:   - `false` - `true` |
| **useKerberosForPasswordAuthentication**  boolean | Use Kerberos login module for authenticate username/password against Kerberos server instead of authenticating against LDAP server with Directory Service API.  Choices:   - `false` ← (default) - `true` |
| **usePasswordModifyExtendedOp**  boolean | Use the LDAPv3 Password Modify Extended Operation (RFC-3062). The password modify extended operation usually requires that LDAP user already has password in the LDAP server. So when this is used with ‘Sync Registrations’, it can be good to add also ‘Hardcoded LDAP attribute mapper’ with randomly generated initial password.  Choices:   - `false` ← (default) - `true` |
| **usernameLDAPAttribute**  string | Name of LDAP attribute, which is mapped as Keycloak username. For many LDAP server vendors it can be `uid`. For Active directory it can be `sAMAccountName` or `cn`. The attribute should be filled for all LDAP user records you want to import from LDAP to Keycloak. |
| **userObjectClasses**  string | All values of LDAP objectClass attribute for users in LDAP divided by comma. For example `inetOrgPerson, organizationalPerson`. Newly created Keycloak users will be written to LDAP with all those object classes and existing LDAP user records are found just if they contain all those object classes. |
| **usersDn**  string | Full DN of LDAP tree where your users are. This DN is the parent of LDAP users. |
| **useTruststoreSpi**  string | Specifies whether LDAP connection will use the truststore SPI with the truststore configured in standalone.xml/domain.xml. `Always` means that it will always use it. `Never` means that it will not use it. `Only for ldaps` means that it will use if your connection URL use ldaps. Note even if standalone.xml/domain.xml is not configured, the default Java cacerts or certificate specified by `javax.net.ssl.trustStore` property will be used.  Choices:   - `"always"` - `"ldapsOnly"` ← (default) - `"never"` |
| **uuidLDAPAttribute**  string | Name of LDAP attribute, which is used as unique object identifier (UUID) for objects in LDAP. For many LDAP server vendors, it is `entryUUID`; however some are different. For example for Active directory it should be `objectGUID`. If your LDAP server does not support the notion of UUID, you can use any other attribute that is supposed to be unique among LDAP users in tree. |
| **validatePasswordPolicy**  boolean | Determines if Keycloak should validate the password with the realm password policy before updating it.  Choices:   - `false` ← (default) - `true` |
| **vendor**  string | LDAP vendor (provider).  Use short name. For instance, write `rhds` for “Red Hat Directory Server”. |
| **connection_timeout**  integer  added in community.general 4.5.0 | Controls the HTTP connections timeout period (in seconds) to Keycloak API.  Default: `10` |
| **http_agent**  string  added in community.general 5.4.0 | Configures the HTTP User-Agent header.  Default: `"Ansible"` |
| **id**  string | The unique ID for this user federation. If left empty, the user federation will be searched by its *name*. |
| **mappers**  list / elements=dictionary | A list of dicts defining mappers associated with this Identity Provider. |
| **config**  dictionary | Dict specifying the configuration options for the mapper; the contents differ depending on the value of *identityProviderMapper*. |
| **id**  string | Unique ID of this mapper. |
| **name**  string | Name of the mapper. If no ID is given, the mapper will be searched by name. |
| **parentId**  string | Unique ID for the parent of this mapper. ID of the user federation will automatically be used if left blank. |
| **providerId**  string | The mapper type for this mapper (for instance `user-attribute-ldap-mapper`). |
| **providerType**  string | Component type for this mapper (only supported value is `org.keycloak.storage.ldap.mappers.LDAPStorageMapper`). |
| **name**  string | Display name of provider when linked in admin console. |
| **parent_id**  aliases: parentId  string | Unique ID for the parent of this user federation. Realm ID will be automatically used if left blank. |
| **provider_id**  aliases: providerId  string | Provider for this user federation.  Choices:   - `"ldap"` - `"kerberos"` - `"sssd"` |
| **provider_type**  aliases: providerType  string | Component type for user federation (only supported value is `org.keycloak.storage.UserStorageProvider`).  Default: `"org.keycloak.storage.UserStorageProvider"` |
| **realm**  string | The Keycloak realm under which this user federation resides.  Default: `"master"` |
| **state**  string | State of the user federation.  On `present`, the user federation will be created if it does not yet exist, or updated with the parameters you provide.  On `absent`, the user federation will be removed if it exists.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string  added in community.general 3.0.0 | Authentication token for Keycloak API. |
| **validate_certs**  boolean | Verify TLS certificates (do not disable this in production).  Choices:   - `false` - `true` ← (default) |

## [Examples](keycloak_user_federation_module.md#id3)

```yaml+jinja
- name: Create LDAP user federation
  community.general.keycloak_user_federation:
    auth_keycloak_url: https://keycloak.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: my-realm
    name: my-ldap
    state: present
    provider_id: ldap
    provider_type: org.keycloak.storage.UserStorageProvider
    config:
      priority: 0
      enabled: true
      cachePolicy: DEFAULT
      batchSizeForSync: 1000
      editMode: READ_ONLY
      importEnabled: true
      syncRegistrations: false
      vendor: other
      usernameLDAPAttribute: uid
      rdnLDAPAttribute: uid
      uuidLDAPAttribute: entryUUID
      userObjectClasses: inetOrgPerson, organizationalPerson
      connectionUrl: ldaps://ldap.example.com:636
      usersDn: ou=Users,dc=example,dc=com
      authType: simple
      bindDn: cn=directory reader
      bindCredential: password
      searchScope: 1
      validatePasswordPolicy: false
      trustEmail: false
      useTruststoreSpi: ldapsOnly
      connectionPooling: true
      pagination: true
      allowKerberosAuthentication: false
      debug: false
      useKerberosForPasswordAuthentication: false
    mappers:
      - name: "full name"
        providerId: "full-name-ldap-mapper"
        providerType: "org.keycloak.storage.ldap.mappers.LDAPStorageMapper"
        config:
          ldap.full.name.attribute: cn
          read.only: true
          write.only: false

- name: Create Kerberos user federation
  community.general.keycloak_user_federation:
    auth_keycloak_url: https://keycloak.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: my-realm
    name: my-kerberos
    state: present
    provider_id: kerberos
    provider_type: org.keycloak.storage.UserStorageProvider
    config:
      priority: 0
      enabled: true
      cachePolicy: DEFAULT
      kerberosRealm: EXAMPLE.COM
      serverPrincipal: HTTP/host.example.com@EXAMPLE.COM
      keyTab: keytab
      allowPasswordAuthentication: false
      updateProfileFirstLogin: false

- name: Create sssd user federation
  community.general.keycloak_user_federation:
    auth_keycloak_url: https://keycloak.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: my-realm
    name: my-sssd
    state: present
    provider_id: sssd
    provider_type: org.keycloak.storage.UserStorageProvider
    config:
      priority: 0
      enabled: true
      cachePolicy: DEFAULT

- name: Delete user federation
  community.general.keycloak_user_federation:
    auth_keycloak_url: https://keycloak.example.com/auth
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: my-realm
    name: my-federation
    state: absent
```

## [Return Values](keycloak_user_federation_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **end_state**  dictionary | Representation of user federation after module execution.  Returned: on success  Sample: `{"config": {"allowPasswordAuthentication": "false", "cachePolicy": "DEFAULT", "enabled": "true", "kerberosRealm": "EXAMPLE.COM", "keyTab": "/etc/krb5.keytab", "priority": "0", "serverPrincipal": "HTTP/host.example.com@EXAMPLE.COM", "updateProfileFirstLogin": "false"}, "id": "cf52ae4f-4471-4435-a0cf-bb620cadc122", "mappers": [], "name": "kerberos", "parentId": "myrealm", "providerId": "kerberos", "providerType": "org.keycloak.storage.UserStorageProvider"}` |
| **existing**  dictionary | Representation of existing user federation.  Returned: always  Sample: `{"config": {"allowKerberosAuthentication": "false", "authType": "simple", "batchSizeForSync": "1000", "bindCredential": "**********", "bindDn": "cn=directory reader", "cachePolicy": "DEFAULT", "changedSyncPeriod": "-1", "connectionPooling": "true", "connectionUrl": "ldaps://ldap.example.com:636", "debug": "false", "editMode": "READ_ONLY", "enabled": "true", "fullSyncPeriod": "-1", "importEnabled": "true", "pagination": "true", "priority": "0", "rdnLDAPAttribute": "uid", "searchScope": "1", "syncRegistrations": "false", "trustEmail": "false", "useKerberosForPasswordAuthentication": "false", "useTruststoreSpi": "ldapsOnly", "userObjectClasses": "inetOrgPerson, organizationalPerson", "usernameLDAPAttribute": "uid", "usersDn": "ou=Users,dc=example,dc=com", "uuidLDAPAttribute": "entryUUID", "validatePasswordPolicy": "false", "vendor": "other"}, "id": "01122837-9047-4ae4-8ca0-6e2e891a765f", "mappers": [{"config": {"always.read.value.from.ldap": "false", "is.mandatory.in.ldap": "false", "ldap.attribute": "mail", "read.only": "true", "user.model.attribute": "email"}, "id": "17d60ce2-2d44-4c2c-8b1f-1fba601b9a9f", "name": "email", "parentId": "01122837-9047-4ae4-8ca0-6e2e891a765f", "providerId": "user-attribute-ldap-mapper", "providerType": "org.keycloak.storage.ldap.mappers.LDAPStorageMapper"}], "name": "myfed", "parentId": "myrealm", "providerId": "ldap", "providerType": "org.keycloak.storage.UserStorageProvider"}` |
| **msg**  string | Message as to what action was taken.  Returned: always  Sample: `"No changes required to user federation 164bb483-c613-482e-80fe-7f1431308799."` |
| **proposed**  dictionary | Representation of proposed user federation.  Returned: always  Sample: `{"config": {"allowKerberosAuthentication": "false", "authType": "simple", "batchSizeForSync": "1000", "bindCredential": "**********", "bindDn": "cn=directory reader", "cachePolicy": "DEFAULT", "connectionPooling": "true", "connectionUrl": "ldaps://ldap.example.com:636", "debug": "false", "editMode": "READ_ONLY", "enabled": "true", "importEnabled": "true", "pagination": "true", "priority": "0", "rdnLDAPAttribute": "uid", "searchScope": "1", "syncRegistrations": "false", "trustEmail": "false", "useKerberosForPasswordAuthentication": "false", "useTruststoreSpi": "ldapsOnly", "userObjectClasses": "inetOrgPerson, organizationalPerson", "usernameLDAPAttribute": "uid", "usersDn": "ou=Users,dc=example,dc=com", "uuidLDAPAttribute": "entryUUID", "validatePasswordPolicy": "false", "vendor": "other"}, "name": "ldap", "providerId": "ldap", "providerType": "org.keycloak.storage.UserStorageProvider"}` |

### Authors

- Laurent Paumier (@laurpaum)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
