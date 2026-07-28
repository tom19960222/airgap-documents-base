---
collection: ansible
version: "6"
title: "sensu.sensu_go.ad_auth_provider module – Manage Sensu AD authentication provider"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/ad_auth_provider_module.html
fetched_at: 2026-07-28T00:19:18+00:00
---
# sensu.sensu_go.ad_auth_provider module – Manage Sensu AD authentication provider

> **Note:**
>
> This module is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install sensu.sensu_go`.
> You need further requirements to be able to use this module,
> see [Requirements](ad_auth_provider_module.md#ansible-collections-sensu-sensu-go-ad-auth-provider-module-requirements) for details.
>
> To use it in a playbook, specify: `sensu.sensu_go.ad_auth_provider`.

New in sensu.sensu_go 1.10.0

- [Synopsis](ad_auth_provider_module.md#synopsis)
- [Requirements](ad_auth_provider_module.md#requirements)
- [Parameters](ad_auth_provider_module.md#parameters)
- [See Also](ad_auth_provider_module.md#see-also)
- [Examples](ad_auth_provider_module.md#examples)
- [Return Values](ad_auth_provider_module.md#return-values)

## [Synopsis](ad_auth_provider_module.md#id1)

- Create, update or delete a Sensu Go AD authentication provider.
- For more information, refer to the Sensu Go documentation at <https://docs.sensu.io/sensu-go/latest/operations/control-access/ad-auth/>.

## [Requirements](ad_auth_provider_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7

## [Parameters](ad_auth_provider_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **auth**  dictionary | Authentication parameters. Can define each of them with ENV as well. |
| **api_key**  string  added in sensu.sensu_go 1.3.0 | The API key that should be used when authenticating. If this is not set, the value of the SENSU_API_KEY environment variable will be checked.  This replaces *auth.user* and *auth.password* parameters.  For more information about the API key, refer to the official Sensu documentation at <https://docs.sensu.io/sensu-go/latest/guides/use-apikey-feature/>. |
| **ca_path**  path  added in sensu.sensu_go 1.5.0 | Path to the CA bundle that should be used to validate the backend certificate.  If this parameter is not set, module will use the CA bundle that python is using.  It is also possible to set this parameter via the *SENSU_CA_PATH* environment variable. |
| **password**  string | The Sensu user’s password. If this is not set the value of the SENSU_PASSWORD environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"P@ssw0rd!"` |
| **url**  string | Location of the Sensu backend API. If this is not set the value of the SENSU_URL environment variable will be checked.  Default: `"http://localhost:8080"` |
| **user**  string | The username to use for connecting to the Sensu API. If this is not set the value of the SENSU_USER environment variable will be checked.  This parameter is ignored if the *auth.api_key* parameter is set.  Default: `"admin"` |
| **verify**  boolean  added in sensu.sensu_go 1.5.0 | Flag that controls the certificate validation.  If you are using self-signed certificates, you can set this parameter to `false`.  ONLY USE THIS PARAMETER IN DEVELOPMENT SCENARIOS! In you use self-signed certificates in production, see the *auth.ca_path* parameter.  It is also possible to set this parameter via the *SENSU_VERIFY* environment variable.  Choices:   - `false` - `true` ← (default) |
| **groups_prefix**  string | The prefix added to all AD groups. |
| **name**  string / required | The Sensu resource’s name. This name (in combination with the namespace where applicable) uniquely identifies the resource that Ansible operates on.  If the resource with selected name already exists, Ansible module will update it to match the specification in the task.  Consult the *name* metadata attribute specification in the upstream docs on <https://docs.sensu.io/sensu-go/latest/reference/> for more details about valid names and other restrictions. |
| **servers**  list / elements=dictionary | An array of AD servers for your directory. |
| **binding**  dictionary | The AD account that performs user and group lookups.  If your sever supports anonymous binding, you can omit the user_dn or password attributes to query the directory without credentials. |
| **password**  string / required | Password for the user_dn account.  If your sever supports anonymous binding, you can omit this attribute. |
| **user_dn**  string / required | The AD account that performs user and group lookups.  If your sever supports anonymous binding, you can omit this attribute. |
| **client_cert_file**  string | Path to the certificate that should be sent to the server if requested. |
| **client_key_file**  string | Path to the key file associated with the client_cert_file.  Required if *client_cert_file* is present. |
| **default_upn_domain**  string | Enables UPN authentication when set. The default UPN suffix that will be appended to the username when a domain is not specified during login (for example, user becomes [user@defaultdomain.xyz](mailto:user%40defaultdomain.xyz)). |
| **group_search**  dictionary | Search configuration for groups. |
| **attribute**  string | Used for comparing result entries.  Default: `"member"` |
| **base_dn**  string / required | Which part of the directory tree to search. |
| **name_attribute**  string | Represents the attribute to use as the entry name.  Default: `"cn"` |
| **object_class**  string | Identifies the class of objects returned in the search result.  Default: `"group"` |
| **host**  string / required | AD server IP address. |
| **include_nested_groups**  boolean | If true, the group search includes any nested groups a user is a member of. If false, the group search includes only the top-level groups a user is a member of.  Choices:   - `false` - `true` |
| **insecure**  boolean | Skips SSL certificate verification when set to true.  Choices:   - `false` ← (default) - `true` |
| **port**  integer | AD server port. |
| **security**  string | Encryption type to be used for the connection to the AD server.  Choices:   - `"insecure"` - `"tls"` ← (default) - `"starttls"` |
| **trusted_ca_file**  string | Path to an alternative CA bundle file. |
| **user_search**  dictionary | Search configuration for users. |
| **attribute**  string | Used for comparing result entries.  Default: `"sAMAccountName"` |
| **base_dn**  string / required | Which part of the directory tree to search. |
| **name_attribute**  string | Represents the attribute to use as the entry name.  Default: `"displayName"` |
| **object_class**  string | Identifies the class of objects returned in the search result.  Default: `"person"` |
| **state**  string | Target state of the Sensu object.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username_prefix**  string | The prefix added to all AD usernames. |

## [See Also](ad_auth_provider_module.md#id4)

> **See also:**
>
> [sensu.sensu_go.auth_provider_info](auth_provider_info_module.md#ansible-collections-sensu-sensu-go-auth-provider-info-module)
> :   List Sensu authentication providers.
>
> [sensu.sensu_go.ldap_auth_provider](ldap_auth_provider_module.md#ansible-collections-sensu-sensu-go-ldap-auth-provider-module)
> :   Manage Sensu LDAP authentication provider.
>
> [sensu.sensu_go.oidc_auth_provider](oidc_auth_provider_module.md#ansible-collections-sensu-sensu-go-oidc-auth-provider-module)
> :   Manage Sensu OIDC authentication provider.

## [Examples](ad_auth_provider_module.md#id5)

```yaml+jinja
- name: Create a AD auth provider
  sensu.sensu_go.ad_auth_provider:
    name: activedirectory
    servers:
      - host: 127.0.0.1
        group_search:
          base_dn: dc=acme,dc=org
        user_search:
          base_dn: dc=acme,dc=org
- name: Delete a AD auth provider
  sensu.sensu_go.ad_auth_provider:
    name: activedirectory
    state: absent
```

## [Return Values](ad_auth_provider_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **object**  dictionary | Object representing Sensu AD authentication provider.  Returned: success  Sample: `{"groups_prefix": "AD", "metadata": {"name": "activedirectory"}, "servers": {"binding": {"user_dn": "cn=binder,dc=acme,dc=org"}, "client_cert_file": "/path/to/ssl/cert.pem", "client_key_file": "/path/to/ssl/key.pem", "default_upn_domain": "example.org", "group_search": {"attribute": "member", "base_dn": "dc=acme,dc=org", "name_attribute'": "cn", "object_class": "group"}, "host": "127.0.0.1", "insecure": "False", "port": "636", "security": "tls", "trusted_ca_file": "/path/to/trusted-certificate-authorities.pem", "user_search": {"attribute": "sAMAccountName", "base_dn": "dc=acme,dc=org", "name_attribute": "displayName", "object_class": "person"}}, "username_prefix": "AD"}` |

### Authors

- Aljaz Kosir (@aljazkosir)
- Manca Bizjak (@mancabizjak)
- Miha Dolinar (@mdolin)
- Tadej Borovsak (@tadeboro)

### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
