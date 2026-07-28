---
collection: ansible
version: "8"
title: "Filter guide"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/hashi_vault/docsite/filter_guide.html
fetched_at: 2026-07-28T01:53:21+00:00
---
# [Filter guide](filter_guide.md#id1)

> **Note:**
>
> Filter Plugins are now included with other [plugin documentation](../index.md#plugins-in-community-hashi-vault).

Filters

- [Filter guide](filter_guide.md#filter-guide)

  - [`vault_login_token` filter](filter_guide.md#vault-login-token-filter)

## [`vault_login_token` filter](filter_guide.md#id2)

New in version 2.2.0.

The `vault_login_token` filter extracts the token value from the structure returned by a Vault token creation operation, such as those returned by the `community.hashi_vault.vault_login` [module](../vault_login_module.md#ansible-collections-community-hashi-vault-vault-login-module) or [lookup plugin](../vault_login_lookup.md#ansible-collections-community-hashi-vault-vault-login-lookup), or the `community.hashi_vault.vault_token_create` [module](../vault_token_create_module.md#ansible-collections-community-hashi-vault-vault-token-create-module) or [lookup plugin](../vault_token_create_lookup.md#ansible-collections-community-hashi-vault-vault-token-create-lookup).

The filter takes an optional parameter `optional_field` with defaults to `login`. If this field exists in the input dictionary, then the value of that field is taken the be the login response, rather than the input dictionary itself.

The purpose of this is primarily to deal with the difference between the output of lookup plugins (which return the login response directly) and modules, which return the login response in a `login` field in its return.

Here is a sample login response:

```json
{
    "auth": {
        "accessor": "mQewzgKRx5Yui1h1eMemJlMu",
        "client_token": "s.drgLxu6ZtttSVn5Zkoy0huMR",
        "entity_id": "8a74ffd3-f71b-8ebe-7942-610428051ea9",
        "lease_duration": 3600,
        "metadata": {
            "username": "testuser"
        },
        "orphan": true,
        "policies": [
            "alt-policy",
            "default",
            "userpass-policy"
        ],
        "renewable": true,
        "token_policies": [
            "alt-policy",
            "default",
            "userpass-policy"
        ],
        "token_type": "service"
    },
    "data": null,
    "lease_duration": 0,
    "lease_id": "",
    "renewable": false,
    "request_id": "511e8fba-83f0-4b7e-95ea-770aa19c1957",
    "warnings": null,
    "wrap_info": null
}
```

The token that we want to extract is in `auth.client_token`.

Here’s an example usage with the `vault_login` module and lookup.

```yaml+jinja
- name: Set defaults
  vars:
    ansible_hashi_vault_url: https://vault:9801/
    ansible_hashi_vault_auth_method: userpass
    ansible_hashi_vault_username: user
    ansible_hashi_vault_password: "{{ lookup('env', 'MY_SECRET_PASSWORD') }}"
  module_defaults:
    community.hashi_vault.vault_login:
      url: '{{ ansible_hashi_vault_url }}'
      auth_method: '{{ ansible_hashi_vault_auth_method }}'
      username: '{{ ansible_hashi_vault_username }}'
      password: '{{ ansible_hashi_vault_password }}'
  block:
    - name: Perform a login with a lookup and display the token
      vars:
        login_response: "{{ lookup('community.hashi_vault.vault_login') }}"
      debug:
        msg: "The token is {{ login_response | community.hashi_vault.vault_login_token }}"

    - name: Perform a login with a module
      community.hashi_vault.vault_login:
      register: login_response

    - name: Display the token
      debug:
        msg: "The token is {{ login_response | community.hashi_vault.vault_login_token }}"
```

Which produces:

```ansible-output
TASK [Perform a login with a lookup and display the token]  ********************************
ok: [localhost] => {
    "msg": "s.drgLxu6ZtttSVn5Zkoy0huMR"
}

TASK [Perform a login with a module]  *****************************************************
ok: [localhost] => {"changed": true, "login": {"auth": { "accessor": "mQewzgKRx5Yui1h1eMemJlMu",
"client_token": "s.drgLxu6ZtttSVn5Zkoy0huMR", "entity_id": "8a74ffd3-f71b-8ebe-7942-610428051ea9",
"lease_duration": 3600, "metadata": {"username": "testuser"}, "orphan": true, "policies":
["alt-policy", "default", "userpass-policy"], "renewable": true, "token_policies": ["alt-policy",
"default", "userpass-policy"], "token_type": "service"}, "data": null, "lease_duration": 0,
"lease_id": "", "renewable": false, "request_id": "511e8fba-83f0-4b7e-95ea-770aa19c1957",
"warnings": null, "wrap_info": null}}
}

TASK [Display the token]  *****************************************************************
ok: [localhost] => {
    "msg": "s.drgLxu6ZtttSVn5Zkoy0huMR"
}
```

This filter is the equivalent of reading into the dictionary directly, but it has the advantages of providing semantic meaning and automatically working against the differing output of modules and lookups.

```yaml+jinja
---
lookup_token: "{{ lookup_login_response['auth']['client_token'] }}"
module_token: "{{ module_login_response['login']['auth']['client_token'] }}"
```

The `optional_field` can be changed in case you’ve put the raw login response in some other structure, but you could also dereference that directly instead.

```yaml+jinja
---
my_data:
  something: somedata
  vault_login: "{{ lookup_login_response }}"

token_from_param: "{{ my_data | community.hashi_vault.vault_login_token(optional_field='vault_login') }}"
token_from_deref: "{{ my_data['vault_login'] | community.hashi_vault.vault_login_token }}"
# if the optional field doesn't exist, the dictionary itself is still checked
unused_optional: "{{ my_data['vault_login'] | community.hashi_vault.vault_login_token(optional_field='missing') }}"
```
