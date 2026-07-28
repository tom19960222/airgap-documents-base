---
collection: ansible
version: "6"
title: "community.general.tss lookup – Get secrets from Thycotic Secret Server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/tss_lookup.html
fetched_at: 2026-07-27T17:15:14+00:00
---
# community.general.tss lookup – Get secrets from Thycotic Secret Server

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](tss_lookup.md#ansible-collections-community-general-tss-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.tss`.

New in community.general 1.0.0

- [Synopsis](tss_lookup.md#synopsis)
- [Requirements](tss_lookup.md#requirements)
- [Terms](tss_lookup.md#terms)
- [Keyword parameters](tss_lookup.md#keyword-parameters)
- [Notes](tss_lookup.md#notes)
- [Examples](tss_lookup.md#examples)
- [Return Value](tss_lookup.md#return-value)

## [Synopsis](tss_lookup.md#id1)

- Uses the Thycotic Secret Server Python SDK to get Secrets from Secret Server using token authentication with *username* and *password* on the REST API at *base_url*.
- When using self-signed certificates the environment variable `REQUESTS_CA_BUNDLE` can be set to a file containing the trusted certificates (in `.pem` format).
- For example, `export REQUESTS_CA_BUNDLE='/etc/ssl/certs/ca-bundle.trust.crt'`.

## [Requirements](tss_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- python-tss-sdk - <https://pypi.org/project/python-tss-sdk/>

## [Terms](tss_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  integer / required | The integer ID of the secret. |

## [Keyword parameters](tss_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.tss', key1=value1, key2=value2, ...)` and `query('community.general.tss', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **api_path_uri**  string | The path to append to the base URL to form a valid REST API request.  Default: `"/api/v1"`  Configuration:   - Environment variable: [`TSS_API_PATH_URI`](../../environment_variables.md#envvar-TSS_API_PATH_URI) |
| **base_url**  string / required | The base URL of the server, e.g. `https://localhost/SecretServer`.  Configuration:   - INI entry:  ```YAML+Jinja   [tss_lookup]   base_url = VALUE   ``` - Environment variable: [`TSS_BASE_URL`](../../environment_variables.md#envvar-TSS_BASE_URL) |
| **domain**  string  added in community.general 3.6.0 | The domain with which to request the OAuth2 Access Grant.  Optional when *token* is not provided.  Requires `python-tss-sdk` version 1.0.0 or greater.  Default: `""`  Configuration:   - INI entry:  ```YAML+Jinja   [tss_lookup]   domain = ""   ``` - Environment variable: [`TSS_DOMAIN`](../../environment_variables.md#envvar-TSS_DOMAIN) |
| **password**  string | The password associated with the supplied username.  Required when *token* is not provided.  Configuration:   - INI entry:  ```YAML+Jinja   [tss_lookup]   password = VALUE   ``` - Environment variable: [`TSS_PASSWORD`](../../environment_variables.md#envvar-TSS_PASSWORD) |
| **token**  string  added in community.general 3.7.0 | Existing token for Thycotic authorizer.  If provided, *username* and *password* are not needed.  Requires `python-tss-sdk` version 1.0.0 or greater.  Configuration:   - INI entry:  ```YAML+Jinja   [tss_lookup]   token = VALUE   ``` - Environment variable: [`TSS_TOKEN`](../../environment_variables.md#envvar-TSS_TOKEN) |
| **token_path_uri**  string | The path to append to the base URL to form a valid OAuth2 Access Grant request.  Default: `"/oauth2/token"`  Configuration:   - Environment variable: [`TSS_TOKEN_PATH_URI`](../../environment_variables.md#envvar-TSS_TOKEN_PATH_URI) |
| **username**  string | The username with which to request the OAuth2 Access Grant.  Configuration:   - INI entry:  ```YAML+Jinja   [tss_lookup]   username = VALUE   ``` - Environment variable: [`TSS_USERNAME`](../../environment_variables.md#envvar-TSS_USERNAME) |

## [Notes](tss_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.tss', term1, term2, key1=value1, key2=value2)` and `query('community.general.tss', term1, term2, key1=value1, key2=value2)`

## [Examples](tss_lookup.md#id6)

```yaml+jinja
- hosts: localhost
  vars:
      secret: >-
        {{
            lookup(
                'community.general.tss',
                102,
                base_url='https://secretserver.domain.com/SecretServer/',
                username='user.name',
                password='password'
            )
        }}
  tasks:
      - ansible.builtin.debug:
          msg: >
            the password is {{
              (secret['items']
                | items2dict(key_name='slug',
                             value_name='itemValue'))['password']
            }}

- hosts: localhost
  vars:
      secret: >-
        {{
            lookup(
                'community.general.tss',
                102,
                base_url='https://secretserver.domain.com/SecretServer/',
                username='user.name',
                password='password',
                domain='domain'
            )
        }}
  tasks:
      - ansible.builtin.debug:
          msg: >
            the password is {{
              (secret['items']
                | items2dict(key_name='slug',
                             value_name='itemValue'))['password']
            }}

- hosts: localhost
  vars:
      secret_password: >-
        {{
            ((lookup(
                'community.general.tss',
                102,
                base_url='https://secretserver.domain.com/SecretServer/',
                token='thycotic_access_token',
            )  | from_json).get('items') | items2dict(key_name='slug', value_name='itemValue'))['password']
        }}
  tasks:
      - ansible.builtin.debug:
          msg: the password is {{ secret_password }}
```

## [Return Value](tss_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The JSON responses to `GET /secrets/{id}`.  See [https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#operation–secrets–id–get](https://updates.thycotic.net/secretserver/restapiguide/TokenAuth/#operation--secrets--id--get).  Returned: success |

### Authors

- Adam Migus (@amigus)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
