---
collection: ansible
version: "6"
title: "community.general.rundeck_acl_policy module – Manage Rundeck ACL policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/rundeck_acl_policy_module.html
fetched_at: 2026-07-27T17:12:48+00:00
---
# community.general.rundeck_acl_policy module – Manage Rundeck ACL policies

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
> To use it in a playbook, specify: `community.general.rundeck_acl_policy`.

- [Synopsis](rundeck_acl_policy_module.md#synopsis)
- [Parameters](rundeck_acl_policy_module.md#parameters)
- [Examples](rundeck_acl_policy_module.md#examples)
- [Return Values](rundeck_acl_policy_module.md#return-values)

## [Synopsis](rundeck_acl_policy_module.md#id1)

- Create, update and remove Rundeck ACL policies through HTTP API.

## [Parameters](rundeck_acl_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_version**  integer | Sets the API version used by module.  API version must be at least 14.  Default: `14` |
| **client_cert**  path  added in community.general 0.2.0 | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, `client_key` is not required. |
| **client_key**  path  added in community.general 0.2.0 | PEM formatted file that contains your private key to be used for SSL client authentication.  If `client_cert` contains both the certificate and key, this option is not required. |
| **force**  boolean  added in community.general 0.2.0 | If `yes` do not get a cached copy.  Choices:   - `false` ← (default) - `true` |
| **force_basic_auth**  boolean  added in community.general 0.2.0 | Credentials specified with *url_username* and *url_password* should be passed in HTTP Header.  Choices:   - `false` ← (default) - `true` |
| **http_agent**  string  added in community.general 0.2.0 | Header to identify as, generally appears in web server logs.  Default: `"ansible-httpget"` |
| **name**  string / required | Sets the project name. |
| **policy**  string | Sets the ACL policy content.  ACL policy content is a YAML object as described in <http://rundeck.org/docs/man5/aclpolicy.html>.  It can be a YAML string or a pure Ansible inventory YAML object. |
| **project**  string | Sets the project which receive the ACL policy.  If unset, it’s a system ACL policy. |
| **state**  string | Create or remove Rundeck project.  Choices:   - `"present"` ← (default) - `"absent"` |
| **token**  string / required | Sets the token to authenticate against Rundeck API. |
| **url**  string / required | Sets the rundeck instance URL. |
| **url_password**  string  added in community.general 0.2.0 | The password for use in HTTP basic authentication.  If the *url_username* parameter is not specified, the *url_password* parameter will not be used. |
| **url_username**  string  added in community.general 0.2.0 | The username for use in HTTP basic authentication.  This parameter can be used without *url_password* for sites that allow empty passwords |
| **use_gssapi**  boolean  added in ansible-core 2.11 | Use GSSAPI to perform the authentication, typically this is for Kerberos or Kerberos through Negotiate authentication.  Requires the Python library [gssapi](https://github.com/pythongssapi/python-gssapi) to be installed.  Credentials for GSSAPI can be specified with *url_username*/*url_password* or with the GSSAPI env var `KRB5CCNAME` that specified a custom Kerberos credential cache.  NTLM authentication is `not` supported even if the GSSAPI mech for NTLM has been installed.  Choices:   - `false` ← (default) - `true` |
| **use_proxy**  boolean  added in community.general 0.2.0 | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean  added in community.general 0.2.0 | If `no`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](rundeck_acl_policy_module.md#id3)

```yaml+jinja
- name: Create or update a rundeck ACL policy in project Ansible
  community.general.rundeck_acl_policy:
    name: "Project_01"
    api_version: 18
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: present
    project: "Ansible"
    policy:
      description: "my policy"
      context:
        application: rundeck
      for:
        project:
          - allow: read
      by:
        group: "build"

- name: Remove a rundeck system policy
  community.general.rundeck_acl_policy:
    name: "Project_02"
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: absent
```

## [Return Values](rundeck_acl_policy_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | Dictionary containing ACL policy informations after modification.  Returned: success |
| **before**  dictionary | Dictionary containing ACL policy informations before modification.  Returned: success |
| **rundeck_response**  string | Rundeck response when a failure occurs.  Returned: failed |

### Authors

- Loic Blot (@nerzhul)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
