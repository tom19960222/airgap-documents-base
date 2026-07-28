---
collection: ansible
version: "6"
title: "community.okd.openshift_auth module – Authenticate to OpenShift clusters which require an explicit login step"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/okd/openshift_auth_module.html
fetched_at: 2026-07-27T17:20:11+00:00
---
# community.okd.openshift_auth module – Authenticate to OpenShift clusters which require an explicit login step

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
> see [Requirements](openshift_auth_module.md#ansible-collections-community-okd-openshift-auth-module-requirements) for details.
>
> To use it in a playbook, specify: `community.okd.openshift_auth`.

New in community.okd 0.2.0

- [Synopsis](openshift_auth_module.md#synopsis)
- [Requirements](openshift_auth_module.md#requirements)
- [Parameters](openshift_auth_module.md#parameters)
- [Examples](openshift_auth_module.md#examples)
- [Return Values](openshift_auth_module.md#return-values)

## [Synopsis](openshift_auth_module.md#id1)

- This module handles authenticating to OpenShift clusters requiring *explicit* authentication procedures, meaning ones where a client logs in (obtains an authentication token), performs API operations using said token and then logs out (revokes the token).
- On the other hand a popular configuration for username+password authentication is one utilizing HTTP Basic Auth, which does not involve any additional login/logout steps (instead login credentials can be attached to each and every API call performed) and as such is handled directly by the `k8s` module (and other resource–specific modules) by utilizing the `host`, `username` and `password` parameters. Please consult your preferred module’s documentation for more details.

## [Requirements](openshift_auth_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.6
- urllib3
- requests
- requests-oauthlib

## [Parameters](openshift_auth_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | When `state` is set to *absent*, this specifies the token to revoke. |
| **ca_cert**  aliases: ssl_ca_cert  path | Path to a CA certificate file used to verify connection to the API server. The full certificate chain must be provided to avoid certificate validation errors. |
| **host**  string / required | Provide a URL for accessing the API server. |
| **password**  string | Provide a password for authenticating with the API server. |
| **state**  string | If set to *present* connect to the API server using the URL specified in `host` and attempt to log in.  If set to *absent* attempt to log out by revoking the authentication token specified in `api_key`.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string | Provide a username for authenticating with the API server. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether or not to verify the API server’s SSL certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](openshift_auth_module.md#id4)

```yaml+jinja
- hosts: localhost
  module_defaults:
    group/k8s:
      host: https://k8s.example.com/
      ca_cert: ca.pem
  tasks:
  - block:
    # It's good practice to store login credentials in a secure vault and not
    # directly in playbooks.
    - include_vars: openshift_passwords.yml

    - name: Log in (obtain access token)
      community.okd.openshift_auth:
        username: admin
        password: "{{ openshift_admin_password }}"
      register: openshift_auth_results

    # Previous task provides the token/api_key, while all other parameters
    # are taken from module_defaults
    - name: Get a list of all pods from any namespace
      kubernetes.core.k8s_info:
        api_key: "{{ openshift_auth_results.openshift_auth.api_key }}"
        kind: Pod
      register: pod_list

    always:
    - name: If login succeeded, try to log out (revoke access token)
      when: openshift_auth_results.openshift_auth.api_key is defined
      community.okd.openshift_auth:
        state: absent
        api_key: "{{ openshift_auth_results.openshift_auth.api_key }}"
```

## [Return Values](openshift_auth_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **k8s_auth**  complex | Same as returned openshift_auth. Kept only for backwards compatibility  Returned: success |
| **api_key**  string | Authentication token.  Returned: success |
| **ca_cert**  string | Path to a CA certificate file used to verify connection to the API server.  Returned: success |
| **host**  string | URL for accessing the API server.  Returned: success |
| **username**  string | Username for authenticating with the API server.  Returned: success |
| **validate_certs**  boolean | Whether or not to verify the API server’s SSL certificates.  Returned: success |
| **openshift_auth**  complex | OpenShift authentication facts.  Returned: success |
| **api_key**  string | Authentication token.  Returned: success |
| **ca_cert**  string | Path to a CA certificate file used to verify connection to the API server.  Returned: success |
| **host**  string | URL for accessing the API server.  Returned: success |
| **username**  string | Username for authenticating with the API server.  Returned: success |
| **validate_certs**  boolean | Whether or not to verify the API server’s SSL certificates.  Returned: success |

### Authors

- KubeVirt Team (@kubevirt)
- Fabian von Feilitzsch (@fabianvf)

### Collection links

[Issue Tracker](https://github.com/openshift/community.okd/issues)
[Repository (Sources)](https://github.com/openshift/community.okd)
